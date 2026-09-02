---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-231
title: 自定义组件如何实现类似系统组件的链式调用
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 自定义组件如何实现类似系统组件的链式调用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5057a87fed49a20800f96c3699e8a21ba806a18d241209164cdab3c7c6a0a3df
---

目前ArkTS语法不支持这种链式调用，组件本身无法像普通对象一样调用方法，只能在组件声明时通过参数传递回调方法来修改组件的参数，无法直接使用链式调用来实现。若需要在自定义组件内实现类似系统组件的链式调用，推荐使用modifier用法，示例代码如下：

```ts
@Entry
@Component
struct CustomComponentChainCall {
  @Styles
  pressedStyles() {
    .backgroundColor(Color.Blue)
  }

  build() {
    Column() {
      CustomSysComp({
        textInputModifier: new MyTextInputModifier()
          .backgroundColor(Color.Blue)
          .placeholderColor(Color.Red),
        buttonModifier: new MyButtonModifier()
          .opacity(0.5)
          .backgroundColor(Color.Orange)
      })
        .width('100%')
        .height(400)
    }
    .width('100%')
    .height('100%')
  }
}

@Component
struct CustomSysComp {
  // Set custom TextInput.
  textInputModifier: MyTextInputModifier = new MyTextInputModifier();
  // Set custom Button.
  buttonModifier: MyButtonModifier = new MyButtonModifier();

  build() {
    Column() {
      TextInput({ placeholder: 'placeholder' })
        .attributeModifier(this.textInputModifier)
      Button('button')
        .attributeModifier(this.buttonModifier)
    }
    .width('100%')
    .height('100%')
  }
}

// The provider creates custom classes to implement the system AttributeModifier interface.
export class MyTextInputModifier implements AttributeModifier<TextInputAttribute> {
  // Default Attributes
  private mWidth: Length = '100%';
  private mHeight: Length = 100;
  // custom attribute
  private mPlaceholderColor: ResourceColor = Color.Gray;

  placeholderColor(placeholderColor: ResourceColor): MyTextInputModifier {
    this.mPlaceholderColor = placeholderColor;
    return this;
  }

  private mBackgroundColor: ResourceColor = Color.Orange;

  backgroundColor(backgroundColor: ResourceColor): MyTextInputModifier {
    this.mBackgroundColor = backgroundColor;
    return this;
  }

  applyNormalAttribute(instance: TextInputAttribute): void {
    instance.width(this.mWidth);
    instance.height(this.mHeight);
    instance.placeholderColor(this.mPlaceholderColor);
    instance.backgroundColor(this.mBackgroundColor);
  }
}

// The provider creates custom classes to implement the system AttributeModifier interface.
export class MyButtonModifier implements AttributeModifier<ButtonAttribute> {
  // Default Attributes
  private mWidth: Length = '50%';
  private mHeight: Length = 100;
  // custom attribute
  private mOpacity: number = 0;

  opacity(opacity: number): MyButtonModifier {
    this.mOpacity = opacity;
    return this;
  }

  private mBackgroundColor: ResourceColor = Color.Orange;

  backgroundColor(backgroundColor: ResourceColor): MyButtonModifier {
    this.mBackgroundColor = backgroundColor;
    return this;
  }

  applyNormalAttribute(instance: ButtonAttribute): void {
    instance.width(this.mWidth);
    instance.height(this.mHeight);
    instance.opacity(this.mOpacity);
    instance.backgroundColor(this.mBackgroundColor);
  }
}
```
