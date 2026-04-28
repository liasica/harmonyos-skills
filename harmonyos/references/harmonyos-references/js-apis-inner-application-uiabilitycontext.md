---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiabilitycontext
title: UIAbilityContext
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > UIAbilityContext
category: harmonyos-references
scraped_at: 2026-04-28T07:58:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0e17b462fa8c3866a1491504c0070195f22ba78685de62839a90411ee043b567
---

UIAbilityContext是[UIAbility](js-apis-app-ability-uiability.md)组件的上下文，继承自[Context](js-apis-inner-application-context.md)。各类Context之间的关联与差异详见[应用上下文Context](../harmonyos-guides/application-context-stage.md)。

每个UIAbility组件实例化时，系统都会自动创建对应的UIAbilityContext。开发者可以通过UIAbilityContext获取组件信息AbilityInfo、获取应用信息ApplicationInfo、拉起其他UIAbility、连接系统服务、销毁UIAbility等。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 在本文档的示例中，通过this.context来获取UIAbilityContext，其中this代表继承自UIAbility的实例。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## UIAbilityContext

PhonePC/2in1TabletTVWearable

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| abilityInfo | [AbilityInfo](js-apis-bundlemanager-abilityinfo.md) | 否 | 否 | UIAbility的相关信息。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| currentHapModuleInfo | [HapModuleInfo](js-apis-bundlemanager-hapmoduleinfo.md) | 否 | 否 | 当前UIAbility所属HAP的信息。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| config | [Configuration](js-apis-app-ability-configuration.md) | 否 | 否 | 应用运行时的环境变量，如语言、颜色模式等。  **元服务API**：从API version 11开始，该接口支持在元服务中使用。 |
| windowStage12+ | [window.WindowStage](arkts-apis-window-windowstage.md) | 否 | 否 | 当前WindowStage对象。仅支持在主线程调用。  **元服务API**：从API version 12开始，该接口支持在元服务中使用。 |

### startAbility

PhonePC/2in1TabletTVWearable

startAbility(want: Want, callback: AsyncCallback<void>): void

启动一个UIAbility。使用callback异步回调。仅支持在主线程调用。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UIAbility的必要信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当接口调用成功，err中code为0，message为空字符串；否则err会返回对应的错误码和错误信息。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let want: Want = {
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EntryAbility'
9. };

11. try {
12. this.context.startAbility(want, (err: BusinessError) => {
13. if (err.code) {
14. // 处理业务逻辑错误
15. console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
16. return;
17. }
18. // 执行正常业务
19. console.info('startAbility succeed');
20. });
21. } catch (err) {
22. // 处理入参错误异常
23. let code = (err as BusinessError).code;
24. let message = (err as BusinessError).message;
25. console.error(`startAbility failed, code is ${code}, message is ${message}`);
26. }
27. }
28. }
```

### startAbility

PhonePC/2in1TabletTVWearable

startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void

启动一个UIAbility。使用callback异步回调。仅支持在主线程调用。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UIAbility的必要信息。 |
| options | [StartOptions](js-apis-app-ability-startoptions.md) | 是 | 启动UIAbility所携带的参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当接口调用成功，err中code为0，message为空字符串；否则err会返回对应的错误码和错误信息。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not support. |
| 16000001 | The specified ability does not exist. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000067 | The StartOptions check failed. |
| 16000068 | The ability is already running. |
| 16300003 | The target application is not the current application. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { UIAbility, Want, StartOptions } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let want: Want = {
7. deviceId: '',
8. bundleName: 'com.example.myapplication',
9. abilityName: 'EntryAbility'
10. };
11. let options: StartOptions = {
12. displayId: 0
13. };

15. try {
16. this.context.startAbility(want, options, (err: BusinessError) => {
17. if (err.code) {
18. // 处理业务逻辑错误
19. console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
20. return;
21. }
22. // 执行正常业务
23. console.info('startAbility succeed');
24. });
25. } catch (err) {
26. // 处理入参错误异常
27. let code = (err as BusinessError).code;
28. let message = (err as BusinessError).message;
29. console.error(`startAbility failed, code is ${code}, message is ${message}`);
30. }
31. }
32. }
```

### startAbility

PhonePC/2in1TabletTVWearable

startAbility(want: Want, options?: StartOptions): Promise<void>

启动一个UIAbility。使用Promise异步回调。仅支持在主线程调用。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UIAbility的必要信息。 |
| options | [StartOptions](js-apis-app-ability-startoptions.md) | 否 | 启动UIAbility所携带的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not support. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000067 | The StartOptions check failed. |
| 16000068 | The ability is already running. |
| 16300003 | The target application is not the current application. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { UIAbility, Want, StartOptions } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let want: Want = {
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EntryAbility'
9. };
10. let options: StartOptions = {
11. displayId: 0
12. };

14. try {
15. this.context.startAbility(want, options)
16. .then(() => {
17. // 执行正常业务
18. console.info('startAbility succeed');
19. })
20. .catch((err: BusinessError) => {
21. // 处理业务逻辑错误
22. console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
23. });
24. } catch (err) {
25. // 处理入参错误异常
26. let code = (err as BusinessError).code;
27. let message = (err as BusinessError).message;
28. console.error(`startAbility failed, code is ${code}, message is ${message}`);
29. }
30. }
31. }
```

### startAbilityForResult

PhonePC/2in1TabletTVWearable

startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void

启动一个UIAbility，并通过回调函数接收被拉起的UIAbility退出时的返回结果。使用callback异步回调。仅支持在主线程调用。

UIAbility被启动后，有如下情况：

* 正常情况下可以通过调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口销毁自身，并将结果返回给调用方。
* 异常情况下比如杀死UIAbility会将异常结果返回给调用方，异常结果中resultCode为-1。
* 如果被启动的UIAbility是[单实例模式](../harmonyos-guides/uiability-launch-type.md#singleton启动模式)，且这个UIAbility被不同应用多次调用该接口启动，当这个UIAbility调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口销毁自身时，只将正常结果返回给最后一个调用方，其它调用方返回异常结果，异常结果中resultCode为-1。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动Ability的必要信息。 |
| callback | AsyncCallback<[AbilityResult](js-apis-inner-ability-abilityresult.md)> | 是 | 回调函数，当接口调用成功，err中code为0，data为被拉起方退出时的结果码和数据；否则err会返回对应的错误码和错误信息。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { UIAbility, Want, common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let want: Want = {
7. deviceId: '',
8. bundleName: 'com.example.myapplication',
9. abilityName: 'EntryAbility'
10. };

12. try {
13. this.context.startAbilityForResult(want, (err: BusinessError, result: common.AbilityResult) => {
14. if (err.code) {
15. // 处理业务逻辑错误
16. console.error(`startAbilityForResult failed, code is ${err.code}, message is ${err.message}`);
17. return;
18. }
19. // 执行正常业务
20. console.info('startAbilityForResult succeed');
21. });
22. } catch (err) {
23. // 处理入参错误异常
24. let code = (err as BusinessError).code;
25. let message = (err as BusinessError).message;
26. console.error(`startAbilityForResult failed, code is ${code}, message is ${message}`);
27. }
28. }
29. }
```

### startAbilityForResult

PhonePC/2in1TabletTVWearable

startAbilityForResult(want: Want, options: StartOptions, callback: AsyncCallback<AbilityResult>): void

启动一个UIAbility，并通过回调函数接收被拉起的UIAbility退出时的返回结果。使用callback异步回调。仅支持在主线程调用。

UIAbility被启动后，有如下情况：

* 正常情况下可以通过调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口销毁自身，并将结果返回给调用方。
* 异常情况下比如杀死UIAbility会将异常结果返回给调用方，异常结果中resultCode为-1。
* 如果被启动的UIAbility是[单实例模式](../harmonyos-guides/uiability-launch-type.md#singleton启动模式)，且这个UIAbility被不同应用多次调用该接口启动，当这个UIAbility调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口销毁自身时，只将正常结果返回给最后一个调用方，其它调用方返回异常结果，异常结果中resultCode为-1。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动Ability的必要信息。 |
| options | [StartOptions](js-apis-app-ability-startoptions.md) | 是 | 启动Ability所携带的参数。 |
| callback | AsyncCallback<[AbilityResult](js-apis-inner-ability-abilityresult.md)> | 是 | 回调函数，当接口调用成功，err中code为0，data为被拉起方退出时的结果码和数据；否则err会返回对应的错误码和错误信息。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { UIAbility, Want, common, StartOptions } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let want: Want = {
7. deviceId: '',
8. bundleName: 'com.example.myapplication',
9. abilityName: 'EntryAbility'
10. };
11. let options: StartOptions = {
12. displayId: 0
13. };

15. try {
16. this.context.startAbilityForResult(want, options, (err: BusinessError, result: common.AbilityResult) => {
17. if (err.code) {
18. // 处理业务逻辑错误
19. console.error(`startAbilityForResult failed, code is ${err.code}, message is ${err.message}`);
20. return;
21. }
22. // 执行正常业务
23. console.info('startAbilityForResult succeed');
24. });
25. } catch (err) {
26. // 处理入参错误异常
27. let code = (err as BusinessError).code;
28. let message = (err as BusinessError).message;
29. console.error(`startAbilityForResult failed, code is ${code}, message is ${message}`);
30. }
31. }
32. }
```

### startAbilityForResult

PhonePC/2in1TabletTVWearable

startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>

启动一个UIAbility，并通过回调函数接收被拉起的UIAbility退出时的返回结果。使用Promise异步回调。仅支持在主线程调用。

UIAbility被启动后，有如下情况：

* 正常情况下可以通过调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口销毁自身，并将结果返回给调用方。
* 异常情况下比如杀死UIAbility会将异常结果返回给调用方，异常结果中resultCode为-1。
* 如果被启动的UIAbility是[单实例模式](../harmonyos-guides/uiability-launch-type.md#singleton启动模式)，且这个UIAbility被不同应用多次调用该接口启动，当这个UIAbility调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口销毁自身时，只将正常结果返回给最后一个调用方，其它调用方返回异常结果，异常结果中resultCode为-1。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动Ability的必要信息。 |
| options | [StartOptions](js-apis-app-ability-startoptions.md) | 否 | 启动Ability所携带的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AbilityResult](js-apis-inner-ability-abilityresult.md)> | Promise对象，包含返回给拉起方的信息。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { UIAbility, Want, common, StartOptions } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let want: Want = {
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EntryAbility'
9. };
10. let options: StartOptions = {
11. displayId: 0
12. };

14. try {
15. this.context.startAbilityForResult(want, options)
16. .then((result: common.AbilityResult) => {
17. // 执行正常业务
18. console.info('startAbilityForResult succeed');
19. })
20. .catch((err: BusinessError) => {
21. // 处理业务逻辑错误
22. console.error(`startAbilityForResult failed, code is ${err.code}, message is ${err.message}`);
23. });
24. } catch (err) {
25. // 处理入参错误异常
26. let code = (err as BusinessError).code;
27. let message = (err as BusinessError).message;
28. console.error(`startAbilityForResult failed, code is ${code}, message is ${message}`);
29. }
30. }
31. }
```

### terminateSelf

PhonePC/2in1TabletTVWearable

terminateSelf(callback: AsyncCallback<void>): void

销毁UIAbility自身。使用callback异步回调。仅支持在主线程调用。

说明

调用该接口后，任务中心的任务默认不会清理，如需清理，需要配置[removeMissionAfterTerminate](../harmonyos-guides/module-configuration-file.md#abilities标签)为true。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数，当销毁UIAbility自身成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

1. 使用terminateSelf接口停止UIAbility示例代码如下，默认情况下应用会在最近任务列表中保留快照。

   ```
   1. import { UIAbility } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. export default class EntryAbility extends UIAbility {
   5. onForeground() {
   6. try {
   7. this.context.terminateSelf((err: BusinessError) => {
   8. if (err.code) {
   9. // 处理业务逻辑错误
   10. console.error(`terminateSelf failed, code is ${err.code}, message is ${err.message}`);
   11. return;
   12. }
   13. // 执行正常业务
   14. console.info('terminateSelf succeed');
   15. });
   16. } catch (err) {
   17. // 捕获同步的参数错误
   18. let code = (err as BusinessError).code;
   19. let message = (err as BusinessError).message;
   20. console.error(`terminateSelf failed, code is ${code}, message is ${message}`);
   21. }
   22. }
   23. }
   ```
2. （可选）如果需要在停止UIAbility时，清理任务中心的相关任务（即不保留最近任务列表中的快照），需要在[module.json5](../harmonyos-guides/module-configuration-file.md)配置文件中将removeMissionAfterTerminate字段取值配置为true。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "abilities": [
   5. {
   6. // ...
   7. "removeMissionAfterTerminate": true
   8. }
   9. ]
   10. }
   11. }
   ```

### terminateSelf

PhonePC/2in1TabletTVWearable

terminateSelf(): Promise<void>

销毁UIAbility自身。使用Promise异步回调。仅支持在主线程调用。

说明

调用该接口后，任务中心的任务默认不会清理，如需清理，需要配置[removeMissionAfterTerminate](../harmonyos-guides/module-configuration-file.md#abilities标签)为true。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

1. 使用terminateSelf接口停止UIAbility示例代码如下，默认情况下应用会在最近任务列表中保留快照。

   ```
   1. import { UIAbility } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. export default class EntryAbility extends UIAbility {
   5. onForeground() {
   6. try {
   7. this.context.terminateSelf()
   8. .then(() => {
   9. // 执行正常业务
   10. console.info('terminateSelf succeed');
   11. })
   12. .catch((err: BusinessError) => {
   13. // 处理业务逻辑错误
   14. console.error(`terminateSelf failed, code is ${err.code}, message is ${err.message}`);
   15. });
   16. } catch (err) {
   17. // 捕获同步的参数错误
   18. let code = (err as BusinessError).code;
   19. let message = (err as BusinessError).message;
   20. console.error(`terminateSelf failed, code is ${code}, message is ${message}`);
   21. }
   22. }
   23. }
   ```
2. （可选）如果需要在停止UIAbility时，清理任务中心的相关任务（即不保留最近任务列表中的快照），需要在[module.json5](../harmonyos-guides/module-configuration-file.md)配置文件中将removeMissionAfterTerminate字段取值配置为true。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "abilities": [
   5. {
   6. // ...
   7. "removeMissionAfterTerminate": true
   8. }
   9. ]
   10. }
   11. }
   ```

### terminateSelfWithResult

PhonePC/2in1TabletTVWearable

terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void

销毁UIAbility自身。使用callback异步回调。仅支持在主线程调用。

仅当UIAbility通过[startAbilityForResult](js-apis-inner-application-uiabilitycontext.md#startabilityforresult)接口拉起时，调用terminateSelfWithResult接口销毁UIAbility，才会返回结果给调用方。

说明

调用该接口后，任务中心的任务默认不会清理，如需清理，需要配置[removeMissionAfterTerminate](../harmonyos-guides/module-configuration-file.md#abilities标签)为true。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [AbilityResult](js-apis-inner-ability-abilityresult.md) | 是 | 返回给startAbilityForResult 接口调用方的相关信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当销毁UIAbility自身成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility, Want, common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let want: Want = {
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EntryAbility'
9. };
10. let resultCode = 100;
11. // 返回给接口调用方AbilityResult信息
12. let abilityResult: common.AbilityResult = {
13. want,
14. resultCode
15. };

17. try {
18. this.context.terminateSelfWithResult(abilityResult, (err: BusinessError) => {
19. if (err.code) {
20. // 处理业务逻辑错误
21. console.error(`terminateSelfWithResult failed, code is ${err.code}, message is ${err.message}`);
22. return;
23. }
24. // 执行正常业务
25. console.info('terminateSelfWithResult succeed');
26. });
27. } catch (err) {
28. // 处理入参错误异常
29. let code = (err as BusinessError).code;
30. let message = (err as BusinessError).message;
31. console.error(`terminateSelfWithResult failed, code is ${code}, message is ${message}`);
32. }
33. }
34. }
```

### terminateSelfWithResult

PhonePC/2in1TabletTVWearable

terminateSelfWithResult(parameter: AbilityResult): Promise<void>

销毁UIAbility自身。使用Promise异步回调。仅支持在主线程调用。

仅当UIAbility通过[startAbilityForResult](js-apis-inner-application-uiabilitycontext.md#startabilityforresult)接口拉起时，调用terminateSelfWithResult接口销毁UIAbility，才会返回结果给调用方。

说明

调用该接口后，任务中心的任务默认不会清理，如需清理，需要配置[removeMissionAfterTerminate](../harmonyos-guides/module-configuration-file.md#abilities标签)为true。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [AbilityResult](js-apis-inner-ability-abilityresult.md) | 是 | 返回给startAbilityForResult 接口调用方的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility, Want, common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let want: Want = {
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EntryAbility'
9. };
10. let resultCode = 100;
11. // 返回给接口调用方AbilityResult信息
12. let abilityResult: common.AbilityResult = {
13. want,
14. resultCode
15. };

17. try {
18. this.context.terminateSelfWithResult(abilityResult)
19. .then(() => {
20. // 执行正常业务
21. console.info('terminateSelfWithResult succeed');
22. })
23. .catch((err: BusinessError) => {
24. // 处理业务逻辑错误
25. console.error(`terminateSelfWithResult failed, code is ${err.code}, message is ${err.message}`);
26. });
27. } catch (err) {
28. // 处理入参错误异常
29. let code = (err as BusinessError).code;
30. let message = (err as BusinessError).message;
31. console.error(`terminateSelfWithResult failed, code is ${code}, message is ${message}`);
32. }
33. }
34. }
```

### connectServiceExtensionAbility

PhonePC/2in1TabletTVWearable

connectServiceExtensionAbility(want: Want, options: ConnectOptions): number

将当前UIAbility连接到一个[ServiceExtensionAbility](../harmonyos-guides/extensionability-overview.md)，通过返回的proxy与ServiceExtensionAbility进行通信，以使用ServiceExtensionAbility对外提供的能力。仅支持在主线程调用。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 连接ServiceExtensionAbility的Want信息。 |
| options | [ConnectOptions](js-apis-inner-ability-connectoptions.md) | 是 | 回调对象，返回服务连接成功、连接失败、断开的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回连接id，调用方可以通过[disconnectServiceExtensionAbility](js-apis-inner-application-uiabilitycontext.md#disconnectserviceextensionability)传入该连接id来断开连接。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |

**示例：**

```
1. import { UIAbility, Want, common } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onForeground() {
7. let want: Want = {
8. deviceId: '',
9. bundleName: 'com.example.myapplication',
10. abilityName: 'ServiceExtensionAbility'
11. };
12. let commRemote: rpc.IRemoteObject;
13. let options: common.ConnectOptions = {
14. onConnect(elementName, remote) {
15. commRemote = remote;
16. console.info('onConnect...');
17. },
18. onDisconnect(elementName) {
19. console.info('onDisconnect...');
20. },
21. onFailed(code) {
22. console.info('onFailed...');
23. }
24. };
25. let connection: number;

27. try {
28. connection = this.context.connectServiceExtensionAbility(want, options);
29. } catch (err) {
30. // 处理入参错误异常
31. let code = (err as BusinessError).code;
32. let message = (err as BusinessError).message;
33. console.error(`connectServiceExtensionAbility failed, code is ${code}, message is ${message}`);
34. }
35. }
36. }
```

### disconnectServiceExtensionAbility

PhonePC/2in1TabletTVWearable

disconnectServiceExtensionAbility(connection: number): Promise<void>

断开与[ServiceExtensionAbility](../harmonyos-guides/extensionability-overview.md)的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用Promise异步回调。仅支持在主线程调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 连接的ServiceExtensionAbility的标识id，即[connectServiceExtensionAbility](js-apis-inner-application-uiabilitycontext.md#connectserviceextensionability)返回的connectionId。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onForeground() {
7. // connection为connectServiceExtensionAbility中的返回值
8. let connection = 1;
9. let commRemote: rpc.IRemoteObject | null;

11. try {
12. this.context.disconnectServiceExtensionAbility(connection).then(() => {
13. commRemote = null;
14. // 执行正常业务
15. console.info('disconnectServiceExtensionAbility succeed');
16. }).catch((err: BusinessError) => {
17. // 处理业务逻辑错误
18. console.error(`disconnectServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}`);
19. });
20. } catch (err) {
21. commRemote = null;
22. // 处理入参错误异常
23. let code = (err as BusinessError).code;
24. let message = (err as BusinessError).message;
25. console.error(`disconnectServiceExtensionAbility failed, code is ${code}, message is ${message}`);
26. }
27. }
28. }
```

### disconnectServiceExtensionAbility

PhonePC/2in1TabletTVWearable

disconnectServiceExtensionAbility(connection: number, callback: AsyncCallback<void>): void

断开与[ServiceExtensionAbility](../harmonyos-guides/extensionability-overview.md)的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用callback异步回调。仅支持在主线程调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 连接的ServiceExtensionAbility的标识id，即[connectServiceExtensionAbility](js-apis-inner-application-uiabilitycontext.md#connectserviceextensionability)返回的connectionId。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当断开与ServiceExtensionAbility的连接成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onForeground() {
7. // connection为connectServiceExtensionAbility中的返回值
8. let connection = 1;
9. let commRemote: rpc.IRemoteObject | null;

11. try {
12. this.context.disconnectServiceExtensionAbility(connection, (err: BusinessError) => {
13. commRemote = null;
14. if (err.code) {
15. // 处理业务逻辑错误
16. console.error(`disconnectServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}`);
17. return;
18. }
19. // 执行正常业务
20. console.info('disconnectServiceExtensionAbility succeed');
21. });
22. } catch (err) {
23. commRemote = null;
24. // 处理入参错误异常
25. let code = (err as BusinessError).code;
26. let message = (err as BusinessError).message;
27. console.error(`disconnectServiceExtensionAbility failed, code is ${code}, message is ${message}`);
28. }
29. }
30. }
```

### startAbilityByCall

PhonePC/2in1TabletTVWearable

startAbilityByCall(want: Want): Promise<Caller>

该接口用于获取[Caller](js-apis-app-ability-uiability.md#caller)通信对象，以便于与[Callee](js-apis-app-ability-uiability.md#callee)进行通信。如果指定UIAbility未启动，则会将UIAbility启动至前台或后台。使用Promise异步回调。仅支持在主线程调用。

该接口不支持拉起启动模式为[specified模式](../harmonyos-guides/uiability-launch-type.md#specified启动模式)的UIAbility。

说明

* 跨设备场景下，调用方与目标方必须为同一应用。
* 同设备场景下，要求调用方与目标方为不同应用，且调用方具备ohos.permission.ABILITY\_BACKGROUND\_COMMUNICATION权限（该权限仅系统应用可申请）。
* 此外如果应用需要在后台调用该接口，需要具备ohos.permission.START\_ABILITIES\_FROM\_BACKGROUND（该权限仅系统应用可申请）。更多的组件启动规则详见[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**需要权限**：ohos.permission.DISTRIBUTED\_DATASYNC

说明

* API version 10及之前版本，需申请ohos.permission.ABILITY\_BACKGROUND\_COMMUNICATION（该权限仅系统应用可用）。
* API version 11开始，仅需申请ohos.permission.DISTRIBUTED\_DATASYNC（该权限仅当执行应用间建链操作时由软总线实施权限校验，在应用拉起阶段不做校验）。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 传入需要启动的UIAbility信息，包含abilityName、moduleName、bundleName、deviceId、parameters（可选）。将parameters中的'ohos.aafwk.param.callAbilityToForeground'配置为true可将UIAbility拉起到前台；否则表示将UIAbility拉起到后台。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Caller](js-apis-app-ability-uiability.md#caller)> | Promise对象，获取要通讯的caller对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000018 | Redirection to a third-party application is not allowed in API version greater than 11. |
| 16000050 | Internal error. Possible causes: 1.Connect to system service failed. 2.Sending restart message to system service failed. 3.System service failed to communicate with dependency module. 4.Non-system applications are only allowed to call this interface across devices, not on the current device. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |

**示例：**

下面代码展示的是，调用方启动目标方到后台，获取Caller成功后发消息到目标方，然后释放Caller对象。

```
1. import { Caller, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { rpc } from '@kit.IPCKit';

5. const DOMAIN = 0x0000;
6. const LOG_TAG = 'TEST_TAG';

8. class TestParcelable implements rpc.Parcelable {
9. age: number = 0;
10. name: string = '';
11. marshalling(dataOut: rpc.MessageSequence): boolean {
12. dataOut.writeInt(this.age);
13. dataOut.writeString(this.name);
14. return true;
15. }
16. unmarshalling(dataIn: rpc.MessageSequence): boolean {
17. this.age = dataIn.readInt();
18. this.name = dataIn.readString();
19. return true;
20. }
21. }

23. export default class EntryAbility extends UIAbility {
24. async onForeground() {
25. let caller: Caller;
26. // 后台启动Ability
27. let wantBackground: Want = {
28. bundleName: 'com.example.myapplication',
29. abilityName: 'EntryAbility',
30. };

32. try {
33. caller = await this.context.startAbilityByCall(wantBackground);
34. await caller.call('TEST_CALL', new TestParcelable());
35. caller.release();
36. } catch (err) {
37. // 处理入参错误异常
38. hilog.error(DOMAIN, LOG_TAG, `startAbilityByCall failed ${err}`);
39. }
40. }
41. }
```

下面代码展示，目标方启动后注册监听，销毁时取消监听。

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { rpc } from '@kit.IPCKit';

5. const DOMAIN = 0x0000;
6. const LOG_TAG = 'TEST_TAG';

8. class TestParcelable implements rpc.Parcelable {
9. age: number = 0;
10. name: string = '';
11. marshalling(dataOut: rpc.MessageSequence): boolean {
12. dataOut.writeInt(this.age);
13. dataOut.writeString(this.name);
14. return true;
15. }
16. unmarshalling(dataIn: rpc.MessageSequence): boolean {
17. this.age = dataIn.readInt();
18. this.name = dataIn.readString();
19. return true;
20. }
21. }

23. export default class EntryAbility extends UIAbility {
24. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
25. hilog.info(DOMAIN, LOG_TAG, '%{public}s', 'Ability onCreate');
26. // 注册监听
27. this.callee.on('TEST_CALL', (data: rpc.MessageSequence) => {
28. let recv = new TestParcelable();
29. data.readParcelable(recv);
30. recv.age++;
31. return recv;
32. });
33. }

35. onDestroy(): void {
36. hilog.info(DOMAIN, LOG_TAG, '%{public}s', 'Ability onDestroy');
37. // 取消监听
38. this.callee.off('TEST_CALL');
39. }
40. }
```

下面代码展示，调用方启动目标方到前台场景。

```
1. import { Caller, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const DOMAIN = 0x0000;
5. const LOG_TAG = 'TEST_TAG';

7. export default class EntryAbility extends UIAbility {
8. async onForeground() {
9. let caller: Caller;
10. // 启动UIAbility到前台，将parameters中的'ohos.aafwk.param.callAbilityToForeground'配置为true
11. let wantForeground: Want = {
12. bundleName: 'com.example.myapplication',
13. abilityName: 'EntryAbility',
14. parameters: {
15. 'ohos.aafwk.param.callAbilityToForeground': true
16. }
17. };

19. try {
20. caller = await this.context.startAbilityByCall(wantForeground);
21. caller.release();
22. } catch (err) {
23. // 处理入参错误异常
24. hilog.error(DOMAIN, LOG_TAG, `startAbilityByCall failed ${err}`);
25. }
26. }
27. }
```

### setMissionLabel

PhonePC/2in1TabletTVWearable

setMissionLabel(label: string, callback: AsyncCallback<void>): void

设置UIAbility在多任务界面中显示的名称。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 是 | 任务的名称。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当设置UIAbility在多任务界面中显示的名称成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
6. this.context.setMissionLabel('test', (result: BusinessError) => {
7. console.info(`setMissionLabel: ${JSON.stringify(result)}`);
8. });
9. }
10. }
```

### setMissionLabel

PhonePC/2in1TabletTVWearable

setMissionLabel(label: string): Promise<void>

设置UIAbility在多任务界面中显示的名称。使用Promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 是 | 任务的名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
6. this.context.setMissionLabel('test').then(() => {
7. console.info('success');
8. }).catch((err: BusinessError) => {
9. let code = (err as BusinessError).code;
10. let message = (err as BusinessError).message;
11. console.error(`setMissionLabel failed, code is ${code}, message is ${message}`);
12. });
13. }
14. }
```

### setMissionContinueState10+

PhonePC/2in1TabletTVWearable

setMissionContinueState(state: AbilityConstant.ContinueState, callback: AsyncCallback<void>): void

设置UIAbility任务的流转状态。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AbilityConstant.ContinueState](js-apis-app-ability-abilityconstant.md#continuestate10) | 是 | 流转状态。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当设置UIAbility任务的流转状态成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**错误码：**

错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility, AbilityConstant } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. this.context.setMissionContinueState(AbilityConstant.ContinueState.INACTIVE, (result: BusinessError) => {
7. console.info(`setMissionContinueState: ${JSON.stringify(result)}`);
8. });
9. }
10. }
```

### setMissionContinueState10+

PhonePC/2in1TabletTVWearable

setMissionContinueState(state: AbilityConstant.ContinueState): Promise<void>

设置UIAbility任务的流转状态。使用Promise异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| state | [AbilityConstant.ContinueState](js-apis-app-ability-abilityconstant.md#continuestate10) | 是 | 流转状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

**错误码：**

错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility, AbilityConstant } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. this.context.setMissionContinueState(AbilityConstant.ContinueState.INACTIVE).then(() => {
7. console.info('success');
8. }).catch((err: BusinessError) => {
9. console.error(`setMissionContinueState failed, code is ${err.code}, message is ${err.message}`);
10. });
11. }
12. }
```

### restoreWindowStage

PhonePC/2in1TabletTVWearable

restoreWindowStage(localStorage: LocalStorage): void

恢复UIAbility中的WindowStage数据。仅支持在主线程调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| localStorage | [LocalStorage](../harmonyos-guides/arkts-localstorage.md) | 是 | 用于恢复window stage的存储数据。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onForeground() {
5. let storage = new LocalStorage();
6. this.context.restoreWindowStage(storage);
7. }
8. }
```

### isTerminating

PhonePC/2in1TabletTVWearable

isTerminating(): boolean

查询UIAbility是否处于消亡中状态。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 表示是否处于消亡中状态。true表示处于消亡中状态，false表示不处于消亡中状态。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onForeground() {
5. let isTerminating: boolean = this.context.isTerminating();
6. console.info(`ability state is ${isTerminating}`);
7. }
8. }
```

### requestDialogService

PhonePC/2in1TabletTVWearable

requestDialogService(want: Want, result: AsyncCallback<dialogRequest.RequestResult>): void

启动一个支持模态弹框的ServiceExtensionAbility。ServiceExtensionAbility被启动后，应用弹出模态弹框，通过调用[setRequestResult](js-apis-app-ability-dialogrequest.md#requestcallbacksetrequestresult)接口返回结果给调用者。使用callback异步回调。仅支持在主线程调用。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动ServiceExtensionAbility的Want信息。 |
| result | AsyncCallback<[dialogRequest.RequestResult](js-apis-app-ability-dialogrequest.md#requestresult)> | 是 | 回调函数，当启动一个支持模态弹框的ServiceExtensionAbility成功，err中code为0，data为模态弹框请求结果；否则err会返回对应的错误码和错误信息。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { UIAbility, Want, dialogRequest } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let want: Want = {
7. deviceId: '',
8. bundleName: 'com.example.myapplication',
9. abilityName: 'AuthAccountServiceExtension'
10. };

12. try {
13. this.context.requestDialogService(want, (err: BusinessError, result: dialogRequest.RequestResult) => {
14. if (err.code) {
15. // 处理业务逻辑错误
16. console.error(`requestDialogService failed, code is ${err.code}, message is ${err.message}`);
17. return;
18. }
19. // 执行正常业务
20. console.info(`requestDialogService succeed, result = ${JSON.stringify(result)}`);
21. });
22. } catch (err) {
23. // 处理入参错误异常
24. let code = (err as BusinessError).code;
25. let message = (err as BusinessError).message;
26. console.error(`requestDialogService failed, code is ${code}, message is ${message}`);
27. }
28. }
29. }
```

### requestDialogService

PhonePC/2in1TabletTVWearable

requestDialogService(want: Want): Promise<dialogRequest.RequestResult>

启动一个支持模态弹框的ServiceExtensionAbility。ServiceExtensionAbility被启动后，应用弹出模态弹框，通过调用[setRequestResult](js-apis-app-ability-dialogrequest.md#requestcallbacksetrequestresult)接口返回结果给调用者。使用Promise异步回调。仅支持在主线程调用。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动ServiceExtensionAbility的Want信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[dialogRequest.RequestResult](js-apis-app-ability-dialogrequest.md#requestresult)> | Promise对象，包含接口执行结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { UIAbility, Want, dialogRequest } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let want: Want = {
7. bundleName: 'com.example.myapplication',
8. abilityName: 'AuthAccountServiceExtension'
9. };

11. try {
12. this.context.requestDialogService(want)
13. .then((result: dialogRequest.RequestResult) => {
14. // 执行正常业务
15. console.info(`requestDialogService succeed, result = ${JSON.stringify(result)}`);
16. })
17. .catch((err: BusinessError) => {
18. // 处理业务逻辑错误
19. console.error(`requestDialogService failed, code is ${err.code}, message is ${err.message}`);
20. });
21. } catch (err) {
22. // 处理入参错误异常
23. let code = (err as BusinessError).code;
24. let message = (err as BusinessError).message;
25. console.error(`requestDialogService failed, code is ${code}, message is ${message}`);
26. }
27. }
28. }
```

### reportDrawnCompleted10+

PhonePC/2in1TabletTVWearable

reportDrawnCompleted(callback: AsyncCallback<void>): void

用于通知系统UIAbility对应的窗口内容已经绘制完成。使用callback异步回调。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数，当通知系统UIAbility对应的窗口内容已经绘制完成的操作成功，err中code为0；否则err会返回对应的错误码和错误信息。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. windowStage.loadContent('pages/Index', (err, data) => {
8. if (err.code) {
9. return;
10. }

12. try {
13. this.context.reportDrawnCompleted((err) => {
14. if (err.code) {
15. // 处理业务逻辑错误
16. console.error(`reportDrawnCompleted failed, code is ${err.code}, message is ${err.message}`);
17. return;
18. }
19. // 执行正常业务
20. console.info('reportDrawnCompleted succeed');
21. });
22. } catch (err) {
23. // 捕获同步的参数错误
24. let code = (err as BusinessError).code;
25. let message = (err as BusinessError).message;
26. console.error(`reportDrawnCompleted failed, code is ${code}, message is ${message}`);
27. }
28. });
29. console.info("MainAbility onWindowStageCreate");
30. }
31. };
```

### startAbilityByType11+

PhonePC/2in1TabletTVWearable

startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback, callback: AsyncCallback<void>) : void

通过type隐式启动[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)。使用callback异步回调。仅支持在主线程调用，仅支持处于前台的应用调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 启动的UIExtensionAbility类型，取值详见[通过startAbilityByType接口拉起垂类面板](../harmonyos-guides/start-intent-panel.md#匹配规则)。 |
| wantParam | Record<string, Object> | 是 | 表示扩展参数。 |
| abilityStartCallback | [AbilityStartCallback](js-apis-inner-application-abilitystartcallback.md) | 是 | 回调函数，返回启动失败后的详细错误信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数，当接口调用成功，err为undefined；否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility, common } from '@kit.AbilityKit';

3. export default class EntryAbility extends UIAbility {
4. onForeground() {
5. let wantParam: Record<string, Object> = {
6. 'time': '2023-10-23 20:45'
7. };
8. let abilityStartCallback: common.AbilityStartCallback = {
9. onError: (code: number, name: string, message: string) => {
10. console.info(`code:` + code + `name:` + name + `message:` + message);
11. },
12. onResult: (abilityResult: common.AbilityResult) => {
13. console.info(`resultCode:` + abilityResult.resultCode + `bundleName:` + abilityResult.want?.bundleName);
14. }
15. };

17. this.context.startAbilityByType("photoEditor", wantParam, abilityStartCallback, (err) => {
18. if (err) {
19. console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
20. } else {
21. console.info(`success`);
22. }
23. });
24. }
25. }
```

### startAbilityByType11+

PhonePC/2in1TabletTVWearable

startAbilityByType(type: string, wantParam: Record<string, Object>, abilityStartCallback: AbilityStartCallback) : Promise<void>

通过type隐式启动[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)。使用Promise异步回调。仅支持在主线程调用，仅支持处于前台的应用调用。

**元服务API**：从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 启动的UIExtensionAbility类型，取值详见[通过startAbilityByType接口拉起垂类面板](../harmonyos-guides/start-intent-panel.md#匹配规则)。 |
| wantParam | Record<string, Object> | 是 | 表示扩展参数。 |
| abilityStartCallback | [AbilityStartCallback](js-apis-inner-application-abilitystartcallback.md) | 是 | 回调函数，返回启动失败后的详细错误信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility, common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let wantParam: Record<string, Object> = {
7. 'time': '2023-10-23 20:45'
8. };
9. let abilityStartCallback: common.AbilityStartCallback = {
10. onError: (code: number, name: string, message: string) => {
11. console.info(`code:` + code + `name:` + name + `message:` + message);
12. },
13. onResult: (abilityResult: common.AbilityResult) => {
14. console.info(`resultCode:` + abilityResult.resultCode + `bundleName:` + abilityResult.want?.bundleName);
15. }
16. };

18. this.context.startAbilityByType("photoEditor", wantParam, abilityStartCallback).then(() => {
19. console.info(`startAbilityByType success`);
20. }).catch((err: BusinessError) => {
21. console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
22. });
23. }
24. }
```

### showAbility12+

PhonePC/2in1TabletTVWearable

showAbility(): Promise<void>

显示当前UIAbility。使用Promise异步回调。仅支持在主线程调用。

调用此接口前要求确保应用已添加至状态栏。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在PC/2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not support. |
| 16000050 | Internal error. |
| 16000067 | The StartOptions check failed. |

**示例：**

```
1. // Index.ets
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. @State showAbility: string = 'showAbility'

10. build() {
11. Row() {
12. Column() {
13. Text(this.showAbility)
14. .fontSize(30)
15. .fontWeight(FontWeight.Bold)
16. .onClick(() => {
17. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

19. context.showAbility().then(() => {
20. console.info(`showAbility success`);
21. }).catch((err: BusinessError) => {
22. console.error(`showAbility fail, err: ${JSON.stringify(err)}`);
23. });
24. });
25. }
26. .width('100%')
27. }
28. .height('100%')
29. }
30. }
```

```
1. // EntryAbility.ts
2. import { UIAbility, Want, StartOptions, contextConstant } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onForeground() {
7. let want: Want = {
8. deviceId: '',
9. bundleName: 'com.example.myapplication',
10. abilityName: 'EntryAbility'
11. };
12. let options: StartOptions = {
13. displayId: 0,
14. processMode: contextConstant.ProcessMode.NEW_PROCESS_ATTACH_TO_STATUS_BAR_ITEM,
15. startupVisibility: contextConstant.StartupVisibility.STARTUP_SHOW
16. };

18. try {
19. this.context.startAbility(want, options, (err: BusinessError) => {
20. if (err.code) {
21. // 处理业务逻辑错误
22. console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
23. return;
24. }
25. // 执行正常业务
26. console.info('startAbility succeed');
27. });
28. } catch (err) {
29. // 处理入参错误异常
30. let code = (err as BusinessError).code;
31. let message = (err as BusinessError).message;
32. console.error(`startAbility failed, code is ${code}, message is ${message}`);
33. }
34. }
35. }
```

### hideAbility12+

PhonePC/2in1TabletTVWearable

hideAbility(): Promise<void>

隐藏当前UIAbility。使用Promise异步回调。仅支持在主线程调用。

调用此接口前要求确保应用已添加至状态栏。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在PC/2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not support. |
| 16000050 | Internal error. |
| 16000067 | The StartOptions check failed. |

**示例：**

```
1. // Index.ets
2. import { common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct Index {
8. @State hideAbility: string = 'hideAbility'

10. build() {
11. Row() {
12. Column() {
13. Text(this.hideAbility)
14. .fontSize(30)
15. .fontWeight(FontWeight.Bold)
16. .onClick(() => {
17. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

19. context.hideAbility().then(() => {
20. console.info(`hideAbility success`);
21. }).catch((err: BusinessError) => {
22. console.error(`hideAbility fail, err: ${JSON.stringify(err)}`);
23. });
24. });
25. }
26. .width('100%')
27. }
28. .height('100%')
29. }
30. }
```

```
1. // EntryAbility.ts
2. import { UIAbility, Want, StartOptions, contextConstant } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onForeground() {
7. let want: Want = {
8. deviceId: '',
9. bundleName: 'com.example.myapplication',
10. abilityName: 'EntryAbility'
11. };
12. let options: StartOptions = {
13. displayId: 0,
14. processMode: contextConstant.ProcessMode.NEW_PROCESS_ATTACH_TO_STATUS_BAR_ITEM,
15. startupVisibility: contextConstant.StartupVisibility.STARTUP_HIDE
16. };

18. try {
19. this.context.startAbility(want, options, (err: BusinessError) => {
20. if (err.code) {
21. // 处理业务逻辑错误
22. console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
23. return;
24. }
25. // 执行正常业务
26. console.info('startAbility succeed');
27. });
28. } catch (err) {
29. // 处理入参错误异常
30. let code = (err as BusinessError).code;
31. let message = (err as BusinessError).message;
32. console.error(`startAbility failed, code is ${code}, message is ${message}`);
33. }
34. }
35. }
```

### moveAbilityToBackground12+

PhonePC/2in1TabletTVWearable

moveAbilityToBackground(): Promise<void>

将处于前台的UIAbility移动到后台。使用Promise异步回调。仅支持在主线程调用。

该接口仅支持手机和平板设备。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：

* 从API version 12开始，该接口仅在Phone、Wearable和TV设备中可正常调用，在其他设备上返回16000061错误码。
* 从API version 13开始，该接口仅在Phone、Tablet、Wearable和TV设备中可正常调用，在其他设备上返回16000061错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000061 | Operation not supported. |
| 16000065 | The API can be called only when the ability is running in the foreground. |
| 16000066 | An ability cannot switch to the foreground or background in Wukong mode. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. @State moveAbilityToBackground: string = 'Move To Background'

9. build() {
10. Row() {
11. Column() {
12. Text(this.moveAbilityToBackground)
13. .fontSize(30)
14. .fontWeight(FontWeight.Bold)
15. .onClick(() => {
16. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

18. context.moveAbilityToBackground().then(() => {
19. console.info(`moveAbilityToBackground success.`);
20. }).catch((err: BusinessError) => {
21. console.error(`moveAbilityToBackground error: ${JSON.stringify(err)}.`);
22. });
23. });
24. }
25. .width('100%')
26. }
27. .height('100%')
28. }
29. }
```

### openAtomicService12+

PhonePC/2in1TabletTVWearable

openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>

启动一个独立窗口的元服务。使用Promise异步回调。仅支持在主线程调用。

元服务被启动后，有如下情况：

* 正常情况下元服务可以通过[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口销毁自身，并且返回结果给调用方。
* 异常情况下比如杀死元服务会返回异常结果给调用方，异常结果的resultCode为-1。
* 如果不同应用多次调用该接口启动同一个元服务，当这个元服务调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口销毁自身时，只将正常结果返回给最后一个调用方, 其它调用方返回异常结果，异常结果中resultCode为-1。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的唯一标识，由云端统一分配。 |
| options | [AtomicServiceOptions](js-apis-app-ability-atomicserviceoptions.md) | 否 | 启动元服务所携带的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AbilityResult](js-apis-inner-ability-abilityresult.md)> | Promise对象，包含返回给拉起方的信息。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000002 | Incorrect ability type. |
| 16000003 | The specified ID does not exist. |
| 16000004 | Cannot start an invisible component. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000050 | Internal error. |
| 16000053 | The ability is not on the top of the UI. |
| 16000055 | Installation-free timed out. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { UIAbility, common, AtomicServiceOptions } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let appId: string = '6918661953712445909';
7. let options: AtomicServiceOptions = {
8. displayId: 0
9. };

11. try {
12. this.context.openAtomicService(appId, options)
13. .then((result: common.AbilityResult) => {
14. // 执行正常业务
15. console.info('openAtomicService succeed');
16. })
17. .catch((err: BusinessError) => {
18. // 处理业务逻辑错误
19. console.error(`openAtomicService failed, code is ${err.code}, message is ${err.message}`);
20. });
21. } catch (err) {
22. // 处理入参错误异常
23. let code = (err as BusinessError).code;
24. let message = (err as BusinessError).message;
25. console.error(`openAtomicService failed, code is ${code}, message is ${message}`);
26. }
27. }
28. }
```

### openLink12+

PhonePC/2in1TabletTVWearable

openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>

通过[App Linking](../harmonyos-guides/app-linking-startup.md)或[Deep Linking](../harmonyos-guides/deep-linking-startup.md)方式启动UIAbility，并通过回调函数接收被拉起的UIAbility退出时的返回结果。使用Promise异步回调。仅支持在主线程调用。

通过在link字段中传入标准格式的URL，基于隐式want匹配规则拉起目标UIAbility。目标方必须同时具备以下过滤器特征，才能处理App Linking链接：

* "actions"列表中包含"ohos.want.action.viewData"。
* "entities"列表中包含"entity.system.browsable"。
* "uris"列表中包含"scheme"为"https"且"domainVerify"为true的元素。

如果希望获取被拉起方终止后的结果，可以设置callback参数，此参数的使用可参照[startAbilityForResult](js-apis-inner-application-uiabilitycontext.md#startabilityforresult)接口。

传入的参数不合法时，如未设置必选参数或link字符串不是标准格式的URL，接口会直接抛出异常。参数校验通过，拉起目标方时出现的错误通过promise返回错误信息。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| link | string | 是 | 指示要打开的标准格式URL。 |
| options | [OpenLinkOptions](js-apis-app-ability-openlinkoptions.md) | 否 | 打开URL的选项参数。 |
| callback | AsyncCallback<[AbilityResult](js-apis-inner-ability-abilityresult.md)> | 否 | 回调函数，包含返回给拉起方的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000019 | No matching ability is found. |
| 16200001 | The caller has been released. |
| 16000053 | The ability is not on the top of the UI. |
| 16000136 | The UIAbility is prohibited from launching itself via App Linking. |

**示例：**

```
1. import { common, OpenLinkOptions } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. const DOMAIN = 0xeeee;
6. const TAG: string = '[openLinkDemo]';

8. @Entry
9. @Component
10. struct Index {
11. build() {
12. RelativeContainer() {
13. Button("Call StartAbilityForResult")
14. .onClick(() => {
15. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
16. let link: string = 'https://www.example.com';
17. let openLinkOptions: OpenLinkOptions = {
18. appLinkingOnly: true,
19. parameters: { demo_key: 'demo_value' }
20. };

22. try {
23. context.openLink(
24. link,
25. openLinkOptions,
26. (err, result) => {
27. hilog.error(DOMAIN, TAG, `openLink callback error.code: ${JSON.stringify(err)}`);
28. hilog.info(DOMAIN, TAG, `openLink callback result: ${JSON.stringify(result.resultCode)}`);
29. hilog.info(DOMAIN, TAG, `openLink callback result data: ${JSON.stringify(result.want)}`);
30. }
31. ).then(() => {
32. hilog.info(DOMAIN, TAG, `open link success.`);
33. }).catch((err: BusinessError) => {
34. hilog.error(DOMAIN, TAG, `open link failed, errCode ${JSON.stringify(err.code)}`);
35. });
36. }
37. catch (e) {
38. hilog.error(DOMAIN, TAG, `exception occured, errCode ${JSON.stringify(e.code)}`);
39. }
40. })
41. }
42. .height('100%')
43. .width('100%')
44. }
45. }
```

### backToCallerAbilityWithResult12+

PhonePC/2in1TabletTVWearable

backToCallerAbilityWithResult(abilityResult: AbilityResult, requestCode: string): Promise<void>

当通过[startAbilityForResult](js-apis-inner-application-uiabilitycontext.md#startabilityforresult)或[openLink](js-apis-inner-application-uiabilitycontext.md#openlink12)拉起目标方UIAbility，且需要目标方返回结果时，目标方可以通过该接口将结果返回并拉起调用方。与[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)不同的是，本接口在返回时不会销毁当前UIAbility。使用Promise异步回调。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| abilityResult | [AbilityResult](js-apis-inner-ability-abilityresult.md) | 是 | 包含目标方返回给拉起方的结果。 |
| requestCode | string | 是 | 通过[startAbilityForResult](js-apis-inner-application-uiabilitycontext.md#startabilityforresult)或[openLink](js-apis-inner-application-uiabilitycontext.md#openlink12)拉起目标方Ability且需要目标方返回结果时，系统生成的用于标识本次调用的requestCode。该值可以通过want中的[CALLER\_REQUEST\_CODE](js-apis-app-ability-wantconstant.md)字段获取。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000074 | The caller does not exist. |
| 16000075 | BackToCaller is not supported. |

**示例：**

调用方通过startAbilityForResult接口拉起目标方, 目标方再调用backToCallerAbilityWithResult接口返回到调用方。

```
1. // 调用方
2. // index.ets
3. import { common, Want } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. @Entry
8. @Component
9. struct Index {
10. @State message: string = 'Hello World';

12. build() {
13. Row() {
14. Column() {
15. Text(this.message)
16. .fontSize(30)
17. .fontWeight(FontWeight.Bold)

19. Button("Call StartAbilityForResult")
20. .onClick(() => {
21. let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
22. let want: Want = {
23. bundleName: 'com.example.demo2',
24. abilityName: 'EntryAbility'
25. };

27. try {
28. // 通过startAbilityForResult拉起目标应用
29. context.startAbilityForResult(want, (err: BusinessError, result: common.AbilityResult) => {
30. if (err.code) {
31. // 处理业务逻辑错误
32. hilog.error(0x0000, 'testTag', `startAbilityForResult failed, code is ${err.code}, message is ${err.message}`);
33. this.message = `startAbilityForResult failed: code is ${err.code}, message is ${err.message}`
34. return;
35. }
36. // 执行正常业务
37. hilog.info(0x0000, 'testTag', `startAbilityForResult succeed`);
38. hilog.info(0x0000, 'testTag', `AbilityResult is ${JSON.stringify(result)}`);
39. this.message = `AbilityResult.resultCode: ${JSON.stringify(result.resultCode)}`
40. });
41. } catch (err) {
42. // 处理入参错误异常
43. let code = (err as BusinessError).code;
44. let message = (err as BusinessError).message;
45. hilog.error(0x0000, 'testTag', `startAbilityForResult failed, code is ${code}, message is ${message}`);
46. this.message = `startAbilityForResult failed, code is ${code}, message is ${message}`;
47. }
48. })
49. }
50. .width('100%')
51. }
52. .height('100%')
53. }
54. }
```

```
1. // 目标方
2. // EntryAbility.ets
3. import { AbilityConstant, common, UIAbility, Want, wantConstant } from '@kit.AbilityKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';
5. import { BusinessError } from '@kit.BasicServicesKit';

7. export default class EntryAbility extends UIAbility {
8. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
9. // 从want中获取调用方的CALLER_REQUEST_CODE，并保存
10. let callerRequestCode: string = want?.parameters?.[wantConstant.Params.CALLER_REQUEST_CODE] as string;
11. AppStorage.setOrCreate<string>("callerRequestCode", callerRequestCode)
12. }

14. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
15. let callerRequestCode: string = want?.parameters?.[wantConstant.Params.CALLER_REQUEST_CODE] as string;
16. AppStorage.setOrCreate<string>("callerRequestCode", callerRequestCode)
17. }

19. onForeground(): void {
20. // 获取保存的CALLER_REQUEST_CODE
21. let callerRequestCode: string = AppStorage.get<string>("callerRequestCode") as string;
22. hilog.info(0x0000, 'testTag', `callerRequestCode is ${callerRequestCode}`);
23. let want: Want = {};
24. let resultCode = 100;
25. let abilityResult: common.AbilityResult = {
26. want,
27. resultCode
28. };
29. try {
30. // 将结果信息返回给调用方
31. this.context.backToCallerAbilityWithResult(abilityResult, callerRequestCode)
32. .then(() => {
33. // 执行正常业务
34. hilog.info(0x0000, 'testTag', 'backToCallerAbilityWithResult succeed');
35. })
36. .catch((err: BusinessError) => {
37. // 处理业务逻辑错误
38. hilog.error(0x0000, 'testTag', `backToCallerAbilityWithResult failed, code is ${err.code}, message is ${err.message}`);
39. });
40. } catch (err) {
41. // 捕获同步的参数错误
42. let code = (err as BusinessError).code;
43. let message = (err as BusinessError).message;
44. hilog.error(0x0000, 'testTag', `backToCallerAbilityWithResult failed, code is ${code}, message is ${message}`);
45. }
46. }
47. }
```

### setRestoreEnabled14+

PhonePC/2in1TabletTVWearable

setRestoreEnabled(enabled: boolean): void

设置UIAbility是否启用备份恢复。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 表示是否启用恢复。true表示启用，false表示不启用。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | If the input parameter is not valid parameter. |
| 16000011 | The context does not exist. |

**示例：**

```
1. import { UIAbility, AbilityConstant, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. let enabled = true;
7. try {
8. this.context.setRestoreEnabled(enabled);
9. } catch (paramError) {
10. let code = (paramError as BusinessError).code;
11. let message = (paramError as BusinessError).message;
12. console.error(`setRestoreEnabled failed, err code: ${code}, err msg: ${message}`);
13. }
14. }
15. }
```

### startUIServiceExtensionAbility14+

PhonePC/2in1TabletTVWearable

startUIServiceExtensionAbility(want: Want): Promise<void>

启动一个UIServiceExtensionAbility。使用Promise异步回调。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UIServiceExtensionAbility的必要信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16200001 | The caller has been released. |

**示例：**

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. Column() {
9. Row() {
10. // 创建启动按钮
11. Button('start ability')
12. .enabled(true)
13. .onClick(() => {
14. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
15. let startWant: Want = {
16. bundleName: 'com.acts.uiserviceextensionability',
17. abilityName: 'UiServiceExtAbility',
18. };
19. try {
20. // 启动UIServiceExtensionAbility
21. context.startUIServiceExtensionAbility(startWant).then(() => {
22. console.info('startUIServiceExtensionAbility success');
23. }).catch((error: BusinessError) => {
24. console.info('startUIServiceExtensionAbility error', JSON.stringify(error));
25. })
26. } catch (err) {
27. console.info('startUIServiceExtensionAbility failed', JSON.stringify(err));
28. }
29. })
30. }
31. }
32. }
33. }
```

### connectUIServiceExtensionAbility14+

PhonePC/2in1TabletTVWearable

connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>

连接一个UIServiceExtensionAbility。使用Promise异步回调。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 连接UIServiceExtensionAbility的必要信息。 |
| callback | [UIServiceExtensionConnectCallback](nner-application-uiserviceextensionconnectcallback.md) | 是 | 连接UIServiceExtensionAbility回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<UIServiceProxy> | Promise对象，包含connectUIServiceExtensionAbility执行后返回的[UIServiceProxy](js-apis-inner-application-uiserviceproxy.md)对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 801 | Capability not supported. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000055 | Installation-free timed out. |

**示例：**

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const TAG: string = '[Extension] ';

6. @Entry
7. @Component
8. struct UIServiceExtensionAbility {
9. dataCallBack : common.UIServiceExtensionConnectCallback = {
10. // 接收数据
11. onData: (data: Record<string, Object>) => {
12. console.info(`dataCallBack received data`, JSON.stringify(data));
13. },
14. // 连接断开
15. onDisconnect: () => {
16. console.info(`dataCallBack onDisconnect`);
17. }
18. }

20. async myConnect() {
21. // 获取上下文
22. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
23. let startWant: Want = {
24. deviceId: '',
25. bundleName: 'com.example.myapplication',
26. abilityName: 'UiServiceExtAbility'
27. };

29. try {
30. // 连接服务
31. context.connectUIServiceExtensionAbility(startWant, this.dataCallBack)
32. .then((proxy: common.UIServiceProxy) => {
33. console.info(TAG + `try to connectUIServiceExtensionAbility`, JSON.stringify(proxy));
34. }).catch((err: Error) => {
35. let code = (err as BusinessError).code;
36. let message = (err as BusinessError).message;
37. console.error(TAG + `connectUIServiceExtensionAbility failed, code is ${code}, message is ${message}`);
38. });
39. } catch (err) {
40. let code = (err as BusinessError).code;
41. let message = (err as BusinessError).message;
42. console.error(TAG + `connectUIServiceExtensionAbility failed, code is ${code}, message is ${message}`);
43. };
44. }

46. build() {
47. RelativeContainer() {
48. // 创建连接按钮
49. Button('connectServiceExtensionAbility', { type: ButtonType.Capsule, stateEffect: true })
50. .alignRules({
51. center: { anchor: '__container__', align: VerticalAlign.Center },
52. middle: { anchor: '__container__', align: HorizontalAlign.Center }
53. })
54. .onClick(() => {
55. this.myConnect()
56. });
57. }
58. .height('100%')
59. .width('100%')
60. }
61. }
```

### disconnectUIServiceExtensionAbility14+

PhonePC/2in1TabletTVWearable

disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>

断开与UIServiceExtensionAbility的连接。使用Promise异步回调。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxy | [UIServiceProxy](js-apis-inner-application-uiserviceproxy.md) | 是 | [connectUIServiceExtensionAbility](js-apis-inner-application-uiabilitycontext.md#connectuiserviceextensionability14)执行返回的Proxy。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. const TAG: string = '[Extension] ';

6. @Entry
7. @Component
8. struct UIServiceExtensionAbility {
9. comProxy: common.UIServiceProxy | null = null;

11. build() {
12. Scroll() {
13. Column() {
14. // 创建断开连接的按钮
15. Button('disconnectUIServiceExtensionAbility', { type: ButtonType.Capsule, stateEffect: true })
16. .margin({
17. top: 5,
18. left: 10,
19. right: 10,
20. bottom: 5
21. })
22. .alignRules({
23. center: { anchor: '__container__', align: VerticalAlign.Center },
24. middle: { anchor: '__container__', align: HorizontalAlign.Center }
25. })
26. .onClick(() => {
27. this.myDisconnectUIServiceExtensionAbility()
28. });
29. }
30. .width('100%')
31. }
32. .height('100%')
33. }

35. myDisconnectUIServiceExtensionAbility() {
36. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;

38. try {
39. // 断开UIServiceExtension连接
40. context.disconnectUIServiceExtensionAbility(this.comProxy)
41. .then(() => {
42. console.info(TAG + `disconnectUIServiceExtensionAbility succeed ${this.comProxy}`);
43. }).catch((err: Error) => {
44. let code = (err as BusinessError).code;
45. let message = (err as BusinessError).message;
46. console.error(TAG + `disconnectUIServiceExtensionAbility failed, code is ${code}, message is ${message}`);
47. });
48. } catch (err) {
49. let code = (err as BusinessError).code;
50. let message = (err as BusinessError).message;
51. console.error(TAG + `disconnectUIServiceExtensionAbility failed, code is ${code}, message is ${message}`);
52. }
53. }
54. }
```

### setAbilityInstanceInfo15+

PhonePC/2in1TabletTVWearable

setAbilityInstanceInfo(label: string, icon: image.PixelMap): Promise<void>

设置当前UIAbility实例的图标和标签信息。图标与标签信息可在任务中心和快捷栏的界面中显示。使用Promise异步回调。

**需要权限**： ohos.permission.SET\_ABILITY\_INSTANCE\_INFO

**系统能力**： SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 是 | 新的图标标签。标签长度不超过1024字节，且不可为空字符串。 |
| icon | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 新的图标。建议图标大小为512px\*512px。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例**：

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. export default class EntryAbility extends UIAbility {
7. onWindowStageCreate(windowStage: window.WindowStage): void {
8. windowStage.loadContent('pages/Index', async (err, data) => {
9. if (err.code) {
10. console.error(`loadContent failed, code is ${err.code}`);
11. return;
12. }

14. let newLabel: string = 'instance label';
15. let color = new ArrayBuffer(512 * 512 * 4); // 创建一个ArrayBuffer对象，用于存储图像像素。该对象的大小为（height * width * 4）字节。
16. let bufferArr = new Uint8Array(color);
17. for (let i = 0; i < bufferArr.length; i += 4) {
18. bufferArr[i] = 255;
19. bufferArr[i+1] = 0;
20. bufferArr[i+2] = 122;
21. bufferArr[i+3] = 255;
22. }
23. let opts: image.InitializationOptions = {
24. editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 512, width: 512 }
25. };
26. let imagePixelMap: image.PixelMap = await image.createPixelMap(color, opts);
27. this.context.setAbilityInstanceInfo(newLabel, imagePixelMap)
28. .then(() => {
29. console.info('setAbilityInstanceInfo success');
30. }).catch((err: BusinessError) => {
31. console.error(`setAbilityInstanceInfo failed, code is ${err.code}, message is ${err.message}`);
32. });
33. });
34. }
35. }
```

### revokeDelegator17+

PhonePC/2in1TabletTVWearable

revokeDelegator(): Promise<void>

如果Module下首个UIAbility启动时期望重定向到另一个UIAbility，该重定向的UIAbility被称为“DelegatorAbility”。DelegatorAbility的设置详见当前接口示例的步骤1。

当DelegatorAbility完成特定操作时，可以使用该接口回到首个UIAbility。使用Promise异步回调。

说明

当接口调用成功后，DelegatorAbility中的[Window](arkts-apis-window.md)方法会失效。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，包含接口执行结果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not support. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000065 | The API can be called only when the ability is running in the foreground. |
| 16000084 | Only DelegatorAbility is allowed to call this API, and only once. |
| 16000085 | An error occurred during the interaction between the ability and window. |

**示例**：

1. 设置DelegatorAbility。

   在[module.json5](../harmonyos-guides/module-configuration-file.md)配置文件标签中配置abilitySrcEntryDelegator和abilityStageSrcEntryDelegator。当Module下首个UIAbility冷启动时，系统优先启动abilitySrcEntryDelegator指向的UIAbility。

   说明

   * 当UIAbility是通过[startAbilityByCall](js-apis-inner-application-uiabilitycontext.md#startabilitybycall)启动时，系统会忽略在[module.json5](../harmonyos-guides/module-configuration-file.md)配置文件标签中配置的abilitySrcEntryDelegator和abilityStageSrcEntryDelegator。
   * abilityStageSrcEntryDelegator指定的ModuleName不能与当前ModuleName相同。

   ```
   1. {
   2. "module": {
   3. // ...
   4. "abilityStageSrcEntryDelegator": "xxxModuleName",
   5. "abilitySrcEntryDelegator": "xxxAbilityName",
   6. // ...
   7. }
   8. }
   ```
2. 取消DelegatorAbility。

   ```
   1. import { UIAbility } from '@kit.AbilityKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. export default class DelegatorAbility extends UIAbility {
   5. onForeground() {
   6. // DelegatorAbility完成特定操作后，调用revokeDelegator回到首个UIAbility
   7. this.context.revokeDelegator().then(() => {
   8. console.info('revokeDelegator success');
   9. }).catch((err: BusinessError) => {
   10. console.error(`revokeDelegator failed, code is ${err.code}, message is ${err.message}`);
   11. });
   12. }
   13. }
   ```

### setColorMode18+

PhonePC/2in1TabletTVWearable

setColorMode(colorMode: ConfigurationConstant.ColorMode): void

设置UIAbility的深浅色模式。调用该接口前需要保证该UIAbility对应页面已完成加载。仅支持主线程调用。

说明

* 调用该接口前，需要确保窗口已完成创建、且UIAbility对应的页面已完成加载，即在[onWindowStageCreate()](js-apis-app-ability-uiability.md#onwindowstagecreate)生命周期中通过[loadContent](arkts-apis-window-windowstage.md#loadcontent9)方法加载页面之后调用。
* 调用该接口后会创建新的资源管理器对象，如果此前有缓存资源管理器，需要进行更新。
* 深浅色模式生效的优先级：UIAbility的深浅色模式 > 应用的深浅色模式（[ApplicationContext.setColorMode](js-apis-inner-application-applicationcontext.md#applicationcontextsetcolormode11)）> 系统的深浅色模式。

**元服务API**：从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorMode | [ConfigurationConstant.ColorMode](js-apis-app-ability-configurationconstant.md) | 是 | 设置颜色模式，包括:  - COLOR\_MODE\_DARK：深色模式  - COLOR\_MODE\_LIGHT：浅色模式  - COLOR\_MODE\_NOT\_SET：不设置（跟随系统或应用） |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |

**示例**：

```
1. import { UIAbility, ConfigurationConstant } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';

5. export default class MyAbility extends UIAbility {
6. onWindowStageCreate(windowStage: window.WindowStage) {
7. windowStage.loadContent('pages/Index', (err, data) => {
8. if (err.code) {
9. hilog.error(0x0000, 'testTag', 'Failed to load the content.');
10. return;
11. }
12. let uiAbilityContext = this.context;
13. uiAbilityContext.setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
14. });
15. }
16. }
```

### startAppServiceExtensionAbility20+

PhonePC/2in1TabletTVWearable

startAppServiceExtensionAbility(want: Want): Promise<void>

启动[AppServiceExtensionAbility](js-apis-app-ability-appserviceextensionability.md)实例。使用Promise异步回调。

说明

该接口的调用方必须为[AppServiceExtensionAbility](js-apis-app-ability-appserviceextensionability.md)所属应用或者在AppServiceExtensionAbility支持的应用清单（即[extensionAbilities标签](../harmonyos-guides/module-configuration-file.md#extensionabilities标签)的appIdentifierAllowList属性）中的应用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动[AppServiceExtensionAbility](js-apis-app-ability-appserviceextensionability.md)的Want信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000200 | The caller is not in the appIdentifierAllowList of the target application. |

**示例：**

```
1. import { UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let want: Want = {
7. deviceId: '',
8. bundleName: 'com.example.myapplication',
9. abilityName: 'AppServiceExtensionAbility'
10. };

12. try {
13. this.context.startAppServiceExtensionAbility(want)
14. .then(() => {
15. // 执行正常业务
16. console.info('startAppServiceExtensionAbility succeed');
17. })
18. .catch((err: BusinessError) => {
19. // 处理业务逻辑错误
20. console.error(`startAppServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}`);
21. });
22. } catch (err) {
23. // 处理入参错误异常
24. let code = (err as BusinessError).code;
25. let message = (err as BusinessError).message;
26. console.error(`startAppServiceExtensionAbility failed, code is ${code}, message is ${message}`);
27. }
28. }
29. }
```

### stopAppServiceExtensionAbility20+

PhonePC/2in1TabletTVWearable

stopAppServiceExtensionAbility(want: Want): Promise<void>

停止[AppServiceExtensionAbility](js-apis-app-ability-appserviceextensionability.md)实例。使用Promise异步回调。

说明

该接口的调用方必须为[AppServiceExtensionAbility](js-apis-app-ability-appserviceextensionability.md)所属应用或者在AppServiceExtensionAbility支持的应用清单（即[extensionAbilities标签](../harmonyos-guides/module-configuration-file.md#extensionabilities标签)的appIdentifierAllowList属性）中的应用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 停止[AppServiceExtensionAbility](js-apis-app-ability-appserviceextensionability.md)的Want信息。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000200 | The caller is not in the appIdentifierAllowList of the target application. |

**示例：**

```
1. import { UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let want: Want = {
7. deviceId: '',
8. bundleName: 'com.example.myapplication',
9. abilityName: 'AppServiceExtensionAbility'
10. };

12. try {
13. this.context.stopAppServiceExtensionAbility(want)
14. .then(() => {
15. // 执行正常业务
16. console.info('stopAppServiceExtensionAbility succeed');
17. })
18. .catch((err: BusinessError) => {
19. // 处理业务逻辑错误
20. console.error(`stopAppServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}`);
21. });
22. } catch (err) {
23. // 处理入参错误异常
24. let code = (err as BusinessError).code;
25. let message = (err as BusinessError).message;
26. console.error(`stopAppServiceExtensionAbility failed, code is ${code}, message is ${message}`);
27. }
28. }
29. }
```

### connectAppServiceExtensionAbility20+

PhonePC/2in1TabletTVWearable

connectAppServiceExtensionAbility(want: Want, callback: ConnectOptions): number

将当前UIAbility连接到[AppServiceExtensionAbility](js-apis-app-ability-appserviceextensionability.md)。通过返回的proxy与AppServiceExtensionAbility进行通信，以使用AppServiceExtensionAbility对外提供的能力。仅支持在主线程调用。

说明

如果[AppServiceExtensionAbility](js-apis-app-ability-appserviceextensionability.md)实例未启动，该接口的调用方必须为AppServiceExtensionAbility所属应用或者在AppServiceExtensionAbility支持的应用清单（即[extensionAbilities标签](../harmonyos-guides/module-configuration-file.md#extensionabilities标签)的appIdentifierAllowList属性）中的应用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 连接[AppServiceExtensionAbility](js-apis-app-ability-appserviceextensionability.md)的Want信息。 |
| callback | [ConnectOptions](js-apis-inner-ability-connectoptions.md) | 是 | ConnectOptions类型的回调函数，返回服务连接成功、连接失败、断开的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回连接id，[disconnectAppServiceExtensionAbility](js-apis-inner-application-uiabilitycontext.md#disconnectappserviceextensionability20)根据该连接id断开连接。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |
| 16000201 | The target service has not been started yet. |

**示例：**

```
1. import { UIAbility, Want, common } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onForeground() {
7. let want: Want = {
8. deviceId: '',
9. bundleName: 'com.example.myapplication',
10. abilityName: 'AppServiceExtensionAbility'
11. };
12. let commRemote: rpc.IRemoteObject;
13. let callback: common.ConnectOptions = {
14. onConnect(elementName, remote) {
15. commRemote = remote;
16. console.info('onConnect...');
17. },
18. onDisconnect(elementName) {
19. console.info('onDisconnect...');
20. },
21. onFailed(code) {
22. console.info('onFailed...');
23. }
24. };
25. let connection: number;

27. try {
28. connection = this.context.connectAppServiceExtensionAbility(want, callback);
29. } catch (err) {
30. // 处理入参错误异常
31. let code = (err as BusinessError).code;
32. let message = (err as BusinessError).message;
33. console.error(`connectAppServiceExtensionAbility failed, code is ${code}, message is ${message}`);
34. }
35. }
36. }
```

### disconnectAppServiceExtensionAbility20+

PhonePC/2in1TabletTVWearable

disconnectAppServiceExtensionAbility(connection: number): Promise<void>

断开与[AppServiceExtensionAbility](js-apis-app-ability-appserviceextensionability.md)的连接。仅支持在主线程调用。使用Promise异步回调。

断开连接之后，为了防止使用可能失效的remote对象进行通信，建议将连接成功时返回的remote对象设置为null。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 在[connectAppServiceExtensionAbility](js-apis-inner-application-uiabilitycontext.md#connectappserviceextensionability20)返回的连接id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onForeground() {
7. // connection为connectAppServiceExtensionAbility中的返回值
8. let connection = 1;
9. let commRemote: rpc.IRemoteObject | null;

11. try {
12. this.context.disconnectAppServiceExtensionAbility(connection).then(() => {
13. commRemote = null;
14. // 执行正常业务
15. console.info('disconnectAppServiceExtensionAbility succeed');
16. }).catch((err: BusinessError) => {
17. // 处理业务逻辑错误
18. console.error(`disconnectAppServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}`);
19. });
20. } catch (err) {
21. commRemote = null;
22. // 处理入参错误异常
23. let code = (err as BusinessError).code;
24. let message = (err as BusinessError).message;
25. console.error(`disconnectAppServiceExtensionAbility failed, code is ${code}, message is ${message}`);
26. }
27. }
28. }
```

### setOnNewWantSkipScenarios20+

PhonePC/2in1TabletTVWearable

setOnNewWantSkipScenarios(scenarios: number): Promise<void>

在特定场景下拉起UIAbility时，如果不需要触发[onNewWant](js-apis-app-ability-uiability.md#onnewwant)生命周期回调，可以通过该接口设置。仅支持在主线程调用。使用Promise异步回调。

说明

该接口通常用于[onCreate](js-apis-app-ability-uiability.md#oncreate)生命周期回调中。入参取值建议包含所有的[Scenarios](js-apis-app-ability-contextconstant.md#scenarios20)枚举值。详见下方示例代码。

**元服务API**：从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scenarios | number | 是 | 取值范围请参考[Scenarios](js-apis-app-ability-contextconstant.md#scenarios20)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. Possible causes: Connection to service failed. |

**示例：**

```
1. import { AbilityConstant, contextConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
6. let scenarios: number = contextConstant.Scenarios.SCENARIO_MOVE_MISSION_TO_FRONT |
7. contextConstant.Scenarios.SCENARIO_SHOW_ABILITY |
8. contextConstant.Scenarios.SCENARIO_BACK_TO_CALLER_ABILITY_WITH_RESULT;

10. try {
11. this.context.setOnNewWantSkipScenarios(scenarios).then(() => {
12. // 执行正常业务
13. console.info('setOnNewWantSkipScenarios succeed');
14. }).catch((err: BusinessError) => {
15. // 处理业务逻辑错误
16. console.error(`setOnNewWantSkipScenarios failed, code is ${err.code}, message is ${err.message}`);
17. });
18. } catch (err) {
19. // 处理入参错误异常
20. let code = (err as BusinessError).code;
21. let message = (err as BusinessError).message;
22. console.error(`setOnNewWantSkipScenarios failed, code is ${code}, message is ${message}`);
23. }
24. }
25. }
```

### startSelfUIAbilityInCurrentProcess22+

PhonePC/2in1TabletTVWearable

startSelfUIAbilityInCurrentProcess(want: Want, specifiedFlag: string, options?: StartOptions): Promise<void>

在当前进程中启动应用程序自己的UIAbility。

说明

* 只能冷启动目标UIAbility，如果目标UIAbility实例已经启动过，则启动失败。
* 通过该接口启动的UIAbility实例，将运行在调用方所在的进程中。其他关于目标UIAbility的进程相关的策略（例如在[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中通过isolationProcess或isolationMode字段来指定进程），均不会生效。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：

* 从API version 23开始，该接口仅在PC/2in1和Tablet设备中可正常调用，在其他设备中返回801错误码。
* 从API version 22开始，该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动Ability的必要信息。只支持[显式启动](../harmonyos-guides/explicit-implicit-want-mappings.md#显式want匹配原理)，不支持[隐式启动](../harmonyos-guides/explicit-implicit-want-mappings.md#隐式want匹配原理)。 |
| specifiedFlag | string | 是 | 开发者自定义的UIAbility标识。该标识不能与已启动的UIAbility标识相同，否则将返回错误。  **说明：**  当通过该接口拉起启动模式为[specified](../harmonyos-guides/uiability-launch-type.md#specified启动模式)的UIAbility时，将不会触发[onAcceptWant](js-apis-app-ability-abilitystage.md#onacceptwant)回调。 |
| options | [StartOptions](js-apis-app-ability-startoptions.md) | 否 | 启动Ability所携带的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000001 | The specified ability does not exist. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. Connect to system service failed. |
| 16000053 | The ability is not on the top of the UI. |
| 16000122 | The target component is blocked by the system module and does not support startup. |
| 16000123 | Implicit startup is not supported. |
| 16000124 | Starting a remote UIAbility is not supported. |
| 16000130 | The UIAbility not belong to caller. |
| 16000131 | The UIAbility is already exist, can not start again. |

**示例：**

```
1. import { UIAbility, StartOptions, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onForeground() {
6. let want: Want = {
7. deviceId: '',
8. bundleName: 'com.example.myapplication',
9. abilityName: 'EntryAbility'
10. };
11. let accountId = 100;
12. let options: StartOptions = {
13. displayId: 0
14. };

16. let instanceFlag = 'instance1';

18. try {
19. this.context.startSelfUIAbilityInCurrentProcess(want, instanceFlag, options);
20. } catch (err) {
21. // 处理入参错误异常
22. let code = (err as BusinessError).code;
23. let message = (err as BusinessError).message;
24. console.error(`startSelfUIAbilityInCurrentProcess failed, code is ${code}, message is ${message}`);
25. }
26. }
27. }
```

### restartApp22+

PhonePC/2in1TabletTVWearable

restartApp(want: Want): Promise<void>

处于获焦状态的UIAbility可以通过该接口，重启当前UIAbility所在的进程，并拉起应用内的指定UIAbility。仅支持主线程调用。使用Promise异步回调。

如果指定UIAbility就是当前UIAbility，则会刷新窗口至初始状态；如果是其他UIAbility，则会跳转并打开新的UIAbility窗口。

说明

通过该接口重启进程时，不会触发进程中Ability的onDestroy生命周期回调。

在元服务调用本接口成功后的3秒内，再次调用本接口、[restartSelfAtomicService()](js-apis-app-ability-abilitymanager.md#abilitymanagerrestartselfatomicservice20)或[ApplicationContext.restartApp()](js-apis-inner-application-applicationcontext.md#applicationcontextrestartapp12)接口中的任一接口，系统将返回错误码16000064。

在应用调用本接口成功后的3秒内，若再次调用本接口或[ApplicationContext.restartApp()](js-apis-inner-application-applicationcontext.md#applicationcontextrestartapp12)接口中的任一接口，系统将返回错误码16000064。

**元服务API**：从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在Phone设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | Want类型参数，传入需要启动的UIAbility的信息，校验bundleName、abilityName。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000011 | The context does not exist. |
| 16000050 | Connect to system server error. |
| 16000063 | The target to restart does not belong to the caller or is not a UIAbility. |
| 16000064 | Restart too frequently. |
| 16000065 | The API can be called only when the ability is focused. |

**示例：**

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. import { common, Want } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'restartApp with window';

9. build() {
10. RelativeContainer() {
11. Text(this.message)
12. .id('HelloWorld')
13. .fontSize($r('app.float.page_text_font_size'))
14. .fontWeight(FontWeight.Bold)
15. .alignRules({
16. center: { anchor: '__container__', align: VerticalAlign.Center },
17. middle: { anchor: '__container__', align: HorizontalAlign.Center }
18. })
19. .onClick(async () => {
20. let want: Want = {
21. bundleName: 'com.example.myapplication',
22. abilityName: 'EntryAbility'
23. };
24. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
25. try {
26. await context.restartApp(want);
27. } catch (err) {
28. hilog.error(0x0000, 'testTag', `restart failed: ${err.code}, ${err.message}`);
29. }
30. })
31. }
32. .height('100%')
33. .width('100%')
34. }
35. }
```

### setMissionWindowIcon22+

PhonePC/2in1TabletTVWearable

setMissionWindowIcon(windowIcon: image.PixelMap): Promise<void>

设置当前UIAbility在应用窗口、任务中心应用卡片、快捷栏窗口快照的图标。使用Promise异步回调。

说明

setMissionWindowIcon和[setAbilityInstanceInfo](js-apis-inner-application-uiabilitycontext.md#setabilityinstanceinfo15)之间不存在调用优先级关系。当多个接口被依次调用时，后一次调用的接口所设置的图标信息将覆盖之前调用接口所设置的内容，最终生效的图标以最后一次调用的接口为准。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口仅在PC/2in1设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowIcon | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 在应用窗口、任务中心应用卡片、快捷栏窗口快照显示的Ability图标。图标必须为正方形，且大小不能超过128M，否则返回401参数错误。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000050 | Internal error. 1. Connect to system service failed; 2.System service failed to communicate with dependency module. |
| 16000135 | The main window of this ability not exist. |

**示例：**

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class EntryAbility extends UIAbility {
6. onForeground() {
7. let imagePixelMap: image.PixelMap;
8. let color = new ArrayBuffer(1024 * 1024 * 4); // 创建一个ArrayBuffer对象，用于存储图像像素。该对象的大小为（height * width * 4）字节。
9. let bufferArr = new Uint8Array(color);
10. for (let i = 0; i < bufferArr.length; i += 4) {
11. bufferArr[i] = 255;
12. bufferArr[i+1] = 0;
13. bufferArr[i+2] = 122;
14. bufferArr[i+3] = 255;
15. }
16. image.createPixelMap(color, {
17. editable: true, pixelFormat: image.PixelMapFormat.RGBA_8888, size: { height: 1024, width: 1024 }
18. }).then((data) => {
19. imagePixelMap = data;
20. this.context.setMissionWindowIcon(imagePixelMap)
21. .then(() => {
22. console.info('setMissionWindowIcon succeed');
23. })
24. .catch((err: BusinessError) => {
25. console.error(`setMissionWindowIcon failed, code is ${err.code}, message is ${err.message}`);
26. });
27. }).catch((err: BusinessError) => {
28. console.error(`createPixelMap failed, code is ${err.code}, message is ${err.message}`);
29. });
30. }
31. }
```
