---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-492
title: 如何设置仅文字输入的键盘，即屏蔽键盘中AI功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何设置仅文字输入的键盘，即屏蔽键盘中AI功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0f54c77d881488880148ea4dc4bc00bd9b65d83766f5a108a4b3927479422ca5
---

简单键盘是不具有任何智能功能的键盘。在EntryAbility.ets文件的onWindowStageCreate方法中调用[inputMethod.setSimpleKeyboardEnabled](../harmonyos-references/js-apis-inputmethod.md#inputmethodsetsimplekeyboardenabled20)(true)，即可启用简单键盘模式。相关代码如下：

```ts
onWindowStageCreate(windowStage: window.WindowStage): void {
  // Main window is created, set main page for this ability
  hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
  AppStorage.setOrCreate('windowStage',windowStage);

  windowStage.loadContent('pages/Index', (err) => {
    if (err.code) {
      hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
      return;
    }
    hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
    // Settings Simple Keyboard
    let enable: boolean = true;
    inputMethod.setSimpleKeyboardEnabled(enable);
  });
}
```
