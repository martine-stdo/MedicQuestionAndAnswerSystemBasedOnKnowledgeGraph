<template>
  <div class="data-view">
    <div ref="barChart" class="chart"></div>
    <div ref="pieChart" class="chart"></div>
  </div>
</template>

<script>
import * as echarts from "echarts";

export default {
  data() {
    return {
      departmentData: {
        儿科: 3277,
        内分泌科: 2050,
        口腔科: 840,
        呼吸内科: 1262,
        妇产科: 2584,
        影像检验科: 9,
        心胸外科: 476,
        心血管内科: 1401,
        性病科: 28,
        普外科: 888,
        普通内科: 807,
        泌尿外科: 910,
        消化内科: 1839,
        甲状腺乳腺外科: 400,
        "疼痛科 麻醉科": 113,
        皮肤科: 2675,
        眼科: 1054,
        神经内科: 2425,
        神经外科: 459,
        精神心理科: 894,
        美容整形科: 154,
        耳鼻咽喉科: 1021,
        肝胆胰腺外科: 502,
        肾脏内科: 883,
        肿瘤科: 567,
        血液科: 831,
        风湿免疫科: 617,
        骨科: 2815,
      },
      tooltipText: "",
    };
  },
  mounted() {
    this.renderBarChart();
    this.renderPieChart();
  },
  methods: {
    renderBarChart() {
      const chartDom = this.$refs.barChart;
      const myChart = echarts.init(chartDom);
      const departmentNames = Object.keys(this.departmentData);
      const departmentCounts = Object.values(this.departmentData);

      const option = {
        title: {
          text: "各部门问答数目（柱状图）",
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        xAxis: {
          type: "category",
          data: departmentNames,
        },
        yAxis: {
          type: "value",
        },
        series: [
          {
            data: departmentCounts,
            type: "bar",
          },
        ],
      };

      myChart.setOption(option);

      // 添加点击事件
      myChart.on("click", (params) => {
        const selectedDepartment = params.name;
        const count = this.departmentData[selectedDepartment];
        this.tooltipText = `${selectedDepartment}：${count}个问答`;
      });
    },
    renderPieChart() {
      const chartDom = this.$refs.pieChart;
      const myChart = echarts.init(chartDom);
      const departmentNames = Object.keys(this.departmentData);
      const departmentCounts = Object.values(this.departmentData);

      if (departmentNames.length > 0) {
        const option = {
          title: {
            text: "各部门问答数目（饼图）",
            left: "center",
          },
          tooltip: {
            trigger: "item",
            formatter: "{a} <br/>{b}: {c} ({d}%)",
          },
          legend: {
            orient: "vertical",
            left: 30,
            top: 40,
            data: departmentNames,
          },
          series: [
            {
              name: "问答数目",
              type: "pie",
              radius: ["50%", "70%"],
              center: ["70%", "50%"], // 调整饼图的中心位置
              avoidLabelOverlap: false,
              label: {
                show: false,
                position: "center",
              },
              emphasis: {
                label: {
                  show: true,
                  fontSize: "14",
                  fontWeight: "bold",
                },
              },
              labelLine: {
                show: false,
              },
              data: departmentNames.map((name, index) => ({
                name,
                value: departmentCounts[index],
              })),
            },
          ],
        };

        myChart.setOption(option);
      }
    },
  },
};
</script>

<style scoped>
.data-view {
  display: flex;
  /* 使用 flexbox 布局 */
  justify-content: space-around;
  /* 子元素水平分布 */
  margin-left: auto;
  margin-right: auto;
  margin-top: 49px;
  width: 95%;
  height: 510px;
  border: none;
  background: #eeeeee;
  opacity: 0.95;
  border-radius: 15px;
}

.chart {
  margin-top: 40px;
  width: 45%;
  height: 400px;
}

.tooltip {
  position: absolute;
  top: 10px;
  right: 10px;
  padding: 10px;
  background-color: rgba(255, 255, 255, 0.8);
  border: 1px solid #ccc;
  border-radius: 5px;
}
</style>
