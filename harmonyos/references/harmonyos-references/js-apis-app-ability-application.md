---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-application
title: @ohos.app.ability.application (应用工具类)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.application (应用工具类)
category: harmonyos-references
scraped_at: 2026-04-29T13:48:26+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:a733c07725760ea67bb35db09c8c8deea6b6fb34014f38b47eda7a41306dc4ae
---

开发者可以通过该模块管理和获取应用的上下文[Context](../harmonyos-guides/application-context-stage.md)，以及控制应用进程的状态。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { application } from '@kit.AbilityKit';
```

## AppPreloadType22+

PhonePC/2in1TabletTVWearable

表示应用当前进程的预加载类型枚举。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNSPECIFIED | 0 | 未发生预加载或预加载数据已被清除。 |
| TYPE\_CREATE\_PROCESS | 1 | 进程最终预加载到进程创建完成阶段。 |
| TYPE\_CREATE\_ABILITY\_STAGE | 2 | 进程最终预加载到[AbilityStage](js-apis-app-ability-abilitystage.md)创建完成阶段。 |
| TYPE\_CREATE\_WINDOW\_STAGE | 3 | 进程最终预加载到[WindowStage](arkts-apis-window-windowstage.md)创建完成阶段。 |
| TYPE\_CREATE\_BACKGROUND\_ABILITY 23+ | 4 | 进程最终预加载到[onBackground](js-apis-app-ability-uiability.md#onbackground)执行完成阶段。 |

## application.createModuleContext

PhonePC/2in1TabletTVWearable

createModuleContext(context: Context, moduleName: string): Promise<Context>

创建指定模块的上下文。创建出的模块上下文中[resourceManager.Configuration](js-apis-resource-manager.md#configuration)资源继承自入参上下文，便于开发者获取[跨HAP/HSP包资源](../harmonyos-guides/resource-categories-and-access.md#访问跨haphsp包资源)。使用Promise异步回调。

说明

由于创建模块上下文的过程涉及资源查询与初始化，耗时相对较长，在对应用流畅性要求较高的场景下，不建议频繁或多次调用createModuleContext接口创建多个Context实例，以免影响用户体验。

**元服务API**：从API version 12开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 表示应用上下文。 |
| moduleName | string | 是 | 表示应用模块名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Context](js-apis-inner-application-context.md)> | Promise对象。返回创建的Context。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码说明文档](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |

**示例：**

```
1. import { AbilityConstant, UIAbility, application, common, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. let moduleContext: common.Context;
7. try {
8. application.createModuleContext(this.context, 'entry').then((data: Context) => {
9. moduleContext = data;
10. console.info('createModuleContext success!');
11. }).catch((error: BusinessError) => {
12. let code: number = (error as BusinessError).code;
13. let message: string = (error as BusinessError).message;
14. console.error(`createModuleContext failed, error.code: ${code}, error.message: ${message}`);
15. });
16. } catch (error) {
17. let code: number = (error as BusinessError).code;
18. let message: string = (error as BusinessError).message;
19. console.error(`createModuleContext failed, error.code: ${code}, error.message: ${message}`);
20. }
21. }
22. }
```

## application.getApplicationContext14+

PhonePC/2in1TabletTVWearable

getApplicationContext(): ApplicationContext

获取应用上下文。开发者使用该接口时，无需依赖Context基类。

重复调用该接口，将生成新的ApplicationContext对象。

**元服务API**：从API version 14开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ApplicationContext](js-apis-inner-application-applicationcontext.md) | 应用上下文。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. |

**示例：**

```
1. import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. let applicationContext = application.getApplicationContext();
8. } catch (error) {
9. let code: number = (error as BusinessError).code;
10. let message: string = (error as BusinessError).message;
11. console.error(`getApplicationContext failed, error.code: ${code}, error.message: ${message}`);
12. }
13. }
14. }
```

## application.getApplicationContextInstance23+

PhonePC/2in1TabletTVWearable

getApplicationContextInstance(): ApplicationContext

获取应用上下文。开发者使用该接口时，无需依赖Context基类。

重复调用该接口，将获取同一个ApplicationContext实例。

**元服务API**：从API version 23开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ApplicationContext](js-apis-inner-application-applicationcontext.md) | 应用上下文。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000050 | Internal error. Possible causes: Memory operation error. |

**示例：**

```
1. import { AbilityConstant, UIAbility, application, Want, common } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. let applicationContext: common.ApplicationContext = application.getApplicationContextInstance();
8. } catch (error) {
9. let code: number = (error as BusinessError).code;
10. let message: string = (error as BusinessError).message;
11. console.error(`getApplicationContextInstance failed, error.code: ${code}, error.message: ${message}`);
12. }
13. }
14. }
```

## application.createPluginModuleContext19+

PhonePC/2in1TabletTVWearable

createPluginModuleContext(context: Context, pluginBundleName: string, pluginModuleName: string): Promise<Context>

根据入参Context、指定的插件包名和插件模块名，创建本应用下插件的Context，用于获取插件的基本信息。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [Context](js-apis-inner-application-context.md) | 是 | 表示应用上下文。 |
| pluginBundleName | string | 是 | 表示应用的插件包名。 |
| pluginModuleName | string | 是 | 表示应用的插件模块名。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Context](js-apis-inner-application-context.md)> | Promise对象。返回创建的Context。 |

**示例：**

```
1. import { AbilityConstant, UIAbility, application, common, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. let moduleContext: common.Context;
7. try {
8. application.createPluginModuleContext(this.context, 'com.example.pluginBundleName', 'pluginModuleName')
9. .then((data: Context) => {
10. moduleContext = data;
11. console.info('createPluginModuleContext success!');
12. })
13. .catch((error: BusinessError) => {
14. let code: number = (error as BusinessError).code;
15. let message: string = (error as BusinessError).message;
16. console.error(`createPluginModuleContext failed, error.code: ${code}, error.message: ${message}`);
17. });
18. } catch (error) {
19. let code: number = (error as BusinessError).code;
20. let message: string = (error as BusinessError).message;
21. console.error(`createPluginModuleContext failed, error.code: ${code}, error.message: ${message}`);
22. }
23. }
24. }
```

## application.promoteCurrentToCandidateMasterProcess20+

PhonePC/2in1TabletTVWearable

promoteCurrentToCandidateMasterProcess(insertToHead: boolean): Promise<void>

开发者可以调用该接口将当前进程放入[备选主控进程](../harmonyos-guides/ability-terminology.md#candidatemasterprocess备选主控进程)链表。使用Promise异步回调。

当[主控进程](../harmonyos-guides/ability-terminology.md#masterprocess主控进程)销毁后，再次启动配置了isolationProcess为true的UIAbility/UIExtensionAbility组件时，系统会根据是否存在备选主控进程执行相应操作。

* 如果存在备选主控进程，系统会将备选主控进程链表首节点的进程设置为主控进程，触发[onNewProcessRequest](js-apis-app-ability-abilitystage.md#onnewprocessrequest11)回调。
* 如果不存在备选主控进程，系统会根据组件类型执行相应的操作。
  + 对于UIAbility组件，系统将创建新的空进程作为主控进程。
  + 对于UIExtensionAbility组件，系统会优先复用已有的UIExtensionAbility进程作为新的主控进程，无可用进程时则创建新的空进程作为主控进程。

说明

如果当前进程已经是[主控进程](../harmonyos-guides/ability-terminology.md#masterprocess主控进程)，调用该接口无效并且不会抛出错误码。

当前进程只有运行了isolationProcess字段设为true的组件，或曾经成为过主控进程，开发者才可将其设置为备选主控进程。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口在PC/2in1、Tablet中可正常调用，在其他设备类型中返回801错误码。

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| insertToHead | boolean | 是 | 表示是否将当前进程放入备选主控进程链表的表头。true表示放入表头，false表示放入表尾。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码说明文档](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000115 | The current process cannot be set as a candidate master process. |

**示例：**

```
1. import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. application.promoteCurrentToCandidateMasterProcess(true)
8. .then(() => {
9. console.info('promote succeed');
10. })
11. .catch((err: BusinessError) => {
12. console.error(`promote failed, code is ${err.code}, message is ${err.message}`);
13. });
14. } catch (error) {
15. let code: number = (error as BusinessError).code;
16. let message: string = (error as BusinessError).message;
17. console.error(`promoteCurrentToCandidateMasterProcess failed, error.code: ${code}, error.message: ${message}`);
18. }
19. }
20. }
```

## application.demoteCurrentFromCandidateMasterProcess20+

PhonePC/2in1TabletTVWearable

demoteCurrentFromCandidateMasterProcess(): Promise<void>

撤销当前进程的备选主控进程资格。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异**：该接口在PC/2in1、Tablet中可正常调用，在其他设备类型中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码说明文档](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000116 | The current process is already a master process and does not support cancellation. |
| 16000117 | The current process is not a candidate master process and does not support cancellation. |

**示例：**

```
1. import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. application.demoteCurrentFromCandidateMasterProcess()
8. .then(() => {
9. console.info('demote succeed');
10. })
11. .catch((err: BusinessError) => {
12. console.error(`demote failed, code is ${err.code}, message is ${err.message}`);
13. });
14. } catch (error) {
15. let code: number = (error as BusinessError).code;
16. let message: string = (error as BusinessError).message;
17. console.error(`demoteCurrentFromCandidateMasterProcess failed, error.code: ${code}, error.message: ${message}`);
18. }
19. }
20. }
```

## application.exitMasterProcessRole21+

PhonePC/2in1TabletTVWearable

exitMasterProcessRole(): Promise<void>

放弃当前进程的[主控进程](../harmonyos-guides/ability-terminology.md#masterprocess主控进程)身份。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**设备行为差异：** 该接口仅在2in1、Tablet设备中可正常调用，在其他设备中返回801错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码说明文档](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 801 | Capability not supported. |
| 16000118 | Not a master process. |
| 16000119 | Cannot exit because there is an unfinished request. |

**示例：**

```
1. import { AbilityConstant, UIAbility, application, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class EntryAbility extends UIAbility {
5. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
6. try {
7. application.exitMasterProcessRole()
8. .then(() => {
9. console.info('exitMasterProcessRole succeed');
10. })
11. .catch((err: BusinessError) => {
12. console.error(`exitMasterProcessRole failed, code is ${err.code}, message is ${err.message}`);
13. });
14. } catch (error) {
15. let code: number = (error as BusinessError).code;
16. let message: string = (error as BusinessError).message;
17. console.error(`exitMasterProcessRole failed, error.code: ${code}, error.message: ${message}`);
18. }
19. }
20. }
```

## application.getAppPreloadType22+

PhonePC/2in1TabletTVWearable

getAppPreloadType(): AppPreloadType

获取应用当前进程的预加载类型。

说明

* 只有在进程首次执行[AbilityStage.onCreate](js-apis-app-ability-abilitystage.md#oncreate)完成之前调用该接口，才可以返回真实的预加载类型。
* AbilityStage创建完成后，应用的预加载数据将被清除，调用该接口将返回UNSPECIFIED，无法获取到真实的预加载类型。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AppPreloadType](js-apis-app-ability-application.md#apppreloadtype22) | 应用当前进程的预加载类型。 |

**示例：**

```
1. import { AbilityStage, application } from '@kit.AbilityKit';

3. export default class MyAbilityStage extends AbilityStage{
4. onCreate() {
5. let appPreloadType = application.getAppPreloadType();
6. }
7. }
```
