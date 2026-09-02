---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-361
title: Button组件无法设置字体最大、最小值
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Button组件无法设置字体最大、最小值
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c232bae8df6b2cef1828100d9767d431b2991eef1c4f62fc76be4c389d15afa3
---

Button组件的[labelStyle](../harmonyos-references/ts-basic-components-button.md#labelstyle10)属性可以设置按钮标签文本和字体的样式。示例代码如下

```ts
@Entry
@Component
struct FontSizeButtonExample {
  @State text: string = 'hello';
  @State widthShortSize: number = 300;

  build() {
    Row() {
      Button(this.text)
        .width(this.widthShortSize)
        .height(100)
        //// Set the font size range to 20-40vp，Automatically adjust during actual rendering.
        .labelStyle({
          overflow: TextOverflow.Clip,
          maxLines: 1,
          minFontSize: 20,
          maxFontSize: 40,
          font: {
            size: 30,
            weight: FontWeight.Bolder,
            family: 'cursive',
            style: FontStyle.Italic
          }
        })
    }
  }
}
```

**参考链接**

[Button](../harmonyos-references/ts-basic-components-button.md)
