---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gameservice-gameplayer-minigame-pay
title: 小游戏支付
breadcrumb: 指南 > 应用服务 > Game Service Kit（游戏服务） > 基础游戏服务（必选） > 小游戏 > 小游戏支付
category: harmonyos-guides
scraped_at: 2026-04-29T13:38:10+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ec57763f56806911335e401f198d629cbf35996e92c389852c29cda55240bf5a
---

小游戏接入基础游戏服务的小游戏支付API后，支持在小游戏内提供付费商品，玩家可以在小游戏内进行购买。

## 前提条件

* 已完成[开发准备](gameservice-gameplayer-minigame-preparation.md)。
* 已开通[商户服务](../start/merchant-service-0000001053025967.md)。
* 已前往AGC控制台为小游戏[添加数字商品](../app/agc-help-release-minigame-goods-0000002424923350.md)。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/-U5wyzfIQjOrjTZkhsviqQ/zh-cn_image_0000002558605742.png?HW-CC-KV=V1&HW-CC-Date=20260429T053809Z&HW-CC-Expire=86400&HW-CC-Sign=26971BFEB2BD6388983D5D7309CCC5AB1272D5558B7EAD026E38EF7042118ED8)

1. 玩家在小游戏内购买商品。
2. 小游戏调用[miniGamePay](../harmonyos-references/gameservice-gameplayer.md#gameplayerminigamepay)向Game Service Kit发起支付请求。
3. Game Service Kit向IAP Kit发送请求拉起收银台，IAP Kit处理支付请求，详情请参考[商品购买](iap-integrate-purchase.md)。
4. IAP Kit处理完成后向Game Service Kit返回此次商品购买的结果等信息。
5. Game Service Kit返回此次商品购买的结果等信息，开发者将接收到一个[CreatePurchaseResult](../harmonyos-references/gameservice-gameplayer.md#createpurchaseresult)对象，对象内的purchaseData字段包括了此次购买的结果信息。

## 接口说明

具体API说明详见[接口文档](../harmonyos-references/gameservice-gameplayer.md)。

| 接口名 | 描述 |
| --- | --- |
| [init](../harmonyos-references/gameservice-gameplayer.md#gameplayerinit-1)(context: common.UIAbilityContext, callback: AsyncCallback<void>): void | 游戏初始化接口，使用默认的上下文信息，通过callback回调获取返回值。 |
| [miniGamePay](../harmonyos-references/gameservice-gameplayer.md#gameplayerminigamepay)(context: common.Context, parameter: PurchaseParameter): Promise<CreatePurchaseResult> | 小游戏支付接口，通过Promise对象获取返回值。 |

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

### 发起支付请求

调用[miniGamePay](../harmonyos-references/gameservice-gameplayer.md#gameplayerminigamepay)向Game Service Kit发起支付请求，Game Service Kit将向IAP Kit发送请求拉起收银台，IAP Kit处理支付请求。IAP Kit处理完成后向Game Service Kit返回此次商品购买的结果等信息，Game Service Kit将此次商品购买的结果等信息通过[CreatePurchaseResult](../harmonyos-references/gameservice-gameplayer.md#createpurchaseresult)对象返回给开发者。

```
1. let context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
2. let request: gamePlayer.PurchaseParameter = {
3. productId: 'xxx', // 待支付的商品ID
4. productType: 0, // 待查询的商品类型
5. developerPayload: 'xxx', // 商户侧保留信息，该参数长度限制为[0, 256]。若该字段有值，在支付成功后的回调结果中会原样返回给应用
6. reservedInfo: 'xxx' // 要求JSON String格式，商户可以将额外需要传入的字段以key-value的形式设置在JSON String中，并通过该参数传入
7. };
8. try {
9. gamePlayer.miniGamePay(context, request).then((result: gamePlayer.CreatePurchaseResult) => {
10. hilog.info(0x0000, 'testTag', `Succeeded in paying`);
11. }).catch((error: BusinessError) => {
12. hilog.error(0x0000, 'testTag', `Failed to pay. Code: ${error.code}, message: ${error.message}`);
13. });
14. } catch (error) {
15. let err = error as BusinessError;
16. hilog.error(0x0000, 'testTag', `Failed to pay. Code: ${err.code}, message: ${err.message}`);
17. }
```
