<template>
  <div id="basicLayout">
    <a-layout style="min-height: 100vh">
      <a-layout-header class="header">
        <GlobalHeader></GlobalHeader>
      </a-layout-header>
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
#basicLayout .header {
  margin-bottom: 10px;
  box-shadow: #eee 1px 1px 5px;
}

#basicLayout .content {
  /* background: linear-gradient(#e66465, #9198e5); */
  background: url(https://api.bimg.cc/random);

  margin-bottom: 16px;
  padding: 20px;
}

#basicLayout .footer {
  background: #efefef;
  padding: 16px;
  position: sticky;
  bottom: 0;
  left: 0;
  right: 0;
  text-align: center;
}
</style>

<script setup lang="ts">
import GlobalHeader from "@/components/GlobalHeader.vue";
</script>
