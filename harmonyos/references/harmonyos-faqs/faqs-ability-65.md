---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-65
title: UIAbility和UIExtensionAbility有什么区别？分别推荐在什么场景使用
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > UIAbility和UIExtensionAbility有什么区别？分别推荐在什么场景使用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:46+08:00
doc_updated_at: 2026-03-20
content_hash: sha256:87f35200a8e14bd3b2efae0b03ec31fbb4cfcc2db93943d3fe5035ecb942dd75
---

UIAbility 用于实现独立界面，UIExtensionAbility 用于功能扩展。

* UIAbility组件包含UI，用于与用户交互。UIAbility运行时，任务列表中会显示对应的任务视图。建议在主界面、视频播放页、设置页面等场景下使用。

  ```
  1. import { UIAbility } from "@kit.AbilityKit";
  2. import { window } from "@kit.ArkUI";

  4. // MainAbility.ets
  5. export default class MainAbility extends UIAbility {
  6. onWindowStageCreate(windowStage: window.WindowStage) {
  7. windowStage.loadContent('pages/MainPage', (err) => {
  8. if (err) {
  9. console.error('Page loading failed');
  10. }
  11. });
  12. }
  13. }
  ```

  [MainAbility.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/MainAbility.ets#L21-L34)
* UIExtensionAbility组件是一种带UI的扩展组件。UIExtensionAbility运行时没有独立窗口，而是作为宿主的节点嵌入宿主窗口显示，任务列表中也没有对应的任务视图。推荐用于悬浮窗、快捷菜单等场景。

  ```
  1. import { UIExtensionAbility, AbilityConstant } from '@kit.AbilityKit';

  3. export default class UIExtAbility extends UIExtensionAbility {
  4. onCreate(launchParam: AbilityConstant.LaunchParam) {
  5. console.log(`onCreate, launchParam: ${JSON.stringify(launchParam)}`);
  6. }
  7. }
  ```

  [UIExtAbility.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/AbilityKit/entry/src/main/ets/pages/UIExtAbility.ets#L21-L27)

**参考链接**

[UIAbility组件概述](../harmonyos-guides/uiability-overview.md)
