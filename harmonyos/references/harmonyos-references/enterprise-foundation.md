---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/enterprise-foundation
title: "@hms.pcService.enterpriseDeployRestore (企业场景下的数据备份与还原)"
breadcrumb: API参考 > 系统 > 基础功能 > Enterprise Foundation Kit（企业办公开发服务） > ArkTS API > @hms.pcService.enterpriseDeployRestore (企业场景下的数据备份与还原)
category: harmonyos-references
scraped_at: 2026-11-12T09:55:59+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:f5a61a00f9bc9c38ccc8bf8a54aca7d87cf5b8df7b1f811213a1f2638f1a317b
---

本模块提供企业批量部署还原能力，包括用户数据备份、用户数据还原、应用沙箱数据备份、应用沙箱数据还原等。

**起始版本：** 26.0.1

## 导入模块

```typescript
import { enterpriseDeployRestore } from '@kit.EnterpriseFoundationKit';
```

## BundleInfo

可备份或还原应用的信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.EnterpriseDeployRestore

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 应用包名。 |
| versionCode | number | 否 | 否 | 应用包的版本号，对应[app.json5](../harmonyos-guides/app-configuration-file.md)中配置的versionCode字段。 |
| versionName | string | 否 | 否 | 应用包的版本文本描述信息。 |

## BackupRestoreProgressInfo

备份或还原的进度信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.EnterpriseDeployRestore

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| progress | number | 否 | 否 | 备份或还原的进度。 |

## BackupRestoreProgressCallback

type BackupRestoreProgressCallback = (progressInfo: BackupRestoreProgressInfo) => void

备份或还原进度回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.EnterpriseDeployRestore

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| progressInfo | [BackupRestoreProgressInfo](enterprise-foundation.md#backuprestoreprogressinfo) | 是 | 备份或还原的进度信息。 |

## DirectoryIdentifier

目录标识符枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.EnterpriseDeployRestore

**起始版本：** 26.0.1

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DOCUMENTS | 0 | 表示“文档”目录。 |
| DOWNLOAD | 1 | 表示“下载”目录。 |

## RestoreUserDataOptions

还原用户数据的配置项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.EnterpriseDeployRestore

**起始版本：** 26.0.1

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| excludeDirIdentifiers | [DirectoryIdentifier](enterprise-foundation.md#directoryidentifier)[] | 否 | 是 | 还原用户数据时，表示选择禁止还原目录的标识符。默认为还原所有目录。 |

## backupUserData

backupUserData(dest: string, progressCallback: BackupRestoreProgressCallback):Promise<void>

备份用户数据。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BACKUP

**系统能力：** SystemCapability.PCService.EnterpriseDeployRestore

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| progressCallback | [BackupRestoreProgressCallback](enterprise-foundation.md#backuprestoreprogresscallback) | 是 | 备份进度的回调。注意：回调接口中不能处理耗时业务。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。当备份用户数据失败时会抛出错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-foundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1029200001 | The enterprise batch deploy restore service is not started. |
| 1029200002 | The enterprise batch deploy restore service is busy. |
| 1029200004 | The backup or restore operation was canceled by the user. |
| 1029200005 | No such directory. |
| 1029200006 | Not a directory. |
| 1029200007 | The enterprise batch deploy restore service is abnormal.Possible causes: File operation exception. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import enterpriseDeployRestore from '@hms.pcService.enterpriseDeployRestore';

// “/userData”为示例目标目录，根据实际情况进行替换
let destPath = context.filesDir + "/userData";
let progressCallback: enterpriseDeployRestore.BackupRestoreProgressCallback =
    (progressInfo: enterpriseDeployRestore.BackupRestoreProgressInfo) => {
    console.info(`Progress: ${progressInfo.progress}`);
};

enterpriseDeployRestore.backupUserData(destPath, progressCallback).then(() => {
    console.info('Succeeded in backing up user data.');
}).catch((err: BusinessError) => {
    console.error(`Failed to back up user data. Code: ${err.code}, Message: ${err.message}.`);
});
```

## restoreUserData

restoreUserData(src: string, progressCallback: BackupRestoreProgressCallback, options?: RestoreUserDataOptions):Promise<void>

还原用户数据。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BACKUP

**系统能力：** SystemCapability.PCService.EnterpriseDeployRestore

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| src | string | 是 | 源目录的应用沙箱路径。 |
| progressCallback | [BackupRestoreProgressCallback](enterprise-foundation.md#backuprestoreprogresscallback) | 是 | 还原进度的回调。注意：回调接口中不能处理耗时业务。 |
| options | [RestoreUserDataOptions](enterprise-foundation.md#restoreuserdataoptions) | 否 | 还原用户数据的可选配置项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。当还原用户数据失败时会抛出错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-foundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1029200001 | The enterprise batch deploy restore service is not started. |
| 1029200002 | The enterprise batch deploy restore service is busy. |
| 1029200004 | The backup or restore operation was canceled by the user. |
| 1029200005 | No such directory. |
| 1029200006 | Not a directory. |
| 1029200007 | The enterprise batch deploy restore service is abnormal.Possible causes: File operation exception. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import enterpriseDeployRestore from '@hms.pcService.enterpriseDeployRestore';

// “/userData”为示例源目录，根据实际情况进行替换
let srcPath = context.filesDir + "/userData";
let progressCallback: enterpriseDeployRestore.BackupRestoreProgressCallback =
    (progressInfo: enterpriseDeployRestore.BackupRestoreProgressInfo) => {
    console.info(`Progress: ${progressInfo.progress}`);
};

enterpriseDeployRestore.restoreUserData(srcPath, progressCallback).then(() => {
    console.info('Succeeded in restoring user data.');
}).catch((err: BusinessError) => {
    console.error(`Failed to restore user data. Code: ${err.code}, Message: ${err.message}.`);
});
```

## getUserBackupDataSize

getUserBackupDataSize():Promise<number>

获取待备份用户的数据量大小。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BACKUP

**系统能力：** SystemCapability.PCService.EnterpriseDeployRestore

**起始版本：** 26.0.1

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回待备份用户数据的数据量大小。单位：Byte。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-foundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1029200001 | The enterprise batch deploy restore service is not started. |
| 1029200002 | The enterprise batch deploy restore service is busy. |
| 1029200007 | The enterprise batch deploy restore service is abnormal.Possible causes: File operation exception. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import enterpriseDeployRestore from '@hms.pcService.enterpriseDeployRestore';

enterpriseDeployRestore.getUserBackupDataSize().then((totalSize: number) => {
    console.info(`Size: ${totalSize}`);
}).catch((err: BusinessError) => {
    console.error(`Failed to get data size. Code: ${err.code}, Message: ${err.message}.`);
});
```

## getAllowedBackupAndRestoreBundleList

getAllowedBackupAndRestoreBundleList():Promise<BundleInfo[]>

获取可备份或还原的应用信息列表。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BACKUP

**系统能力：** SystemCapability.PCService.EnterpriseDeployRestore

**起始版本：** 26.0.1

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<BundleInfo[]> | Promise对象，返回可备份或还原的应用信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-foundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1029200001 | The enterprise batch deploy restore service is not started. |
| 1029200007 | The enterprise batch deploy restore service is abnormal.Possible causes: File operation exception. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import enterpriseDeployRestore from '@hms.pcService.enterpriseDeployRestore';

enterpriseDeployRestore.getAllowedBackupAndRestoreBundleList().then((result: Array<enterpriseDeployRestore.BundleInfo>) => {
    console.info('Succeeded in getting backup and restore bundle list.');
}).catch((err: BusinessError) => {
    console.error(`Failed to get backup and restore bundle list. Code:${err.code}, Message:${err.message}.`);
});
```

## backupBundles

backupBundles(bundleList: string[], dest: string, progressCallback: BackupRestoreProgressCallback):Promise<void>

备份应用沙箱数据。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BACKUP

**系统能力：** SystemCapability.PCService.EnterpriseDeployRestore

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleList | string[] | 是 | 待备份的应用包列表。 |
| dest | string | 是 | 目标目录的应用沙箱路径。 |
| progressCallback | [BackupRestoreProgressCallback](enterprise-foundation.md#backuprestoreprogresscallback) | 是 | 备份进度的回调。注意：回调接口中不能处理耗时业务。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。当备份应用沙箱数据失败时会抛出错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-foundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1029200001 | The enterprise batch deploy restore service is not started. |
| 1029200002 | The enterprise batch deploy restore service is busy. |
| 1029200004 | The backup or restore operation was canceled by the user. |
| 1029200005 | No such directory. |
| 1029200006 | Not a directory. |
| 1029200007 | The enterprise batch deploy restore service is abnormal.Possible causes: File operation exception. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import enterpriseDeployRestore from '@hms.pcService.enterpriseDeployRestore';

let bundleInfoList: enterpriseDeployRestore.BundleInfo[] =
  await enterpriseDeployRestore.getAllowedBackupAndRestoreBundleList();
let bundleNameList: string[] = [];
bundleInfoList.forEach((bundleInfo: enterpriseDeployRestore.BundleInfo) => {
  bundleNameList.push(bundleInfo.bundleName);
})

// “/appData”为示例目标目录，根据实际情况进行替换
let destPath = context.filesDir + "/appData";
let progressCallback: enterpriseDeployRestore.BackupRestoreProgressCallback =
    (progressInfo: enterpriseDeployRestore.BackupRestoreProgressInfo) => {
    console.info(`Progress: ${progressInfo.progress}`);
};
        
enterpriseDeployRestore.backupBundles(bundleNameList, destPath, progressCallback).then(() => {
    console.info('Succeeded in backing up bundles.');
}).catch((err: BusinessError) => {
    console.error(`Failed to back up bundles. Code: ${err.code}, Message: ${err.message}.`);
});
```

## restoreBundles

restoreBundles(bundleList: string[], src: string, progressCallback: BackupRestoreProgressCallback):Promise<void>

还原应用沙箱数据。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BACKUP

**系统能力：** SystemCapability.PCService.EnterpriseDeployRestore

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleList | string[] | 是 | 待还原的应用包列表。 |
| src | string | 是 | 源目录的应用沙箱路径。 |
| progressCallback | [BackupRestoreProgressCallback](enterprise-foundation.md#backuprestoreprogresscallback) | 是 | 还原进度的回调。注意：回调接口中不能处理耗时业务。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。当还原应用沙箱数据失败时会抛出错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-foundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1029200001 | The enterprise batch deploy restore service is not started. |
| 1029200002 | The enterprise batch deploy restore service is busy. |
| 1029200004 | The backup or restore operation was canceled by the user. |
| 1029200005 | No such directory. |
| 1029200006 | Not a directory. |
| 1029200007 | The enterprise batch deploy restore service is abnormal.Possible causes: File operation exception. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import enterpriseDeployRestore from '@hms.pcService.enterpriseDeployRestore';

let bundleInfoList: enterpriseDeployRestore.BundleInfo[] =
  await enterpriseDeployRestore.getAllowedBackupAndRestoreBundleList();
let bundleNameList: string[] = [];
bundleInfoList.forEach((bundleInfo: enterpriseDeployRestore.BundleInfo) => {
  bundleNameList.push(bundleInfo.bundleName);
})

// “/appData”为示例源目录，根据实际情况进行替换
let srcPath = context.filesDir + "/appData";
let progressCallback: enterpriseDeployRestore.BackupRestoreProgressCallback =
    (progressInfo: enterpriseDeployRestore.BackupRestoreProgressInfo) => {
    console.info(`Progress: ${progressInfo.progress}`);
};

enterpriseDeployRestore.restoreBundles(bundleNameList, srcPath, progressCallback).then(() => {
    console.info('Succeeded in restoring bundles.');
}).catch((err: BusinessError) => {
    console.error(`Failed to restore bundles. Code: ${err.code}, Message: ${err.message}.`);
});
```

## getBundlesBackupDataSize

getBundlesBackupDataSize(bundleList: string[]):Promise<number>

获取待备份的应用沙箱数据量大小。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BACKUP

**系统能力：** SystemCapability.PCService.EnterpriseDeployRestore

**起始版本：** 26.0.1

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleList | string[] | 是 | 待备份的应用包列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回待备份应用沙箱数据的数据量大小。单位：Byte。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-foundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1029200001 | The enterprise batch deploy restore service is not started. |
| 1029200002 | The enterprise batch deploy restore service is busy. |
| 1029200007 | The enterprise batch deploy restore service is abnormal.Possible causes: File operation exception. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import enterpriseDeployRestore from '@hms.pcService.enterpriseDeployRestore';

let bundleInfoList: enterpriseDeployRestore.BundleInfo[] =
  await enterpriseDeployRestore.getAllowedBackupAndRestoreBundleList();
let bundleNameList: string[] = [];
bundleInfoList.forEach((bundleInfo: enterpriseDeployRestore.BundleInfo) => {
  bundleNameList.push(bundleInfo.bundleName);
})

enterpriseDeployRestore.getBundlesBackupDataSize(bundleNameList).then((totalSize: number) => {
    console.info(`Size: ${totalSize}`);
}).catch((err: BusinessError) => {
    console.error(`Failed to get data size. Code: ${err.code}, Message: ${err.message}.`);
});
```

## cancelBackupRestore

cancelBackupRestore():Promise<void>

取消备份或还原操作。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ENTERPRISE\_MANAGE\_BACKUP

**系统能力：** SystemCapability.PCService.EnterpriseDeployRestore

**起始版本：** 26.0.1

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。当取消备份或还原操作失败时会抛出错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-enterprise-foundation.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1029200001 | The enterprise batch deploy restore service is not started. |
| 1029200003 | No backup or restore task in progress. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import enterpriseDeployRestore from '@hms.pcService.enterpriseDeployRestore';

enterpriseDeployRestore.cancelBackupRestore().then(() => {
    console.info('Succeeded in cancelling backup or restore.');
}).catch((err: BusinessError) => {
    console.error(`Failed to cancel backup or restore. Code: ${err.code}, Message: ${err.message}.`);
});
```
