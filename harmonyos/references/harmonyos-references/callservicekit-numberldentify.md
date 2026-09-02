---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/callservicekit-numberldentify
title: numberIdentify (号码识别查询基本能力)
breadcrumb: API参考 > 应用服务 > Call Service Kit（通话服务） > ArkTS API > numberIdentify (号码识别查询基本能力)
category: harmonyos-references
scraped_at: 2026-09-02T14:53:16+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:ef251f50bea47dfb2757068668f2bbbd764ecafe487e3936f3a3ccbd240015b5
---

numberIdentify模块提供企业来电相关能力查询，包括查询是否有企业来电能力、陌生号码与信息识别开关、企业信息等。

**起始版本：** 6.1.0(23)

## 导入模块

```typescript
import { numberIdentify } from '@kit.CallServiceKit';
```

## isSupportEnterpriseNumberIdentify

isSupportEnterpriseNumberIdentify(context: Context): Promise<boolean>

返回企业来电显示权限的开关状态，供设置页面展示。使用Promise异步回调。

**模型约束：** 该接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-app-ability-common.md#context) | 是 | 应用内上下文信息 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回是否已开通企业来电显示权限，true:已开通。false:未开通。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8300001 | Invalid parameter value. |
| 8300002 | The enterprise permission is not verified. |
| 8300003 | System internal error. |
| 8300999 | Unknown error code. |

**示例：**

```typescript
import { numberIdentify } from '@kit.CallServiceKit';
import type {common} from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let isSupport = await numberIdentify.isSupportEnterpriseNumberIdentify(context);
hilog.info(0, 'TAG', `isSupport:${isSupport}`);
```

## queryNumberIdentifySwitchState

queryNumberIdentifySwitchState(context: Context):SwitchState

查询陌生号码与信息识别总开关状态以及应用号码识别开关状态。

**模型约束：** 该接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 6.1.0(23)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-app-ability-common.md#context) | 是 | 应用内上下文信息 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [SwitchState](callservicekit-numberldentify.md#switchstate) | 查询陌生号码与信息识别总开关状态以及调用该接口的应用号码识别开关状态。 |

**错误码：**

以下错误码的详细介绍请参见[电话子系统错误码](errorcode-telephony.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 8300001 | Invalid parameter value. |
| 8300002 | The enterprise permission is not verified. |
| 8300999 | Unknown error code. |

**示例：**

```typescript
import type {common} from '@kit.AbilityKit';
import { numberIdentify } from '@kit.CallServiceKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
 
let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
let switchState = numberIdentify.queryNumberIdentifySwitchState(context);
hilog.info(0, 'TAG', `switchState is:${JSON.stringify(switchState)}`);
```

## SwitchState

陌生号码与信息识别总开关状态以及应用号码识别开关状态。

**模型约束：** 该接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 6.1.0(23)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| isNumberIdentifyEnabled | boolean | 否 | 否 | 是否开启号码识别能力。true:是。false:否。 |
| isApplicationNumberIdentifyEnabled | boolean | 否 | 否 | 企业应用是否开启号码识别能力。true:是。false:否。 |
| isBusinessServiceDataEnabled | boolean | 否 | 否 | 企业应用是否开启服务信息展示能力。true:是。false:否。**起始版本：** 6.1.1(24) |

## BusinessServiceData

企业服务信息。

**模型约束：** 该接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 6.1.1(24)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| type | [BusinessServiceType](callservicekit-numberldentify.md#businessservicetype) | 否 | 否 | 企业服务类型。 |
| delivery | [DeliveryData](callservicekit-numberldentify.md#deliverydata) | 否 | 是 | 快递服务数据。 |

## BusinessServiceType

企业服务类型枚举。

**模型约束：** 该接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 6.1.1(24)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DELIVERY | 0 | 企业服务类型为快递。 |

## DeliveryData

快递服务数据。

**模型约束：** 该接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 6.1.1(24)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| customerName | string | 否 | 否 | 客户姓名。长度小于20个字符，如果超出将会截取前20个字符。 |
| deliveryNumber | string | 否 | 否 | 快递单号。长度小于20个字符，如果超出将会截取前20个字符。 |
| deliveryStatus | string | 否 | 否 | 订单状态。长度小于10个字符，如果超出将会截取前10个字符。 |
| deliveryStatusColor | [DeliveryStatusColor](callservicekit-numberldentify.md#deliverystatuscolor) | 否 | 否 | 订单状态颜色。 |
| deliveryAddress | string | 否 | 否 | 派送地址。长度小于150个字符，如果超出将会截取前150个字符。 |
| deliveryTimeout | string | 否 | 否 | 派送超时时间。长度小于20个字符，如果超出将会截取前20个字符。 |

## DeliveryStatusColor

订单状态颜色的枚举。

**模型约束：** 该接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Telephony.NumberIdentifyService

**起始版本：** 6.1.1(24)

| 名称 | 值 | 说明 |
| --- | --- | --- |
| BLUE | 0 | 订单状态颜色为蓝色。 |
| GREEN | 1 | 订单状态颜色为绿色。 |
| RED | 2 | 订单状态颜色为红色。 |
