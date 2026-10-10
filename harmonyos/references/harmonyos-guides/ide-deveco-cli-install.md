---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-cli-install
title: 快速入门
breadcrumb: 指南 > DevEco CLI > 快速入门
category: harmonyos-guides
scraped_at: 2026-10-11T07:23:26+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:8af2f101f5c27b8eb967fbadec1b79141f9ea0a0a48901be1d5b110686424493
---

## 环境准备

DevEco CLI支持在Windows、macOS、Linux和鸿蒙电脑上运行。

从1.3.0版本开始支持在Linux上运行。

### 搭建环境（Windows/macOS/Linux）

* 下载和安装[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/) 6.0.0及以上版本。
* 安装[Node.js](https://nodejs.org/)，推荐使用22及以上版本。

**说明** 

在Linux环境运行时，需要手动配置环境变量来指定工具链路径。

```shell
export DEVECO_CLI_CLI_PATH=/opt/command-line-tools
```

### 搭建环境（鸿蒙电脑）

1. 在鸿蒙电脑上查看**设置** **> 系统**中**开发者选项**是否存在，如果不存在，可在**设置 >** **具体的设备名称**中，连续七次单击**软件****版本**，直到提示“开启开发者选项”，点击**确认开启**后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
2. 如需使用多设备预览器，需要打开DevEco Studio，并且鸿蒙电脑需要在**设置 > 系统 >** **开发者选项**中，打开**无线调试**开关。
3. DevEco CLI通过npm进行分发，安装前需要先下载和安装[DevEco Studio](ide-hmos-software-install.md)或[Command Line Tools](ide-hmos-commandline-get.md)。

   如果安装DevEco Studio，按以下步骤配置环境变量。

   1. 执行以下命令，打开环境变量配置文件。

      ```screen
      vim ~/.zshrc
      ```
   2. 添加Node.js环境变量。hmos-clt\_x.x.x请根据实际情况进行修改，可在鸿蒙电脑终端或DevEco Studio终端中进入/data/service/hnp/hmos-clt.org目录查看。

      ```shell
      export PATH=/data/service/hnp/hmos-clt.org/hmos-clt_x.x.x/node/bin:$PATH
      ```
   3. 在终端中执行以下命令，设置npm包安装路径，建议设置到个人目录下/storage/Users/currentUser/npm。

      ```shell
      npm config set prefix /storage/Users/currentUser/npm
      ```
   4. 在.zshrc文件中添加npm环境变量。

      ```shell
      export PATH=/storage/Users/currentUser/npm/bin:$PATH
      ```
   5. 保存并关闭文件，使用source命令重新加载.zshrc配置文件。

      ```screen
      source ~/.zshrc
      ```

   如果安装Command Line Tools，按以下步骤配置环境变量。

   1. 在终端中执行命令，解压命令行工具commandline-tools-harmonyos-xxx.tar.gz，工具名称请根据实际情况进行修改。

      ```shell
      tar -zxvf commandline-tools-harmonyos-xxx.tar.gz
      ```
   2. 执行以下命令，打开环境变量配置文件。

      ```screen
      vim ~/.zshrc
      ```
   3. 在.zshrc文件中添加Node.js环境变量。

      ```shell
      export COMMAND_LINE_TOOL_PATH=${Command Line Tools解压路径}/command-line-tools   # 解压路径替换为实际的解压路径
      export PATH=$COMMAND_LINE_TOOL_PATH/node/bin:$PATH  # 配置Node.js环境变量
      ```
   4. 保存并关闭文件，使用source命令重新加载.zshrc配置文件。

      ```screen
      source ~/.zshrc
      ```
   5. 在终端中执行以下命令，设置npm包安装路径，建议设置到个人目录下/storage/Users/currentUser/npm。

      ```shell
      npm config set prefix /storage/Users/currentUser/npm
      ```
   6. 在.zshrc文件中添加npm环境变量。

      ```shell
      export PATH=/storage/Users/currentUser/npm/bin:$PATH
      ```
   7. 保存并关闭文件，使用source命令重新加载.zshrc配置文件。

      ```screen
      source ~/.zshrc
      ```

### 检验环境是否搭建成功

在终端Shell中，验证Node.js环境：

```shell
node -v
npm -v
```

## 安装和更新

**安装**（稳定版）

```shell
npm install -g @deveco/deveco-cli@stable
```

**安装**（尝鲜版）

```shell
npm install -g @deveco/deveco-cli
```

**查看版本**

```shell
devecocli --version
```

**更新**

```shell
devecocli update
```

**说明** 

* 鸿蒙电脑版DevEco CLI仅支持通过npm install -g @deveco/deveco-cli命令安装尝鲜版。
* 安装命令中的@stable标签是可选项，带有@stable标签表示下载安装稳定版本，未带有@stable标签表示下载安装最新版本。

## 首次使用

1. 初始化。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/j8WEOMEET_Gz7JzZFNOiTg/zh-cn_image_0000002701823622.png)
2. 创建一个HarmonyOS应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/p6EMl8T5Sp2MZxdILPYLRA/zh-cn_image_0000002701663700.png)
