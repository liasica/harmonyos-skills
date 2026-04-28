---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-366
title: 如何实现通过侧滑手势关闭打开的悬浮框
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现通过侧滑手势关闭打开的悬浮框
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:33+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:3b98fc5e11384a0f4daf8df42c02992aab1bd6cffb8b49d78a232cd07c6ccfc9
---

在页面的onBackPress()生命周期函数中隐藏子窗口。示例如下：

1. 在EntryAbility的onWindowStageCreate方法中创建子窗口。

   ```
   1. onWindowStageCreate(windowStage: window.WindowStage): void {
   2. // Create application subwindow
   3. let windowClass: window.Window | undefined = undefined;
   4. windowStage.createSubWindow('mySubWindow', (err: BusinessError, data) => {
   5. if (err.code) {
   6. console.error(`Failed to create the subwindow. Cause code: ${err.code}, message: ${err.message}`);
   7. return;
   8. }
   9. windowClass = data;
   10. console.info('Succeeded in creating the subwindow. Data: ' + JSON.stringify(data));
   11. // After the child window is created successfully, set the position, size, and related properties of the child window.
   12. windowClass.moveWindowTo(300, 300);
   13. windowClass.resize(200, 200);
   14. windowClass.setWindowTouchable(true);
   15. // Load the corresponding target page for the child window.
   16. windowClass.setUIContent('pages/Index',(err: BusinessError) => {
   17. if (err.code) {
   18. console.error(`Failed to load the content. Cause code: ${err.code}, message: ${err.message}`);
   19. return;
   20. }
   21. if (windowClass) {
   22. windowClass.setWindowBackgroundColor('#64b38c');
   23. }
   24. });
   25. (windowClass as window.Window).showWindow();
   26. })
   27. // ...
   28. }
   ```

   [EntryAbilityFloatingFrame.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityFloatingFrame.ets#L29-L56)
2. Page中使用onBackPress监听并销毁子窗口。

   ```
   1. import { window } from '@kit.ArkUI';

   3. @Entry
   4. @Component
   5. struct CloseWindowDemo {
   6. @State message: string = 'Hello World';

   8. onBackPress(): boolean | void {
   9. console.log('Triggered');
   10. const subWindow = window.findWindow('mySubWindow');
   11. if (subWindow) {
   12. subWindow.destroyWindow();
   13. }
   14. return true;
   15. }

   17. build() {
   18. RelativeContainer() {
   19. Text(this.message)
   20. .id('HelloWorld')
   21. .fontSize(20)
   22. .fontWeight(FontWeight.Bold)
   23. .alignRules({
   24. center: { anchor: '__container__', align: VerticalAlign.Center },
   25. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   26. })
   27. }
   28. .height('100%')
   29. .width('100%')
   30. }
   31. }
   ```

   [SlideGestureToCloseFloatingFrame.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SlideGestureToCloseFloatingFrame.ets#L21-L52)
