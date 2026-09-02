---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/enterprisethreatprotection-virusremediation-interface
title: virusRemediation（病毒检测与处置）
breadcrumb: API参考 > 系统 > 安全 > Enterprise Threat Protection Kit（企业威胁防护服务） > ArkTS API > virusRemediation（病毒检测与处置）
category: harmonyos-references
scraped_at: 2026-09-02T15:01:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0a3aaabfb83fc684e15751450333ca0bba7aec8da7ab63a6e21f619338c08711
---

病毒检测与处置功能旨在保障数据安全，为安全防护类应用提供威胁文件的扫描与处置、威胁进程终止能力。其主要功能包括文件打开、应用目录扫描，以及文件隔离、已隔离文件恢复、已隔离文件删除、隔离文件查询和终止进程等处置操作。本服务需由安全防护类应用申请相应[权限](../harmonyos-guides/permissions-for-enterprise-apps.md#ohospermissionscan_remediate_virus)后使用。

**起始版本：** 6.1.1(24)

## 导入模块

```typescript
import { virusRemediation } from '@kit.EnterpriseThreatProtectionKit';
```

## IsolatedFileInfo

隔离文件信息。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 表示隔离ID，UUID格式，长度为36个字符。 |
| absolutePath | string | 否 | 否 | 表示文件的原始路径。 |
| size | number | 否 | 否 | 表示文件大小，单位: byte。 |
| isolatedTime | number | 否 | 否 | 表示文件隔离时间，单位: ms。 |

## ScanTargetType

扫描对象类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BUNDLE | 0 | 应用安装包目录。 |
| SANDBOX | 1 | 应用el2级别加密数据目录。 |

## ScanCallback

扫描结果的回调类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

### onReceive

onReceive(paths: string[]): void

文件目录扫描结果回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| paths | string[] | 是 | 表示扫描文件的绝对路径列表。 |

**示例：**

```typescript
let onReceive: (paths: string[]) => void = (files: Array<string>) => {
  files.forEach((value: string, index: number) => {
    console.info(`Succeeded in getting file: ${value}.`);
  })
};
```

### onComplete

onComplete(): void

文件目录扫描完成信息获取回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

**示例：**

```typescript
let onComplete: () => void = () => {
  console.info(`Query completed`);
};
```

### onError

onError(code: number, message: string): void

文件目录扫描报错信息获取回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 错误码。 |
| message | string | 是 | 错误信息。 |

**示例：**

```typescript
let onError: (code: number, message: string) => void = (code: number, message: string) => {
  console.error(`Query error, error code: ${code}, message: ${message}`);
};
```

## QueryCallback

查询隔离文件信息的回调类。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

### onQuery

onQuery(files: IsolatedFileInfo[]): void

隔离文件信息查询结果回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| files | [IsolatedFileInfo](enterprisethreatprotection-virusremediation-interface.md#isolatedfileinfo)[] | 是 | 表示隔离文件信息的列表。 |

**示例：**

```typescript
let onQuery: (files: virusRemediation.IsolatedFileInfo[]) => void = (files: virusRemediation.IsolatedFileInfo[]) => {
  files.forEach((value: virusRemediation.IsolatedFileInfo, index: number) => {
    console.info(`Succeeded in getting isolated file, file id: ${value.id}.`);
  })
};
```

### onComplete

onComplete(): void

隔离文件信息查询完成信息获取回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

**示例：**

```typescript
let onComplete: () => void = () => {
  console.info(`Query completed`);
};
```

### onError

onError(code: number, message: string): void

隔离文件信息查询报错信息获取回调函数。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 错误码。 |
| message | string | 是 | 错误信息。 |

**示例：**

```typescript
let onError: (code: number, message: string) => void = (code: number, message: string) => {
  console.error(`Query error, error code: ${code}, message: ${message}`);
};
```

## scanBundleFiles

scanBundleFiles(type: ScanTargetType, callback: ScanCallback, bundleName?: string, batchNum?: number): void

扫描目标应用目录文件，调用前需确保已获取权限且入参符合规范，否则调用失败。使用callback异步回调。

**需要权限：** ohos.permission.SCAN\_REMEDIATE\_VIRUS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [ScanTargetType](enterprisethreatprotection-virusremediation-interface.md#scantargettype) | 是 | 扫描对象类型，取值为0或1，其余取值无效。其中，0代表BUNDLE，即应用安装包目录；1代表SANDBOX，即应用el2级别加密数据目录。当需要扫描特定应用的安装包目录时，选择BUNDLE。 |
| callback | [ScanCallback](enterprisethreatprotection-virusremediation-interface.md#scancallback) | 是 | 回调函数，返回文件列表和扫描结束通知。 |
| bundleName | string | 否 | 扫描的应用包名。参数为空时，则返回所有允许扫描的应用的文件。 |
| batchNum | number | 否 | 每一轮调用回调函数时返回的文件列表数量。取值范围为[1,200]，超出此范围则参数设置无效不执行扫描任务。不填则取默认值100。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-enterprise-threat-protection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. The application calls an API without the required permission. Check the permission required to call the API and make sure the application has the permission. |
| 1023801001 | System service exception. The system is in an insecure state (for example, the device is not unlocked), or there is a hardware failure. Ensure that the system status is normal and try again. |
| 1023802002 | Access and disposal denied for this path. The target path does not meet the access restrictions or handling restrictions, such as permission levels and app sandbox restrictions. Check whether the path meets the access and handling restrictions. |

**示例：**

```typescript
// 启动文件扫描任务，通过指定回调函数处理扫描过程中接收到的文件路径、扫描完成和错误信息
function startFileScanTask() {
  // 接收扫描结果的回调函数，用于处理扫描得到的文件路径列表
  let onReceive: (paths: string[]) => void = (files: Array<string>) => {
    files.forEach((value: string, index: number) => {
      console.info(`Succeeded in getting file: ${value}.`);
    })
  };
  let onComplete: () => void = () => {
    console.info(`Scan completed`);
  };
  let onError: (code: number, message: string) => void = (code: number, message: string) => {
    console.error(`Scan error, error code: ${code}, message: ${message}`);
  }
  let scanFileCallback: virusRemediation.ScanCallback = {
    onReceive: onReceive,
    onComplete: onComplete,
    onError: onError
  };
  // 调用 scanBundleFiles 方法扫描应用安装包目录下的文件，并通过 scanFileCallback 回调处理结果
  try {
    virusRemediation.scanBundleFiles(virusRemediation.ScanTargetType.BUNDLE, scanFileCallback);
  } catch (error) {
    console.error(`Failed to scan bundle files. Error: ${error}`);
  }
}
```

## openFile

openFile(path: string): Promise<number>

打开文件。使用Promise异步回调。

**需要权限：** ohos.permission.SCAN\_REMEDIATE\_VIRUS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | [默认路径范围](../harmonyos-guides/enterprisethreatprotection-introduction.md#文件访问限制)下的绝对路径，路径长度不做限制。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回文件描述符。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-enterprise-threat-protection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. The application calls an API without the required permission. Check the permission required to call the API and make sure the application has the permission. |
| 1023801001 | System service exception. The system is in an insecure state (for example, the device is not unlocked), or there is a hardware failure. Ensure that the system status is normal and try again. |
| 1023802001 | File not found. The target path is incorrectly configured or the file has been deleted. Verify the target path and file status. |
| 1023802002 | Access and disposal denied for this path. The target path does not meet the access restrictions or handling restrictions, such as permission levels and app sandbox restrictions. Check whether the path meets the access and handling restrictions. |
| 1023803001 | Access to other users' files is restricted. The file resources are not under the current user account. Verify the identity of the current user and change the path to a valid one. |
| 1023804001 | Invalid file type. Currently, only single files can be handled. Directories are not supported. Check whether the path contains a single file. If not, change the target to a single file and perform the operation again. |

**示例：**

```typescript
import { fileIo } from '@kit.CoreFileKit';

function openFilePromise() {
  // 目标文件路径，此处为示例路径，实际使用时需替换为用户指定的真实路径
  let path: string = '/example/path/to/file.txt';
  virusRemediation.openFile(path).then((fd: number) => {
    console.info(`Succeeded in opening file. path: ${path} , fd: ${fd}.`);
    fileIo.closeSync(fd);
  }).catch((err: BusinessError) => {
    console.error(`Failed to open file. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

## queryIsolatedFiles

queryIsolatedFiles(callback: QueryCallback, batchNum?: number): void

查询隔离文件信息。使用callback异步回调。

**需要权限：** ohos.permission.SCAN\_REMEDIATE\_VIRUS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [QueryCallback](enterprisethreatprotection-virusremediation-interface.md#querycallback) | 是 | 回调函数，返回隔离文件信息列表，并在所有信息成功返回后通知用户查询结束。 |
| batchNum | number | 否 | 每一轮调用回调函数时返回的文件列表数量。取值范围为[1,200]，超出此范围则参数设置无效不执行查询任务。不填则取默认值100。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-enterprise-threat-protection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. The application calls an API without the required permission. Check the permission required to call the API and make sure the application has the permission. |
| 1023801001 | System service exception. The system is in an insecure state (for example, the device is not unlocked), or there is a hardware failure. Ensure that the system status is normal and try again. |

**示例：**

```typescript
function startQueryTask() {
  // 查询隔离文件信息回调
  let onQuery: (files: virusRemediation.IsolatedFileInfo[]) => void = (files: virusRemediation.IsolatedFileInfo[]) => {
    files.forEach((value: virusRemediation.IsolatedFileInfo, index: number) => {
      console.info(`Succeeded in getting isolated file, file id: ${value.id}.`);
    })
  };
  // 查询隔离文件信息结束通知
  let onComplete: () => void = () => {
    console.info(`Query completed`);
  };
  // 查询隔离文件信息错误报告
  let onError: (code: number, message: string) => void = (code: number, message: string) => {
    console.error(`Query error, error code: ${code}, message: ${message}`);
  }
  let cb: virusRemediation.QueryCallback = {
    onQuery: onQuery,
    onComplete: onComplete,
    onError: onError
  };
  try {
    virusRemediation.queryIsolatedFiles(cb);
  } catch (error) {
    console.error(`Failed to get isolated file. Error: ${error}`);
  }
}
```

## isolateThreatFile

isolateThreatFile(path: string): Promise<string>

隔离指定路径的文件，在调用前应确保当前路径正确有效且隔离区磁盘空间充足。使用Promise异步回调。

**需要权限：** ohos.permission.SCAN\_REMEDIATE\_VIRUS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| path | string | 是 | 待隔离文件的绝对路径，路径长度不做限制。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回隔离ID。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-enterprise-threat-protection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. The application calls an API without the required permission. Check the permission required to call the API and make sure the application has the permission. |
| 1023801001 | System service exception. The system is in an insecure state (for example, the device is not unlocked), or there is a hardware failure. Ensure that the system status is normal and try again. |
| 1023802001 | File not found. The target path is incorrectly configured or the file has been deleted. Verify the target path and file status. |
| 1023802002 | Access and disposal denied for this path. The target path does not meet the access restrictions or handling restrictions, such as permission levels and app sandbox restrictions. Check whether the path meets the access and handling restrictions. |
| 1023803001 | Access to other users' files is restricted. The file resources are not under the current user account. Verify the identity of the current user and change the path to a valid one. |
| 1023804001 | Invalid file type. Currently, only single files can be handled. Directories are not supported. Check whether the path contains a single file. If not, change the target to a single file and perform the operation again. |
| 1023804002 | Disposal is not supported. Please handle it manually. The target path is the app package path. You are advised to handle it in the following ways: 1. Prohibit the app from running. 2. Uninstall the app. Check whether the path is the app package path and select a proper handling method. |
| 1023805001 | Quarantine storage space is full. The disk in the isolation zone is full or has reached the upper capacity limit. Check the space usage and status of the current isolation zone. |

**示例：**

```typescript
function isolateFilePromise() {
  // 目标文件路径，此处为示例路径，实际使用时需替换为用户指定的真实路径
  let path: string = '/data/service/el2/test/test.txt';
  virusRemediation.isolateThreatFile(path).then((id: string) => {
    console.info(`Succeeded in isolating file. path: ${path} , id: ${id}.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to isolate file. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

## restoreIsolatedFile

restoreIsolatedFile(id: string): Promise<string>

恢复指定隔离ID的文件。使用Promise异步回调。

**需要权限：** ohos.permission.SCAN\_REMEDIATE\_VIRUS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 待恢复文件的隔离ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回文件恢复的路径。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-enterprise-threat-protection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. The application calls an API without the required permission. Check the permission required to call the API and make sure the application has the permission. |
| 1023801001 | System service exception. The system is in an insecure state (for example, the device is not unlocked), or there is a hardware failure. Ensure that the system status is normal and try again. |
| 1023802003 | Existed same file in the restored path. The restoration fails because new and old files have the same name. Check whether duplicate file names exist in the restoration path. You can rename the files or delete the old files to rectify the fault. |
| 1023803001 | Access to other users' files is restricted. The file resources are not under the current user account. Verify the identity of the current user and change the path to a valid one. |
| 1023804003 | Invalid operation. The requested ID is in an incorrect format or is invalid. Check whether the isolation ID is the same as that stored in the app and whether the file corresponding to the isolation ID is in the isolated state (that is, there is an isolation record that has not been released). |
| 1023806001 | Database corruption detected. The table structure is abnormal or the connection fails. Run preliminary self-check commands or view logs to obtain detailed error information. |

**示例：**

```typescript
function restoreFilePromise() {
  // 隔离文件ID，可通过queryIsolatedFiles()接口获取
  let id: string = 'example-id-12345';
  virusRemediation.restoreIsolatedFile(id).then((path: string) => {
    console.info(`Succeeded in restoring file. restore path: ${path} , id: ${id}.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to restore file. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

## removeIsolatedFile

removeIsolatedFile(id: string): Promise<void>

删除指定隔离ID的文件。使用Promise异步回调。

**需要权限：** ohos.permission.SCAN\_REMEDIATE\_VIRUS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 待删除文件的隔离ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-enterprise-threat-protection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. The application calls an API without the required permission. Check the permission required to call the API and make sure the application has the permission. |
| 1023801001 | System service exception. The system is in an insecure state (for example, the device is not unlocked), or there is a hardware failure. Ensure that the system status is normal and try again. |
| 1023803001 | Access to other users' files is restricted. The file resources are not under the current user account. Verify the identity of the current user and change the path to a valid one. |
| 1023804003 | Invalid operation. The requested ID is in an incorrect format or is invalid. Check whether the isolation ID is the same as that stored in the app and whether the file corresponding to the isolation ID is in the isolated state (that is, there is an isolation record that has not been released). |
| 1023806001 | Database corruption detected. The table structure is abnormal or the connection fails. Run preliminary self-check commands or view logs to obtain detailed error information. |

**示例：**

```typescript
function removeIsolatedFilePromise() {
  // 隔离文件ID，可通过queryIsolatedFiles()接口获取
  let id: string = 'example-id-12345';
  virusRemediation.removeIsolatedFile(id).then(() => {
    console.info(`Succeeded in removing file.`);
  }).catch((err: BusinessError) => {
    console.error(`Failed to remove file. Code: ${err.code}, message: ${err.message}.`);
  });
}
```

## terminateProcess

terminateProcess(pid: number): Promise<void>

终止正在运行的指定进程。使用Promise异步回调。

**需要权限：** ohos.permission.SCAN\_REMEDIATE\_VIRUS

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.PCService.VirusRemediation

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pid | number | 是 | 待终止的威胁进程ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API 错误码](errorcode-enterprise-threat-protection.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. The application calls an API without the required permission. Check the permission required to call the API and make sure the application has the permission. |
| 1023801001 | System service exception. The system is in an insecure state (for example, the device is not unlocked), or there is a hardware failure. Ensure that the system status is normal and try again. |
| 1023807001 | Process not found. The specified process does not exist or has already terminated. Ensure the provided process ID is valid. |
| 1023807002 | Access and disposal are denied for this process. The process is protected and cannot be terminated or accessed. Ensure the process is not a critical system process and termination is permitted. |
| 1023807003 | Access to other users' processes is not allowed. The target process belongs to a different user and cannot be accessed. Only operate on processes owned by the current user or run with elevated privileges. |

**示例：**

```typescript
function terminateProcessPromise() {
  let pid: number = 0;
  virusRemediation.terminateProcess(pid).then(() => {
    console.info(`Succeeded in terminating process.`);
  }).catch((err: BusinessError) => {
    if (err.code === 1023807001) {
      console.error('Process not found.');
    } else if (err.code === 1023807002) {
      console.error('Access and disposal are denied for this process.');
    } else if (err.code === 1023807003) {
      console.error(`Access to other users' processes is not allowed.`);
    } else {
      console.error(`Failed to terminate process. Code: ${err.code}, message: ${err.message}.`);
    }
  });
}
```
