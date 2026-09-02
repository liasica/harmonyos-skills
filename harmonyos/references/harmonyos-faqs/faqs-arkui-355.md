---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-355
title: 汉字转拼音如何去掉音标
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 汉字转拼音如何去掉音标
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f2ffc82e65666b4bdf700eeab8c57714fab96672e9022870fabf425869495cda
---

可以使用“Any-Latn”将汉字内容转写为拼音，再使用“Latin-ASCII”去除声调符号。示例代码如下：

```ts
import { i18n } from '@kit.LocalizationKit';

@Entry
@Component
struct RemovePinyin {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .fontSize(50)
        .onClick(() => {
          // 1. Chinese characters to Pinyin
          let transliterator1 = i18n.Transliterator.getInstance('Any-Latn');
          let res = transliterator1.transform('中国');
          // 2. Remove tone marks
          let transliterator2 = i18n.Transliterator.getInstance('Latin-ASCII');
          let pinyinResult = transliterator2.transform(res);
          console.info('pinyinResult: ' + pinyinResult);
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
