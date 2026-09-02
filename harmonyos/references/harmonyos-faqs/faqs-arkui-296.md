---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-296
title: 如何清除输入框焦点
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何清除输入框焦点
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:b49fd6cc8006d464f6360794013235d8a059a80702f6ecddb2e1c0edd31e3269
---

可以使用FocusController的[clearFocus](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#clearfocus12)方法来清除焦点并关闭软键盘，示例代码如下：

```typescript
this.getUIContext().getFocusController().clearFocus()
```
