<template>
  <a-row id="globalHeader" class="grid-demo" align="center" :wrap="false">
    <a-col flex="100px">
      <div
        :style="{ padding: 0, marginRight: '38px' }"
        @click="handleIconClick"
      >
        <div class="titleBar">
          <img class="icon" src="../assets/logo2.png" />
          <div class="title">QA系统</div>
        </div>
      </div>
    </a-col>
    <a-col flex="auto">
      <div>
        <a-menu
          mode="horizontal"
          :selected-keys="selectedKeys"
          @menu-item-click="doMenuClick"
        >
          <a-menu-item v-for="item in visibleRoutes" :key="item.path">{{
            item.name
          }}</a-menu-item>
          <!-- 从routes中获取path的值和name值并且显示 -->
        </a-menu>
      </div>
    </a-col>
    <a-col flex="100px">
      <div class="contact">
        <a href="http://www.nighterdream.cn">联系我们</a>
      </div>
    </a-col>
    <a-col flex="100px">
      <div>{{ store.state.user?.loginUser?.userName ?? "未登录" }}</div>
    </a-col>
  </a-row>
</template>

<script setup lang="ts">
import { routes } from "../router/routes";
import { useRouter } from "vue-router";
import { computed, ref } from "vue";
import { useStore } from "vuex";
import checkAccess from "@/access/checkAccess";
import { ACCESS_ENUM } from "@/access/accessEnum";

const store = useStore();
const router = useRouter();

//展示在菜单的路由,权限管理
const visibleRoutes = computed(() => {
  return routes.filter((item, index) => {
    if (item.meta?.hideInMenu) {
      return false;
    }
    //根据用户权限过滤菜单
    if (!checkAccess(store.state.user.loginUser, item.meta?.access as string)) {
      return false;
    }
    return true;
  });
});

//默认主页
const selectedKeys = ref(["/"]);

//路由跳转后，更新选中的菜单项
router.afterEach((to) => {
  selectedKeys.value = [to.path];
});
// router.afterEach 是一个 Vue Router 钩子函数，它在每次路由导航完成后执行，
// 并调用回调函数来更新 selectedKeys，以确保页面中显示的菜单项正确反映当前路由的选中状态。
const doMenuClick = (key: string) => {
  router.push({
    path: key,
  });
};
// 通过menu-item-click获取key值就是item对应的name值之后调用并传递给doMenuClick
// 之后通过router.push实现页面的跳转

//处理点击icon的函数，点击icon后跳转到/路径
const handleIconClick = () => {
  router.push("/");
};

//获取用户登录信息模块

// console.log(store.state.user.loginUser);

//测试状态更新
// setTimeout(() => {
//   store.dispatch("user/getLoginUser", {
//     userName: "roger",
//     userRole: ACCESS_ENUM.ADMIN,
//   });
// }, 3000);
</script>

<style scoped>
.titleBar {
  display: flex;
  align-items: center;
}

.titleBar .title {
  flex-grow: 1; /* 让 .title 元素横向填充整个可用空间 */
}

.icon {
  height: 50px;
}

.title {
  color: #444;
  margin-left: 16px;
}

.contact a {
  text-decoration: none; /* 取消下划线 */
  color: black; /* 修改字体颜色为黑色 */
}
</style>
