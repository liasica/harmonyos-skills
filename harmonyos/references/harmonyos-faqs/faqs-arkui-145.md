---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-145
title: 控制中心的下拉背景实时模糊是如何实现的
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 控制中心的下拉背景实时模糊是如何实现的
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:30635f4e71c39d55728aa0eaeff99c25c7adbbcc27217e0506c3e1f71a35341f
---

实时模糊，就是通过状态变量实时改变模糊值。实现模糊可以通过组件的通用属性[backdropBlur](../harmonyos-references/ts-universal-attributes-background.md#backdropblur)来设置组件的模糊效果。参考代码如下：

```ts
// xxx.ets
@Entry
@Component
struct BackGroundBlur {
  private imageSize: number = 150;

  build() {
    Column() {
      // backdropBlur Only blur radius and grayscale parameters can be set
      Stack() {
        Image($r('app.media.startIcon'))
          .width(this.imageSize)
          .height(this.imageSize)
        Column()
          .width(this.imageSize)
          .height(this.imageSize)
          .backdropBlur(20, { grayscale: [30, 50] })
      }
    }
    .width('100%')
    .padding({ top: 5 })
  }
}
```

**参考链接**

[图像效果](../harmonyos-references/ts-universal-attributes-image-effect.md)
