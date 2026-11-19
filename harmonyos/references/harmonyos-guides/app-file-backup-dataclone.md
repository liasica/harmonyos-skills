---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-file-backup-dataclone
title: 应用数据备份恢复验证指导
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 应用数据备份恢复验证指导
category: harmonyos-guides
scraped_at: 2026-11-19T09:47:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c99bf0f794fb49c44e653c9cdbb3693a89deb95c37cefa62a5223cff1c232844
---

为方便开发者验证[应用接入数据备份恢复](app-file-backup-extension.md)结果，此篇指南介绍了在鸿蒙设备上通过数据克隆应用触发数据备份恢复，以及常见问题说明。

## 环境准备

* 调试设备：两部鸿蒙设备，系统版本在HarmonyOS 6.0.0.115及以上，数据克隆版本在6.0.0.516及以上。
* 安装应用：两部设备都要安装待测试应用。

## 触发数据备份恢复

1. 打开数据克隆应用，一部设备选择“这是新设备”，作为数据恢复侧，另一部设备选择“这是旧设备”，作为数据备份侧，按照提示连接两部设备。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/lMsXpJVdQKefoKivvTfTYQ/zh-cn_image_0000002791725522.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=B40768562A11B0C8AE813E152977A07C11264ADDBBD3BDBC8A1A56386E63337F)
2. 在选择数据页面，点击应用及数据，勾选待测试应用。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/Pf2xBs7VSvGbGKhXf9al1w/zh-cn_image_0000002791565550.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=0794F33FCE7B1B3BF914C9A66D9E7CBF45C0FEA8BCA381DA05047D69DC962956)
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/3evqVQtuT2eCmBzBJotkNA/zh-cn_image_0000002820525503.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=1BB9B4D66FC9841D99251CF93F50477D9F86CA70447A5BB531E56AFE365C3B82)

**可能原因**

onBackup/onBackupEx未按照规范实现。

**解决措施**

请排查是否符合[应用接入数据备份恢复](app-file-backup-extension.md)规范，并结合日志分析onBackup/onBackupEx执行流程。

### 迁移结果显示“应用数据恢复失败”

**问题现象**

克隆结束后，迁移结果显示“应用数据恢复失败”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/I4ULNvcOR5K5Fjh1Hx4kjA/zh-cn_image_0000002820405503.png?HW-CC-KV=V1&HW-CC-Date=20261119T014754Z&HW-CC-Expire=31536000000&HW-CC-Sign=064D30C5A5B567F412BC180EA54C7C6202F740D224B4EFF5D8BDC899C2A3037F)

**可能原因**

1. 恢复侧设备未安装待测试应用。
2. onRestore/onRestoreEx未按照规范实现。

**解决措施**

1. 在恢复侧设备安装待测试应用。
2. 请排查是否符合[应用接入数据备份恢复](app-file-backup-extension.md)规范，并结合日志分析onRestore/onRestoreEx执行流程。
