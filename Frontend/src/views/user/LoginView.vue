<template>
  <div id="userLogin" class="login-container">
    <a-form :model="form" @submit="handleSubmit" class="login-form">
      <a-form-item
        field="userAccount"
        tooltip="密码不少于8位"
        label="账号"
        class="form-item"
      >
        <a-input v-model="form.userAccount" placeholder="请输入账号" />
      </a-form-item>
      <a-form-item
        field="userPassword"
        tooltip="密码不少于8位"
        label="密码"
        class="form-item"
      >
        <a-input-password
          v-model="form.userPassword"
          placeholder="请输入密码"
          allow-clear
        />
      </a-form-item>
      <a-form-item field="isRead" class="agreement-checkbox">
        <a-checkbox v-model="form.isRead">同意用户注册协议</a-checkbox>
      </a-form-item>
      <a-form-item>
        <a-button html-type="submit" class="login-button">登录</a-button>
      </a-form-item>
    </a-form>
  </div>
</template>

<script setup lang="ts">
import { reactive } from "vue";
import message from "@arco-design/web-vue/es/message";
import { useRouter } from "vue-router";
import { useStore } from "vuex";
import axios from "axios";

const router = useRouter();
const store = useStore();

const form = reactive({
  userAccount: "",
  userPassword: "",
  isRead: false,
});

const handleSubmit = async () => {
  if (!form.isRead) {
    message.error("请先同意用户协议");
  } else {
    const requestData = {
      userAccount: form.userAccount,
      userPassword: form.userPassword,
    };
    try {
      const response = await axios.post(
        "http://localhost:8000/user/login/",
        requestData
      );
      console.log(response.data);

      if (response.data.code === 0) {
        // 登录成功
        // 登录成功，调用getLoginUser并传递账号和密码
        await store.dispatch("user/getLoginUser", {
          userAccount: form.userAccount,
          userPassword: form.userPassword,
        });
        message.success("登录成功！即将回到主页");
        setTimeout(() => {
          router.push({ path: "/", replace: true });
        }, 3000);
      } else {
        // 登录失败，显示后端返回的错误消息
        message.error("登录失败，" + response.data.message);
      }
    } catch (error) {
      // 请求出错，显示默认错误消息
      message.error("登录失败，发生了一些错误，请稍后再试。");
    }
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.login-form {
  width: 400px;
  padding: 70px 90px 20px 20px;
  margin-bottom: 180px;

  border-radius: 5px;
  background-color: rgba(255, 255, 255, 0.3); /* 设置背景颜色及透明度 */
  backdrop-filter: blur(10px); /* 毛玻璃特效 */
}

.form-item {
  display: flex;
  align-items: center;
}

.form-item .ant-form-item-label {
  flex: 0 0 80px; /* 账号和密码的标签宽度 */
}

.form-item .ant-form-item-control {
  flex: 1; /* 输入框宽度自适应 */
}

.login-form .login-button {
  width: 100%;
}

.agreement-checkbox {
  margin-bottom: 20px;
}

.agreement-checkbox .ant-checkbox-wrapper {
  display: flex;
  align-items: center;
}

.agreement-checkbox .ant-checkbox-wrapper span {
  margin-left: 5px;
}

.agreement-checkbox .ant-checkbox-wrapper:hover {
  cursor: pointer;
}
</style>
