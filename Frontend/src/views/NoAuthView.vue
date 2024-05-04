<template>
  <div class="cover">
    <h1 id="er">
      未授权用户
      <small>404</small>
    </h1>
    <h2 id="lead">
      你貌似未能获得授权，或者服务器崩溃了<br />
      请通过以下方式联系管理员⬇️
    </h2>
    <a-layout-footer class="footer">
      <a href="http://nighterdream.cn" rel="nofollow">
        <img
          class="picture"
          src="https://img.shields.io/badge/%E6%88%91%E7%9A%84%E5%8D%9A%E5%AE%A2-nighterdream.cn-40c5f1.svg"
          alt="博客"
          data-canonical-src="https://img.shields.io/badge/%E6%88%91%E7%9A%84%E5%8D%9A%E5%AE%A2-nighterdream.cn-40c5f1.svg"
          style="max-width: 100%"
        />
      </a>
      <a
        href="https://space.bilibili.com/33934287?spm_id_from=333.1007.0.0"
        rel="nofollow"
      >
        <img
          class="picture"
          src="https://img.shields.io/badge/BiliBili-blue.svg?logo=bilibili&amp;logoColor=white"
          alt="Bilibili"
          data-canonical-src="https://img.shields.io/badge/BiliBili-blue.svg?logo=bilibili&amp;logoColor=white"
          tyle="max-width: 100%"
        />
      </a>
      <a href="mailto:nighterdream123@gmail.com">
        <img
          class="picture"
          src="https://img.shields.io/badge/%E9%82%AE%E7%AE%B1-nighterdream123@gmail.com-b69118.svg"
          alt="邮箱"
          data-canonical-src="https://img.shields.io/badge/%E9%82%AE%E7%AE%B1-nighterdream123@gmail.com-b69118.svg"
          style="max-width: 100%"
        />
      </a>
    </a-layout-footer>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.cover {
  width: 500px;
  height: 350px;
  border: none;
  border-radius: 5px;
  display: inline-block;
  align-items: center;
  margin-top: 100px;
  position: relative;
  margin-right: 400px;
  left: 480px;
  background-color: rgba(255, 255, 255, 0.8);
  padding: 10px;
}

.footer {
  border: none;
  border-radius: 5px;
  display: inline-block;
  box-sizing: border-box;
  position: relative;
  top: 50px;
  left: 48px;
  padding: 10px;
}

h1 {
  position: absolute;
  top: 60px;
  left: 150px;
  text-align: center;
}

#lead {
  position: absolute;
  top: 115px;
  left: 70px;
  text-align: center;
}

.picture {
  position: relative;
  top: 265px;
  left: -40px;
  align-items: center;
  height: 22px;
}
</style>
