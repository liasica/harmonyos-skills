---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-install
title: 下载与安装
breadcrumb: 指南 > DevEco Code > DevEco Code TUI > 下载与安装
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:ed66da0e0f95732714f7a0cbabc2ac8018702791ff5e5e7048ca3ad8c6501e43
---

DevEco Code支持通过npm包管理器进行分发，开发者可以在系统命令窗口或PowerShell中全局安装后，独立调用相关命令，灵活性高。同时，DevEco Code也支持在DevEco Studio的集成终端中直接使用，开发者无需额外配置即可在DevEco Studio终端调用相关命令，操作便捷。

Windows/macOS版DevEco Code支持通过npm安装，鸿蒙电脑版DevEco Code支持通过npm安装和在DevEco Studio中安装。

## 通过npm分发安装和启动

### 环境要求

DevEco Code支持在Windows、macOS和鸿蒙电脑上运行，具体运行环境要求如下。

**Windows运行环境：**

| 类别 | 要求 |
| --- | --- |
| 操作系统 | Windows 11 22H2及以上版本 |
| RAM | * 8GB及以上（以短会话、单模块代码编辑场景为主） * 16GB及以上（以长会话、大工程代码编辑、频繁编译构建和模拟器/真机调试场景为主） |
| 磁盘空间 | 8GB及以上  若需对HarmonyOS工程进行编译构建，以及调用模拟器/真机调试工具链时，需20GB及以上 |
| 终端Shell | PowerShell5.1及以上版本，推荐使用PowerShell7及以上版本 |

**macOS运行环境：**

| 类别 | 要求 |
| --- | --- |
| 操作系统 | macOS 15 Sequoia及以上版本 |
| CPU | Intel芯片或M系列Apple芯片，推荐使用M系列Apple芯片 |
| RAM | * 8GB及以上（以短会话、单模块代码编辑场景为主） * 16GB及以上（以长会话、大工程代码编辑、频繁编译构建和模拟器/真机调试场景为主） |
| 磁盘空间 | 8GB及以上  若需对HarmonyOS工程进行编译构建，以及调用模拟器/真机调试工具链时，需20GB及以上 |
| 终端Shell | Zsh（Z Shell） |

**鸿蒙电脑运行环境****：**

| 类别 | 要求 |
| --- | --- |
| 操作系统 | HarmonyOS 7.0及以上版本 |
| RAM | 16GB及以上 |
| 磁盘空间 | 100GB及以上 |
| 终端Shell | HiShell |

### 搭建环境（Windows/macOS）

DevEco Code通过npm分发，安装前请先准备以下环境：

1. 安装[Node.js](https://nodejs.org/)，推荐使用22及以上版本。
2. （可选）安装[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/) 6.1.0及以上版本，不安装会影响HarmonyOS工程的编译构建、推包等。
3. （可选）配置DEVECO\_HOME环境变量，指向DevEco Studio安装目录。DevEco Studio默认路径为：
   * macOS：/Applications/DevEco-Studio.app
   * Windows：C:\Program Files\Huawei\DevEco Studio

### 搭建环境（鸿蒙电脑）

1. 在鸿蒙电脑上查看**设置** **> 系统**中**开发者选项**是否存在，如果不存在，可在**设置 >** **具体的设备名称**中，连续七次单击**软件****版本**，直到提示“开启开发者选项”，点击**确认开启**后输入PIN码（如果已设置），设备将自动重启，请等待设备完成重启。
2. 如需使用多设备预览器，需要打开DevEco Studio，并且鸿蒙电脑需要在**设置 > 系统 >** **开发者选项**中，打开**无线调试**开关。
3. DevEco Code通过npm进行分发，安装前需要先下载和安装[DevEco Studio](ide-hmos-software-install.md)或[Command Line Tools](ide-hmos-commandline-get.md)。

   如果安装DevEco Studio，按以下步骤配置环境变量。

   1. 在终端中执行以下命令，打开环境变量配置文件。

      ```screen
      vim ~/.zshrc
      ```
   2. 在.zshrc文件中添加Node.js环境变量。hmos-clt\_x.x.x请根据实际情况进行修改，可在鸿蒙电脑终端或DevEco Studio终端中进入/data/service/hnp/hmos-clt.org目录查看。

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

   1. 在终端中执行以下命令，解压命令行工具commandline-tools-harmonyos-xxx.tar.gz，工具名称请根据实际情况进行修改。

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

### 安装

**安装**（稳定版）

```shell
npm install -g @deveco/deveco-code@stable
```

**安装**（尝鲜版）

```shell
npm install -g @deveco/deveco-code
```

**说明** 

* 鸿蒙电脑版DevEco Code仅支持通过npm install -g @deveco/deveco-code命令安装尝鲜版。
* 安装命令中的标签@stable是可选项，加标签@stable表示下载安装稳定版本，不加标签@stable表示下载安装最新版本。
* 可通过npm的registry参数配置不同的镜像源，命令为npm install -g @deveco/deveco-code --registry=string。推荐使用npm官方源（https://registry.npmjs.org/）或淘宝镜像源（https://registry.npmmirror.com），其他镜像源可能因同步延迟导致安装失败或版本滞后。

  安装时默认使用npm官方源，指定淘宝镜像源时命令为npm install -g @deveco/deveco-code --registry=https://registry.npmmirror.com。

### 启动与登录

在终端Shell中执行以下命令启动DevEco Code，若未登录按照指引先登录华为账号。

```shell
deveco
```

执行以下命令退出登录，下次启动时需重新登录。

```shell
deveco auth logout
```

### 更新与卸载

**查看版本**

```shell
deveco --version
```

**更新**

```shell
deveco upgrade
```

**卸载**

```shell
deveco uninstall   // 卸载运行时数据和安装包，适用于彻底清除所有数据的场景
npm uninstall -g @deveco/deveco-code   // 保留运行时数据，只卸载安装包，适用于保留配置项卸载重装的场景
```

## 在DevEco Studio中安装和启动

**说明** 

当前仅鸿蒙电脑版DevEco Code支持在DevEco Studio中安装和启动。

### 安装

在鸿蒙电脑版DevEco Studio的菜单栏点击**安装DevEco Code**，等待完成安装。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/k1oMlIo6RduT_X6eEzBNVA/zh-cn_image_0000002779407184.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=C47F2CE3468772D8EC45507C233E0AA22A855A3B7E21F48273A87AACD53ECC69 "点击放大")

### 启动与登录

1. 安装完成后，点击**新对话**新建并开启一个会话。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/4SAJ7LzgTjK_bGRn-sxMVQ/zh-cn_image_0000002779567160.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A1C8BA4E5B5B589D5A6724CF14384C14AF1ED38364430B1BDE68BC3598F1D04)
2. 选择信任当前文件夹，并点击链接登录华为账号。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/SFARz-4hT6m7SsCJ8PnX2Q/zh-cn_image_0000002779407182.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=BEE95CD93E836A89022B60083C2E5115B769645285653D08E9417CE1B11F98C0)
3. 登录完成后，在终端开始体验DevEco Code。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/O07u0o_mQPiGyDU5yuNPow/zh-cn_image_0000002779567162.png?HW-CC-KV=V1&HW-CC-Date=20261112T233231Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A98982E16A3F000033A07F87DAD1CE19FB36096411CA8DA54009FF24B3E7D84 "点击放大")

### 更新与卸载

卸载命令

```shell
deveco uninstall
```

更新命令

```shell
deveco upgrade
```
