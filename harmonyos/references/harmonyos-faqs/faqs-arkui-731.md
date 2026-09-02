---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-731
title: 如何实现TextArea、TextInput获取光标时不拉起键盘
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现TextArea、TextInput获取光标时不拉起键盘
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:861c1fe8369df330ee69aeb881c3f11ea3191e258fff0122867259f3416dfb6b
---

## 问题现象

TextArea获取光标时会拉起键盘，挡住应用操作界面，如何实现TextArea获取光标时不拉起键盘？

## 背景知识

* [TextArea](../harmonyos-references/ts-basic-components-textarea.md)是多行文本输入框组件。其高度未设置时默认自适应内容高度；宽度未设置时默认撑满最大宽度。
* [customKeyboard](../harmonyos-references/ts-basic-components-textarea.md#customkeyboard10)可用于设置自定义键盘。

## 解决方案

1. 创建自定义键盘，并设置其宽高都为0。
2. 通过customKeyboard属性绑定该自定义键盘。

完整示例参考如下：

```ts
@Entry
@Component
struct TextAreaExample {
  controller: TextAreaController = new TextAreaController();
  @State inputValue: string = '';

  // 自定义键盘组件
  @Builder
  CustomKeyboardBuilder() {
    Column() {
      Grid() {
        ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
          GridItem() {
            Button(item + '').width(110).onClick(() => {
              this.inputValue += item;
            });
          };
        });
      }
      .height(0)
      .width(0);
    }.backgroundColor(Color.Gray);
  }

  build() {
    Column() {
      TextArea({ controller: this.controller, text: this.inputValue })
        .customKeyboard(this.CustomKeyboardBuilder())
        .margin(10)
        .border({ width: 1 })
        .height(200);
    };
  }
}
```
