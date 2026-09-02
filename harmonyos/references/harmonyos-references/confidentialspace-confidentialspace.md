---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/confidentialspace-confidentialspace
title: "@hms.security.confidentialSpace (机密空间服务)"
breadcrumb: API参考 > 系统 > 安全 > Confidential Space Kit（机密空间服务） > ArkTS API > @hms.security.confidentialSpace (机密空间服务)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:a82e9d7751fd5beaa9ff8f01931af378c7d9706176a2d037e6c3d20ec64511be
---

机密空间服务提供了在机密空间内部运行数据应用、处理隐私数据的能力，支持应用与系统、应用与应用在空间内安全地共享数据。

**起始版本：** 26.0.0

## 导入模块

```typescript
import { confidentialSpace } from '@kit.ConfidentialSpaceKit';
```

## DataAppErrorInfo

数据应用错误的详细信息。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.ConfidentialSpace

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| dataAppErrorCode | number | 是 | 否 | 数据应用产生的原始错误码。取值应为[1, 32]内的整数。 |

## DataAppHandle

数据应用句柄，表示一个数据应用实例。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.ConfidentialSpace

### constructor

private constructor()

DataAppHandle仅提供私有构造函数，不能直接实例化。创建本类对象请参见[runApp](confidentialspace-confidentialspace.md#confidentialspacerunapp)。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.ConfidentialSpace

### stop

public stop(): void

结束数据应用。调用后，数据应用进程将被通知中止，无法再进行后续的数据收发操作。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.ConfidentialSpace

**示例：**

```typescript
import { confidentialSpace } from '@kit.ConfidentialSpaceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'ConfidentialSpace';

let handle: confidentialSpace.DataAppHandle;
try {
  handle = await confidentialSpace.runApp(`/data/storage/el1/bundle/libs/arm64/libdemo_da.so`, []);
} catch (e) {
  hilog.error(0x0000, TAG, `Failed to run app. code=${e.code}, message=${e.message}`);
  return;
}
// ...
handle.stop();
```

### sendData

public sendData(data: Uint8Array): Promise<void>

向数据应用发送数据。使用Promise异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.ConfidentialSpace

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | Uint8Array | 是 | 待发送的数据。最大长度为16777216字节。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-confidentialspace.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1028700001 | Invalid argument. |
| 1028700008 | The data app has stopped running. |
| 1028700009 | Communication between client and data manager failed. |
| 1028700010 | Communication between data manager and data app failed. |
| 1028700011 | Message exceeded size limit. |

**示例：**

```typescript
import { buffer } from '@kit.ArkTS';
import { confidentialSpace } from '@kit.ConfidentialSpaceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'ConfidentialSpace';

let handle: confidentialSpace.DataAppHandle;
try {
  handle = await confidentialSpace.runApp(`/data/storage/el1/bundle/libs/arm64/libdemo_da.so`, []);
} catch (e) {
  hilog.error(0x0000, TAG, `Failed to run app. code=${e.code}, message=${e.message}`);
  return;
}
let payload = new Uint8Array(buffer.from('Message to send', 'utf-8').buffer);
try {
  await handle.sendData(payload);
} catch (e) {
  hilog.error(0x0000, TAG, `Failed to send data. code=${e.code}, message=${e.message}`);
}
```

### onReceiveData

public onReceiveData(callback: Callback<Uint8Array>): void

注册从数据应用接收数据的回调函数。当接收到从数据应用发送的数据时，会调用所有注册的回调。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.ConfidentialSpace

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<Uint8Array> | 是 | 回调函数，返回接收的数据。 |

**示例：**

```typescript
import { confidentialSpace } from '@kit.ConfidentialSpaceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'ConfidentialSpace';

let handle: confidentialSpace.DataAppHandle;
try {
  handle = await confidentialSpace.runApp(`/data/storage/el1/bundle/libs/arm64/libdemo_da.so`, []);
} catch (e) {
  hilog.error(0x0000, TAG, `Failed to run app. code=${e.code}, message=${e.message}`);
  return;
}
handle.onReceiveData((data: Uint8Array) => {
  hilog.info(0x0000, TAG, `Received data, length=${data.length}`);
  handle.stop();
});
```

### offReceiveData

public offReceiveData(callback?: Callback<Uint8Array>): void

取消注册从数据应用接收数据的回调函数。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.ConfidentialSpace

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<Uint8Array> | 否 | 回调函数，返回接收的数据。如果传入了callback，则取消该callback的注册；如果参数为空，则取消所有callback的注册。 |

**示例：**

```typescript
import { buffer } from '@kit.ArkTS';
import { confidentialSpace } from '@kit.ConfidentialSpaceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'ConfidentialSpace';

let handle: confidentialSpace.DataAppHandle;
try {
  handle = await confidentialSpace.runApp(`/data/storage/el1/bundle/libs/arm64/libdemo_da.so`, []);
} catch (e) {
  hilog.error(0x0000, TAG, `Failed to run app. code=${e.code}, message=${e.message}`);
  return;
}

// 处理第一段接收数据
handle.onReceiveData((data: Uint8Array) => {
  hilog.info(0x0000, TAG, `Received data segment 1, length=${data.length}`);
  handle.offReceiveData();
  // 注册第二段数据接收回调
  handle.onReceiveData((data: Uint8Array) => {
    hilog.info(0x0000, TAG, `Received data segment 2, length=${data.length}`);
    handle.offReceiveData();
  });
  // 发送第二段数据
  handle.sendData(new Uint8Array(buffer.from(`Segment 2`, 'utf-8').buffer))
    .catch((e: BusinessError) => {
      hilog.error(0x0000, TAG, `Failed to send data segment 2. code=${e.code} message=${e.message}`);
    });
});

// 发送第一段数据
try {
  await handle.sendData(new Uint8Array(buffer.from(`Segment 1`, 'utf-8').buffer));
} catch (e) {
  hilog.error(0x0000, TAG, `Failed to send data segment 1. code=${e.code} message=${e.message}`);
  handle.stop();
  handle.offReceiveData();
}
```

### onReceiveDataError

public onReceiveDataError(callback: ErrorCallback<BusinessError<DataAppErrorInfo>>): void

注册处理接收数据时发生错误的回调函数。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.ConfidentialSpace

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | ErrorCallback<BusinessError<[DataAppErrorInfo](confidentialspace-confidentialspace.md#dataapperrorinfo)>> | 是 | 回调函数，返回接收数据时发生的错误。  可能产生的错误码包括1028700009、1028700010、1028700011、1028700013、1028700014。详细介绍请参见[ArkTS API错误码](errorcode-confidentialspace.md)。  若错误码为1028700014，则回调函数接收到的BusinessError对象的data字段非空，为[DataAppErrorInfo](confidentialspace-confidentialspace.md#dataapperrorinfo)类型，该对象的dataAppErrorCode字段是数据应用抛出的原始错误码。  若错误码不为1028700014，则回调函数接收到的BusinessError对象的data字段为undefined。 |

**示例：**

```typescript
import { confidentialSpace } from '@kit.ConfidentialSpaceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'ConfidentialSpace';

let handle: confidentialSpace.DataAppHandle;
try {
  handle = await confidentialSpace.runApp(`/data/storage/el1/bundle/libs/arm64/libdemo_da.so`, []);
} catch (e) {
  hilog.error(0x0000, TAG, `Failed to run app. code=${e.code}, message=${e.message}`);
  return;
}
handle.onReceiveData((data: Uint8Array) => {
  hilog.info(0x0000, TAG, `Received data, length=${data.length}`);
  handle.stop();
});
// 注册数据接收时错误回调
handle.onReceiveDataError((e: BusinessError<confidentialSpace.DataAppErrorInfo>) => {
  let msg = `Failed to receive data. code=${e.code}, message=${e.message}`;
  if (e.code === 1028700014) {
    msg += `; DA raw error code=${e.data?.dataAppErrorCode}`;
  }
  hilog.error(0x0000, TAG, msg);
});
```

### offReceiveDataError

public offReceiveDataError(callback?: ErrorCallback<BusinessError<DataAppErrorInfo>>): void

取消注册处理接收数据时发生错误的回调函数。使用callback异步回调。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.ConfidentialSpace

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | ErrorCallback<BusinessError<[DataAppErrorInfo](confidentialspace-confidentialspace.md#dataapperrorinfo)>> | 否 | 回调函数，返回接收数据时发生的错误。如果传入了callback，则取消该callback的注册。如果传入参数为空，则取消所有callback的注册。 |

**示例：**

```typescript
import { confidentialSpace } from '@kit.ConfidentialSpaceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'ConfidentialSpace';

let handle: confidentialSpace.DataAppHandle;
try {
  handle = await confidentialSpace.runApp(`/data/storage/el1/bundle/libs/arm64/libdemo_da.so`, []);
} catch (e) {
  hilog.error(0x0000, TAG, `Failed to run app. code=${e.code}, message=${e.message}`);
  return;
}
handle.onReceiveData((data: Uint8Array) => {
  hilog.info(0x0000, TAG, `Received data, length=${data.length}`);
  handle.stop();
  // 取消所有注册的回调
  handle.offReceiveData();
  handle.offReceiveDataError();
});
handle.onReceiveDataError((e: BusinessError<confidentialSpace.DataAppErrorInfo>) => {
  let msg = `Failed to receive data. code=${e.code}, message=${e.message}`;
  if (e.code === 1028700014) {
    msg += `; DA raw error code=${e.data?.dataAppErrorCode}`;
  }
  hilog.error(0x0000, TAG, msg);
});
```

## confidentialSpace.runApp

runApp(appPath: string, argv: string[]): Promise<DataAppHandle>

在机密空间中启动数据应用。使用Promise异步回调。

数据应用单次运行时长不得超过5秒（从runApp被调用起计时），超时的实例将被强制结束。创建实例后，无论实例是正常退出还是被强制结束，都需要手动调用[DataAppHandle.stop](confidentialspace-confidentialspace.md#stop)方法释放资源。

**起始版本：** 26.0.0

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Security.ConfidentialSpace

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appPath | string | 是 | 待运行的数据应用文件路径。最大长度为256，不能为空。应为应用沙箱内的绝对路径。 |
| argv | string[] | 是 | 运行数据应用进程的命令行参数。最大长度为64。取值约束：参数字符串长度之和不超过32768。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DataAppHandle](confidentialspace-confidentialspace.md#dataapphandle)> | Promise对象，返回新运行数据应用的句柄。 |

**错误码：**

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-confidentialspace.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1028700001 | Invalid argument. |
| 1028700002 | Signature file does not exist. |
| 1028700003 | Failed to start the confidential space. |
| 1028700004 | Failed to start the data app. |
| 1028700005 | Access permission denied. |
| 1028700006 | Call limit reached. |
| 1028700007 | Operation timed out. |
| 1028700012 | The profile contains invalid configuration items. |
| 1028700015 | Internal error on the client side. |
| 1028700016 | Internal error on the confidential space manager side. |
| 1028700017 | Invalid certificate of the signature file. |
| 1028700018 | The hash contained in the signature file does not match the actual hash of the data app. |
| 1028700019 | Invalid signature file format. |
| 1028700020 | The number of data app sessions exceeds the limit. |
| 1028700021 | The number of data apps exceeds the limit. |
| 1028700022 | The entry of the data app is missing or invalid. |
| 1028700023 | Failed to load dynamic library when loading the data app. |
| 1028700024 | Confidential space memory exceeds limit. |
| 1028700025 | The device is not authorized for debugging. |
| 1028700026 | The profile is not within its validity period. |
| 1028700027 | Failed to parse profile. |
| 1028700028 | Failed to verify the signature of the profile. |
| 1028700029 | The certificate chain in the profile is invalid. |
| 1028700030 | Failed to verify the signature of the signature file. |

**示例：**

```typescript
import { confidentialSpace } from '@kit.ConfidentialSpaceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'ConfidentialSpace';

try {
  let handle: confidentialSpace.DataAppHandle = await confidentialSpace.runApp(`/data/storage/el1/bundle/libs/arm64/libdemo_da.so`, []);
  hilog.info(0x0000, TAG, 'RunApp success');
} catch (e) {
  hilog.error(0x0000, TAG, `Failed to run app. code=${e.code} message=${e.message}`);
}
```
