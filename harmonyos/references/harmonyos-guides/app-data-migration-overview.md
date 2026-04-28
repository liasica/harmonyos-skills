---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-data-migration-overview
title: 应用数据迁移功能介绍
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 应用数据迁移功能介绍
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:95b2fe1942b6f3970002b485fc727de61592b2dab53e391290edb994efc2ca22
---

## 使用场景

终端设备从HarmonyOS 3.1 Release API 9及之前版本（简称HarmonyOS）升级到HarmonyOS NEXT Developer Preview1及之后版本（简称HarmonyOS NEXT）时，原HarmonyOS中运行的APK应用，升级后需要切换为HarmonyOS NEXT中的HarmonyOS应用。APK应用的部分数据需要转换并迁移到指定位置后，才能被HarmonyOS应用访问。HarmonyOS NEXT提供了“数据迁移框架”和“备份恢复框架”，为开发者提供应用数据的迁移和转换能力。开发者完成适配，APK应用切换为HarmonyOS应用后，可继承原APK应用中适配HarmonyOS应用的数据。

如下图所示，应用需要的数据，包含云端服务器中的数据，本地应用沙箱中的数据和本地公共媒体库中的数据。为了应用的数据可以继承，开发者需要保证云端数据定义兼容APK应用和HarmonyOS应用，确保系统升级后同一账号下的数据可识别。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/fbtj9_rGQIu2h0jWNBFUYg/zh-cn_image_0000002552798616.png?HW-CC-KV=V1&HW-CC-Date=20260427T234113Z&HW-CC-Expire=86400&HW-CC-Sign=3F5DDE7A9EDF8587B132518778853CC0E4B4761C1B8F5BA30613E74E949E70E4)

## 数据迁移机制

### 应用沙箱数据迁移机制

终端设备从HarmonyOS升级到HarmonyOS NEXT后，APK应用沙箱数据被搬迁到中间目录。针对应用沙箱数据，HarmonyOS NEXT提供“数据迁移框架”统一调度应用数据迁移任务。

应用数据迁移任务需要执行的步骤包括：应用安装，数据迁移和数据恢复。

1. **应用安装步骤：**

   1. “数据迁移框架”向华为应用市场发送HarmonyOS应用下载和安装请求。
   2. 华为应用市场下载并安装HarmonyOS应用。
2. **数据迁移步骤：**

   在HarmonyOS应用安装完成之后，“数据迁移框架”将应用沙箱数据从中间目录搬迁到备份恢复目录。
3. **数据恢复步骤：**

   1. 在应用数据搬迁到备份恢复目录后，“数据迁移框架”向“备份恢复框架”发送应用数据恢复请求。
   2. “备份恢复框架”拉起应用的“BackupExtensionAbility”独立进程，启动应用数据恢复。
   3. 应用通过“BackupExtensionAbility”从备份恢复目录加载APK应用的数据，处理后保存到HarmonyOS应用沙箱中，完成应用数据恢复。
   4. “备份恢复框架”在应用数据恢复完成后，清空备份恢复目录。

后续HarmonyOS应用通过访问HarmonyOS应用沙箱获取应用的数据。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/VXlTNWG_SOCShygNeaolNw/zh-cn_image_0000002583438311.png?HW-CC-KV=V1&HW-CC-Date=20260427T234113Z&HW-CC-Expire=86400&HW-CC-Sign=0FBDF25923706AB51788F5C34762747DC035845E9B6F8AE36D4663E784A72047)

### 公共媒体库中数据迁移机制

公共媒体库中的数据，在终端设备从HarmonyOS升级到HarmonyOS NEXT后，会整体搬迁直接继承。应用可以使用HarmonyOS NEXT提供的API，访问公共媒体库中的数据。媒体库的使用指导可以参考：[媒体文件管理服务](photoaccesshelper-overview.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/Lzlma4mGSACS4BdKfmmraQ/zh-cn_image_0000002552958266.png?HW-CC-KV=V1&HW-CC-Date=20260427T234113Z&HW-CC-Expire=86400&HW-CC-Sign=A8EC5E6A5E94260EDE9C5AD4A762819693E60C9F4730392F7344260E7DF5555B)
