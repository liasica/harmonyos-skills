---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-connectedtag
title: "@ohos.connectedTag (有源标签)"
breadcrumb: API参考 > 系统 > 网络 > Connectivity Kit（短距通信服务） > ArkTS API > @ohos.connectedTag (有源标签)
category: harmonyos-references
scraped_at: 2026-09-02T15:01:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:77c0612f7812e1812d05b05863aeb911c25eee9b8ff7b2ea4101ddd80ab6ba5e
---

本模块提供有源标签的使用，包括初始化有源标签芯片、读取有源标签内容、写入内容到有源标签等。

**说明** 

本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import { connectedTag } from '@kit.ConnectivityKit';
```

## connectedTag.init(deprecated)

init(): boolean

初始化有源标签芯片。

**说明** 

从API version 8开始支持，从API version 9开始废弃，建议使用[initialize](js-apis-connectedtag.md#connectedtaginitialize9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true：初始化成功。  false：初始化失败。 |

## connectedTag.initialize9+

initialize(): void

初始化有源标签芯片。对有源标签进行读写操作前需调用本接口初始化一次，若想再次初始化需先调用[uninitialize](js-apis-connectedtag.md#connectedtaguninitialize9)。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';

try {
    console.info("connectedTag initialize");
    connectedTag.initialize();
} catch (error) {
    console.error("initialize error:" + error);
}
```

## connectedTag.uninit(deprecated)

uninit(): boolean

卸载有源标签芯片资源。

**说明** 

从API version 8开始支持，从API version 9开始废弃，建议使用[uninitialize](js-apis-connectedtag.md#connectedtaguninitialize9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**返回值：**

| **类型** | **说明** |
| --- | --- |
| boolean | true：卸载操作成功。  false：卸载操作失败。 |

## connectedTag.uninitialize9+

uninitialize(): void

卸载有源标签芯片资源。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';

try {
    console.info("connectedTag uninitialize");
    connectedTag.uninitialize();
} catch (error) {
    console.error("connectedTag error: " + error);
}
```

## connectedTag.readNdefTag(deprecated)

readNdefTag(): Promise<string>

读取有源标签内容。使用Promise异步回调。

**说明** 

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.read](js-apis-connectedtag.md#connectedtagread9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<string> | Promise对象，返回读取有源标签内容的列表。 |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

connectedTag.readNdefTag().then((data) => {
    console.info("connectedTag readNdefTag Promise data = " + data);
}).catch((err: BusinessError)=> {
    console.error("connectedTag readNdefTag Promise err: " + err);
});
```

## connectedTag.read9+

read(): Promise<number[]>

读取有源标签内容。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<number[]> | Promise对象，返回读取有源标签内容的列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

connectedTag.read().then((data) => {
    console.info("connectedTag read Promise data = " + data);
}).catch((err: BusinessError)=> {
    console.error("connectedTag read Promise err: " + err);
});
```

## connectedTag.readNdefTag(deprecated)

readNdefTag(callback: AsyncCallback<string>): void

读取有源标签内容，使用AsyncCallback方式作为异步方法。

**说明** 

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.read](js-apis-connectedtag.md#connectedtagread9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| callback | AsyncCallback<string> | 是 | 回调函数。当读取成功时data为读取到有源标签的内容；否则为err错误对象。 |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';

connectedTag.readNdefTag((err, data)=> {
    if (err) {
        console.error("connectedTag readNdefTag AsyncCallback err: " + err);
    } else {
        console.info("connectedTag readNdefTag AsyncCallback data: " + data);
    }
});
```

## connectedTag.read9+

read(callback: AsyncCallback<number[]>): void

读取有源标签内容，使用AsyncCallback方式作为异步方法。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| callback | AsyncCallback<number[]> | 是 | 回调函数。当读取成功时data为读取到有源标签的内容；否则为err错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';

connectedTag.read((err, data)=> {
    if (err) {
        console.error("connectedTag read AsyncCallback err: " + err);
    } else {
        console.info("connectedTag read AsyncCallback data: " + data);
    }
});
```

## connectedTag.writeNdefTag(deprecated)

writeNdefTag(data: string): Promise<void>

写入内容到有源标签。使用Promise异步回调。

**说明** 

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.write](js-apis-connectedtag.md#connectedtagwrite9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| data | string | 是 | 有源标签内容，最大长度为1024个字节。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rawData = "010203"; // change it to be correct.
connectedTag.writeNdefTag(rawData).then(() => {
    console.info("connectedTag.writeNdefTag Promise success.");
}).catch((err: BusinessError)=> {
    console.error("connectedTag.writeNdefTag Promise err: " + err);
});
```

## connectedTag.write9+

write(data: number[]): Promise<void>

写入内容到有源标签。使用Promise异步回调。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| data | number[] | 是 | 有源标签内容，由十六进制数字组成。范围：0x00至0xFF。 |

**返回值：**

| **类型** | **说明** |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

let rawData = [0x01, 0x02, 0x03]; // change it to be correct.
connectedTag.write(rawData).then(() => {
    console.info("connectedTag.write Promise success.");
}).catch((err: BusinessError)=> {
    console.error("connectedTag.write Promise err: " + err);
});
```

## connectedTag.writeNdefTag(deprecated)

writeNdefTag(data: string, callback: AsyncCallback<void>): void

写入内容到有源标签，使用AsyncCallback方式作为异步方法。

**说明** 

从 API version 8 开始支持，从 API version 9 开始废弃，建议使用[connectedTag.write](js-apis-connectedtag.md#connectedtagwrite9)替代。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| data | string | 是 | 有源标签内容，最大长度为1024个字节。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当写入标签成功，err为undefined，否则为错误对象。 |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';

let rawData = "010203"; // change it to be correct.
connectedTag.writeNdefTag(rawData, (err)=> {
    if (err) {
        console.error("connectedTag.writeNdefTag AsyncCallback err: " + err);
    } else {
        console.info("connectedTag.writeNdefTag AsyncCallback success.");
    }
});
```

## connectedTag.write9+

write(data: number[], callback: AsyncCallback<void>): void

写入内容到有源标签，使用AsyncCallback方式作为异步方法。

**需要权限：** ohos.permission.NFC\_TAG

**系统能力：** SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| data | number[] | 是 | 有源标签内容，由十六进制数字组成。范围：0x00至0xFF。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当写入标签成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[NFC错误码](errorcode-nfc.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | The parameter check failed. Possible causes:  1. Mandatory parameters are left unspecified.  2. Incorrect parameters types.  3. Parameter verification failed. |
| 801 | Capability not supported. |
| 3200101 | Connected NFC tag running state is abnormal in service. |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';

let rawData = [0x01, 0x02, 0x03]; // change it to be correct.
connectedTag.write(rawData, (err)=> {
    if (err) {
        console.error("connectedTag.write AsyncCallback err: " + err);
    } else {
        console.info("connectedTag.write AsyncCallback success.");
    }
});
```

## connectedTag.on('notify')

on(type: "notify", callback: Callback<number>): void

注册NFC场强状态事件。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"notify"字符串。 |
| callback | Callback<number> | 是 | 回调函数。注册成功的返回值参见[NfcRfType](js-apis-connectedtag.md#nfcrftype)。 |

## connectedTag.off('notify')

off(type: "notify", callback?: Callback<number>): void

取消NFC场强状态事件的注册。

**需要权限**：ohos.permission.NFC\_TAG

**系统能力**：SystemCapability.Communication.ConnectedTag

**参数：**

| **参数名** | **类型** | **必填** | **说明** |
| --- | --- | --- | --- |
| type | string | 是 | 固定填"notify"字符串。 |
| callback | Callback<number> | 否 | 状态改变回调函数。如果callback不填，将“去注册”该事件关联的所有回调函数。 |

**示例：**

```js
import { connectedTag } from '@kit.ConnectivityKit';

function nfcStatusCb(rfState: connectedTag.NfcRfType) {
    console.info("connectedTag on Callback rfState: ", rfState);
}

// 有源NFC标签的使用流程
async function nfcTagTestOn(): Promise<void> {
    try {
        console.info("connectedTag initialize");
        connectedTag.initialize();
    } catch (error) {
        console.error("initialize error:" + error);
    }
    // 注册回调以接收nfc进离场状态更改通知
    connectedTag.on("notify", nfcStatusCb);
    try {
        let tag = [3, 1, 0];
        console.info("connectedTag write: tag=" + tag);
        await connectedTag.write(tag);
        let data = await connectedTag.read();
        console.info("connectedTag read: data=" + data);
    } catch (error) {
        console.error("connectedTag error: " + error);
    }
}

// 业务退出时，取消注册回调、取消初始化
async function nfcTagTestOff(): Promise<void> {
    // 取消注册回调
    connectedTag.off("notify", nfcStatusCb);
    try {
        console.info("connectedTag uninitialize");
        connectedTag.uninitialize();
    } catch (error) {
        console.error("connectedTag error: " + error);
    }
}
```

## NfcRfType

表示NFC场强状态的枚举。

**系统能力**：SystemCapability.Communication.ConnectedTag

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NFC\_RF\_LEAVE | 0 | NFC离场事件。 |
| NFC\_RF\_ENTER | 1 | NFC进场事件。 |
