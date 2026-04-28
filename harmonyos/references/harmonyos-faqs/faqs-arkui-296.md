---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-296
title: 如何清除输入框焦点
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何清除输入框焦点
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:16+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d55daf1959c2d324e863c92b0bae6b8bf86fd4709d59fac7191d926b340dfd3b
---

可以使用FocusController的[clearFocus](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#clearfocus12)方法来清除焦点并关闭软键盘，示例代码如下：

```
1. this.getUIContext().getFocusController().clearFocus()
```

[ClearFocus.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ClearFocus.ets#L10-L10)
