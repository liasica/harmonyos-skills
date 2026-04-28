---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/displaysync-ui
title: 请求UI绘制帧率
breadcrumb: 指南 > 图形 > ArkGraphics 2D（方舟2D图形服务） > 使用可变帧率能力定制不同内容的绘制帧率 > 请求UI绘制帧率
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:50ae843045d5b81892ed2aaff7c653e715310ff571968d5834dd19e9760d81e4
---

如果开发者需要以独立的帧率绘制更新操作UI界面时，可以通过DisplaySync来实现。应用中绘制内容的帧率可以使用DisplaySync实例来控制，具体请查阅[@ohos.graphics.displaySync (可变帧率)](../harmonyos-references/js-apis-graphics-displaysync.md)。

## 开发步骤

此处以不同帧率改变文件组件字体大小为例，来模拟不同UI绘制帧率的效果。

1. 导入模块。

   ```
   1. import { displaySync } from '@kit.ArkGraphics2D';
   ```

   [CustomDrawDisplaySync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/ets/DispalySync/CustomDrawDisplaySync.ets#L16-L18)
2. 定义和构建DisplaySync对象。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. // ...

   6. private backDisplaySyncSlow: displaySync.DisplaySync | undefined = undefined;
   7. private backDisplaySyncFast: displaySync.DisplaySync | undefined = undefined;
   8. // ...
   9. }
   ```

   [CustomDrawDisplaySync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/ets/DispalySync/CustomDrawDisplaySync.ets#L24-L211)
3. 定义两个文本组件。

   ```
   1. @State drawFirstSize: number = 25;
   2. @State drawSecondSize: number = 25;

   4. // ...

   6. @Builder
   7. doSomeRenderFirst() {
   8. Text('30')
   9. .fontSize(this.drawFirstSize)
   10. }

   12. @Builder
   13. doSomeRenderSecond() {
   14. Text('60')
   15. .fontSize(this.drawSecondSize)
   16. }
   ```

   [CustomDrawDisplaySync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/ets/DispalySync/CustomDrawDisplaySync.ets#L28-L53)
4. 通过DisplaySync实例设置帧率和注册订阅函数。

   说明

   订阅函数运行于UI主线程，故涉及UI线程的耗时操作不应运行于订阅函数中，以免影响性能。

   ```
   1. CreateDisplaySyncSlow() {
   2. let range: ExpectedFrameRateRange = {
   3. expected: 30,
   4. min: 0,
   5. max: 120
   6. };

   8. let draw30 = (intervalInfo: displaySync.IntervalInfo) => {
   9. if (this.isBigger_30) {
   10. this.drawFirstSize += 1;
   11. if (this.drawFirstSize > 150) {
   12. this.isBigger_30 = false;
   13. }
   14. } else {
   15. this.drawFirstSize -= 1;
   16. if (this.drawFirstSize < 25) {
   17. this.isBigger_30 = true;
   18. }
   19. }
   20. };

   22. this.backDisplaySyncSlow = displaySync.create();
   23. this.backDisplaySyncSlow.setExpectedFrameRateRange(range);
   24. this.backDisplaySyncSlow.on("frame", draw30);
   25. }
   ```

   [CustomDrawDisplaySync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/ets/DispalySync/CustomDrawDisplaySync.ets#L55-L81)
5. 开始每帧回调。

   ```
   1. Button('Start')
   2. .id('CustomDrawStart')
   3. .fontSize(14)
   4. .fontWeight(500)
   5. .margin({ bottom: 10, left: 5 })
   6. .fontColor(Color.White)
   7. .onClick((): void => {
   8. if (this.backDisplaySyncSlow == undefined) {
   9. this.CreateDisplaySyncSlow();
   10. }
   11. if (this.backDisplaySyncFast == undefined) {
   12. this.CreateDisplaySyncFast();
   13. }
   14. if (this.backDisplaySyncSlow) {
   15. this.backDisplaySyncSlow.start();
   16. }
   17. if (this.backDisplaySyncFast) {
   18. this.backDisplaySyncFast.start();
   19. }
   20. })
   21. .width('20%')
   22. .height(40)
   23. .shadow(ShadowStyle.OUTER_DEFAULT_LG)
   ```

   [CustomDrawDisplaySync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/ets/DispalySync/CustomDrawDisplaySync.ets#L135-L159)

   说明

   创建的DisplaySync实例在start使能后需要aboutToDisappear函数中进行stop操作并置空，避免内存泄漏问题。

   ```
   1. aboutToDisappear() {
   2. if (this.backDisplaySyncSlow) {
   3. this.backDisplaySyncSlow.stop();
   4. this.backDisplaySyncSlow = undefined;
   5. }
   6. if (this.backDisplaySyncFast) {
   7. this.backDisplaySyncFast.stop();
   8. this.backDisplaySyncFast = undefined;
   9. }
   10. }
   ```

   [CustomDrawDisplaySync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/ets/DispalySync/CustomDrawDisplaySync.ets#L109-L120)
6. 结束每帧回调。

   ```
   1. Button('Stop')
   2. .id('CustomDrawStop')
   3. .fontSize(14)
   4. .fontWeight(500)
   5. .margin({ bottom: 10, left: 5 })
   6. .fontColor(Color.White)
   7. .onClick((): void => {
   8. if (this.backDisplaySyncSlow) {
   9. this.backDisplaySyncSlow.stop();
   10. }
   11. if (this.backDisplaySyncFast) {
   12. this.backDisplaySyncFast.stop();
   13. }
   14. })
   15. .width('20%')
   16. .height(40)
   17. .shadow(ShadowStyle.OUTER_DEFAULT_LG)
   ```

   [CustomDrawDisplaySync.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkGraphics2D/DisplaySync/entry/src/main/ets/DispalySync/CustomDrawDisplaySync.ets#L161-L179)
