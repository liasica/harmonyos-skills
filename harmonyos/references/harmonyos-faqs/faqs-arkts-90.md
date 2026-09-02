---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-90
title: 如何将ArrayBuffer转成string
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何将ArrayBuffer转成string
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ae732f8fabc58362aa061227036d2838043bc14b5d1bb9d11578a2cede72a391
---

可以通过util.TextDecoder.create()方法创建一个实例，再通过[decodeToString()](../harmonyos-references/js-apis-util.md#decodetostring12)方法进行转换。

```ts
let decoder = util.TextDecoder.create('utf-8');
let str = decoder.decodeToString(new Uint8Array(arrayBuffer));
```

开发者可以将 proArrayBuffer 返回的 ArrayBuffer 类型的数据 arrayBufferVal 转换为字符串。

```ts
import { util, buffer } from '@kit.ArkTS';

let blobValue: buffer.Blob = new buffer.Blob(['name', 'age', 'sex']);
let proArrayBuffer = blobValue.arrayBuffer();

proArrayBuffer.then((arrayBufferVal: ArrayBuffer) => {
  let decoder = util.TextDecoder.create('utf-8');
  let stringData = decoder.decodeToString(new Uint8Array(arrayBufferVal));
  console.log('stringData:', stringData);
});
```
