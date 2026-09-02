---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/dataguard-fileguard
title: fileGuard (文件分级管控)
breadcrumb: API参考 > 系统 > 安全 > Enterprise Data Guard Kit（企业数据保护服务） > ArkTS API > fileGuard (文件分级管控)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:afb47be1fa61e25ac47b5f99203c547d40fcf0907f6aa467b71a276a9a5f6cbe
---

文件分级管控为企业安全管控类[MDM](../harmonyos-guides/mdm-kit.md)应用提供统一企业关键信息资产（KIA）文件的识别和外发管控能力，保证企业数据安全。功能包括扫描全盘目录下的文档，识别KIA文件，并管控KIA文件通过网络发送到非可信网段。

仅供企业安全管控类MDM应用申请权限后使用。

**起始版本：** 4.0.0(10)

## 导入模块

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
```

## CommonDirScanType

公共目录扫描类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MEDIA\_ONLY | 0 | 表示媒体库目录。 |
| MEDIA\_AND\_SANDBOX | 1 | 表示媒体库和沙箱目录。 |

## SecurityLevel

文件安全等级枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | -1 | 表示文件安全等级不生效。  **起始版本：** 5.1.1(19) |
| EXTERNAL | 0 | 表示文件安全等级为外部公开。 |
| INTERNAL | 1 | 表示文件安全等级为内部公开。 |
| SECRET | 2 | 表示文件安全等级为秘密。 |
| CONFIDENTIAL | 3 | 表示文件安全等级为机密。 |
| TOP\_SECRET | 4 | 表示文件安全等级为绝密。 |

## AuthenticateKeyType

HDC认证的密钥类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 6.1.1(24)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PUBLIC\_KEY | 0 | 表示HDC认证的密钥类型为公钥。 |
| PRIVATE\_KEY | 1 | 表示HDC认证的密钥类型为私钥。 |

## AuthenticateDeviceType

HDC认证的设备类型枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 6.1.1(24)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UPPER | 0 | 表示HDC认证的设备类型为上位机。 |
| LOWER | 1 | 表示HDC认证的设备类型为下位机。 |

## ManagedProcessStatus

进程管控策略状态枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 26.0.0

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TIME\_BASED | 0 | 表示该进程按时间管控。 |
| LIFE\_LONG | 1 | 表示该进程按全生命周期持久化管控。 |

## ManagedProcessPolicy

表示进程管控策略。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| status | [ManagedProcessStatus](dataguard-fileguard.md#managedprocessstatus) | 否 | 否 | 表示进程管控策略状态。 |
| time | number | 否 | 是 | 用于统一设置所有策略的管控时长，当设置该时长后，基于[updatePolicy](dataguard-fileguard.md#updatepolicy)设置的时长将不再生效。当status为LIFE\_LONG时非必选，默认为undefined，设置管控时长不生效；当status为TIME\_BASED时必选，单位：ms，取值范围：(0, 86400000)。 |

## ManagedProcessInfo

表示进程管控信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pid | number | 否 | 否 | 表示进程的PID。 |
| policy | string | 否 | 是 | 表示管控策略类别。6种固定取值：KIA，TAG1~TAG5，不区分大小写。"KIA"表示按照默认策略管控该进程；"TAG1"至"TAG5"分别表示按照对应的自定义标签策略管控该进程；当[addManagedProcess](dataguard-fileguard.md#addmanagedprocess)未设置该参数时，表示设置该进程默认管控策略；当[removeManagedProcess](dataguard-fileguard.md#removemanagedprocess)未设置该参数时，表示删除该进程所有管控策略。 |

## FilePathInfo

表示文件路径信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| absolutePath | string | 否 | 否 | 表示文件绝对路径。 |
| uri | string | 否 | 否 | 表示文件URI。 |

## FileTagInfo

表示文件的标签属性信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| securityLevel | number | 否 | 否 | 表示文件安全等级，其值参考[SecurityLevel](dataguard-fileguard.md#securitylevel)枚举类型。 |
| tag | string | 否 | 否 | 表示文件标签信息。 |

## ScanFileCallback

表示扫描结果回调类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

### onReceiveFileList

onReceiveFileList(files: Array<string>): void

文件目录扫描结果回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | Array<string> | 是 | 表示扫描文件的绝对路径列表。 |

**示例：**

```typescript
let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
  files.forEach((value: string) => {
    console.info(`Succeeded in getting file: ${value}.`);
  })
};
```

### onTaskCompleted

onTaskCompleted(count: number): void

文件目录扫描完成信息获取回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| count | number | 是 | 表示扫描完成后文件的数量。 |

**示例：**

```typescript
let onTaskCompleted: (count: number) => void = (count: number) => {
  console.info(`Succeeded in getting count: ${count}.`);
};
```

## FileGuard

FileGuard类提供了文件分级管控相关接口，包括如下功能：文件目录扫描、标注文件扩展属性、下发文件管控策略等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

### constructor

constructor()

创建FileGuard对象。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**示例：**

```typescript
let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
```

### startFileScanTask

startFileScanTask(type: CommonDirScanType, callback: ScanFileCallback, batchNum?: number): void

启动公共目录文件扫描任务。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [CommonDirScanType](dataguard-fileguard.md#commondirscantype) | 是 | 公共目录扫描范围。取值：MEDIA\_ONLY | MEDIA\_AND\_SANDBOX。 |
| callback | [ScanFileCallback](dataguard-fileguard.md#scanfilecallback) | 是 | 回调函数，返回文件列表和扫描结束通知。 |
| batchNum | number | 否 | 每次调用回调函数时返回的文件列表数量。取值范围：[1, 200]，如果超出此范围，参数设置无效，按照默认每次调用回调函数返回100个文件，直到扫描结束。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
// 文件目录扫描结果回调函数
let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
  console.info(`Succeeded in getting number of files obtained in each callback: ${files.length}.`);
  files.forEach((value: string) => {
    console.info(`Succeeded in getting file: ${value}.`);
  })
};
// 文件目录扫描完成信息获取回调函数
let onCompleteScanTask: (count: number) => void = (count: number) => {
  console.info(`Succeeded in getting count: ${count}.`);
};
// 扫描结果回调
let scanFileCallback: fileGuard.ScanFileCallback = {
  onReceiveFileList: onReceiveFileList,
  onTaskCompleted: onCompleteScanTask
};
guard.startFileScanTask(fileGuard.CommonDirScanType.MEDIA_ONLY, scanFileCallback);
```

### startFileScanTask

startFileScanTask(path: string, callback: ScanFileCallback, batchNum?: number): void

启动指定目录文件扫描任务。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的目录子集。 |
| callback | [ScanFileCallback](dataguard-fileguard.md#scanfilecallback) | 是 | 回调函数，返回文件列表和扫描结束通知。 |
| batchNum | number | 否 | 每次调用回调函数时返回的文件列表数量。取值范围：[1, 200]，如果超出此范围，参数设置无效，按照默认每次调用回调函数返回100个文件，直到扫描结束。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test';
// 文件目录扫描结果回调函数
let onReceiveFileList: (files: string[]) => void = (files: Array<string>) => {
  console.info(`Succeeded in getting number of files obtained in each callback: ${files.length}.`);
  files.forEach((value: string) => {
    console.info(`Succeeded in getting file: ${value}.`);
  })
};
// 文件目录扫描完成信息获取回调函数
let onCompleteScanTask: (count: number) => void = (count: number) => {
  console.info(`Succeeded in getting count: ${count}.`);
};
// 扫描结果回调
let scanFileCallback: fileGuard.ScanFileCallback = {
  onReceiveFileList: onReceiveFileList,
  onTaskCompleted: onCompleteScanTask
};
guard.startFileScanTask(path, scanFileCallback);
```

### openFile

openFile(path: string, callback: AsyncCallback<number>): void

打开文件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |
| callback | AsyncCallback<number> | 是 | 回调函数，当打开文件成功，err为undefined，data为获取到的文件描述符，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
guard.openFile(path, (err: BusinessError, fd: number) => {
  if (err) {
    console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}.`);
    return;
  }
  console.info(`Succeeded in opening file. path: ${path}, fd: ${fd}.`);
});
```

### openFile

openFile(path: string): Promise<number>

打开文件。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
guard.openFile(path).then((fd: number) => {
  console.info(`Succeeded in opening file. path: ${path}, fd: ${fd}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}.`);
});
```

### openFileWrite

openFileWrite(path: string, callback: AsyncCallback<number>): void

只写模式打开文件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [用户的个人数据目录](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |
| callback | AsyncCallback<number> | 是 | 回调函数，当只写模式打开文件成功，err为undefined，data为获取到的文件描述符，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
guard.openFileWrite(path, (err: BusinessError, fd: number) => {
  if (err) {
    console.error(`Failed to open file in write-only mode. Code: ${err.code}, message: ${err.message}.`);
    return;
  }
  console.info(`Succeeded in opening file in write-only mode. path: ${path}, fd: ${fd}.`);
});
```

### openFileWrite

openFileWrite(path: string): Promise<number>

只写模式打开文件。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [用户的个人数据目录](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameter types.  3. Parameter verification failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
guard.openFileWrite(path).then((fd: number) => {
  console.info(`Succeeded in opening file in write-only mode. path: ${path}, fd: ${fd}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to open file in write-only mode. Code: ${err.code}, message: ${err.message}.`);
});
```

### setFileTag

setFileTag(path: string, level: SecurityLevel, tag: string, callback: AsyncCallback<void>): void

设置文件属性标签。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |
| level | [SecurityLevel](dataguard-fileguard.md#securitylevel) | 是 | 用于标识文件安全等级（外部公开、内部公开、秘密、机密、绝密），需由开发者设定，并配合[queryFileTag](dataguard-fileguard.md#queryfiletag)接口使用。 |
| tag | string | 是 | 标签名称，使用[updatePolicy](dataguard-fileguard.md#updatepolicy)接口设置自定义标签策略后，根据标签名称进行相应管控。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步设置文件属性标签成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
let tag: string = 'test';
guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
    return;
  }
  console.info(`Succeeded in setting file tag.`);
});
```

### setFileTag

setFileTag(path: string, level: SecurityLevel, tag: string): Promise<void>

设置文件属性标签。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |
| level | [SecurityLevel](dataguard-fileguard.md#securitylevel) | 是 | 用于标识文件安全等级（外部公开、内部公开、秘密、机密、绝密），需由开发者设定，并配合[queryFileTag](dataguard-fileguard.md#queryfiletag)接口使用。 |
| tag | string | 是 | 标签名称，使用[updatePolicy](dataguard-fileguard.md#updatepolicy)接口设置自定义标签策略后，根据标签名称进行相应管控。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
let tag: string = 'test';
guard.setFileTag(path, fileGuard.SecurityLevel.EXTERNAL, tag).then(() => {
  console.info(`Succeeded in setting file tag.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set file tag. Code: ${err.code}, message: ${err.message}.`);
});
```

### setFileCustomTag

setFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void

设置文件自定义属性标签。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |
| tagList | Array<string> | 是 | 标签列表，标签数量不超过5个。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步设置文件自定义属性标签成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1001700103 | Invalid path. |
| 1001700104 | Failed to check the tag list. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
guard.setFileCustomTag(path, tagList, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to set file custom tag. Code: ${err.code}, message: ${err.message}.`);
  } else {
    console.info(`Succeeded in setting file custom tag.`);
  }
});
```

### setFileCustomTag

setFileCustomTag(path: string, tagList: Array<string>): Promise<void>

设置文件自定义属性标签。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |
| tagList | Array<string> | 是 | 标签列表，标签数量不超过5个。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1001700103 | Invalid path. |
| 1001700104 | Failed to check the tag list. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
guard.setFileCustomTag(path, tagList).then(() => {
  console.info(`Succeeded in setting file custom tag.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set file custom tag. Code: ${err.code}, message: ${err.message}.`);
});
```

### unsetFileCustomTag

unsetFileCustomTag(path: string, tagList: Array<string>, callback: AsyncCallback<void>): void

取消文件自定义属性标签。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |
| tagList | Array<string> | 是 | 标签列表，标签数量不超过5个。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步取消文件自定义属性标签成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1001700103 | Invalid path. |
| 1001700104 | Failed to check the tag list. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
guard.unsetFileCustomTag(path, tagList, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to unset file custom tag. Code: ${err.code}, message: ${err.message}.`);
  } else {
    console.info(`Succeeded in unsetting file custom tag.`);
  }
});
```

### unsetFileCustomTag

unsetFileCustomTag(path: string, tagList: Array<string>): Promise<void>

取消文件自定义属性标签。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.1.1(19)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |
| tagList | Array<string> | 是 | 标签列表，标签数量不超过5个。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1001700103 | Invalid path. |
| 1001700104 | Failed to check the tag list. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
let tagList: string[] = ['sensitive', 'confidential', 'public', 'general', 'special'];
guard.unsetFileCustomTag(path, tagList).then(() => {
  console.info(`Succeeded in unsetting file custom tag.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to unset file custom tag. Code: ${err.code}, message: ${err.message}.`);
});
```

### queryFileTag

queryFileTag(path: string, callback: AsyncCallback<FileTagInfo>): void

获取文件属性标签。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |
| callback | AsyncCallback<[FileTagInfo](dataguard-fileguard.md#filetaginfo)> | 是 | 回调函数。当异步获取文件属性标签成功，err为undefined，data为获取到的文件标签信息对象[FileTagInfo](dataguard-fileguard.md#filetaginfo)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
guard.queryFileTag(path, (err: BusinessError, data: fileGuard.FileTagInfo) => {
  if (err) {
    console.error(`Failed to query file tag. Code: ${err.code}, message: ${err.message}.`);
    return;
  }
  console.info(`Succeeded in querying file tag. securityLevel: ${data.securityLevel}, tag: ${data.tag}.`);
});
```

### queryFileTag

queryFileTag(path: string): Promise<FileTagInfo>

获取文件属性标签。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FileTagInfo](dataguard-fileguard.md#filetaginfo)> | Promise对象，返回文件标签信息对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/test/test.txt';
guard.queryFileTag(path).then((data: fileGuard.FileTagInfo) => {
  console.info(`Succeeded in querying file tag. securityLevel: ${data.securityLevel}, tag: ${data.tag}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to query file tag. Code: ${err.code}, message: ${err.message}.`);
});
```

### getFileUri

getFileUri(path: string, callback: AsyncCallback<FilePathInfo>): void

获取文件URI。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [用户的个人数据目录](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |
| callback | AsyncCallback<[FilePathInfo](dataguard-fileguard.md#filepathinfo)> | 是 | 回调函数。当获取文件URI成功，err为undefined，data为获取到的[FilePathInfo](dataguard-fileguard.md#filepathinfo)；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/test/test.txt';
guard.getFileUri(path, (err: BusinessError, data: fileGuard.FilePathInfo) => {
  if (err) {
    console.error(`Failed to get file uri. Code: ${err.code}, message: ${err.message}.`);
  } else {
    console.info(`Succeeded in getting file uri. absolutePath: ${data.absolutePath}, uri: ${data.uri}.`);
  }
});
```

### getFileUri

getFileUri(path: string): Promise<FilePathInfo>

获取文件URI。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [用户的个人数据目录](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[FilePathInfo](dataguard-fileguard.md#filepathinfo)> | Promise对象，返回文件绝对路径和URI。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/test/test.txt';
guard.getFileUri(path).then((data: fileGuard.FilePathInfo) => {
  console.info(`Succeeded in getting file uri. absolutePath: ${data.absolutePath}, uri: ${data.uri}.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get file uri. Code: ${err.code}, message: ${err.message}.`);
});
```

### deleteFile

deleteFile(path: string, callback: AsyncCallback<void>): void

删除指定路径下的文件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [用户的个人数据目录](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步删除文件成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
guard.deleteFile(path, (err: BusinessError) => {
  if (err) {
    console.error(`Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
  } else {
    console.info(`Succeeded in deleting file.`);
  }
});
```

### deleteFile

deleteFile(path: string): Promise<void>

删除指定路径下的文件。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [用户的个人数据目录](../harmonyos-guides/dataguard-introduction.md#访问限制)下文件的绝对路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let path: string = '/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/test.txt';
guard.deleteFile(path).then(() => {
  console.info(`Succeeded in deleting file.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to delete file. Code: ${err.code}, message: ${err.message}.`);
});
```

### updatePolicy

updatePolicy(policy: string, callback: AsyncCallback<void>): void

更新安全管控策略。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_FILE\_GUARD\_POLICY

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policy | string | 是 | 安全管控策略：网络策略、文件策略、蓝牙策略、星闪策略、多用户策略、可信任应用列表和五种自定义标签。受[IPC](../harmonyos-guides/ipc-rpc-overview.md)通信的限制，单次传输数据上限为100KB。  - **网络策略**  - net\_intercept\_toggle：KIA网络拦截使能开关。0表示关闭，设置为0时，KIA网络拦截不生效；1表示开启拦截（在默认策略中的缺省值为1，其他用户策略下缺省值为0）。  - boundary：管控网段范围。限定管控的网段范围，向不在此范围内的ip地址外发文件默认会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.0.0.0-10.255.255.255"。  - netsegment\_trustlist：管控网段范围中的可信任网段，外发至该网段内的文件不会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.10.0.0-10.100.255.255"。  - netsegment\_blocklist：管控网段范围中的不可信网段，外发至该网段内的文件会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.200.0.0-10.200.255.255"。  - default\_policy：在管控网段范围内，但不处于可信任网段和不可信网段范围内的网段范围称为unspecified\_segment，该字段用于判断外发至unspecified\_segment内的文件是否会被拦截，具体拦截规则如下：  当default\_policy设置为0时，向unspecified\_segment范围发送不会被拦截。  当default\_policy设置为1时，向unspecified\_segment范围发送会被拦截。  - netsegment\_update\_type：网段更新方式。0表示下发策略中的网段信息将覆盖原有策略中的网段信息；1表示在原有网段信息的基础下追加新下发策略中的网段信息，默认为0。  - net\_reject\_cache\_time：网络外发拦截管控时间。当成功触发网络外发拦截后，在该管控时间范围内，相关进程通过网络进行的任何文件外发操作都会被拦截。正整数，在默认策略中的缺省值为30，其他用户策略下缺省值为0，单位：s。  - **文件策略**  - usb\_intercept\_toggle：U盘拦截管控开关。当KIA文件外发到U盘时，设置为0表示关闭拦截（不启用管控），设置为1表示开启拦截，默认为0。  - smb\_client\_intercept\_toggle：Samba客户端拦截管控开关。当通过网络邻居外发KIA文件时，0表示关闭拦截（不启用管控），1表示开启拦截，在默认策略中的缺省值为1，其他用户策略下缺省值为0。从API版本6.0.1(21)开始支持此管控策略。  - smb\_server\_intercept\_toggle：Samba服务端拦截管控开关。当通过网络邻居访问KIA文件时，0表示关闭拦截（不启用管控），1表示开启拦截，在默认策略中的缺省值为1，其他用户策略下缺省值为0。从API版本6.0.1(21)开始支持此管控策略。  - new\_file\_audit\_toggle：新建文件审计开关。开启后，会向审计框架上报文件新建的审计事件，0表示关闭，1表示开启，默认为0。从API版本5.1.1(19)开始支持此管控策略。  - kia\_variant\_toggle：KIA变种开关。开启后，系统将监控KIA变种事件，并支持通过注册回调的方式监听并处理相关变种事件，0表示关闭，1表示开启，在默认策略中的缺省值为1，其他用户策略下缺省值为0。从API版本5.0.3(15)开始支持此管控策略。  - audit\_filter\_toggle：KIA文件创建事件及变种事件的过滤开关。0表示关闭，关闭后，会记录所有进程行为下的KIA文件创建事件及变种事件；1表示开启，开启后，仅记录应用行为下的KIA文件创建事件及变种事件，默认为0。从API版本5.0.3(15)开始支持此管控策略。  - print\_intercept\_toggle：打印管控开关。0表示关闭，关闭后，打印KIA文件的行为不会被拦截，默认为0；1表示开启，开启后，打印KIA文件的行为将会被拦截。从API版本6.1.1(24)开始支持此管控策略。  - **蓝牙策略**  从API版本6.0.1(21)开始支持此管控策略。  - bluetooth\_intercept\_toggle：蓝牙拦截管控开关。设置后，通过蓝牙外发KIA文件会被拦截。字符串列表，可填入"bt\_socket","bt\_ble","bt\_opp"三种蓝牙协议名称，默认为空。  - bluetooth\_intercept\_time：蓝牙外发拦截管控时间。当成功触发蓝牙外发拦截后，在该管控时间范围内，通过蓝牙进行的任何文件外发操作都会被拦截。正整数，在默认策略中的缺省值为15，其他用户策略下缺省值为0，单位：s。  - **星闪策略**  从API版本6.0.1(21)开始支持此管控策略。  - nearlink\_intercept\_toggle：星闪拦截管控开关。设置后，通过相关星闪协议外发KIA文件会被拦截。字符串列表，可填入"nearlink\_ssap","nearlink\_dataTransfer"两种星闪协议名称，默认为空。  - nearlink\_intercept\_time：星闪外发拦截管控时间。当成功触发星闪外发拦截后，在该管控时间范围内，通过星闪进行的任何文件外发操作都会被拦截。正整数，在默认策略中的缺省值为15，其他用户策略下缺省值为0，单位：s。  - **多用户策略**  从API版本5.1.1(19)开始支持此管控策略。  - user\_id：用户ID。设置用户ID后，本次下发的管控策略范围将仅适用于该user\_id对应的用户；若未指定user\_id，则采用默认的管控策略。在使用过程中，系统会优先采用用户的专属策略，若无法匹配，则自动采用默认策略。  - **可信任应用列表**  - trust\_app\_list：可信任应用列表，在可信任应用列表中的应用才可读取KIA文件。字符串列表，元素为[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)，默认为空。从API版本5.0.3(15)开始支持此管控策略。  - kia\_file\_access\_toggle：KIA文件访问限制开关。1表示开启，开启后，应用读取KIA文件的行为将会受到限制，需将应用的[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)加入到trust\_app\_list中，应用才被允许读取KIA文件；0表示关闭，关闭后，任何应用和进程都可以读取KIA文件的内容，默认为0。 从API版本6.1.1(24)开始支持此管控策略。  - **五种自定义标签**  从API版本5.1.1(19)开始支持此管控策略。最多支持五种自定义标签管控策略，该策略会自动识别文件扩展属性中包含指定"tag"内容的文件，并对这些文件进行相应管控。  - "tag": 标签名称，用于在[setFileTag](dataguard-fileguard.md#setfiletag)、[setFileCustomTag](dataguard-fileguard.md#setfilecustomtag)和[unsetFileCustomTag](dataguard-fileguard.md#unsetfilecustomtag)中管控对应标签的文件，默认为空。  - "usb\_intercept\_toggle"：U盘拦截管控开关，默认为0。  - "net\_intercept\_toggle"：网络拦截管控开关，默认为0。  - "boundary"：默认网段范围。  - "netsegment\_trustlist"：可信任网段。  - "netsegment\_blocklist"：不可信网段。  自定义标签从API版本26.0.0开始新增支持以下管控策略：  - "smb\_client\_intercept\_toggle"：Samba客户端拦截管控开关，默认为0。  - "smb\_server\_intercept\_toggle"：Samba服务端拦截管控开关，默认为0。  - "print\_intercept\_toggle"：打印管控开关，默认为0。  - "bluetooth\_intercept\_toggle"：蓝牙拦截管控开关。  - "bluetooth\_intercept\_time"：蓝牙外发拦截管控时间。  - "nearlink\_intercept\_toggle"：星闪拦截管控开关。  - "nearlink\_intercept\_time"：星闪外发拦截管控时间。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步更新安全管控策略成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { BusinessError, osAccount } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

async function updatePolicy() {
  let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  let userId: number = await accountManager.getOsAccountLocalId();

  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let policy: string = '{' +
    // 网络策略
    '"net_intercept_toggle":1,' +
    '"boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255","192.168.0.0-192.168.255.255"],' +
    '"netsegment_trustlist":["10.10.0.0-10.100.255.255","172.20.0.0-172.20.255.255"],' +
    '"netsegment_blocklist":["10.200.0.0-10.200.255.255","192.168.100.0-192.168.200.255"],' +
    '"default_policy":1,' +
    '"netsegment_update_type": 0,' +
    '"net_reject_cache_time":30,' +
    // 文件策略
    '"usb_intercept_toggle":1,' +
    '"smb_client_intercept_toggle":1,' +
    '"smb_server_intercept_toggle":1,' +
    '"new_file_audit_toggle":1,' +
    '"kia_variant_toggle":1,' +
    '"audit_filter_toggle":1,' +
    '"print_intercept_toggle":0,' +
    // 蓝牙策略
    '"bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '"bluetooth_intercept_time":30,' +
    // 星闪策略
    '"nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '"nearlink_intercept_time":30,' +
    // 多用户策略
    `"user_id": ${userId},` +
    // 可信任应用列表
    '"trust_app_list":["ohos.app.hap.myapplication_BPch04bPYBrkJX8RAsmiGDbHFaG+BYvhkg4TK4fHQzJOL4VnoBCZU3boBBXGVEB+M/j0X2nnd7KVeyWuEORVxI2g="],' +
    '"kia_file_access_toggle":0,' +
    // 五种自定义标签
    '"Tag1":{' +
    '   "tag":"sensitive",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '   "netsegment_trustlist":["10.10.0.0-10.10.255.255"],' +
    '   "netsegment_blocklist":["172.20.0.0-172.20.255.255"],' +
    '   "smb_client_intercept_toggle":1,' +
    '   "smb_server_intercept_toggle":1,' +
    '   "print_intercept_toggle":1,' +
    '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '   "bluetooth_intercept_time":30,' +
    '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '   "nearlink_intercept_time":30' +
    '  },' +
    '"Tag2":{' +
    '   "tag":"confidential",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '   "netsegment_trustlist":["10.10.0.0-10.10.255.255"],' +
    '   "netsegment_blocklist":["172.20.0.0-172.20.255.255"],' +
    '   "smb_client_intercept_toggle":1,' +
    '   "smb_server_intercept_toggle":1,' +
    '   "print_intercept_toggle":1,' +
    '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '   "bluetooth_intercept_time":30,' +
    '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '   "nearlink_intercept_time":30' +
    '  },' +
    '"Tag3":{' +
    '   "tag":"public",' +
    '   "usb_intercept_toggle":0,' +
    '   "net_intercept_toggle":0,' +
    '   "boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '   "netsegment_trustlist":["10.10.0.0-10.10.255.255"],' +
    '   "netsegment_blocklist":["172.20.0.0-172.20.255.255"],' +
    '   "smb_client_intercept_toggle":1,' +
    '   "smb_server_intercept_toggle":1,' +
    '   "print_intercept_toggle":1,' +
    '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '   "bluetooth_intercept_time":30,' +
    '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '   "nearlink_intercept_time":30' +
    '  },' +
    '"Tag4":{' +
    '   "tag":"general",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":0,' +
    '   "boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '   "netsegment_trustlist":["10.10.0.0-10.10.255.255"],' +
    '   "netsegment_blocklist":["172.20.0.0-172.20.255.255"],' +
    '   "smb_client_intercept_toggle":1,' +
    '   "smb_server_intercept_toggle":1,' +
    '   "print_intercept_toggle":1,' +
    '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '   "bluetooth_intercept_time":30,' +
    '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '   "nearlink_intercept_time":30' +
    '  },' +
    '"Tag5":{' +
    '   "tag":"special",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '   "netsegment_trustlist":["10.10.0.0-10.10.255.255"],' +
    '   "netsegment_blocklist":["172.20.0.0-172.20.255.255"],' +
    '   "smb_client_intercept_toggle":1,' +
    '   "smb_server_intercept_toggle":1,' +
    '   "print_intercept_toggle":1,' +
    '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '   "bluetooth_intercept_time":30,' +
    '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '   "nearlink_intercept_time":30' +
    '  }' +
    '}';
  guard.updatePolicy(policy, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to update policy. Code: ${err.code}, message: ${err.message}.`);
    } else {
      console.info(`Succeeded in updating policy.`);
    }
  });
}
```

### updatePolicy

updatePolicy(policy: string): Promise<void>

更新安全管控策略。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_FILE\_GUARD\_POLICY

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policy | string | 是 | 安全管控策略：网络策略、文件策略、蓝牙策略、星闪策略、多用户策略、可信任应用列表和五种自定义标签。受[IPC](../harmonyos-guides/ipc-rpc-overview.md)通信的限制，单次传输数据上限为100KB。  - **网络策略**  - net\_intercept\_toggle：KIA网络拦截使能开关。0表示关闭，设置为0时，KIA网络拦截不生效；1表示开启拦截（在默认策略中的缺省值为1，其他用户策略下缺省值为0）。  - boundary：管控网段范围。限定管控的网段范围，向不在此范围内的ip地址外发文件默认会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.0.0.0-10.255.255.255"。  - netsegment\_trustlist：管控网段范围中的可信任网段，外发至该网段内的文件不会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.10.0.0-10.100.255.255"。  - netsegment\_blocklist：管控网段范围中的不可信网段，外发至该网段内的文件会被拦截。字符串列表，元素为ip网段范围(包含IPV4和IPV6)，如"10.200.0.0-10.200.255.255"。  - default\_policy：在管控网段范围内，但不处于可信任网段和不可信网段范围内的网段范围称为unspecified\_segment，该字段用于判断外发至unspecified\_segment内的文件是否会被拦截，具体拦截规则如下：  当default\_policy设置为0时，向unspecified\_segment范围发送不会被拦截。  当default\_policy设置为1时，向unspecified\_segment范围发送会被拦截。  - netsegment\_update\_type：网段更新方式。0表示下发策略中的网段信息将覆盖原有策略中的网段信息；1表示在原有网段信息的基础下追加新下发策略中的网段信息，默认为0。  - net\_reject\_cache\_time：网络外发拦截管控时间。当成功触发网络外发拦截后，在该管控时间范围内，相关进程通过网络进行的任何文件外发操作都会被拦截。正整数，在默认策略中的缺省值为30，其他用户策略下缺省值为0，单位：s。  - **文件策略**  - usb\_intercept\_toggle：U盘拦截管控开关。当KIA文件外发到U盘时，设置为0表示关闭拦截（不启用管控），设置为1表示开启拦截，默认为0。  - smb\_client\_intercept\_toggle：Samba客户端拦截管控开关。当通过网络邻居外发KIA文件时，0表示关闭拦截（不启用管控），1表示开启拦截，在默认策略中的缺省值为1，其他用户策略下缺省值为0。从API版本6.0.1(21)开始支持此管控策略。  - smb\_server\_intercept\_toggle：Samba服务端拦截管控开关。当通过网络邻居访问KIA文件时，0表示关闭拦截（不启用管控），1表示开启拦截，在默认策略中的缺省值为1，其他用户策略下缺省值为0。从API版本6.0.1(21)开始支持此管控策略。  - new\_file\_audit\_toggle：新建文件审计开关。开启后，会向审计框架上报文件新建的审计事件，0表示关闭，1表示开启，默认为0。从API版本5.1.1(19)开始支持此管控策略。  - kia\_variant\_toggle：KIA变种开关。开启后，系统将监控KIA变种事件，并支持通过注册回调的方式监听并处理相关变种事件，0表示关闭，1表示开启，在默认策略中的缺省值为1，其他用户策略下缺省值为0。从API版本5.0.3(15)开始支持此管控策略。  - audit\_filter\_toggle：KIA文件创建事件及变种事件的过滤开关。0表示关闭，关闭后，会记录所有进程行为下的KIA文件创建事件及变种事件；1表示开启，开启后，仅记录应用行为下的KIA文件创建事件及变种事件，默认为0。从API版本5.0.3(15)开始支持此管控策略。  - print\_intercept\_toggle：打印管控开关。0表示关闭，关闭后，打印KIA文件的行为不会被拦截，默认为0；1表示开启，开启后，打印KIA文件的行为将会被拦截。从API版本6.1.1(24)开始支持此管控策略。  - **蓝牙策略**  从API版本6.0.1(21)开始支持此管控策略。  - bluetooth\_intercept\_toggle：蓝牙拦截管控开关。设置后，通过蓝牙外发KIA文件会被拦截。字符串列表，可填入"bt\_socket","bt\_ble","bt\_opp"三种蓝牙协议名称，默认为空。  - bluetooth\_intercept\_time：蓝牙外发拦截管控时间。当成功触发蓝牙外发拦截后，在该管控时间范围内，通过蓝牙进行的任何文件外发操作都会被拦截。正整数，在默认策略中的缺省值为15，其他用户策略下缺省值为0，单位：s。  - **星闪策略**  从API版本6.0.1(21)开始支持此管控策略。  - nearlink\_intercept\_toggle：星闪拦截管控开关。设置后，通过相关星闪协议外发KIA文件会被拦截。字符串列表，可填入"nearlink\_ssap","nearlink\_dataTransfer"两种星闪协议名称，默认为空。  - nearlink\_intercept\_time：星闪外发拦截管控时间。当成功触发星闪外发拦截后，在该管控时间范围内，通过星闪进行的任何文件外发操作都会被拦截。正整数，在默认策略中的缺省值为15，其他用户策略下缺省值为0，单位：s。  - **多用户策略**  从API版本5.1.1(19)开始支持此管控策略。  - user\_id：用户ID。设置用户ID后，本次下发的管控策略范围将仅适用于该user\_id对应的用户；若未指定user\_id，则采用默认的管控策略。在使用过程中，系统会优先采用用户的专属策略，若无法匹配，则自动采用默认策略。  - **可信任应用列表**  - trust\_app\_list：可信任应用列表，在可信任应用列表中的应用才可读取KIA文件。字符串列表，元素为[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)，默认为空。从API版本5.0.3(15)开始支持此管控策略。  - kia\_file\_access\_toggle：KIA文件访问限制开关。1表示开启，开启后，应用读取KIA文件的行为将会受到限制，需将应用的[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)加入到trust\_app\_list中，应用才被允许读取KIA文件；0表示关闭，关闭后，任何应用和进程都可以读取KIA文件的内容，默认为0。 从API版本6.1.1(24)开始支持此管控策略。  - **五种自定义标签**  从API版本5.1.1(19)开始支持此管控策略。最多支持五种自定义标签管控策略，该策略会自动识别文件扩展属性中包含指定"tag"内容的文件，并对这些文件进行相应管控。  - "tag": 标签名称，用于在[setFileTag](dataguard-fileguard.md#setfiletag)、[setFileCustomTag](dataguard-fileguard.md#setfilecustomtag)和[unsetFileCustomTag](dataguard-fileguard.md#unsetfilecustomtag)中管控对应标签的文件，默认为空。  - "usb\_intercept\_toggle"：U盘拦截管控开关，默认为0。  - "net\_intercept\_toggle"：网络拦截管控开关，默认为0。  - "boundary"：默认网段范围。  - "netsegment\_trustlist"：可信任网段。  - "netsegment\_blocklist"：不可信网段。  自定义标签从API版本26.0.0开始新增支持以下管控策略：  - "smb\_client\_intercept\_toggle"：Samba客户端拦截管控开关，默认为0。  - "smb\_server\_intercept\_toggle"：Samba服务端拦截管控开关，默认为0。  - "print\_intercept\_toggle"：打印管控开关，默认为0。  - "bluetooth\_intercept\_toggle"：蓝牙拦截管控开关。  - "bluetooth\_intercept\_time"：蓝牙外发拦截管控时间。  - "nearlink\_intercept\_toggle"：星闪拦截管控开关。  - "nearlink\_intercept\_time"：星闪外发拦截管控时间。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { BusinessError, osAccount } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

async function updatePolicy() {
  let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  let userId: number = await accountManager.getOsAccountLocalId();

  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let policy: string = '{' +
    // 网络策略
    '"net_intercept_toggle":1,' +
    '"boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255","192.168.0.0-192.168.255.255"],' +
    '"netsegment_trustlist":["10.10.0.0-10.100.255.255","172.20.0.0-172.20.255.255"],' +
    '"netsegment_blocklist":["10.200.0.0-10.200.255.255","192.168.100.0-192.168.200.255"],' +
    '"default_policy":1,' +
    '"netsegment_update_type": 0,' +
    '"net_reject_cache_time":30,' +
    // 文件策略
    '"usb_intercept_toggle":1,' +
    '"smb_client_intercept_toggle":1,' +
    '"smb_server_intercept_toggle":1,' +
    '"new_file_audit_toggle":1,' +
    '"kia_variant_toggle":1,' +
    '"audit_filter_toggle":1,' +
    '"print_intercept_toggle":0,' +
    // 蓝牙策略
    '"bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '"bluetooth_intercept_time":30,' +
    // 星闪策略
    '"nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '"nearlink_intercept_time":30,' +
    // 多用户策略
    `"user_id": ${userId},` +
    // 可信任应用列表
    '"trust_app_list":["ohos.app.hap.myapplication_BPch04bPYBrkJX8RAsmiGDbHFaG+BYvhkg4TK4fHQzJOL4VnoBCZU3boBBXGVEB+M/j0X2nnd7KVeyWuEORVxI2g="],' +
    '"kia_file_access_toggle":0,' +
    // 五种自定义标签
    '"Tag1":{' +
    '   "tag":"sensitive",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '   "netsegment_trustlist":["10.10.0.0-10.10.255.255"],' +
    '   "netsegment_blocklist":["172.20.0.0-172.20.255.255"],' +
    '   "smb_client_intercept_toggle":1,' +
    '   "smb_server_intercept_toggle":1,' +
    '   "print_intercept_toggle":1,' +
    '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '   "bluetooth_intercept_time":30,' +
    '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '   "nearlink_intercept_time":30' +
    '  },' +
    '"Tag2":{' +
    '   "tag":"confidential",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '   "netsegment_trustlist":["10.10.0.0-10.10.255.255"],' +
    '   "netsegment_blocklist":["172.20.0.0-172.20.255.255"],' +
    '   "smb_client_intercept_toggle":1,' +
    '   "smb_server_intercept_toggle":1,' +
    '   "print_intercept_toggle":1,' +
    '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '   "bluetooth_intercept_time":30,' +
    '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '   "nearlink_intercept_time":30' +
    '  },' +
    '"Tag3":{' +
    '   "tag":"public",' +
    '   "usb_intercept_toggle":0,' +
    '   "net_intercept_toggle":0,' +
    '   "boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '   "netsegment_trustlist":["10.10.0.0-10.10.255.255"],' +
    '   "netsegment_blocklist":["172.20.0.0-172.20.255.255"],' +
    '   "smb_client_intercept_toggle":1,' +
    '   "smb_server_intercept_toggle":1,' +
    '   "print_intercept_toggle":1,' +
    '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '   "bluetooth_intercept_time":30,' +
    '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '   "nearlink_intercept_time":30' +
    '  },' +
    '"Tag4":{' +
    '   "tag":"general",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":0,' +
    '   "boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '   "netsegment_trustlist":["10.10.0.0-10.10.255.255"],' +
    '   "netsegment_blocklist":["172.20.0.0-172.20.255.255"],' +
    '   "smb_client_intercept_toggle":1,' +
    '   "smb_server_intercept_toggle":1,' +
    '   "print_intercept_toggle":1,' +
    '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '   "bluetooth_intercept_time":30,' +
    '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '   "nearlink_intercept_time":30' +
    '  },' +
    '"Tag5":{' +
    '   "tag":"special",' +
    '   "usb_intercept_toggle":1,' +
    '   "net_intercept_toggle":1,' +
    '   "boundary":["10.0.0.0-10.255.255.255","172.16.0.0-172.31.255.255"],' +
    '   "netsegment_trustlist":["10.10.0.0-10.10.255.255"],' +
    '   "netsegment_blocklist":["172.20.0.0-172.20.255.255"],' +
    '   "smb_client_intercept_toggle":1,' +
    '   "smb_server_intercept_toggle":1,' +
    '   "print_intercept_toggle":1,' +
    '   "bluetooth_intercept_toggle":["bt_socket","bt_ble","bt_opp"],' +
    '   "bluetooth_intercept_time":30,' +
    '   "nearlink_intercept_toggle":["nearlink_ssap","nearlink_dataTransfer"],' +
    '   "nearlink_intercept_time":30' +
    '  }' +
    '}';
  guard.updatePolicy(policy).then(() => {
    console.info(`Succeeded in updating policy.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to update policy. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

### getPolicy

getPolicy(): Promise<string | null>

获取当前设备生效的管控策略内容。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_FILE\_GUARD\_POLICY

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string | null> | Promise对象，返回当前设备生效的管控策略内容，当没有策略时返回空。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1001700001 | System service error. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
guard.getPolicy().then((policy: string | null) => {
  if (policy === null) {
    console.info(`The obtained policy is null.`);
    return;
  }
  console.info(`Succeeded in getting policy. policy length: ${policy.length}`);
  // 返回字符串较长，分次打印
  let len: number = 2000; // 每次打印2000字符
  let totalLen: number = policy.length;
  for (let i: number = 0; i < totalLen; i += len) {
    let end: number = Math.min(i + len, totalLen);
    let item: string = policy.substring(i, end);
    console.info(`policy: ${item}`);
  }
}).catch((err: BusinessError) => {
  console.error(`Failed to get policy. Code: ${err.code}, message: ${err.message}.`);
});
```

### setKiaFilelist

setKiaFilelist(filelist: string, callback: AsyncCallback<void>): void

设置KIA文件列表。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filelist | string | 是 | 受[IPC](../harmonyos-guides/ipc-rpc-overview.md)通信的限制，单次传输数据上限为100KB。  - kia\_filelist：[默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的KIA文件绝对路径列表，相关文件会被标记为KIA文件。  - kia\_keyword：受控文件关键字列表，文件名中包含相关关键字的文件会被管控。  - kia\_suffix：受控文件后缀名列表，文件名包含相关后缀名的文件会被管控。  - compress\_suffix：压缩文件后缀名列表，只有经过压缩后的文件后缀名在该列表范围内，才会上报压缩变种事件。  - user\_id：用户ID。设置用户ID后，本次设置范围将仅适用于该user\_id对应的用户；若未指定user\_id，则设置默认的。在使用过程中，系统会优先采用对应的用户，若无法匹配，则自动采用默认。从API版本5.1.1(19)开始支持。  - kia\_update\_type：KIA文件更新类型，当type为0时，新增策略将会替换原有策略；当type为1时，会在原有策略的基础上追加新增策略；当type为2时，会在原有策略的基础上删除新的策略，默认为0。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当异步设置KIA文件列表成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { osAccount, BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

async function setKiaFilelist() {
  let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  let userId: number = await accountManager.getOsAccountLocalId();
  
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let fileListStr: string =
    '{"kia_filelist":["/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/1.txt",' +
      '"/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/2.txt"],' +
      '"kia_keyword":["key1","key2","key3"],' +
      '"kia_suffix":[".java", ".html", ".cpp", ".docx"],' +
      '"compress_suffix":[".rar", ".zip"],' +
      `"user_id":${userId},` +
      '"kia_update_type":0}';
  guard.setKiaFilelist(fileListStr, (err: BusinessError) => {
    if (err) {
      console.error(`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.`);
    } else {
      console.info(`Succeeded in setting the list of KIA file.`);
    }
  });
}
```

### setKiaFilelist

setKiaFilelist(filelist: string): Promise<void>

设置KIA文件列表。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 4.0.0(10)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filelist | string | 是 | 受[IPC](../harmonyos-guides/ipc-rpc-overview.md)通信的限制，单次传输数据上限为100KB。  - kia\_filelist：[默认路径范围](../harmonyos-guides/dataguard-introduction.md#访问限制)下的KIA文件绝对路径列表，相关文件会被标记为KIA文件。  - kia\_keyword：受控文件关键字列表，文件名中包含相关关键字的文件会被管控。  - kia\_suffix：受控文件后缀名列表，文件名包含相关后缀名的文件会被管控。  - compress\_suffix：压缩文件后缀名列表，只有经过压缩后的文件后缀名在该列表范围内，才会上报压缩变种事件。  - user\_id：用户ID。设置用户ID后，本次设置范围将仅适用于该user\_id对应的用户；若未指定user\_id，则设置默认的。在使用过程中，系统会优先采用对应的用户，若无法匹配，则自动采用默认。从API版本5.1.1(19)开始支持。  - kia\_update\_type：KIA文件更新类型，当type为0时，新增策略将会替换原有策略；当type为1时，会在原有策略的基础上追加新增策略；当type为2时，会在原有策略的基础上删除新的策略，默认为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { osAccount, BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

async function setKiaFilelist() {
  let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
  let userId: number = await accountManager.getOsAccountLocalId();

  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let fileListStr: string =
    '{"kia_filelist":["/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/1.txt",' +
      '"/data/service/el2/{account_id}/hmdfs/account/files/Docs/Documents/2.txt"],' +
      '"kia_keyword":["key1","key2","key3"],' +
      '"kia_suffix":[".java", ".html", ".cpp", ".docx"],' +
      '"compress_suffix":[".rar", ".zip"],' +
      `"user_id":${userId},` +
      '"kia_update_type":0}';
  guard.setKiaFilelist(fileListStr).then(() => {
    console.info(`Succeeded in setting the list of KIA file.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to set the list of KIA file. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

### isKia

isKia(path: string): boolean

检查文件或文件夹是否为KIA。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 文件路径，字符串长度不超过4096。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 布尔值，返回true表示该文件或文件夹是KIA，否则返回false。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1001700001 | System service error. |
| 1001700103 | Invalid path. |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

try {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let path: string = '/data/service/el2/account_id/hmdfs/account/files/Docs/Documents/1.txt';
  let isKIA: boolean = guard.isKia(path);
  console.info(`Succeeded in determining whether the file is a KIA file. isKIA: ${isKIA}`);
} catch (e) {
  console.error(`Failed to determine whether the file is a KIA file. Code: ${e.code}, message: ${e.message}.`);
}
```

### on('kiaCopy')

on(type: 'kiaCopy', callback: Callback<string>): void

订阅KIA文件拷贝事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaCopy'：固定取值，表示监听KIA文件拷贝事件。 |
| callback | Callback<string> | 是 | 回调函数，返回KIA文件拷贝事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function onKiaCopyCallback(eventData: string) {
  console.info(`Succeeded in receiving eventData: ${eventData}.`);
}

try {
  guard.on('kiaCopy', onKiaCopyCallback);
} catch (e) {
  console.error(`Failed to listen the kia file copy event. Code: ${e.code}, message: ${e.message}.`);
}
```

### off('kiaCopy')

off(type: 'kiaCopy', callback?: Callback<string>): void

取消订阅KIA文件拷贝事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaCopy'：固定取值，表示取消监听KIA文件拷贝事件。 |
| callback | Callback<string> | 否 | 回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function offKiaCopyCallback(eventData: string) {
  console.info(`Succeeded in receiving eventData: ${eventData}.`);
}

try {
  guard.off('kiaCopy', offKiaCopyCallback);
} catch (e) {
  console.error(`Failed to cancel listen the KIA file copy event. Code: ${e.code}, message: ${e.message}.`);
}
```

### on('kiaRename')

on(type: 'kiaRename', callback: Callback<string>): void

订阅KIA文件重命名事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaRename'：固定取值，表示监听KIA文件重命名事件。 |
| callback | Callback<string> | 是 | 回调函数，返回KIA文件重命名事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function onKiaRenameCallback(eventData: string) {
  console.info(`Succeeded in receiving eventData: ${eventData}.`);
}

try {
  guard.on('kiaRename', onKiaRenameCallback);
} catch (e) {
  console.error(`Failed to listen the KIA file rename event. Code: ${e.code}, message: ${e.message}.`);
}
```

### off('kiaRename')

off(type: 'kiaRename', callback?: Callback<string>): void

取消订阅KIA文件重命名事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaRename'：固定取值，表示取消监听KIA文件重命名事件。 |
| callback | Callback<string> | 否 | 回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function offKiaRenameCallback(eventData: string) {
  console.info(`Succeeded in receiving eventData: ${eventData}.`);
}

try {
  guard.off('kiaRename', offKiaRenameCallback);
} catch (e) {
  console.error(`Failed to cancel listen the KIA file rename event. Code: ${e.code}, message: ${e.message}.`);
}
```

### on('kiaCompress')

on(type: 'kiaCompress', callback: Callback<string>): void

订阅KIA文件压缩事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaCompress'：固定取值，表示监听KIA文件压缩事件。 |
| callback | Callback<string> | 是 | 回调函数，返回KIA文件压缩事件。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function onKiaCompressCallback(eventData: string) {
  console.info(`Succeeded in receiving eventData: ${eventData}.`);
}

try {
  guard.on('kiaCompress', onKiaCompressCallback);
} catch (e) {
  console.error(`Failed to listen the KIA file compress event. Code: ${e.code}, message: ${e.message}.`);
}
```

### off('kiaCompress')

off(type: 'kiaCompress', callback?: Callback<string>): void

取消订阅KIA文件压缩事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 'kiaCompress'：固定取值，表示取消监听KIA文件压缩事件。 |
| callback | Callback<string> | 否 | 回调函数。可以指定传入on中的callback取消对应的监听，也可以不指定callback清空所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();

function offKiaCompressCallback(eventData: string) {
  console.info(`Succeeded in receiving eventData: ${eventData}.`);
}

try {
  guard.off('kiaCompress', offKiaCompressCallback);
} catch (e) {
  console.error(`Failed to cancel listen the KIA file compress event. Code: ${e.code}, message: ${e.message}.`);
}
```

### setKiaWatermarkImage

setKiaWatermarkImage(image: Uint8Array, info: string): Promise<void>

设置KIA文件水印图片。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_FILE\_GUARD\_POLICY

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 5.0.3(15)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| image | Uint8Array | 是 | 水印图片，仅支持PNG格式，图像像素占用大小不得超过375KB。当传入的数组为空时，可取消已设置的水印。 |
| info | string | 是 | 水印附加信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

async function testSetKiaWatermarkImage() {
  let fd: number = -1;
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let imagePath: string = `/data/service/el2/test_water.png`;
    fd = await guard.openFile(imagePath);
    let stat: fileIo.Stat = fileIo.statSync(fd);
    let buffer: ArrayBuffer = new ArrayBuffer(stat.size);
    fileIo.readSync(fd, buffer);

    let image: Uint8Array = new Uint8Array(buffer);
    let info: string = new Date().toLocaleString();
    guard.setKiaWatermarkImage(image, info).then(() => {
      console.info(`Succeeded in setting the watermark image for KIA file.`);
    }).catch((err: BusinessError) => {
      console.error(`Failed to set the watermark image for KIA file. Code: ${err.code}, message: ${err.message}.`);
    })
  } catch (e) {
    console.error(`testSetKiaWatermarkImage Exception, Code: ${e.code}, message: ${e.message}`);
  } finally {
    if (fd !== -1) {
      fileIo.close(fd);
    }
  }
}
```

### addUnrestrictedApplicationList

addUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>

添加放通应用列表，放通应用不受[updatePolicy](dataguard-fileguard.md#updatepolicy)接口下发的网络、U盘、蓝牙、星闪、Samba客户端和服务端策略管控，但打印管控策略仍会受到限制。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_FILE\_GUARD\_POLICY

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appIds | Array<string> | 是 | 放通应用[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)列表。 |
| userId | number | 否 | 用户ID，正整数。添加放通应用列表并针对指定用户ID策略生效；若未指定用户ID，则添加的放通应用列表将对默认管控策略生效。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1001700001 | System service error. |
| 1001700101 | Invalid userId. |
| 1001700105 | Invalid appId. |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { osAccount, BusinessError } from '@kit.BasicServicesKit';
import { bundleManager } from '@kit.AbilityKit';

async function addUnrestrictedApplicationList() {
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let userId: number = await accountManager.getOsAccountLocalId();
    let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
      bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
    let bundleInfo: bundleManager.BundleInfo = await bundleManager.getBundleInfoForSelf(bundleFlags);
    let appId: string = bundleInfo.signatureInfo.appId;
    let appIds: string[] = [appId];

    guard.addUnrestrictedApplicationList(appIds, userId).then(() => {
      console.info(`Succeeded in adding the application from the unrestricted list.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to add the application from the unrestricted list. Code: ${error.code}, message: ${error.message}.`);
    })
  } catch (err) {
    console.error(`Failed to test addUnrestrictedApplicationList. Code: ${err.code}, message: ${err.message}.`);
  }
}
```

### removeUnrestrictedApplicationList

removeUnrestrictedApplicationList(appIds: Array<string>, userId?: number): Promise<void>

删除放通应用列表。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_FILE\_GUARD\_POLICY

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appIds | Array<string> | 是 | 放通应用[appId](../harmonyos-guides/common-problem-of-application.md#什么是appid)列表。 |
| userId | number | 否 | 用户ID，正整数。删除指定用户ID策略下的放通应用列表；若未指定用户ID，则删除默认管控策略下的放通应用列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1001700001 | System service error. |
| 1001700101 | Invalid userId. |
| 1001700105 | Invalid appId. |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { osAccount, BusinessError } from '@kit.BasicServicesKit';
import { bundleManager } from '@kit.AbilityKit';

async function removeUnrestrictedApplicationList() {
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let userId: number = await accountManager.getOsAccountLocalId();
    let bundleFlags = bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION |
      bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_SIGNATURE_INFO;
    let bundleInfo: bundleManager.BundleInfo = await bundleManager.getBundleInfoForSelf(bundleFlags);
    let appId: string = bundleInfo.signatureInfo.appId;
    let appIds: string[] = [appId];
    guard.removeUnrestrictedApplicationList(appIds, userId).then(() => {
      console.info(`Succeeded in removing the application from the unrestricted list.`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to remove the application from the unrestricted list. Code: ${error.code}, message: ${error.message}.`);
    })
  } catch (err) {
    console.error(`Failed to test removeUnrestrictedApplicationList. Code: ${err.code}, message: ${err.message}.`);
  }
}
```

### getUnrestrictedApplicationList

getUnrestrictedApplicationList(userId?: number): Promise<Array<string>>

获取放通应用列表。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_FILE\_GUARD\_POLICY

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| userId | number | 否 | 用户ID，正整数。获取指定用户ID策略下的放通应用列表；若未指定用户ID，则获取默认管控策略下的放通应用列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<string>> | Promise对象，返回放通应用appId列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1001700001 | System service error. |
| 1001700101 | Invalid userId. |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { osAccount, BusinessError } from '@kit.BasicServicesKit';

async function getUnrestrictedApplicationList() {
  try {
    let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
    let accountManager: osAccount.AccountManager = osAccount.getAccountManager();
    let userId: number = await accountManager.getOsAccountLocalId();

    guard.getUnrestrictedApplicationList(userId).then((appIds: string[]) => {
      console.info(`Succeeded in getting the application from the unrestricted list. appIds: ${appIds.toString()}`);
    }).catch((error: BusinessError) => {
      console.error(`Failed to get the application from the unrestricted list. Code: ${error.code}, message: ${error.message}.`);
    })
  } catch (err) {
    console.error(`Failed to test getUnrestrictedApplicationList. Code: ${err.code}, message: ${err.message}.`);
  }
}
```

### setHdcAuthenticationKey

setHdcAuthenticationKey(devType: AuthenticateDeviceType, keyType: AuthenticateKeyType, key: Uint8Array): Promise<void>

设置上下位机间的[HDC](../harmonyos-guides/hdc.md)认证密钥。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_FILE\_GUARD\_POLICY

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| devType | [AuthenticateDeviceType](dataguard-fileguard.md#authenticatedevicetype) | 是 | HDC认证的设备类型枚举。当设备类型为上位机时，需设置私钥；当设备类型为下位机时，需设置公钥。 |
| keyType | [AuthenticateKeyType](dataguard-fileguard.md#authenticatekeytype) | 是 | HDC认证的密钥类型枚举。 |
| key | Uint8Array | 是 | PEM格式的RSA-3072密钥。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported.  适用版本：26.0.0+ |
| 1001700001 | System service error. |
| 1001700201 | The HDC status is abnormal. |
| 1001700202 | Failed to save the private key. |
| 1001700203 | Failed to save the public key. |
| 1001700204 | The key type does not match the device type. |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';
import { BusinessError } from '@kit.BasicServicesKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let devType: fileGuard.AuthenticateDeviceType = fileGuard.AuthenticateDeviceType.UPPER;
let keyType: fileGuard.AuthenticateKeyType = fileGuard.AuthenticateKeyType.PRIVATE_KEY;
let key: Uint8Array = new Uint8Array([0]);

guard.setHdcAuthenticationKey(devType, keyType, key).then(() => {
  console.info(`Succeeded in setting the HDC authentication key.`);
}).catch((error: BusinessError) => {
  console.error(`Failed to set the HDC authentication key. Code: ${error.code}, message: ${error.message}.`);
})
```

### onPrintStartup

onPrintStartup(callback: Callback<void>): void

订阅打印服务启动事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 是 | 回调函数，用于监听打印服务启动事件。如果打印服务先于该回调函数启动，则该回调函数不会触发回调。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

function printStartupCallBack() {
  console.info(`Succeeded in listening print-startup.`);
}

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
guard.onPrintStartup(printStartupCallBack);
```

### offPrintStartup

offPrintStartup(callback?: Callback<void>): void

取消订阅打印服务启动事件。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<void> | 否 | 回调函数。可以指定传入[onPrintStartup](dataguard-fileguard.md#onprintstartup)中的callback取消对应的监听，也可以不指定callback清空所有监听。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported.  适用版本：26.0.0+ |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
guard.offPrintStartup();
```

### getManagedProcessPolicy

getManagedProcessPolicy(): Promise<ManagedProcessPolicy | null>

获取当前设备处于管控状态下的进程管控策略。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ManagedProcessPolicy](dataguard-fileguard.md#managedprocesspolicy) | null> | Promise对象，返回当前设备进程管控策略，当没有策略时返回空。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1001700001 | System service error. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
guard.getManagedProcessPolicy().then((policy: fileGuard.ManagedProcessPolicy | null) => {
  if (policy === null) {
    console.info(`The managed process policy is null.`);
    return;
  }
  console.info(`Succeeded in getting the managed process policy. status: ${policy.status}, time: ${policy.time}`);
}).catch((err: BusinessError) => {
  console.error(`Failed to get the managed process policy. Code: ${err.code}, message: ${err.message}.`);
});
```

### setManagedProcessPolicy

setManagedProcessPolicy(policy: ManagedProcessPolicy): Promise<void>

设置当前设备进程管控策略。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_FILE\_GUARD\_POLICY

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| policy | [ManagedProcessPolicy](dataguard-fileguard.md#managedprocesspolicy) | 是 | 进程管控策略。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1001700001 | System service error. |
| 1001700106 | Invalid policy. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let policy: fileGuard.ManagedProcessPolicy = {
  status: fileGuard.ManagedProcessStatus.TIME_BASED,
  time: 3000
};
guard.setManagedProcessPolicy(policy).then(() => {
  console.info(`Succeeded in setting the managed process policy.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to set the managed process policy. Code: ${err.code}, message: ${err.message}.`);
});
```

### getManagedProcessList

getManagedProcessList(): Promise<ManagedProcessInfo[]>

获取当前设备处于管控状态下的进程管控信息列表。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.FILE\_GUARD\_MANAGER

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ManagedProcessInfo](dataguard-fileguard.md#managedprocessinfo)[]> | Promise对象，返回进程管控信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1001700001 | System service error. |

**示例：**

```typescript
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
guard.getManagedProcessList().then((infos: fileGuard.ManagedProcessInfo[]) => {
  console.info(`Succeeded in getting the managed process list.`);
  infos.forEach((info: fileGuard.ManagedProcessInfo) => {
    console.info(`ManagedProcessInfo pid: ${info.pid}, policy: ${info.policy}.`);
  });
}).catch((err: BusinessError) => {
  console.error(`Failed to get the managed process list. Code: ${err.code}, message: ${err.message}.`);
});
```

### addManagedProcess

addManagedProcess(processInfo: ManagedProcessInfo): Promise<void>

添加管控进程。需要提供该进程的Pid以及管控策略类别（如KIA，TAG1~TAG5），基于[updatePolicy](dataguard-fileguard.md#updatepolicy)接口配置的策略进行管控。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_FILE\_GUARD\_POLICY

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| processInfo | [ManagedProcessInfo](dataguard-fileguard.md#managedprocessinfo) | 是 | 进程管控信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1001700001 | System service error. |
| 1001700106 | Invalid policy. |

**示例：**

```typescript
import { process } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let processInfo: fileGuard.ManagedProcessInfo = {
  pid: process.pid,
  policy: 'Tag1'
};

guard.addManagedProcess(processInfo).then(() => {
  console.info(`Succeeded in adding the managed process.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to add the managed process. Code: ${err.code}, message: ${err.message}.`);
});
```

### removeManagedProcess

removeManagedProcess(processInfo: ManagedProcessInfo): Promise<void>

删除管控进程。如果未配置进程管控信息中的管控策略，将删除该进程下的所有管控策略，如果配置了策略，则仅删除指定进程指定的管控策略。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.SET\_FILE\_GUARD\_POLICY

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| processInfo | [ManagedProcessInfo](dataguard-fileguard.md#managedprocessinfo) | 是 | 进程管控信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[企业数据保护服务错误码](errorcode-enterprise-dataguard.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 1001700001 | System service error. |

**示例：**

```typescript
import { process } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
let processInfo: fileGuard.ManagedProcessInfo = {
  pid: process.pid
};
guard.removeManagedProcess(processInfo).then(() => {
  console.info(`Succeeded in removing the managed process.`);
}).catch((err: BusinessError) => {
  console.error(`Failed to remove the managed process. Code: ${err.code}, message: ${err.message}.`);
});
```

### isFileGuardSupported

isFileGuardSupported(): boolean

检查设备是否支持文件分级管控。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.FileGuard

**起始版本：** 26.0.0

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 布尔值，返回true表示支持文件分级管控，否则返回false。 |

**示例：**

```typescript
import { fileGuard } from '@kit.EnterpriseDataGuardKit';

try {
  let guard: fileGuard.FileGuard = new fileGuard.FileGuard();
  let isSupported: boolean = guard.isFileGuardSupported();
  console.info(`Succeeded in determining whether the device supports FileGuard. isSupported: ${isSupported}`);
} catch (e) {
  console.error(`Failed to determine whether the device supports FileGuard. Code: ${e.code}, message: ${e.message}.`);
}
```
