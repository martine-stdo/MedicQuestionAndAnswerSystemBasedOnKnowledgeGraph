<template>
  <div id="UserLayout">
    <a-layout style="min-height: 100vh">
      <a-layout-header class="header"></a-layout-header>
      <a-space class="space">
        <img
          src="../assets/kg_logo.png"
          class="logo"
          style="
            height: 50px;
            width: 50px;
            border-radius: 50%;
            margin-left: 15px;
            margin-top: -2px;
            margin-bottom: 2px;
          "
        />
        <div class="title">欢迎使用基于知识图谱的医学问答系统</div>
      </a-space>
      <a-layout-content class="content">
        <router-view />
      </a-layout-content>
      <a-layout-footer class="footer">
        <p class="schoolMessage">
          Copyright &copy; 武汉轻工大学 数学与计算机学院 2024
        </p>
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
  background: url(https://api.bimg.cc/random);
  margin-bottom: 16px;
  padding: 20px;
}

#UserLayout .footer {
  background: #efefef;
  padding: 16px;
  position: sticky;
  bottom: 0;
  height: 16px;
  left: 0;
  right: 0;
  text-align: center;
}
</style>

<script setup lang="ts"></script>
