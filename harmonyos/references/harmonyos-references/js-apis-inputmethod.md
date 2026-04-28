---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inputmethod
title: @ohos.inputMethod (输入法框架)
breadcrumb: API参考 > 应用框架 > IME Kit（输入法开发服务） > ArkTS API > @ohos.inputMethod (输入法框架)
category: harmonyos-references
scraped_at: 2026-04-28T08:06:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c3851b5f75977791581202a5bb6cf99561084c5f879432371284286efeb266c6
---

本模块主要面向普通前台应用（备忘录、信息、设置等系统应用与三方应用），提供对输入法（输入法应用）的控制、管理能力，包括显示/隐藏输入法软键盘、切换输入法、获取所有输入法列表等等。

说明

本模块首批接口从API version 6开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { inputMethod } from '@kit.IMEKit';
```

## 常量

PhonePC/2in1TabletTVWearable

常量值。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 参数名 | 类型 | 常量值 | 说明 |
| --- | --- | --- | --- |
| MAX\_TYPE\_NUM8+ | number | 128 | 可支持的最大输入法个数。 |

## InputMethodProperty8+

PhonePC/2in1TabletTVWearable

输入法应用属性。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name9+ | string | 是 | 否 | 必填。输入法包名。 |
| id9+ | string | 是 | 否 | 必填。输入法扩展在应用内唯一标识，与name一起组成输入法扩展的全局唯一标识。 |
| label9+ | string | 是 | 是 | 非必填。  - 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展。  - 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](js-apis-inputmethod.md#inputmethodgetcurrentinputmethod9)），此字段表示输入法扩展对外显示的名称，优先使用InputMethodExtensionAbility中配置的label，若未配置，自动使用应用入口ability的label；当应用入口ability未配置label时，自动使用应用AppScope中配置的label。 |
| labelId10+ | number | 是 | 是 | 非必填。  - 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展。  - 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](js-apis-inputmethod.md#inputmethodgetcurrentinputmethod9)），此字段表示label字段的资源号。 |
| icon9+ | string | 是 | 是 | 非必填。  - 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展。  - 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](js-apis-inputmethod.md#inputmethodgetcurrentinputmethod9)），此字段表示输入法图标数据，可以通过iconId查询获取。 |
| iconId9+ | number | 是 | 是 | 非必填。  - 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展。  - 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](js-apis-inputmethod.md#inputmethodgetcurrentinputmethod9)），此字段表示icon字段的资源号。 |
| enabledState20+ | [EnabledState](js-apis-inputmethod.md#enabledstate15) | 是 | 是 | 非必填。  - 当InputMethodProperty用于切换、查询等接口的入参时，开发者可不填写此字段，通过name和id即可唯一指定一个输入法扩展  - 当InputMethodProperty作为查询接口的返回值时（如[getCurrentInputMethod](js-apis-inputmethod.md#inputmethodgetcurrentinputmethod9)），此字段表示该输入法启用状态。 |
| extra9+ | object | 否 | 是 | 输入法扩展信息。预留字段，当前无具体含义，暂不支持使用。  - API version 10起：非必填；  - API version 9：必填。 |
| packageName(deprecated) | string | 是 | 否 | 输入法包名。必填。  说明：从API version 8开始支持，从API version 9开始废弃，建议使用name替代。 |
| methodId(deprecated) | string | 是 | 否 | 输入法唯一标识。必填。  说明：从API version 8开始支持，从API version 9开始废弃，建议使用id替代。 |

## CapitalizeMode20+

PhonePC/2in1TabletTVWearable

枚举，定义了文本首字母大写的不同模式。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 不进行任何首字母大写处理。 |
| SENTENCES | 1 | 每个句子的首字母大写。 |
| WORDS | 2 | 每个单词首字母大写。 |
| CHARACTERS | 3 | 每个字母都大写。 |

## inputMethod.getController9+

PhonePC/2in1TabletTVWearable

getController(): InputMethodController

获取客户端实例[InputMethodController](js-apis-inputmethod.md#inputmethodcontroller)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodController](js-apis-inputmethod.md#inputmethodcontroller) | 返回当前客户端实例。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800006 | input method controller error. Possible cause: create InputMethodController object failed. |

**示例：**

```
1. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
```

## inputMethod.getDefaultInputMethod11+

PhonePC/2in1TabletTVWearable

getDefaultInputMethod(): InputMethodProperty

获取默认输入法。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8) | 返回默认输入法属性对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. let defaultIme: inputMethod.InputMethodProperty = inputMethod.getDefaultInputMethod();
```

## inputMethod.getSystemInputMethodConfigAbility11+

PhonePC/2in1TabletTVWearable

getSystemInputMethodConfigAbility(): ElementName

获取系统输入法设置界面Ability信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ElementName](js-apis-bundlemanager-elementname.md) | 系统输入法设置界面Ability的ElementName。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { bundleManager } from '@kit.AbilityKit';

3. let inputMethodConfig: bundleManager.ElementName = inputMethod.getSystemInputMethodConfigAbility();
```

## inputMethod.getSetting9+

PhonePC/2in1TabletTVWearable

getSetting(): InputMethodSetting

获取客户端设置实例[InputMethodSetting](js-apis-inputmethod.md#inputmethodsetting8)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodSetting](js-apis-inputmethod.md#inputmethodsetting8) | 返回当前客户端设置实例。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800007 | input method setter error. Possible cause: create InputMethodSetting object failed. |

**示例：**

```
1. let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();
```

## inputMethod.switchInputMethod9+

PhonePC/2in1TabletTVWearable

switchInputMethod(target: InputMethodProperty, callback: AsyncCallback<boolean>): void

切换输入法，使用callback异步回调。

说明

* 在API version 9-10版本，仅支持系统应用调用且需要权限ohos.permission.CONNECT\_IME\_ABILITY。
* 在API version 11版本起，仅支持当前输入法应用调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8) | 是 | 目标输入法。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当输入法切换成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
4. inputMethod.switchInputMethod(currentIme, (err: BusinessError, result: boolean) => {
5. if (err) {
6. console.error(`Failed to switchInputMethod, code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. if (result) {
10. console.info('Succeeded in switching input method.');
11. } else {
12. console.error('Failed to switch input method.');
13. }
14. });
```

说明

在 API11 中 201 permissions check fails. 这个错误码被移除。

## inputMethod.switchInputMethod9+

PhonePC/2in1TabletTVWearable

switchInputMethod(target: InputMethodProperty): Promise<boolean>

切换输入法，使用promise异步回调。

说明

* 在API version 9-10版本，仅支持系统应用调用且需要权限ohos.permission.CONNECT\_IME\_ABILITY。
* 在API version 11版本起，仅支持当前输入法应用调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8) | 是 | 目标输入法。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示切换输入法成功，返回false表示切换输入法失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
4. inputMethod.switchInputMethod(currentIme).then((result: boolean) => {
5. if (result) {
6. console.info('Succeeded in switching input method.');
7. } else {
8. console.error('Failed to switch input method.');
9. }
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to switchInputMethod, code: ${err.code}, message: ${err.message}`);
12. });
```

说明

在 API11 中 201 permissions check fails. 这个错误码被移除。

## inputMethod.getCurrentInputMethod9+

PhonePC/2in1TabletTVWearable

getCurrentInputMethod(): InputMethodProperty

使用同步方法获取当前输入法。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8) | 返回当前输入法属性对象。 |

**示例：**

```
1. let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
```

## inputMethod.switchCurrentInputMethodSubtype9+

PhonePC/2in1TabletTVWearable

switchCurrentInputMethodSubtype(target: InputMethodSubtype, callback: AsyncCallback<boolean>): void

切换当前输入法的子类型。使用callback异步回调。

说明

* 在API version 9版本，仅支持系统应用调用且需要权限ohos.permission.CONNECT\_IME\_ABILITY。
* 在API version 10版本，支持系统应用和当前输入法应用调用；需要权限ohos.permission.CONNECT\_IME\_ABILITY。
* 在API version 11版本起，仅支持当前输入法调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [InputMethodSubtype](js-apis-inputmethod-subtype.md#inputmethodsubtype) | 是 | 目标输入法子类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当输入法子类型切换成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let extra: Record<string, string> = {}
4. // 参考InputMethodSubtype参数说明
5. inputMethod.switchCurrentInputMethodSubtype({
6. id: "ServiceExtAbility",
7. label: "",
8. name: "com.example.keyboard",
9. mode: "upper",
10. locale: "",
11. language: "",
12. icon: "",
13. iconId: 0,
14. extra: extra
15. }, (err: BusinessError, result: boolean) => {
16. if (err) {
17. console.error(`Failed to switchCurrentInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
18. return;
19. }
20. if (result) {
21. console.info('Succeeded in switching currentInputMethodSubtype.');
22. } else {
23. console.error('Failed to switchCurrentInputMethodSubtype');
24. }
25. });
```

说明

在 API11 中 201 permissions check fails. 这个错误码被移除。

## inputMethod.switchCurrentInputMethodSubtype9+

PhonePC/2in1TabletTVWearable

switchCurrentInputMethodSubtype(target: InputMethodSubtype): Promise<boolean>

切换当前输入法的子类型。使用promise异步回调。

说明

* 在API version 9版本，仅支持系统应用调用且需要权限ohos.permission.CONNECT\_IME\_ABILITY。
* 在API version 10版本，支持系统应用和当前输入法应用调用；需要权限ohos.permission.CONNECT\_IME\_ABILITY。
* 在API version 11版本起，仅支持当前输入法调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [InputMethodSubtype](js-apis-inputmethod-subtype.md#inputmethodsubtype) | 是 | 目标输入法子类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示当前输入法切换子类型成功，返回false表示当前输入法切换子类型成功失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let extra: Record<string, string> = {}
4. // 参考InputMethodSubtype参数说明
5. inputMethod.switchCurrentInputMethodSubtype({
6. id: "ServiceExtAbility",
7. label: "",
8. name: "com.example.keyboard",
9. mode: "upper",
10. locale: "",
11. language: "",
12. icon: "",
13. iconId: 0,
14. extra: extra
15. }).then((result: boolean) => {
16. if (result) {
17. console.info('Succeeded in switching currentInputMethodSubtype.');
18. } else {
19. console.error('Failed to switchCurrentInputMethodSubtype.');
20. }
21. }).catch((err: BusinessError) => {
22. console.error(`Failed to switchCurrentInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
23. });
```

说明

在 API11 中 201 permissions check fails. 这个错误码被移除。

## inputMethod.getCurrentInputMethodSubtype9+

PhonePC/2in1TabletTVWearable

getCurrentInputMethodSubtype(): InputMethodSubtype

获取当前输入法的子类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodSubtype](js-apis-inputmethod-subtype.md#inputmethodsubtype) | 返回当前输入法子类型对象。 |

**示例：**

```
1. import { InputMethodSubtype } from '@kit.IMEKit';

3. let currentImeSubType: InputMethodSubtype = inputMethod.getCurrentInputMethodSubtype();
```

## inputMethod.switchCurrentInputMethodAndSubtype9+

PhonePC/2in1TabletTVWearable

switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype, callback: AsyncCallback<boolean>): void

切换至指定输入法的指定子类型，适用于跨输入法切换子类型。使用callback异步回调。

说明

* 在API version 9-10版本，仅支持系统应用调用且需要权限ohos.permission.CONNECT\_IME\_ABILITY。
* 在API version 11版本起，仅支持当前输入法调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputMethodProperty | [InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8) | 是 | 目标输入法。 |
| inputMethodSubtype | [InputMethodSubtype](js-apis-inputmethod-subtype.md#inputmethodsubtype) | 是 | 目标输入法子类型。 |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当输入法和子类型切换成功，err为undefined，data为获取到的切换子类型结果true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { InputMethodSubtype } from '@kit.IMEKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
5. let imSubType: InputMethodSubtype = inputMethod.getCurrentInputMethodSubtype();
6. inputMethod.switchCurrentInputMethodAndSubtype(currentIme, imSubType, (err: BusinessError, result: boolean) => {
7. if (err) {
8. console.error(`Failed to switchCurrentInputMethodAndSubtype, code: ${err.code}, message: ${err.message}`);
9. return;
10. }
11. if (result) {
12. console.info('Succeeded in switching currentInputMethodAndSubtype.');
13. } else {
14. console.error('Failed to switchCurrentInputMethodAndSubtype.');
15. }
16. });
```

说明

在 API11 中 201 permissions check fails. 这个错误码被移除。

## inputMethod.switchCurrentInputMethodAndSubtype9+

PhonePC/2in1TabletTVWearable

switchCurrentInputMethodAndSubtype(inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype): Promise<boolean>

切换至指定输入法的指定子类型，适用于跨输入法切换子类型。使用promise异步回调。

说明

* 在API version 9-10版本，仅支持系统应用调用且需要权限ohos.permission.CONNECT\_IME\_ABILITY。
* 在API version 11版本起，仅支持当前输入法调用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputMethodProperty | [InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8) | 是 | 目标输入法。 |
| inputMethodSubtype | [InputMethodSubtype](js-apis-inputmethod-subtype.md#inputmethodsubtype) | 是 | 目标输入法子类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示切换至指定输入法的指定子类型成功，返回false表示切换至指定输入法的指定子类型失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800005 | configuration persistence error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { InputMethodSubtype } from '@kit.IMEKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let currentIme: inputMethod.InputMethodProperty = inputMethod.getCurrentInputMethod();
5. let imSubType: InputMethodSubtype = inputMethod.getCurrentInputMethodSubtype();
6. inputMethod.switchCurrentInputMethodAndSubtype(currentIme, imSubType).then((result: boolean) => {
7. if (result) {
8. console.info('Succeeded in switching currentInputMethodAndSubtype.');
9. } else {
10. console.error('Failed to switchCurrentInputMethodAndSubtype.');
11. }
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to switchCurrentInputMethodAndSubtype, code: ${err.code}, message: ${err.message}`);
14. });
```

说明

在 API11 中 201 permissions check fails. 这个错误码被移除。

## inputMethod.getInputMethodController(deprecated)

PhonePC/2in1TabletTVWearable

getInputMethodController(): InputMethodController

获取客户端实例[InputMethodController](js-apis-inputmethod.md#inputmethodcontroller)。

说明

从API version 6开始支持，从API version 9开始废弃，建议使用[getController](js-apis-inputmethod.md#inputmethodgetcontroller9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodController](js-apis-inputmethod.md#inputmethodcontroller) | 回调返回当前客户端实例。 |

**示例：**

```
1. let inputMethodController: inputMethod.InputMethodController = inputMethod.getInputMethodController();
```

## inputMethod.getInputMethodSetting(deprecated)

PhonePC/2in1TabletTVWearable

getInputMethodSetting(): InputMethodSetting

获取客户端设置实例[InputMethodSetting](js-apis-inputmethod.md#inputmethodsetting8)。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getSetting](js-apis-inputmethod.md#inputmethodgetsetting9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [InputMethodSetting](js-apis-inputmethod.md#inputmethodsetting8) | 返回当前客户端设置实例。 |

**示例：**

```
1. let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getInputMethodSetting();
```

## inputMethod.setSimpleKeyboardEnabled20+

PhonePC/2in1TabletTVWearable

setSimpleKeyboardEnabled(enable: boolean): void

编辑框应用设置简单键盘标志。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | 简单键盘是否使能标志，true标识简单键盘使能，false标识简单键盘去使能。  原生编辑框组件在下一次点击获焦时生效；自绘控件在下一次调用[attach](js-apis-inputmethod.md#attach10)绑定输入法时生效。 |

**示例：**

```
1. let enable: boolean = false;
2. inputMethod.setSimpleKeyboardEnabled(enable);
```

## inputMethod.onAttachmentDidFail22+

PhonePC/2in1TabletTVWearable

onAttachmentDidFail(callback: Callback<AttachFailureReason>): void

订阅绑定失败事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AttachFailureReason](js-apis-inputmethod.md#attachfailurereason22)> | 是 | 回调函数，返回绑定失败的原因，仅当注册者进程触发的绑定失败时，调用该回调函数。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let attachmentDidFailCallback: Callback<inputMethod.AttachFailureReason> =
4. (reason: inputMethod.AttachFailureReason): void => {
5. console.info(`Attachment failed with reason: ${reason}.`);
6. if (reason === inputMethod.AttachFailureReason.CALLER_NOT_FOCUSED) {
7. console.info(`Failure reason is CALLER_NOT_FOCUSED.`);
8. }
9. };
10. inputMethod.onAttachmentDidFail(attachmentDidFailCallback);
```

## inputMethod.offAttachmentDidFail22+

PhonePC/2in1TabletTVWearable

offAttachmentDidFail(callback?: Callback<AttachFailureReason>): void

取消订阅绑定失败事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[AttachFailureReason](js-apis-inputmethod.md#attachfailurereason22)> | 否 | 取消订阅的回调函数，需要与订阅接口传入的保持一致。参数不填写时，取消订阅该事件的所有回调函数。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let attachmentDidFailCallback: Callback<inputMethod.AttachFailureReason> =
4. (reason: inputMethod.AttachFailureReason): void => {
5. console.info(`Attachment failed with reason: ${reason}.`);
6. if (reason === inputMethod.AttachFailureReason.CALLER_NOT_FOCUSED) {
7. console.info(`Failure reason is CALLER_NOT_FOCUSED.`);
8. }
9. };
10. inputMethod.onAttachmentDidFail(attachmentDidFailCallback);
11. inputMethod.offAttachmentDidFail(attachmentDidFailCallback);
```

## TextInputType10+

PhonePC/2in1TabletTVWearable

文本输入类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | -1 | NONE。 |
| TEXT | 0 | 文本类型。 |
| MULTILINE | 1 | 多行类型。 |
| NUMBER | 2 | 数字类型。 |
| PHONE | 3 | 电话号码类型。 |
| DATETIME | 4 | 日期类型。 |
| EMAIL\_ADDRESS | 5 | 邮箱地址类型。 |
| URL | 6 | 链接类型。 |
| VISIBLE\_PASSWORD | 7 | 密码类型。 |
| NUMBER\_PASSWORD11+ | 8 | 数字密码类型。 |
| SCREEN\_LOCK\_PASSWORD20+ | 9 | 锁屏密码类型。 |
| USER\_NAME20+ | 10 | 用户名类型。 |
| NEW\_PASSWORD20+ | 11 | 新密码类型。 |
| NUMBER\_DECIMAL20+ | 12 | 带小数点的数字类型。 |
| ONE\_TIME\_CODE20+ | 13 | 验证码类型。 |

## EnterKeyType10+

PhonePC/2in1TabletTVWearable

Enter键的功能类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSPECIFIED | 0 | 未指定。 |
| NONE | 1 | NONE。 |
| GO | 2 | 前往。 |
| SEARCH | 3 | 查找。 |
| SEND | 4 | 发送。 |
| NEXT | 5 | 下一步。 |
| DONE | 6 | 完成。 |
| PREVIOUS | 7 | 上一步。 |
| NEWLINE12+ | 8 | 换行。 |

## KeyboardStatus10+

PhonePC/2in1TabletTVWearable

输入法软键盘状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | NONE。 |
| HIDE | 1 | 隐藏状态。 |
| SHOW | 2 | 显示状态。 |

## Direction10+

PhonePC/2in1TabletTVWearable

光标移动方向。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CURSOR\_UP | 1 | 向上。 |
| CURSOR\_DOWN | 2 | 向下。 |
| CURSOR\_LEFT | 3 | 向左。 |
| CURSOR\_RIGHT | 4 | 向右。 |

## ExtendAction10+

PhonePC/2in1TabletTVWearable

编辑框中文本的扩展编辑操作类型，如剪切、复制等。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SELECT\_ALL | 0 | 全选。 |
| CUT | 3 | 剪切。 |
| COPY | 4 | 复制。 |
| PASTE | 5 | 粘贴。 |

## FunctionKey10+

PhonePC/2in1TabletTVWearable

输入法功能键类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| enterKeyType | [EnterKeyType](js-apis-inputmethod.md#enterkeytype10) | 否 | 否 | 输入法enter键类型。 |

## InputAttribute10+

PhonePC/2in1TabletTVWearable

编辑框属性，包含文本输入类型和Enter键功能类型。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| textInputType | [TextInputType](js-apis-inputmethod.md#textinputtype10) | 否 | 否 | 文本输入类型。 |
| enterKeyType | [EnterKeyType](js-apis-inputmethod.md#enterkeytype10) | 否 | 否 | Enter键功能类型。 |
| placeholder20+ | string | 否 | 是 | 编辑框设置的占位符信息。  - 编辑框设置占位符信息时，长度不超过255个字符（如果超出将会自动截断为255个字符），用于提示或引导用户输入临时性文本或符号。（例如：提示输入项为"必填"或"非必填"的输入结果反馈。）  - 编辑框没有设置占位符信息时，默认为空字符串。  - 该字段在调用[attach](js-apis-inputmethod.md#attach10)时提供给输入法应用。 |
| abilityName20+ | string | 否 | 是 | 编辑框设置的ability名称。  - 编辑框设置ability名称时，长度不超过127个字符（如果超出将会自动截断为127个字符）。  - 编辑框未设置ability名称时，默认为空字符串。  - 该字段在调用绑定[attach](js-apis-inputmethod.md#attach10)时提供给输入法应用。 |

## TextConfig10+

PhonePC/2in1TabletTVWearable

编辑框的配置信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| inputAttribute | [InputAttribute](js-apis-inputmethod.md#inputattribute10) | 否 | 否 | 编辑框属性。 |
| cursorInfo | [CursorInfo](js-apis-inputmethod.md#cursorinfo10) | 否 | 是 | 光标信息。 |
| selection | [Range](js-apis-inputmethod.md#range10) | 否 | 是 | 文本选中的范围。 |
| windowId | number | 否 | 是 | 编辑框所在的窗口Id，该参数应为整数。  推荐使用[getWindowProperties](arkts-apis-window-window.md#getwindowproperties9)方法获取窗口id属性。 |
| newEditBox20+ | boolean | 否 | 是 | 表示是否为新编辑框。true表示新编辑框，false表示非新编辑框。 |
| capitalizeMode20+ | [CapitalizeMode](js-apis-inputmethod.md#capitalizemode20) | 否 | 是 | 编辑框设置大小写模式。如果没有设置或设置非法值，默认不进行任何首字母大写处理。 |

## CursorInfo10+

PhonePC/2in1TabletTVWearable

光标信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 光标的横坐标，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的宽度。 |
| top | number | 否 | 否 | 光标的纵坐标，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的高度。 |
| width | number | 否 | 否 | 光标的宽度，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的宽度。 |
| height | number | 否 | 否 | 光标的高度，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的高度 |

## Range10+

PhonePC/2in1TabletTVWearable

文本的选中范围。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| start | number | 否 | 否 | 选中文本的首字符在编辑框的索引值。该参数应为大于或等于0的整数，不超过文本实际长度。 |
| end | number | 否 | 否 | 选中文本的末字符在编辑框的索引值。该参数应为大于或等于0的整数，不超过文本实际长度，end值要大于start值。 |

## Movement10+

PhonePC/2in1TabletTVWearable

选中文本时，光标移动的方向。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| direction | [Direction](js-apis-inputmethod.md#direction10) | 否 | 否 | 选中文本时，光标的移动方向。 |

## InputWindowInfo10+

PhonePC/2in1TabletTVWearable

输入法软键盘的窗口信息。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| name | string | 否 | 否 | 输入法窗口的名称。 |
| left | number | 否 | 否 | 输入法窗口左上顶点的横坐标，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的宽度。 |
| top | number | 否 | 否 | 输入法窗口左上顶点的纵坐标，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的高度。 |
| width | number | 否 | 否 | 输入法窗口的宽度，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的宽度。 |
| height | number | 否 | 否 | 输入法窗口的高度，单位为px。该参数应为整数，最小值为0，最大值为当前屏幕的高度。 |
| displayId23+ | number | 否 | 是 | 输入法软键盘窗口所在的屏幕ID。  **模型约束：** 该参数仅可在Stage模型下使用。 |

## EnabledState15+

PhonePC/2in1TabletTVWearable

输入法启用状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DISABLED | 0 | 未启用。 |
| BASIC\_MODE | 1 | 基础模式。 |
| FULL\_EXPERIENCE\_MODE | 2 | 完整体验模式。 |

## RequestKeyboardReason15+

PhonePC/2in1TabletTVWearable

请求键盘输入的原因。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 表示没有特定的原因触发键盘请求。 |
| MOUSE | 1 | 表示键盘请求是由鼠标操作触发的。 |
| TOUCH | 2 | 表示键盘请求是由触摸操作触发的。 |
| OTHER | 20 | 表示键盘请求是由其他原因触发的。 |

## MessageHandler15+

PhonePC/2in1TabletTVWearable

自定义通信对象。

说明

开发者可通过注册此对象来接收输入法应用发送的自定义通信数据，接收到自定义通信数据时会触发此对象中[onMessage](js-apis-inputmethod.md#onmessage15)回调函数。

此对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的[onTerminated](js-apis-inputmethod.md#onterminated15)回调函数。

若取消注册全局已注册的对象时，会触发被取消对象中[onTerminated](js-apis-inputmethod.md#onterminated15)回调函数。

### onMessage15+

PhonePC/2in1TabletTVWearable

onMessage(msgId: string, msgParam?: ArrayBuffer): void

接收输入法应用发送的自定义数据回调函数。

说明

当已注册的MessageHandler接收到来自输入法应用发送的自定义通信数据时，会触发该回调函数。

msgId为必选参数，msgParam为可选参数。存在收到仅有msgId自定义数据的可能，需与数据发送方确认自定义数据。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msgId | string | 是 | 接收到的自定义通信数据的标识符。 |
| msgParam | ArrayBuffer | 否 | 接收到的自定义通信数据的消息体。 |

**示例：**

```
1. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

3. let messageHandler: inputMethod.MessageHandler = {
4. onTerminated(): void {
5. console.info('OnTerminated.');
6. },
7. onMessage(msgId: string, msgParam?: ArrayBuffer): void {
8. console.info(`recv message, msg: ${msgId}, msgParam: ${JSON.stringify(msgParam)}`);
9. }
10. };
11. inputMethodController.recvMessage(messageHandler);
```

### onTerminated15+

PhonePC/2in1TabletTVWearable

onTerminated(): void

监听对象终止回调函数。

说明

当应用注册新的MessageHandler对象时，会触发上一个已注册MessageHandler对象的OnTerminated回调函数。

当应用取消注册时，会触发当前已注册MessageHandler对象的OnTerminated回调函数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**示例：**

```
1. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();

3. let messageHandler: inputMethod.MessageHandler = {
4. onTerminated(): void {
5. console.info('OnTerminated.');
6. },
7. onMessage(msgId: string, msgParam?: ArrayBuffer): void {
8. console.info(`recv message, msg: ${msgId}, msgParam: ${JSON.stringify(msgParam)}`);
9. }
10. };
11. inputMethodController.recvMessage(messageHandler);
```

## SetPreviewTextCallback17+

PhonePC/2in1TabletTVWearable

type SetPreviewTextCallback = (text: string, range: Range) => void

当输入法框架需要显示预览文本时触发的回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 预览文本内容。 |
| range | [Range](js-apis-inputmethod.md#range10) | 是 | 文本的选中范围。 |

## AttachFailureReason22+

PhonePC/2in1TabletTVWearable

枚举，绑定失败的原因。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 值 | 说明 |
| --- | --- | --- |
| CALLER\_NOT\_FOCUSED | 0 | 表示调用者非焦点窗口所属应用导致的失败。 |
| IME\_ABNORMAL | 1 | 表示输入法应用异常导致的失败。 |
| SERVICE\_ABNORMAL | 2 | 表示输入法框架服务异常导致的失败。 |

## AttachOptions23+

PhonePC/2in1TabletTVWearable

绑定输入法的附加选项。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| requestKeyboardReason | [RequestKeyboardReason](js-apis-inputmethod.md#requestkeyboardreason15) | 否 | 是 | 请求键盘输入的原因。 |
| showKeyboard | boolean | 否 | 是 | 绑定输入法成功后，是否拉起输入法键盘。  - true表示拉起。  - false表示不拉起。 |

## InputMethodController

PhonePC/2in1TabletTVWearable

下列API示例中都需使用[getController](js-apis-inputmethod.md#inputmethodgetcontroller9)获取到InputMethodController实例，再通过实例调用对应方法。

### attach10+

PhonePC/2in1TabletTVWearable

attach(showKeyboard: boolean, textConfig: TextConfig, callback: AsyncCallback<void>): void

自绘控件绑定输入法。使用callback异步回调。

说明

需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。

当自绘控件所在窗口通过[setWindowFocusable](arkts-apis-window-window.md#setwindowfocusable9)设置为不可获焦窗口时，系统将无法保证自绘输入控件与输入法正常交互。若开发者希望在不可获焦窗口中绘制输入框，建议参考[不可获焦窗口中输入框与输入法交互指南](../harmonyos-guides/use-inputmethod-in-not-focusable-window.md)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| showKeyboard | boolean | 是 | 绑定输入法成功后，是否拉起输入法键盘。  - true表示拉起。  - false表示不拉起。 |
| textConfig | [TextConfig](js-apis-inputmethod.md#textconfig10) | 是 | 编辑框的配置信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当绑定输入法成功后，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let inputAttribute: inputMethod.InputAttribute = {
4. textInputType: inputMethod.TextInputType.TEXT,
5. enterKeyType: inputMethod.EnterKeyType.GO
6. }
7. let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
8. inputMethod.getController().attach(true, textConfig, (err: BusinessError) => {
9. if (err) {
10. console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
11. return;
12. }
13. console.info('Succeeded in attaching the inputMethod.');
14. });
```

### attach10+

PhonePC/2in1TabletTVWearable

attach(showKeyboard: boolean, textConfig: TextConfig): Promise<void>

自绘控件绑定输入法。使用promise异步回调。

说明

需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。

当自绘控件所在窗口通过[setWindowFocusable](arkts-apis-window-window.md#setwindowfocusable9)设置为不可获焦窗口时，系统将无法保证自绘输入控件与输入法正常交互。若开发者希望在不可获焦窗口中绘制输入框，建议参考[不可获焦窗口中输入框与输入法交互指南](../harmonyos-guides/use-inputmethod-in-not-focusable-window.md)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| showKeyboard | boolean | 是 | 绑定输入法成功后，是否拉起输入法键盘。  - true表示拉起。  - false表示不拉起。 |
| textConfig | [TextConfig](js-apis-inputmethod.md#textconfig10) | 是 | 编辑框的配置信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let inputAttribute: inputMethod.InputAttribute = {
4. textInputType: inputMethod.TextInputType.TEXT,
5. enterKeyType: inputMethod.EnterKeyType.GO
6. }
7. let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
8. inputMethod.getController().attach(true, textConfig).then(() => {
9. console.info('Succeeded in attaching inputMethod.');
10. }).catch((err: BusinessError) => {
11. console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
12. });
```

### attach15+

PhonePC/2in1TabletTVWearable

attach(showKeyboard: boolean, textConfig: TextConfig, requestKeyboardReason: RequestKeyboardReason): Promise<void>

自绘控件绑定输入法。使用promise异步回调。

说明

需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。

当自绘控件所在窗口通过[setWindowFocusable](arkts-apis-window-window.md#setwindowfocusable9)设置为不可获焦窗口时，系统将无法保证自绘输入控件与输入法正常交互。若开发者希望在不可获焦窗口中绘制输入框，建议参考[不可获焦窗口中输入框与输入法交互指南](../harmonyos-guides/use-inputmethod-in-not-focusable-window.md)。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| showKeyboard | boolean | 是 | 绑定输入法成功后，是否拉起输入法键盘。  - true表示拉起。  - false表示不拉起。 |
| textConfig | [TextConfig](js-apis-inputmethod.md#textconfig10) | 是 | 编辑框的配置信息。 |
| requestKeyboardReason | [RequestKeyboardReason](js-apis-inputmethod.md#requestkeyboardreason15) | 是 | 请求键盘输入的原因。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)和[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let inputAttribute: inputMethod.InputAttribute = {
4. textInputType: inputMethod.TextInputType.TEXT,
5. enterKeyType: inputMethod.EnterKeyType.GO
6. }
7. let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
8. let requestKeyboardReason: inputMethod.RequestKeyboardReason = inputMethod.RequestKeyboardReason.MOUSE;

10. inputMethod.getController().attach(true, textConfig, requestKeyboardReason).then(() => {
11. console.info('Succeeded in attaching inputMethod.');
12. }).catch((err: BusinessError) => {
13. console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
14. });
```

### attachWithUIContext23+

PhonePC/2in1TabletTVWearable

attachWithUIContext(uiContext: UIContext, textConfig: TextConfig, attachOptions?: AttachOptions): Promise<void>

自绘控件绑定输入法。使用promise异步回调。

说明

需要先调用此接口，完成自绘控件与输入法的绑定，才能使用以下功能：显示/隐藏键盘、更新光标信息、更改编辑框选中范围、保存配置信息、监听处理由输入法应用发送的信息或命令等。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | UIContext实例对象。 |
| textConfig | [TextConfig](js-apis-inputmethod.md#textconfig10) | 是 | 编辑框的配置信息。 |
| attachOptions | [AttachOptions](js-apis-inputmethod.md#attachoptions23) | 否 | 绑定附加选项。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes:1.the edit box is not focused. 2.no edit box is bound to current input method application.3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { UIContext } from '@kit.ArkUI';

4. let uiContext: UIContext | undefined = UIContext.getCallingScopeUIContext();
5. let inputAttribute: inputMethod.InputAttribute = {
6. textInputType: inputMethod.TextInputType.TEXT,
7. enterKeyType: inputMethod.EnterKeyType.GO
8. }
9. let textConfig: inputMethod.TextConfig = { inputAttribute: inputAttribute };
10. let attachOptions: inputMethod.AttachOptions = { showKeyboard: true };
11. inputMethod.getController().attachWithUIContext(uiContext, textConfig, attachOptions).then(() => {
12. console.info('Succeeded in attaching inputMethod.');
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to attach, code: ${err.code}, message: ${err.message}`);
15. });
```

### discardTypingText20+

PhonePC/2in1TabletTVWearable

discardTypingText(): Promise<void>

编辑框应用发送“清空正在输入的文字”命令到输入法。使用promise异步回调。

说明

当编辑框应用与输入法绑定成功后，才可调用该接口实现此功能。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800009 | input method client detached. |
| 12800015 | the other side does not accept the request. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().discardTypingText().then(() => {
4. console.info('Succeeded discardTypingText.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to discardTypingText, code: ${err.code}, message: ${err.message}`);
7. });
```

### showTextInput10+

PhonePC/2in1TabletTVWearable

showTextInput(callback: AsyncCallback<void>): void

进入文本编辑状态。使用callback异步回调。

说明

编辑框与输入法绑定成功后，可调用该接口拉起软键盘，进入文本编辑状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。若成功进入编辑状态，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().showTextInput((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in showing the inputMethod.');
9. });
```

### showTextInput10+

PhonePC/2in1TabletTVWearable

showTextInput(): Promise<void>

进入文本编辑状态。使用promise异步回调。

说明

编辑框与输入法绑定成功后，可调用该接口拉起软键盘，进入文本编辑状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().showTextInput().then(() => {
4. console.info('Succeeded in showing text input.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
7. });
```

### showTextInput15+

PhonePC/2in1TabletTVWearable

showTextInput(requestKeyboardReason: RequestKeyboardReason): Promise<void>

进入文本编辑状态。使用promise异步回调。

说明

编辑框与输入法绑定成功后，可调用该接口拉起软键盘，进入文本编辑状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| requestKeyboardReason | [RequestKeyboardReason](js-apis-inputmethod.md#requestkeyboardreason15) | 是 | 请求键盘输入的原因。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let requestKeyboardReason: inputMethod.RequestKeyboardReason = inputMethod.RequestKeyboardReason.MOUSE;

5. inputMethod.getController().showTextInput(requestKeyboardReason).then(() => {
6. console.info('Succeeded in showing text input.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to showTextInput, code: ${err.code}, message: ${err.message}`);
9. });
```

### hideTextInput10+

PhonePC/2in1TabletTVWearable

hideTextInput(callback: AsyncCallback<void>): void

退出文本编辑状态。使用callback异步回调。

说明

调用接口时，若软键盘处于显示状态，调用接口后软键盘会被隐藏。

调用该接口不会解除与输入法的绑定，再次调用[showTextInput](js-apis-inputmethod.md#showtextinput10)时，可重新进入文本编辑状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当成功退出编辑状态时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().hideTextInput((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to hideTextInput, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in hiding text input.');
9. });
```

### hideTextInput10+

PhonePC/2in1TabletTVWearable

hideTextInput(): Promise<void>

退出文本编辑状态。使用promise异步回调。

说明

调用接口时，若软键盘处于显示状态，调用接口后软键盘会被隐藏。

调用该接口不会解除与输入法的绑定，再次调用[showTextInput](js-apis-inputmethod.md#showtextinput10)时，可重新进入文本编辑状态。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().hideTextInput().then(() => {
4. console.info('Succeeded in hiding inputMethod.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to hideTextInput, code: ${err.code}, message: ${err.message}`);
7. })
```

### detach10+

PhonePC/2in1TabletTVWearable

detach(callback: AsyncCallback<void>): void

自绘控件解除与输入法的绑定。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当解绑定输入法成功时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().detach((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to detach, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in detaching inputMethod.');
9. });
```

### detach10+

PhonePC/2in1TabletTVWearable

detach(): Promise<void>

自绘控件解除与输入法的绑定。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().detach().then(() => {
4. console.info('Succeeded in detaching inputMethod.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to detach, code: ${err.code}, message: ${err.message}`);
7. });
```

### setCallingWindow10+

PhonePC/2in1TabletTVWearable

setCallingWindow(windowId: number, callback: AsyncCallback<void>): void

设置要避让软键盘的窗口。使用callback异步回调。

说明

将绑定到输入法的应用程序所在的窗口Id传入，此窗口可以避让输入法窗口。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | number | 是 | 绑定输入法应用的应用程序所在的窗口Id。该参数应为整数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当设置成功时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let windowId: number = 2000;
4. inputMethod.getController().setCallingWindow(windowId, (err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to setCallingWindow, code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in setting callingWindow.');
10. });
```

### setCallingWindow10+

PhonePC/2in1TabletTVWearable

setCallingWindow(windowId: number): Promise<void>

设置要避让软键盘的窗口。使用promise异步回调。

说明

将绑定到输入法的应用程序所在的窗口Id传入，此窗口可以避让输入法窗口。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | number | 是 | 绑定输入法应用的应用程序所在的窗口Id。该参数应为整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let windowId: number = 2000;
4. inputMethod.getController().setCallingWindow(windowId).then(() => {
5. console.info('Succeeded in setting callingWindow.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to setCallingWindow, code: ${err.code}, message: ${err.message}`);
8. })
```

### updateCursor10+

PhonePC/2in1TabletTVWearable

updateCursor(cursorInfo: CursorInfo, callback: AsyncCallback<void>): void

当编辑框内的光标信息发生变化时，调用该接口使输入法感知到光标变化。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cursorInfo | [CursorInfo](js-apis-inputmethod.md#cursorinfo10) | 是 | 光标信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当光标信息更新成功时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let cursorInfo: inputMethod.CursorInfo = {
4. left: 0,
5. top: 0,
6. width: 600,
7. height: 800
8. };
9. inputMethod.getController().updateCursor(cursorInfo, (err: BusinessError) => {
10. if (err) {
11. console.error(`Failed to updateCursor, code: ${err.code}, message: ${err.message}`);
12. return;
13. }
14. console.info('Succeeded in updating cursorInfo.');
15. });
```

### updateCursor10+

PhonePC/2in1TabletTVWearable

updateCursor(cursorInfo: CursorInfo): Promise<void>

当编辑框内的光标信息发生变化时，调用该接口使输入法感知到光标变化。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| cursorInfo | [CursorInfo](js-apis-inputmethod.md#cursorinfo10) | 是 | 光标信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let cursorInfo: inputMethod.CursorInfo = {
4. left: 0,
5. top: 0,
6. width: 600,
7. height: 800
8. };
9. inputMethod.getController().updateCursor(cursorInfo).then(() => {
10. console.info('Succeeded in updating cursorInfo.');
11. }).catch((err: BusinessError) => {
12. console.error(`Failed to updateCursor, code: ${err.code}, message: ${err.message}`);
13. });
```

### changeSelection10+

PhonePC/2in1TabletTVWearable

changeSelection(text: string, start: number, end: number, callback: AsyncCallback<void>): void

当编辑框内被选中的文本信息内容或文本范围发生变化时，可调用该接口更新文本信息，使输入法应用感知到变化。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 整个输入文本。 |
| start | number | 是 | 所选文本的起始位置。该参数应为大于或等于0的整数。 |
| end | number | 是 | 所选文本的结束位置。该参数应为大于或等于0的整数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当文本信息更新成功时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().changeSelection('text', 0, 5, (err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to changeSelection, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in changing selection.');
9. });
```

### changeSelection10+

PhonePC/2in1TabletTVWearable

changeSelection(text: string, start: number, end: number): Promise<void>

当编辑框内被选中的文本信息内容或文本范围发生变化时，可调用该接口更新文本信息，使输入法应用感知到变化。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 整个输入文本。 |
| start | number | 是 | 所选文本的起始位置。该参数应为大于或等于0的整数。 |
| end | number | 是 | 所选文本的结束位置。该参数应为大于或等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().changeSelection('test', 0, 5).then(() => {
4. console.info('Succeeded in changing selection.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to changeSelection, code: ${err.code}, message: ${err.message}`);
7. });
```

### updateAttribute10+

PhonePC/2in1TabletTVWearable

updateAttribute(attribute: InputAttribute, callback: AsyncCallback<void>): void

更新编辑框属性信息。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attribute | [InputAttribute](js-apis-inputmethod.md#inputattribute10) | 是 | 编辑框属性对象。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当编辑框属性信息更新成功时，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let inputAttribute: inputMethod.InputAttribute = { textInputType: 0, enterKeyType: 1 };
4. inputMethod.getController().updateAttribute(inputAttribute, (err: BusinessError) => {
5. if (err) {
6. console.error(`Failed to updateAttribute, code: ${err.code}, message: ${err.message}`);
7. return;
8. }
9. console.info('Succeeded in updating attribute.');
10. });
```

### updateAttribute10+

PhonePC/2in1TabletTVWearable

updateAttribute(attribute: InputAttribute): Promise<void>

更新编辑框属性信息。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| attribute | [InputAttribute](js-apis-inputmethod.md#inputattribute10) | 是 | 编辑框属性对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |
| 12800009 | input method client detached. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let inputAttribute: inputMethod.InputAttribute = { textInputType: 0, enterKeyType: 1 };
4. inputMethod.getController().updateAttribute(inputAttribute).then(() => {
5. console.info('Succeeded in updating attribute.');
6. }).catch((err: BusinessError) => {
7. console.error(`Failed to updateAttribute, code: ${err.code}, message: ${err.message}`);
8. });
```

### stopInputSession9+

PhonePC/2in1TabletTVWearable

stopInputSession(callback: AsyncCallback<boolean>): void

结束输入会话。使用callback异步回调。

说明

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当结束输入会话成功时，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().stopInputSession((err: BusinessError, result: boolean) => {
4. if (err) {
5. console.error(`Failed to stopInputSession, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. if (result) {
9. console.info('Succeeded in stopping inputSession.');
10. } else {
11. console.error('Failed to stopInputSession.');
12. }
13. });
```

### stopInputSession9+

PhonePC/2in1TabletTVWearable

stopInputSession(): Promise<boolean>

结束输入会话。使用promise异步回调。

说明

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示结束输入会话成功，返回false表示结束输入会话失败。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().stopInputSession().then((result: boolean) => {
4. if (result) {
5. console.info('Succeeded in stopping inputSession.');
6. } else {
7. console.error('Failed to stopInputSession.');
8. }
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to stopInputSession, code: ${err.code}, message: ${err.message}`);
11. });
```

### showSoftKeyboard9+

PhonePC/2in1TabletTVWearable

showSoftKeyboard(callback: AsyncCallback<void>): void

显示输入法软键盘。使用callback异步回调。

说明

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用显示当前输入法的软键盘。

**需要权限：** ohos.permission.CONNECT\_IME\_ABILITY，仅系统应用可用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当软键盘显示成功。err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permissions check fails. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().showSoftKeyboard((err: BusinessError) => {
4. if (!err) {
5. console.info('Succeeded in showing softKeyboard.');
6. } else {
7. console.error(`Failed to show softKeyboard, ${err.code}, message: ${err.message}`);
8. }
9. });
```

### showSoftKeyboard9+

PhonePC/2in1TabletTVWearable

showSoftKeyboard(): Promise<void>

显示输入法软键盘。使用Promise异步回调。

说明

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用显示当前输入法的软键盘。

**需要权限：** ohos.permission.CONNECT\_IME\_ABILITY，仅系统应用可用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permissions check fails. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().showSoftKeyboard().then(() => {
4. console.info('Succeeded in showing softKeyboard.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to show softKeyboard, code: ${err.code}, message: ${err.message}`);
7. });
```

### hideSoftKeyboard9+

PhonePC/2in1TabletTVWearable

hideSoftKeyboard(callback: AsyncCallback<void>): void

隐藏输入法软键盘。使用callback异步回调。

说明

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用隐藏当前输入法的软键盘。

**需要权限：** ohos.permission.CONNECT\_IME\_ABILITY，仅系统应用可用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当软键盘隐藏成功。err为undefined，否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permissions check fails. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().hideSoftKeyboard((err: BusinessError) => {
4. if (!err) {
5. console.info('Succeeded in hiding softKeyboard.');
6. } else {
7. console.error(`Failed to hide softKeyboard, code: ${err.code}, message: ${err.message}`);
8. }
9. })
```

### hideSoftKeyboard9+

PhonePC/2in1TabletTVWearable

hideSoftKeyboard(): Promise<void>

隐藏输入法软键盘。使用Promise异步回调。

说明

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用隐藏当前输入法的软键盘。

**需要权限：** ohos.permission.CONNECT\_IME\_ABILITY，仅系统应用可用。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | permissions check fails. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().hideSoftKeyboard().then(() => {
4. console.info('Succeeded in hiding softKeyboard.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to hide softKeyboard, code: ${err.code}, message: ${err.message}`);
7. });
```

### sendMessage15+

PhonePC/2in1TabletTVWearable

sendMessage(msgId: string, msgParam?: ArrayBuffer): Promise<void>

发送自定义通信至输入法应用。使用Promise异步回调。

说明

该接口需要编辑框与输入法绑定并进入编辑状态，且输入法应用处于完整体验模式时才能调用。

msgId最大限制256B，msgParam最大限制128KB。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msgId | string | 是 | 需要发送至输入法应用的自定义数据的标识符。 |
| msgParam | ArrayBuffer | 否 | 需要发送至输入法应用的自定义数据的消息体。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Incorrect parameter types. 2. Incorrect parameter length. |
| 12800003 | input method client error. Possible causes: 1.the edit box is not focused. 2.no edit box is bound to current input method application. 3.ipc failed due to the large amount of data transferred or other reasons. |
| 12800009 | input method client detached. |
| 12800014 | the input method is in basic mode. |
| 12800015 | the other side does not accept the request. |
| 12800016 | input method client is not editable. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let msgId: string = "testMsgId";
4. let msgParam: ArrayBuffer = new ArrayBuffer(128);
5. inputMethod.getController().sendMessage(msgId, msgParam).then(() => {
6. console.info('Succeeded send message.');
7. }).catch((err: BusinessError) => {
8. console.error(`Failed to send message, code: ${err.code}, message: ${err.message}`);
9. });
```

### recvMessage15+

PhonePC/2in1TabletTVWearable

recvMessage(msgHandler?: MessageHandler): void

注册或取消注册MessageHandler。

说明

[MessageHandler](js-apis-inputmethod.md#messagehandler15)对象全局唯一，多次注册仅保留最后一次注册的对象及有效性，并触发上一个已注册对象的[onTerminated](js-apis-inputmethod.md#onterminated15)回调函数。

未填写参数，则取消全局已注册的[MessageHandler](js-apis-inputmethod.md#messagehandler15)，并触发被取消注册对象中[onTerminated](js-apis-inputmethod.md#onterminated15)回调函数。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| msgHandler | [MessageHandler](js-apis-inputmethod.md#messagehandler15) | 否 | 该对象通过[onMessage](js-apis-inputmethod.md#onmessage15)接收来自输入法应用所发送的自定义通信数据，并通过[onTerminated](js-apis-inputmethod.md#onterminated15)接收终止此对象订阅的消息。  若不填写此参数，则取消全局已注册的[MessageHandler](js-apis-inputmethod.md#messagehandler15)对象，同时触发其[onTerminated](js-apis-inputmethod.md#onterminated15)回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Incorrect parameter types. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let messageHandler: inputMethod.MessageHandler = {
4. onTerminated(): void {
5. console.info('OnTerminated.');
6. },
7. onMessage(msgId: string, msgParam?: ArrayBuffer): void {
8. console.info('recv message.');
9. }
10. };
11. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
12. inputMethodController.recvMessage(messageHandler);
13. // 取消已注册的MessageHandler
14. inputMethodController.recvMessage();
```

### stopInput(deprecated)

PhonePC/2in1TabletTVWearable

stopInput(callback: AsyncCallback<boolean>): void

结束输入会话。使用callback异步回调。

说明

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

从API version 6开始支持，从API version 9开始废弃，建议使用[stopInputSession](js-apis-inputmethod.md#stopinputsession9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当会话结束成功，err为undefined，data为true；否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().stopInput((err: BusinessError, result: boolean) => {
4. if (err) {
5. console.error(`Failed to stopInput, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. if (result) {
9. console.info('Succeeded in stopping input.');
10. } else {
11. console.error('Failed to stopInput.');
12. }
13. });
```

### stopInput(deprecated)

PhonePC/2in1TabletTVWearable

stopInput(): Promise<boolean>

结束输入会话。使用promise异步回调。

说明

该接口需要编辑框与输入法绑定时才能调用，即点击编辑控件后，才可调用该接口结束输入会话。

从API version 6开始支持，从API version 9开始废弃，建议使用[stopInputSession](js-apis-inputmethod.md#stopinputsession9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回true表示会话结束成功；返回false表示会话结束失败。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getController().stopInput().then((result: boolean) => {
4. if (result) {
5. console.info('Succeeded in stopping input.');
6. } else {
7. console.error('Failed to stopInput.');
8. }
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to stopInput, code: ${err.code}, message: ${err.message}`);
11. })
```

### on('insertText')10+

PhonePC/2in1TabletTVWearable

on(type: 'insertText', callback: (text: string) => void): void

订阅输入法应用插入文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'insertText'。 |
| callback | (text: string) => void | 是 | 回调函数，返回需要插入的文本内容。  根据传入的文本，在回调函数中操作编辑框中的内容。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```
1. function callback1(text: string): void {
2. console.info(`Succeeded in getting callback1, data: ${text}`);
3. }

5. function callback2(text: string): void {
6. console.info(`Succeeded in getting callback2, data: ${text}`);
7. }

9. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
10. // 注册回调
11. inputMethodController.on('insertText', callback1);
12. inputMethodController.on('insertText', callback2);
13. // 仅取消insertText的callback1的回调
14. inputMethodController.off('insertText', callback1);
15. // 取消insertText的所有回调
16. inputMethodController.off('insertText');
```

### off('insertText')10+

PhonePC/2in1TabletTVWearable

off(type: 'insertText', callback?: (text: string) => void): void

取消订阅输入法应用插入文本事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'insertText'。 |
| callback | (text: string) => void | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。  参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let onInsertTextCallback: Callback<string> = (text: string): void => {
4. console.info(`Succeeded in subscribing insertText: ${text}`);
5. };

7. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
8. inputMethodController.off('insertText', onInsertTextCallback);
9. inputMethodController.off('insertText');
```

### on('deleteLeft')10+

PhonePC/2in1TabletTVWearable

on(type: 'deleteLeft', callback: (length: number) => void): void

订阅输入法应用向左删除文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'deleteLeft'。 |
| callback | (length: number) => void | 是 | 回调函数，返回需要向左删除的文本长度。  根据传入的删除长度，在回调函数中操作编辑框中的文本。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```
1. inputMethod.getController().on('deleteLeft', (length: number) => {
2. console.info(`Succeeded in subscribing deleteLeft, length: ${length}`);
3. });
```

### off('deleteLeft')10+

PhonePC/2in1TabletTVWearable

off(type: 'deleteLeft', callback?: (length: number) => void): void

取消订阅输入法应用向左删除文本事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听，固定取值为'deleteLeft'。 |
| callback | (length: number) => void | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。  参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let onDeleteLeftCallback: Callback<number> = (length: number): void => {
4. console.info(`Succeeded in subscribing deleteLeft, length: ${length}`);
5. };

7. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
8. inputMethodController.off('deleteLeft', onDeleteLeftCallback);
9. inputMethodController.off('deleteLeft');
```

### on('deleteRight')10+

PhonePC/2in1TabletTVWearable

on(type: 'deleteRight', callback: (length: number) => void): void

订阅输入法应用向右删除文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'deleteRight'。 |
| callback | (length: number) => void | 是 | 回调函数，返回需要向右删除的文本长度。  根据传入的删除长度，在回调函数中操作编辑框中的文本。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```
1. inputMethod.getController().on('deleteRight', (length: number) => {
2. console.info(`Succeeded in subscribing deleteRight, length: ${length}`);
3. });
```

### off('deleteRight')10+

PhonePC/2in1TabletTVWearable

off(type: 'deleteRight', callback?: (length: number) => void): void

取消订阅输入法应用向右删除文本事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为deleteRight。 |
| callback | (length: number) => void | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。  参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let onDeleteRightCallback: Callback<number> = (length: number): void => {
4. console.info(`Succeeded in subscribing deleteRight, length: ${length}`);
5. };
6. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
7. inputMethodController.off('deleteRight', onDeleteRightCallback);
8. inputMethodController.off('deleteRight');
```

### on('sendKeyboardStatus')10+

PhonePC/2in1TabletTVWearable

on(type: 'sendKeyboardStatus', callback: (keyboardStatus: KeyboardStatus) => void): void

订阅输入法应用发送输入法软键盘状态事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'sendKeyboardStatus'。 |
| callback | (keyboardStatus: [KeyboardStatus](js-apis-inputmethod.md#keyboardstatus10)) => void | 是 | 回调函数，返回软键盘状态。  根据传入的软键盘状态，在回调函数中做相应操作。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```
1. inputMethod.getController().on('sendKeyboardStatus', (keyboardStatus: inputMethod.KeyboardStatus) => {
2. console.info(`Succeeded in subscribing sendKeyboardStatus, keyboardStatus: ${keyboardStatus}`);
3. });
```

### off('sendKeyboardStatus')10+

PhonePC/2in1TabletTVWearable

off(type: 'sendKeyboardStatus', callback?: (keyboardStatus: KeyboardStatus) => void): void

取消订阅输入法应用发送输入法软键盘状态事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'sendKeyboardStatus'。 |
| callback | (keyboardStatus: [KeyboardStatus](js-apis-inputmethod.md#keyboardstatus10)) => void | 否 | 取消订阅的回调函数。参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let onSendKeyboardStatus: Callback<inputMethod.KeyboardStatus> = (keyboardStatus: inputMethod.KeyboardStatus): void => {
4. console.info(`Succeeded in subscribing sendKeyboardStatus, keyboardStatus: ${keyboardStatus}`);
5. };

7. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
8. inputMethodController.off('sendKeyboardStatus', onSendKeyboardStatus);
9. inputMethodController.off('sendKeyboardStatus');
```

### on('sendFunctionKey')10+

PhonePC/2in1TabletTVWearable

on(type: 'sendFunctionKey', callback: (functionKey: FunctionKey) => void): void

订阅输入法应用发送功能键事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'sendFunctionKey'。 |
| callback | (functionKey: [FunctionKey](js-apis-inputmethod.md#functionkey10)) => void | 是 | 回调函数，返回输入法应用发送的功能键信息。  根据返回的功能键信息，做相应操作。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```
1. inputMethod.getController().on('sendFunctionKey', (functionKey: inputMethod.FunctionKey) => {
2. console.info(`Succeeded in subscribing sendFunctionKey, functionKey.enterKeyType: ${functionKey.enterKeyType}`);
3. });
```

### off('sendFunctionKey')10+

PhonePC/2in1TabletTVWearable

off(type: 'sendFunctionKey', callback?: (functionKey: FunctionKey) => void): void

取消订阅输入法应用发送功能键事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'sendFunctionKey'。 |
| callback | (functionKey: [FunctionKey](js-apis-inputmethod.md#functionkey10)) => void | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。  参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let onSendFunctionKey: Callback<inputMethod.FunctionKey> = (functionKey: inputMethod.FunctionKey): void => {
4. console.info(`Succeeded in subscribing sendFunctionKey, functionKey: ${functionKey.enterKeyType}`);
5. };

7. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
8. inputMethodController.off('sendFunctionKey', onSendFunctionKey);
9. inputMethodController.off('sendFunctionKey');
```

### on('moveCursor')10+

PhonePC/2in1TabletTVWearable

on(type: 'moveCursor', callback: (direction: Direction) => void): void

订阅输入法应用移动光标事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'moveCursor'。 |
| callback | (direction: [Direction](js-apis-inputmethod.md#direction10)) => void | 是 | 回调函数，返回光标信息。  根据返回的光标移动方向，改变光标位置，如光标向上或向下。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```
1. inputMethod.getController().on('moveCursor', (direction: inputMethod.Direction) => {
2. console.info(`Succeeded in subscribing moveCursor, direction: ${direction}`);
3. });
```

### off('moveCursor')10+

PhonePC/2in1TabletTVWearable

off(type: 'moveCursor', callback?: (direction: Direction) => void): void

取消订阅输入法应用移动光标事件。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'moveCursor'。 |
| callback | (direction: [Direction](js-apis-inputmethod.md#direction10)) => void | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。  参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let onMoveCursorCallback: Callback<inputMethod.Direction> = (direction: inputMethod.Direction): void => {
4. console.info(`Succeeded in subscribing moveCursor, direction: ${direction}`);
5. };

7. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
8. inputMethodController.off('moveCursor', onMoveCursorCallback);
9. inputMethodController.off('moveCursor');
```

### on('handleExtendAction')10+

PhonePC/2in1TabletTVWearable

on(type: 'handleExtendAction', callback: (action: ExtendAction) => void): void

订阅输入法应用发送扩展编辑操作事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'handleExtendAction'。 |
| callback | (action: [ExtendAction](js-apis-inputmethod.md#extendaction10)) => void | 是 | 回调函数，返回扩展编辑操作类型。  根据传入的扩展编辑操作类型，做相应的操作，如剪切、复制等。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```
1. inputMethod.getController().on('handleExtendAction', (action: inputMethod.ExtendAction) => {
2. console.info(`Succeeded in subscribing handleExtendAction, action: ${action}`);
3. });
```

### off('handleExtendAction')10+

PhonePC/2in1TabletTVWearable

off(type: 'handleExtendAction', callback?: (action: ExtendAction) => void): void

取消订阅输入法应用发送扩展编辑操作事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'handleExtendAction'。 |
| callback | (action: [ExtendAction](js-apis-inputmethod.md#extendaction10)) => void | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。  参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let onHandleExtendActionCallback: Callback<inputMethod.ExtendAction> = (action: inputMethod.ExtendAction): void => {
4. console.info(`Succeeded in subscribing handleExtendAction, action: ${action}`);
5. };

7. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
8. inputMethodController.off('handleExtendAction', onHandleExtendActionCallback);
9. inputMethodController.off('handleExtendAction');
```

### on('selectByRange')10+

PhonePC/2in1TabletTVWearable

on(type: 'selectByRange', callback: Callback<Range>): void

订阅输入法应用按范围选中文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'selectByRange'。 |
| callback | Callback<[Range](js-apis-inputmethod.md#range10)> | 是 | 回调函数，返回需要选中的文本范围。  根据传入的文本范围，开发者在回调函数中编辑框中相应文本。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. inputMethod.getController().on('selectByRange', (range: inputMethod.Range) => {
2. console.info(`Succeeded in subscribing selectByRange: start: ${range.start} , end: ${range.end}`);
3. });
```

### off('selectByRange')10+

PhonePC/2in1TabletTVWearable

off(type: 'selectByRange', callback?: Callback<Range>): void

取消订阅输入法应用按范围选中文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'selectByRange'。 |
| callback | Callback<[Range](js-apis-inputmethod.md#range10)> | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。  参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let onSelectByRangeCallback: Callback<inputMethod.Range> = (range: inputMethod.Range): void => {
4. console.info(`Succeeded in subscribing selectByRange, start: ${range.start} , end: ${range.end}`);
5. };

7. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
8. inputMethodController.off('selectByRange', onSelectByRangeCallback);
9. inputMethodController.off('selectByRange');
```

### on('selectByMovement')10+

PhonePC/2in1TabletTVWearable

on(type: 'selectByMovement', callback: Callback<Movement>): void

订阅输入法应用按光标移动方向，选中文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'selectByMovement'。 |
| callback | Callback<[Movement](js-apis-inputmethod.md#movement10)> | 是 | 回调函数，返回光标移动的方向。  根据传入的光标移动方向，选中编辑框中相应文本。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. inputMethod.getController().on('selectByMovement', (movement: inputMethod.Movement) => {
2. console.info('Succeeded in subscribing selectByMovement: direction: ' + movement.direction);
3. });
```

### off('selectByMovement')10+

PhonePC/2in1TabletTVWearable

off(type: 'selectByMovement', callback?: Callback<Movement>): void

取消订阅输入法应用按光标移动方向，选中文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'selectByMovement'。 |
| callback | Callback<[Movement](js-apis-inputmethod.md#movement10)> | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。  参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let onSelectByMovementCallback: Callback<inputMethod.Movement> = (movement: inputMethod.Movement): void => {
4. console.info(`Succeeded in subscribing selectByMovement, movement.direction: ${movement.direction}`);
5. };

7. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
8. inputMethodController.off('selectByMovement', onSelectByMovementCallback);
9. inputMethodController.off('selectByMovement');
```

### on('getLeftTextOfCursor')10+

PhonePC/2in1TabletTVWearable

on(type: 'getLeftTextOfCursor', callback: (length: number) => string): void

订阅输入法应用获取光标左侧指定长度文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'getLeftTextOfCursor'。 |
| callback | (length: number) => string | 是 | 回调函数，获取编辑框最新状态下光标左侧指定长度的文本内容并返回。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```
1. inputMethod.getController().on('getLeftTextOfCursor', (length: number) => {
2. console.info(`Succeeded in subscribing getLeftTextOfCursor, length: ${length}`);
3. let text: string = "";
4. return text;
5. });
```

### off('getLeftTextOfCursor')10+

PhonePC/2in1TabletTVWearable

off(type: 'getLeftTextOfCursor', callback?: (length: number) => string): void

取消订阅输入法应用获取光标左侧指定长度文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'getLeftTextOfCursor'。 |
| callback | (length: number) => string | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。  参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. let getLeftTextOfCursorCallback: (length: number) => string = (length: number): string => {
2. console.info(`Succeeded in unsubscribing getLeftTextOfCursor, length: ${length}`);
3. let text: string = "";
4. return text;
5. };

7. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
8. inputMethodController.off('getLeftTextOfCursor', getLeftTextOfCursorCallback);
9. inputMethodController.off('getLeftTextOfCursor');
```

### on('getRightTextOfCursor')10+

PhonePC/2in1TabletTVWearable

on(type: 'getRightTextOfCursor', callback: (length: number) => string): void

订阅输入法应用获取光标右侧指定长度文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'getRightTextOfCursor'。 |
| callback | (length: number) => string | 是 | 回调函数，获取编辑框最新状态下光标右侧指定长度的文本内容并返回。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```
1. inputMethod.getController().on('getRightTextOfCursor', (length: number) => {
2. console.info(`Succeeded in subscribing getRightTextOfCursor, length: ${length}`);
3. let text: string = "";
4. return text;
5. });
```

### off('getRightTextOfCursor')10+

PhonePC/2in1TabletTVWearable

off(type: 'getRightTextOfCursor', callback?: (length: number) => string): void

取消订阅输入法应用获取光标右侧指定长度文本事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'getRightTextOfCursor'。 |
| callback | (length: number) => string | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。  参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. let getRightTextOfCursorCallback: (length: number) => string = (length: number): string => {
2. console.info(`Succeeded in unsubscribing getRightTextOfCursor, length: ${length}`);
3. let text: string = "";
4. return text;
5. };

7. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
8. inputMethodController.off('getRightTextOfCursor', getRightTextOfCursorCallback);
9. inputMethodController.off('getRightTextOfCursor');
```

### on('getTextIndexAtCursor')10+

PhonePC/2in1TabletTVWearable

on(type: 'getTextIndexAtCursor', callback: () => number): void

订阅输入法应用获取光标处文本索引事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'getTextIndexAtCursor'。 |
| callback | () => number | 是 | 回调函数，获取编辑框最新状态下光标处文本索引并返回。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800009 | input method client detached. |

**示例：**

```
1. inputMethod.getController().on('getTextIndexAtCursor', () => {
2. console.info(`Succeeded in subscribing getTextIndexAtCursor.`);
3. let index: number = 0;
4. return index;
5. });
```

### off('getTextIndexAtCursor')10+

PhonePC/2in1TabletTVWearable

off(type: 'getTextIndexAtCursor', callback?: () => number): void

取消订阅输入法应用获取光标处文本索引事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'getTextIndexAtCursor'。 |
| callback | () => number | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。  参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. let getTextIndexAtCursorCallback: () => number = (): number => {
2. console.info(`Succeeded in unsubscribing getTextIndexAtCursor.`);
3. let index: number = 0;
4. return index;
5. };

7. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
8. inputMethodController.off('getTextIndexAtCursor', getTextIndexAtCursorCallback);
9. inputMethodController.off('getTextIndexAtCursor');
```

### on('setPreviewText')17+

PhonePC/2in1TabletTVWearable

on(type: 'setPreviewText', callback: SetPreviewTextCallback): void

订阅输入法应用操作文本预览内容的事件。使用callback异步回调。

说明

使用预览文本功能，需在调用[attach](js-apis-inputmethod.md#attach10)前订阅此事件，并和[on('finishTextPreview')](js-apis-inputmethod.md#onfinishtextpreview17)一起订阅。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'setPreviewText'。 |
| callback | [SetPreviewTextCallback](js-apis-inputmethod.md#setpreviewtextcallback17) | 是 | 回调函数。用于接收文本预览的内容并返回。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. let setPreviewTextCallback1: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
2. console.info(`SetPreviewTextCallback1: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
3. };

5. let setPreviewTextCallback2: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
6. console.info(`setPreviewTextCallback2: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
7. };

9. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
10. inputMethodController.on('setPreviewText', setPreviewTextCallback1);
11. console.info(`SetPreviewTextCallback1 subscribed to setPreviewText`);
12. inputMethodController.on('setPreviewText', setPreviewTextCallback2);
13. console.info(`SetPreviewTextCallback2 subscribed to setPreviewText`);
14. // 仅取消setPreviewText的callback1的回调。
15. inputMethodController.off('setPreviewText', setPreviewTextCallback1);
16. console.info(`SetPreviewTextCallback1 unsubscribed from setPreviewText`);
17. // 取消setPreviewText的所有回调。
18. inputMethodController.off('setPreviewText');
19. console.info(`All callbacks unsubscribed from setPreviewText`);
```

### off('setPreviewText')17+

PhonePC/2in1TabletTVWearable

off(type: 'setPreviewText', callback?: SetPreviewTextCallback): void

取消订阅输入法应用操作文本预览内容的事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'setPreviewText'。 |
| callback | [SetPreviewTextCallback](js-apis-inputmethod.md#setpreviewtextcallback17) | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。  参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. let setPreviewTextCallback1: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
2. console.info(`SetPreviewTextCallback1: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
3. };

5. let setPreviewTextCallback2: inputMethod.SetPreviewTextCallback = (text: string, range: inputMethod.Range): void => {
6. console.info(`setPreviewTextCallback2: Received text - ${text}, Received range - start: ${range.start}, end: ${range.end}`);
7. };

9. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
10. inputMethodController.on('setPreviewText', setPreviewTextCallback1);
11. console.info(`SetPreviewTextCallback1 subscribed to setPreviewText`);
12. inputMethodController.on('setPreviewText', setPreviewTextCallback2);
13. console.info(`SetPreviewTextCallback2 subscribed to setPreviewText`);
14. // 仅取消setPreviewText的callback1的回调。
15. inputMethodController.off('setPreviewText', setPreviewTextCallback1);
16. console.info(`SetPreviewTextCallback1 unsubscribed from setPreviewText`);
17. // 取消setPreviewText的所有回调。
18. inputMethodController.off('setPreviewText');
19. console.info(`All callbacks unsubscribed from setPreviewText`);
```

### on('finishTextPreview')17+

PhonePC/2in1TabletTVWearable

on(type: 'finishTextPreview', callback: Callback<void>): void

订阅结束文本预览事件。使用callback异步回调。

说明

使用预览文本功能，需在调用[attach](js-apis-inputmethod.md#attach10)前订阅此事件，并和[on('setPreviewText')](js-apis-inputmethod.md#onsetpreviewtext17)一起订阅。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'finishTextPreview'。 |
| callback | Callback<void> | 是 | 回调函数。用于处理预览文本结束的逻辑，类型为void。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let finishTextPreviewCallback1: Callback<void> = (): void => {
4. console.info(`FinishTextPreviewCallback1: finishTextPreview event triggered`);
5. };
6. let finishTextPreviewCallback2: Callback<void> = (): void => {
7. console.info(`FinishTextPreviewCallback2: finishTextPreview event triggered`);
8. };

10. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
11. inputMethodController.on('finishTextPreview', finishTextPreviewCallback1);
12. console.info(`FinishTextPreviewCallback1 subscribed to finishTextPreview`);
13. inputMethodController.on('finishTextPreview', finishTextPreviewCallback2);
14. console.info(`FinishTextPreviewCallback2 subscribed to finishTextPreview`);
15. // 仅取消finishTextPreview的callback1的回调。
16. inputMethodController.off('finishTextPreview', finishTextPreviewCallback1);
17. console.info(`FinishTextPreviewCallback1 unsubscribed from finishTextPreview`);
18. // 取消finishTextPreview的所有回调。
19. inputMethodController.off('finishTextPreview');
20. console.info(`All callbacks unsubscribed from finishTextPreview`);
```

### off('finishTextPreview')17+

PhonePC/2in1TabletTVWearable

off(type: 'finishTextPreview', callback?: Callback<void>): void

取消订阅结束文本预览事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'finishTextPreview'。 |
| callback | Callback<void> | 否 | 取消订阅的回调函数，需要与on接口传入的保持一致。  参数不填写时，取消订阅type对应的所有回调事件。 |

**示例：**

```
1. import { Callback } from '@kit.BasicServicesKit';

3. let finishTextPreviewCallback1: Callback<void> = (): void => {
4. console.info(`FinishTextPreviewCallback1: finishTextPreview event triggered`);
5. };
6. let finishTextPreviewCallback2: Callback<void> = (): void => {
7. console.info(`FinishTextPreviewCallback2: finishTextPreview event triggered`);
8. };

10. let inputMethodController: inputMethod.InputMethodController = inputMethod.getController();
11. inputMethodController.on('finishTextPreview', finishTextPreviewCallback1);
12. console.info(`FinishTextPreviewCallback1 subscribed to finishTextPreview`);
13. inputMethodController.on('finishTextPreview', finishTextPreviewCallback2);
14. console.info(`FinishTextPreviewCallback2 subscribed to finishTextPreview`);
15. // 仅取消finishTextPreview的callback1的回调。
16. inputMethodController.off('finishTextPreview', finishTextPreviewCallback1);
17. console.info(`FinishTextPreviewCallback1 unsubscribed from finishTextPreview`);
18. // 取消finishTextPreview的所有回调。
19. inputMethodController.off('finishTextPreview');
20. console.info(`All callbacks unsubscribed from finishTextPreview`);
```

## InputMethodSetting8+

PhonePC/2in1TabletTVWearable

下列API均需使用[getSetting](js-apis-inputmethod.md#inputmethodgetsetting9)获取到InputMethodSetting实例后，通过实例调用。

### on('imeChange')9+

PhonePC/2in1TabletTVWearable

on(type: 'imeChange', callback: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void): void

订阅输入法及子类型变化监听事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'imeChange'。 |
| callback | (inputMethodProperty: [InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8), inputMethodSubtype: [InputMethodSubtype](js-apis-inputmethod-subtype.md#inputmethodsubtype)) => void | 是 | 回调函数，返回输入法属性对象及子类型对象。 |

**示例：**

```
1. import { InputMethodSubtype } from '@kit.IMEKit';

3. inputMethod.getSetting()
4. .on('imeChange', (inputMethodProperty: inputMethod.InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => {
5. console.info(`Succeeded in subscribing imeChange: inputMethodProperty.name: ${inputMethodProperty.name} ` +
6. `, inputMethodSubtype.id: ${inputMethodSubtype.id}`);
7. });
```

### off('imeChange')9+

PhonePC/2in1TabletTVWearable

off(type: 'imeChange', callback?: (inputMethodProperty: InputMethodProperty, inputMethodSubtype: InputMethodSubtype) => void): void

取消订阅输入法及子类型变化监听事件。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 设置监听类型，固定取值为'imeChange'。 |
| callback | (inputMethodProperty: [InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8), inputMethodSubtype: [InputMethodSubtype](js-apis-inputmethod-subtype.md#inputmethodsubtype)) => void | 否 | 回调函数，返回取消订阅的输入法属性对象及子类型对象。 |

**示例：**

```
1. inputMethod.getSetting().off('imeChange');
```

### listInputMethodSubtype9+

PhonePC/2in1TabletTVWearable

listInputMethodSubtype(inputMethodProperty: InputMethodProperty, callback: AsyncCallback<Array<InputMethodSubtype>>): void

获取指定输入法应用的所有子类型。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputMethodProperty | [InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8) | 是 | 输入法应用。 |
| callback | AsyncCallback<Array<[InputMethodSubtype](js-apis-inputmethod-subtype.md#inputmethodsubtype)>> | 是 | 回调函数，返回指定输入法应用的所有子类型。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { InputMethodSubtype } from '@kit.IMEKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let inputMethodProperty: inputMethod.InputMethodProperty = {
5. name: 'com.example.keyboard',
6. id: 'propertyId',
7. packageName: 'com.example.keyboard',
8. methodId: 'propertyId',
9. }
10. let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();

12. inputMethodSetting.listInputMethodSubtype(inputMethodProperty,
13. (err: BusinessError, data: Array<InputMethodSubtype>) => {
14. if (err) {
15. console.error(`Failed to listInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
16. return;
17. }
18. console.info('Succeeded in listing inputMethodSubtype.');
19. });
```

### listInputMethodSubtype9+

PhonePC/2in1TabletTVWearable

listInputMethodSubtype(inputMethodProperty: InputMethodProperty): Promise<Array<InputMethodSubtype>>

获取指定输入法应用的所有子类型。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| inputMethodProperty | [InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8) | 是 | 输入法应用。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[InputMethodSubtype](js-apis-inputmethod-subtype.md#inputmethodsubtype)>> | Promise对象，返回指定输入法应用的所有子类型。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { InputMethodSubtype } from '@kit.IMEKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let inputMethodProperty: inputMethod.InputMethodProperty = {
5. name: 'com.example.keyboard',
6. id: 'propertyId',
7. packageName: 'com.example.keyboard',
8. methodId: 'propertyId',
9. }
10. let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();

12. inputMethodSetting.listInputMethodSubtype(inputMethodProperty).then((data: Array<InputMethodSubtype>) => {
13. console.info('Succeeded in listing inputMethodSubtype.');
14. }).catch((err: BusinessError) => {
15. console.error(`Failed to listInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
16. })
```

### listCurrentInputMethodSubtype9+

PhonePC/2in1TabletTVWearable

listCurrentInputMethodSubtype(callback: AsyncCallback<Array<InputMethodSubtype>>): void

查询当前输入法应用的所有子类型。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[InputMethodSubtype](js-apis-inputmethod-subtype.md#inputmethodsubtype)>> | 是 | 回调函数，返回当前输入法应用的所有子类型。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { InputMethodSubtype } from '@kit.IMEKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();
5. inputMethodSetting.listCurrentInputMethodSubtype((err: BusinessError, data: Array<InputMethodSubtype>) => {
6. if (err) {
7. console.error(`Failed to listCurrentInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
8. return;
9. }
10. console.info('Succeeded in listing currentInputMethodSubtype.');
11. });
```

### listCurrentInputMethodSubtype9+

PhonePC/2in1TabletTVWearable

listCurrentInputMethodSubtype(): Promise<Array<InputMethodSubtype>>

查询当前输入法应用的所有子类型。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[InputMethodSubtype](js-apis-inputmethod-subtype.md#inputmethodsubtype)>> | Promise对象，返回当前输入法应用的所有子类型。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { InputMethodSubtype } from '@kit.IMEKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let inputMethodSetting: inputMethod.InputMethodSetting = inputMethod.getSetting();

6. inputMethodSetting.listCurrentInputMethodSubtype().then((data: Array<InputMethodSubtype>) => {
7. console.info('Succeeded in listing currentInputMethodSubtype.');
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to listCurrentInputMethodSubtype, code: ${err.code}, message: ${err.message}`);
10. })
```

### getInputMethods9+

PhonePC/2in1TabletTVWearable

getInputMethods(enable: boolean, callback: AsyncCallback<Array<InputMethodProperty>>): void

获取已激活/未激活的输入法应用列表。使用callback异步回调。

说明

已激活输入法为使能的输入法应用。默认输入法默认使能，其他输入法可被设置为使能或非使能。

已激活输入法列表包括默认输入法和已被设置为使能的输入法应用，未激活输入法列表包括除使能输入法以外的其他已安装的输入法。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | true表示返回已激活输入法列表，false表示返回未激活输入法列表。 |
| callback | AsyncCallback<Array<[InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8)>> | 是 | 回调函数，返回已激活/未激活输入法列表。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getSetting().getInputMethods(true, (err: BusinessError, data: Array<inputMethod.InputMethodProperty>) => {
4. if (err) {
5. console.error(`Failed to getInputMethods, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in getting inputMethods.');
9. });
```

### getInputMethods9+

PhonePC/2in1TabletTVWearable

getInputMethods(enable: boolean): Promise<Array<InputMethodProperty>>

获取已激活/未激活的输入法应用列表。使用promise异步回调。

说明

已激活输入法为使能的输入法应用。默认输入法默认使能，其他输入法可被设置为使能或非使能。

已激活输入法列表包括默认输入法和已被设置为使能的输入法应用，未激活输入法列表包括除使能输入法以外的其他已安装的输入法。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | - true表示返回已激活输入法列表，false表示返回未激活输入法列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8)>> | Promise对象，返回已激活/未激活输入法列表。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getSetting().getInputMethods(true).then((data: Array<inputMethod.InputMethodProperty>) => {
4. console.info('Succeeded in getting inputMethods.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to getInputMethods, code: ${err.code}, message: ${err.message}`);
7. })
```

### getInputMethodsSync11+

PhonePC/2in1TabletTVWearable

getInputMethodsSync(enable: boolean): Array<InputMethodProperty>

获取已激活/未激活的输入法应用列表。同步接口。

说明

已激活输入法为使能的输入法应用。默认输入法默认使能，其他输入法可被设置为使能或非使能。

已激活输入法列表包括默认输入法和已被设置为使能的输入法应用，未激活输入法列表包括除使能输入法以外的其他已安装的输入法。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enable | boolean | 是 | - true表示返回已激活输入法列表，false表示返回未激活输入法列表。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8)> | 返回已激活/未激活输入法列表。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. let imeProperty: Array<inputMethod.InputMethodProperty> = inputMethod.getSetting().getInputMethodsSync(true);
```

### getAllInputMethods11+

PhonePC/2in1TabletTVWearable

getAllInputMethods(callback: AsyncCallback<Array<InputMethodProperty>>): void

获取所有输入法应用列表。使用callback异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8)>> | 是 | 回调函数，返回所有输入法列表。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getSetting().getAllInputMethods((err: BusinessError, data: Array<inputMethod.InputMethodProperty>) => {
4. if (err) {
5. console.error(`Failed to getAllInputMethods, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in getting all inputMethods.');
9. });
```

### getAllInputMethods11+

PhonePC/2in1TabletTVWearable

getAllInputMethods(): Promise<Array<InputMethodProperty>>

获取所有输入法应用列表。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8)>> | Promise对象，返回所有输入法列表。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)，[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getSetting().getAllInputMethods().then((data: Array<inputMethod.InputMethodProperty>) => {
4. console.info('Succeeded in getting all inputMethods.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to getAllInputMethods, code: ${err.code}, message: ${err.message}`);
7. })
```

### getAllInputMethodsSync11+

PhonePC/2in1TabletTVWearable

getAllInputMethodsSync(): Array<InputMethodProperty>

获取所有输入法应用列表。同步接口。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<[InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8)> | 返回所有输入法列表 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800001 | bundle manager error. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. let imeProperty: Array<inputMethod.InputMethodProperty> = inputMethod.getSetting().getAllInputMethodsSync();
```

### showOptionalInputMethods(deprecated)

PhonePC/2in1TabletTVWearable

showOptionalInputMethods(callback: AsyncCallback<boolean>): void

显示输入法选择对话框。使用callback异步回调。

说明

从API version 9开始支持，从API version 18开始废弃，建议使用[InputMethodListDialog](js-apis-inputmethodlist.md#inputmethodlistdialog)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数。当输入法选择对话框显示成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getSetting().showOptionalInputMethods((err: BusinessError, result: boolean) => {
4. if (err) {
5. console.error(`Failed to showOptionalInputMethods, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. if (result) {
9. console.info('Succeeded in showing optionalInputMethods.');
10. } else {
11. console.error(`Failed to showOptionalInputMethods.`);
12. }
13. });
```

### showOptionalInputMethods(deprecated)

PhonePC/2in1TabletTVWearable

showOptionalInputMethods(): Promise<boolean>

显示输入法选择对话框。使用promise异步回调。

说明

从API version 9开始支持，从API version 18开始废弃，建议使用[InputMethodListDialog](js-apis-inputmethodlist.md#inputmethodlistdialog)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。当输入法选择对话框显示成功，err为undefined，data为true；否则为错误对象。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getSetting().showOptionalInputMethods().then((result: boolean) => {
4. if (result) {
5. console.info('Succeeded in showing optionalInputMethods.');
6. } else {
7. console.error(`Failed to showOptionalInputMethods.`);
8. }
9. }).catch((err: BusinessError) => {
10. console.error(`Failed to showOptionalInputMethods, code: ${err.code}, message: ${err.message}`);
11. })
```

### listInputMethod(deprecated)

PhonePC/2in1TabletTVWearable

listInputMethod(callback: AsyncCallback<Array<InputMethodProperty>>): void

查询已安装的输入法列表。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getInputMethods](js-apis-inputmethod.md#getinputmethods9)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<Array<[InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8)>> | 是 | 回调函数，返回已安装的输入法列表。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getSetting().listInputMethod((err: BusinessError, data: Array<inputMethod.InputMethodProperty>) => {
4. if (err) {
5. console.error(`Failed to listInputMethod, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in listing inputMethod.');
9. });
```

### listInputMethod(deprecated)

PhonePC/2in1TabletTVWearable

listInputMethod(): Promise<Array<InputMethodProperty>>

查询已安装的输入法列表。使用promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getInputMethods](js-apis-inputmethod.md#getinputmethods9-1)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[InputMethodProperty](js-apis-inputmethod.md#inputmethodproperty8)>> | Promise对象，返回已安装输入法列表。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getSetting().listInputMethod().then((data: Array<inputMethod.InputMethodProperty>) => {
4. console.info('Succeeded in listing inputMethod.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to listInputMethod, code: ${err.code}, message: ${err.message}`);
7. })
```

### displayOptionalInputMethod(deprecated)

PhonePC/2in1TabletTVWearable

displayOptionalInputMethod(callback: AsyncCallback<void>): void

显示输入法选择对话框。使用callback异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[InputMethodListDialog](js-apis-inputmethodlist.md#inputmethodlistdialog)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当输入法选择对话框显示成功。err为undefined，否则为错误对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getSetting().displayOptionalInputMethod((err: BusinessError) => {
4. if (err) {
5. console.error(`Failed to displayOptionalInputMethod, code: ${err.code}, message: ${err.message}`);
6. return;
7. }
8. console.info('Succeeded in displaying optionalInputMethod.');
9. });
```

### displayOptionalInputMethod(deprecated)

PhonePC/2in1TabletTVWearable

displayOptionalInputMethod(): Promise<void>

显示输入法选择对话框。使用promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[InputMethodListDialog](js-apis-inputmethodlist.md#inputmethodlistdialog)替代。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | 无返回结果的Promise对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getSetting().displayOptionalInputMethod().then(() => {
4. console.info('Succeeded in displaying optionalInputMethod.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to displayOptionalInputMethod, code: ${err.code}, message: ${err.message}`);
7. })
```

### getInputMethodState15+

PhonePC/2in1TabletTVWearable

getInputMethodState(): Promise<EnabledState>

查询输入法的启用状态。使用promise异步回调。

**系统能力：** SystemCapability.MiscServices.InputMethodFramework

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[EnabledState](js-apis-inputmethod.md#enabledstate15)> | Promise对象，返回EnabledState.DISABLED表示未启用; 返回EnabledState.BASIC\_MODE表示基础模式; 返回EnabledState.FULL\_EXPERIENCE\_MODE表示完整体验模式。 |

**错误码：**

以下错误码的详细介绍请参见[输入法框架错误码](errorcode-inputmethod-framework.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 12800004 | not an input method application. |
| 12800008 | input method manager service error. Possible cause: a system error, such as null pointer, IPC exception. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. inputMethod.getSetting().getInputMethodState().then((status: inputMethod.EnabledState) => {
4. console.info(`Succeeded in getInputMethodState, status: ${status}`);
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to getInputMethodState, code: ${err.code}, message: ${err.message}`);
7. })
```
