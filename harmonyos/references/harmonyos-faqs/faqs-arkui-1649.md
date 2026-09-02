---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1649
title: TextInput输入框绑定自定义键盘不生效的解决方案
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > TextInput输入框绑定自定义键盘不生效的解决方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:0bb3a3751b49339c5ef059daf8a79d4501571f023beaca80d39eb70185bbb317
---

## 问题现象

使用customKeyboard属性绑定不同的自定义键盘到输入框时不生效，问题代码如下：

```ts
@Entry
@Component
struct TextInputClearFocusExample {
  @State index: number = 0;

  @Builder
  keyboard() {
    Column() {
      Text('键盘0');
    }
    .width('100%')
    .height('40%')
    .backgroundColor(Color.Pink)
    .justifyContent(FlexAlign.Center);
  }

  @Builder
  keyboard1() {
    Column() {
      Text('键盘1');
    }
    .width('100%')
    .height('40%')
    .backgroundColor(Color.Pink)
    .justifyContent(FlexAlign.Center);
  }

  @Builder
  keyboard2() {
    Column() {
      Text('键盘2');
    }
    .width('100%')
    .height('40%')
    .backgroundColor(Color.Pink)
    .justifyContent(FlexAlign.Center);
  }

  build() {
    Column({ space: 10 }) {
      TextInput({ placeholder: 'input your word...' }) // 绑定自定义键盘
        .customKeyboard(this.index === 0 ? this.keyboard() : (this.index === 1 ? this.keyboard1() : this.keyboard2()))
        .margin(10)
        .border({ width: 1 })
        .height('48vp');

      Button('切换键盘0')
        .onClick(() => {
          this.index = 0;
        });
      Button('切换键盘1')
        .onClick(() => {
          this.index = 1;
        });
      Button('切换键盘2')
        .onClick(() => {
          this.index = 2;
        });
    };
  }
}
```

问题现象见下图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/jTEfkAHzTQ270WGMnV7bGg/zh-cn_image_0000002664281407.png "点击放大")

## 背景知识

[TextInput](../harmonyos-references/ts-basic-components-textinput.md)是单行文本输入框组件，常用于响应用户的输入操作，比如手机号输入，表单的输入等。组件的[customKeyboard](../harmonyos-references/ts-basic-components-textinput.md#customkeyboard10)属性可以设置自定义键盘。

## 解决方案

[customKeyboard](../harmonyos-references/ts-basic-components-textinput.md#customkeyboard10)属性不支持使用响应式，将三元表达式替换为正常的if-else语句可以正常绑定不同的自定义键盘。示例代码如下：

```ts
@Entry
@Component
struct TextInputClearFocusExample {
  @State index: number = 0;

  @Builder
  keyboard() {
    Column() {
      Text('样式 0');
    }
    .width('100%')
    .height('40%')
    .backgroundColor('#F1F3F5')
    .justifyContent(FlexAlign.Center);
  }

  @Builder
  keyboard1() {
    Column() {
      Text('样式 1');
    }
    .width('100%')
    .height('40%')
    .backgroundColor('#F1F3F5')
    .justifyContent(FlexAlign.Center);
  }

  @Builder
  keyboard2() {
    Column() {
      Text('样式 2');
    }
    .width('100%')
    .height('40%')
    .backgroundColor('#F1F3F5')
    .justifyContent(FlexAlign.Center);
  }

  build() {
    Column() {
      if (this.index === 0) {
        TextInput({ placeholder: 'input your word...' }) // 绑定自定义键盘
          .customKeyboard(this.keyboard())
          .margin(10)
          .height('48vp');
      } else if (this.index === 1) {
        TextInput({ placeholder: 'input your word...' }) // 绑定自定义键盘
          .customKeyboard(this.keyboard1())
          .margin(10)
          .height('48vp');
      } else {
        TextInput({ placeholder: 'input your word...' }) // 绑定自定义键盘
          .customKeyboard(this.keyboard2())
          .margin(10)
          .height('48vp');
      }

      Button('切换键盘 样式0')
        .onClick(() => {
          this.index = 0;
        })
        .margin({ top: 10, bottom: 10 });
      Button('切换键盘 样式1')
        .onClick(() => {
          this.index = 1;
        })
        .margin({ top: 10, bottom: 10 });
      Button('切换键盘 样式2')
        .onClick(() => {
          this.index = 2;
        })
        .margin({ top: 10, bottom: 10 });
    };
  }
}
```

## 常见FAQ

Q：在[TextInput](../harmonyos-references/ts-basic-components-textinput.md)中使用[.customKeyboard()](../harmonyos-references/ts-basic-components-textinput.md#customkeyboard10)方法自定义了键盘，请问如何触发TextInput的onSubmit事件？

A：目前自定义键盘无法触发onSubmit事件。
