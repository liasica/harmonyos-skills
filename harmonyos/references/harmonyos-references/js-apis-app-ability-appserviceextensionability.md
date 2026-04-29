---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-appserviceextensionability
title: @ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件)
breadcrumb: API参考 > 应用框架 > Ability Kit（程序框架服务） > ArkTS API > Stage模型能力的接口 > @ohos.app.ability.AppServiceExtensionAbility (应用后台服务扩展组件)
category: harmonyos-references
scraped_at: 2026-04-29T13:48:27+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ade7b2ede88f71d03bc90741452b59548bcfe60f35e2d30003ce6cf131f7a0f5
---

AppServiceExtensionAbility模块提供后台服务相关扩展能力，包括后台服务的创建、销毁、连接、断开等生命周期回调。

说明

本模块首批接口从API version 20开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

本模块接口仅可在Stage模型下使用。

## 约束限制

PhonePC/2in1TabletTVWearable

* 当前仅支持2in1设备。
* 应用集成AppServiceExtensionAbility的组件需要申请ACL权限（ohos.permission.SUPPORT\_APP\_SERVICE\_EXTENSION）。该ACL权限当前只对企业普通应用开放申请，申请方式参考[权限申请指导](../harmonyos-guides/declare-permissions.md)。

## 生命周期

PhonePC/2in1TabletTVWearable

AppServiceExtensionAbility提供了[onCreate()](js-apis-app-ability-appserviceextensionability.md#oncreate)、[onRequest()](js-apis-app-ability-appserviceextensionability.md#onrequest)、[onConnect()](js-apis-app-ability-appserviceextensionability.md#onconnect)、[onDisconnect()](js-apis-app-ability-appserviceextensionability.md#ondisconnect)和[onDestroy()](js-apis-app-ability-appserviceextensionability.md#ondestroy)生命周期回调，开发者可根据需要重写对应的回调方法。下图展示了AppServiceExtensionAbility的生命周期。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/V2we3f3oT7e49MjACH25yw/zh-cn_image_0000002589245725.png?HW-CC-KV=V1&HW-CC-Date=20260429T054506Z&HW-CC-Expire=86400&HW-CC-Sign=495428F2EE475A09DB54CACF4D0C15751D245A949BBCE612C1614E0C195BA8E6)

* **onCreate**

  在AppServiceExtensionAbility实例创建时，系统会触发该回调。
* **onDestroy**

  在AppServiceExtensionAbility实例销毁时，系统会触发该回调。
* **onRequest**

  调用方使用[startAppServiceExtensionAbility()](js-apis-inner-application-uiabilitycontext.md#startappserviceextensionability20)拉起AppServiceExtensionAbility实例时，系统会触发该回调。
* **onConnect**

  调用方使用[connectAppServiceExtensionAbility](js-apis-inner-application-uiabilitycontext.md#connectappserviceextensionability20)连接AppServiceExtensionAbility实例时，系统会触发该回调。
* **onDisconnect**

  当所有连接方断开与AppServiceExtensionAbility实例的连接时，系统会触发该回调。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { AppServiceExtensionAbility } from '@kit.AbilityKit';
```

## AppServiceExtensionAbility

PhonePC/2in1TabletTVWearable

AppServiceExtensionAbility模块提供后台服务相关扩展能力，包括后台服务的创建、销毁、连接、断开等生命周期回调。

### 属性

PhonePC/2in1TabletTVWearable

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [AppServiceExtensionContext](-apis-inner-application-appserviceextensioncontext.md) | 否 | 否 | AppServiceExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

### onCreate

PhonePC/2in1TabletTVWearable

onCreate(want: Want): void

在AppServiceExtensionAbility实例创建时，系统会触发该回调。应用可以在该接口中执行自己的业务逻辑初始化操作，例如注册公共事件监听等。

说明

如果AppServiceExtensionAbility实例已创建，再次启动或连接该实例时不会触发onCreate()回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 调用方拉起当前AppServiceExtensionAbility实例时传递的Want类型信息，包括Ability名称、Bundle名称等。 |

**示例：**

```
1. import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[AppServiceExtAbility]';

6. export default class AppServiceExtAbility extends AppServiceExtensionAbility {
7. onCreate(want: Want) {
8. hilog.info(0x0000, TAG, `onCreate, want: ${want.abilityName}`);
9. }
10. }
```

### onDestroy

PhonePC/2in1TabletTVWearable

onDestroy(): void

在AppServiceExtensionAbility实例销毁时，系统会触发该回调。应用可以在该接口中执行资源清理等操作，如注销监听等。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**示例：**

```
1. import { AppServiceExtensionAbility } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[AppServiceExtAbility]';

6. export default class AppServiceExtAbility extends AppServiceExtensionAbility {
7. onDestroy() {
8. hilog.info(0x0000, TAG, `onDestroy`);
9. }
10. }
```

### onRequest

PhonePC/2in1TabletTVWearable

onRequest(want: Want, startId: number): void

调用方每次使用[startAppServiceExtensionAbility()](js-apis-inner-application-uiabilitycontext.md#startappserviceextensionability20)拉起AppServiceExtensionAbility实例时，系统都会触发该回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 调用方拉起当前AppServiceExtensionAbility实例时传递的Want类型信息，包括Ability名称、Bundle名称等。 |
| startId | number | 是 | 返回拉起次数。首次拉起初始值返回1，多次拉起时自动递增。 |

**示例：**

```
1. import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[AppServiceExtAbility]';

6. export default class AppServiceExtAbility extends AppServiceExtensionAbility {
7. onRequest(want: Want, startId: number) {
8. hilog.info(0x0000, TAG, `onRequest, want: ${want.abilityName}, startId: ${startId}`);
9. }
10. }
```

### onConnect

PhonePC/2in1TabletTVWearable

onConnect(want: Want): rpc.RemoteObject

调用方使用[connectAppServiceExtensionAbility](js-apis-inner-application-uiabilitycontext.md#connectappserviceextensionability20)连接AppServiceExtensionAbility实例时，系统会触发该回调。

应用需要在该接口中返回一个RemoteObject对象，用于客户端和服务端进行通信。当AppServiceExtensionAbility实例处于连接状态时，如果调用方发起新的连接，系统会返回缓存的RemoteObject对象，而不会重复回调onConnect()接口。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 调用方拉起当前AppServiceExtensionAbility实例时传递的Want类型信息，包括Ability名称、Bundle名称等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [rpc.RemoteObject](js-apis-rpc.md#iremoteobject) | 一个RemoteObject对象，用于客户端和服务端进行通信。 |

**示例：**

```
1. import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
2. import { rpc } from '@kit.IPCKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';

5. const TAG: string = '[AppServiceExtAbility]';

7. class StubTest extends rpc.RemoteObject {
8. constructor(des: string) {
9. super(des);
10. }

12. onConnect(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence, option: rpc.MessageOption) {
13. }
14. }

16. export default class AppServiceExtAbility extends AppServiceExtensionAbility {
17. onConnect(want: Want) {
18. hilog.info(0x0000, TAG, `onConnect, want: ${want.abilityName}`);
19. return new StubTest('test');
20. }
21. }
```

### onDisconnect

PhonePC/2in1TabletTVWearable

onDisconnect(want: Want): void

当所有连接方断开与AppServiceExtensionAbility实例的连接时，系统会触发该回调。

**系统能力**：SystemCapability.Ability.AbilityRuntime.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | AppServiceExtensionAbility实例最近一次被拉起或者连接时，调用方传递的Want类型信息，包括Ability名称、Bundle名称等。 |

**示例：**

```
1. import { AppServiceExtensionAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';

4. const TAG: string = '[AppServiceExtAbility]';

6. export default class AppServiceExtAbility extends AppServiceExtensionAbility {
7. onDisconnect(want: Want) {
8. hilog.info(0x0000, TAG, `onDisconnect, want: ${want.abilityName}`);
9. }
10. }
```
