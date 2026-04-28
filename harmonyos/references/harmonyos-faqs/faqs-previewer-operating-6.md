---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-previewer-operating-6
title: 预览窗口顶部和底部出现白边
breadcrumb: FAQ > DevEco Studio > 界面预览 > 预览窗口顶部和底部出现白边
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5040cfed7864e0285424f35f7b943601a1a67a44419acc94635b17dea776683a
---

**问题现象**

预览窗口顶部和底部出现白边。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/zmKSdQosQJCjvC94aERxHA/zh-cn_image_0000002229603709.png?HW-CC-KV=V1&HW-CC-Date=20260428T002905Z&HW-CC-Expire=86400&HW-CC-Sign=3B8F7F6DC755625A27D4ECF3062BD25E8DC8EEC2BA58C217E8E04368123CB6A7)

**解决措施**

这是应用了沉浸式的特性，在沉浸式布局中，状态栏和导航条区域称为避让区，其余区域称为安全区。在默认情况下，开发者的组件被布局在安全区内。如果开发者希望将页面布局应用到全屏窗口，可以采用如下两种方式：

* 方法一：预览场景下，使用[expandSafeArea()](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)扩展安全区域属性。

  ```
  1. //Index.ets
  2. @Entry
  3. @Component
  4. struct Index {
  5. @State message: string = 'Hello World';

  8. build() {
  9. RelativeContainer() {
  10. Text(this.message)
  11. .id('HelloWorld')
  12. .fontSize(50)
  13. .fontWeight(FontWeight.Bold)
  14. .alignRules({
  15. center: { anchor: '__container__', align: VerticalAlign.Center },
  16. middle: { anchor: '__container__', align: HorizontalAlign.Center }
  17. })
  18. }
  19. .height('100%')
  20. .width('100%')
  21. .backgroundColor('#008000')
  22. .expandSafeArea([SafeAreaType.SYSTEM])
  23. }
  24. }
  ```

  [ExpandSafeArea.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/PreviewerOperating/entry/src/main/ets/pages/ExpandSafeArea.ets#L3-L26)

* 方法二：预览调试时，调用[setWindowLayoutFullScreen()](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)接口设置窗口全屏。

  ```
  1. // EntryAbility.ets
  2. onWindowStageCreate(windowStage: window.WindowStage): void {
  3. // Main window is created, set main page for this ability
  4. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
  5. windowStage.loadContent('pages/Index', (err) => {
  6. // ...
  7. });
  8. windowStage.getMainWindow((err, data) => {
  9. if (!err.code) {
  10. data.setWindowLayoutFullScreen(true)
  11. }
  12. });
  13. }
  ```

  [EntryAbility.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/PreviewerOperating/entry/src/main/ets/entryability/EntryAbility.ets#L22-L40)

**参考链接**

[开发应用沉浸式效果](../harmonyos-guides/arkts-develop-apply-immersive-effects.md)
