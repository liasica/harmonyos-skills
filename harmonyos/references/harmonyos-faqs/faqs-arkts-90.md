---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-90
title: 如何将ArrayBuffer转成string
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何将ArrayBuffer转成string
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:07+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:1fc979ea44d12c68e6c96868bd9747e8c79037902201f5af5610fc1cd5446aff
---

可以通过util.TextDecoder.create()方法创建一个实例，再通过[decodeToString()](../harmonyos-references/js-apis-util.md#decodetostring12)方法进行转换。

```
1. let decoder = util.TextDecoder.create('utf-8');
2. let str = decoder.decodeToString(new Uint8Array(arrayBuffer));
```

[TextDecoder.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TextDecoder.ets#L36-L37)

开发者可以将 proArrayBuffer 返回的 ArrayBuffer 类型的数据 arrayBufferVal 转换为字符串。

```
1. import { util, buffer } from '@kit.ArkTS';

3. let blobValue: buffer.Blob = new buffer.Blob(['name', 'age', 'sex']);
4. let proArrayBuffer = blobValue.arrayBuffer();

6. proArrayBuffer.then((arrayBufferVal: ArrayBuffer) => {
7. let decoder = util.TextDecoder.create('utf-8');
8. let stringData = decoder.decodeToString(new Uint8Array(arrayBufferVal));
9. console.log('stringData:', stringData);
10. });
```

[TextDecoder.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TextDecoder.ets#L21-L30)
