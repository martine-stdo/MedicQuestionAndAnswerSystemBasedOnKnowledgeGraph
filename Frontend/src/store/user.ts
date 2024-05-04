// 引入 Vuex 中的 StoreOptions 类型
import { ACCESS_ENUM } from "@/access/accessEnum";
import { StoreOptions } from "vuex";
import axios from "axios";

// 导出 Vuex store 的配置对象
export default {
  // 命名空间，使得模块化 Vuex store 更容易管理
  namespaced: true,

  // 定义 Vuex store 的初始状态
  state: () => ({
    loginUser: {
      userName: "未登录",
      userAvatar_url: "",
      userRole: ACCESS_ENUM.NOT_LOGIN,
    },
  }),

  // 定义异步操作，可通过提交 mutations 来修改状态
  actions: {
    // 异步操作，获取登录用户信息
    // 参数包括 commit 方法用于提交 mutations，state
    async getLoginUser({ commit, state }, { userAccount, userPassword }) {
      // 从远程获取登录信息
      try {
        // 发送登录请求
        const loginResponse = await axios.post(
          "http://localhost:8000/user/login/",
          {
            userAccount: userAccount,
            userPassword: userPassword,
          }
        );
        if (loginResponse.data.code === 0) {
          // 登录成功，直接使用登录接口的响应更新用户信息
          const updatedUser = {
            userName: loginResponse.data.user.username,
            userAvatar_url: loginResponse.data.user.avatar_url,
            userRole: loginResponse.data.user.user_role,
          };
          commit("updateUser", updatedUser); // 更新用户信息

          // 保存 token 到浏览器中
          localStorage.setItem("token", loginResponse.data.token);
        } else {
          // 更新用户信息为未登录状态
          commit("updateUser", {
            ...state.loginUser,
            userRole: ACCESS_ENUM.NOT_LOGIN,
          });
        }
      } catch (error) {
        console.error("获取登录用户信息出错:");
        // 更新用户信息为未登录状态
        commit("updateUser", {
          ...state.loginUser,
          userRole: ACCESS_ENUM.NOT_LOGIN,
        });
      }
    },
  },
  // 定义同步操作，通过直接修改状态来实现
  mutations: {
    // 更新用户信息的 mutations
    // 参数包括当前状态对象 state 和负载数据 payload
    updateUser(state, payload) {
      // 更新用户信息
      state.loginUser = payload;
    },
  },
} as StoreOptions<any>;
