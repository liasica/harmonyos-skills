---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-8
title: 数字支持货币分隔符显示吗
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 数字支持货币分隔符显示吗
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:34+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1b0aa8d7377bd2bb0e151cac24e0083a9c9b9a957c64baa7a314b09875259d6b
---

可以通过NumberFormat设置数字的显示格式

```
1. let numberFormat = new Intl.NumberFormat('zh-CN');
2. console.info(`numfmt: ${numberFormat.format(1000000)}`);
```

[CurrencyDelimiter.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/LocalizationKit/entry/src/main/ets/pages/CurrencyDelimiter.ets#L21-L22)

**参考链接**

[numberformat使用参考](../harmonyos-references/js-apis-intl.md#numberformat)
