---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/upgrade-tool-chain
title: 开发工具链升级
breadcrumb: 版本说明 > 应用升级适配指导-向6.0.0(20)升级 > 开发工具链升级
category: harmonyos-releases
scraped_at: 2026-04-28T07:37:19+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:988cb04500a679ead30179836124036ab4b9a913dfc95d64a7db7bb8d9da5263
---

## 升级DevEco Studio

1. 获取并安装6.0.0(20)配套的DevEco Studio。

   已安装历史版本DevEco Studio的开发者可从软件界面检查升级，或者在[官网下载中心](https://developer.huawei.com/consumer/cn/download/)重新下载最新版本DevEco Studio并重新安装。
2. 安装后请阅读DevEco Studio的[变更说明](change-description-600-beta1.md)，查看软件变更是否涉及适配操作。
3. 6.0.0(20)配套的DevEco Studio已预置6.0.0(20)版本的HarmonyOS SDK，再次编译应用时将会使用该SDK进行编译。

## 升级命令行工具

命令行工具中同样预置了6.0.0(20)的HarmonyOS SDK，DevEco Studio升级后，请同步升级相同版本的命令行工具，确保使用命令行工具在流水线编译出的应用包与DevEco Studio编译的应用包使用了相同的SDK工具链。

可在[官网下载中心](https://developer.huawei.com/consumer/cn/download/)的Command Line Tools部分获取与DevEco Studio同版本的命令行工具。
