// 引入Vue Router实例和Vuex实例
import router from "@/router";
import store from "@/store";
import { ACCESS_ENUM } from "./accessEnum";
import checkAccess from "./checkAccess";

// 全局导航守卫，用于在每次路由切换前进行权限检查和用户信息获取
router.beforeEach(async (to, from, next) => {
  // 打印登录用户信息，用于调试
  console.log("登录用户信息", store.state.user.loginUser);

  // 从状态管理中获取登录用户信息
  const loginUser = store.state.user.loginUser;

  //   // 如果之前未登录，自动登录
  //   if (!loginUser || !loginUser.userRole) {
  //     // 加 await 是为了等用户登录成功之后，再执行后续的代码
  //     await store.dispatch("user/getLoginUser");
  //   }

  // 获取需要访问的页面所需的权限，默认为 NOT_LOGIN
  const needAccess = (to.meta?.access as string) ?? ACCESS_ENUM.NOT_LOGIN;

  // 要跳转的页面需要登录
  if (needAccess !== ACCESS_ENUM.NOT_LOGIN) {
    // 如果未登录，跳转到登录页面
    if (!loginUser || !loginUser.userRole) {
      next(`/user/login?redirect=${to.fullPath}`);
      return;
    }

    // 如果已登录，但权限不足，跳转到无权限页面
    if (!checkAccess(loginUser, needAccess)) {
      next("/noAuth");
      return;
    }
  }

  // 允许导航继续
  next();
});
