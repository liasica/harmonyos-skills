---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-file-backup-dataclone
title: 应用数据备份恢复验证指导
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 应用数据备份恢复验证指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8ba9f9334502e987ce07b00ac1a10afd1ea93d3cd3f84df00d5f85c88214c7e3
---

为方便开发者验证[应用接入数据备份恢复](app-file-backup-extension.md)结果，此篇指南介绍了在鸿蒙设备上通过数据克隆应用触发数据备份恢复，以及常见问题说明。

## 环境准备

* 调试设备：两部鸿蒙设备，系统版本在HarmonyOS 6.0.0.115及以上，数据克隆版本在6.0.0.516及以上。
* 安装应用：两部设备都要安装待测试应用。

## 触发数据备份恢复

1. 打开数据克隆应用，一部设备选择“这是新设备”，作为数据恢复侧，另一部设备选择“这是旧设备”，作为数据备份侧，按照提示连接两部设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/CPzYJxjeR12uygp5vGtj_g/zh-cn_image_0000002583478263.png?HW-CC-KV=V1&HW-CC-Date=20260427T234112Z&HW-CC-Expire=86400&HW-CC-Sign=49A59DCD3BB56474CCF039443FBD72638A3AB832FBA6B45EC6553CB0CCA352FC)
2. 在选择数据页面，点击应用及数据，勾选待测试应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/de4hTq5yQ6eEYwYeCryqlg/zh-cn_image_0000002552798614.png?HW-CC-KV=V1&HW-CC-Date=20260427T234112Z&HW-CC-Expire=86400&HW-CC-Sign=BD903C057CEB93E931B48160334E0365047BE366B2218B8B77FB0111693A338B)
3. 等待备份恢复完成，根据备份恢复结果，并结合日志分析备份和恢复流程是否正常。

## 常见问题说明

### 在“应用及数据”页面没有找到待测试应用

**问题现象**

在“应用及数据”页面勾选应用时，找不到待测试应用。

**可能原因**

备份侧设备没有安装待测试应用。

**解决措施**

在备份侧设备安装待测试应用。

### 迁移结果显示“仅克隆应用，不迁移数据”

**问题现象**

克隆结束后，迁移结果显示“仅克隆应用，不迁移数据”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/zphL6K_MSDmUo6yZOx26lA/zh-cn_image_0000002583438309.png?HW-CC-KV=V1&HW-CC-Date=20260427T234112Z&HW-CC-Expire=86400&HW-CC-Sign=CB0A33CC560238201BFFD2E570467A81EC6974E96FE01DEC45BE7F20F50180F4)

**可能原因**

onBackup/onBackupEx未按照规范实现。

**解决措施**

请排查是否符合[应用接入数据备份恢复](app-file-backup-extension.md)规范，并结合日志分析onBackup/onBackupEx执行流程。

### 迁移结果显示“应用数据恢复失败”

**问题现象**

克隆结束后，迁移结果显示“应用数据恢复失败”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/F8f-n7G7T_uIxzj-1g8fnA/zh-cn_image_0000002552958264.png?HW-CC-KV=V1&HW-CC-Date=20260427T234112Z&HW-CC-Expire=86400&HW-CC-Sign=B2C610B7D0559103A916FE0E033BADC1C4353245151138F4B79CF3498AC1D0FD)

**可能原因**

1. 恢复侧设备未安装待测试应用。
2. onRestore/onRestoreEx未按照规范实现。

**解决措施**

1. 在恢复侧设备安装待测试应用。
2. 请排查是否符合[应用接入数据备份恢复](app-file-backup-extension.md)规范，并结合日志分析onRestore/onRestoreEx执行流程。
