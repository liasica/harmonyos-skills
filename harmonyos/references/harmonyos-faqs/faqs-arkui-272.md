---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-272
title: 如何实现跨文件组件复用
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现跨文件组件复用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9c256902c42cf0f526867c5d0d66bd99087f330ce898f8f60d88a698eef27137
---

在应用开发中，需要使用相同功能和样式的ArkUI组件，例如购物页面中会使用相同样式的Button按钮和Text组件。常用的方法是抽取公共样式或封装成自定义组件，放入公共组件库中，以减少冗余代码。

在需要多个组件结合的场景中，例如Image和Text组成的复合自定义组件，推荐使用跨文件组件复用方案实现多组件组合。

具体实现可参考如下步骤：

1.提供方在公共组件库CommonText中创建自定义组件ImageText，支持外部传入attributeModifier属性。

```ts
// Set Image width & height
export class ImageModifier implements AttributeModifier<ImageAttribute> {
  width: number = 60;
  height: number = 60;

  constructor(width: number, height: number) {
    this.width = width;
    this.height = height
  }

  applyNormalAttribute(instance: ImageAttribute): void {
    instance.width(this.width);
    instance.height(this.height);
  }
}

/*
  Custom class implementation of the AttributeModifier interface for text, used for initialization
*/
// Set Text textSize
export class TextModifier implements AttributeModifier<TextAttribute> {
  textSize: number = 12;

  constructor(textSize: number) {
    this.textSize = textSize;
  }

  applyNormalAttribute(instance: TextAttribute): void {
    instance.fontSize(this.textSize);
    instance.fontColor(Color.Orange);
    instance.textAlign(TextAlign.Center);
    instance.border({ width: 1, color: Color.Orange, style: BorderStyle.Solid });
    instance.margin({ right: 10 });
  }
}

/*
  Customize class to implement the AttributeModifier interface for the checkbox, used for initialization
*/
export class CheckboxModifier implements AttributeModifier<CheckboxAttribute> {
  size: number = 15;

  constructor(size: number) {
    if (size < 0) {
      size = 15;
    }
    this.size = size;
  }

  applyNormalAttribute(instance: CheckboxAttribute): void {
    instance.width(this.size);
    instance.height(this.size);
  }
}

/**
 * Customize encapsulated graphic and text components
 */
@Component
export struct ImageText {
  @State textContent: string | Resource = 'default';
  @State imageSrc: PixelMap | ResourceStr | DrawableDescriptor = $r('app.media.icon');
  //Accept externally passed AttributeModifier class instances, which can customize only some components and selectively pass parameters.
  @State textModifier: AttributeModifier<TextAttribute> = new TextModifier(12);
  @State imageModifier: AttributeModifier<ImageAttribute> = new ImageModifier(60, 60);
  @State checkboxModifier: AttributeModifier<CheckboxAttribute> = new CheckboxModifier(15);

  build() {
    Row() {
      Checkbox()
        .attributeModifier(this.checkboxModifier)

      Image(this.imageSrc)
        .attributeModifier(this.imageModifier)
        .margin({ right: 10 })

      Text(this.textContent)
        .attributeModifier(this.textModifier)
        .fontColor(Color.Orange)
    }
    .padding({ top: 5 })
    .margin({ right: 10, bottom: 15 })
    .width(200)
    .height(100)
  }
}
```

2. 实现 Image 组件、Text 组件和 Checkbox 的 AttributeModifier 接口实现类，然后使用自定义组件 ImageText 和所需参数，即可实现跨文件组件复用。

```ts
import { ImageText, ImageModifier, TextModifier, CheckboxModifier } from './CommonText';

@Entry
@Component
struct Details {
  // User creates an AttributeModifier implementation class instance for the provider
  @State textOne: TextModifier = new TextModifier(36);
  @State imageModifier: ImageModifier = new ImageModifier(100, 100);
  @State checkboxModifier: CheckboxModifier = new CheckboxModifier(20);

  build() {
    Row() {
      ImageText({
        textModifier: this.textOne,
        imageModifier: this.imageModifier,
        imageSrc: $r('app.media.icon'),
        checkboxModifier: this.checkboxModifier,
        textContent: 'hello'
      })
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
