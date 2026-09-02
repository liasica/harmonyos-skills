---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-deveco-cli-install
title: 快速入门
breadcrumb: 指南 > AI Coding > DevEco CLI > 快速入门
category: harmonyos-guides
scraped_at: 2026-09-02T15:00:30+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:042724f7fda740a87ec4be22c388608101f1aee34dfb8ddf564462025fe1d215
---

## 环境准备

DevEco CLI支持在Windows、macOS和Linux上运行。

从1.3.0版本开始支持在Linux上运行。

### 环境搭建

* 下载和安装[DevEco Studio](https://developer.huawei.com/consumer/cn/deveco-studio/) 6.0.0及以上版本。
* 安装[Node.js](https://nodejs.org/)，推荐使用22及以上版本。

**说明** 

在Linux环境运行时，需要手动配置环境变量来指定工具链路径。

```shell
export DEVECO_CLI_CLI_PATH=/opt/command-line-tools
```

### 检验环境是否搭建成功

在终端Shell中，验证Node.js环境：

```shell
node -v
npm -v
```

## 安装和更新

安装DevEco CLI（稳定版）

```shell
npm install -g @deveco/deveco-cli@stable
```

安装DevEco CLI（尝鲜版）

```shell
npm install -g @deveco/deveco-cli
```

查看版本

```shell
devecocli --version
```

更新

```shell
devecocli update
```

**说明** 

安装命令中的@stable标签是可选项，带有@stable标签表示下载安装稳定版本，未带有@stable标签表示下载安装最新版本。

## 首次使用

1. 初始化。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/pcjzwJWkTaq7z4mzgeLqCw/zh-cn_image_0000002701823622.png)
2. 创建一个HarmonyOS应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/Mlh5v9l7TpW06ub0q3uQ_w/zh-cn_image_0000002701663700.png)
