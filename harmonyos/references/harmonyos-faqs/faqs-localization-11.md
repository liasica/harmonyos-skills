---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-localization-11
title: 如何实现汉字转拼音
breadcrumb: FAQ > 应用框架开发 > 无障碍和本地化 > 本地化开发（Localization） > 如何实现汉字转拼音
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:34+08:00
doc_updated_at: 2026-03-25
content_hash: sha256:cd0c5541ece25eaba58f8521609d52464da1f7b80c45bfb2f04973ea1a88d11b
---

可以通过Transliterator将汉字转成拼音。

参考代码如下：

```
1. import { i18n } from '@kit.LocalizationKit';

3. let transliterator = i18n.Transliterator.getInstance('Any-Latn');
4. let res: string = transliterator.transform('中国'); // res = 'zhōng guó'

6. // Remove voice parts
7. let voiceRemovedTransliterator = i18n.Transliterator.getInstance('Latin-ASCII');
8. let res2 = voiceRemovedTransliterator.transform(res);
9. console.info('去除声部后拼音为：',res2);
```

[ToPingyin.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/LocalizationKit/entry/src/main/ets/pages/ToPingyin.ets#L21-L29)

**参考链接**

[Transliterator](../harmonyos-references/js-apis-i18n.md#transliterator9)
