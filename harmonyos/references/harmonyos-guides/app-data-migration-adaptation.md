---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-data-migration-adaptation
title: 应用数据迁移适配指导
breadcrumb: 指南 > 应用框架 > Core File Kit（文件基础服务） > 应用文件 > 应用数据备份恢复 > 设备升级应用数据迁移适配指导 > 应用数据迁移适配指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:14+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fa6415e4b8ce38567e3ca3496f7e1b60057c4a3f4ad1b1d8153ed98f10ba7b60
---

## 环境准备

开发者需要通过OTA升级的形式，将终端设备升级到HarmonyOS NEXT Developer Beta1及之后版本。

| 工具 | 版本 | 说明 |
| --- | --- | --- |
| “迁移调试”工具 | 205.0.0.115及之后版本 | 模拟验证数据迁移 |
| DevEco Studio | DevEco Studio NEXT Developer Beta3及之后版本 | 请参考：[DevEco Studio使用指南](ide-tools-overview.md)。 |
| Compatible SDK | 5.0.0(12) | 请参考：[版本说明](../harmonyos-releases/overview-allversion.md)。 |

## 应用数据迁移适配流程

### 创建新工程

本章节从[创建新工程](ide-create-new-project.md)开始，指导开发者接入“备份恢复框架”，已经创建工程的开发者可以跳过本节。

### BackupExtensionAbility的实现

开发者可以在BackupExtension.ts文件中自定义类继承BackupExtensionAbility，通过重写其中的onBackup和onRestore方法，自定义应用数据的转换和迁移。终端设备从HarmonyOS升级到HarmonyOS NEXT数据迁移场景中，onRestore回调接口中的参数**bundleVersion.name**的**前缀**为“**0.0.0.0**”。

注意

**onRestore 接口是同步接口，其内部所有的异步操作请进行同步等待。**

以下步骤以空工程为例，介绍如何实现BackupExtensionAbility：

1. 在**entry/src/main/ets/**目录下，点击 **New > Directory** 创建**backupExtension**目录。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/nWIZLheHRkOU1_grZmfJ5A/zh-cn_image_0000002583438313.png?HW-CC-KV=V1&HW-CC-Date=20260427T234113Z&HW-CC-Expire=86400&HW-CC-Sign=14B2310C6D9D8BE402392FE45A3BF09F0309D3AA07CD1FE3CA4DDF821D53B356)
2. 点击**entry/src/main/ets/backupExtension/**目录，点击 **New > File** 创建**BackupExtension.ets**文件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/dLE-XesNTkyoWIa81OtSiQ/zh-cn_image_0000002552958268.png?HW-CC-KV=V1&HW-CC-Date=20260427T234113Z&HW-CC-Expire=86400&HW-CC-Sign=B6D2DFC80E2681073A1E7D1F9339727E29D2E6BC5042EF4AC5678037B6699760)
3. 参考示例代码实现BackupExtensionAbility，应用的数据转换和迁移逻辑，请在指定位置填充实现。

   终端设备从HarmonyOS升级到HarmonyOS NEXT中，会将原有APK应用沙箱目录中文件放置到HarmonyOS备份恢复目录。对应关系详见[APK应用沙箱目录与备份恢复目录映射关系](app-data-migration-adaptation.md#apk应用沙箱目录与备份恢复目录映射关系)。

   ```
   1. import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';

   3. const TAG = `EntryBackupAbility`;

   5. /**
   6. * serviceExt进程入口
   7. */
   8. export default class EntryBackupAbility extends  BackupExtensionAbility {
   9. async onBackup () {
   10. console.info(TAG,`onBackup ok`);
   11. await Promise.resolve();
   12. }

   14. /**
   15. * 数据恢复处理接口。接口是同步接口，其内部所有的异步操作请进行同步等待。
   16. *
   17. * @param bundleVersion 版本信息
   18. */
   19. async onRestore (bundleVersion : BundleVersion): Promise<void> {
   20. console.info(TAG, `onRestore ok ${JSON.stringify(bundleVersion)}`);
   21. //bundleVersion.name的前缀为“0.0.0.0”时，表示终端设备从HarmonyOS升级到HarmonyOS NEXT数据迁移场景
   22. if (bundleVersion.name.startsWith("0.0.0.0")){
   23. // 在此处实现终端设备从HarmonyOS 4.x升级到HarmonyOS NEXT后，应用数据的转换和迁移
   24. // 涉及异步操作请进行同步等待
   25. console.info(TAG, `HarmonyOS to HarmonyOS NEXT scenario`);
   26. } else {
   27. // 在此处实现从HarmonyOS NEXT设备迁移到HarmonyOS NEXT设备后，应用数据的处理。无特殊要求，可以空实现
   28. // 涉及异步操作请进行同步等待
   29. console.info(TAG, `Other scenario`);
   30. }
   31. }
   32. }
   ```

   注意

   1. 单个应用设定的最长数据迁移时间为十五分钟，超过十五分钟还未完成应用数据迁移的应用，应用数据迁移会失败。
   2. 应用的“BackupExtensionAbility”执行完后，“备份恢复框架”会清空备份恢复目录，开发者请在应用的“BackupExtensionAbility”执行结束前，完成所有所需数据的转换和迁移。

### 元数据资源配置文件适配

开发者通过元数据资源配置文件backup\_config.json，启用备份恢复，并定义备份恢复框架需要传输的文件。

以下步骤以空工程为例，介绍如何配置元数据资源文件：

1. 在**entry/src/main/resources/base/profile/**目录下，点击 **New > File** 创建**backup\_config.json**文件。
2. 参考示例代码实现元数据资源文件配置。

   ```
   1. {
   2. "allowToBackupRestore": true,
   3. "extraInfo": {
   4. "supportScene": [
   5. "hmos2next"
   6. ]
   7. }
   8. }
   ```

### module.json5适配

开发者需要在应用配置文件module.json5中进行注册，其中注册类型type需要设置为backup，元数据信息metadata需要新增一个name为ohos.extension.backup的条目。

注意

**extensionAbilities需要配置在entry内的module.json5才能正常访问。**

以下步骤以空工程为例，介绍如何配置[module.json5](module-configuration-file.md#extensionabilities标签)文件：

1. 开发者需要在entry内的module.json5里面进行注册,参考示例代码实现元数据资源文件配置。

   ```
   1. "extensionAbilities": [
   2. {
   3. "description": "DemoBackupExtension",
   4. "icon": "$media:app_icon",
   5. "name": "BackupExtensionAbility",
   6. "srcEntry": "./ets/backupExtension/BackupExtension.ets",  // 对应BackupExtension.ets在代码仓中的位置
   7. "type": "backup",                                         // 类型需要选择backup
   8. "exported": false,
   9. "metadata": [                                             // 对应注册的元数据资源
   10. {
   11. "name": "ohos.extension.backup",
   12. "resource": "$profile:backup_config"
   13. }
   14. ]
   15. }
   16. ]
   ```

## APK应用沙箱目录与备份恢复目录映射关系

APK应用沙箱目录与备份恢复目录映射关系见下表中所示：

| APK应用沙箱目录 | 备份恢复目录示例 | 备份恢复目录获取方式 |
| --- | --- | --- |
| /data/user\_de/{userId}/{APK包名}/ | /data/storage/el1/base/.backup/restore/{APK包名}/de/ | this.context.area = contextConstant.AreaMode.EL1;  let deSourcePath = this.context.backupDir + "restore/{APK包名}/de/" |
| /data/user/{userId}/{APK包名}/ | /data/storage/el2/base/.backup/restore/{APK包名}/ce/ | this.context.area = contextConstant.AreaMode.EL2;  let ceSourcePath = this.context.backupDir + "restore/{APK包名}/ce/" |
| /data/media/{userId}/Android/data/{APK包名}/ | /data/storage/el2/base/.backup/restore/{APK包名}/A/data/ | this.context.area = contextConstant.AreaMode.EL2;  let dataSourcePath = this.context.backupDir + "restore/{APK包名}/A/data/" |
| /data/media/{userId}/Android/obb/{APK包名}/ | /data/storage/el2/base/.backup/restore/{APK包名}/A/obb/ | this.context.area = contextConstant.AreaMode.EL2;  let obbSourcePath = this.context.backupDir + "restore/{APK包名}/A/obb/" |
