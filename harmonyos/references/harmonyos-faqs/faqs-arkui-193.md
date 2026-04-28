---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-193
title: 应用如何设置隐藏顶部的状态栏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 应用如何设置隐藏顶部的状态栏
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:53+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:dc105f87da05b70a9b80172353a9ecbe6f9526fd60566485ab4e6e16b0712688
---

在UIAbility的onWindowStageCreate生命周期中，设置setWindowSystemBarEnable接口。

```
1. onWindowStageCreate(windowStage: window.WindowStage): void {
2. windowStage.getMainWindowSync().setWindowSystemBarEnable([])
3. // ...
4. }
```

[EntryAbilityForHideBar.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityForHideBar.ets#L21-L37)

**参考链接**

[体验窗口沉浸式能力](../harmonyos-guides/application-window-stage.md#体验窗口沉浸式能力)
