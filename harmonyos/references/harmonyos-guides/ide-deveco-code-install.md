---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-code-install
title: 下载与安装
breadcrumb: 指南 > AI Coding > DevEco Code > 下载与安装
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4192329a50e7ad2152a9808e59953ab23fb95290b595c5490ad1ef79c333fc61
---

## 环境准备

### 环境要求

DevEco Code支持在Windows和macOS上运行，具体运行环境要求如下。

Windows运行环境：

| 类别 | 要求 |
| --- | --- |
| 操作系统 | Windows 11 22H2及以上版本 |
| RAM | * 8GB及以上（以短会话、单模块代码编辑场景为主） * 16GB及以上（以长会话、大工程代码编辑、频繁编译构建和模拟器/真机调试场景为主） |
| 磁盘空间 | 8GB及以上  若需对HarmonyOS工程进行编译构建，以及调用模拟器/真机调试工具链时，需20GB及以上 |
| 终端Shell | PowerShell5.1及以上版本，推荐使用PowerShell7及以上版本 |

macOS运行环境：

| 类别 | 要求 |
| --- | --- |
| 操作系统 | macOS 15 Sequoia及以上版本 |
| CPU | Intel芯片或M系列Apple芯片，推荐使用M系列Apple芯片 |
| RAM | * 8GB及以上（以短会话、单模块代码编辑场景为主） * 16GB及以上（以长会话、大工程代码编辑、频繁编译构建和模拟器/真机调试场景为主） |
| 磁盘空间 | 8GB及以上  若需对HarmonyOS工程进行编译构建，以及调用模拟器/真机调试工具链时，需20GB及以上 |
| 终端Shell | Zsh（Z Shell） |

### 搭建环境

DevEco Code通过npm分发，安装前请先准备以下环境：

1. 安装[Node.js](https://nodejs.org/)，推荐使用22及以上版本。
2. （可选）安装[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/) 6.1.0及以上版本，不安装会影响HarmonyOS工程的编译构建、推包等。
3. （可选）配置DEVECO\_HOME环境变量，指向DevEco Studio安装目录。DevEco Studio默认路径为：
   * macOS：/Applications/DevEco-Studio.app
   * Windows：C:\Program Files\Huawei\DevEco Studio

### 检验环境是否搭建成功

在终端Shell中，验证Node.js环境：

```shell
node -v
npm -v
```

## 安装

**安装**（稳定版）

```shell
npm install -g @deveco/deveco-code@stable
```

**安装**（尝鲜版）

```shell
npm install -g @deveco/deveco-code
```

**说明** 

* 可通过npm的registry参数配置不同的镜像源，命令为npm install -g @deveco/deveco-code --registry=string。推荐使用npm官方源（https://registry.npmjs.org/）或淘宝镜像源（https://registry.npmmirror.com），其他镜像源可能因同步延迟导致安装失败或版本滞后。

  安装时默认使用npm官方源，指定淘宝镜像源时命令为npm install -g @deveco/deveco-code --registry=https://registry.npmmirror.com。
* 安装命令中的标签@stable是可选项，加标签@stable表示下载安装稳定版本，不加标签@stable表示下载安装最新版本。

## 更新与卸载

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

## 启动与登录

在终端Shell中执行以下命令启动DevEco Code，若未登录按照指引先登录华为账号。

```shell
deveco
```

执行以下命令退出登录，下次启动时需重新登录。

```shell
deveco auth logout
```
