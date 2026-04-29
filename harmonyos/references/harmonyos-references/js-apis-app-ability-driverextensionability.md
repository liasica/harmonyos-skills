---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-app-ability-driverextensionability
title: @ohos.app.ability.DriverExtensionAbility (驱动程序扩展能力)
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > ArkTS API > @ohos.app.ability.DriverExtensionAbility (驱动程序扩展能力)
category: harmonyos-references
scraped_at: 2026-04-29T14:01:19+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:8d4dcdc73ab926b72e1d0b21538ed6eca428a272dfcff5bafe781ff5f1664ffa
---

DriverExtensionAbility模块提供驱动相关扩展能力，提供驱动创建、销毁、连接、断开等生命周期回调。

说明

本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PC/2in1

```
1. import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
```

## DriverExtensionAbility

PC/2in1

### 属性

PC/2in1

DriverExtensionAbility类，包含驱动生命周期回调的定义。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [DriverExtensionContext](js-apis-inner-application-driverextensioncontext.md) | 否 | 否 | DriverExtension的上下文环境，继承自ExtensionContext。 |

### onInit

PC/2in1

onInit(want: Want): void

Extension生命周期回调，在创建时回调，执行初始化业务逻辑操作。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

**示例：**

```
1. import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
2. import { Want } from '@kit.AbilityKit';

4. class DriverExt extends DriverExtensionAbility {
5. onInit(want : Want) {
6. console.info(`onInit, want: ${want.abilityName}`);
7. }
8. }
```

### onRelease

PC/2in1

onRelease(): void

Extension生命周期回调，在销毁时回调，执行资源清理等操作。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**示例：**

```
1. class DriverExt extends DriverExtensionAbility {
2. onRelease() {
3. console.info('onRelease');
4. }
5. }
```

### onConnect

PC/2in1

onConnect(want: Want): rpc.RemoteObject | Promise<rpc.RemoteObject>

Extension生命周期回调，会在[onCreate](js-apis-app-ability-abilitystage.md#oncreate)之后回调。返回一个[RemoteObject](js-apis-rpc.md#remoteobject)对象，用于客户端和服务端进行通信。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| rpc.[RemoteObject](js-apis-rpc.md#remoteobject) | Promise<rpc.[RemoteObject](js-apis-rpc.md#remoteobject)> | 一个RemoteObject对象，用于客户端和服务端进行通信；或一个Promise对象，返回用于通信的RemoteObject对象。 |

**示例：**

```
1. import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
2. import { rpc } from '@kit.IPCKit';
3. import { Want } from '@kit.AbilityKit';

5. class StubTest extends rpc.RemoteObject{
6. constructor(des : string) {
7. super(des);
8. }
9. onRemoteMessageRequest(code : number, data : rpc.MessageSequence, reply : rpc.MessageSequence, option : rpc.MessageOption) {
10. // 必须重写此接口
11. return true;
12. }
13. }
14. class DriverExt extends DriverExtensionAbility {
15. onConnect(want : Want) {
16. console.info(`onConnect , want: ${want.abilityName}`);
17. return new StubTest('test');
18. }
19. }
```

如果生成返回值[RemoteObject](js-apis-rpc.md#remoteobject)依赖一个异步接口，可以使用异步生命周期：

```
1. import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
2. import { rpc } from '@kit.IPCKit';
3. import { Want } from '@kit.AbilityKit';

5. class StubTest extends rpc.RemoteObject{
6. constructor(des : string) {
7. super(des);
8. }
9. onRemoteMessageRequest(code : number, data : rpc.MessageSequence, reply : rpc.MessageSequence, option : rpc.MessageOption) {
10. // 必须重写此接口
11. return true;
12. }
13. }
14. async function getDescriptor() {
15. // 调用异步函数...
16. return "asyncTest";
17. }
18. class DriverExt extends DriverExtensionAbility {
19. async onConnect(want : Want) {
20. console.info(`onConnect , want: ${want.abilityName}`);
21. let descriptor = await getDescriptor();
22. return new StubTest(descriptor);
23. }
24. }
```

### onDisconnect

PC/2in1

onDisconnect(want: Want): void | Promise<void>

Extension的生命周期回调，客户端执行断开连接服务时回调。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| want | [Want](js-apis-app-ability-want.md) | 是 | 当前Extension相关的Want类型信息，包括ability名称、bundle名称等。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| void | Promise<void> | 返回值为空；或一个Promise对象，无返回结果。 |

**示例：**

```
1. import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
2. import { Want } from '@kit.AbilityKit';

4. class DriverExt extends DriverExtensionAbility {
5. onDisconnect(want : Want) {
6. console.info(`onDisconnect, want: ${want.abilityName}`);
7. }
8. }
```

在执行完onDisconnect生命周期回调后，应用可能会退出，从而可能导致onDisconnect中的异步函数未能正确执行，比如异步写入数据库。可以使用异步生命周期，以确保异步onDisconnect完成后再继续后续的生命周期。

```
1. import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
2. import { Want } from '@kit.AbilityKit';

4. class DriverExt extends DriverExtensionAbility {
5. async onDisconnect(want : Want) {
6. console.info(`onDisconnect, want: ${want.abilityName}`);
7. // 调用异步函数...
8. }
9. }
```

### onDump

PC/2in1

onDump(params: Array<string>): Array<string>

转储客户端信息时调用，建议不要转储敏感信息。

**模型约束**：此接口仅在Stage模型下使用。

**系统能力**：SystemCapability.Driver.ExternalDevice

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| params | Array<string> | 是 | 表示命令形式的参数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<string> | 一个string类型的数组，用于转存客户端信息。 |

**示例：**

```
1. class DriverExt extends DriverExtensionAbility {
2. onDump(params : Array<string>) {
3. console.info(`dump, params: ${JSON.stringify(params)}`);
4. return ['params'];
5. }
6. }
```

## DriverExtensionContext

PC/2in1

type DriverExtensionContext = \_DriverExtensionContext;

DriverExtensionAbility的上下文环境。

**系统能力**：SystemCapability.Driver.ExternalDevice

| 类型 | 说明 |
| --- | --- |
| \_DriverExtensionContext | DriverExtensionAbility的上下文环境，继承自ExtensionContext，其具体使用方法可参考[DriverExtensionContext](js-apis-inner-application-driverextensioncontext.md)。 |
