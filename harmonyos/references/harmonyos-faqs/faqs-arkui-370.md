---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-370
title: 如何实现沉浸式页面（包括沉浸式状态栏、沉浸式导航条）
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现沉浸式页面（包括沉浸式状态栏、沉浸式导航条）
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:34+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:09534788a18ef6e21275790fecbbaf0ef1dcdb03b0ce45c8b460dd3f39f0eec3
---

**解决措施**

沉浸式页面开发分为以下两步：

1. 实现沉浸式效果。
   * 方案一：使用[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)方法设置窗口为全屏模式。

     ```
     1. import { UIAbility } from '@kit.AbilityKit';
     2. import { window } from '@kit.ArkUI';
     3. import { BusinessError } from '@kit.BasicServicesKit';

     6. export default class EntryAbility extends UIAbility {
     7. onWindowStageCreate(windowStage: window.WindowStage) {
     8. // 1.Get the main window of the application.
     9. let windowClass: window.Window | undefined = undefined;
     10. windowStage.getMainWindow().then(windowClass => {
     11. console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(windowClass));
     12. // 2.Set the window to full screen to achieve immersive effects.
     13. windowClass.setWindowLayoutFullScreen(true).then(() => {
     14. console.info('Succeeded in setting the window layout to full-screen mode.');
     15. }).catch((e: BusinessError) => {
     16. console.error('Failed to set the window layout to full-screen mode. Cause:' + JSON.stringify(e));
     17. })
     18. }).catch((err: BusinessError) => {
     19. console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
     20. })
     21. // 3.Load the corresponding target page for the immersive window.
     22. windowStage.loadContent("pages/Index", (err) => {
     23. if (err.code) {
     24. console.error('Failed to load the content. Cause:' + JSON.stringify(err));
     25. return;
     26. }
     27. console.info('Succeeded in loading the content.');
     28. });
     29. }
     30. };
     ```

     [EntryAbilityImmersivePages.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityImmersivePages.ets#L21-L50)
   * 方案二：设置组件的[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性，扩展组件的安全区域到状态栏和导航栏，从而实现沉浸式。

     ```
     1. @Entry
     2. @Component
     3. struct Example {
     4. build() {
     5. Column() {
     6. Row() {
     7. Text('Top Row')
     8. .fontSize(40)
     9. .textAlign(TextAlign.Center)
     10. .width('100%')
     11. }
     12. .backgroundColor('#F08080')
     13. // Set the top drawing to extend to the status bar
     14. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])

     17. Row() {
     18. Text('ROW2')
     19. .fontSize(40)
     20. }
     21. .backgroundColor(Color.Orange)
     22. .padding(20)

     25. Row() {
     26. Text('ROW3')
     27. .fontSize(40)
     28. }
     29. .backgroundColor(Color.Orange)
     30. .padding(20)

     33. Row() {
     34. Text('ROW4')
     35. .fontSize(40)
     36. }
     37. .backgroundColor(Color.Orange)
     38. .padding(20)

     41. Row() {
     42. Text('ROW5')
     43. .fontSize(40)
     44. }
     45. .backgroundColor(Color.Orange)
     46. .padding(20)

     49. Row() {
     50. Text('Bottom Row')
     51. .fontSize(40)
     52. .textAlign(TextAlign.Center)
     53. .width('100%')
     54. }
     55. .backgroundColor(Color.Orange)
     56. // Set the bottom drawing to extend to the navigation bar
     57. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
     58. }
     59. .width('100%')
     60. .height('100%')
     61. .alignItems(HorizontalAlign.Center)
     62. .backgroundColor('#008000')
     63. .justifyContent(FlexAlign.SpaceBetween)
     64. }
     65. }
     ```

     [ImplementImmersivePages.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementImmersivePages.ets#L21-L85)
2. 处理避让区域与页面内容的适配问题。

   避让区包含状态栏中的电量、时间等系统信息，或手势交互如导航栏点击或上滑。实现应用页面沉浸式效果后，可能会与避让区产生UI元素遮挡、视觉违和或交互冲突等问题。开发者可针对不同场景选择以下方式对避让区和应用页面进行适配。

   * 使用[setWindowSystemBarEnable()](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarenable9)方法或[setSpecificSystemBarEnabled()](../harmonyos-references/arkts-apis-window-window.md#setspecificsystembarenabled11)方法设置状态栏和导航栏的显隐。
   * 使用[setWindowSystemBarProperties()](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)方法设置状态栏和导航栏的样式。
   * 使用[getWindowAvoidArea()](../harmonyos-references/js-apis-arkui-uiextension.md#getwindowavoidarea)方法获取避让区域的高度，据此设置应用页面内容的上下padding实现避让状态栏和导航栏。
   * 使用[getCutoutInfo()](../harmonyos-references/js-apis-display.md#getcutoutinfo9-1)方法获取挖孔区域宽高和位置信息，设置对应避让元素的margin实现挖孔区避让。
   * 对于需要动态调整的场景推荐使用getWindowAvoidArea()方法。

**参考链接**

[窗口沉浸式](../best-practices/bpta-multi-device-window-immersive.md)
