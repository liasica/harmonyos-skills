---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-gamebuddyservice-development
title: 实现游戏伴随
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > 游戏伴随服务 > 实现游戏伴随
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:22+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:36ffaa869ad07ca45aa1cc2d9f8b9d56d8460e00029544c6c1dbf8c38b673d49
---

从API版本26.0.0开始，新增游戏伴随服务。游戏伴随服务为游戏陪玩类的应用提供游戏应用状态感知、游戏应用截图等基础能力。

* **游戏应用状态感知**：实时感知游戏的进程创建、切换前台、后台或者终止等状态变化并通知应用。
* **游戏应用截图**：实时捕获游戏画面并以文件描述符方式传递给应用，用于实现游戏画面分享等功能。

## 约束与限制

1. 从API版本26.0.0开始，仅支持Phone设备。
2. 截图频率当前为1s截一张图。

## 业务流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/LtKjw1cxQQOhtYUBdotaYQ/zh-cn_image_0000002736313845.png)

1. 用户启动游戏陪玩类应用。
2. 用户启动游戏。
3. 游戏进程创建。
4. 游戏陪伴类应用调用[onGameApplicationStatus](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#ongameapplicationstatus)接口注册游戏应用状态监听，监听游戏前后台状态变化。
5. 游戏陪伴类应用调用[onGameSnapshot](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#ongamesnapshot)接口注册游戏应用截图监听，用于接收游戏画面截图。
6. 游戏状态发生变化时（切换到前台、后台或终止时）。
7. 游戏伴随服务通过[onGameApplicationStatus](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#ongameapplicationstatus)回调通知已注册的游戏陪伴类应用。
8. 游戏伴随服务通过[onGameSnapshot](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#ongamesnapshot)回调向游戏陪伴类应用发送游戏截图数据（文件描述符方式）。
9. 用户退出所有游戏，游戏伴随服务通过[onGameApplicationStatus](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#ongameapplicationstatus)回调通知游戏陪伴类应用BUDDY\_TERMINATED状态，表示游戏伴随服务已终止。

## 接口说明

具体API说明请详见游戏伴随服务[接口文档](../harmonyos-references/graphics-accelerate-gamebuddyservice.md)。

| 接口名 | 描述 |
| --- | --- |
| [onGameApplicationStatus](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#ongameapplicationstatus)(callback: Callback<[GameApplicationStatusInfo](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#gameapplicationstatusinfo)>): void | 注册游戏应用状态变化的事件监听。 |
| [offGameApplicationStatus](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#offgameapplicationstatus)(callback?: Callback<[GameApplicationStatusInfo](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#gameapplicationstatusinfo)>): void | 取消游戏应用状态变化的事件监听。 |
| [onGameSnapshot](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#ongamesnapshot)(callback: Callback<number>): void | 注册游戏应用截图的事件监听。 |
| [offGameSnapshot](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#offgamesnapshot)(callback?: Callback<number>): void | 取消游戏应用截图的事件监听。 |

## 开发步骤

1. 导入模块。

   ```typescript
    import { gameBuddyService } from '@kit.GraphicsAccelerateKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { image } from '@kit.ImageKit';
    import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 注册回调函数

   ```typescript
   private statusCallback: (statusInfo: gameBuddyService.GameApplicationStatusInfo) => void = (statusInfo) => {
     hilog.info(0x0000, 'gameBuddyService', `Game application status changed: ` + statusInfo.status);
   };
   private snapshotCallback: (fd: number) => void = (fd) => {
     hilog.info(0x0000, 'gameBuddyService', `Game snapshot fd: ${fd}`);
   };
   ```
3. 调用[onGameApplicationStatus](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#ongameapplicationstatus)接口，注册游戏应用状态监听。

   ```typescript
   try {
     gameBuddyService.onGameApplicationStatus(this.statusCallback);
   } catch (err) {
     hilog.error(0x0000, 'gameBuddyService',
       `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
   }
   ```
4. 调用[onGameSnapshot](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#ongamesnapshot)接口，注册游戏应用截图监听。

   ```typescript
   try {
     gameBuddyService.onGameSnapshot(this.snapshotCallback);
   } catch (err) {
     hilog.error(0x0000, 'gameBuddyService',
       `failed to register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
   }
   ```
5. 调用[offGameApplicationStatus](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#offgameapplicationstatus)接口，取消游戏应用状态监听。

   ```typescript
   try {
     gameBuddyService.offGameApplicationStatus(this.statusCallback);
   } catch (err) {
     hilog.error(0x0000, 'gameBuddyService',
       `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
   }
   ```
6. 调用[offGameSnapshot](../harmonyos-references/graphics-accelerate-gamebuddyservice.md#offgamesnapshot)接口，取消游戏应用截图监听。

   ```typescript
   try {
     gameBuddyService.offGameSnapshot(this.snapshotCallback);
   } catch (err) {
     hilog.error(0x0000, 'gameBuddyService', `failed to cancel register listener, errorCode: ${err.code}, errorMessage: ${err.message}`);
   }
   ```
