// 引入 Vuex 中的 createStore 方法
import { createStore } from "vuex";

// 引入名为 "user" 的模块
import user from "./user";

// 创建 Vuex store 实例
export default createStore({
  // 根模块中的 mutations（用于同步修改状态）
  mutations: {},

  // 根模块中的 actions（用于包含异步逻辑的操作）
  actions: {},

  // 根模块中的 modules（用于引入其他模块，这里引入了名为 "user" 的模块）
  modules: {
    user, // 将名为 "user" 的模块添加到根模块中
  },
});
