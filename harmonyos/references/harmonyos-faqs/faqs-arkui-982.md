---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-982
title: 不同类型组件复用相同动态属性
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 不同类型组件复用相同动态属性
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0e75007abc52832f0f8c1c2490e7418a0236c93ef71ef1fdaf4eea43c6671c34
---

## 问题现象

不同组件（Text、TextInput、Button等）是否可以复用相同的动态属性？

## 背景知识

[动态属性设置](../harmonyos-references/ts-universal-attributes-attribute-modifier.md)可以让开发者通过自定义class实现AttributeModifier接口，动态设置组件的属性，使组件在不同的形态展示不同的样式。

## 解决方案

AttributeModifier的泛型类和回调方法参数对象类型可以写多个，不同组件可以复用相同的动态属性，如：applyNormalAttribute(instance: TextAttribute|TextInputAttribute|ButtonAttribute)。如果有组件与其他组件有区别需单独处理，可以在自定义实现的class构造器中增加一个参数，用以作为分支逻辑的判断条件。如点击Text组件和Button组件，背景色可以在绿色与蓝色之间切换；复用相同动态属性，点击TextInput组件，背景色切换与Text组件和Button组件不同。

完整示例参考如下：

```ts
class MyModifier implements AttributeModifier<TextAttribute | TextInputAttribute | ButtonAttribute> {
  isDark: boolean = false;
  type: string = 'TextInputAttribute';

  constructor(dark?: boolean, type?: string) {
    this.isDark = dark ?? false;
    this.type = type ?? '';
  }

  applyNormalAttribute(instance: TextAttribute | TextInputAttribute | ButtonAttribute): void {
    if (this.type === 'TextInputAttribute') {
      if (this.isDark) {
        instance.backgroundColor('#fff0f1f3');
      } else {
        instance.backgroundColor('#ffcfdaef');
      }
    } else {
      if (this.isDark) {
        instance.backgroundColor(Color.Blue);
      } else {
        instance.backgroundColor(Color.Green);
      }
    }
  }
}

@Entry
@Component
struct MultiComponentAttributeDemo {
  @State modifierText: MyModifier = new MyModifier();
  @State modifierButton: MyModifier = new MyModifier();
  @State modifierTextInput: MyModifier = new MyModifier(false, 'TextInputAttribute');

  build() {
    Column() {
      Text('Text')
        .fontSize(30)
        .attributeModifier(this.modifierText)
        .onClick(() => {
          this.modifierText.isDark = !this.modifierText.isDark;
        });

      Button('Button')
        .attributeModifier(this.modifierButton)
        .onClick(() => {
          this.modifierButton.isDark = !this.modifierButton.isDark;
        });

      TextInput()
        .borderColor(Color.Black)
        .borderWidth(1)
        .attributeModifier(this.modifierTextInput)
        .onClick(() => {
          this.modifierTextInput.isDark = !this.modifierTextInput.isDark;
        })
    }
    .justifyContent(FlexAlign.SpaceEvenly)
    .width('100%')
    .height('100%')
  }
}
```

## 总结

ArkUI支持多种样式复用方式，[@Styles装饰器](../harmonyos-guides/arkts-style.md)，定义组件重用样式，仅支持通用属性和通用事件；[@Extend装饰器](../harmonyos-guides/arkts-extend.md)，定义扩展组件样式；@Styles和@Extend都是仅限在当前文件内使用，不支持导出，如果要实现export功能，推荐使用[AttributeModifier](../harmonyos-guides/arkts-user-defined-extension-attributemodifier.md)。
