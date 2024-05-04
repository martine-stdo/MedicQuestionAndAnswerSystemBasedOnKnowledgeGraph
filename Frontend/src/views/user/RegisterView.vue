<template>
  <div id="userRegister" class="register-container">
    <a-form :model="form" @submit="handleSubmit" class="register-form">
      <a-form-item
        field="userAccount"
        tooltip="用户名至少3个字符"
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
      <a-form-item
        field="confirmPassword"
        tooltip="请确认密码"
        label="确认密码"
        class="form-item"
      >
        <a-input-password
          v-model="form.confirmPassword"
          placeholder="请再次输入密码"
          allow-clear
        />
      </a-form-item>
      <a-form-item>
        <a-button html-type="submit" class="register-button">注册</a-button>
      </a-form-item>
      <a-form-item class="toLogin">
        <a href="http://localhost:8080/user/login">已有账号？点击登录</a>
      </a-form-item>
    </a-form>
  </div>
</template>

<script setup lang="ts">
import { reactive } from "vue";
import message from "@arco-design/web-vue/es/message";
import { useRouter } from "vue-router";
import axios from "axios";

const router = useRouter();

const form = reactive({
  userAccount: "",
  userPassword: "",
  confirmPassword: "",
});

const handleSubmit = async () => {
  if (form.userPassword !== form.confirmPassword) {
    message.error("密码和确认密码不匹配");
  } else {
    const requestData = {
      userAccount: form.userAccount,
      userPassword: form.userPassword,
    };
    try {
      const response = await axios.post(
        "http://localhost:8000/user/register/",
        requestData
      );
      console.log(response.data);

      if (response.data.code === 200) {
        message.success("注册成功！即将跳转到登录页面");
        setTimeout(() => {
          router.push({ path: "/user/login", replace: true });
        }, 3000);
      } else {
        message.error("注册失败，" + response.data.message);
      }
    } catch (error) {
      message.error("注册失败，发生了一些错误，请稍后再试。");
    }
  }
};
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
}

.register-form {
  width: 400px;
  padding: 70px 90px 20px 20px;
  margin-bottom: 180px;

  border-radius: 5px;
  background-color: rgba(255, 255, 255, 0.3);
  backdrop-filter: blur(10px);
}

.form-item {
  display: flex;
  align-items: center;
}

.form-item .ant-form-item-label {
  flex: 0 0 80px;
}

.form-item .ant-form-item-control {
  flex: 1;
}

.register-form .register-button {
  width: 100%;
}

.toLogin {
  text-align: center;
  margin-top: 20px;
  margin-left: 80px;
}
</style>
