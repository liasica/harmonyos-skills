---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sms
title: "@ohos.telephony.sms (短信服务)"
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > ArkTS API > @ohos.telephony.sms (短信服务)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:4b92eeafe5aecbf4870930d1825d302d3e62ea9aab962cabe53ef7b78db069ce
---

短信服务提供了管理短信的一些基础能力，包括：

* 创建、发送短信。
* 获取发送短信的默认SIM卡槽ID。
* 检查当前设备是否具备短信发送和接收能力等。

**说明** 

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { sms } from '@kit.TelephonyKit';
```

## sms.createMessage

createMessage(pdu: Array<number>, specification: string, callback: AsyncCallback<ShortMessage>): void

根据协议数据单元(PDU)和指定的短信协议创建短信实例。使用callback异步回调。

使用场景：在接收到短信后，将系统返回的PDU数据解析为短信实例，以读取短信正文、发送者地址等内容。

**系统能力**：SystemCapability.Telephony.SmsMms

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pdu | Array<number> | 是 | 协议数据单元，从收到的信息中获取。 |
| specification | string | 是 | 短信协议类型。  - 3gpp：表示GSM/UMTS/LTE SMS。  - 3gpp2：表示CDMA SMS。 |
| callback | AsyncCallback<[ShortMessage](js-apis-sms.md#shortmessage)> | 是 | 获取短信实例的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```ts
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

const specification: string = '3gpp';
// 以数组的形式显示协议数据单元(PDU)，类型为number。
const pdu: Array<number> = [0x01, 0x00, 0x05, 0x81, 0x01, 0x80, 0xF6, 0x00, 0x00, 0x05, 0xE8, 0x32, 0x9B, 0xFD, 0x06];
sms.createMessage(pdu, specification, (err: BusinessError, data: sms.ShortMessage) => {
    if (err) {
        console.error('callback: err->${JSON.stringify(err)}');
        return;
    }
    console.info('callback: data->${JSON.stringify(data)}');
});
```

## sms.createMessage

createMessage(pdu: Array<number>, specification: string): Promise<ShortMessage>

根据协议数据单元(PDU)和指定的短信协议创建短信实例。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.SmsMms

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pdu | Array<number> | 是 | 协议数据单元，从收到的信息中获取。 |
| specification | string | 是 | 短信协议类型。  - 3gpp：表示GSM/UMTS/LTE SMS。  - 3gpp2：表示CDMA SMS。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[ShortMessage](js-apis-sms.md#shortmessage)> | 以Promise形式返回创建的短信实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```ts
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

const specification: string = '3gpp';
// 以数组的形式显示协议数据单元(PDU)，类型为number。
const pdu: Array<number> = [0x01, 0x00, 0x05, 0x81, 0x01, 0x80, 0xF6, 0x00, 0x00, 0x05, 0xE8, 0x32, 0x9B, 0xFD, 0x06];
sms.createMessage(pdu, specification).then((data: sms.ShortMessage) => {
    console.info(`createMessage success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`createMessage failed, promise: errCode:${err.code},errMsg:${err.message}`);
});
```

## sms.sendMessage(deprecated)

sendMessage(options: SendMessageOptions): void

发送短信。

**说明** 

从API version 6开始支持，从API version 10开始废弃。建议使用[sendShortMessage](js-apis-sms.md#smssendshortmessage10)替代。

**需要权限**：ohos.permission.SEND\_MESSAGES（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Telephony.SmsMms

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SendMessageOptions](js-apis-sms.md#sendmessageoptions) | 是 | 发送短信的参数和回调，参考[SendMessageOptions](js-apis-sms.md#sendmessageoptions)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```ts
import { sms } from '@kit.TelephonyKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

let sendCallback: AsyncCallback<sms.ISendShortMessageCallback> = (err: BusinessError, data: sms.ISendShortMessageCallback) => {
    if (err) {
        console.error('sendCallback: err->${JSON.stringify(err)}');
        return;
    }
    console.info('sendCallback: data->${JSON.stringify(data)}');
};
let deliveryCallback: AsyncCallback<sms.IDeliveryShortMessageCallback> = (err: BusinessError, data: sms.IDeliveryShortMessageCallback) => {
    if (err) {
        console.error('deliveryCallback: err->${JSON.stringify(err)}');
        return;
    }
    console.info('deliveryCallback: data->${JSON.stringify(data)}');
let options: sms.SendMessageOptions = {
    slotId: 0,
    content: '短信内容',
    destinationHost: '+861xxxxxxxxxx',
    serviceCenter: '+861xxxxxxxxxx',
    destinationPort: 1000,
    sendCallback: sendCallback,
    deliveryCallback: deliveryCallback
};
sms.sendMessage(options);
```

## sms.sendShortMessage10+

sendShortMessage(options: SendMessageOptions, callback: AsyncCallback<void>): void

发送短信。使用callback异步回调。

**需要权限**：ohos.permission.SEND\_MESSAGES（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Telephony.SmsMms

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SendMessageOptions](js-apis-sms.md#sendmessageoptions) | 是 | 发送短信的参数和回调，参考[SendMessageOptions](js-apis-sms.md#sendmessageoptions)。 |
| callback | AsyncCallback<void> | 是 | 发送短信的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```ts
import { sms } from '@kit.TelephonyKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

let sendCallback: AsyncCallback<sms.ISendShortMessageCallback> = (err: BusinessError, data: sms.ISendShortMessageCallback) => {
    if (err) {
        console.error('sendCallback: err->${JSON.stringify(err)}');
        return;
    }
    console.info('sendCallback: data->${JSON.stringify(data)}');
};
let deliveryCallback: AsyncCallback<sms.IDeliveryShortMessageCallback> = (err: BusinessError, data: sms.IDeliveryShortMessageCallback) => {
    if (err) {
        console.error('deliveryCallback: err->${JSON.stringify(err)}');
        return;
    }
    console.info('deliveryCallback: data->${JSON.stringify(data)}');
};
let options: sms.SendMessageOptions = {
    slotId: 0,
    content: '短信内容',
    destinationHost: '+861xxxxxxxxxx',
    serviceCenter: '+861xxxxxxxxxx',
    destinationPort: 1000,
    sendCallback: sendCallback,
    deliveryCallback: deliveryCallback
};
sms.sendShortMessage(options, (err: BusinessError) => {
    console.info(`callback: err->${JSON.stringify(err)}`);
});
```

## sms.sendShortMessage10+

sendShortMessage(options: SendMessageOptions): Promise<void>

发送短信。使用Promise异步回调。

**需要权限**：ohos.permission.SEND\_MESSAGES（该权限仅系统应用可申请）

**系统能力**：SystemCapability.Telephony.SmsMms

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SendMessageOptions](js-apis-sms.md#sendmessageoptions) | 是 | 发送短信的参数和回调，参考[SendMessageOptions](js-apis-sms.md#sendmessageoptions)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```ts
import { sms } from '@kit.TelephonyKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';

let sendCallback: AsyncCallback<sms.ISendShortMessageCallback> = (err: BusinessError, data: sms.ISendShortMessageCallback) => {
    if (err) {
        console.error('sendCallback: err->${JSON.stringify(err)}');
        return;
    }
    console.info('sendCallback: data->${JSON.stringify(data)}');
};
let deliveryCallback: AsyncCallback<sms.IDeliveryShortMessageCallback> = (err: BusinessError, data: sms.IDeliveryShortMessageCallback) => {
    if (err) {
        console.error('deliveryCallback: err->${JSON.stringify(err)}');
        return;
    }
    console.info('deliveryCallback: data->${JSON.stringify(data)}');
};
let options: sms.SendMessageOptions = {
    slotId: 0,
    content: '短信内容',
    destinationHost: '+861xxxxxxxxxx',
    serviceCenter: '+861xxxxxxxxxx',
    destinationPort: 1000,
    sendCallback: sendCallback,
    deliveryCallback: deliveryCallback
};
let promise = sms.sendShortMessage(options);
promise.then(() => {
    console.info(`sendShortMessage success`);
}).catch((err: BusinessError) => {
    console.error(`sendShortMessage failed, promise: errCode:${err.code},errMsg:${err.message}`);
});
```

## sms.getDefaultSmsSlotId7+

getDefaultSmsSlotId(callback: AsyncCallback<number>): void

获取发送短信的默认SIM卡槽ID。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.SmsMms

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 获取发送短信的默认SIM卡槽ID的回调函数。  - 0：卡槽1  - 1：卡槽2 |

**示例：**

```ts
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

sms.getDefaultSmsSlotId((err: BusinessError, data: number) => {
    if (err) {
        console.error('callback: err->${JSON.stringify(err)}');
        return;
    }
    console.info('callback: data->${JSON.stringify(data)}');
});
```

## sms.getDefaultSmsSlotId7+

getDefaultSmsSlotId(): Promise<number>

获取发送短信的默认SIM卡槽ID。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.SmsMms

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回发送短信的默认SIM卡：  - 0：卡槽1  - 1：卡槽2 |

**示例：**

```ts
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

sms.getDefaultSmsSlotId().then((data: number) => {
    console.info(`getDefaultSmsSlotId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getDefaultSmsSlotId failed, promise: errCode${err.code},errMsg:${err.message}`);
});
```

## sms.hasSmsCapability7+

hasSmsCapability(): boolean

检查当前设备是否具备短信发送和接收能力。该方法是同步方法。

**系统能力**：SystemCapability.Telephony.SmsMms

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | - true：设备具备短信发送和接收能力。  - false：设备不具备短信发送和接收能力。 |

**示例：**

```ts
import { sms } from '@kit.TelephonyKit';

let result = sms.hasSmsCapability();
console.info(`hasSmsCapability: ${JSON.stringify(result)}`);
```

## sms.getDefaultSmsSimId10+

getDefaultSmsSimId(callback: AsyncCallback<number>): void

获取发送短信的默认SIM卡ID。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.SmsMms

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 获取默认短信SIM的SIM ID的回调函数。  与SIM卡绑定，从1开始递增。  无卡时返回值为-1。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300004 | Do not have sim card. |
| 8300999 | Unknown error code. |
| 8301001 | SIM card is not activated. |

**示例：**

```ts
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

sms.getDefaultSmsSimId((err: BusinessError, data: number) => {
    if (err) {
        console.error('callback: err->${JSON.stringify(err)}');
        return;
    }
    console.info('callback: data->${JSON.stringify(data)}');
});
```

## sms.getDefaultSmsSimId10+

getDefaultSmsSimId(): Promise<number>

获取发送短信的默认SIM卡ID。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.SmsMms

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回发送短信的默认SIM卡ID：  与SIM卡绑定，从1开始递增。  无卡时返回值为-1。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300004 | Do not have sim card. |
| 8300999 | Unknown error code. |
| 8301001 | SIM card is not activated. |

**示例：**

```ts
import { sms } from '@kit.TelephonyKit';
import { BusinessError } from '@kit.BasicServicesKit';

let promise = sms.getDefaultSmsSimId();
promise.then((data: number) => {
    console.info(`getDefaultSmsSimId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getDefaultSmsSimId failed, promise: errCode:${err.code},errMsg:${err.message}`);
});
```

## ShortMessage

短信实例。

**系统能力**：SystemCapability.Telephony.SmsMms

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| hasReplyPath | boolean | 否 | 否 | 收到的短信是否包含“TP-Reply-Path”，默认为false。  - true：是  - false：否  "TP-Reply-Path"：设备根据发送SMS消息的短消息中心进行回复。 |
| isReplaceMessage | boolean | 否 | 否 | 收到的短信是否为“替换短信”，默认为false。  - true：是  - false：否  “替换短信”有关详细信息，参见 [“3GPP TS 23.040 9.2.3.9”](https://www.3gpp.org/ftp/specs/archive/23_series/23.040)。 |
| isSmsStatusReportMessage | boolean | 否 | 否 | 当前消息是否为“短信状态报告”，默认为false。  - true：是  - false：否  “短信状态报告”是一种特定格式的短信，被用来从Service Center到Mobile Station传输状态报告。 |
| messageClass | [ShortMessageClass](js-apis-sms.md#shortmessageclass) | 否 | 否 | 短信类型。 |
| pdu | Array<number> | 否 | 否 | SMS消息中的协议数据单元(PDU)。 |
| protocolId | number | 否 | 否 | 发送短信时使用的协议标识。 |
| scAddress | string | 否 | 否 | 短信服务中心(SMSC)地址。 |
| scTimestamp | number | 否 | 否 | SMSC时间戳。单位：ms。以UTC时间为基准的毫秒数 |
| status | number | 否 | 否 | SMS-STATUS-REPORT消息中的短信状态指示短信服务中心(SMSC)发送的短信状态。 |
| visibleMessageBody | string | 否 | 否 | 短信正文。 |
| visibleRawAddress | string | 否 | 否 | 发送者地址。 |

## ShortMessageClass

短信类型。

**系统能力**：SystemCapability.Telephony.SmsMms

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 未知类型。 |
| INSTANT\_MESSAGE | 1 | 即时消息，收到后立即显示。 |
| OPTIONAL\_MESSAGE | 2 | 存储在设备或SIM卡上的短信。 |
| SIM\_MESSAGE | 3 | 包含SIM卡信息的短信，需要存储在SIM卡中。 |
| FORWARD\_MESSAGE | 4 | 要转发到另一台设备的短信。 |

## SendMessageOptions

发送短信的参数和回调。根据SendMessageOptions中的参数content的值判断短信类型。

**系统能力**：SystemCapability.Telephony.SmsMms

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| slotId | number | 否 | 否 | 用于发送短信的SIM卡槽ID：  - 0：卡槽1  - 1：卡槽2 |
| destinationHost | string | 否 | 否 | 短信的发送地址，格式为带国家代码的手机号，如'+861xxxxxxxxxx'。 |
| content | string | Array<number> | 否 | 否 | 如果内容是字符串，则这是一条文本短信。如果内容是字节数组，则这是一条数据短信。 |
| serviceCenter | string | 否 | 是 | 短信中心地址，格式为带国家代码的手机号。默认使用SIM卡中的短信中心地址。 |
| destinationPort | number | 否 | 是 | 如果发送数据短信，destinationPort 是必需的。否则是可选的，不传入时不设置数据端口。 |
| sendCallback | AsyncCallback<[ISendShortMessageCallback](js-apis-sms.md#isendshortmessagecallback)> | 否 | 是 | 短信发送结果回调，返回短信发送的结果，参考[ISendShortMessageCallback](js-apis-sms.md#isendshortmessagecallback)。发送数据短信时，此项必填；发送文本短信时，此项可选，不填写则不会收到短信发送结果的回调通知。 |
| deliveryCallback | AsyncCallback<[IDeliveryShortMessageCallback](js-apis-sms.md#ideliveryshortmessagecallback)> | 否 | 是 | 短信送达结果回调，返回短信递送报告，参考[IDeliveryShortMessageCallback](js-apis-sms.md#ideliveryshortmessagecallback)。发送数据短信时，此项必填；发送文本短信时，此项可选，不填写则不会收到短信送达报告的回调通知。 |

## ISendShortMessageCallback

回调实例。返回短信发送结果、存储已发送短信的URI和是否为长短信的最后一部分。

**系统能力**：SystemCapability.Telephony.SmsMms

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isLastPart | boolean | 否 | 否 | 指定这是否是长短信的最后一部分。默认为false。  -true：是  -false：否 |
| result | [SendSmsResult](js-apis-sms.md#sendsmsresult) | 否 | 否 | 短信发送结果。 |
| url | string | 否 | 否 | 存储发送短信的URI。 |

## IDeliveryShortMessageCallback

回调实例，返回短信送达报告。

**系统能力**：SystemCapability.Telephony.SmsMms

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pdu | Array<number> | 否 | 否 | 短信送达报告。 |

## SendSmsResult

短信发送结果。

**系统能力**：SystemCapability.Telephony.SmsMms

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SEND\_SMS\_SUCCESS | 0 | 发送短信成功。 |
| SEND\_SMS\_FAILURE\_UNKNOWN | 1 | 发送短信失败，原因未知。 |
| SEND\_SMS\_FAILURE\_RADIO\_OFF | 2 | 发送短信失败，原因为调制解调器关机。 |
| SEND\_SMS\_FAILURE\_SERVICE\_UNAVAILABLE | 3 | 发送短信失败，原因为网络不可用、不支持发送或接收短信。 |
