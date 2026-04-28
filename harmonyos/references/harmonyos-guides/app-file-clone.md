---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-file-clone
title: 应用克隆适配指导
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 应用克隆适配指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6ebdb76421aa98c42280b430b8c964ff8f030914347ee3a08251314de7c856df
---

## 简介

用户在日常换机过程中，需要将一台设备的数据备份并发送到另一台设备上进行恢复，以完成跨设备的数据迁移，此时需要使用克隆工具（"数据克隆"应用）。接入克隆工具时，应用需实现备份恢复接口[BackupExtensionAbility](../harmonyos-references/js-apis-application-backupextensionability.md#backupextensionability)，在onBackup中实现数据备份，在onRestore中实现数据恢复。若应用未实现BackupExtensionAbility，克隆过程将仅迁移旧设备上的应用，而不迁移应用数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/YzTXDResTo2UuaC_R3IhwQ/zh-cn_image_0000002583478265.png?HW-CC-KV=V1&HW-CC-Date=20260427T234112Z&HW-CC-Expire=86400&HW-CC-Sign=5674B3ED1B58C7F81D26AE12F4EEC8463BA71F2EED19296C5E0F7F931EED6CDB)

## 适配指导

API version 12开始，三方应用接入克隆只需要接入备份恢复能力即可，接入指导： **[应用接入数据备份恢复](app-file-backup-extension.md)**。
