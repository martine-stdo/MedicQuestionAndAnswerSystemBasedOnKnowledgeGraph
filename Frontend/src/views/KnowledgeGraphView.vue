<template>
  <div>
    <div class="toolBar">
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
    </div>

    <!-- 节点图容器 -->
    <div id="mynetwork"></div>
    <div
      id="info-box"
      style="
        display: none;
        position: absolute;
        background-color: white;
        padding: 5px;
        border: none;
        border-radius: 5px;
        opacity: 0.8;
      "
    >
      <p id="info-text"></p>
    </div>
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
    const departments = [
      "儿科",
      "内分泌科",
      "口腔科",
      "呼吸内科",
      "妇产科",
      "影像检验科",
      "心胸外科",
      "心血管内科",
      "性病科",
      "普外科",
      "普通内科",
      "泌尿外科",
      "消化内科",
      "甲状腺乳腺外科",
      "疼痛科 麻醉科",
      "皮肤科",
      "眼科",
      "神经内科",
      "神经外科",
      "精神心理科",
      "美容整形科",
      "耳鼻咽喉科",
      "肝胆胰腺外科",
      "肾脏内科",
      "肿瘤科",
      "血液科",
      "风湿免疫科",
      "骨科",
    ]; // 可选部门列表
    const network = ref(null); // 节点图实例
    const selectedQuestion = ref(null); // 当前选中的问题节点
    const selectedAnswer = ref(null); // 当前选中的答案节点
    let nodesMap = {}; // 存储节点信息的映射
    let doubleClickAnswerNodes = [];
    // 初始化副本答案节点
    let copiedAnswerNode = null;

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
        // 清空doubleClickAnswerNodes

        doubleClickAnswerNodes = [];
        // 清空副本答案
        copiedAnswerNode = null;
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
      const options = {
        nodes: {
          shape: "dot",
          size: 20,
          font: {
            size: 14,
            color: "#2a1616", // 更改字体颜色为白色
          },
          borderWidth: 2,
          color: {
            border: "#8fd3e9", // 更改边框颜色为深灰色
            background: "#a4dbfd", // 更改背景颜色为科技绿色
            highlight: {
              border: "#999999", // 更改高亮边框颜色为浅灰色
              background: "#A5F", // 更改高亮背景颜色为科技紫色
            },
          },
        },

        edges: {
          width: 2,
          color: {
            color: "#91c2fd", // 更改边颜色为浅灰色
            highlight: "#e683ad", // 更改高亮边颜色为科技紫色
          },
          arrows: {
            to: {
              enabled: true,
              scaleFactor: 0.5,
            },
          },
        },
        physics: {
          stabilization: {
            enabled: true,
            iterations: 1000,
            updateInterval: 100,
            onlyDynamicEdges: false,
            fit: true,
          },
          barnesHut: {
            gravitationalConstant: -2000,
            centralGravity: 0.3,
            springLength: 95,
            springConstant: 0.04,
            damping: 0.15, // 将damping值从0.09提高到0.15
            avoidOverlap: 0.1,
          },
        },
      };
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
    // 修改 renderAnswerNodeAndEdges 函数
    const renderAnswerNodeAndEdges = (questionNode, answerNode) => {
      if (questionNode && answerNode) {
        // 将answer节点加入doubleClickAnswerNodes
        doubleClickAnswerNodes.push(answerNode);
        // 添加 Answer 节点到 DataSet 中
        network.value.body.data.nodes.add({
          id: answerNode.id,
          label: answerNode.label,
        });

        console.log(doubleClickAnswerNodes);
        // 添加边连接 Answer 节点和对应的 Question 节点
        network.value.body.data.edges.add({
          from: questionNode.id,
          to: answerNode.id,
          label: "reply",
        });

        // 添加单击事件监听器到答案节点上
        network.value.on("click", (params) => {
          // 如果单击的是答案节点
          if (params.nodes.length === 1) {
            const nodeId = params.nodes[0];
            // 假设在遍历结束后未找到匹配的节点的标志为 foundMatchedNode
            let foundMatchedNode = false;
            doubleClickAnswerNodes.forEach((node) => {
              if (node.id === nodeId) {
                // 找到匹配的答案节点，进行复制
                copiedAnswerNode = { ...node };
                foundMatchedNode = true;
                showInfoBox(params, copiedAnswerNode);
              }
            });
            if (!foundMatchedNode) {
              hideInfoBox();
            }
          } else {
            // 点击空白处也隐藏
            hideInfoBox();
          }
        });
      }
    };

    // 显示文本框
    const showInfoBox = (params, copiedAnswerNode) => {
      const infoBox = document.getElementById("info-box");
      const infoText = document.getElementById("info-text");

      // 计算文本框位置
      const canvasPos = network.value.canvasToDOM({
        x: params.pointer.canvas.x,
        y: params.pointer.canvas.y,
      });
      infoBox.style.left = `${canvasPos.x}px`;
      infoBox.style.top = `${canvasPos.y}px`;

      // 显示文本框
      console.log(copiedAnswerNode);
      const answerText = copiedAnswerNode.properties.A;
      infoText.innerHTML = answerText.trim();
      infoBox.style.display = "block";
    };

    // 隐藏文本框
    const hideInfoBox = () => {
      const infoBox = document.getElementById("info-box");
      infoBox.style.display = "none";
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
  margin-left: auto;
  margin-right: auto;
  margin-top: 10px;
  width: 95%;
  height: 510px;
  border: none;
  background: #eeeeee;
  opacity: 0.8;
  border-radius: 15px;
}

/* 选择部门模块样式 */
select {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #f9f9f9;
  font-size: 16px;
  margin-right: 10px; /* 可根据需要调整间距 */
}

/* 输入框样式 */
input[type="number"] {
  padding: 8px;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 16px;
  width: 100px; /* 可根据需要调整宽度 */
  margin-right: 10px; /* 可根据需要调整间距 */
  margin-left: 10px;
}

/* 加载模块按钮样式 */
button {
  padding: 10px 20px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
}

/* 鼠标悬停时按钮样式 */
button:hover {
  background-color: #0056b3;
}

.toolBar {
  display: flex;
  justify-content: flex-end; /* 将内容向右对齐 */
  margin-right: 50px;
}
</style>
