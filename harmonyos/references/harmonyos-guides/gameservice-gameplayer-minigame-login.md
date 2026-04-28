---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameplayer-minigame-login
title: 小游戏登录（必选）
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 基础游戏服务（必选） > 小游戏 > 小游戏登录（必选）
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:50ab7b7dc1e2656f773e797196d93a0447507813e81aba53fdbeebca94d090d3
---

小游戏接入基础游戏服务的小游戏登录API后，支持玩家使用华为账号快速进入游戏，且小游戏的华为账号实名认证、未成年人防沉迷功能由基础游戏服务实现。

## 前提条件

已完成[开发准备](gameservice-gameplayer-minigame-preparation.md)。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/_kWAX3_uRh6c5tZj0Yn8yA/zh-cn_image_0000002552958898.png?HW-CC-KV=V1&HW-CC-Date=20260427T234903Z&HW-CC-Expire=86400&HW-CC-Sign=165D5B90B1B7D3B4DB3FD563AFB26FF53AEFF6E4AFEFC707C8E0BC80E50A2A5A)

1. 玩家启动小游戏。
2. 小游戏调用[init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)接口初始化Game Service Kit。初始化后，弹出华为隐私协议窗口，玩家确认同意后，可继续往下执行。
3. 小游戏调用[on](../harmonyos-references/gameservice-gameplayer.md#gameplayeronminigameaddictionprevented)接口注册小游戏防沉迷事件监听。
4. 小游戏调用[miniGameLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerminigamelogin)接口。小游戏顶部弹出欢迎横幅，并向小游戏返回playerId、playerSign等信息。同时对玩家是否完成实名认证及是否成年进行校验。

   * 若玩家未完成实名认证，[miniGameLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerminigamelogin)接口自动弹出实名认证窗口要求玩家进行实名认证。
   * 若玩家账号实名认证为未成年人，[miniGameLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerminigamelogin)接口将自动检测未成年人的游戏时间。若玩家不在指定时间内登录小游戏，将强制玩家退出小游戏并返回[1002000006](../harmonyos-references/gameservice-error-code.md#section1002000006-玩家未成年并且当前不在可游戏时间)错误码。

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

```
1. import { gamePlayer } from '@kit.GameServiceKit';
2. import { common } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { window } from '@kit.ArkUI';
```

### 初始化

调用[init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)接口初始化Game Service Kit。

```
1. onWindowStageCreate(windowStage: window.WindowStage) {
2. windowStage.loadContent("pages/index", (err, data) => {
3. try {
4. gamePlayer.init(this.context,()=>{
5. hilog.info(0x0000, 'testTag', `Succeeded in initializing.`);
6. });
7. } catch (error) {
8. let err = error as BusinessError;
9. hilog.error(0x0000, 'testTag', `Failed to init. Code: ${err.code}, message: ${err.message}`);
10. }
11. });
12. }
```

### 监听小游戏防沉迷事件

调用[on](../harmonyos-references/gameservice-gameplayer.md#gameplayeronminigameaddictionprevented)接口注册小游戏防沉迷事件监听。

```
1. private miniGameAddictionPreventedCallback(result: string) {
2. // 退出小游戏
3. }
4. // ...
5. // 调用on接口注册小游戏防沉迷事件监听
6. try {
7. gamePlayer.on('miniGameAddictionPrevented', this.miniGameAddictionPreventedCallback);
8. } catch (error) {
9. let err = error as BusinessError;
10. hilog.error(0x0000, 'testTag', `Failed to register. Code: ${err.code}, message: ${err.message}`);
11. }
```

### 小游戏登录

调用[miniGameLogin](../harmonyos-references/gameservice-gameplayer.md#gameplayerminigamelogin)接口登录小游戏。

```
1. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
2. let request: gamePlayer.MiniGameLoginParam = {
3. 'gameAppId': '123xxx', // 小游戏appId
4. 'extraData': 'xxx' // 附加信息，要求JSON String格式
5. };
6. try {
7. gamePlayer.miniGameLogin(context, request).then((result: gamePlayer.MiniGamePlayer) => {
8. hilog.info(0x0000, 'testTag', `Succeeded in logging in`);
9. }).catch((error: BusinessError) => {
10. hilog.error(0x0000, 'testTag', `Failed to login. Code: ${error.code}, message: ${error.message}`);
11. });
12. } catch (error) {
13. let err = error as BusinessError;
14. hilog.error(0x0000, 'testTag', `Failed to login. Code: ${err.code}, message: ${err.message}`);
15. }
```

### 取消监听小游戏防沉迷事件

游戏退出时通过调用[off](../harmonyos-references/gameservice-gameplayer.md#gameplayeroffminigameaddictionprevented)接口取消监听状态。

```
1. // 取消miniGameAddictionPrevented事件的全部监听
2. try {
3. gamePlayer.off('miniGameAddictionPrevented');
4. } catch (error) {
5. let err = error as BusinessError;
6. hilog.error(0x0000, 'testTag', `Failed to unregister. Code: ${err.code}, message: ${err.message}`);
7. }
```
