---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-272
title: 如何实现跨文件组件复用
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现跨文件组件复用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:11+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1122b1b5aaa7d58f80579b1c716423792bd21e6b77918d4970ea955a73e748fd
---

在应用开发中，需要使用相同功能和样式的ArkUI组件，例如购物页面中会使用相同样式的Button按钮和Text组件。常用的方法是抽取公共样式或封装成自定义组件，放入公共组件库中，以减少冗余代码。

在需要多个组件结合的场景中，例如Image和Text组成的复合自定义组件，推荐使用跨文件组件复用方案实现多组件组合。

具体实现可参考如下步骤：

1.提供方在公共组件库CommonText中创建自定义组件ImageText，支持外部传入attributeModifier属性。

```
1. // Set Image width & height
2. export class ImageModifier implements AttributeModifier<ImageAttribute> {
3. width: number = 60;
4. height: number = 60;

6. constructor(width: number, height: number) {
7. this.width = width;
8. this.height = height
9. }

11. applyNormalAttribute(instance: ImageAttribute): void {
12. instance.width(this.width);
13. instance.height(this.height);
14. }
15. }

17. /*
18. Custom class implementation of the AttributeModifier interface for text, used for initialization
19. */
20. // Set Text textSize
21. export class TextModifier implements AttributeModifier<TextAttribute> {
22. textSize: number = 12;

24. constructor(textSize: number) {
25. this.textSize = textSize;
26. }

28. applyNormalAttribute(instance: TextAttribute): void {
29. instance.fontSize(this.textSize);
30. instance.fontColor(Color.Orange);
31. instance.textAlign(TextAlign.Center);
32. instance.border({ width: 1, color: Color.Orange, style: BorderStyle.Solid });
33. instance.margin({ right: 10 });
34. }
35. }

37. /*
38. Customize class to implement the AttributeModifier interface for the checkbox, used for initialization
39. */
40. export class CheckboxModifier implements AttributeModifier<CheckboxAttribute> {
41. size: number = 15;

43. constructor(size: number) {
44. if (size < 0) {
45. size = 15;
46. }
47. this.size = size;
48. }

50. applyNormalAttribute(instance: CheckboxAttribute): void {
51. instance.width(this.size);
52. instance.height(this.size);
53. }
54. }

56. /**
57. * Customize encapsulated graphic and text components
58. */
59. @Component
60. export struct ImageText {
61. @State textContent: string | Resource = 'default';
62. @State imageSrc: PixelMap | ResourceStr | DrawableDescriptor = $r('app.media.icon');
63. //Accept externally passed AttributeModifier class instances, which can customize only some components and selectively pass parameters.
64. @State textModifier: AttributeModifier<TextAttribute> = new TextModifier(12);
65. @State imageModifier: AttributeModifier<ImageAttribute> = new ImageModifier(60, 60);
66. @State checkboxModifier: AttributeModifier<CheckboxAttribute> = new CheckboxModifier(15);

68. build() {
69. Row() {
70. Checkbox()
71. .attributeModifier(this.checkboxModifier)

73. Image(this.imageSrc)
74. .attributeModifier(this.imageModifier)
75. .margin({ right: 10 })

77. Text(this.textContent)
78. .attributeModifier(this.textModifier)
79. .fontColor(Color.Orange)
80. }
81. .padding({ top: 5 })
82. .margin({ right: 10, bottom: 15 })
83. .width(200)
84. .height(100)
85. }
86. }
```

[CommonText.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/CommonText.ets#L21-L107)

2. 实现 Image 组件、Text 组件和 Checkbox 的 AttributeModifier 接口实现类，然后使用自定义组件 ImageText 和所需参数，即可实现跨文件组件复用。

```
1. import { ImageText, ImageModifier, TextModifier, CheckboxModifier } from './CommonText';

3. @Entry
4. @Component
5. struct Details {
6. // User creates an AttributeModifier implementation class instance for the provider
7. @State textOne: TextModifier = new TextModifier(36);
8. @State imageModifier: ImageModifier = new ImageModifier(100, 100);
9. @State checkboxModifier: CheckboxModifier = new CheckboxModifier(20);

11. build(){
12. Row(){
13. ImageText({
14. textOne: this.textOne,
15. imageModifier: this.imageModifier,
16. imageSrc: $r('app.media.icon'),
17. checkboxModifier: this.checkboxModifier,
18. textOneContent: 'hello'
19. })
20. }
21. .width('100%')
22. .height('100%')
23. .alignItems(VerticalAlign.Center)
24. .justifyContent(FlexAlign.Center)
25. }
26. }
```

[ImplementCrossFilComponentReuse.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementCrossFilComponentReuse.ets#L21-L46)

**参考链接**

[attributeModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#attributemodifier)
