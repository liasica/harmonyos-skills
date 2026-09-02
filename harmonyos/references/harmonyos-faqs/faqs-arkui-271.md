---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-271
title: 如何实现跨文件样式复用
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现跨文件样式复用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9f7b8a4e7660127b312eefca225c68e5f80773e623e6e321469f4c25756d86d8
---

在应用开发中，需要使用相同功能和样式的ArkUI组件，例如购物页面中会使用相同样式的Button、Text等组件。常用的方法是抽取公共样式或封装成一个自定义组件，添加到公共组件库中，以减少冗余代码。

需要提供单一组件的样式定制效果时，推荐使用跨文件样式复用方案。具体步骤如下：

1. 提供方应创建AttributeModifier接口的实现类。

```ts
/*
  Customize class to implement AttributeModifier interface for Text
*/
export class CommodityText implements AttributeModifier<TextAttribute> {
  textType: TextType = TextType.TYPE_ONE;
  textSize: number = 15;

  constructor( textType: TextType, textSize: number) {
    this.textType = textType;
    this.textSize = textSize;
  }

  applyNormalAttribute(instance: TextAttribute): void {
    if (typeof this.textSize !== 'number' || this.textSize <= 0) {
      throw new Error('Invalid textSize')
    }

    if (this.textType === TextType.TYPE_ONE) {
      instance.fontSize(this.textSize);
      instance.fontColor(Color.Orange);
      instance.fontWeight(FontWeight.Bolder);
      instance.width(200);
    } else if (this.textType === TextType.TYPE_TWO) {
      instance.fontSize(this.textSize);
      instance.fontWeight(FontWeight.Bold);
      instance.fontColor(Color.Blue);
      instance.width(200);
    } else if (this.textType === TextType.TYPE_THREE) {
      instance.fontColor(Color.Gray);
      instance.fontSize(this.textSize);
      instance.fontWeight(FontWeight.Normal);
      instance.width(200);
    } else if (this.textType === TextType.TYPE_FOUR) {
      instance.fontSize(this.textSize);
      instance.fontColor(Color.Orange);
      instance.textAlign(TextAlign.Center);
      instance.border({ width: 1, color: Color.Orange, style: BorderStyle.Solid });
      instance.margin({ right: 10 });
    } else {
     console.log(`TYPE is ${this.textType}`);
    }
  }
}
/*
 *  Enumerate text types
 */
export enum TextType {
  TYPE_ONE,
  TYPE_TWO,
  TYPE_THREE,
  TYPE_FOUR
}
```

2.使用方创建提供方的AttributeModifier实现类实例，并将其作为attributeModifier属性方法的参数传入系统组件。

```ts
import { CommodityText, TextType } from './attributeModifier';

@Entry
@Component
export struct Details {
  // User creates an AttributeModifier implementation class instance for the provider
  @State textOne: CommodityText = new CommodityText(TextType.TYPE_FOUR, 15);

  build(){
    Row(){
      Text($r('app.string.app_name'))
        .attributeModifier(this.textOne)
        .textAlign(TextAlign.Center)
    }
    .width('100%')
    .height('100%')
    .alignItems(VerticalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}
```

**参考链接**

[attributeModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#attributemodifier)
