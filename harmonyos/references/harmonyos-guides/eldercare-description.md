---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/eldercare-description
title: 获取关怀模式状态
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 应用长辈关怀功能体验 > 获取关怀模式状态
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:44+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:23f73a11f972a9c4140cc0ad818a7db121980609e8907f5e2fb516993c771edf
---

## 场景介绍

从API版本26.0.0开始，若应用内关怀模式希望跟随系统关怀模式变化，应用可通过以下两种方式获取或监听系统关怀模式的状态，让长辈看得更清楚，操控得更顺畅。

1. 查询系统关怀模式状态：应用启动时，可通过isSeniorModeEnabled接口查询系统设置中的关怀模式开关状态。若系统关怀模式已开启，则应用应跟随系统开启关怀模式，若系统关怀模式未开启，则应用应跟随系统关闭关怀模式。
2. 监听系统的关怀模式状态：应用进程存在时，可通过AccessibilityKit提供的接口onSeniorModeStateChange监听系统关怀模式开关状态，当监听到系统关怀模式变化时，应用可跟随进行关怀模式状态切换。

## 接口说明

以下是应用与系统关怀模式的相关接口说明。

| 接口名 | 描述 |
| --- | --- |
| isSeniorModeEnabled(): Promise<boolean> | 异步接口，获取关怀模式的开关状态。 |
| onSeniorModeStateChange(callback: Callback<boolean>): void | 注册系统关怀模式状态变化事件的监听回调。 |
| offSeniorModeStateChange(callback?: Callback<boolean>): void | 取消注册系统关怀模式状态变化事件的监听回调。 |

## 开发实例

1. 导入accessibility模块及相关公共模块。

   ```typescript
   import { accessibility } from '@kit.AccessibilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   ```
2. 对系统关怀模式状态进行监听。

   在aboutToAppear进行对系统关怀模式状态注册监听，在aboutToDisappear取消对系统关怀模式状态注册监听。

   ```typescript
   @Entry
   @Component
   struct SeniorModeDemo1 {

    // 关怀模式状态变化的回调，回调值为true时，代表系统关怀模式已打开，否则代表系统关怀模式已关闭。
    callBack = (data: boolean) => {
      console.info(`subscribe senior mode state change, result: ${JSON.stringify(data)}`);
    }

     aboutToAppear(): void {
       // 注册系统关怀模式状态变化监听。
       accessibility.onSeniorModeStateChange(this.callback);
     }

     aboutToDisappear(): void {
       // 取消注册系统关怀模式状态变化监听。
       accessibility.offSeniorModeStateChange(this.callback);
     }

     build() {
       // 开发者自行展示UX界面。
     }
   }
   ```
3. 查询系统关怀模式状态。

   ```typescript
   @Entry
   @Component
   struct SeniorModeDemo2 {
     aboutToAppear(): void {
       // 调用异步接口isSeniorModeEnabled查询当前系统关怀模式状态，返回值为true时，代表系统关怀模式已打开，否则代表系统关怀模式已关闭。
       accessibility.isSeniorModeEnabled().then((data: boolean) => {
         console.info(`success data:isSeniorModeEnabled : ${JSON.stringify(data)}`);
       }).catch((err: BusinessError) => {
         console.error(`failed to call isSeniorModeEnabled, Code is ${err.code}, message is ${err.message}`);
       });
     }

     build() {
       // 开发者自行展示UX界面。
     }
   }
   ```
