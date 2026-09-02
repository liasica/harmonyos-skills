---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/wearenginelite_api
title: wearEngineLite（穿戴设备能力开放）（Lite）
breadcrumb: API参考 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > ArkTS API > wearEngineLite（穿戴设备能力开放）（Lite）
category: harmonyos-references
scraped_at: 2026-09-02T15:02:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:1344424cd6e5afaaece9711d58f9132d05185f73c00ccece54b7888e5cda67a9
---

本模块提供穿戴设备侧三方应用订阅手表和手机连接状态的能力。

**起始版本**：6.1.1(24)

## 导入模块

```js
import WearEngineLite from '@hms.health.WearEngineLite';
```

## WearEngineLite

订阅和取消订阅手表与手机之间连接状态的基类。

### onConnectionStateChange

static onConnectionStateChange(callback: MonitorEventCallback): void

监听设备状态变化，使用callback异步回调。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Health.WearEngine.Lite

**设备行为差异：** 该接口在wearable、litewearable中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MonitorEventCallback](wearenginelite_api.md#monitoreventcallback) | 是 | 回调函数，返回设备状态的变化信息。 |

**示例：**

```js
  let eventCallback = {
    // 事件变化回调（设备连接状态变化时触发）
    eventChange: (data) => {
      console.info(`Succeeded in subscribing connection status. event: ${data.event}， data: ${data.data.data}`);
    },

    success: (code, data) => {
      console.info(`Succeeded in subscribing connection status. Code：${code.code}， data：${data.data}`);
    },

    fail: (error, errorMessage) => {
      console.error(`Failed to subscribe connection status. Code：${error.code}， data：${errorMessage.data}`);
    }
  };

  WearEngineLite.onConnectionStateChange(eventCallback);
```

### offConnectionStateChange

static offConnectionStateChange(callback?: MonitorEventCallback): void

取消监听设备状态变化，使用callback异步回调。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Health.WearEngine.Lite

**设备行为差异：** 该接口在wearable、litewearable中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [MonitorEventCallback](wearenginelite_api.md#monitoreventcallback) | 否 | 回调函数，返回MonitorEventCallback类信息。若不填写则成功取消监听事件。 |

**示例：**

```js
  let eventCallback = {
    success: (code, data) => {
      console.info(`Succeeded in unsubscribing connection status. code：${code.code}， data：${data.data}`);
    },

    fail: (error, errorMessage) => {
      console.error(`Failed to unsubscribe connection status. code:${error.code}， data:${errorMessage.data}`);
    }
  };

  WearEngineLite.offConnectionStateChange(eventCallback);
```

### onFileReceive

static onFileReceive(remoteAppInfo: AppInfo, callback: FileReceiverCallback): void

订阅对端设备向本端设备发送文件和查看文件接收进度的事件，使用callback异步回调

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Health.WearEngine.Lite

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| remoteAppInfo | [AppInfo](wearenginelite_api.md#appinfo) | 是 | 对端设备的应用信息。 |
| callback | [FileReceiverCallback](wearenginelite_api.md#filereceivercallback) | 是 | 回调函数，返回FileReceiverCallback类信息。 |

**示例：**

```js
 // 设置设备侧应用的应用信息：包名与指纹
 let remoteAppInfo = {
    bundleName: '',
    fingerprint: ''
 };
 // 设置需要接收的文件存储路径
 globalThis.__fileDir__ = 'xxxx/xxxx';
 // 设置需要接收的文件信息和传输进度
 let FileReceiverCallback =
 {
    onReceive: (fileName, filePath, progress)=>{
         console.info(`Succeeded in onFileReceiving, fileName:  ${fileName}, filePath: ${filePath}, progress: ${progress}`);
    },
    success: (code, data) => {
         console.info(`Succeeded in onFileReceiving, Code: ${code}, data:  ${data}`);
    },
    fail: (code, data) => {
         console.error(`Failed to onFileReceive, Code: ${code}, data: ${data}`);
    }
 };
 try {
    WearEngineLite.onFileReceive(remoteAppInfo, FileReceiverCallback);
 } catch (error) {
    console.error(`Failed to onFileReceive. Code: ${error.code}, message: ${error.data}.`);
 };
```

### offFileReceive

static offFileReceive(remoteAppInfo: AppInfo, callback?: FileReceiverCallback): void

取消订阅对端设备向本端设备发送文件和查看文件接收进度的事件，使用callback异步回调。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Health.WearEngine.Lite

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| remoteAppInfo | [AppInfo](wearenginelite_api.md#appinfo) | 是 | 对端设备的应用信息。 |
| callback | [FileReceiverCallback](wearenginelite_api.md#filereceivercallback) | 否 | 回调函数，返回FileReceiverCallback类信息。若不填写则成功取消订阅事件。 |

**示例：**

```js
 // 设置设备侧应用的应用信息：包名与指纹
 let remoteAppInfo = {
    bundleName: '',
    fingerprint: ''
 };
 // 设置需要接收的文件信息回调
 let fileReceiverCallback =
 {
     onReceive: (fileName, filePath, progress)=>{
         console.info(`Succeeded in offFileReceiving, fileName:  ${fileName}, filePath: ${filePath}, progress: ${progress}`);
     },
     success: (code, data) => {
         console.info(`Succeeded in offFileReceiving, Code: ${code}, data: ${data}`);
     },
     fail: (code, data) => {
         console.error(`Failed to offFileReceive, Code: ${code}, data: ${data}`);
     }
   };

 try {
    WearEngineLite.offFileReceive(remoteAppInfo, fileReceiverCallback);
 } catch (error) {
    console.error(`Failed to offFileReceive. Code: ${error.code}, message: ${error.data}.`);
 };
```

## MonitorEventCallback

作为[onConnectionStateChange](wearenginelite_api.md#onconnectionstatechange)接口的入参，当订阅监听的事件触发时，将变化后的设备状态信息传递给回调函数；作为[offConnectionStateChange](wearenginelite_api.md#offconnectionstatechange)接口的入参，用于取消监听设备连接状态的变化。

### eventChange

eventChange(data: MonitorEventData): void

监听设备状态变化的事件。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Health.WearEngine.Lite

**设备行为差异：** 该接口在wearable、litewearable中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| data | [MonitorEventData](wearenginelite_api.md#monitoreventdata) | 是 | 变化后的设备状态信息。 |

**示例：**

```js
  let eventCallback = {
    // 事件变化回调（设备连接状态变化时触发）
    eventChange: (data) => {
      console.info(`Succeeded in subscribing connection status, event: ${data.event}， data: ${data.data.data}`);
    }
  };

  WearEngineLite.onConnectionStateChange(eventCallback);
```

### success

success(code: number, data?: string): void

表示订阅成功或者是取消订阅成功。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Health.WearEngine.Lite

**设备行为差异：** 该接口在wearable、litewearable中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 返回0。 |
| data | string | 否 | 默认值undefined。 |

**示例：**

```js
  let eventCallback = {
    success: (code, data) => {
      console.info(`Succeeded in subscribing connection status, Code：${code.code}， data：${data.data}`);
    }
  };

  WearEngineLite.onConnectionStateChange(eventCallback);
```

### fail

fail(code: number, data?: string): void

表示订阅失败或者是取消订阅失败。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Health.WearEngine.Lite

**设备行为差异：** 该接口在wearable、litewearable中可正常调用，在其他设备类型中无效果。

**起始版本：** 6.1.1(24)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | Wearable返回-1，Lite Wearable返回401，表示订阅失败或取消订阅失败。  可能原因是必填参数为空（如eventChange为空）。 |
| data | string | 否 | 默认值undefined。 |

**示例：**

```js
  let eventCallback = {
    fail: (error, errorMessage) => {
      console.error(`Failed to subscribe connection status. Code：${error.code}， data：${errorMessage.data}`);
    }
  };

  WearEngineLite.onConnectionStateChange(eventCallback);
```

## MonitorData

设备的状态信息。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Health.WearEngine.Lite

**起始版本：** 6.1.1(24)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| code | number | 否 | 否 | 返回0。 |
| data | string | 否 | 是 | 设备的连接状态，2表示连接成功，3表示连接断开。 |

## MonitorEventData

作为[eventChange](wearenginelite_api.md#eventchange)的参数，当订阅监听的事件触发时，将设备状态的变化信息传递给回调函数。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Health.WearEngine.Lite

**起始版本：** 6.1.1(24)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| event | string | 否 | 否 | 回调函数上报的监听事件。 |
| data | [MonitorData](wearenginelite_api.md#monitordata) | 否 | 否 | 变化后的设备状态信息。 |

## FileReceiverCallback

作为[onFileReceive](wearenginelite_api.md#onfilereceive)接口的入参，当接收文件进度发生变化时，将变化后的文件传输进度传递给回调函数；作为[offFileReceive](wearenginelite_api.md#offfilereceive)接口的入参，用于取消订阅对端应用向本端应用发送文件的事件。

### onReceive

onReceive(fileName: string, filePath: string, progress: number): void

用于接收对端设备发送的文件和查看接收进度。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Health.WearEngine.Lite

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fileName | string | 是 | 接收文件的名称。 |
| filePath | string | 是 | 接收文件的存储路径。 |
| progress | number | 是 | 接收文件的进度，返回值范围：[0，100]。 |

**示例：**

```js
// 设置设备侧应用的应用信息：包名与指纹
 let remoteAppInfo = {
 bundleName: '',
 fingerprint: ''
    };
// 设置需要接收的文件信息回调
 let fileReceiverCallback =
 {
    onReceive: (fileName, filePath, progress)=>{
         console.info(`Succeeded in onFileReceiving, fileName:  ${fileName}, filePath: ${filePath}, progress: ${progress}`);
    },
    success: (code, data) => {
         console.info(`Succeeded in onFileReceiving, Code: ${code}, data: ${data}`);
    },
    fail: (code, data) => {
         console.error(`Failed to onFileReceive, Code: ${code}, data: ${data}`);
    }
 };

 try {
    WearEngineLite.onFileReceive(remoteAppInfo, fileReceiverCallback);
 } catch (error) {
    console.error(`Failed to onFileReceive. Code: ${error.code}, message: ${error.data}.`);
 };
```

### success

success(code: number, data?: string): void

表示文件接收事件订阅成功或者是取消订阅成功。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Health.WearEngine.Lite

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | 返回0，表示订阅成功或取消订阅成功。 |
| data | string | 否 | 默认值undefined。 |

**示例：**

```js
 // 设置设备侧应用的应用信息：包名与指纹
 let remoteAppInfo = {
 bundleName: '',
 fingerprint: ''
 };
 // 设置需要接收的文件信息回调
 let fileReceiverCallback =
 {
    onReceive: (fileName, filePath, progress)=>{
        console.info(`Succeeded in onFileReceiving, fileName:  ${fileName}, filePath: ${filePath}, progress: ${progress}`);
    },
    success: (code, data) => {
         console.info(`Succeeded in onFileReceiving, Code: ${code}, data: ${data}`);
    },
    fail: (code, data) => {
         console.error(`Failed to onFileReceive, Code: ${code}, data: ${data}`);
    }
 };

 try {
    WearEngineLite.onFileReceive(remoteAppInfo, fileReceiverCallback);
 } catch (error) {
    console.error(`Failed to onFileReceive. Code: ${error.code}, message: ${error.data}.`);
 };
```

### fail

fail(code: number, data?: string): void

表示文件接收事件订阅失败或者是取消订阅失败。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Health.WearEngine.Lite

**起始版本：** 26.0.0

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| code | number | 是 | Wearable返回-1，Lite Wearable返回401，表示订阅失败或取消订阅失败。  可能原因是必填参数为空（如onReceive为空）或参数值范围错误（如包名长度不符合规范）。 |
| data | string | 否 | 默认值undefined。 |

**示例：**

```js
// 设置设备侧应用的应用信息：包名与指纹
 let remoteAppInfo = {
    bundleName: '',
    fingerprint: ''
 };
// 设置需要接收的文件信息回调
 let fileReceiverCallback =
 {
    onReceive: (fileName, filePath, progress)=>{
        console.info(`Succeeded in onFileReceiving, fileName:  ${fileName}, filePath: ${filePath}, progress: ${progress}`);
    },
    success: (code, data) => {
        console.info(`Succeeded in onFileReceiving, Code: ${code}, data: ${data}`);
    },
    fail: (code, data) => {
        console.error(`Failed to onFileReceive, Code: ${code}, data: ${data}`);
    }
 };

 try {
    WearEngineLite.onFileReceive(remoteAppInfo, fileReceiverCallback);
 } catch (error) {
     console.error(`Failed to onFileReceive. Code: ${error.code}, message: ${error.data}.`);
 };
```

## AppInfo

设备侧应用信息类。

**模型约束：** 此接口仅可在FA模型下使用。

**系统能力：** SystemCapability.Health.WearEngine.Lite

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 否 | 应用名称。 |
| fingerprint | string | 否 | 否 | 应用指纹，用于标识应用的唯一身份。  应用指纹获取请参考[如何获取应用指纹。](../harmonyos-guides/wearengine_faq-9.md) |
