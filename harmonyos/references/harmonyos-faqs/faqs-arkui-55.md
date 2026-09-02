---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-55
title: 图片如何添加渐变模糊
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 图片如何添加渐变模糊
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d5cced6789e68d04001a0b65e41fbfcdcda0addd6196666f063f4afb4199e1cb
---

组件通用样式属性linearGradientBlur可以为当前组件添加线性渐变模糊效果。以下为参考代码：

```typescript
@Entry
@Component
struct ImageExample1 {
  privateResource1: Resource = $r('app.media.icon');
  @State imageSrc: Resource = this.privateResource1;

  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row({ space: 5 }) {
          Image(this.imageSrc)
            .linearGradientBlur(60, {
              fractionStops: [[0, 0], [0, 0.33], [1, 0.66], [1, 1]],
              direction: GradientDirection.Bottom
            })
        }
      }
    }
  }
}
```

**参考链接**

[linearGradientBlur](../harmonyos-references/ts-universal-attributes-image-effect.md#lineargradientblur12)
