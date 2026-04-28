---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-15
title: ArkTS中有类似Java中的System.arraycopy数组复制的方法吗
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS中有类似Java中的System.arraycopy数组复制的方法吗
category: harmonyos-faqs
scraped_at: 2026-04-28T08:23:58+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:73c8510628f433d462324d9972a11df2c26e2f72124565d7a61497f8e62a6b74
---

可以通过 buffer.concat() 方法，将数组中的内容复制到新的 Buffer 对象中并返回。参考代码如下：

```
1. import { buffer } from '@kit.ArkTS';

3. let buf1 = buffer.from("1234");
4. let buf2 = buffer.from("abcd");
5. let buf = buffer.concat([buf1, buf2]);
6. console.info(buf.toString('hex'));
7. // Output result:3132333461626364
```

[Buffer.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkTS/entry/src/main/ets/pages/Buffer.ets#L21-L27)

**参考链接**

[buffer.concat](../harmonyos-references/js-apis-buffer.md#bufferconcat)
