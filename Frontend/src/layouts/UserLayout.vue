<template>
  <div id="UserLayout">
    <a-layout style="min-height: 100vh">
      <a-layout-header class="header"></a-layout-header>
      <a-space class="space">
        <img src="../assets/logo2.png" class="logo" />
        <div class="title">OJ 平台</div>
        <div class="slogan">欢迎使用由黑夜梦想家开发的OJ平台</div>
      </a-space>
      <a-layout-content class="content">
        <router-view />
      </a-layout-content>
      <a-layout-footer class="footer">
        <a href="http://www.nighterdream.cn/" class="href">nighterdream</a>
      </a-layout-footer>
    </a-layout>
  </div>
</template>

<style scoped>
#UserLayout .logo {
  width: 64px;
  height: 64px;
}

#UserLayout .space {
  display: flex;
  justify-content: center;
  align-items: center;
}

#UserLayout .title {
  margin-left: 20px;
  font-size: 24px;
  font-weight: bold;
}

#UserLayout .slogan {
  margin-top: 10px;
  font-size: 16px;
  color: #555; /* 设置文字颜色 */
  text-align: center; /* 文字居中对齐 */
}

#UserLayout .header {
  margin-bottom: 10px;
  box-shadow: #eee 1px 1px 5px;
}

@keyframes gradient {
  0% {
    background: linear-gradient(#e66465, #9198e5);
    background-size: 200% 200%;
    background-position: left bottom;
  }
  50% {
    background-position: right top;
  }
  100% {
    background: linear-gradient(#e66465, #9198e5);
    background-size: 200% 200%;
    background-position: left bottom;
  }
}

#UserLayout .content {
  background: linear-gradient(#e66465, #9198e5);
  margin-bottom: 16px;
  padding: 20px;
  animation: gradient 5s linear infinite;
}

#UserLayout .footer {
  background: #efefef;
  padding: 16px;
  position: sticky;
  bottom: 0;
  left: 0;
  right: 0;
  text-align: center;
}
</style>

<script setup lang="ts"></script>
