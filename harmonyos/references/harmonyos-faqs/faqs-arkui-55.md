---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-55
title: 图片如何添加渐变模糊
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 图片如何添加渐变模糊
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4d16671cfcfdff0d1cda055bc7b52bf756db6fadb6ee8d80c536d8672b926372
---

组件通用样式属性linearGradientBlur可以为当前组件添加线性渐变模糊效果。以下为参考代码：

```
1. @Entry
2. @Component
3. struct ImageExample1 {
4. privateResource1: Resource = $r('app.media.icon');
5. @State imageSrc: Resource = this.privateResource1;

7. build() {
8. Column() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
10. Row({ space: 5 }) {
11. Image(this.imageSrc)
12. .linearGradientBlur(60, {
13. fractionStops: [[0, 0], [0, 0.33], [1, 0.66], [1, 1]],
14. direction: GradientDirection.Bottom
15. })
16. }
17. }
18. }
19. }
20. }
```

[ImageAddGradientBlur.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImageAddGradientBlur.ets#L21-L40)

**参考链接**

[linearGradientBlur](../harmonyos-references/ts-universal-attributes-image-effect.md#lineargradientblur12)
