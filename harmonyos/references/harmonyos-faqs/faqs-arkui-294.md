---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-294
title: 如何实现带图片的二维码效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现带图片的二维码效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:53de67cc978248b0603ca5539fc2767ea8b0e52f4046a79ef63657596c33e3d3
---

可以通过Stack布局，将Image组件放置在QRCode组件之上。开发者应调整Image尺寸，避免图片过大影响二维码识别。示例代码如下：

```typescript
@Entry
@Component
struct QRCodeWithImage {
  private value: string = 'hello world';

  build() {
    Stack() {
      QRCode(this.value)
        .width(200)
        .height(200)
      Image($r('app.media.app_icon'))
        .height(50)
        .width(50)
    }
    .height('100%')
    .width('100%')
  }
}
```
