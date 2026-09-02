---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-521
title: 输入组件获焦时实现提示文本的动态效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 输入组件获焦时实现提示文本的动态效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:990624eb9c2ec4c0672b21a7b242829ead958bc2294ea7c26857d0fd26709ead
---

## 问题现象

在使用TextInput和TextArea组件进行输入时，如何实现提示文字的动态效果？

## 背景知识

* 组件的某些通用属性变化时，可以通过[animation属性动画](../harmonyos-references/ts-animatorproperty.md)实现渐变过渡效果，提升用户体验。
* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)是HarmonyOS提供的一种单行文本输入框组件。
* [TextArea](../harmonyos-references/ts-basic-components-textarea.md)是多行文本输入框组件，当输入的文本内容超过组件宽度时会自动换行显示。
* [attributeModifier](../harmonyos-references/ts-universal-attributes-attribute-modifier.md#attributemodifier)接口支持动态属性设置，支持开发者在属性设置时使用if/else语法，且根据需要使用多态样式设置属性。

## 解决方案

1. 在Stack组件中创建Text提示文本和TextInput输入框。
2. 创建TextModifier类，实现attributeModifier接口，该类中的applyNormalAttribute方法可根据对应的boolean类型的值动态修改对应组件的样式属性。
3. 当点击TextInput组件时，执行onFocus方法，若文本值为空，将对应的TextModifier类的属性装载至该组件上，从而实现animation动画效果。

完整示例参考如下：

```ts
@Entry
@Component
struct TextInputTestOne {
  // 定义状态变量
  message: string = 'Hello World';
  textAreaValue: string = '';
  textInputValue: string = '';
  selectValue: string = '';
  @State modifierOne: TextModifier = new TextModifier(50, 150, 20);
  @State modifierTwo: TextModifier = new TextModifier(50, 0, 20);
  opacityOne: number = 0.3;
  opacityTwo: number = 0.3;

  build() {
    Column() {
      Column() {
        Stack() {
          Text('请在这输入文字：')
            .fontSize(this.modifierOne.fontSize)
            .textAlign(TextAlign.Start)
            .fontColor(Color.Black)
            .margin({ left: this.modifierOne.marginLeft, bottom: this.modifierOne.marginBottom })
            .attributeModifier(this.modifierOne)
            .width('100%')
            .opacity(this.opacityOne)
            // 实现动画效果
            .animation({
              duration: 300,
              curve: Curve.Friction,
              iterations: 1,
              playMode: PlayMode.Normal
            });
          TextArea({ text: $$this.textAreaValue })
          // 聚焦回调时间
            .onFocus(() => {
              if (this.textAreaValue === '') {
                this.modifierOne.isFocus = true;
                this.opacityOne = 1;
              }
            })
            // 失焦回调事件
            .onBlur(() => {
              if (this.textAreaValue === '') {
                this.modifierOne.isFocus = false;
                this.opacityOne = 0.3;
              }
            })
            .height('80%');
        };
      }
      .justifyContent(FlexAlign.Center)
      .height('30%')
      .margin({ left: 20, right: 20 });

      Column() {
        Stack() {
          Text('请在这输入文字：')
            .fontSize(this.modifierTwo.fontSize)
            .fontColor(Color.Black)
            .textAlign(TextAlign.Start)
            .width('100%')
            .margin({ left: this.modifierTwo.marginLeft, bottom: this.modifierTwo.marginBottom })
            .attributeModifier(this.modifierTwo)
            .opacity(this.opacityTwo)
            // 实现动画效果
            .animation({
              duration: 300,
              curve: Curve.Friction,
              iterations: 1,
              playMode: PlayMode.Normal
            });
          TextInput({ text: $$this.textInputValue })
          // 聚焦回调时间
            .onFocus(() => {
              if (this.textInputValue === '') {
                this.modifierTwo.isFocus = true;
                this.opacityTwo = 1;
              }
            })
            // 失焦回调事件
            .onBlur(() => {
              if (this.textInputValue === '') {
                this.modifierTwo.isFocus = false;
                this.opacityTwo = 0.3;
              }
            });
        };
      }
      .justifyContent(FlexAlign.Center)
      .height('30%')
      .margin({ left: 20, right: 20 });
    }
    .height('100%')
    .width('100%');
  }
}

class TextModifier implements AttributeModifier<TextAttribute> {
  isFocus: boolean | undefined = undefined;
  marginLeft: number = 0;
  marginBottom: number = 0;
  fontSize: number = 0;

  // 绑定属性
  applyNormalAttribute(instance: TextAttribute): void {
    if (this.isFocus) {
      this.marginLeft -= 10;
      this.marginBottom += 40;
      this.fontSize -= 7;
      instance
        .fontSize(this.fontSize)
        .margin({ left: this.marginLeft, bottom: this.marginBottom });
    } else if (this.isFocus === false) {
      this.marginLeft += 10;
      this.marginBottom -= 40;
      this.fontSize += 7;
      instance
        .fontSize(this.fontSize)
        .margin({ left: this.marginLeft, bottom: this.marginBottom });
    }
  }

  constructor(marginLeft: number, marginBottom: number, fontSize: number) {
    this.marginLeft = marginLeft;
    this.marginBottom = marginBottom;
    this.fontSize = fontSize;
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/XU17LLP4RR2dutx_FENzLw/zh-cn_image_0000002628391170.png "点击放大")
