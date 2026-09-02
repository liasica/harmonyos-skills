---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-launchacceleration
title: launchAcceleration（游戏启动加速）
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > ArkTS API > launchAcceleration（游戏启动加速）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ff616dce52b0f806f22bd1fa3bbc0297091b5856e248aa4a4761dc2798471e8f
---

本模块提供游戏启动加速能力。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GraphicsGame.LaunchAcceleration

**起始版本：** 6.0.0(20)

## 导入模块

```typescript
import { launchAcceleration } from '@kit.GraphicsAccelerateKit';
```

## isLaunchMirrorEnabled

isLaunchMirrorEnabled(): boolean

查询游戏的内存镜像功能是否使能。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GraphicsGame.LaunchAcceleration

**起始版本：** 6.0.0(20)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 系统将结合当前设备的游戏热度、内存镜像数、当日磁盘换出量综合判定是否使能内存镜像功能：  - true：游戏使能了内存镜像功能。游戏先切换场景（建议开发者将场景切换至游戏登录界面），系统在退出游戏前自动制作内存镜像，制作内存镜像大概需要4s。  - false：游戏未使能内存镜像功能，系统将直接退出游戏进程。  默认为false。 |

**示例**：

```typescript
import { launchAcceleration } from '@kit.GraphicsAccelerateKit';

onWindowStageWillDestroy(): void {
    // 查询当前游戏内存镜像功能是否使能。
    let enable = launchAcceleration.isLaunchMirrorEnabled()
    if (enable) {
        // 切换场景的代码逻辑
    }
}
```

## completeGamePrelaunch

completeGamePrelaunch(context: common.UIAbilityContext): Promise<void>

通知系统当前游戏预启动已完成。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GraphicsGame.LaunchAcceleration

**起始版本：** 26.0.0

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-app-ability-common.md#uiabilitycontext) | 是 | UIAbility组件上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-graphics-accelerate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1019400001 | Service error. 1. Connect to system service failed; 2.System service failed to communicate with dependency module. |
| 1019400002 | The app is not in a preloading state. |
| 1019400401 | Parameter error. |

**示例**：

```typescript
import { UIAbility } from '@kit.AbilityKit';
import { launchAcceleration } from '@kit.GraphicsAccelerateKit';

export default class EntryAbility extends UIAbility {
  async completeGamePrelaunch() {
    try {
      await launchAcceleration.completeGamePrelaunch(this.context);
    } catch (err) {
      console.error(`completeGamePrelaunch failed, code is ${err.code}, message is ${err.message}`);
    }
  }
}
```

## terminateGamePrelaunch

terminateGamePrelaunch(context: common.UIAbilityContext): Promise<void>

通知系统退出当前游戏预启动流程。使用Promise异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GraphicsGame.LaunchAcceleration

**起始版本：** 26.0.0

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| context | [common.UIAbilityContext](js-apis-app-ability-common.md#uiabilitycontext) | 是 | UIAbility组件上下文。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[ArkTS API错误码](errorcode-graphics-accelerate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 1019400001 | Service error. 1. Connect to system service failed; 2.System service failed to communicate with dependency module. |
| 1019400002 | The app is not in a preloading state. |
| 1019400401 | Parameter error. |

**示例**：

```typescript
import { UIAbility } from '@kit.AbilityKit';
import { launchAcceleration } from '@kit.GraphicsAccelerateKit';

export default class EntryAbility extends UIAbility {
  async terminateGamePrelaunch() {
    try {
      await launchAcceleration.terminateGamePrelaunch(this.context);
    } catch (err) {
      console.error(`terminateGamePrelaunch failed, code is ${err.code}, message is ${err.message}`);
    }
  }
}
```
