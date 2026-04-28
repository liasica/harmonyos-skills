---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-294
title: 如何实现带图片的二维码效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现带图片的二维码效果
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:15+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:5f3cac5143974aa05332739a463e33941dd8b09aca65037bcd6c2c566414e257
---

可以通过Stack布局，将Image组件放置在QRCode组件之上。开发者应调整Image尺寸，避免图片过大影响二维码识别。示例代码如下：

```
1. @Entry
2. @Component
3. struct QRCodeWithImage {
4. private value: string = 'hello world';

7. build() {
8. Stack() {
9. QRCode(this.value)
10. .width(200)
11. .height(200)
12. Image($r('app.media.app_icon'))
13. .height(50)
14. .width(50)
15. }
16. .height('100%')
17. .width('100%')
18. }
19. }
```

[ImplementQRCodeEffectWithImages.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementQRCodeEffectWithImages.ets#L21-L39)
