---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1648
title: ForEach嵌套TextArea时如何确保软键盘输入后不收起
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > ForEach嵌套TextArea时如何确保软键盘输入后不收起
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:d8527d7105d6a67a6e4ffaf675959ca9fc542a2b9fb47cb436cc0081ebaa0ea5
---

## 问题现象

在ForEach嵌套TextArea组件的使用场景下，TextArea输入完成后软键盘会收起，导致继续输入不方便，如何确保软键盘在输入后不退出？

问题代码如下：

```ts
@Entry
@Component
struct TextAreaPage {
  @State contentArr: Array<string> = [''];

  build() {
    Row() {
      Column({ space: 24 }) {
        ForEach(this.contentArr, (item: string, index: number) => {
          TextArea({ text: item })
            .width('95%')
            .onChange((val: string) => {
              this.contentArr[index] = val;
            })
            .textAlign(TextAlign.Start)
            .height(42);
        });
      }
      .width('100%');
    }
    .height('100%');
  }
}
```

问题效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/zSSKmnRuS36rOZVXBpZZYw/zh-cn_image_0000002628820884.png "点击放大")

## 背景知识

[@State](../harmonyos-guides/arkts-state.md)装饰的变量，或称为状态变量，一旦变量拥有了状态属性，就可以触发其直接绑定UI组件的刷新。当状态改变时，UI会发生对应的渲染改变。

## 解决方案

上述问题是由于@State装饰的变量contentArr在TextArea值发生改变时同步更新，导致UI刷新，最后软键盘收起。因此将ForEach使用的变量contentArr和TextArea值分开更新即可解决问题。

示例代码如下：

```ts
@Entry
@Component
struct TextAreaPage {
  @State contentArr: Array<string> = [''];
  @State editContentArr: Array<string> = [];

  build() {
    Row() {
      Column({ space: 24 }) {
        ForEach(this.contentArr, (item: string) => {
          TextArea({ text: item })
            .width('95%')
            .onChange((val: string) => {
              this.editContentArr.push(val); // 使用editContentArr替代contentArr存入输入值
            })
            .textAlign(TextAlign.Start);
        })
      }
      .width('100%');
    }
    .margin({ left: 16, right: 16 })
    .height('100%');
  }
}
```

效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/-Nt3y-PhTUCrQCKDfxcYBQ/zh-cn_image_0000002659020189.png "点击放大")
