---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-commandline-get
title: 获取Command Line Tools
breadcrumb: 指南 > 命令行工具 > 获取Command Line Tools
category: harmonyos-guides
scraped_at: 2026-09-04T06:27:25+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:6ed1004013df6f42f78661394d33fcf4ec60e22dfb1ee056644fccb44492207f
---

Command Line Tools集合了HarmonyOS应用开发所用到的系列工具，包括代码检查codelinter、堆栈解析hstack、命令行构建hvigorw、三方依赖管理ohpm和SDK中包含的一系列工具，本文主要讲解codelinter、hstack、hvigorw等工具的使用方式，关于SDK中包含的工具的使用指导请参考[SDK命令行工具](command-line-tools-overview.md)。

## 下载Command Line Tools

请前往[下载中心](https://developer.huawei.com/consumer/cn/download/command-line-tools-for-hmos)获取命令行工具Command Line Tools，并根据下载中心页面**工具完整性**指导进行完整性校验。

**说明** 

HarmonyOS SDK已嵌入命令行工具中，无需额外下载配置。

## 配置环境变量

将命令行工具进行解压，codelinter、ohpm等工具存放在Command Line Tools的bin目录下，需要将该目录配置到PATH环境变量中。

### Windows

命令行工具解压后，将${Command Line Tools解压路径}\command-line-tools\bin目录配置到系统或者用户的PATH环境变量中，配置完成后重新打开命令行窗口。

例如将命令行工具解压到D盘根目录，示例如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/mEuj1VRPQfmWaPnHf2DWNw/zh-cn_image_0000002731542679.png)

### macOS/Linux

1. 将下载后的命令行工具解压到本地。
2. 打开终端工具，执行以下命令，根据输出结果分别执行不同命令。

   ```bash
   echo $SHELL
   ```

   * 如果输出结果为/bin/bash，则执行以下命令，打开.bash\_profile文件。

     ```bash
     vi ~/.bash_profile
     ```
   * 如果输出结果为/bin/zsh，则执行以下命令，打开.zshrc文件。

     ```bash
     vi ~/.zshrc
     ```
3. 单击字母“i”，进入**Insert**模式。
4. 输入以下内容，在PATH下添加环境变量。请以实际命令行工具解压路径为准。

   ```bash
   export PATH=${Command Line Tools解压路径}/command-line-tools/bin:$PATH
   ```
5. 编辑完成后，单击**Esc**键，退出编辑模式，然后输入“:wq”，单击**Enter**键保存。
6. 执行以下命令，使配置的环境变量生效。
   * 如果[步骤2](ide-commandline-get.md#zh-cn_topic_0000001169160500_zh-cn_topic_0000001056725590_li56571525162613)时打开的是.bash\_profile文件，请执行如下命令：

     ```bash
     source ~/.bash_profile
     ```
   * 如果[步骤2](ide-commandline-get.md#zh-cn_topic_0000001169160500_zh-cn_topic_0000001056725590_li56571525162613)时打开的是.zshrc文件，请执行如下命令：

     ```bash
     source ~/.zshrc
     ```

**说明** 

如需验证是否配置成功，可以使用相关命令验证，例如执行codelinter -v指令，检查是否可以正确获取codelinter工具版本。
