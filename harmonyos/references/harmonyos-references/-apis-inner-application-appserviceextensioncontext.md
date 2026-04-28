---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/-apis-inner-application-appserviceextensioncontext
title: AppServiceExtensionContext (应用后台服务扩展组件上下文)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > 接口依赖的元素及定义 > application > AppServiceExtensionContext (应用后台服务扩展组件上下文)
category: harmonyos-references
scraped_at: 2026-04-28T07:58:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6e73085e508db4dbbc56e648a87c1e9b1a10d64c8940b495223ef856342dbdaa
---

AppServiceExtensionContext模块是[AppServiceExtensionAbility](js-apis-app-ability-appserviceextensionability.md)的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。

AppServiceExtensionContext提供了连接、断开ServiceExtensionAbility（系统应用后台服务扩展组件）的能力，以及AppServiceExtensionAbility终止自身的能力。这里的ServiceExtensionAbility只能由系统应用开发，支持三方应用连接。

说明

* 本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口仅可在Stage模型下使用。
* 本模块接口需要在主线程中使用，不要在Worker、TaskPool等子线程中使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { common } from '@kit.AbilityKit';
```

## 使用说明

PhonePC/2in1TabletTVWearable

在使用AppServiceExtensionContext的功能前，需要通过AppServiceExtensionAbility子类实例获取。

**示例：**

```
1. import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';

3. export default class AppServiceExtension extends AppServiceExtensionAbility {
4. onCreate(want: Want) {
5. let context = this.context; // 获取AppServiceExtensionContext
6. }
7. }
```

## AppServiceExtensionContext

PhonePC/2in1TabletTVWearable

### startAbility

PhonePC/2in1TabletTVWearable

startAbility(want: Want, options?: StartOptions): Promise<void>

启动UIAbility。仅支持在主线程调用。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | Want类型参数，传入需要启动的Ability的信息，如Ability名称、Bundle名称等。 |
| options | [StartOptions](js-apis-app-ability-startoptions.md) | 否 | 启动Ability所携带的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码详细介绍请参考[通用错误码](errorcode-universal.md)和[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | The application does not have permission to call the interface. |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000008 | The crowdtesting application expires. |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000010 | The call with the continuation and prepare continuation flag is forbidden. |
| 16000011 | The context does not exist. |
| 16000012 | The application is controlled. |
| 16000013 | The application is controlled by EDM. |
| 16000019 | No matching ability is found. |
| 16000050 | Internal error. |
| 16000055 | Installation-free timed out. |
| 16000071 | App clone is not supported. |
| 16000072 | App clone or multi-instance is not supported. |
| 16000073 | The app clone index is invalid. |
| 16000076 | The app instance key is invalid. |
| 16000077 | The number of app instances reaches the limit. |
| 16000078 | The multi-instance is not supported. |
| 16000079 | The APP\_INSTANCE\_KEY cannot be specified. |
| 16000080 | Creating a new instance is not supported. |

**示例：**

```
1. import { AppServiceExtensionAbility, Want, StartOptions } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. export default class MyAppServiceExtensionAbility extends AppServiceExtensionAbility {
5. onCreate(want: Want) {
6. let wantInfo: Want = {
7. bundleName: 'com.example.myapplication',
8. abilityName: 'EntryAbility'
9. };
10. let options: StartOptions = {
11. displayId: 0
12. };

14. try {
15. this.context.startAbility(wantInfo, options)
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

### connectServiceExtensionAbility

PhonePC/2in1TabletTVWearable

connectServiceExtensionAbility(want: Want, callback: ConnectOptions): number

将当前AppServiceExtensionAbility连接到一个ServiceExtensionAbility，通过返回的proxy与ServiceExtensionAbility进行通信，以使用ServiceExtensionAbility对外提供的能力。仅支持在主线程调用。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | Want类型参数，传入需要连接的Ability的信息，如Ability名称，Bundle名称等。 |
| callback | [ConnectOptions](js-apis-inner-ability-connectoptions.md) | 是 | ConnectOptions类型的回调函数，返回服务连接成功、连接失败、断开的信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回连接id，客户端可以通过[disconnectServiceExtensionAbility](-apis-inner-application-appserviceextensioncontext.md#disconnectserviceextensionability)传入该连接id来断开连接。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000001 | The specified ability does not exist. |
| 16000002 | Incorrect ability type. |
| 16000004 | Cannot start an invisible component. |
| 16000005 | The specified process does not have the permission. |
| 16000006 | Cross-user operations are not allowed. |
| 16000008 | The crowdtesting application expires. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { AppServiceExtensionAbility, Want, common } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { hilog } from '@kit.PerformanceAnalysisKit';

6. let commRemote: rpc.IRemoteObject | null = null; // 断开连接时需要释放
7. const TAG: string = '[AppServiceExtensionAbility]';

9. export default class AppServiceExtension extends AppServiceExtensionAbility {
10. connection: number = 0;

12. onCreate(localWant: Want) {
13. let want: Want = {
14. bundleName: 'com.example.myapp',
15. abilityName: 'MyAbility'
16. };
17. let callback: common.ConnectOptions = {
18. onConnect(elementName, remote) {
19. commRemote = remote;
20. hilog.info(0x0000, TAG, '----------- onConnect -----------');
21. },
22. onDisconnect(elementName) {
23. hilog.info(0x0000, TAG, '----------- onDisconnect -----------');
24. },
25. onFailed(code) {
26. hilog.error(0x0000, TAG, '----------- onFailed -----------');
27. }
28. };

31. try {
32. this.connection = this.context.connectServiceExtensionAbility(want, callback);
33. } catch (paramError) {
34. commRemote = null;
35. // 处理入参错误异常
36. hilog.error(0x0000, TAG, `error.code: ${(paramError as BusinessError).code}, error.message: ${(paramError as BusinessError).message}`);
37. }
38. }

40. onDestroy(): void {
41. this.context.disconnectServiceExtensionAbility(this.connection).then(() => {
42. commRemote = null;
43. // 执行正常业务
44. hilog.info(0x0000, TAG, '----------- disconnectServiceExtensionAbility success -----------');
45. })
46. .catch((error: BusinessError) => {
47. commRemote = null;
48. // 处理业务逻辑错误
49. hilog.error(0x0000, TAG, `disconnectServiceExtensionAbility failed, error.code: ${error.code}, error.message: ${error.message}`);
50. });
51. }
52. }
```

### disconnectServiceExtensionAbility

PhonePC/2in1TabletTVWearable

disconnectServiceExtensionAbility(connection: number): Promise<void>

将AppServiceExtensionAbility与已连接的ServiceExtensionAbility断开连接。仅支持在主线程调用。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| connection | number | 是 | 在[connectServiceExtensionAbility](-apis-inner-application-appserviceextensioncontext.md#connectserviceextensionability)中返回的连接id。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

参见[connectServiceExtensionAbility](-apis-inner-application-appserviceextensioncontext.md#connectserviceextensionability)。

### terminateSelf

PhonePC/2in1TabletTVWearable

terminateSelf(): Promise<void>

销毁AppServiceExtensionAbility自身。仅支持在主线程调用。使用Promise异步回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码详细介绍请参考[元能力子系统错误码](errorcode-ability.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 16000009 | An ability cannot be started or stopped in Wukong mode. |
| 16000011 | The context does not exist. |
| 16000050 | Internal error. |

**示例：**

```
1. import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG: string = '[AppServiceExtensionAbility]';

7. export default class AppServiceExtension extends AppServiceExtensionAbility {
8. onCreate(want: Want) {
9. this.context.terminateSelf().then(() => {
10. // 执行正常业务
11. hilog.info(0x0000, TAG, '----------- terminateSelf succeed -----------');
12. }).catch((error: BusinessError) => {
13. // 处理业务逻辑错误
14. hilog.error(0x0000, TAG, `terminateSelf failed, error.code: ${error.code}, error.message: ${error.message}`);
15. });
16. }
17. }
```
