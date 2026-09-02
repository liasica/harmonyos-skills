---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-radio
title: "@ohos.telephony.radio (网络搜索)"
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > ArkTS API > @ohos.telephony.radio (网络搜索)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:00+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c3f7ec85d7551216a7cb8e72d38f28964725d431628ac2c355563d69cbd4cb58
---

网络搜索模块提供管理网络搜索的一些基础功能，包括获取当前接入的CS域和PS域无线接入技术、获取网络状态、获取当前选网模式、获取注册网络所在国家的ISO国家码、获取主卡所在卡槽的索引号、获取指定SIM卡槽对应的注册网络信号强度信息列表、获取运营商名称，判断当前设备是否支持NR(New Radio)、判断主卡的Radio是否打开等。其中，CS(Circuit Switched)域为电路交换域，PS(Packet Switched)为分组交换域。

**说明** 

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { radio } from '@kit.TelephonyKit';
```

## radio.getRadioTech

getRadioTech(slotId: number, callback: AsyncCallback<[NetworkRadioTech](js-apis-radio.md#networkradiotech11)>): void

获取当前接入的CS域和PS域无线接入技术。使用callback异步回调。其中，CS域为电路交换域，PS为分组交换域。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<[NetworkRadioTech](js-apis-radio.md#networkradiotech11)> | 是 | 回调函数。返回当前接入的CS域和PS域无线接入技术。其中，CS域为电路交换域，PS为分组交换域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 指定卡槽ID，0表示卡槽1
let slotId: number = 0;
// 获取当前接入的CS域和PS域无线接入技术
radio.getRadioTech(slotId, (err: BusinessError, data: radio.NetworkRadioTech) => {
    if (err) {
        console.error(`getRadioTech failed, callback: err code: ${err.code}, message: ${err.message}`);
        return;
    }
    console.info(`getRadioTech success, callback: data->${JSON.stringify(data)}`);
});
```

## radio.getRadioTech

getRadioTech(slotId: number): Promise<[NetworkRadioTech](js-apis-radio.md#networkradiotech11)>

获取当前接入的CS域和PS域无线接入技术。使用Promise异步回调。其中，CS域为电路交换域，PS为分组交换域。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetworkRadioTech](js-apis-radio.md#networkradiotech11)> | 以Promise形式返回当前接入的CS域和PS域技术。CS域为电路交换域，PS为分组交换域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getRadioTech(slotId).then((data: radio.NetworkRadioTech) => {
    console.info(`getRadioTech success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getRadioTech failed, promise: err code: ${err.code}, message: ${err.message}`);
});
```

## radio.getRadioTechSync18+

getRadioTechSync(slotId: number): [NetworkRadioTech](js-apis-radio.md#networkradiotech11)

获取当前接入的CS域和PS域无线接入技术，为[getRadioTech](js-apis-radio.md#radiogetradiotech)的同步版本，直接返回结果。与异步方法getRadioTech功能相同，适用于需要立即获取结果且能接受阻塞调用的场景；若需要非阻塞调用，请使用getRadioTech。CS域为电路交换域，PS为分组交换域。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NetworkRadioTech](js-apis-radio.md#networkradiotech11) | 返回当前接入的CS域和PS域技术。CS域为电路交换域，PS为分组交换域。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
// 指定卡槽ID，0表示卡槽1
let slotId: number = 0;
try {
    // 同步获取当前接入的CS域和PS域无线接入技术
    let networkRadioTech: radio.NetworkRadioTech = radio.getRadioTechSync(slotId);
    console.info(`getRadioTechSync success, NetworkRadioTech->${JSON.stringify(networkRadioTech)}`);
} catch (err) {
    console.error(`getRadioTechSync failed, err->${JSON.stringify(err)}`);
}
```

## radio.getNetworkState

getNetworkState(callback: AsyncCallback<NetworkState>): void

获取网络状态。使用callback异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<[NetworkState](js-apis-radio.md#networkstate)> | 是 | 回调函数。返回当前网络状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

radio.getNetworkState((err: BusinessError, data: radio.NetworkState) => {
    if (err) {
        console.error(`getNetworkState failed, callback: err code: ${err.code}, message: ${err.message}`);
        return;
    }
    console.info(`getNetworkState success, callback: data->${JSON.stringify(data)}`);
});
```

## radio.getNetworkState

getNetworkState(slotId: number, callback: AsyncCallback<NetworkState>): void

获取网络状态。使用callback异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<[NetworkState](js-apis-radio.md#networkstate)> | 是 | 回调函数。返回当前网络状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getNetworkState(slotId, (err: BusinessError, data: radio.NetworkState) => {
    if (err) {
        console.error(`getNetworkState failed, callback: err code: ${err.code}, message: ${err.message}`);
        return;
    }
    console.info(`getNetworkState success, callback: data->${JSON.stringify(data)}`);
});
```

## radio.getNetworkState

getNetworkState(slotId?: number): Promise<NetworkState>

获取网络状态。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 否 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。  未指定卡槽时，默认为卡槽1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetworkState](js-apis-radio.md#networkstate)> | Promise对象，返回网络状态。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

// 指定卡槽ID，0表示卡槽1
let slotId: number = 0;
// 获取网络状态，使用Promise异步回调
radio.getNetworkState(slotId).then((data: radio.NetworkState) => {
    console.info(`getNetworkState success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getNetworkState failed, promise: err code: ${err.code}, message: ${err.message}`);
});
```

## radio.getNetworkSelectionMode

getNetworkSelectionMode(slotId: number, callback: AsyncCallback<NetworkSelectionMode>): void

获取当前选网模式。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<[NetworkSelectionMode](js-apis-radio.md#networkselectionmode)> | 是 | 回调函数。返回当前选网模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getNetworkSelectionMode(slotId, (err: BusinessError, data: radio.NetworkSelectionMode) => {
    if (err) {
        console.error(`getNetworkSelectionMode failed, callback: err code: ${err.code}, message: ${err.message}`);
        return;
    }
    console.info(`getNetworkSelectionMode success, callback: data->${JSON.stringify(data)}`);
});
```

## radio.getNetworkSelectionMode

getNetworkSelectionMode(slotId: number): Promise<NetworkSelectionMode>

获取当前选网模式。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[NetworkSelectionMode](js-apis-radio.md#networkselectionmode)> | 以Promise形式返回当前选网模式。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getNetworkSelectionMode(slotId).then((data: radio.NetworkSelectionMode) => {
    console.info(`getNetworkSelectionMode success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getNetworkSelectionMode failed, promise: err code: ${err.code}, message: ${err.message}`);
});
```

## radio.getISOCountryCodeForNetwork7+

getISOCountryCodeForNetwork(slotId: number, callback: AsyncCallback<string>): void

获取注册网络所在国家的ISO国家码。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<string> | 是 | 回调函数。返回国家码，例如：CN(中国)。如果设备没有注册任何网络，接口返回空字符串。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getISOCountryCodeForNetwork(slotId, (err: BusinessError, data: string) => {
    if (err) {
        console.error(`getISOCountryCodeForNetwork failed, callback: err code: ${err.code}, message: ${err.message}`);
        return;
    }
    console.info(`getISOCountryCodeForNetwork success, callback: data->${JSON.stringify(data)}`);
});
```

## radio.getISOCountryCodeForNetwork7+

getISOCountryCodeForNetwork(slotId: number): Promise<string>

获取注册网络所在国家的ISO国家码。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回注册网络所在国家的ISO国家码，例如CN(中国)。如果设备没有注册任何网络，接口返回空字符串。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getISOCountryCodeForNetwork(slotId).then((data: string) => {
    console.info(`getISOCountryCodeForNetwork success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getISOCountryCodeForNetwork failed, promise: err code: ${err.code}, message: ${err.message}`);
});
```

## radio.getISOCountryCodeForNetworkSync10+

getISOCountryCodeForNetworkSync(slotId: number): string

获取注册网络所在国家的ISO国家码。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回注册网络所在国家的ISO国家码，例如CN(中国)。如果设备没有注册任何网络，接口返回空字符串。 |

**示例：**

```ts
let slotId: number = 0;
try {
    let countryISO: string = radio.getISOCountryCodeForNetworkSync(slotId);
    console.info(`the country ISO is:` + countryISO);
} catch (err) {
    console.error(`getISOCountryCodeForNetworkSync failed, err->${JSON.stringify(err)}`);
}
```

## radio.getPrimarySlotId7+

getPrimarySlotId(callback: AsyncCallback<number>): void

获取主卡所在卡槽的索引号。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。返回主卡所在卡槽的索引号。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

radio.getPrimarySlotId((err: BusinessError, data: number) => {
    if (err) {
        console.error(`getPrimarySlotId failed, callback: err code: ${err.code}, message: ${err.message}`);
        return;
    }
    console.info(`getPrimarySlotId success, callback: data->${JSON.stringify(data)}`);
});
```

## radio.getPrimarySlotId7+

getPrimarySlotId(): Promise<number>

获取主卡所在卡槽的索引号。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回设备主卡所在卡槽的索引号。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

radio.getPrimarySlotId().then((data: number) => {
    console.info(`getPrimarySlotId success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getPrimarySlotId failed, promise: err code: ${err.code}, message: ${err.message}`);
});
```

## radio.getSignalInformation7+

getSignalInformation(slotId: number, callback: AsyncCallback<Array<SignalInformation>>): void

获取指定SIM卡槽对应的注册网络信号强度信息列表。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<Array<[SignalInformation](js-apis-radio.md#signalinformation)>> | 是 | 回调函数，返回从[SignalInformation](js-apis-radio.md#signalinformation)中派生出的子类对象的数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getSignalInformation(slotId, (err: BusinessError, data: Array<radio.SignalInformation>) => {
    if (err) {
        console.error(`getSignalInformation failed, callback: err code: ${err.code}, message: ${err.message}`);
        return;
    }
    console.info(`getSignalInformation success, callback: data->${JSON.stringify(data)}`);
});
```

## radio.getSignalInformation7+

getSignalInformation(slotId: number): Promise<Array<SignalInformation>>

获取指定SIM卡槽对应的注册网络信号强度信息列表。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[SignalInformation](js-apis-radio.md#signalinformation)>> | 以Promise形式返回网络信号强度[SignalInformation](js-apis-radio.md#signalinformation)子类对象的数组。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getSignalInformation(slotId).then((data: Array<radio.SignalInformation>) => {
    console.info(`getSignalInformation success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getSignalInformation failed, promise: err code: ${err.code}, message: ${err.message}`);
});
```

## radio.getSignalInformationSync10+

getSignalInformationSync(slotId: number): Array<SignalInformation>

获取指定SIM卡槽对应的注册网络信号强度信息列表。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[SignalInformation](js-apis-radio.md#signalinformation)> | 返回网络信号强度[SignalInformation](js-apis-radio.md#signalinformation)子类对象的数组。 |

**示例：**

```ts
let slotId: number = 0;
try {
    let signalInfo: Array<radio.SignalInformation> = radio.getSignalInformationSync(slotId);
    console.info(`signal information size is:` + signalInfo.length);
} catch (err) {
    console.error(`getSignalInformationSync failed, err->${JSON.stringify(err)}`);
}
```

## radio.isNrSupported(deprecated)

isNrSupported(): boolean

判断当前设备是否支持NR(New Radio)。

**说明** 

从 API version 7开始支持，从API version 9开始废弃。建议使用[isNRSupported](js-apis-radio.md#radioisnrsupported9)替代。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前设备是否支持NR。- true：支持。  - false：不支持。 |

**示例：**

```ts
let result: boolean = radio.isNrSupported();
console.info("Result: " + result);
```

## radio.isNrSupported(deprecated)

isNrSupported(slotId: number): boolean

判断当前设备是否支持NR(New Radio)。

**说明** 

从 API version 8开始支持，从API version 9开始废弃。建议使用[isNRSupported](js-apis-radio.md#radioisnrsupported9-1)替代。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前设备是否支持NR。- true：支持。  - false：不支持。 |

**示例：**

```ts
// 指定卡槽ID，0表示卡槽1
let slotId: number = 0;
// 判断当前设备是否支持NR（该接口已废弃，建议使用isNRSupported）
let result: boolean = radio.isNrSupported(slotId);
console.info("Result: " + result);
```

## radio.isNRSupported9+

isNRSupported(): boolean

判断当前设备是否支持NR(New Radio)。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前设备是否支持NR。- true：支持。  - false：不支持。 |

**示例：**

```ts
let result: boolean = radio.isNRSupported();
console.info("Result: " + result);
```

## radio.isNRSupported9+

isNRSupported(slotId: number): boolean

判断当前设备是否支持NR(New Radio)。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前设备是否支持NR。- true：支持。  - false：不支持。 |

**示例：**

```ts
let slotId: number = 0;
let result: boolean = radio.isNRSupported(slotId);
console.info("Result: " + result);
```

## radio.isRadioOn7+

isRadioOn(callback: AsyncCallback<boolean>): void

判断主卡的Radio是否打开。使用callback异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回主卡的Radio状态。  - true：Radio打开。  - false：Radio关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

radio.isRadioOn((err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`isRadioOn failed, callback: err code: ${err.code}, message: ${err.message}`);
        return;
    }
    console.info(`isRadioOn success, callback: data->${JSON.stringify(data)}`);
});
```

## radio.isRadioOn7+

isRadioOn(slotId: number, callback: AsyncCallback<boolean>): void

判断指定卡槽位的Radio是否打开。使用callback异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回指定卡槽的Radio状态。  - true：Radio打开。  - false：Radio关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.isRadioOn(slotId, (err: BusinessError, data: boolean) => {
    if (err) {
        console.error(`isRadioOn failed, callback: err code: ${err.code}, message: ${err.message}`);
        return;
    }
    console.info(`isRadioOn success, callback: data->${JSON.stringify(data)}`);
});
```

## radio.isRadioOn7+

isRadioOn(slotId?: number): Promise<boolean>

判断Radio是否打开。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_NETWORK\_INFO

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 否 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。  如果不指定slotId，默认判断主卡Radio是否打开。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise形式返回判断Radio是否打开的结果。  - true：Radio打开。  - false：Radio关闭。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.isRadioOn(slotId).then((data: boolean) => {
    console.info(`isRadioOn success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`isRadioOn failed, promise: err code: ${err.code}, message: ${err.message}`);
});
```

## radio.getOperatorName7+

getOperatorName(slotId: number, callback: AsyncCallback<string>): void

获取运营商名称。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<string> | 是 | 回调函数，返回运营商名称。例如：中国移动。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getOperatorName(slotId, (err: BusinessError, data: string) => {
    if (err) {
        console.error(`getOperatorName failed, callback: err code: ${err.code}, message: ${err.message}`);
        return;
    }
    console.info(`getOperatorName success, callback: data->${JSON.stringify(data)}`);
});
```

## radio.getOperatorName7+

getOperatorName(slotId: number): Promise<string>

获取运营商名称。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回运营商名称。例如：中国移动。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let slotId: number = 0;
radio.getOperatorName(slotId).then((data: string) => {
    console.info(`getOperatorName success, promise: data->${JSON.stringify(data)}`);
}).catch((err: BusinessError) => {
    console.error(`getOperatorName failed, promise: err code: ${err.code}, message: ${err.message}`);
});
```

## radio.getOperatorNameSync10+

getOperatorNameSync(slotId: number): string

获取运营商名称，为[getOperatorName](js-apis-radio.md#radiogetoperatorname7)的同步版本，直接返回结果。与异步方法getOperatorName功能相同，适用于需要立即获取结果且能接受阻塞调用的场景；若需要非阻塞调用，请使用getOperatorName。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回运营商名称。例如：中国移动。 |

**示例：**

```ts
// 指定卡槽ID，0表示卡槽1
let slotId: number = 0;
try {
    // 同步获取运营商名称
    let operatorName: string = radio.getOperatorNameSync(slotId);
    console.info(`operator name is:` + operatorName);
} catch (err) {
    console.error(`getOperatorNameSync failed, err->${JSON.stringify(err)}`);
}
```

## NetworkRadioTech11+

网络中PS（分组交换域）和CS（电路交换域）的无线接入技术。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| psRadioTech | [RadioTechnology](js-apis-radio.md#radiotechnology) | 否 | 否 | PS无线接入技术。 |
| csRadioTech | [RadioTechnology](js-apis-radio.md#radiotechnology) | 否 | 否 | CS无线接入技术。 |

## RadioTechnology

无线接入技术。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RADIO\_TECHNOLOGY\_UNKNOWN | 0 | 未知无线接入技术(RAT)。 |
| RADIO\_TECHNOLOGY\_GSM | 1 | 无线接入技术GSM(Global System For Mobile Communication)。 |
| RADIO\_TECHNOLOGY\_1XRTT | 2 | 无线接入技术1XRTT(Single-Carrier Radio Transmission Technology)。 |
| RADIO\_TECHNOLOGY\_WCDMA | 3 | 无线接入技术WCDMA(Wideband Code Division Multiple Access)。 |
| RADIO\_TECHNOLOGY\_HSPA | 4 | 无线接入技术HSPA(High Speed Packet Access)。 |
| RADIO\_TECHNOLOGY\_HSPAP | 5 | 无线接入技术HSPAP(High Speed Packet Access+)。 |
| RADIO\_TECHNOLOGY\_TD\_SCDMA | 6 | 无线接入技术TD\_SCDMA(TimeDivision-Synchronous Code Division Multiple Access)。 |
| RADIO\_TECHNOLOGY\_EVDO | 7 | 无线接入技术EVDO(Evolution Data Only)。 |
| RADIO\_TECHNOLOGY\_EHRPD | 8 | 无线接入技术EHRPD(Evolved High Rate Packet Data)。 |
| RADIO\_TECHNOLOGY\_LTE | 9 | 无线接入技术LTE(Long Term Evolution)。 |
| RADIO\_TECHNOLOGY\_LTE\_CA | 10 | 无线接入技术LTE\_CA(Long Term Evolution\_Carrier Aggregation)。 |
| RADIO\_TECHNOLOGY\_IWLAN | 11 | 无线接入技术IWLAN(Interworking Wireless LAN)。 |
| RADIO\_TECHNOLOGY\_NR | 12 | 无线接入技术NR(New Radio)。 |

## SignalInformation

网络信号强度信息对象。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| signalType | [NetworkType](js-apis-radio.md#networktype) | 否 | 否 | 网络信号强度类型。 |
| signalLevel | number | 否 | 否 | 网络信号强度等级，范围为[0, 5]，超出范围返回错误。 |
| dBm9+ | number | 否 | 否 | 网络信号强度，范围为[-140, 140]，超出范围返回错误。 |

## NetworkType

网络类型。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NETWORK\_TYPE\_UNKNOWN | 0 | 未知网络类型。 |
| NETWORK\_TYPE\_GSM | 1 | 网络类型为GSM(Global System For Mobile Communication)。 |
| NETWORK\_TYPE\_CDMA | 2 | 网络类型为CDMA(Code Division Multiple Access)。 |
| NETWORK\_TYPE\_WCDMA | 3 | 网络类型为WCDMA(Wideband Code Division Multiple Access)。 |
| NETWORK\_TYPE\_TDSCDMA | 4 | 网络类型为TDSCDMA(TimeDivision-Synchronous Code Division Multiple Access)。 |
| NETWORK\_TYPE\_LTE | 5 | 网络类型为LTE(Long Term Evolution)。 |
| NETWORK\_TYPE\_NR | 6 | 网络类型为NR(New Radio)。 |

## NetworkState

网络注册状态。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| longOperatorName | string | 否 | 否 | 注册网络的长运营商名称。 |
| shortOperatorName | string | 否 | 否 | 注册网络的短运营商名称。 |
| plmnNumeric | string | 否 | 否 | 注册网络的PLMN(Public Land Mobile Network，公共陆地移动网络)码。 |
| isRoaming | boolean | 否 | 否 | 是否处于漫游状态。  - true：处于漫游状态。  - false：未处于漫游状态。 |
| regState | [RegState](js-apis-radio.md#regstate) | 否 | 否 | 设备的网络注册状态。 |
| cfgTech8+ | [RadioTechnology](js-apis-radio.md#radiotechnology) | 否 | 否 | 设备的无线接入技术。 |
| nsaState | [NsaState](js-apis-radio.md#nsastate) | 否 | 否 | 设备的NSA网络注册状态。 |
| isCaActive | boolean | 否 | 否 | CA（Carrier Aggregation，载波聚合）的状态。  - true：CA已激活。  - false：CA未激活。 |
| isEmergency | boolean | 否 | 否 | 此设备是否只允许拨打紧急呼叫。 |

## RegState

网络注册状态。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| REG\_STATE\_NO\_SERVICE | 0 | 设备不能使用任何服务，包括数据业务、短信、通话等。 |
| REG\_STATE\_IN\_SERVICE | 1 | 设备可以正常使用服务，包括数据业务、短信、通话等。 |
| REG\_STATE\_EMERGENCY\_CALL\_ONLY | 2 | 设备只能使用紧急呼叫业务。 |
| REG\_STATE\_POWER\_OFF | 3 | 蜂窝无线电已关闭，modem下电，无法和网侧进行通信。 |

## NsaState

非独立组网状态。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NSA\_STATE\_NOT\_SUPPORT | 1 | 设备在不支持NSA的LTE小区下处于空闲状态或连接状态。 |
| NSA\_STATE\_NO\_DETECT | 2 | 在支持NSA但不支持NR覆盖检测的LTE小区下，设备处于空闲状态。 |
| NSA\_STATE\_CONNECTED\_DETECT | 3 | 设备在LTE小区下连接到LTE网络支持NSA和NR覆盖检测。 |
| NSA\_STATE\_IDLE\_DETECT | 4 | 支持NSA和NR覆盖检测的LTE小区下设备处于空闲状态。 |
| NSA\_STATE\_DUAL\_CONNECTED | 5 | 设备在支持NSA的LTE小区下连接到LTE + NR网络。 |
| NSA\_STATE\_SA\_ATTACHED | 6 | 设备在5GC（5G核心网）附着时在NG-RAN（下一代无线接入网）小区下空闲或连接到NG-RAN小区。 |

## NetworkSelectionMode

选网模式。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NETWORK\_SELECTION\_UNKNOWN | 0 | 未知选网模式。 |
| NETWORK\_SELECTION\_AUTOMATIC | 1 | 自动选网模式。 |
| NETWORK\_SELECTION\_MANUAL | 2 | 手动选网模式。 |

## CellInformation8+

小区信息。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| networkType | [NetworkType](js-apis-radio.md#networktype) | 否 | 否 | 获取服务单元的网络类型。 |
| signalInformation | [SignalInformation](js-apis-radio.md#signalinformation) | 否 | 否 | 信号信息。 |
