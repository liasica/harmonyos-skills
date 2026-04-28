---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-355
title: 汉字转拼音如何去掉声调符号
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 汉字转拼音如何去掉声调符号
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9263267e0974d0e1a5709ad42b48b87a73119ba4e457304a397103bcacb649a0
---

可以使用“Any-Latn”将汉字内容转写为拼音，再使用“Latin-ASCII”去除声调符号。示例代码如下：

```
1. import { i18n } from '@kit.LocalizationKit';

3. @Entry
4. @Component
5. struct RemovePinyin {
6. @State message: string = 'Hello World';

8. build() {
9. RelativeContainer() {
10. Text(this.message)
11. .fontSize(50)
12. .onClick(() => {
13. // 1. Chinese characters to Pinyin
14. let transliterator1 = i18n.Transliterator.getInstance('Any-Latn');
15. let res = transliterator1.transform('中国');
16. // 2. Remove tone marks
17. let transliterator2 = i18n.Transliterator.getInstance('Latin-ASCII');
18. let pinyinResult = transliterator2.transform(res);
19. console.info('pinyinResult: ' + pinyinResult);
20. })
21. }
22. .height('100%')
23. .width('100%')
24. }
25. }
```

[ConvertChineseCharactersToPinyin.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ConvertChineseCharactersToPinyin.ets#L21-L46)
