---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-20
title: 如何生成UUID的字符串
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何生成UUID的字符串
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f4836eab711c4995fb0bdcd30fb41b02117d0be2dfed7192e53b5f683f1c1d38
---

使用util工具的generateRandomUUID函数可以生成字符串类型的UUID，示例如下：

```
1. let uuid = util.generateRandomUUID(true);
2. console.info("RFC 4122 Version 4 UUID:" + uuid); // Output randomly generated UUID
```

[Uuid.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Uuid.ets#L7-L8)

**参考链接**

[util.generateRandomUUID](../harmonyos-references/js-apis-util.md#utilgeneraterandomuuid9)
