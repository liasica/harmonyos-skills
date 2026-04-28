---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-271
title: 如何实现跨文件样式复用
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现跨文件样式复用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:10+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:fe3986529c6c58496394e49183fd1a1bbe27e8b6a7c4bacb8886c44de65aa237
---

在应用开发中，需要使用相同功能和样式的ArkUI组件，例如购物页面中会使用相同样式的Button、Text等组件。常用的方法是抽取公共样式或封装成一个自定义组件，添加到公共组件库中，以减少冗余代码。

需要提供单一组件的样式定制效果时，推荐使用跨文件样式复用方案。具体步骤如下：

1. 提供方应创建AttributeModifier接口的实现类。

```
1. /*
2. Customize class to implement AttributeModifier interface for Text
3. */
4. export class CommodityText implements AttributeModifier<TextAttribute> {
5. textType: TextType = TextType.TYPE_ONE;
6. textSize: number = 15;

8. constructor( textType: TextType, textSize: number) {
9. this.textType = textType;
10. this.textSize = textSize;
11. }

13. applyNormalAttribute(instance: TextAttribute): void {
14. if (typeof this.textSize !== 'number' || this.textSize <= 0) {
15. throw new Error('Invalid textSize')
16. }

18. if (this.textType === TextType.TYPE_ONE) {
19. instance.fontSize(this.textSize);
20. instance.fontColor(Color.Orange);
21. instance.fontWeight(FontWeight.Bolder);
22. instance.width(200);
23. } else if (this.textType === TextType.TYPE_TWO) {
24. instance.fontSize(this.textSize);
25. instance.fontWeight(FontWeight.Bold);
26. instance.fontColor(Color.Blue);
27. instance.width(200);
28. } else if (this.textType === TextType.TYPE_THREE) {
29. instance.fontColor(Color.Gray);
30. instance.fontSize(this.textSize);
31. instance.fontWeight(FontWeight.Normal);
32. instance.width(200);
33. } else if (this.textType === TextType.TYPE_FOUR) {
34. instance.fontSize(this.textSize);
35. instance.fontColor(Color.Orange);
36. instance.textAlign(TextAlign.Center);
37. instance.border({ width: 1, color: Color.Orange, style: BorderStyle.Solid });
38. instance.margin({ right: 10 });
39. } else {
40. console.log(`TYPE is ${this.textType}`);
41. }
42. }
43. }
44. /*
45. *  Enumerate text types
46. */
47. export enum TextType {
48. TYPE_ONE,
49. TYPE_TWO,
50. TYPE_THREE,
51. TYPE_FOUR
52. }
```

[attributeModifier.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/attributeModifier.ets#L21-L72)

2.使用方创建提供方的AttributeModifier实现类实例，并将其作为attributeModifier属性方法的参数传入系统组件。

```
1. import { CommodityText, TextType } from './attributeModifier';

3. @Entry
4. @Component
5. export struct Details {
6. // User creates an AttributeModifier implementation class instance for the provider
7. @State textOne: CommodityText = new CommodityText(TextType.TYPE_FOUR, 15);

9. build(){
10. Row(){
11. Text($r('app.string.app_name'))
12. .attributeModifier(this.textOne)
13. .textAlign(TextAlign.Center)
14. }
15. .width('100%')
16. .height('100%')
17. .alignItems(VerticalAlign.Center)
18. .justifyContent(FlexAlign.Center)
19. }
20. }
```

[ImplementCrossFileStyleReuse.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImplementCrossFileStyleReuse.ets#L21-L40)

**参考链接**

[attributeModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#attributemodifier)
