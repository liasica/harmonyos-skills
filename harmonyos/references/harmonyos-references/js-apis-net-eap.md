---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-net-eap
title: "@ohos.net.eap (扩展认证)"
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > ArkTS API > @ohos.net.eap (扩展认证)
category: harmonyos-references
scraped_at: 2026-11-12T09:55:40+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:31eb27de32f6adef5582e5b5c8f0288a3700b44a8c8c4205f2d28ee48bbbca67
---

该模块提供了第三方客户端接入802.1X认证（一种基于端口的网络接入控制协议）流程的机制，支撑客户端的定制认证等功能，同时提供以太网802.1X EAP配置管理、认证控制和认证状态监听功能。

**说明** 

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```js
import {eap} from '@kit.NetworkKit';
```

## eap.regCustomEapHandler

regCustomEapHandler(netType: number, eapCode: number, eapType: number, callback: Callback<EapData>): void

用于指定需要定制化处理的EAP报文类型和对应的处理callback。使用callback异步回调。

系统会将符合条件的EAP报文送入callback函数中供企业应用获取。

**需要权限**：ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION

**系统能力**：SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netType | number | 是 | 网络类型，取值为1或2。  netType=1表示WLAN（WLAN仅支持PC/2in1），netType=2表示以太网。 |
| eapCode | number | 是 | 需要进行定制的EAP code，取值为1、2、3、4 。  code=1 Request、 code=2 Response、 code=3 Success、 code=4 Failure。 |
| eapType | number | 是 | 需要进行定制处理的EAP method类型，取值范围[0, 255]。  常用取值包括：eapType=1 Identity，eapType=2 Notification，eapType=3 NAK，eapType=4 MD5-Challenge，eapType=5 OTP（One-Time Password），eapType=6 GTC（Generic Token Card），eapType=13 EAP-TLS，eapType=21 EAP-TTLS，eapType=25 EAP-PEAP，eapType=254 Expanded Types，eapType=255 Experimental use。 |
| callback | Callback<[EapData](js-apis-net-eap.md#eapdata)> | 是 | 回调函数，返回指定的eapCode+eapType的报文。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[扩展认证错误码](errorcode-net-eap.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 33200006 | Invalid net type. |
| 33200007 | Invalid eap code. |
| 33200008 | Invalid eap type. |
| 33200009 | netmanager stop. |
| 33200099 | internal error. |

**示例：**

```js
import {eap} from '@kit.NetworkKit';
let netType = 1;
let eapCode = 1;
let eapType = 25;
let eapData = (eapData:eap.EapData):void => {
  console.info("rsp result", JSON.stringify(eapData));
};

eap.regCustomEapHandler(netType, eapCode, eapType, eapData);
console.info('regCustomEapHandler success');
```

## eap.unregCustomEapHandler

unregCustomEapHandler(netType:number, eapCode: number, eapType: number, callback: Callback<EapData>): void

用于指定需要取消定制化处理的EAP报文类型和对应的处理callback。使用callback异步回调。

**需要权限**：ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION

**系统能力**：SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netType | number | 是 | 网络类型，取值为1或2。  netType=1表示WLAN（WLAN仅支持PC/2in1），netType=2表示以太网。 |
| eapCode | number | 是 | 需要进行定制的EAP code，取值为1、2、3、4 。  code=1 Request、 code=2 Response、 code=3 Success、 code=4 Failure。 |
| eapType | number | 是 | 需要进行定制处理的EAP method类型，取值范围[0, 255]。  常用取值包括：eapType=1 Identity，eapType=2 Notification，eapType=3 NAK，eapType=4 MD5-Challenge，eapType=5 OTP（One-Time Password），eapType=6 GTC（Generic Token Card），eapType=13 EAP-TLS，eapType=21 EAP-TTLS，eapType=25 EAP-PEAP，eapType=254 Expanded Types，eapType=255 Experimental use。 |
| callback | Callback<[EapData](js-apis-net-eap.md#eapdata)> | 是 | 回调函数，返回指定的eapCode+eapType的报文。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[扩展认证错误码](errorcode-net-eap.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 33200006 | Invalid net type. |
| 33200007 | Invalid eap code. |
| 33200008 | Invalid eap type. |
| 33200009 | netmanager stop. |
| 33200099 | internal error. |

**示例：**

```js
import {eap} from '@kit.NetworkKit';
let netType = 1;
let eapCode = 1;
let eapType = 25;
let eapData = (eapData:eap.EapData):void => {
  console.info("rsp result", JSON.stringify(eapData));
};

eap.unregCustomEapHandler(netType, eapCode, eapType, eapData);
console.info('unregCustomEapHandler success');
```

## eap.replyCustomEapData

replyCustomEapData(result: CustomResult, data: EapData): void

该接口用于通知系统已完成该步定制化处理。

**说明** 

* 若用于处理收EAP数据包(rx)时的callback，传给系统的EAP数据需要剥离服务器添加的定制部分。
* 若用于处理发EAP数据包(tx)时的callback，传给系统的EAP数据为经过添加定制部分后的EAP数据。

**需要权限**：ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION

**系统能力**：SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | [CustomResult](js-apis-net-eap.md#customresult) | 是 | 定制化判定结果。 |
| data | [EapData](js-apis-net-eap.md#eapdata) | 是 | 经过定制化的EAP数据。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[扩展认证错误码](errorcode-net-eap.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 33200004 | Invalid result. |
| 33200005 | Invalid size of eap data. |
| 33200009 | netmanager stop. |
| 33200099 | internal error. |

```js
import {eap} from '@kit.NetworkKit';
let eapData:eap.EapData= {
  msgId: 1,
  eapBuffer: new Uint8Array([1, 2, 3, 4, 5]),
  bufferLen: 5,
};
let result = 1;

try {
  eap.replyCustomEapData(result, eapData);
  console.info('replyCustomEapData success');
} catch (err) {
  console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```

## eap.startEthEap

startEthEap(netId: number, profile: EthEapProfile): void

该接口用于指定一个以太网卡发起EAP认证。

**需要权限**：ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION

**系统能力**：SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netId | number | 是 | 以太网卡Id。（传入默认参数-1，系统将自动匹配以太网卡发起EAP认证） |
| profile | [EthEapProfile](js-apis-net-eap.md#etheapprofile) | 是 | EAP配置信息。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[扩展认证错误码](errorcode-net-eap.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 33200001 | Invalid netId. |
| 33200003 | Invalid profile. |
| 33200009 | netmanager stop. |
| 33200010 | invalid eth state. |
| 33200099 | internal error. |

**示例：**

```js
import {eap} from '@kit.NetworkKit';
let netId = 100;
let profile: eap.EthEapProfile = {
  eapMethod: eap.EapMethod.EAP_TTLS,
  phase2Method: eap.Phase2Method.PHASE2_AKA_PRIME,
  identity: "identity",
  anonymousIdentity: "anonymousIdentity",
  password: "password",
  caCertAliases: "caCertAliases",
  caPath: "caPath",
  clientCertAliases: "clientCertAliases",
  certEntry: new Uint8Array([5,6,7,8,9,10]),
  certPassword: "certPassword",
  altSubjectMatch: "altSubjectMatch",
  domainSuffixMatch: "domainSuffixMatch",
  realm: "realm",
  plmn: "plmn",
  eapSubId: 1
};
    
try {
  eap.startEthEap(netId, profile);
  console.info('startEthEap success');
} catch (err) {
  console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```

## eap.logOffEthEap

logOffEthEap(netId: number): void

该接口用于指定一个以太网卡从EAP已认证状态退出。

**需要权限**：ohos.permission.MANAGE\_ENTERPRISE\_WIFI\_CONNECTION

**系统能力**：SystemCapability.Communication.NetManager.Eap

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| netId | number | 是 | 以太网卡Id。（传入默认参数-1，系统将自动匹配以太网卡发起EAP认证） |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[扩展认证错误码](errorcode-net-eap.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |
| 33200001 | Invalid netId. |
| 33200002 | Log off fail. |
| 33200009 | netmanager stop. |
| 33200010 | invalid eth state. |
| 33200099 | internal error. |

**示例：**

```js
import {eap} from '@kit.NetworkKit';
let netId = 100;
try{
  eap.logOffEthEap(netId);
  console.info("logOffEthEap success");
} catch (err) {
  console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
}
```

## eap.setEthEapConfig

setEthEapConfig(config: EthEapConfig): void

设置以太网802.1X认证配置，配置将加密并持久化保存。

多次调用本接口时，若config参数中任意字段发生变化，会触发一次自动认证流程。如果802.1X功能或自动认证已禁用，则保存配置并停止自动认证；如果当前认证由企业应用通过[eap.startEthEap](js-apis-net-eap.md#eapstartetheap)发起，则仅保存配置，不触发自动认证，企业应用仍保留认证控制权。认证结果通过[eap.onStateChange](js-apis-net-eap.md#eaponstatechange)注册的回调返回，本接口调用返回不代表认证成功。

**起始版本：** 26.0.1

**需要权限**：ohos.permission.ENTERPRISE\_MANAGE\_EAP

**系统能力**：SystemCapability.Communication.NetManager.Eap

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | [EthEapConfig](js-apis-net-eap.md#etheapconfig) | 是 | 待设置的以太网802.1X认证配置。当EthEapProfile中的敏感字段password、certPassword传入空字符串，或certEntry传入空数组时，表示保留原值；通过getEthEapConfig读取时，password、certPassword返回空字符串，certEntry返回空数组。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ts
import { eap } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

// 请根据实际认证环境替换身份、密码和证书等配置。
let profile: eap.EthEapProfile = {
  eapMethod: eap.EapMethod.EAP_PEAP,
  phase2Method: eap.Phase2Method.PHASE2_MSCHAPV2,
  identity: 'identity',
  anonymousIdentity: '',
  password: 'password',
  caCertAliases: 'caCertAliases',
  caPath: '',
  clientCertAliases: '',
  certEntry: new Uint8Array(0),
  certPassword: '',
  altSubjectMatch: '',
  domainSuffixMatch: 'example.com',
  realm: '',
  plmn: '',
  eapSubId: 0
};
let config: eap.EthEapConfig = {
  profile: profile,
  enabled: true,
  autoAuth: true,
  locked: false
};

try {
  eap.setEthEapConfig(config);
  console.info('setEthEapConfig success');
} catch (error) {
  let err = error as BusinessError;
  console.error(`setEthEapConfig failed. Code: ${err.code}, message: ${err.message}`);
}
```

## eap.getEthEapConfig

getEthEapConfig(): Promise<EthEapConfig>

获取已保存的以太网802.1X认证配置。使用Promise异步回调。

返回配置中profile的敏感字段password、certPassword始终为空字符串，certEntry始终为空数组。

**起始版本：** 26.0.1

**需要权限**：ohos.permission.ENTERPRISE\_MANAGE\_EAP

**系统能力**：SystemCapability.Communication.NetManager.Eap

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[EthEapConfig](js-apis-net-eap.md#etheapconfig)> | Promise对象，返回已保存的以太网802.1X认证配置，其中password、certPassword返回空字符串，certEntry返回空数组。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ts
import { eap } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  eap.getEthEapConfig().then((config: eap.EthEapConfig) => {
    console.info(`enabled: ${config.enabled}, autoAuth: ${config.autoAuth}, locked: ${config.locked}`);
  }).catch((err: BusinessError) => {
    console.error(`getEthEapConfig failed. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let err = error as BusinessError;
  console.error(`getEthEapConfig failed. Code: ${err.code}, message: ${err.message}`);
}
```

## eap.deleteEthEapConfig

deleteEthEapConfig(): Promise<void>

删除已持久化保存的以太网802.1X EAP配置。若当前存在正在进行的自动认证，则会停止本次认证流程。使用Promise异步回调。

**起始版本：** 26.0.1

**需要权限**：ohos.permission.ENTERPRISE\_MANAGE\_EAP

**系统能力**：SystemCapability.Communication.NetManager.Eap

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ts
import { eap } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  eap.deleteEthEapConfig().then(() => {
    console.info('deleteEthEapConfig success');
  }).catch((err: BusinessError) => {
    console.error(`deleteEthEapConfig failed. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let err = error as BusinessError;
  console.error(`deleteEthEapConfig failed. Code: ${err.code}, message: ${err.message}`);
}
```

## eap.getEthEapStateInfo

getEthEapStateInfo(): EthEapStateInfo

同步获取当前以太网802.1X认证状态信息，包括认证状态、重试次数和补充信息。

**起始版本：** 26.0.1

**需要权限**：ohos.permission.ENTERPRISE\_MANAGE\_EAP

**系统能力**：SystemCapability.Communication.NetManager.Eap

**模型约束：** 此接口仅可在Stage模型下使用。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [EthEapStateInfo](js-apis-net-eap.md#etheapstateinfo) | 当前以太网802.1X认证状态信息。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ts
import { eap } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let stateInfo: eap.EthEapStateInfo = eap.getEthEapStateInfo();
  console.info(`state: ${stateInfo.state}, retryCount: ${stateInfo.retryCount}`);
} catch (error) {
  let err = error as BusinessError;
  console.error(`getEthEapStateInfo failed. Code: ${err.code}, message: ${err.message}`);
}
```

## eap.onStateChange

onStateChange(callback: Callback<EthEapStateInfo>): void

订阅以太网802.1X认证状态变化。使用callback异步回调。

**起始版本：** 26.0.1

**需要权限**：ohos.permission.ENTERPRISE\_MANAGE\_EAP

**系统能力**：SystemCapability.Communication.NetManager.Eap

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[EthEapStateInfo](js-apis-net-eap.md#etheapstateinfo)> | 是 | 回调函数，返回以太网802.1X认证状态信息。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ts
import { eap } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callback = (stateInfo: eap.EthEapStateInfo): void => {
  console.info(`state: ${stateInfo.state}, retryCount: ${stateInfo.retryCount}`);
};

try {
  eap.onStateChange(callback);
  console.info('onStateChange success');
} catch (error) {
  let err = error as BusinessError;
  console.error(`onStateChange failed. Code: ${err.code}, message: ${err.message}`);
}
```

## eap.offStateChange

offStateChange(callback?: Callback<EthEapStateInfo>): void

取消订阅以太网802.1X认证状态变化。

**起始版本：** 26.0.1

**需要权限**：ohos.permission.ENTERPRISE\_MANAGE\_EAP

**系统能力**：SystemCapability.Communication.NetManager.Eap

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[EthEapStateInfo](js-apis-net-eap.md#etheapstateinfo)> | 否 | 待取消的回调函数，应与订阅时传入的回调函数为同一对象。不传入时，取消该事件的所有回调。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ts
import { eap } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

let callback = (stateInfo: eap.EthEapStateInfo): void => {
  console.info(`state: ${stateInfo.state}, retryCount: ${stateInfo.retryCount}`);
};

try {
  eap.onStateChange(callback);
  // 不再需要监听时，传入订阅时使用的同一个回调函数。
  eap.offStateChange(callback);
  // 不传入回调函数时，取消该事件的所有回调。
  eap.offStateChange();
  console.info('offStateChange success');
} catch (error) {
  let err = error as BusinessError;
  console.error(`offStateChange failed. Code: ${err.code}, message: ${err.message}`);
}
```

## eap.connect

connect(action: EthEapConnectAction): Promise<void>

手动触发或断开以太网802.1X认证。使用Promise异步回调。

当action为ACTION\_CONNECT时，使用已保存的802.1X认证配置重新触发认证；未保存802.1X认证配置时，操作失败。认证结果通过[eap.onStateChange](js-apis-net-eap.md#eaponstatechange)注册的回调返回。若当前认证由企业应用通过eap.startEthEap发起，则本接口不生效，仍保持原有认证。

当action为ACTION\_DISCONNECT时，停止自动认证及重试，退出当前以太网802.1X认证，并将认证状态重置为[STATE\_IDLE](js-apis-net-eap.md#etheapstate)。

**起始版本：** 26.0.1

**需要权限**：ohos.permission.ENTERPRISE\_MANAGE\_EAP

**系统能力**：SystemCapability.Communication.NetManager.Eap

**模型约束：** 此接口仅可在Stage模型下使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | [EthEapConnectAction](js-apis-net-eap.md#etheapconnectaction) | 是 | 手动连接操作：ACTION\_CONNECT表示重新触发认证，ACTION\_DISCONNECT表示断开认证。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission denied. |

**示例：**

```ts
import { eap } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // 调用前需先通过setEthEapConfig保存配置。
  // 如需断开认证，将action替换为eap.EthEapConnectAction.ACTION_DISCONNECT。
  eap.connect(eap.EthEapConnectAction.ACTION_CONNECT).then(() => {
    console.info('connect request completed');
  }).catch((err: BusinessError) => {
    console.error(`connect failed. Code: ${err.code}, message: ${err.message}`);
  });
} catch (error) {
  let err = error as BusinessError;
  console.error(`connect failed. Code: ${err.code}, message: ${err.message}`);
}
```

## EapData

EAP信息。

​**系统能力​**：SystemCapability.Communication.NetManager.Eap

| **名称** | **类型** | **只读** | **可选** | **说明** |
| --- | --- | --- | --- | --- |
| msgId | number | 否 | 否 | 伪随机数，用于关联处理前后的EAP数据。 |
| eapBuffer | Uint8Array | 否 | 否 | 从EAP header开始的EAP原始数据，未加密。 |
| bufferLen | number | 否 | 否 | 数据长度。 |

## CustomResult

表示EAP认证处理结果的枚举。

​**系统能力​**：SystemCapability.Communication.NetManager.Eap

| **名称** | **值** | **说明** |
| --- | --- | --- |
| RESULT\_FAIL | 0 | 认证流程结束，结果失败。 |
| RESULT\_NEXT | 1 | 认证当前流程成功，跳转到下一步。 |
| RESULT\_FINISH | 2 | 认证流程结束，结果成功。 |

## EapMethod

表示EAP认证方式的枚举。

**系统能力**：SystemCapability.Communication.NetManager.Eap

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EAP\_NONE | 0 | 不指定。 |
| EAP\_PEAP | 1 | PEAP类型。 |
| EAP\_TLS | 2 | TLS类型。 |
| EAP\_TTLS | 3 | TTLS类型。 |
| EAP\_PWD | 4 | PWD类型。 |
| EAP\_SIM | 5 | SIM类型。 |
| EAP\_AKA | 6 | AKA类型。 |
| EAP\_AKA\_PRIME | 7 | AKA Prime类型。 |
| EAP\_UNAUTH\_TLS | 8 | UNAUTH TLS类型。 |

## Phase2Method

表示第二阶段认证方式的枚举。

**系统能力**：SystemCapability.Communication.NetManager.Eap

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PHASE2\_NONE | 0 | 不指定。 |
| PHASE2\_PAP | 1 | PAP类型。 |
| PHASE2\_MSCHAP | 2 | MSCHAP类型。 |
| PHASE2\_MSCHAPV2 | 3 | MSCHAPV2类型。 |
| PHASE2\_GTC | 4 | GTC类型。 |
| PHASE2\_SIM | 5 | SIM类型。 |
| PHASE2\_AKA | 6 | AKA类型。 |
| PHASE2\_AKA\_PRIME | 7 | AKA Prime类型。 |

## EthEapProfile

可扩展身份验证协议配置信息。

**系统能力：** SystemCapability.Communication.NetManager.Eap

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eapMethod | [EapMethod](js-apis-net-eap.md#eapmethod) | 否 | 否 | EAP认证方式。 |
| phase2Method | [Phase2Method](js-apis-net-eap.md#phase2method) | 否 | 否 | 第二阶段认证方式。 |
| identity | string | 否 | 否 | 身份信息。 |
| anonymousIdentity | string | 否 | 否 | 匿名身份。 |
| password | string | 否 | 否 | 密码。 |
| caCertAliases | string | 否 | 否 | CA证书别名。 |
| caPath | string | 否 | 否 | CA证书路径。 |
| clientCertAliases | string | 否 | 否 | 客户端证书别名。 |
| certEntry | Uint8Array | 否 | 否 | CA证书内容。 |
| certPassword | string | 否 | 否 | CA证书密码。 |
| altSubjectMatch | string | 否 | 否 | 替代主题匹配。 |
| domainSuffixMatch | string | 否 | 否 | 域后缀匹配。 |
| realm | string | 否 | 否 | 通行证凭证的领域。 |
| plmn | string | 否 | 否 | 公共陆地移动网的直通凭证提供商。 |
| eapSubId | number | 否 | 否 | SIM卡的子ID。 |

## EthEapConfig

以太网802.1X认证配置，包括EAP配置信息和功能开关。

**起始版本：** 26.0.1

**系统能力**：SystemCapability.Communication.NetManager.Eap

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| profile | [EthEapProfile](js-apis-net-eap.md#etheapprofile) | 否 | 否 | EAP配置信息。通过[eap.setEthEapConfig](js-apis-net-eap.md#eapsetetheapconfig)设置时，password、certPassword传入空字符串或certEntry传入空数组表示保留原值；通过[eap.getEthEapConfig](js-apis-net-eap.md#eapgetetheapconfig)获取时，password、certPassword返回空字符串，certEntry返回空数组。 |
| enabled | boolean | 否 | 否 | 是否启用802.1X功能。true表示启用，false表示禁用。 |
| autoAuth | boolean | 否 | 否 | 是否在连接网线或设备启动时自动发起认证。true表示自动发起，false表示不自动发起。 |
| locked | boolean | 否 | 否 | 是否锁定配置。true表示锁定，false表示未锁定。锁定后，除解锁外，不允许修改配置。 |

## EthEapState

以太网802.1X认证状态枚举。

**起始版本：** 26.0.1

**系统能力**：SystemCapability.Communication.NetManager.Eap

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| STATE\_IDLE | 0 | 空闲状态，尚未发起认证。 |
| STATE\_AUTHENTICATING | 1 | 正在进行以太网802.1X认证。 |
| STATE\_AUTHENTICATED | 2 | 认证成功。 |
| STATE\_FAILED | 3 | 认证失败，已达到最大重试次数。 |
| STATE\_RETRYING | 4 | 等待下一次重试。 |

## EthEapStateInfo

以太网802.1X认证状态信息，可通过[eap.getEthEapStateInfo](js-apis-net-eap.md#eapgetetheapstateinfo)获取，也可通过[eap.onStateChange](js-apis-net-eap.md#eaponstatechange)注册的回调返回。

**起始版本：** 26.0.1

**系统能力**：SystemCapability.Communication.NetManager.Eap

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| state | [EthEapState](js-apis-net-eap.md#etheapstate) | 否 | 否 | 当前认证状态。 |
| retryCount | number | 否 | 否 | 当前重试次数，取值为整数，认证成功后重置为0。 |
| message | string | 否 | 是 | 补充信息，例如认证失败原因。认证成功时为空。 |

## EthEapConnectAction

以太网802.1X认证操作枚举，用于[eap.connect](js-apis-net-eap.md#eapconnect)。

**起始版本：** 26.0.1

**系统能力**：SystemCapability.Communication.NetManager.Eap

**模型约束：** 此接口仅可在Stage模型下使用。

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACTION\_CONNECT | 0 | 使用已保存的配置重新触发认证。 |
| ACTION\_DISCONNECT | 1 | 停止自动认证及重试，退出当前以太网802.1X认证，并将认证状态重置为空闲。 |
