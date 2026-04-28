---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-application-uiextensioncontext
title: UIExtensionContext
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > UIExtensionContext
category: harmonyos-references
scraped_at: 2026-04-28T07:58:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7cc33285a4a5f60ea85bbc19780a41d8bf97b3de28210aad0b76d40ddfe58e1d
---

UIExtensionContext是[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)，提供[UIExtensionAbility](js-apis-app-ability-uiextensionability.md)的相关配置信息以及操作[UIAbility](js-apis-app-ability-uiability.md)的方法，如启动[UIAbility](js-apis-app-ability-uiability.md)等。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 本模块接口需要在主线程中使用，不要在Worker、TaskPool等子线程中使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## UIExtensionContext

PhonePC/2in1TabletTVWearable

### startAbility

PhonePC/2in1TabletTVWearable

startAbility(want: Want, callback: AsyncCallback<void>): void

启动一个UIAbility。使用callback异步回调。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当启动UIAbility成功时，err为undefined，否则为错误对象。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility, Want } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {

7. onForeground() {
8. let want: Want = {
9. bundleName: 'com.example.myapplication',
10. abilityName: 'EntryAbility'
11. };

13. try {
14. this.context.startAbility(want, (err: BusinessError) => {
15. if (err.code) {
16. // 处理业务逻辑错误
17. console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
18. return;
19. }
20. // 执行正常业务
21. console.info('startAbility succeed');
22. });
23. } catch (err) {
24. // 处理入参错误异常
25. let code = (err as BusinessError).code;
26. let message = (err as BusinessError).message;
27. console.error(`startAbility failed, code is ${code}, message is ${message}`);
28. }
29. }
30. }
```

### startAbility

PhonePC/2in1TabletTVWearable

startAbility(want: Want, options: StartOptions, callback: AsyncCallback<void>): void

启动一个UIAbility。使用callback异步回调。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| options | [StartOptions](js-apis-app-ability-startoptions.md) | 是 | 启动UIAbility所携带的额外参数。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当启动UIAbility成功时，err为undefined，否则为错误对象。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility, Want, StartOptions } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. onForeground() {
7. let want: Want = {
8. deviceId: '',
9. bundleName: 'com.example.myapplication',
10. abilityName: 'EntryAbility'
11. };
12. let options: StartOptions = {
13. displayId: 0
14. };

16. try {
17. this.context.startAbility(want, options, (err: BusinessError) => {
18. if (err.code) {
19. // 处理业务逻辑错误
20. console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
21. return;
22. }
23. // 执行正常业务
24. console.info('startAbility succeed');
25. });
26. } catch (err) {
27. // 处理入参错误异常
28. let code = (err as BusinessError).code;
29. let message = (err as BusinessError).message;
30. console.error(`startAbility failed, code is ${code}, message is ${message}`);
31. }
32. }
33. }
```

### startAbility

PhonePC/2in1TabletTVWearable

startAbility(want: Want, options?: StartOptions): Promise<void>

启动一个UIAbility。使用Promise异步回调。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| options | [StartOptions](js-apis-app-ability-startoptions.md) | 否 | 启动UIAbility所携带的额外参数。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility, Want, StartOptions } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. onForeground() {
7. let want: Want = {
8. bundleName: 'com.example.myapplication',
9. abilityName: 'EntryAbility'
10. };
11. let options: StartOptions = {
12. displayId: 0,
13. };

15. try {
16. this.context.startAbility(want, options)
17. .then(() => {
18. // 执行正常业务
19. console.info('startAbility succeed');
20. })
21. .catch((err: BusinessError) => {
22. // 处理业务逻辑错误
23. console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
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

### startAbilityForResult

PhonePC/2in1TabletTVWearable

startAbilityForResult(want: Want, callback: AsyncCallback<AbilityResult>): void

启动一个UIAbility，开发者可以通过回调函数接收被拉起的UIAbility退出时的返回结果。使用callback异步回调。UIAbility被启动后，有如下情况:

* 正常情况下可通过调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口使之终止并且返回结果给调用方。
* 异常情况下比如杀死UIAbility会返回异常信息给调用方, 异常信息中resultCode为-1。
* 如果被启动的UIAbility模式是单实例模式, 不同应用多次调用该接口启动这个UIAbility，当这个UIAbility调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| callback | AsyncCallback<[AbilityResult](js-apis-inner-ability-abilityresult.md)> | 是 | 回调函数，包含返回给拉起方的信息。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. onForeground() {
7. let want: Want = {
8. deviceId: '',
9. bundleName: 'com.example.myapplication',
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

启动一个UIAbility，开发者可以通过回调函数接收被拉起的UIAbility退出时的返回结果。使用callback异步回调。UIAbility被启动后，有如下情况:

* 正常情况下可通过调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口使之终止并且返回结果给调用方。
* 异常情况下比如杀死UIAbility会返回异常信息给调用方，异常信息中resultCode为-1。
* 如果被启动的UIAbility模式是单实例模式, 不同应用多次调用该接口启动这个UIAbility，当这个UIAbility调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口使之终止时，只将正常结果返回给最后一个调用方，其它调用方返回异常信息, 异常信息中resultCode为-1。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| options | [StartOptions](js-apis-app-ability-startoptions.md) | 是 | 启动UIAbility所携带的额外参数。 |
| callback | AsyncCallback<[AbilityResult](js-apis-inner-ability-abilityresult.md)> | 是 | 回调函数，包含返回给拉起方的信息。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility, Want, common, StartOptions } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. onForeground() {
7. let want: Want = {
8. deviceId: '',
9. bundleName: 'com.example.myapplication',
10. abilityName: 'EntryAbility'
11. };
12. let options: StartOptions = {
13. displayId: 0,
14. };

16. try {
17. this.context.startAbilityForResult(want, options, (err: BusinessError, result: common.AbilityResult) => {
18. if (err.code) {
19. // 处理业务逻辑错误
20. console.error(`startAbilityForResult failed, code is ${err.code}, message is ${err.message}`);
21. return;
22. }
23. // 执行正常业务
24. console.info('startAbilityForResult succeed');
25. });
26. } catch (err) {
27. // 处理入参错误异常
28. let code = (err as BusinessError).code;
29. let message = (err as BusinessError).message;
30. console.error(`startAbilityForResult failed, code is ${code}, message is ${message}`);
31. }
32. }
33. }
```

### startAbilityForResult

PhonePC/2in1TabletTVWearable

startAbilityForResult(want: Want, options?: StartOptions): Promise<AbilityResult>

启动一个UIAbility，开发者可以通过回调函数接收被拉起的UIAbility退出时的返回结果。使用Promise异步回调。UIAbility被启动后，有如下情况:

* 正常情况下可通过调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口使之终止并且返回结果给调用方。
* 异常情况下比如杀死UIAbility会返回异常信息给调用方, 异常信息中resultCode为-1。
* 如果被启动的UIAbility模式是单实例模式, 不同应用多次调用该接口启动这个UIAbility，当这个UIAbility调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息, 异常信息中resultCode为-1。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UIAbility时必要的Want，包含待启动UIAbility的名称等信息。 |
| options | [StartOptions](js-apis-app-ability-startoptions.md) | 否 | 启动UIAbility所携带的额外参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AbilityResult](js-apis-inner-ability-abilityresult.md)> | Promise对象，返回被拉起的UIAbility退出时的返回结果。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16000070 | The extension cannot start the service. |
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
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility, Want, common, StartOptions } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. onForeground() {
7. let want: Want = {
8. bundleName: 'com.example.myapplication',
9. abilityName: 'EntryAbility'
10. };
11. let options: StartOptions = {
12. displayId: 0,
13. };

15. try {
16. this.context.startAbilityForResult(want, options)
17. .then((result: common.AbilityResult) => {
18. // 执行正常业务
19. console.info('startAbilityForResult succeed');
20. })
21. .catch((err: BusinessError) => {
22. // 处理业务逻辑错误
23. console.error(`startAbilityForResult failed, code is ${err.code}, message is ${err.message}`);
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

### connectServiceExtensionAbility

PhonePC/2in1TabletTVWearable

connectServiceExtensionAbility(want: Want, options: ConnectOptions): number

将当前UIExtensionAbility连接到一个ServiceExtensionAbility，通过返回的proxy与ServiceExtensionAbility进行通信，以使用ServiceExtensionAbility对外提供的能力。

ServiceExtensionAbility是一类特殊的[ExtensionAbility](../harmonyos-guides/extensionability-overview.md)组件，这类组件由系统提供，通常用于提供指定场景后台服务能力，不支持开发者自定义。ServiceExtensionAbility可以被其他组件连接，并根据调用者的请求信息在后台处理相关事务。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 连接ServiceExtensionAbility的Want信息，包括Ability名称，Bundle名称等。 |
| options | [ConnectOptions](js-apis-inner-ability-connectoptions.md) | 是 | ConnectOptions类型的回调函数，返回服务连接成功、连接失败、断开的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回连接id，客户端可以通过[disconnectServiceExtensionAbility](js-apis-inner-application-uiextensioncontext.md#disconnectserviceextensionability)传入该连接id来断开连接。 |

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
| 16000070 | The extension cannot start the service. |

**示例：**

```
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class ShareExtAbility extends ShareExtensionAbility {
7. onForeground() {
8. let want: Want = {
9. deviceId: '',
10. bundleName: 'com.example.myapplication',
11. abilityName: 'ServiceExtensionAbility'
12. };
13. let commRemote: rpc.IRemoteObject;
14. let options: common.ConnectOptions = {
15. onConnect(elementName, remote) {
16. commRemote = remote;
17. console.info('onConnect...');
18. },
19. onDisconnect(elementName) {
20. console.info('onDisconnect...');
21. },
22. onFailed(code) {
23. console.error(`onFailed, err code: ${code}.`);
24. }
25. };
26. let connection: number;
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

断开与ServiceExtensionAbility的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用Promise异步回调。

ServiceExtensionAbility是一类特殊的[ExtensionAbility](../harmonyos-guides/extensionability-overview.md)组件，这类组件由系统提供，通常用于提供指定场景后台服务能力，不支持开发者自定义。ServiceExtensionAbility可以被其他组件连接，并根据调用者的请求信息在后台处理相关事务。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 连接的ServiceExtensionAbility的标识Id，即[connectServiceExtensionAbility](js-apis-inner-application-uiextensioncontext.md#connectserviceextensionability)返回的connectionId。 |

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
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class ShareExtAbility extends ShareExtensionAbility {
7. onForeground() {
8. // connection为connectServiceExtensionAbility中的返回值
9. let connection = 1;
10. let commRemote: rpc.IRemoteObject | null;

12. try {
13. this.context.disconnectServiceExtensionAbility(connection).then(() => {
14. commRemote = null;
15. // 执行正常业务
16. console.info('disconnectServiceExtensionAbility succeed');
17. }).catch((err: BusinessError) => {
18. // 处理业务逻辑错误
19. console.error(`disconnectServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}`);
20. })
21. } catch (err) {
22. commRemote = null;
23. // 处理入参错误异常
24. let code = (err as BusinessError).code;
25. let message = (err as BusinessError).message;
26. console.error(`disconnectServiceExtensionAbility failed, code is ${code}, message is ${message}`);
27. }
28. }
29. }
```

### disconnectServiceExtensionAbility

PhonePC/2in1TabletTVWearable

disconnectServiceExtensionAbility(connection: number, callback: AsyncCallback<void>): void

断开与ServiceExtensionAbility的连接，断开连接之后开发者需要将连接成功时返回的remote对象置空。使用callback异步回调。

ServiceExtensionAbility是一类特殊的[ExtensionAbility](../harmonyos-guides/extensionability-overview.md)组件，这类组件由系统提供，通常用于提供指定场景后台服务能力，不支持开发者自定义。ServiceExtensionAbility可以被其他组件连接，并根据调用者的请求信息在后台处理相关事务。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 连接的ServiceExtensionAbility的标识Id，即connectServiceExtensionAbility返回的connectionId。 |
| callback | AsyncCallback<void> | 是 | 回调函数。当断开与ServiceExtensionAbility的连接成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility } from '@kit.AbilityKit';
3. import { rpc } from '@kit.IPCKit';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class ShareExtAbility extends ShareExtensionAbility {
7. onForeground() {
8. // connection为connectServiceExtensionAbility中的返回值
9. let connection = 1;
10. let commRemote: rpc.IRemoteObject | null;

12. try {
13. this.context.disconnectServiceExtensionAbility(connection, (err: BusinessError) => {
14. commRemote = null;
15. if (err.code) {
16. // 处理业务逻辑错误
17. console.error(`disconnectServiceExtensionAbility failed, code is ${err.code}, message is ${err.message}`);
18. return;
19. }
20. // 执行正常业务
21. console.info('disconnectServiceExtensionAbility succeed');
22. });
23. } catch (err) {
24. commRemote = null;
25. // 处理入参错误异常
26. let code = (err as BusinessError).code;
27. let message = (err as BusinessError).message;
28. console.error(`disconnectServiceExtensionAbility failed, code is ${code}, message is ${message}`);
29. }
30. }
31. }
```

### terminateSelf12+

PhonePC/2in1TabletTVWearable

terminateSelf(callback: AsyncCallback<void>): void

销毁UIExtensionAbility自身，同时关闭对应的窗口界面。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。UIExtensionAbility停止成功时，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. onForeground() {
7. try {
8. this.context.terminateSelf((err: BusinessError) => {
9. if (err.code) {
10. // 处理业务逻辑错误
11. console.error(`terminateSelf failed, code is ${err.code}, message is ${err.message}`);
12. return;
13. }
14. // 执行正常业务
15. console.info('terminateSelf succeed');
16. });
17. } catch (err) {
18. // 捕获同步的参数错误
19. let code = (err as BusinessError).code;
20. let message = (err as BusinessError).message;
21. console.error(`terminateSelf failed, code is ${code}, message is ${message}`);
22. }
23. }
24. }
```

### terminateSelf12+

PhonePC/2in1TabletTVWearable

terminateSelf(): Promise<void>

销毁UIExtensionAbility自身，同时关闭对应的窗口界面。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. onForeground() {
7. try {
8. this.context.terminateSelf()
9. .then(() => {
10. // 执行正常业务
11. console.info('terminateSelf succeed');
12. })
13. .catch((err: BusinessError) => {
14. // 处理业务逻辑错误
15. console.error(`terminateSelf failed, code is ${err.code}, message is ${err.message}`);
16. });
17. } catch (err) {
18. // 捕获同步的参数错误
19. let code = (err as BusinessError).code;
20. let message = (err as BusinessError).message;
21. console.error(`terminateSelf failed, code is ${code}, message is ${message}`);
22. }
23. }
24. }
```

### terminateSelfWithResult12+

PhonePC/2in1TabletTVWearable

terminateSelfWithResult(parameter: AbilityResult, callback: AsyncCallback<void>): void

销毁UIExtensionAbility自身，同时关闭对应的窗口界面，并将结果返回给UIExtensionAbility的拉起方，拉起方通常为系统服务。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [AbilityResult](js-apis-inner-ability-abilityresult.md) | 是 | 返回给UIExtensionAbility拉起方的信息。 |
| callback | AsyncCallback<void> | 是 | 回调函数。UIExtensionAbility停止成功时，err为undefined，否则为错误对象。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. onForeground() {
7. let want: Want = {
8. bundleName: 'com.example.myapplication',
9. abilityName: 'EntryAbility'
10. };
11. let resultCode = 100;
12. // 返回给接口调用方AbilityResult信息
13. let abilityResult: common.AbilityResult = {
14. want,
15. resultCode
16. };

18. try {
19. this.context.terminateSelfWithResult(abilityResult, (err: BusinessError) => {
20. if (err.code) {
21. // 处理业务逻辑错误
22. console.error(`terminateSelfWithResult failed, code is ${err.code}, message is ${err.message}`);
23. return;
24. }
25. // 执行正常业务
26. console.info('terminateSelfWithResult succeed');
27. });
28. } catch (err) {
29. // 处理入参错误异常
30. let code = (err as BusinessError).code;
31. let message = (err as BusinessError).message;
32. console.error(`terminateSelfWithResult failed, code is ${code}, message is ${message}`);
33. }
34. }
35. }
```

### terminateSelfWithResult12+

PhonePC/2in1TabletTVWearable

terminateSelfWithResult(parameter: AbilityResult): Promise<void>

销毁UIExtensionAbility自身，同时关闭对应的窗口界面，并将结果返回给UIExtensionAbility的拉起方，拉起方通常为系统服务。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| parameter | [AbilityResult](js-apis-inner-ability-abilityresult.md) | 是 | 返回给UIExtensionAbility拉起方的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码**：

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

```
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility, Want, common } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. onForeground() {
7. let want: Want = {
8. bundleName: 'com.example.myapplication',
9. abilityName: 'EntryAbility'
10. };
11. let resultCode = 100;
12. // 返回给接口调用方AbilityResult信息
13. let abilityResult: common.AbilityResult = {
14. want,
15. resultCode
16. };

18. try {
19. this.context.terminateSelfWithResult(abilityResult)
20. .then(() => {
21. // 执行正常业务
22. console.info('terminateSelfWithResult succeed');
23. })
24. .catch((err: BusinessError) => {
25. // 处理业务逻辑错误
26. console.error(`terminateSelfWithResult failed, code is ${err.code}, message is ${err.message}`);
27. });
28. } catch (err) {
29. // 处理入参错误异常
30. let code = (err as BusinessError).code;
31. let message = (err as BusinessError).message;
32. console.error(`terminateSelfWithResult failed, code is ${code}, message is ${message}`);
33. }
34. }
35. }
```

### reportDrawnCompleted12+

PhonePC/2in1TabletTVWearable

reportDrawnCompleted(callback: AsyncCallback<void>): void

用于应用通知系统UIExtensionAbility对应的窗口内容已绘制完成。系统会根据开发者调用的时机进行资源分配优化等，以优化应用启动及显示时间。使用callback异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<void> | 是 | 回调函数。当打点成功，err为undefined，否则为错误对象。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility, Want, UIExtensionContentSession } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. const TAG: string = '[testTag] ShareExtAbility';

7. export default class ShareExtAbility extends ShareExtensionAbility {
8. onSessionCreate(want: Want, session: UIExtensionContentSession) {
9. console.info(TAG, `onSessionCreate, want: ${JSON.stringify(want)}`);
10. let data: Record<string, UIExtensionContentSession> = {
11. 'session': session
12. };
13. let storage: LocalStorage = new LocalStorage(data);
14. session.loadContent('pages/extension', storage);
15. try {
16. this.context.reportDrawnCompleted((err) => {
17. if (err.code) {
18. // 处理业务逻辑错误
19. console.error(`reportDrawnCompleted failed, code is ${err.code}, message is ${err.message}`);
20. return;
21. }
22. // 执行正常业务
23. console.info('reportDrawnCompleted succeed');
24. });
25. } catch (err) {
26. // 捕获同步的参数错误
27. let code = (err as BusinessError).code;
28. let message = (err as BusinessError).message;
29. console.error(`reportDrawnCompleted failed, code is ${code}, message is ${message}`);
30. }
31. }
32. }
```

### openAtomicService12+

PhonePC/2in1TabletTVWearable

openAtomicService(appId: string, options?: AtomicServiceOptions): Promise<AbilityResult>

打开一个独立窗口的元服务，并返回结果。使用Promise异步回调。

分为以下几种情况：

* 正常情况下可通过调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口使之终止并且返回结果给调用方。
* 异常情况下比如杀死元服务会返回异常信息给调用方，异常信息中resultCode为-1。
* 如果不同应用多次调用该接口启动同一个元服务，当这个元服务调用[terminateSelfWithResult](js-apis-inner-application-uiabilitycontext.md#terminateselfwithresult)接口使之终止时，只将正常结果返回给最后一个调用方, 其它调用方返回异常信息，异常信息中resultCode为-1。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| appId | string | 是 | 应用的唯一标识，由云端统一分配。 |
| options | [AtomicServiceOptions](js-apis-app-ability-atomicserviceoptions.md) | 否 | 启动元服务所携带的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[AbilityResult](js-apis-inner-ability-abilityresult.md)> | Promise对象。返回给拉起方的信息。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16200001 | The caller has been released. |

**示例：**

```
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility, common, AtomicServiceOptions } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. onForeground() {
7. let appId: string = '6918661953712445909';
8. let options: AtomicServiceOptions = {
9. displayId: 0,
10. };

12. try {
13. this.context.openAtomicService(appId, options)
14. .then((result: common.AbilityResult) => {
15. // 执行正常业务
16. console.info('openAtomicService succeed');
17. })
18. .catch((err: BusinessError) => {
19. // 处理业务逻辑错误
20. console.error(`openAtomicService failed, code is ${err.code}, message is ${err.message}`);
21. });
22. } catch (err) {
23. // 处理入参错误异常
24. let code = (err as BusinessError).code;
25. let message = (err as BusinessError).message;
26. console.error(`openAtomicService failed, code is ${code}, message is ${message}`);
27. }
28. }
29. }
```

### openLink12+

PhonePC/2in1TabletTVWearable

openLink(link: string, options?: OpenLinkOptions, callback?: AsyncCallback<AbilityResult>): Promise<void>

通过App Linking或Deep Linking方式启动UIAbility。使用Promise异步回调。

通过在link字段中传入标准格式的URL，基于隐式want匹配规则拉起目标UIAbility。目标方必须具备以下过滤器特征，才能处理App Linking链接：

* "actions"列表中包含"ohos.want.action.viewData"。
* "entities"列表中包含"entity.system.browsable"。
* "uris"列表中包含"scheme"为"https"且"domainVerify"为true的元素。

如果希望获取被拉起方终止后的结果，可以设置callback参数，此参数的使用可参照[startAbilityForResult](js-apis-inner-application-uiextensioncontext.md#startabilityforresult)接口。

传入的参数不合法时，如未设置必选参数或link字符串不是标准格式的URL，接口会直接抛出异常。参数校验通过，拉起目标方时出现的错误通过promise返回错误信息。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

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
| Promise<void> | 无返回结果的Promise对象。 |

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
| 16000069 | The extension cannot start the third party application. |
| 16200001 | The caller has been released. |
| 16000053 | The ability is not on the top of the UI. |
| 16000136 | The UIAbility is prohibited from launching itself via App Linking. |

**示例：**

```
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility, Want, UIExtensionContentSession, OpenLinkOptions } from '@kit.AbilityKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export default class ShareExtAbility extends ShareExtensionAbility {
6. onCreate() {
7. console.info(`UIExtAbility onCreate`);
8. }

10. onForeground() {
11. console.info(`UIExtAbility onForeground`);
12. }

14. onBackground() {
15. console.info(`UIExtAbility onBackground`);
16. }

18. onDestroy() {
19. console.info(`UIExtAbility onDestroy`);
20. }

22. onSessionCreate(want: Want, session: UIExtensionContentSession) {
23. console.info(`UIExtAbility onSessionCreate`);
24. console.info(`UIExtAbility onSessionCreate, want: ${JSON.stringify(want)}`);
25. let record: Record<string, UIExtensionContentSession> = {
26. 'session': session
27. };
28. let storage: LocalStorage = new LocalStorage(record);
29. session.loadContent('pages/UIExtensionIndex', storage);

31. let link: string = 'https://www.example.com';
32. let openLinkOptions: OpenLinkOptions = {
33. appLinkingOnly: true
34. };
35. try {
36. this.context.openLink(
37. link,
38. openLinkOptions,
39. (err, result) => {
40. if (err) {
41. console.error(`openLink callback failed, err code: ${err.code}, err msg: ${err.message}.`);
42. return;
43. }
44. console.info(`openLink success, result code: ${result.resultCode} result data: ${result.want}.`);
45. }
46. ).then(() => {
47. console.info(`open link success.`);
48. }).catch((err: BusinessError) => {
49. console.error(`open link failed, err code: ${err.code}, err msg: ${err.message}.`);
50. });
51. } catch (err) {
52. let code = (err as BusinessError).code;
53. let msg = (err as BusinessError).message;
54. console.error(`openLink failed, err code: ${code}, err msg: ${msg}.`);
55. }
56. }

58. onSessionDestroy(session: UIExtensionContentSession) {
59. console.info(`UIExtAbility onSessionDestroy`);
60. }
61. }
```

### startUIServiceExtensionAbility14+

PhonePC/2in1TabletTVWearable

startUIServiceExtensionAbility(want: Want): Promise<void>

启动一个UIServiceExtensionAbility。使用Promise异步回调。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 启动UIServiceExtensionAbility的Want。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

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
14. let context = this.getUIContext().getHostContext() as common.UIExtensionContext;
15. let startWant: Want = {
16. bundleName: 'com.acts.uiserviceextensionability',
17. abilityName: 'UiServiceExtAbility',
18. };
19. try {
20. // 启动UIServiceExtensionAbility
21. context.startUIServiceExtensionAbility(startWant).then(() => {
22. console.info(`startUIServiceExtensionAbility success.`);
23. }).catch((error: BusinessError) => {
24. console.error(`startUIServiceExtensionAbility failed, err code: ${error.code}, err msg: ${error.message}.`);
25. })
26. } catch (err) {
27. let code = (err as BusinessError).code;
28. let msg = (err as BusinessError).message;
29. console.error(`startUIServiceExtensionAbility failed, err code: ${code}, err msg: ${msg}.`);
30. }
31. })
32. }
33. }
34. }
35. }
```

### connectUIServiceExtensionAbility14+

PhonePC/2in1TabletTVWearable

connectUIServiceExtensionAbility(want: Want, callback: UIServiceExtensionConnectCallback) : Promise<UIServiceProxy>

连接到一个UIServiceExtensionAbility。使用Promise异步回调。

说明

组件启动规则详见：[组件启动规则（Stage模型）](../harmonyos-guides/component-startup-rules.md)。

**需要权限**：ohos.permission.START\_INVISIBLE\_ABILITY

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | Want | 是 | 用于连接的Want信息。 |
| callback | [UIServiceExtensionConnectCallback](nner-application-uiserviceextensionconnectcallback.md) | 是 | 连接UIServiceExtensionAbility回调。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<UIServiceProxy> | Promise对象，连接UIServiceExtensionAbility成功时，返回[UIServiceProxy](js-apis-inner-application-uiserviceproxy.md)对象，借助该对象可以往UIServiceExtensionAbility发送数据。 |

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
| 16000013 | The application is controlled by EDM. |
| 16000050 | Internal error. |
| 16000055 | Installation-free timed out. |

**示例：**

```
1. import { common, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Page_UIServiceExtensionAbility {
7. @State uiServiceProxy: common.UIServiceProxy | null = null;

9. build() {
10. Column() {
11. Row() {
12. // ...
13. }.onClick(() => {
14. const context = this.getUIContext().getHostContext() as common.UIExtensionContext;
15. const want: Want = {
16. deviceId: '',
17. bundleName: 'com.example.myapplication',
18. abilityName: ''
19. };
20. // 定义回调
21. const callback: common.UIServiceExtensionConnectCallback = {
22. onData: (data: Record<string, Object>): void => {
23. console.info(`onData, data: ${JSON.stringify(data)}.`);
24. },
25. onDisconnect: (): void => {
26. console.info(`onDisconnect`);
27. }
28. };
29. // 连接UIServiceExtensionAbility
30. context.connectUIServiceExtensionAbility(want, callback).then((uiServiceProxy: common.UIServiceProxy) => {
31. this.uiServiceProxy = uiServiceProxy;
32. console.info(`connectUIServiceExtensionAbility success`);
33. }).catch((error: BusinessError) => {
34. console.error(`connectUIServiceExtensionAbility failed, err code: ${error.code}, err msg: ${error.message}.`);
35. })
36. })
37. }
38. }
39. }
```

### disconnectUIServiceExtensionAbility14+

PhonePC/2in1TabletTVWearable

disconnectUIServiceExtensionAbility(proxy: UIServiceProxy): Promise<void>

断开UIServiceExtensionAbility。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| proxy | [UIServiceProxy](js-apis-inner-application-uiserviceproxy.md) | 是 | [connectUIServiceExtensionAbility](js-apis-inner-application-uiextensioncontext.md#connectuiserviceextensionability14)返回的Proxy。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

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

4. @Entry
5. @Component
6. struct Page_UIServiceExtensionAbility {
7. @State uiServiceProxy: common.UIServiceProxy | null = null;

9. build() {
10. Column() {
11. Row() {
12. // ...
13. }.onClick(() => {
14. const context = this.getUIContext().getHostContext() as common.UIExtensionContext;
15. // this.uiServiceProxy是连接时保存的proxy对象
16. context.disconnectUIServiceExtensionAbility(this.uiServiceProxy).then(() => {
17. console.info(`disconnectUIServiceExtensionAbility success.`);
18. }).catch((error: BusinessError) => {
19. console.error(`disconnectUIServiceExtensionAbility failed, err code: ${error.code}, err msg: ${error.message}.`);
20. })
21. })
22. }
23. }
24. }
```

### setColorMode18+

PhonePC/2in1TabletTVWearable

setColorMode(colorMode: ConfigurationConstant.ColorMode): void

设置UIExtensionAbility的深浅色模式。调用该接口前需要保证该UIExtensionContext对应页面已完成加载。仅支持主线程调用。

说明

* 调用该接口后会创建新的资源管理器对象，如果此前有缓存资源管理器，需要进行更新。
* 深浅色模式生效的优先级：UIExtensionAbility的深浅色模式 > 应用的深浅色模式（[ApplicationContext.setColorMode](js-apis-inner-application-applicationcontext.md#applicationcontextsetcolormode11)）> 系统的深浅色模式。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorMode | [ConfigurationConstant.ColorMode](js-apis-app-ability-configurationconstant.md#colormode) | 是 | 设置颜色模式，包括：  - COLOR\_MODE\_DARK：深色模式  - COLOR\_MODE\_LIGHT：浅色模式  - COLOR\_MODE\_NOT\_SET：不设置（跟随系统或应用） |

**错误码**：

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |

**示例**：

```
1. // UIExtensionAbility不支持三方应用直接继承，故以派生类ShareExtensionAbility举例说明。
2. import { ShareExtensionAbility, ConfigurationConstant } from '@kit.AbilityKit';

4. export default class MyAbility extends ShareExtensionAbility {
5. onForeground() {
6. let uiExtensionContext = this.context;
7. uiExtensionContext.setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_DARK);
8. }
9. }
```
