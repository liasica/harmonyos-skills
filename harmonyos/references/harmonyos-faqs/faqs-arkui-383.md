---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-383
title: Surface模式下的XComponent组件在设置renderFit后如果出现显示异常，该如何调整以获得正确的显示效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Surface模式下的XComponent组件在设置renderFit后如果出现显示异常，该如何调整以获得正确的显示效果
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:39+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:4d78f575b10ea619f130e32c10fb1b32a923226a3bd7ce8a0c5691977f0dc2a2
---

**解决措施**

当Surface模式下的XComponent组件其内容与组件的尺寸不一致时，可通过设置[renderFit](../harmonyos-references/ts-universal-attributes-renderfit.md#renderfit18)属性，以调整内容在组件尺寸范围内的布局方式，例如拉伸、居中、等比缩放等。在API version 低于18时，Surface模式下的XComponent组件的[renderFit](../harmonyos-references/ts-universal-attributes-renderfit.md#renderfit18)属性仅支持设置为RenderFit.RESIZE\_FILL；如果设置为其他属性值可能在部分机型出现显示异常。如果确实需要设置RESIZE\_FILL之外的属性值，可以通过升级至API version 18或在XComponent组件id字段中包含"RenderFitSurface"关键字来修正显示效果。升级API version 18是推荐方案，适用于新开发项目；id字段修改方案适用于需要兼容旧API version的项目。

**示例代码**

```
1. @Entry
2. @Component
3. struct XComponentSurfaceRenderFit {
4. @State xcWidth: number = 500;
5. @State xcHeight: number = 700;
6. myXComponentController: XComponentController = new XComponentController();

8. build() {
9. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Start }) {
10. XComponent({
11. id: 'myXComponent_RenderFitSurface', // When the string of the id contains "RenderFitSurface", RenderFit can be displayed correctly
12. type: XComponentType.SURFACE,
13. controller: this.myXComponentController
14. })
15. .width(this.xcWidth)
16. .height(this.xcHeight)
17. .renderFit(RenderFit.CENTER)
18. }
19. .width('100%')
20. }
21. }
```

[XComponentSurfaceRenderFit.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/XComponentSurfaceRenderFit.ets#L20-L41)
