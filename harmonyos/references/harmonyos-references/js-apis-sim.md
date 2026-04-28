---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sim
title: @ohos.telephony.sim (SIM卡管理)
breadcrumb: API参考 > 系统 > 网络 > Telephony Kit（蜂窝通信服务） > ArkTS API > @ohos.telephony.sim (SIM卡管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:09:20+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1dca040e026de36454f226ce27c68c6d14ce126cf487159e0a3bda8c5dd8e005
---

SIM卡管理模块提供了SIM卡管理的基础能力，包括获取指定卡槽SIM卡的ISO国家码、归属PLMN号、服务提供商名称、SIM卡状态、卡类型、是否插卡、是否激活等。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhoneTabletWearable

```
1. import { sim } from '@kit.TelephonyKit';
```

## sim.isSimActive7+

PhoneTabletWearable

isSimActive(slotId: number, callback: AsyncCallback<boolean>): void

获取指定卡槽SIM卡是否激活。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。返回指定卡槽是否激活。  - true:激活。  - false：未激活。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.isSimActive(0, (err: BusinessError, data: boolean) => {
5. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
6. });
```

## sim.isSimActive7+

PhoneTabletWearable

isSimActive(slotId: number): Promise<boolean>

获取指定卡槽SIM卡是否激活。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise形式返回指定卡槽是否激活。  - true:激活。  - false：未激活。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.isSimActive(0).then((data: boolean) => {
5. console.info(`isSimActive success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`isSimActive failed, promise: err->${JSON.stringify(err)}`);
8. });
```

## sim.isSimActiveSync10+

PhoneTabletWearable

isSimActiveSync(slotId: number): boolean

获取指定卡槽SIM卡是否激活。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回指定卡槽是否激活。  - true:激活。  - false：未激活。 |

**示例：**

```
1. import { sim } from '@kit.TelephonyKit';

3. let isSimActive: boolean = sim.isSimActiveSync(0);
4. console.info(`the sim is active:` + isSimActive);
```

## sim.getDefaultVoiceSlotId7+

PhoneTabletWearable

getDefaultVoiceSlotId(callback: AsyncCallback<number>): void

获取默认语音业务的卡槽ID。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。  - 0：卡槽1。  - 1：卡槽2。  - -1：未设置或服务不可用。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getDefaultVoiceSlotId((err: BusinessError, data: number) => {
5. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
6. });
```

## sim.getDefaultVoiceSlotId7+

PhoneTabletWearable

getDefaultVoiceSlotId(): Promise<number>

获取默认语音业务的卡槽ID。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回默认语音业务的卡槽ID。  - 0：卡槽1。  - 1：卡槽2。  - -1：未设置或服务不可用。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getDefaultVoiceSlotId().then((data: number) => {
5. console.info(`getDefaultVoiceSlotId success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getDefaultVoiceSlotId failed, promise: err->${JSON.stringify(err)}`);
8. });
```

## sim.hasOperatorPrivileges7+

PhoneTabletWearable

hasOperatorPrivileges(slotId: number, callback: AsyncCallback<boolean>): void

检查应用(调用者)是否已被授予运营商权限。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。 返回检查应用(调用者)是否已被授予运营商权限。  - true:授权。  - false：未授权。 |

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.hasOperatorPrivileges(0, (err: BusinessError, data: boolean) => {
5. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
6. });
```

## sim.hasOperatorPrivileges7+

PhoneTabletWearable

hasOperatorPrivileges(slotId: number): Promise<boolean>

检查应用(调用者)是否已被授予运营商权限。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise形式返回检查应用(调用者)是否已被授予运营商权限。 |

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.hasOperatorPrivileges(0).then((data: boolean) => {
5. console.info(`hasOperatorPrivileges success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`hasOperatorPrivileges failed, promise: err->${JSON.stringify(err)}`);
8. });
```

## sim.getISOCountryCodeForSim

PhoneTabletWearable

getISOCountryCodeForSim(slotId: number, callback: AsyncCallback<string>): void

获取指定卡槽SIM卡的ISO国家码。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<string> | 是 | 回调函数。返回国家码，例如：CN(中国)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getISOCountryCodeForSim(0, (err: BusinessError, data: string) => {
5. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
6. });
```

## sim.getISOCountryCodeForSim

PhoneTabletWearable

getISOCountryCodeForSim(slotId: number): Promise<string>

获取指定卡槽SIM卡的ISO国家码。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回获取指定卡槽SIM卡的ISO国家码。例如：CN(中国)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getISOCountryCodeForSim(0).then((data: string) => {
5. console.info(`getISOCountryCodeForSim success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getISOCountryCodeForSim failed, promise: err->${JSON.stringify(err)}`);
8. });
```

## sim.getISOCountryCodeForSimSync10+

PhoneTabletWearable

getISOCountryCodeForSimSync(slotId: number): string

获取指定卡槽SIM卡的ISO国家码。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回获取指定卡槽SIM卡的ISO国家码。例如：CN(中国)。 |

**示例：**

```
1. import { sim } from '@kit.TelephonyKit';

3. let countryCode: string = sim.getISOCountryCodeForSimSync(0);
4. console.info(`the country ISO is:` + countryCode);
```

## sim.getSimOperatorNumeric

PhoneTabletWearable

getSimOperatorNumeric(slotId: number, callback: AsyncCallback<string>): void

获取指定卡槽SIM卡的归属PLMN(Public Land Mobile Network)号。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<string> | 是 | 回调函数。返回指定卡槽SIM卡的归属PLMN号。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getSimOperatorNumeric(0, (err: BusinessError, data: string) => {
5. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
6. });
```

## sim.getSimOperatorNumeric

PhoneTabletWearable

getSimOperatorNumeric(slotId: number): Promise<string>

获取指定卡槽SIM卡的归属PLMN(Public Land Mobile Network)号。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回获取指定卡槽SIM卡的归属PLMN号。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getSimOperatorNumeric(0).then((data: string) => {
5. console.info(`getSimOperatorNumeric success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getSimOperatorNumeric failed, promise: err->${JSON.stringify(err)}`);
8. });
```

## sim.getSimOperatorNumericSync10+

PhoneTabletWearable

getSimOperatorNumericSync(slotId: number): string

获取指定卡槽SIM卡的归属PLMN(Public Land Mobile Network)号。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回获取指定卡槽SIM卡的归属PLMN号。 |

**示例：**

```
1. import { sim } from '@kit.TelephonyKit';

3. let numeric: string = sim.getSimOperatorNumericSync(0);
4. console.info(`the sim operator numeric is:` + numeric);
```

## sim.getSimSpn

PhoneTabletWearable

getSimSpn(slotId: number, callback: AsyncCallback<string>): void

获取指定卡槽SIM卡的服务提供商名称(Service Provider Name，SPN)。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<string> | 是 | 回调函数。返回指定卡槽SIM卡的SPN。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getSimSpn(0, (err: BusinessError, data: string) => {
5. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
6. });
```

## sim.getSimSpn

PhoneTabletWearable

getSimSpn(slotId: number): Promise<string>

获取指定卡槽SIM卡的服务提供商名称(Service Provider Name，SPN)。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回获取指定卡槽SIM卡的SPN。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getSimSpn(0).then((data: string) => {
5. console.info(`getSimSpn success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getSimSpn failed, promise: err->${JSON.stringify(err)}`);
8. });
```

## sim.getSimSpnSync10+

PhoneTabletWearable

getSimSpnSync(slotId: number): string

获取指定卡槽SIM卡的服务提供商名称(Service Provider Name，SPN)。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回获取指定卡槽SIM卡的SPN。 |

**示例：**

```
1. import { sim } from '@kit.TelephonyKit';

3. let spn: string = sim.getSimSpnSync(0);
4. console.info(`the sim card spn is:` + spn);
```

## sim.getSimState

PhoneTabletWearable

getSimState(slotId: number, callback: AsyncCallback<SimState>): void

获取指定卡槽的SIM卡状态。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<[SimState](js-apis-sim.md#simstate)> | 是 | 回调函数。参考[SimState](js-apis-sim.md#simstate)。 |

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getSimState(0, (err: BusinessError, data: sim.SimState) => {
5. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
6. });
```

## sim.getSimState

PhoneTabletWearable

getSimState(slotId: number): Promise<SimState>

获取指定卡槽的SIM卡状态。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SimState](js-apis-sim.md#simstate)> | 以Promise形式返回获取指定卡槽的SIM卡状态。 |

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getSimState(0).then((data: sim.SimState) => {
5. console.info(`getSimState success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getSimState failed, promise: err->${JSON.stringify(err)}`);
8. });
```

## sim.getSimStateSync10+

PhoneTabletWearable

getSimStateSync(slotId: number): SimState

获取指定卡槽的SIM卡状态。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SimState](js-apis-sim.md#simstate) | 返回获取指定卡槽的SIM卡状态。 |

**示例：**

```
1. import { sim } from '@kit.TelephonyKit';

3. let simState: sim.SimState = sim.getSimStateSync(0);
4. console.info(`The sim state is:` + simState);
```

## sim.getCardType7+

PhoneTabletWearable

getCardType(slotId: number, callback: AsyncCallback<CardType>): void

获取指定卡槽SIM卡的卡类型。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<[CardType](js-apis-sim.md#cardtype7)> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getCardType(0, (err: BusinessError, data: sim.CardType) => {
5. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
6. });
```

## sim.getCardType7+

PhoneTabletWearable

getCardType(slotId: number): Promise<CardType>

获取指定卡槽SIM卡的卡类型。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[CardType](js-apis-sim.md#cardtype7)> | 以Promise形式返回指定卡槽SIM卡的卡类型。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getCardType(0).then((data: sim.CardType) => {
5. console.info(`getCardType success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getCardType failed, promise: err->${JSON.stringify(err)}`);
8. });
```

## sim.getCardTypeSync10+

PhoneTabletWearable

getCardTypeSync(slotId: number): CardType

获取指定卡槽SIM卡的卡类型。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [CardType](js-apis-sim.md#cardtype7) | 返回指定卡槽SIM卡的卡类型。 |

**示例：**

```
1. import { sim } from '@kit.TelephonyKit';

3. let cardType: sim.CardType = sim.getCardTypeSync(0);
4. console.info(`the card type is:` + cardType);
```

## sim.hasSimCard7+

PhoneTabletWearable

hasSimCard(slotId: number, callback: AsyncCallback<boolean>): void

获取指定卡槽SIM卡是否插卡。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<boolean> | 是 | 回调返回指定卡槽是否插卡。  - true:插卡。  - false：未插卡。 |

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.hasSimCard(0, (err: BusinessError, data: boolean) => {
5. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
6. });
```

## sim.hasSimCard7+

PhoneTabletWearable

hasSimCard(slotId: number): Promise<boolean>

获取指定卡槽SIM卡是否插卡。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | 以Promise形式返回指定卡槽是否插卡。  - true:插卡。  - false：未插卡。 |

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

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.hasSimCard(0).then((data: boolean) => {
5. console.info(`hasSimCard success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`hasSimCard failed, promise: err->${JSON.stringify(err)}`);
8. });
```

## sim.hasSimCardSync10+

PhoneTabletWearable

hasSimCardSync(slotId: number): boolean

获取指定卡槽SIM卡是否插卡。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回指定卡槽是否插卡。  - true:插卡。  - false：未插卡。 |

**示例：**

```
1. import { sim } from '@kit.TelephonyKit';

3. let hasSimCard: boolean = sim.hasSimCardSync(0);
4. console.info(`has sim card: ` + hasSimCard);
```

## sim.getSimAccountInfo10+

PhoneTabletWearable

getSimAccountInfo(slotId: number, callback: AsyncCallback<IccAccountInfo>): void

获取SIM卡账户信息。使用callback异步回调。

**需要权限**：ohos.permission.GET\_TELEPHONY\_STATE

说明

获取ICCID和号码信息时需要GET\_TELEPHONY\_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<[IccAccountInfo](js-apis-sim.md#iccaccountinfo10)> | 是 | 回调函数。返回指定卡槽SIM卡的账户信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |
| 8301002 | The SIM card failed to read or update data. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getSimAccountInfo(0, (err:BusinessError , data: sim.IccAccountInfo) => {
5. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
6. });
```

## sim.getSimAccountInfo10+

PhoneTabletWearable

getSimAccountInfo(slotId: number): Promise<IccAccountInfo>

获取SIM卡账户信息。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_TELEPHONY\_STATE

说明

获取ICCID和号码信息时需要GET\_TELEPHONY\_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[IccAccountInfo](js-apis-sim.md#iccaccountinfo10)> | 以Promise形式返回指定卡槽SIM卡的账户信息。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |
| 8301002 | The SIM card failed to read or update data. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getSimAccountInfo(0).then((data: sim.IccAccountInfo) => {
5. console.info(`getSimAccountInfo success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getSimAccountInfo failed, promise: err->${JSON.stringify(err)}`);
8. });
```

## sim.getActiveSimAccountInfoList10+

PhoneTabletWearable

getActiveSimAccountInfoList(callback: AsyncCallback<Array<IccAccountInfo>>): void

获取激活SIM卡账户信息列表。使用callback异步回调。

**需要权限**：ohos.permission.GET\_TELEPHONY\_STATE

说明

获取ICCID和号码信息时需要GET\_TELEPHONY\_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[IccAccountInfo](js-apis-sim.md#iccaccountinfo10)>> | 是 | 回调函数。返回激活SIM卡账户信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getActiveSimAccountInfoList((err: BusinessError, data: Array<sim.IccAccountInfo>) => {
5. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
6. });
```

## sim.getMaxSimCount7+

PhoneTabletWearable

getMaxSimCount(): number

获取卡槽数量。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 卡槽数量。 |

**示例：**

```
1. import { sim } from '@kit.TelephonyKit';

3. console.info("Result: "+ sim.getMaxSimCount());
```

## sim.getActiveSimAccountInfoList10+

PhoneTabletWearable

getActiveSimAccountInfoList(): Promise<Array<IccAccountInfo>>

获取激活SIM卡账户信息列表。使用Promise异步回调。

**需要权限**：ohos.permission.GET\_TELEPHONY\_STATE

说明

获取ICCID和号码信息时需要GET\_TELEPHONY\_STATE权限，ICCID和号码信息为敏感数据，不向三方应用开放。调用接口时，获取到的ICCID和号码信息为空。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[IccAccountInfo](js-apis-sim.md#iccaccountinfo10)>> | 以Promise形式返回激活卡槽SIM卡的账户信息列表。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getActiveSimAccountInfoList().then((data: Array<sim.IccAccountInfo>) => {
5. console.info(`getActiveSimAccountInfoList success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getActiveSimAccountInfoList failed, promise: err->${JSON.stringify(err)}`);
8. });
```

## sim.getOpKey9+

PhoneTabletWearable

getOpKey(slotId: number, callback: AsyncCallback<string>): void

获取指定卡槽中SIM卡的opkey。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<string> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. try {
5. sim.getOpKey(0, (err: BusinessError, data: string) => {
6. if (err) {
7. console.error("getOpKey failed, err: " + JSON.stringify(err));
8. } else {
9. console.info('getOpKey successfully, data: ' + JSON.stringify(data));
10. }
11. });
12. } catch (err) {
13. console.error("getOpKey err: " + JSON.stringify(err));
14. }
```

## sim.getOpKey9+

PhoneTabletWearable

getOpKey(slotId: number): Promise<string>

获取指定卡槽中SIM卡的opkey。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回指定卡槽中SIM卡的opkey。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getOpKey(0).then((data: string) => {
5. console.info(`getOpKey success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getOpKey failed, promise: err->${JSON.stringify(err)}`);
8. });
```

## sim.getOpKeySync10+

PhoneTabletWearable

getOpKeySync(slotId: number): string

获取指定卡槽中SIM卡的opkey。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回指定卡槽中SIM卡的opkey。 |

**示例：**

```
1. import { sim } from '@kit.TelephonyKit';

3. let data: string = sim.getOpKeySync(0);
4. console.info(`getOpKey success, promise: data->${JSON.stringify(data)}`);
```

## sim.getOpName9+

PhoneTabletWearable

getOpName(slotId: number, callback: AsyncCallback<string>): void

获取指定卡槽中SIM卡的OpName。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<string> | 是 | 回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. try {
5. sim.getOpName(0, (err: BusinessError, data: string) => {
6. if (err) {
7. console.error("getOpName failed, err: " + JSON.stringify(err));
8. } else {
9. console.info('getOpName successfully, data: ' + JSON.stringify(data));
10. }
11. });
12. } catch (err) {
13. console.error("getOpName err: " + JSON.stringify(err));
14. }
```

## sim.getOpName9+

PhoneTabletWearable

getOpName(slotId: number): Promise<string>

获取指定卡槽中SIM卡的OpName。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | 以Promise形式返回指定卡槽中SIM卡的OpName。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300999 | Unknown error. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getOpName(0).then((data: string) => {
5. console.info(`getOpName success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getOpName failed, promise: err->${JSON.stringify(err)}`);
8. });
```

## sim.getOpNameSync10+

PhoneTabletWearable

getOpNameSync(slotId: number): string

获取指定卡槽中SIM卡的OpName。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回指定卡槽中SIM卡的OpName。 |

**示例：**

```
1. import { sim } from '@kit.TelephonyKit';

3. let data: string = sim.getOpNameSync(0);
4. console.info(`getOpName success, promise: data->${JSON.stringify(data)}`);
```

## sim.getDefaultVoiceSimId10+

PhoneTabletWearable

getDefaultVoiceSimId(callback: AsyncCallback<number>): void

获取默认语音业务的SIM卡ID。使用callback异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<number> | 是 | 回调函数。  与SIM卡绑定，从1开始递增。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)和[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |
| 8301001 | SIM card is not activated. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getDefaultVoiceSimId((err: BusinessError, data: number) => {
5. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
6. });
```

## sim.getDefaultVoiceSimId10+

PhoneTabletWearable

getDefaultVoiceSimId(): Promise<number>

获取默认语音业务的SIM卡ID。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | 以Promise形式返回默认语音业务的SIM卡ID。  与SIM卡绑定，从1开始递增。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8300001 | Invalid parameter value. |
| 8300002 | Service connection failed. |
| 8300003 | System internal error. |
| 8300004 | No SIM card found. |
| 8300999 | Unknown error. |
| 8301001 | SIM card is not activated. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. let promise = sim.getDefaultVoiceSimId();
5. promise.then((data: number) => {
6. console.info(`getDefaultVoiceSimId success, promise: data->${JSON.stringify(data)}`);
7. }).catch((err: BusinessError) => {
8. console.error(`getDefaultVoiceSimId failed, promise: err->${JSON.stringify(err)}`);
9. });
```

## sim.getSimLabel20+

PhoneTabletWearable

getSimLabel(slotId: number, callback: AsyncCallback<SimLabel>): void

查看卡槽ID和SIM卡的对应关系：

* 卡槽1对应SIM卡1或SIM卡2
* 卡槽2对应SIM卡2或ESIMX

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |
| callback | AsyncCallback<[SimLabel](js-apis-sim.md#simlabel20)> | 是 | 回调函数。获取SIM卡标签信息。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getSimLabel(0, (err: BusinessError, data: sim.SimLabel) => {
5. console.info(`callback: err->${JSON.stringify(err)}, data->${JSON.stringify(data)}`);
6. });
```

## sim.getSimLabel20+

PhoneTabletWearable

getSimLabel(slotId: number): Promise<SimLabel>

获取SIM卡的标签信息。使用Promise异步回调。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SimLabel](js-apis-sim.md#simlabel20) > | 回调函数。获取SIM卡标签信息。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8300001 | Invalid parameter value. |
| 8300002 | Operation failed. Cannot connect to service. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { sim } from '@kit.TelephonyKit';

4. sim.getSimLabel(0).then((data: sim.SimLabel) => {
5. console.info(`getSimLabel success, promise: data->${JSON.stringify(data)}`);
6. }).catch((err: BusinessError) => {
7. console.error(`getSimState failed, promise: err->${JSON.stringify(err)}`);
8. });
```

## sim.getSimLabelSync20+

PhoneTabletWearable

getSimLabelSync(slotId: number): SimLabel

通过传入SIM卡槽的ID，获取对应的SIM卡标签。

**系统能力**：SystemCapability.Telephony.CoreService

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| slotId | number | 是 | 卡槽ID。  - 0：卡槽1。  - 1：卡槽2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SimLabel](js-apis-sim.md#simlabel20) | SIM卡标签。 |

**示例：**

```
1. import { sim } from '@kit.TelephonyKit';

4. let simLabel: sim.SimLabel = sim.getSimLabelSync(0);
5. console.info(`The sim state is:` + simLabel);
```

## SimType20+

PhoneTabletWearable

SIM卡类型的枚举。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PSIM | 0 | 实体SIM卡。 |
| ESIM | 1 | 电子SIM卡。 |

## SimLabel20+

PhoneTabletWearable

SIM卡标签。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| simType | [SimType](js-apis-sim.md#simtype20) | 否 | 否 | 表示SIM卡类型的枚举。 |
| index | number | 否 | 否 | SIM卡的唯一标识索引值。 |

## SimState

PhoneTabletWearable

SIM卡状态。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SIM\_STATE\_UNKNOWN | 0 | SIM卡状态未知，即无法获取准确的状态。 |
| SIM\_STATE\_NOT\_PRESENT | 1 | 表示SIM卡处于not present状态，即卡槽中没有插入SIM卡。 |
| SIM\_STATE\_LOCKED | 2 | 表示SIM卡处于locked状态，即SIM卡被PIN、PUK或网络锁锁定。 |
| SIM\_STATE\_NOT\_READY | 3 | 表示SIM卡处于not ready状态，即SIM卡在位但无法正常工作。 |
| SIM\_STATE\_READY | 4 | 表示SIM卡处于ready状态，即SIM卡在位且工作正常。 |
| SIM\_STATE\_LOADED | 5 | 表示SIM卡处于loaded状态，即SIM卡在位且所有卡文件加载完毕。 |

## CardType7+

PhoneTabletWearable

卡类型。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN\_CARD | -1 | 未知类型。 |
| SINGLE\_MODE\_SIM\_CARD | 10 | 单SIM卡。 |
| SINGLE\_MODE\_USIM\_CARD | 20 | 单USIM卡。 |
| SINGLE\_MODE\_RUIM\_CARD | 30 | 单RUIM卡。 |
| DUAL\_MODE\_CG\_CARD | 40 | 双卡模式C+G。 |
| CT\_NATIONAL\_ROAMING\_CARD | 41 | 中国电信内部漫游卡。 |
| CU\_DUAL\_MODE\_CARD | 42 | 中国联通双模卡。 |
| DUAL\_MODE\_TELECOM\_LTE\_CARD | 43 | 双模式电信LTE卡。 |
| DUAL\_MODE\_UG\_CARD | 50 | 双模式UG卡。 |
| SINGLE\_MODE\_ISIM\_CARD8+ | 60 | 单一ISIM卡类型。 |

## IccAccountInfo10+

PhoneTabletWearable

Icc账户信息。

**系统能力**：SystemCapability.Telephony.CoreService

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| simId | number | 否 | 否 | SIM卡ID。 |
| slotIndex | number | 否 | 否 | 卡槽ID。 |
| isEsim | boolean | 否 | 否 | 标记卡是否是eSim。  - true:是eSim。  - false：不是eSim。 |
| isActive | boolean | 否 | 否 | 卡是否被激活。  - true:激活。  - false：未激活。 |
| iccId | string | 否 | 否 | ICCID号码。 |
| showName | string | 否 | 否 | SIM卡显示名称。 |
| showNumber | string | 否 | 否 | SIM卡显示号码。 |
