import { createApp } from "vue";
import App from "./App.vue";
import ArcoVue from "@arco-design/web-vue";
import "@arco-design/web-vue/dist/arco.css";
import router from "./router";
import store from "./store";
import "@/access";
import "/src/plugins/axios";
import "bytemd/dist/index.css";

createApp(App).use(store).use(ArcoVue).use(router).mount("#app");
