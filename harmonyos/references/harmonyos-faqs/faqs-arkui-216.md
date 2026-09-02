---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-216
title: 如何使用iconfont
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何使用iconfont
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0353a26c0ec7771b04d05a7630dd48038aa4ca174fdd5521e69d0fa96b0d2c62
---

使用iconfont时，开发者需先获取字体库的ttf文件，再通过 `font.registerFont` 接口注册。在 `Text` 上使用对应的 unicode 编码即可。参考代码如下：

```ts
import { Font } from '@kit.ArkUI'
@Entry
@Component
struct UseIconFont {
  // Assuming 0000 is the Unicode for the specified icon, developers actually need to obtain Unicode from the ttf file of the registered iconFont
  @State unicode: string = '\u0000';
  aboutToAppear(): void {
    let font: Font = this.getUIContext().getFont();
    font.registerFont({
      familyName: 'iconfont',
      familySrc: 'xxx.ttf'
    })
  }
  build() {
    Row() {
      Column() {
        Text(this.unicode)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .fontFamily('iconfont')
      }
      .width('100%')
    }
    .height('100%')
  }
}
```

**参考链接**

[registerFont](../harmonyos-references/arkts-apis-uicontext-font.md#registerfont)
