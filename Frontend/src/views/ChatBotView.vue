<template>
  <!-- 聊天容器 -->
  <div class="chat-container" ref="chatContainer">
    <!-- 聊天消息显示区域 -->
    <div class="chat-messages">
      <!-- 遍历消息数组，显示每条消息 -->
      <div
        v-for="(message, index) in messages"
        :key="index"
        :class="message.role"
      >
        {{ message.content }}
      </div>
    </div>
    <!-- 聊天输入框 -->
    <div class="chat-input">
      <input
        v-model="newMessage"
        @keyup.enter="sendMessage"
        placeholder="输入消息..."
      />
      <button @click="sendMessage">发送</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      // 存储用户和机器人的消息
      messages: [],
      // 用户新消息输入框
      newMessage: "",
    };
  },
  methods: {
    // 发送消息
    async sendMessage() {
      // Store the message before clearing the input
      const messageToSend = this.newMessage.trim();

      this.messages.push({ role: "user", content: messageToSend });
      this.newMessage = ""; // 清空输入框
      this.scrollToBottom(); // 滚动到底部

      try {
        const response = await axios.post("http://localhost:8000/user/chat/", {
          question: messageToSend, // 发送之前存储的消息内容
        });
        console.log(response.data);

        this.messages.push({
          role: "bot",
          content: response.data.reply.content,
        });
        this.scrollToBottom(); // 滚动到底部
      } catch (error) {
        console.error("发送消息失败:", error);
      }
    },

    // 滚动到底部
    scrollToBottom() {
      // 设置滚动条位置到最底部
      this.$refs.chatContainer.scrollTop =
        this.$refs.chatContainer.scrollHeight;
    },
  },
};
</script>

<style>
/* 样式代码省略 */

/* 设置聊天消息容器样式 */
.chat-container {
  margin-left: auto;
  margin-right: auto;
  margin-top: 49px;
  width: 95%;
  height: 510px;
  border: none;
  background: #eeeeee;
  opacity: 0.95;
  border-radius: 15px;
  display: flex; /* 使用 Flex 布局 */
  flex-direction: column; /* 垂直排列子元素 */
}

/* 设置聊天消息显示区域样式 */
.chat-messages {
  flex: 1; /* 填充剩余空间 */
  overflow-y: auto; /* 滚动条 */
}

/* 设置聊天消息样式 */
.chat-messages div {
  padding: 10px;
  margin-bottom: 10px;
  border-radius: 5px;
}

/* 设置用户消息样式 */
.user {
  margin-top: 40px;
  align-self: flex-end; /* 用户消息显示在右侧 */
  margin-left: 500px;
  margin-right: 50px;
  background-color: #007bff; /* 用户消息背景颜色 */
  color: white; /* 用户消息文字颜色 */
}

/* 设置机器人消息样式 */
.bot {
  margin-top: 40px;
  align-self: flex-start; /* 机器人消息显示在左侧 */
  margin-right: 500px;
  margin-left: 50px;
  background-color: #28a745; /* 机器人消息背景颜色 */
  color: white; /* 机器人消息文字颜色 */
}

/* 设置聊天输入框样式 */
.chat-input {
  display: flex;
  margin-top: auto; /* 将输入框推到底部 */
  width: 800px;
  margin-left: 300px;
  margin-bottom: 40px;
}

.chat-input input {
  flex: 1; /* 输入框填充剩余空间 */
  padding: 10px;
  border: none;
  border-radius: 5px;
  margin-right: 10px;
}

.chat-input button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

.chat-input button:hover {
  background-color: #0056b3;
}
</style>
