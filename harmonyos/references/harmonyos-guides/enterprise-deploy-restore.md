---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/enterprise-deploy-restore
title: 企业场景下的数据备份与还原
breadcrumb: 指南 > 系统 > 基础功能 > Enterprise Foundation Kit（企业办公开发服务） > 企业场景下的数据备份与还原
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:48+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:4b8c364ad0f33a87946f275f0ea4f77253d6b932705b936ba6f4795ae8b0b136
---

从API版本26.0.1开始，新增企业批量部署还原能力。

该能力提供查询待备份用户数据大小、用户数据备份、用户数据还原、查询可备份应用列表、查询待备份应用沙箱数据大小、备份应用沙箱数据、还原应用沙箱数据以及取消备份还原操作的功能，支持企业普通应用和企业MDM应用完成应用沙箱数据和用户数据的备份与还原。

## 场景介绍

支持企业场景的应用沙箱数据和用户数据的备份或还原。

## 接口说明

详细接口说明可参考[接口文档](../harmonyos-references/enterprise-foundation.md)。

| 接口名 | 描述 |
| --- | --- |
| [getUserBackupDataSize](../harmonyos-references/enterprise-foundation.md#getuserbackupdatasize)(): Promise<number> | 获取待备份用户的数据量大小。使用Promise异步回调。 |
| [backupUserData](../harmonyos-references/enterprise-foundation.md#backupuserdata)(dest: string, progressCallback: [BackupRestoreProgressCallback](../harmonyos-references/enterprise-foundation.md#backuprestoreprogresscallback)): Promise<void> | 备份用户数据，使用Promise异步回调。 |
| [restoreUserData](../harmonyos-references/enterprise-foundation.md#restoreuserdata)(src: string, progressCallback: BackupRestoreProgressCallback, options?: [RestoreUserDataOptions](../harmonyos-references/enterprise-foundation.md#restoreuserdataoptions)): Promise<void> | 还原用户数据，使用Promise异步回调。 |
| [getAllowedBackupAndRestoreBundleList](../harmonyos-references/enterprise-foundation.md#getallowedbackupandrestorebundlelist)(): Promise<[BundleInfo](../harmonyos-references/enterprise-foundation.md#bundleinfo)[]> | 获取可备份或还原的应用信息列表，使用Promise异步回调。 |
| [getBundlesBackupDataSize](../harmonyos-references/enterprise-foundation.md#getbundlesbackupdatasize)(bundleList: string[]): Promise<number> | 获取待备份的应用沙箱数据量大小，使用Promise异步回调。 |
| [backupBundles](../harmonyos-references/enterprise-foundation.md#backupbundles)(bundleList: string[], dest: string, progressCallback: BackupRestoreProgressCallback): Promise<void> | 备份应用沙箱数据，使用Promise异步回调。 |
| [restoreBundles](../harmonyos-references/enterprise-foundation.md#restorebundles)(bundleList: string[], src: string, progressCallback: BackupRestoreProgressCallback): Promise<void> | 还原应用沙箱数据，使用Promise异步回调。 |
| [cancelBackupRestore](../harmonyos-references/enterprise-foundation.md#cancelbackuprestore)(): Promise<void> | 取消备份或还原操作，使用Promise异步回调。 |

## 申请权限

在申请权限前，请保证符合[权限使用的基本原则](app-permission-mgmt-overview.md#权限使用的基本原则)。并且在工程模块对应的[module.json5配置文件](module-configuration-file.md)中requestPermissions标签下声明所需的权限。申请权限ohos.permission.ENTERPRISE\_MANAGE\_BACKUP，该能力受限开放，仅支持企业普通应用和企业MDM应用接入。

示例：

```json
{
  "requestPermissions": [
    {
      "name": "ohos.permission.ENTERPRISE_MANAGE_BACKUP"
    }
  ]
}
```

## 开发步骤

1. 导入模块。

   ```typescript
   import { enterpriseDeployRestore } from '@kit.EnterpriseFoundationKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { common } from '@kit.AbilityKit';
   import { fileIo as fs } from '@kit.CoreFileKit';
   import { hilog } from '@kit.PerformanceAnalysisKit';
   ```
2. 在待备份设备，调用接口[backupUserData](../harmonyos-references/enterprise-foundation.md#backupuserdata)，备份用户数据。

   用户数据备份内容不包含“图片”目录中的“图库”，如果需要备份“图库”里的数据，需要通过备份应用沙箱数据接口实现。
3. 在待备份设备，调用接口[getAllowedBackupAndRestoreBundleList](../harmonyos-references/enterprise-foundation.md#getallowedbackupandrestorebundlelist)，获取可备份或还原的应用信息列表。
4. 在待备份设备，调用接口[getBundlesBackupDataSize](../harmonyos-references/enterprise-foundation.md#getbundlesbackupdatasize)，获取待备份的应用沙箱数据量大小。
5. 在待备份设备，调用接口[backupBundles](../harmonyos-references/enterprise-foundation.md#backupbundles)，备份指定应用的沙箱数据。指定应用沙箱数据的备份路径清单:

   ```typescript
   "data/storage/el1/database/",
   "data/storage/el1/base/files/",
   "data/storage/el1/base/preferences/",
   "data/storage/el1/base/haps/*/files/",
   "data/storage/el1/base/haps/*/preferences/",
   "data/storage/el2/database/",
   "data/storage/el2/base/files/",
   "data/storage/el2/base/preferences/",
   "data/storage/el2/base/haps/*/files/",
   "data/storage/el2/base/haps/*/preferences/",
   "data/storage/el2/distributedfiles/",
   "data/storage/el5/database/",
   "data/storage/el5/base/files/",
   "data/storage/el5/base/preferences/",
   "data/storage/el5/base/haps/*/files/",
   "data/storage/el5/base/haps/*/preferences/"
   ```
6. 在待还原设备，调用接口[restoreUserData](../harmonyos-references/enterprise-foundation.md#restoreuserdata)，将备份的用户数据还原到该设备。

   用户数据还原内容不包含“图片”目录中的“图库”，如果需要还原“图库”里的数据，需要通过还原应用沙箱数据接口实现。
7. 在待还原设备，调用接口[restoreBundles](../harmonyos-references/enterprise-foundation.md#restorebundles)，将备份的应用沙箱数据还原到该设备。
8. 在备份或还原操作过程中，调用接口[cancelBackupRestore](../harmonyos-references/enterprise-foundation.md#cancelbackuprestore)，可以取消当前的备份或还原操作。
9. 在待备份设备，调用接口[getUserBackupDataSize](../harmonyos-references/enterprise-foundation.md#getuserbackupdatasize)，获取待备份的用户数据量大小。
