// const { defineConfig } = require("@vue/cli-service");
// const MonacoWebpackPlugin = require("monaco-editor-webpack-plugin");

// module.exports = defineConfig({
//   transpileDependencies: true,
//   chainWebpack(config) {
//     config.plugin("monaco").use(new MonacoWebpackPlugin());
//   },
//   configureWebpack: {
//     devtool: "source-map",
//   },
// });
module.exports = {
  configureWebpack: {
    devtool: "source-map",
  },
};
