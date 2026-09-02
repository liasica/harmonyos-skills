---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/screentimeguard-timeguardextensionability
title: "@hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility（屏幕时间守护扩展Ability）"
breadcrumb: API参考 > 应用服务 > Screen Time Guard Kit（屏幕时间守护服务） > ArkTS API > @hms.utilityApplication.screenTimeGuard.TimeGuardExtensionAbility（屏幕时间守护扩展Ability）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:31+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dcdf2c9b4baa02faab2dc97f164f2b0462114e73506b69135b33a69415b2968d
---

## 模块概述

TimeGuardExtensionAbility为屏幕时间守护扩展Ability，继承自[ExtensionAbility](js-apis-app-ability-extensionability.md)。为管控应用提供在守护策略生效和结束、获取授权和撤销授权场景下的生命周期回调。开发者通过定义该回调函数，可以在上述场景中执行特定逻辑。

TimeGuardExtensionAbility为轻量级的独立子进程，不允许唤醒主进程。

**起始版本：** 6.0.0(20)

## 导入模块

```typescript
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';
```

## 属性

**模型约束：** 属性仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [TimeGuardExtensionContext](screentimeguard-timeguardextensioncontext.md) | 否 | 否 | TimeGuardExtensionAbility的上下文环境，继承自[ExtensionContext](js-apis-inner-application-extensioncontext.md)。 |

## onStart

onStart(strategyName: string): Promise<void>

当管控应用启动守护策略时，系统将自动触发此回调函数，开发者可在回调函数中执行自己的业务逻辑。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 启动的守护策略名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```typescript
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

let index = 0; // 用于自增操作

function asyncIncrement(): Promise<void> {
  // index自增的异步操作
  return new Promise<void>((resolve) => {
    index++;
    resolve();
  });
}

export default class EntryAbility extends TimeGuardExtensionAbility {
  async onStart(strategyName: string): Promise<void> {
    // strategyName表示启动的守护策略名称
    // 开发者可在回调中处理自己的业务逻辑，本示例代码只执行index自增逻辑
    await asyncIncrement();
    console.info('test --- onStart:', strategyName, index);
  }
}
```

## onStop

onStop(strategyName: string): Promise<void>

当管控应用停止守护策略时，系统将自动触发此回调函数，开发者可在回调函数中执行自己的业务逻辑。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| strategyName | string | 是 | 停止的守护策略名称。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```typescript
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

let index = 0; // 用于自增操作

function asyncIncrement(): Promise<void> {
  // index自增的异步操作
  return new Promise<void>((resolve) => {
    index++;
    resolve();
  });
}

export default class EntryAbility extends TimeGuardExtensionAbility {
  async onStop(strategyName: string): Promise<void> {
    // strategyName表示停止的守护策略名称
    // 开发者可在回调中处理自己的业务逻辑，本示例代码只执行index自增逻辑
    await asyncIncrement();
    console.info('test --- onStop:', strategyName, index);
  }
}
```

## onUserAuthSwitchOn

onUserAuthSwitchOn(): Promise<void>

当用户在“健康使用设备”中授予管控应用权限时，系统将自动触发此回调函数，开发者可在回调函数中执行自己的业务逻辑。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```typescript
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

let index = 0; // 用于自增操作

function asyncIncrement(): Promise<void> {
  // index自增的异步操作
  return new Promise<void>((resolve) => {
    index++;
    resolve();
  });
}

export default class EntryAbility extends TimeGuardExtensionAbility {
  async onUserAuthSwitchOn(): Promise<void> {
    // 开发者可在回调中处理自己的业务逻辑，本示例代码只执行index自增逻辑
    await asyncIncrement();
    console.info('test --- onUserAuthSwitchOn:', index);
  }
}
```

## onUserAuthSwitchOff

onUserAuthSwitchOff(): Promise<void>

当用户在“健康使用设备”中撤销管控应用授权时，系统将自动触发此回调函数，开发者可在回调函数中执行自己的业务逻辑。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ScreenTimeGuard.GuardService

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**示例：**

```typescript
import { TimeGuardExtensionAbility } from '@kit.ScreenTimeGuardKit';

let index = 0; // 用于自增操作

function asyncIncrement(): Promise<void> {
  // index自增的异步操作
  return new Promise<void>((resolve) => {
    index++;
    resolve();
  });
}

export default class EntryAbility extends TimeGuardExtensionAbility {
  async onUserAuthSwitchOff(): Promise<void> {
    // 开发者可在回调中处理自己的业务逻辑，本示例代码只执行index自增逻辑
    await asyncIncrement();
    console.info('test --- onUserAuthSwitchOff:', index);
  }
}
```
