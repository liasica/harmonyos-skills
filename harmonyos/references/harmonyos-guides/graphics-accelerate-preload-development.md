---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-preload-development
title: 实现游戏预启动
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏启动加速服务 > 游戏预启动 > 实现游戏预启动
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:21+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:6056b8f05d6f7005353e0e2a403f5393b7fdeea38befe62257e07f34f17a2301
---

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/AwbwCHUHSLO8S5Gthau5Zw/zh-cn_image_0000002706834738.png)

1. 游戏启动加速服务根据用户的使用习惯，在系统资源充足时提前加载游戏。
2. UIAbility的[onCreate](../harmonyos-references/js-apis-app-ability-uiability.md#oncreate)生命周期回调中会通过[want.parameters](../harmonyos-references/js-apis-app-ability-want.md#want)携带启动参数，若参数ohos.params.gamePrelaunch为true，则表示当前UIAbility是由游戏预启动运行的，开发者需记录该启动原因，为后续通知系统游戏启动完成做判断。
3. 随即游戏进入UIAbility的[onForeground](../harmonyos-references/js-apis-app-ability-uiability.md#onforeground)生命周期，此时游戏引擎开始运行，游戏启动完成状态以及启动过程中的业务检测通常由引擎侧负责处理。因此，游戏可根据不同运行状态，主动通知游戏启动加速服务当前预启动流程的执行结果：当预启动正常完成时，触发完成通知；当检测到需要中断的情况（如资源更新等）时，触发终止通知。

**终止预启动**

1. 开发者需调用[terminateGamePrelaunch](../harmonyos-references/graphics-accelerate-launchacceleration.md#terminategameprelaunch)接口通知游戏启动加速服务退出当前的游戏预启动，游戏加速服务接收到消息后会同步通知程序框架服务。
2. 系统程序框架接收到退出游戏预启动通知后，当前游戏的UIAbility将会进入[onDestroy](../harmonyos-references/js-apis-app-ability-uiability.md#ondestroy)生命周期。

**预启动完成**

1. 游戏会继续运行，引擎会开始自渲染并运行到登录页或大厅界面，若当次为游戏预启动，开发者需调用[completeGamePrelaunch](../harmonyos-references/graphics-accelerate-launchacceleration.md#completegameprelaunch)接口，通知游戏启动加速服务当前游戏已启动完成。
2. 系统程序框架接收到游戏预启动完成通知后，当前游戏的UIAbility将会进入[onBackground](../harmonyos-references/js-apis-app-ability-uiability.md#onbackground)生命周期。
3. 用户启动游戏。
4. 游戏的UIAbility直接进入onForeground，将展示游戏预启动完成时的界面。

## 接口说明

具体API说明请详见[接口文档](../harmonyos-references/graphics-accelerate-launchacceleration.md)。

| 接口名 | 描述 |
| --- | --- |
| [completeGamePrelaunch](../harmonyos-references/graphics-accelerate-launchacceleration.md#completegameprelaunch)(context: common.UIAbilityContext): Promise<void> | 通知系统当前游戏预启动已完成。 |
| [terminateGamePrelaunch](../harmonyos-references/graphics-accelerate-launchacceleration.md#terminategameprelaunch)(context: common.UIAbilityContext): Promise<void> | 通知系统退出当前游戏预启动流程。 |

## 开发步骤

1. 获取UIAbility启动原因。

   开发者可在UIAbility的onCreate生命周期回调中通过want.parameters获取启动原因，当参数ohos.params.gamePrelaunch为true时，表示当前UIAbility是由游戏预启动运行的。

   ```typescript
   onCreate(want: Want, _launchParam: AbilityConstant.LaunchParam): void {
     // ...
     // 判断是否是预启动运行，want中ohos.params.gamePrelaunch可能为undefined，赋值时需设置默认值false
     let isPrelaunchStart = (want.parameters?.["ohos.params.gamePrelaunch"] as boolean) ?? false;
     console.info(`EntryAbility onCreate, isPrelaunchStart:${isPrelaunchStart}`);
     // ...
     // ...
   }
   ```
2. 通知启动加速服务当前游戏预启动完成。

   ```typescript
   async completeGamePrelaunch() {
     if (!isPrelaunchStart) {
       // 若当次非预启动运行，游戏启动完成后不进行任何处理
       return;
     }
     if (canIUse('SystemCapability.GraphicsGame.LaunchAcceleration')) {
       try {
         // 通知启动加速服务，当次预启动已完成
         await launchAcceleration.completeGamePrelaunch(this.context);
         console.info('completeGamePrelaunch success');
       } catch (err) {
         console.error(`completeGamePrelaunch failed, code is ${err.code}, message is ${err.message}`);
       }
     }
   }
   ```
3. 通知启动加速服务取消当次游戏预启动。

   ```typescript
   async terminateGamePrelaunch() {
     if (!isPrelaunchStart) {
       // 若当次非预启动运行，游戏启动完成后不进行任何处理
       return;
     }
     if (canIUse('SystemCapability.GraphicsGame.LaunchAcceleration')) {
       try {
         // 通知启动加速服务，终止当前预启动
         await launchAcceleration.terminateGamePrelaunch(this.context);
         console.info('terminateGamePrelaunch success');
       } catch (err) {
         console.error(`terminateGamePrelaunch failed, code is ${err.code}, message is ${err.message}`);
       }
     }
   }
   ```

## 验证方法

具体验证方法请详见[游戏预启动开发实践](../best-practices/bpta-game-prelaunch-practice.md#section1116272764815)。
