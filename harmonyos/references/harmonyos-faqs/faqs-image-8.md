---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-8
title: 如何设置图片显示的分辨率
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何设置图片显示的分辨率
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:42+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0a2e7b7b166594c08b56e8dc2859e8d9d03dbcf433e36c7fc88ac8983259c04e
---

可以通过[sourceSize](../harmonyos-references/ts-basic-components-image.md#sourcesize)属性设置图片分辨率。实例代码如下，原图尺寸为1280×960，示例将图片解码为40×40。

```ts
@Entry
@Component
struct Index {
  build() {
    Column() {
      Row({ space: 50 }) {
        Image($r('app.media.example'))
          .sourceSize({
            width: 40,
            height: 40
          })
          .objectFit(ImageFit.ScaleDown)
          .aspectRatio(1)
          .width('25%')
          .border({ width: 1 })
          .overlay('width:40 height:40', { align: Alignment.Bottom, offset: { x: 0, y: 40 } })
      }
    }
  }
}
```
