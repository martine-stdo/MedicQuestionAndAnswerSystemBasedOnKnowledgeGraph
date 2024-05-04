<template>
  <div class="app">
    <template v-if="route.path.startsWith('/user')">
      <router-view></router-view>
    </template>

    <template v-else>
      <BasicLayout></BasicLayout>
    </template>
  </div>
</template>

<style></style>

<script setup lang="ts">
import BasicLayout from "@/layouts/BasicLayout";
import { onMounted } from "vue";
import { useRoute } from "vue-router";
import { ACCESS_ENUM } from "../src/access/accessEnum";

import { useRouter } from "vue-router";
import { useStore } from "vuex";

const route = useRoute();

const router = useRouter();
const store = useStore();

// onMounted(() => {
//   const userAccesss = store.state.loginUser?.userRole ?? ACCESS_ENUM.NOT_LOGIN;
//   if (userAccesss === ACCESS_ENUM.NOT_LOGIN) {
//     router.push("/user/login");
//   }
// });

/**
 * 全局初始化函数，全局单次调用的代码都可以写在这里
 */
const doInit = () => {
  console.log();
};

onMounted(() => {
  doInit();
});

//权限管理

//在公共组件中获取下一个路由信息中是否需要meta.access并且通过
</script>
