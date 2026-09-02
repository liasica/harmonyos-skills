---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-15
title: ArkTS中有类似java中的System.arraycopy数组复制的方法吗
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > ArkTS中有类似java中的System.arraycopy数组复制的方法吗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f9ea0a6bad6b5638003d23ed205a4a2e61bc30f37c3b117b66b24ad77f29dee9
---

可以通过 buffer.concat() 方法，将数组中的内容复制到新的 Buffer 对象中并返回。参考代码如下：

```ts
import { buffer } from '@kit.ArkTS';

let buf1 = buffer.from("1234");
let buf2 = buffer.from("abcd");
let buf = buffer.concat([buf1, buf2]);
console.info(buf.toString('hex'));
// Output result:3132333461626364
```

**参考链接**

[buffer.concat](../harmonyos-references/js-apis-buffer.md#bufferconcat)
