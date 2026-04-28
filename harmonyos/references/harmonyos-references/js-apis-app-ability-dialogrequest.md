---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-dialogrequest
title: @ohos.app.ability.dialogRequest (dialogRequest模块)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 通用能力的接口(推荐) > @ohos.app.ability.dialogRequest (dialogRequest模块)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:615a07cdd5c16af83cb45e1b3079cb2d111371f9a826ae9c18027e68a3de5768
---

dialogRequest模块用于处理模态弹框的能力，包括获取RequestInfo（用于绑定模态弹框）、获取RequestCallback（用于设置结果）。

模态弹框是指一个系统弹框，该弹框会拦截弹框之下的页面的鼠标、键盘、触屏等事件。销毁该弹框后，才能对页面进行操作。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口可以在ServiceExtensionAbility下使用，如果ServiceExtensionAbility实现了模态弹框，则可以使用本模块的接口获取请求方的RequestInfo、RequestCallback并返回请求结果。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { dialogRequest } from '@kit.AbilityKit';
```

## dialogRequest.getRequestInfo

PhonePC/2in1TabletTVWearable

getRequestInfo(want: Want): RequestInfo

从Want中获取请求方的RequestInfo。

说明

该接口可以在ServiceExtensionAbility下使用，如果ServiceExtensionAbility实现了模态弹框，则能从Want中获取请求方的RequestInfo。其他场景使用该接口，均无法获取返回值。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 表示发起方请求弹框时传入的want信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RequestInfo](js-apis-app-ability-dialogrequest.md#requestinfo) | 请求方RequestInfo，用于绑定模态窗口。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
5. try {
6. let requestInfo = dialogRequest.getRequestInfo(want);
7. } catch (err) {
8. console.error(`getRequestInfo err= ${JSON.stringify(err)}`);
9. }
10. }
11. }
```

## dialogRequest.getRequestCallback

PhonePC/2in1TabletTVWearable

getRequestCallback(want: Want): RequestCallback

从Want中获取请求方的RequestCallback。

说明

该接口可以在ServiceExtensionAbility下使用，如果ServiceExtensionAbility实现了模态弹框，则能从Want中获取请求方的RequestCallback。其他场景使用该接口，均无法获取返回值。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 表示发起方请求弹框时传入的want信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RequestCallback](js-apis-app-ability-dialogrequest.md#requestcallback) | 请求方RequestCallback，用于设置返回结果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
5. try {
6. let requestCallback = dialogRequest.getRequestCallback(want);
7. } catch(err) {
8. console.error(`getRequestInfo err= ${JSON.stringify(err)}`);
9. }
10. }
11. }
```

## WindowRect10+

PhonePC/2in1TabletTVWearable

表示模态弹框的属性。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 弹框边框的左上角的X坐标。 |
| top | number | 否 | 否 | 弹框边框的左上角的Y坐标。 |
| width | number | 否 | 否 | 弹框的宽度，单位为px。 |
| height | number | 否 | 否 | 弹框的高度，单位为px。 |

## RequestInfo

PhonePC/2in1TabletTVWearable

表示发起方请求信息，作为窗口绑定模态弹框的入参。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| windowRect10+ | [WindowRect](js-apis-app-ability-dialogrequest.md#windowrect10) | 否 | 是 | 表示模态弹框的位置属性。 |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
5. try {
6. let requestInfo = dialogRequest.getRequestInfo(want);
7. console.info(`getRequestInfo windowRect=, ${JSON.stringify(requestInfo.windowRect)}` );
8. } catch(err) {
9. console.error(`getRequestInfo err= ${JSON.stringify(err)}`);
10. }
11. }
12. }
```

## ResultCode

PhonePC/2in1TabletTVWearable

模态弹框请求结果码。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| RESULT\_OK | 0 | 表示成功。 |
| RESULT\_CANCEL | 1 | 表示失败。 |

## RequestResult

PhonePC/2in1TabletTVWearable

模态弹框请求结果，包含结果码ResultCode和请求结果ResultWant。

### 属性

PhonePC/2in1TabletTVWearable

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| result | [ResultCode](js-apis-app-ability-dialogrequest.md#resultcode) | 否 | 否 | 表示结果码。 |
| want10+ | [Want](js-apis-app-ability-want.md) | 否 | 是 | 表示Want类型信息，如ability名称，包名等。 |

## RequestCallback

PhonePC/2in1TabletTVWearable

用于设置模态弹框请求结果的callback接口。

**模型约束**：此接口仅可在Stage模型下使用。

### RequestCallback.setRequestResult

PhonePC/2in1TabletTVWearable

setRequestResult(result: RequestResult): void

设置请求结果

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.AbilityCore

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| result | [RequestResult](js-apis-app-ability-dialogrequest.md#requestresult) | 是 | 模态弹框请求结果信息。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
5. try {
6. let requestCallback = dialogRequest.getRequestCallback(want);
7. let myResult: dialogRequest.RequestResult = {
8. result : dialogRequest.ResultCode.RESULT_CANCEL,
9. };
10. requestCallback.setRequestResult(myResult);
11. } catch(err) {
12. console.error(`getRequestInfo err= ${JSON.stringify(err)}`);
13. }
14. }
15. }
```
