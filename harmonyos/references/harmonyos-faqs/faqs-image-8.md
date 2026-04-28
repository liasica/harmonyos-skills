---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-image-8
title: 如何设置图片显示的分辨率
breadcrumb: FAQ > 媒体开发 > 拍照和图片 > 图片处理（Image） > 如何设置图片显示的分辨率
category: harmonyos-faqs
scraped_at: 2026-04-28T08:28:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:9a256e565d427d3dce05e0651ff418b2b4bbd0b2bcbc2c4cffb96b5e06f8d169
---

可以通过[sourceSize](../harmonyos-references/ts-basic-components-image.md#sourcesize)属性设置图片分辨率。实例代码如下，原图尺寸为1280×960，示例将图片解码为40×40。

```
1. @Entry
2. @Component
3. struct Index {
4. build() {
5. Column() {
6. Row({ space: 50 }) {
7. Image($r('app.media.example'))
8. .sourceSize({
9. width: 40,
10. height: 40
11. })
12. .objectFit(ImageFit.ScaleDown)
13. .aspectRatio(1)
14. .width('25%')
15. .border({ width: 1 })
16. .overlay('width:40 height:40', { align: Alignment.Bottom, offset: { x: 0, y: 40 } })
17. }
18. }
19. }
20. }
```

[DisplayAspectRatio.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ImageKit/entry/src/main/ets/pages/DisplayAspectRatio.ets#L21-L40)
