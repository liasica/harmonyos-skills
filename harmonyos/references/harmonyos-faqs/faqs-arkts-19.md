---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-19
title: 如何实现字符串编解码
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何实现字符串编解码
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:59+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6799f3a31e8b7330a5179e79586e5e1eb45bc7f31449166ee657adb3d24526c8
---

TextEncoder用于将字符串编码为字节数组，支持utf-8、utf-16le/be等编码格式。

TextDecoder用于将字节数组解码为字符串，支持多种编码格式，如utf-8、utf-16le/be、iso-8859和windows-1251。

以下示例代码展示了如何使用TextEncoder和TextDecoder进行字符串编解码：

```
1. import { util } from '@kit.ArkTS';
2. // Create Encoder
3. let textEncoder:util.TextEncoder = new util.TextEncoder('gbk');
4. let buffer:ArrayBuffer = new ArrayBuffer(20);
5. let encodeResult:Uint8Array = new Uint8Array(buffer);

8. // code
9. encodeResult = textEncoder.encodeInto('hello');
10. console.info('Encode result: ', encodeResult);

13. // Create decoder
14. let textDecoder = util.TextDecoder.create('gbk');

17. // decode
18. let decodeResult = textDecoder.decodeToString(encodeResult);
19. console.info('Decode result: ', decodeResult);
```

[TextEncoder.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/TextEncoder.ets#L21-L39)

**参考链接**

[TextEncoder](../harmonyos-references/js-apis-util.md#textencoder)、[TextDecoder](../harmonyos-references/js-apis-util.md#textdecoder)
