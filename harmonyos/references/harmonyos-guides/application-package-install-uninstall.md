---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-package-install-uninstall
title: 应用安装卸载与更新开发指导
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 应用程序包基础知识 > 应用程序包安装卸载与更新 > 应用安装卸载与更新开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c691e354e31b9f078ed7011e452a110f4c05f1e6ba6c9f9f748f0f8c1efa7b2f
---

本章节介绍应用程序包的安装卸载流程和两种更新方式。

## 应用程序包的安装卸载

开发者可以通过调试命令安装和卸载应用，安装应用命令参考bm工具中的[install](bm-tool.md#安装命令install)，卸载应用命令参考bm工具中的[uninstall](bm-tool.md#卸载命令uninstall)，详情参见[编译发布与上架部署流程图](application-package-structure-stage.md#发布态包结构)。

**图1** 应用程序包安装和卸载流程（开发者）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/8kmi2DVUQdS1SGEngeUVJg/zh-cn_image_0000002552957476.png?HW-CC-KV=V1&HW-CC-Date=20260427T233726Z&HW-CC-Expire=86400&HW-CC-Sign=4F6CBD92FCBE2502DC6A8982E25AAE86EC8BB5426CEF468A521013FCFAF2AA0D)

应用上架应用市场后，终端设备用户可在设备上通过应用市场安装应用。

**图2** 应用程序包安装和卸载流程（终端设备用户）

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/28eZ3o9bS_qwr1MQVaaSnQ/zh-cn_image_0000002583477477.png?HW-CC-KV=V1&HW-CC-Date=20260427T233726Z&HW-CC-Expire=86400&HW-CC-Sign=D405626E00E182EACBCEA04E271C70235AD6E5427FBB3783CCBC0F730FA0BDEB)

## 应用程序包的更新

对于开发者，应用程序包的更新，首先需要更新[app.json5配置文件](app-configuration-file.md)中的versionCode版本号字段，通过DevEco Studio打包后在应用市场发布，发布流程与首次发布一致。对于终端设备用户，新版本发布后，可以通过以下两种方式更新应用程序包。

* 应用市场内更新：应用市场通知用户该应用有新版本，用户根据通知到应用市场（客户端）进行升级。
* 应用内检测升级：开发者根据[更新指导](store-update.md#section316371715233)实现版本更新提醒功能，应用启动完成或用户在应用中主动检查新版本时，会弹出升级对话框，用户根据对话框提示升级。
