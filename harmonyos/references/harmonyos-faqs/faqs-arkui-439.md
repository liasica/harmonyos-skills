---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-439
title: ArcSwiper如何适配表冠
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > ArcSwiper如何适配表冠
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:54+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1e5e75bf7d8d4297231da0ba4494c8daa9d28d2cb47a8c85a3d89328f48aad1c
---

可以滑动的组件需要适配旋转表冠，默认支持的组件在获焦时即可响应表冠事件。

1. 默认支持组件只需要添加.focusable(true)、 .focusOnTouch(true)、.defaultFocus(true)属性获焦即可响应。

   默认支持表冠事件的组件: Slider、DatePicker、TextPicker、 TimePicker、Scroll、List、Grid、WaterFlow、ArcList、Refresh和Swiper。

   示例代码如下：

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

   6. build() {
   7. Column() {
   8. List({ space: 20, initialIndex: 0 }) {
   9. ForEach(this.arr, (item: number) => {
   10. ListItem() {
   11. Button('' + item)
   12. .width('100%')
   13. .height(100)
   14. .fontSize(16)
   15. }
   16. .onClick(() => {
   17. })
   18. }, (item: string) => item)
   19. }
   20. .focusable(true)
   21. .defaultFocus(true)
   22. .focusOnTouch(true) // After the list component is focused, it can respond to the sliding control of the rotating crown
   23. .width('90%')
   24. .height('100%')
   25. }
   26. .width('100%')
   27. .height('100%')
   28. .backgroundColor(0xDCDCDC)
   29. .padding({ top: 5 })
   30. }
   31. }
   ```

   [CompatibleCrownExampleOne.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CompatibleCrownExampleOne.ets#L21-L52)
2. 其他组件可以通过onDigitalCrown监听表冠事件。

   示例代码如下：

   ```
   1. @Entry
   2. @Component
   3. struct CityList {
   4. @State message: string = 'onDigitalCrown';

   6. build() {
   7. Column() {
   8. Row() {
   9. Stack() {
   10. Text(this.message)
   11. .fontSize(20)
   12. .fontColor(Color.White)
   13. .backgroundColor('#262626')
   14. .textAlign(TextAlign.Center)
   15. .focusable(true)
   16. .focusOnTouch(true)
   17. .defaultFocus(true)
   18. .borderWidth(2)
   19. .width(223)
   20. .height(223)
   21. .borderRadius(110)
   22. .onDigitalCrown((event: CrownEvent) => {
   23. event.stopPropagation();
   24. this.message = 'CrownEvent\n\n' + JSON.stringify(event);
   25. console.debug('action:%d, angularVelocity:%f,degree:%f,timestamp:%f', event.action, event.angularVelocity,
   26. event.degree, event.timestamp);
   27. })
   28. }
   29. }
   30. }
   31. }
   32. }
   ```

   [CompatibleCrownExampleTwo.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CompatibleCrownExampleTwo.ets#L21-L53)
3. List组件旋转表冠在if/else的else场景里不会自动获焦，旋转表冠不生效。在List的onAppear方法中调用requestFocus手动获焦，示例代码如下：

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
   5. @State isLoading: boolean = true;

   7. onPageShow(): void {
   8. setTimeout(() => {
   9. this.isLoading = false;
   10. }, 3000)
   11. }

   13. build() {
   14. Column() {
   15. if (this.isLoading) {
   16. Text('数据加载中')
   17. } else {
   18. List({ space: 20, initialIndex: 0 }) {
   19. ForEach(this.arr, (item: number) => {
   20. ListItem() {
   21. Button('' + item)
   22. .width('100%')
   23. .height(100)
   24. .fontSize(16)
   25. }
   26. .onClick(() => {
   27. })
   28. }, (item: string) => item)
   29. }
   30. .onAppear(() => {
   31. try {
   32. this.getUIContext().getFocusController().requestFocus('test');
   33. } catch (error) {
   34. console.error('requestFocus failed code is ' + error.code + 'message is ' + error.message);
   35. }
   36. })
   37. .id('test')
   38. .focusable(true)
   39. .defaultFocus(true)
   40. .focusOnTouch(true) // After the list component is focused, it can respond to the sliding control of the rotating crown
   41. .width('90%')
   42. .height('100%')
   43. }
   44. }
   45. .width('100%')
   46. .height('100%')
   47. .backgroundColor(0xDCDCDC)
   48. .padding({ top: 5 })
   49. }
   50. }
   ```

   [CompatibleCrownExampleThree.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CompatibleCrownExampleThree.ets#L21-L71)

**参考链接**

[表冠事件](../harmonyos-references/ts-universal-events-crown.md)

[焦点控制](../harmonyos-references/ts-universal-attributes-focus.md)

[ArcSwiper示例](../harmonyos-references/ts-container-arcswiper.md#示例)
