---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-20
title: 如何生成UUID的字符串
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何生成UUID的字符串
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ae7aad01618b7ec6ad3ba22c4e70034982947b788219c4273ab6ce57e0766cd3
---

使用util工具的generateRandomUUID函数可以生成字符串类型的UUID，示例如下：

```ts
let uuid = util.generateRandomUUID(true);
console.info("RFC 4122 Version 4 UUID:" + uuid); // Output randomly generated UUID
```

**参考链接**

[util.generateRandomUUID](../harmonyos-references/js-apis-util.md#utilgeneraterandomuuid9)
