---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/displaysync-ui
title: 请求UI绘制帧率
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 使用可变帧率能力定制不同内容的绘制帧率 > 请求UI绘制帧率
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:49+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:25ab4c1c4c5e8b5da281cffcf143a63b48c72da6d970629769834facda63cbfc
---

如果开发者需要以独立的帧率绘制更新操作UI界面时，可以通过DisplaySync来实现。应用中绘制内容的帧率可以使用DisplaySync实例来控制，具体请查阅[@ohos.graphics.displaySync (可变帧率)](../harmonyos-references/js-apis-graphics-displaysync.md)。

## 开发步骤

此处以不同帧率改变文本组件字体大小为例，来模拟不同UI绘制帧率的效果。

1. 导入模块。

   ```typescript
   import { displaySync } from '@kit.ArkGraphics2D';
   ```
2. 定义和构建DisplaySync对象。

   ```typescript
   @Entry
   @Component
   struct Index {
     // ...

     private backDisplaySyncSlow: displaySync.DisplaySync | undefined = undefined;
     private backDisplaySyncFast: displaySync.DisplaySync | undefined = undefined;
     // ...
   }
   ```
3. 定义两个文本组件。

   ```typescript
   @State drawFirstSize: number = 25;
   @State drawSecondSize: number = 25;

   // ...

   @Builder
   doSomeRenderFirst() {
     Text('30')
       .fontSize(this.drawFirstSize)
   }

   @Builder
   doSomeRenderSecond() {
     Text('60')
       .fontSize(this.drawSecondSize)
   }
   ```
4. 通过DisplaySync实例设置帧率和注册订阅函数。

   **说明** 

   订阅函数运行于UI主线程，故涉及UI线程的耗时操作不应运行于订阅函数中，以免影响性能。

   ```typescript
   CreateDisplaySyncSlow() {
     let range: ExpectedFrameRateRange = {
       expected: 30,
       min: 0,
       max: 120
     };

     let draw30 = (intervalInfo: displaySync.IntervalInfo) => {
       if (this.isBigger_30) {
         this.drawFirstSize += 1;
         if (this.drawFirstSize > 150) {
           this.isBigger_30 = false;
         }
       } else {
         this.drawFirstSize -= 1;
         if (this.drawFirstSize < 25) {
           this.isBigger_30 = true;
         }
       }
     };

     this.backDisplaySyncSlow = displaySync.create();
     this.backDisplaySyncSlow.setExpectedFrameRateRange(range);
     this.backDisplaySyncSlow.on("frame", draw30);
   }
   ```
5. 开始每帧回调。

   ```typescript
   Button('Start')
     .id('CustomDrawStart')
     .fontSize(14)
     .fontWeight(500)
     .margin({ bottom: 10, left: 5 })
     .fontColor(Color.White)
     .onClick((): void => {
       if (this.backDisplaySyncSlow == undefined) {
         this.CreateDisplaySyncSlow();
       }
       if (this.backDisplaySyncFast == undefined) {
         this.CreateDisplaySyncFast();
       }
       if (this.backDisplaySyncSlow) {
         this.backDisplaySyncSlow.start();
       }
       if (this.backDisplaySyncFast) {
         this.backDisplaySyncFast.start();
       }
     })
     .width('20%')
     .height(40)
     .shadow(ShadowStyle.OUTER_DEFAULT_LG)
   ```

   **说明** 

   创建的DisplaySync实例在start使能后需要在aboutToDisappear函数中进行stop操作并置空，避免内存泄漏问题。

   ```typescript
   aboutToDisappear() {
     if (this.backDisplaySyncSlow) {
       this.backDisplaySyncSlow.stop();
       this.backDisplaySyncSlow = undefined;
     }
     if (this.backDisplaySyncFast) {
       this.backDisplaySyncFast.stop();
       this.backDisplaySyncFast = undefined;
     }
   }
   ```
6. 结束每帧回调。

   ```typescript
   Button('Stop')
     .id('CustomDrawStop')
     .fontSize(14)
     .fontWeight(500)
     .margin({ bottom: 10, left: 5 })
     .fontColor(Color.White)
     .onClick((): void => {
       if (this.backDisplaySyncSlow) {
         this.backDisplaySyncSlow.stop();
       }
       if (this.backDisplaySyncFast) {
         this.backDisplaySyncFast.stop();
       }
     })
     .width('20%')
     .height(40)
     .shadow(ShadowStyle.OUTER_DEFAULT_LG)
   ```
