---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-53
title: 如何在键盘弹出时，让内容上移，而不是整个页面上移
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何在键盘弹出时，让内容上移，而不是整个页面上移
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ba2a8586af9e362111bc545dc767ff2a9ff2eb344045d9dd246a8862fad34720
---

可通过setKeyboardAvoidMode接口设置键盘避让模式为KeyboardAvoidMode.RESIZE，表示压缩模式。参考代码如下：

```
1. // EntryAbility.ets
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. import { window, KeyboardAvoidMode, UIContext } from '@kit.ArkUI';

7. export default class EntryAbility extends UIAbility {
8. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
9. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
10. }

13. onDestroy(): void {
14. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
15. }
16. onWindowStageCreate(windowStage: window.WindowStage) {
17. // Main window is created, set main page for this ability
18. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

21. windowStage.loadContent('pages/Index', (err, data) => {
22. let uiContext :UIContext = windowStage.getMainWindowSync().getUIContext();
23. uiContext.setKeyboardAvoidMode(KeyboardAvoidMode.RESIZE);
24. if (err.code) {
25. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
26. return;
27. }
28. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
29. });
30. }

33. onWindowStageDestroy(): void {
34. // Main window is destroyed, release UI related resources
35. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
36. }

39. onForeground(): void {
40. // Ability has brought to foreground
41. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
42. }

45. onBackground(): void {
46. // Ability has back to background
47. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
48. }
49. }
```

[EntryAbilityKeyboardAvoidMode.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityKeyboardAvoidMode.ets#L21-L69)

**参考链接**

[setKeyboardAvoidMode](../harmonyos-references/arkts-apis-uicontext-uicontext.md#setkeyboardavoidmode11)
