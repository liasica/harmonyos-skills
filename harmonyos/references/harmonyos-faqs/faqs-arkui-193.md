---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-193
title: 应用如何设置隐藏顶部的状态栏
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 应用如何设置隐藏顶部的状态栏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:57fb78b8a7ecbb74bf0139df8b9f30e2a3972eb54b9df64fde8d9d46c43ee67b
---

在UIAbility的onWindowStageCreate生命周期中，设置setWindowSystemBarEnable接口。

```ts
onWindowStageCreate(windowStage: window.WindowStage): void {
  windowStage.getMainWindowSync().setWindowSystemBarEnable([])
  // ...
}
```

**参考链接**

[窗口沉浸式](../harmonyos-guides/immersive-window-feature.md)
