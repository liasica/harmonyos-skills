---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/development-environment-faq-0008
title: ohpm命令行使用与环境变量配置常见问题
breadcrumb: FAQ > DevEco Studio > 环境准备 > 常见问题 > ohpm命令行使用与环境变量配置常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:48+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:f48835ec439e80d817b95a5d42f091475ea9edb20da88b4defd219b59e753fed
---

**Q：安装ohpm后，如果在命令行中无法直接使用ohpm，请检查环境变量配置是否正确？**

**A**：

**须知** 

安装node.js 18.x及以上版本，并配置环境变量。

ohpm 默认解压路径为：DevEco Studio 中默认安装位置：<DevEco Studio 安装目录>\tools\ohpm；命令行工具中默认安装位置：<Command Line Tools 安装目录>/command-line-tools/ohpm。

1. 在Windows系统中，右键点击“此电脑”选择“属性”，进入“高级系统设置”，点击“环境变量”，在“系统变量”中找到“Path”，点击“编辑”，添加ohpm工具包解压后的bin目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/RQgLKnWpRFOXqqevjLXSaA/zh-cn_image_0000002772993938.png "点击放大")
2. 添加变量后，重开命令行窗口，执行ohpm -v查看ohpm版本号，终端输出版本号信息（如1.0.0）即为成功。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/ipnkxogXRDuQVqXsIOmf_Q/zh-cn_image_0000002802393747.png)

**Q：在Linux/Mac系统中，安装ohpm后，不能在命令行中使用ohpm，如何解决？**

**A**：编辑配置文件，将ohpm工具包解压目录中的bin目录路径添加到PATH环境变量中（以 Mac 系统的 Zsh 命令行为例）。

1. 打开终端并编辑 ~/.zshrc 文件。

   ```shell
   vi ~/.zshrc
   ```
2. 在文件末尾添加以下行，将软件的bin目录添加到PATH环境变量中（例如：/home/user/ohpm/bin）：

   ```shell
   export PATH="/home/user/ohpm/bin:$PATH"
   ```
3. 保存 ~/.zshrc 文件并退出编辑器。
4. 使用以下命令使更改生效，或者关闭并重新打开命令行窗口。

   ```shell
   source ~/.zshrc
   ```
5. 执行ohpm -v查看 ohpm 版本号，命令行输出版本号（如 1.0.0）表示成功。

   ```shell
   ohpm -v
   ```

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/h6aQ37ygTHGTk_Hg7AKr4Q/zh-cn_image_0000002802353669.png)

**Q：oh-package.json5文件中dependencies、devDependencies和dynamicDependencies的区别是什么？**

A：

oh-package.json5文件中：

* dependencies（生产依赖）：声明生产依赖，即代码中需要导入的HarmonyOS三方库，用于编译和运行阶段。
* devDependencies（开发依赖）：用于项目的开发或测试阶段。
* dynamicDependencies（动态依赖）：配置用于动态加载的HSP模块。

示例如下：

```json
{
  "name": "parameter-test",
  "version": "@param:version",
  "modelVersion": "5.0.4",
  "description": "test desc.",
  "main": "index.ets",
  "author": "test author",
  "license": "ISC",
  "dependencies": {
    "libtest1": "@param:dependencies.libtest1"
  },
  "devDependencies": {
    "libtest2": "@param:devDependencies.libtest2"
  },
  "dynamicDependencies": {
    "libtest3": "@param:dynamicDependencies.libtest3"
  },
  "parameterFile": '.parameterFile/parameterFile.json5',// Enable parameterization and specify the path to the parameterized configuration file
}
```

参考链接：[oh-package.json5文件](../doccenter-deveco-studio/ide-oh-package-json5.md)，[添加依赖项](../doccenter-deveco-studio/ide-hvigor-dependencies.md)。
