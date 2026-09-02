---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-83
title: 如何让HAP能够安装到其他手机上
breadcrumb: FAQ > DevEco Studio > 应用调试 > 如何让HAP能够安装到其他手机上
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:435a74657f51d17827aaaf77b014d5444f2ca6a5329395d2e53b78ab0775ca36
---

## 问题现象

如何将HAP包安装到其他手机供测试使用？

## 背景知识

[安装应用文件](../harmonyos-guides/hdc.md#安装应用文件)：应用安装功能在设备端集成bm模块[安装命令（install）](../harmonyos-guides/bm-tool.md#安装命令install)，简化了安装流程，开发者可以在电脑端直接执行命令完成应用安装。

## 解决方案

* 通过命令安装应用。
  1. 获取关联手机的[手动签名](../harmonyos-guides/ide-signing.md#section297715173233)（调试签名），并配置。
  2. 打包HAP以及依赖的HSP。
  3. 使用hdc安装包体：hdc install src（src：软件包所在文件目录）。

  注：从API version 22开始，支持安装APP包，即第2步打包APP即可。
* 通过[DevEco Testing](https://developer.huawei.com/consumer/cn/deveco-testing/?ha_source=sousuo&ha_sourceId=89000251)安装：连接真机后，选择实用工具，点击开始投屏，点击右侧安装应用即可选择HAP包进行安装。
* 通过应用市场能力安装：[指定设备发布](../app/agc-help-internal-test-0000002270709477.md)将应用发布上传至您的服务器或者第三方云上，团队参与测试的人员可以将应用下载到授权的设备上测试。
* 安装到模拟器：[安装应用程序包和上传文件](../harmonyos-guides/ide-emulator-install-upload.md)。
