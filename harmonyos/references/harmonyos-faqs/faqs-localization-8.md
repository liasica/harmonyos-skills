---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-8
title: 数字支持货币分隔符显示吗
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 数字支持货币分隔符显示吗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:45ae125e5dd915dba6e739e556d43ace4cbdc119528c30b8d41285b19e21ab3c
---

可以通过NumberFormat设置数字的显示格式

```typescript
let numberFormat = new Intl.NumberFormat('zh-CN');
console.info(`numfmt: ${numberFormat.format(1000000)}`);
```

**参考链接**

[numberformat使用参考](../harmonyos-references/js-apis-intl.md#numberformat)
