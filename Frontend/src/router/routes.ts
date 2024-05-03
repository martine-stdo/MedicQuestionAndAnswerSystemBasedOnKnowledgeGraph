import { RouteRecordRaw } from "vue-router";
import AdminView from "@/views/AdminView.vue";
import NoAuthView from "@/views/NoAuthView.vue";
import { ACCESS_ENUM } from "@/access/accessEnum";
import LoginView from "@/views/user/LoginView.vue";
import RegisterView from "@/views/user/RegisterView.vue";
import UserLayout from "@/layouts/UserLayout.vue";
import ExampleView from "@/views/ExampleView.vue";
import ChatBotView from "@/views/ChatBotView.vue";
import DataView from "@/views/DataView.vue";
import KnowledgeGraphView from "@/views/KnowledgeGraphView.vue";

export const routes: Array<RouteRecordRaw> = [
  {
    path: "/user",
    name: "用户",
    component: UserLayout,
    children: [
      {
        path: "/user/login",
        name: "用户登录",
        component: LoginView,
      },

      {
        path: "/user/register",
        name: "用户注册",
        component: RegisterView,
      },
    ],
    meta: {
      hideInMenu: true,
    },
  },

  {
    path: "/",
    name: "知识图谱",
    component: KnowledgeGraphView,
  },
  {
    path: "/chat",
    name: "智慧问答",
    component: ChatBotView,
  },
  {
    path: "/datas",
    name: "数据展示",
    component: DataView,
  },
  {
    path: "/about",
    name: "关于我们",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/admin",
    name: "管理员可见",
    component: AdminView,
    meta: {
      access: ACCESS_ENUM.ADMIN,
    },
  },
  //给路由增加个属性控制显示还是隐藏
  {
    path: "/hide",
    name: "隐藏页面",
    component: ExampleView,
    meta: {
      hideInMenu: true,
    },
  },

  {
    path: "/noAuth",
    name: "无权限",
    component: NoAuthView,
    meta: {
      hideInMenu: true,
    },
  },
];
