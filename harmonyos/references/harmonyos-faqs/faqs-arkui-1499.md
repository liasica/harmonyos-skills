---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1499
title: 如何防止视频播放时自动熄屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 如何防止视频播放时自动熄屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9d9ac33d191ac9051d93fbc9087fa28e3d3bb35bd985ef9279b0fbdd64f11598
---

## 问题现象

视频播放时自动熄屏。

## 背景知识

[window.setWindowKeepScreenOn](../harmonyos-references/arkts-apis-window-window.md#setwindowkeepscreenon9)：设置屏幕是否为常亮状态。规范使用该接口：

* 仅在必要场景（导航、视频播放、绘画、游戏等场景）下，设置该属性为true；
* 退出上述场景后，应当重置该属性为false；其他场景（无屏幕互动、音频播放等）下，不使用该接口；
* 系统检测到非规范使用该接口时，可能会恢复自动灭屏功能。

## 问题定位

1. 查看是否有关键日志**SetKeepScreenOn**。
2. 如果有关键日志，需要确认加锁与解锁的时机。

   设置屏幕常亮时会有**try lock**日志输出。

   解除屏幕常亮时会有**try unlock**日志输出。

   加锁与解锁都只看type:0的。

   通过**try lock.\*type: 0|try unlock.\*type: 0**过滤日志查看加锁解锁时间，如下所示，加锁和解锁之间时间间隔很短，设置屏幕常亮之后立即解除了屏幕常亮。

   ```txt
   Client CreateRunningLock name: xxxxxx, type = 0
   bundle name for vid=20020020, name=com.xxx.example
   CreateRunningLock name:kankan0_307088416, type:0, lockid:xxxxxxxx
   try Lock, name: xxxxxx_307088416, type: 0 lockid: xxxxxxxxx
   [UL_POWER] RUNNINGLOCK_SCREEN active, and the current power state is 0
   runninglock message: LOCKID=xxxxxxxxxx PID=3304 UID=20020020 TYPE=0 
   try UnLock, name: xxxxxx_307088416, type: 0 lockid: xxxxxxxxxx
   ```

## 分析结论

1. 如果日志中没有关键日志**SetKeepScreenOn**，则是因为应用没有设置屏幕常亮导致。
2. 如果日志中有关键日志**SetKeepScreenOn**，则需要排查加锁解锁时机。

## 修改建议

1. 在视频播放开始时（如playing状态）调用window.setWindowKeepScreenOn(true)。
2. 确保在视频播放结束、暂停或停止才调用setWindowKeepScreenOn(false)，避免重复或错误的调用逻辑。

   ```ts
   import common from '@ohos.app.ability.common';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { window } from '@kit.ArkUI';

   @Entry
   @Component
   struct S20250416165613637594 {
     private controller: VideoController = new VideoController();
     private innerResource: Resource = $rawfile('S20250416165613637594.mp4');
     private windowClass?: window.Window = undefined;

     aboutToAppear(): void {
       (this.getUIContext().getHostContext() as common.UIAbilityContext).windowStage.getMainWindow().then((win) => {
         this.windowClass = win;
       }).catch((err: BusinessError) => {
         console.error(`Failed to get the main window. Cause code: ${err.code}, message: ${err.message}`);
       });
     }

     aboutToDisappear(): void {
       this.setWindowKeepScreenOn(false);
     }

     build() {
       Column() {
         Video({
           src: this.innerResource,
           controller: this.controller
         })
           .margin({bottom: 20})
           .autoPlay(true)
           .objectFit(ImageFit.Contain)
           .onStart(() => {
             // 设置屏幕常亮
             this.setWindowKeepScreenOn(true);
           })
           .onPause(() => {
             // 关闭屏幕常亮
             this.setWindowKeepScreenOn(false);
           })
           .onFinish(() => {
             this.setWindowKeepScreenOn(false);
           })
           .onStop(() => {
             this.setWindowKeepScreenOn(false);
           })
       }
       .height('100%')
       .width('100%')
       .backgroundColor(Color.Black)
     }

     setWindowKeepScreenOn(isKeepScreenOn: boolean): void {
       try {
         this.windowClass?.setWindowKeepScreenOn(isKeepScreenOn, (err: BusinessError) => {
           const errCode: number = err.code;
           if (errCode) {
             console.error(`Failed to set the screen to be always on. Cause code: ${err.code}, message: ${err.message}`);
             return;
           }
           console.info('Succeeded in setting the screen to be always on.');
         });
       } catch (exception) {
         console.error(`Failed to set the screen to be always on. Cause code: ${exception.code}, message: ${exception.message}`);
       }
     }
   }
   ```
