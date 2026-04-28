---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-492
title: 如何设置仅文字输入的键盘，即屏蔽键盘中AI功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何设置仅文字输入的键盘，即屏蔽键盘中AI功能
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:09+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:18384838df96fc57f2ecd64484bca42bb6f6243423dc1ebbbf81dd038d64e7da
---

简单键盘是不具有任何智能功能的键盘。在EntryAbility.ets文件的onWindowStageCreate方法中调用[inputMethod.setSimpleKeyboardEnabled](../harmonyos-references/js-apis-inputmethod.md#inputmethodsetsimplekeyboardenabled20)(true)，即可启用简单键盘模式。相关代码如下：

```
1. onWindowStageCreate(windowStage: window.WindowStage): void {
2. // Main window is created, set main page for this ability
3. hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
4. AppStorage.setOrCreate('windowStage',windowStage);

6. windowStage.loadContent('pages/Index', (err) => {
7. if (err.code) {
8. hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
9. return;
10. }
11. hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
12. // Settings Simple Keyboard
13. let enable: boolean = true;
14. inputMethod.setSimpleKeyboardEnabled(enable);
15. });
16. }
```

[EntryAbilitySimpleKeyboard.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilitySimpleKeyboard.ets#L23-L38)
