<template>
  <div id="exampleView">
    <CodeEditor :value="codeValue" :handle-change="onCodeChange"></CodeEditor>
    <MdEditor :value="mdValue" :handle-change="onMdChange"></MdEditor>
  </div>
</template>

<script setup lang="ts">
import { ref } from "vue";
import MdEditor from "@/components/MdEditor.vue";
import CodeEditor from "@/components/CodeEditor.vue";

const mdValue = ref("");
const codeValue = ref("");

const onMdChange = (v: string) => {
  mdValue.value = v;
};

const onCodeChange = (v: string) => {
  codeValue.value = v;
};
</script>
