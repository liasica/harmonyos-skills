---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-11
title: 如何使用实现汉字转拼音
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 如何使用实现汉字转拼音
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5a5fa166b9e44c636ab0b6e9cbbd39cccd3bd4e1dc49d382e9ac7d19f5e25fc8
---

可以通过Transliterator将汉字转成拼音。

参考代码如下：

```typescript
import { i18n } from '@kit.LocalizationKit';

let transliterator = i18n.Transliterator.getInstance('Any-Latn');
let res: string = transliterator.transform('中国'); // res = 'zhōng guó'

// Remove voice parts
let voiceRemovedTransliterator = i18n.Transliterator.getInstance('Latin-ASCII');
let res2 = voiceRemovedTransliterator.transform(res);
console.info('去除声部后拼音为：',res2);
```

**参考链接**

[Transliterator](../harmonyos-references/js-apis-i18n.md#transliterator9)
