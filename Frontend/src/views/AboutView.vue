<template>
  <div class="box">
    <h2>基于知识图谱的医学领域问答系统</h2>
    <p>开发人员</p>
    <p>大数据2020级学生&nbsp;蒋俊涛</p>
    <p>大数据2022级学生&nbsp;张忠杰</p>
    <p>大数据2020级学生&nbsp;张宇洋</p>
    <p>指导老师&nbsp;胡桓浚&nbsp;刘超贤</p>
    <br />
    <p id="p1">你还能通过以下方式联系我们⬇️</p>
    <img
      id="picture1"
      src="https://th.bing.com/th/id/R.b5960735e6ef65b7c292ada8a1662118?rik=a8uNTKB8x94Xfg&riu=http%3a%2f%2fxnfz.whpu.edu.cn%2fdfiles%2f12936%2fimages%2flogo.png&ehk=l%2bpbrjPCk6LTXx6LGTKs9hKiavb%2b4cwQTvozN0edcNY%3d&risl=&pid=ImgRaw&r=0"
      alt="武汉轻工大学"
    />
    <div id="link">
      <a href="http://nighterdream.cn" rel="nofollow">
        <img
          class="picture2"
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
          class="picture2"
          src="https://img.shields.io/badge/BiliBili-blue.svg?logo=bilibili&amp;logoColor=white"
          alt="Bilibili"
          data-canonical-src="https://img.shields.io/badge/BiliBili-blue.svg?logo=bilibili&amp;logoColor=white"
          style="max-width: 100%"
        />
      </a>
      <a href="mailto:nighterdream123@gmail.com">
        <img
          class="picture2"
          src="https://img.shields.io/badge/%E9%82%AE%E7%AE%B1-nighterdream123@gmail.com-b69118.svg"
          alt="邮箱"
          data-canonical-src="https://img.shields.io/badge/%E9%82%AE%E7%AE%B1-nighterdream123@gmail.com-b69118.svg"
          style="max-width: 100%"
        />
      </a>
    </div>
    <button
      id="but1"
      onclick="window.location.href='http://www.nighterdream.cn/'"
    >
      联系我们
    </button>
  </div>
</template>

<script>
export default {
  name: "ContactUsPage",
};
</script>

<style scoped>
/* 样式表中的 CSS 样式 */

#picture1 {
  position: absolute;
  top: -100px; /* 图片位于祖容器的顶部 */
  left: 50%; /* 图片水平居中 */
  transform: translateX(-50%); /* 使图片水平居中 */
}

.picture2 {
  position: relative;
  top: 190px;
  left: -100px;
  align-items: center;
  height: 22px;
}

.box {
  width: 500px;
  height: 350px;
  padding: 0;
  /* text-shadow: 0 2px 4px rgba(241, 239, 239, 0.5); */
  /* -webkit-box-shadow: inset 0 0 100px rgba(0, 0, 0, 0.8); */
  /* box-shadow: inset 0 0 100px rgba(217, 210, 210, 0.8); */
  display: table;
  font-family: "Open Sans", Arial, sans-serif;
  border: none;
  border-radius: 5px;
  display: inline-block;
  align-items: center;
  justify-content: center;
  box-sizing: border-box;
  position: relative;
  top: 150px;
  left: 450px;
  background-color: rgba(255, 255, 255, 0.4);
  text-align: center;
  padding: 10px;
}

#link {
  position: absolute;
  top: 129px;
  left: 175px;
  text-align: center;
  width: 100%;
  height: 40px;
  left: 100px;
  bottom: 0;
  color: #7f5454;
  font-size: 14px;
}

#but1 {
  border: #5382e1;
  background-color: #5382e1;
  border-radius: 10px;
  width: 350px;
  height: 30px;
  position: absolute;
  left: 70px;
  bottom: 85px;
  transition: background-color 0.5s;
}

#but1:hover {
  background-color: #3a6dd3;
}
#but1:active {
  background-color: #3265ca;
}

#p1 {
  position: absolute;
  bottom: 30px;
  left: 160px;
}
/* 其他 CSS 样式 */
</style>
