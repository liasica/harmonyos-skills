---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameplayer-minigame-login
title: 小游戏登录（必选）
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 基础游戏服务（必选） > 小游戏 > 小游戏登录（必选）
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:07+08:00
doc_updated_at: 2026-07-03
content_hash: sha256:c228d51ede437825e9f03132b21d354459b340049d12c98317d0fbc465748701
---

小游戏接入基础游戏服务的小游戏登录API后，支持玩家使用华为账号快速进入游戏，且小游戏的华为账号实名认证、未成年人防沉迷功能由基础游戏服务实现。

## 前提条件

已完成[开发准备](gameservice-gameplayer-minigame-preparation.md)。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/RGOzl9pfQgiHPoGJWz8lBg/zh-cn_image_0000002712405120.png)

1. 玩家启动小游戏。
2. 小游戏调用[init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)接口初始化Game Service Kit。初始化后，弹出华为隐私协议窗口，玩家确认同意后，可继续往下执行。
3. 小游戏调用[on](../harmonyos-references/gameservice-gameplayer.md#gameplayeronminigameaddictionprevented)接口注册小游戏防沉迷事件监听。
4. 小游戏调用[miniGameLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerminigamelogin)接口。小游戏顶部弹出欢迎横幅，并向小游戏返回playerId、playerSign等信息。同时对玩家是否完成实名认证及是否成年进行校验。

   * 若玩家未完成实名认证，[miniGameLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerminigamelogin)接口自动弹出实名认证窗口要求玩家进行实名认证。
   * 若玩家账号实名认证为未成年人，[miniGameLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerminigamelogin)接口将自动检测未成年人的游戏时间。若玩家不在指定时间内登录小游戏，将强制玩家退出小游戏并返回[1002000006](../harmonyos-references/errorcode-gameservice.md#section1002000006-玩家未成年并且当前不在可游戏时间)错误码。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/gameservice-gameplayer.md)。

| 接口名 | 描述 |
| --- | --- |
| [init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)(context: common.UIAbilityContext, callback: AsyncCallback<void>): void | 游戏初始化接口，使用默认的上下文信息，通过callback回调获取返回值。 |
| [on](../harmonyos-references/gameservice-gameplayer.md#gameplayeronminigameaddictionprevented)(type: 'miniGameAddictionPrevented', callback: Callback<string>): void | 小游戏防沉迷事件监听接口，通过callback回调获取小游戏防沉迷事件结果。 |
| [off](../harmonyos-references/gameservice-gameplayer.md#gameplayeroffminigameaddictionprevented)(type: 'miniGameAddictionPrevented', callback?: Callback<string>): void | 取消小游戏防沉迷事件监听接口。 |
| [miniGameLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerminigamelogin)(context: common.Context, loginParam: MiniGameLoginParam): Promise<MiniGamePlayer> | 小游戏登录接口，通过Promise对象获取返回值。 |

## 开发步骤

### 导入模块

导入Game Service Kit及公共模块。

```typescript
import { gamePlayer } from '@kit.GameServiceKit';
import { common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { window } from '@kit.ArkUI';
```

### 初始化

调用[init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)接口初始化Game Service Kit。

```typescript
onWindowStageCreate(windowStage: window.WindowStage) {
  windowStage.loadContent('pages/index', (err, data) => {
    try {
      gamePlayer.init(this.context,()=>{
        hilog.info(0x0000, 'testTag', `Succeeded in initializing.`);
      });
    } catch (error) {
      let err = error as BusinessError;
      hilog.error(0x0000, 'testTag', `Failed to init. Code: ${err.code}, message: ${err.message}`);
    }
  });
}
```

### 监听小游戏防沉迷事件

调用[on](../harmonyos-references/gameservice-gameplayer.md#gameplayeronminigameaddictionprevented)接口注册小游戏防沉迷事件监听。

```typescript
private miniGameAddictionPreventedCallback(result: string) {
  // 退出小游戏
}
// ...
// 调用on接口注册小游戏防沉迷事件监听
try {
  gamePlayer.on('miniGameAddictionPrevented', this.miniGameAddictionPreventedCallback);
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `Failed to register. Code: ${err.code}, message: ${err.message}`);
}
```

### 小游戏登录

调用[miniGameLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerminigamelogin)接口登录小游戏。

```typescript
let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
let request: gamePlayer.MiniGameLoginParam = {
  'gameAppId': '123xxx', // 小游戏appId
  'extraData': 'xxx' // 附加信息，要求JSON String格式
};
try {
  gamePlayer.miniGameLogin(context, request).then((result: gamePlayer.MiniGamePlayer) => {
    if (result?.playerId) {
      hilog.info(0x0000, 'testTag', `Succeeded in logging in`);
    } else {
      hilog.error(0x0000, 'testTag', `Failed to login.`);
    }
  }).catch((error: BusinessError) => {
    hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
  });
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `Failed to login. Code: ${err.code}, message: ${err.message}`);
}
```

### 取消监听小游戏防沉迷事件

游戏退出时通过调用[off](../harmonyos-references/gameservice-gameplayer.md#gameplayeroffminigameaddictionprevented)接口取消监听状态。

```typescript
// 取消miniGameAddictionPrevented事件的全部监听
try {
  gamePlayer.off('miniGameAddictionPrevented');
} catch (error) {
  let err = error as BusinessError;
  hilog.error(0x0000, 'testTag', `Failed to unregister. Code: ${err.code}, message: ${err.message}`);
}
```
