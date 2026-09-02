---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-19
title: 如何实现字符串编解码
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何实现字符串编解码
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:49afc909c80504c6e69143d254b77b9f820402f04eef7c93e481a24c8c53659c
---

TextEncoder用于将字符串编码为字节数组，支持utf-8、utf-16le/be等编码格式。

TextDecoder用于将字节数组解码为字符串，支持多种编码格式，如utf-8、utf-16le/be、iso-8859和windows-1251。

以下示例代码展示了如何使用TextEncoder和TextDecoder进行字符串编解码：

```ts
import { util } from '@kit.ArkTS';
// Create Encoder
let textEncoder:util.TextEncoder = new util.TextEncoder('gbk');
let buffer:ArrayBuffer = new ArrayBuffer(20);
let encodeResult:Uint8Array = new Uint8Array(buffer);

// code
encodeResult = textEncoder.encodeInto('hello');
console.info('Encode result: ', encodeResult);

// Create decoder
let textDecoder = util.TextDecoder.create('gbk');

// decode
let decodeResult = textDecoder.decodeToString(encodeResult);
console.info('Decode result: ', decodeResult);
```

**参考链接**

[TextEncoder](../harmonyos-references/js-apis-util.md#textencoder)、[TextDecoder](../harmonyos-references/js-apis-util.md#textdecoder)
