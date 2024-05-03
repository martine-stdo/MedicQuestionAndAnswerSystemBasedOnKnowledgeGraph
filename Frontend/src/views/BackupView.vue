<template>
  <div>
    <!-- 选择部门模块 -->
    <select v-model="selectedDepartment">
      <option v-for="department in departments" :key="department">
        {{ department }}
      </option>
    </select>
    <!-- 输入框用于设置节点数量限制 -->
    <input type="number" v-model="nodeLimit" />
    <!-- 加载模块按钮 -->
    <button @click="loadModule">加载模块</button>

    <!-- 节点图容器 -->
    <div id="mynetwork"></div>
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import neo4j from "neo4j-driver";
import vis from "vis-network";
import { DataSet } from "vis-data/peer/esm/vis-data";

export default {
  name: "KnowledgeGraphView",
  setup() {
    // 声明响应式变量
    const selectedDepartment = ref("儿科"); // 当前选择的部门
    const nodeLimit = ref(2); // 设置默认节点数量限制为1
    const departments = ["儿科", "内分泌科", "口腔科", "呼吸内科"]; // 可选部门列表
    const network = ref(null); // 节点图实例
    const selectedQuestion = ref(null); // 当前选中的问题节点
    const selectedAnswer = ref(null); // 当前选中的答案节点
    let nodesMap = {}; // 存储节点信息的映射

    // Neo4j 数据库连接配置
    const driver = neo4j.driver(
      "bolt://localhost:7687",
      neo4j.auth.basic("neo4j", "password")
    );
    const session = driver.session();

    // 加载模块的方法
    const loadModule = async () => {
      try {
        // 清空上次的节点图
        clearNetwork();
        nodesMap = {};
        // 查询数据库获取节点和关系数据
        const result = await session.run(
          `MATCH p=(d:Department {title: '${selectedDepartment.value}'})-[:contain]-() RETURN p LIMIT ${nodeLimit.value}`
        );
        const data = parseNeo4jResult(result); // 解析查询结果
        console.log(data);
        renderNetwork(data); // 渲染节点图
      } catch (error) {
        console.error("Neo4j query error:", error);
      }
    };

    // 解析 Neo4j 返回结果的方法
    const parseNeo4jResult = (result) => {
      const edges = [];

      // 遍历查询结果的每个记录
      result.records.forEach((record) => {
        record._fields[0].segments.forEach((segment) => {
          // 提取起始节点
          const startNode = segment.start;
          const startNodeId = startNode.identity.low.toString();
          const startNodeLabel = startNode.labels[0];
          const startNodeProperties = startNode.properties;

          // 提取结束节点
          const endNode = segment.end;
          const endNodeId = endNode.identity.low.toString();
          const endNodeLabel = endNode.labels[0];
          const endNodeProperties = endNode.properties;

          // 提取关系
          const relationship = segment.relationship;
          const relationshipId = relationship.identity.low.toString();
          const relationshipType = relationship.type;
          const relationshipProperties = relationship.properties;

          // 添加节点到节点映射中
          if (!nodesMap[startNodeId]) {
            nodesMap[startNodeId] = {
              id: startNodeId,
              label: startNodeLabel,
              properties: startNodeProperties,
            };
          }

          if (!nodesMap[endNodeId]) {
            nodesMap[endNodeId] = {
              id: endNodeId,
              label: endNodeLabel,
              properties: endNodeProperties,
            };
          }

          // 将边添加到边数组
          edges.push({
            id: relationshipId,
            from: startNodeId,
            to: endNodeId,
            label: relationshipType,
            properties: relationshipProperties,
          });
        });
      });

      // 将节点映射转换为节点数组
      const nodes = Object.values(nodesMap);
      return { nodes, edges };
    };

    // 渲染节点图的方法
    const renderNetwork = (data) => {
      const container = document.getElementById("mynetwork");

      // 创建一个新的 vis DataSet 来存储节点和边
      const nodesDataSet = new DataSet();
      const edgesDataSet = new DataSet();

      // 添加节点到 DataSet 中
      data.nodes.forEach((node) => {
        nodesDataSet.add({
          id: node.id,
          label: node.properties.title || node.properties.Q,
        });
      });

      // 添加边到 DataSet 中
      data.edges.forEach((edge) => {
        edgesDataSet.add({
          id: edge.id,
          from: edge.from,
          to: edge.to,
          label: edge.label,
        });
      });

      // 创建节点图
      const networkData = {
        nodes: nodesDataSet,
        edges: edgesDataSet,
      };
      const options = {};
      network.value = new vis.Network(container, networkData, options);

      // 添加双击事件监听器
      network.value.on("doubleClick", (params) => {
        if (params.nodes.length === 1) {
          const nodeId = params.nodes[0];
          const questionNode = nodesMap[nodeId];
          if (questionNode && questionNode.label === "Question") {
            fetchAnswer(questionNode); // 获取对应问题的答案
          }
        }
      });
    };

    // 获取 Answer 节点并添加到节点图中
    const fetchAnswer = async (questionNode) => {
      try {
        const result = await session.run(
          `MATCH (n)-[:reply]->(m) WHERE id(n) = ${questionNode.id} RETURN m`
        );
        const answerRecord = result.records[0];
        if (answerRecord) {
          // 从 answerRecord 中提取属性值
          const answerId = answerRecord._fields[0].identity.low.toString();
          const answerLabel = answerRecord._fields[0].labels[0];
          const answerProperties = answerRecord._fields[0].properties;

          // 创建 answerNode 对象并赋值
          const answerNode = {
            id: answerId,
            label: answerLabel,
            properties: answerProperties,
          };
          renderAnswerNodeAndEdges(questionNode, answerNode);
        } else {
          console.log("No answer found.");
        }
      } catch (error) {
        console.error("Neo4j query error:", error);
      }
    };

    // 渲染 Answer 节点的方法
    const renderAnswerNodeAndEdges = (questionNode, answerNode) => {
      if (questionNode && answerNode) {
        // 添加 Answer 节点到 DataSet 中
        network.value.body.data.nodes.add({
          id: answerNode.id,
          label: answerNode.properties.A,
        });
        // 添加边连接 Answer 节点和对应的 Question 节点的边
        network.value.body.data.edges.add({
          from: answerNode.id,
          to: questionNode.id,
          label: "reply",
        });
      }
    };

    // 在组件挂载后执行加载模块方法
    onMounted(() => {
      loadModule();
    });

    // 清空节点图的方法
    const clearNetwork = () => {
      if (network.value !== null) {
        network.value.destroy(); // 销毁节点图实例
        network.value = null;
      }
    };

    // 返回响应式变量和方法
    return {
      selectedDepartment,
      nodeLimit,
      departments,
      loadModule,
      selectedQuestion,
      selectedAnswer,
    };
  },
};
</script>

<style>
#mynetwork {
  width: 100%;
  height: 400px;
  border: 1px solid lightgray;
}
</style>
