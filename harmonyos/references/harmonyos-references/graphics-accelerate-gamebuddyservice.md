---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/graphics-accelerate-gamebuddyservice
title: gameBuddyService（游戏伴随服务）
breadcrumb: API参考 > 图形 > Graphics Accelerate Kit（图形加速服务） > ArkTS API > gameBuddyService（游戏伴随服务）
category: harmonyos-references
scraped_at: 2026-09-02T14:53:11+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:dc327729d0a136a3c23df62680789f90af705ee4f54eaa6121cd4bbf4c9c2897
---

本模块提供游戏伴随服务能力。

**起始版本：** 26.0.0

## 导入模块

```typescript
import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
```

## GameApplicationStatus

此枚举描述游戏应用状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**起始版本：** 26.0.0

| **名称** | **值** | **说明** |
| --- | --- | --- |
| FOREGROUND | 1 | 游戏应用处于前台。 |
| BACKGROUND | 2 | 游戏应用处于后台。 |
| TERMINATED | 3 | 游戏应用已终止。 |
| BUDDY\_TERMINATED | 4 | 游戏伴随服务已终止。 |

## GameApplicationStatusInfo

游戏应用状态结构体，描述当前运行的游戏应用状态。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**起始版本：** 26.0.0

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| gameBundle | string | 否 | 否 | 游戏应用名称。 |
| status | [GameApplicationStatus](graphics-accelerate-gamebuddyservice.md#gameapplicationstatus) | 否 | 否 | 游戏应用状态。 |

## onGameApplicationStatus

onGameApplicationStatus(callback: Callback<GameApplicationStatusInfo>): void

注册游戏应用状态变化的事件监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_GAME\_BUDDY\_SERVICE

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**设备行为差异：** 本接口实际支持的设备类型范围（Phone）小于其所属系统能力支持的设备类型范围（Phone、Tablet、TV）。该接口仅在Phone中可正常调用，在其他设备中不可交互。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[GameApplicationStatusInfo](graphics-accelerate-gamebuddyservice.md#gameapplicationstatusinfo)> | 是 | 回调函数，返回[GameApplicationStatusInfo](graphics-accelerate-gamebuddyservice.md#gameapplicationstatusinfo)对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-graphics-accelerate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1009503001 | The game buddy service is initializing, please retry later. |
| 1009503002 | No game is running, or the current game is not supported by the game buddy service. Please launch a supported game first. |

**示例**：

```typescript
import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 匿名函数注册
try {
  gameBuddyService.onGameApplicationStatus((statusInfo) => {
    hilog.info(0x0000, 'gameBuddyService', `Game application status changed: ${statusInfo.status}`);
  });
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 特定函数注册
let statusCallback = (statusInfo: gameBuddyService.GameApplicationStatusInfo) => {
  hilog.info(0x0000, 'gameBuddyService', `Game application status changed: ${statusInfo.status}`);
};
try {
  gameBuddyService.onGameApplicationStatus(statusCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```

## offGameApplicationStatus

offGameApplicationStatus(callback?: Callback<GameApplicationStatusInfo>): void

取消游戏应用状态变化的事件监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_GAME\_BUDDY\_SERVICE

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**设备行为差异：** 本接口实际支持的设备类型范围（Phone）小于其所属系统能力支持的设备类型范围（Phone、Tablet、TV）。该接口仅在Phone中可正常调用，在其他设备中不可交互。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[GameApplicationStatusInfo](graphics-accelerate-gamebuddyservice.md#gameapplicationstatusinfo)> | 否 | 回调函数，返回[GameApplicationStatusInfo](graphics-accelerate-gamebuddyservice.md#gameapplicationstatusinfo)对象。需与注册时传入的回调函数是同一个。若不设置该参数，则取消注册所有的回调函数监听事件。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例**：

```typescript
import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 匿名函数或无回调调用，取消该事件所有监听
// 无回调
try {
  gameBuddyService.offGameApplicationStatus();
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 匿名函数
try {
  gameBuddyService.offGameApplicationStatus((statusInfo) => {
    hilog.info(0x0000, 'gameBuddyService', `Game application status: ${statusInfo.status}`);
  });
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 特定函数注册，则仅取消该特定函数的监听
let statusCallback = (statusInfo:gameBuddyService.GameApplicationStatusInfo) => {
  hilog.info(0x0000, 'gameBuddyService', `Game application status changed: ${statusInfo.status}`);
};
try {
  gameBuddyService.offGameApplicationStatus( statusCallback );
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```

## onGameSnapshot

onGameSnapshot(callback: Callback<number>): void

注册游戏应用截图的事件监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_GAME\_BUDDY\_SERVICE

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**设备行为差异：** 本接口实际支持的设备类型范围（Phone）小于其所属系统能力支持的设备类型范围（Phone、Tablet、TV）。该接口仅在Phone中可正常调用，在其他设备中不可交互。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<number> | 是 | 回调函数，返回文件描述符。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[ArkTS API错误码](errorcode-graphics-accelerate.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 1009503001 | The game buddy service is initializing, please retry later. |
| 1009503002 | No game is running, or the current game is not supported by the game buddy service. Please launch a supported game first. |

**示例**：

```typescript
import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 匿名函数注册
try {
  gameBuddyService.onGameSnapshot((fd) => {
    hilog.info(0x0000, 'gameBuddyService', `Game snapshot fd: ${fd}`);
  });
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 特定函数注册
let snapShotCallback = (fd: number) => {
  hilog.info(0x0000, 'gameBuddyService', `Game snapshot fd: ${fd}`);
};
try {
  gameBuddyService.onGameSnapshot(snapShotCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```

## offGameSnapshot

offGameSnapshot(callback?: Callback<number>): void

取消游戏应用截图的事件监听。使用callback异步回调。

**模型约束：** 此接口仅可在Stage模型下使用。

**需要权限：** ohos.permission.ACCESS\_GAME\_BUDDY\_SERVICE

**系统能力：** SystemCapability.GraphicsGame.RenderAccelerate

**设备行为差异：** 本接口实际支持的设备类型范围（Phone）小于其所属系统能力支持的设备类型范围（Phone、Tablet、TV）。该接口仅在Phone中可正常调用，在其他设备中不可交互。

**起始版本：** 26.0.0

**参数：**

| **参数名** | **类型** | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<number> | 否 | 回调函数，返回文件描述符。需与注册时传入的回调函数是同一个。若不设置该参数，则取消注册所有的回调函数监听事件。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |

**示例**：

```typescript
import {gameBuddyService} from '@kit.GraphicsAccelerateKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// 匿名函数或无回调调用，取消该事件所有监听
// 无回调
try {
  gameBuddyService.offGameSnapshot();
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 匿名函数
try {
  gameBuddyService.offGameSnapshot((fd) => {
    hilog.info(0x0000, 'gameBuddyService', `Game snapshot fd: ${fd}`);
  });
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}

// 特定函数注册，则仅取消该特定函数的监听
let snapShotCallback = (fd: number) => {
  hilog.info(0x0000, 'gameBuddyService', `Game snapshot fd: ${fd}`);
};
try {
  gameBuddyService.offGameSnapshot(snapShotCallback);
} catch (err) {
  hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
}
```
