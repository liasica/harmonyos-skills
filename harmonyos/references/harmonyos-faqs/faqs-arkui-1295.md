---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1295
title: Row组件设置padding属性不生效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Row组件设置padding属性不生效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:426f5c26afd57c531c4dacd8603d0889536d30729efa37e71c80e33777f7db9c
---

## 问题现象

Row组件中存放一个Text组件和一个TextInput组件，给Row组件设置padding并未生效，该如何解决？

```ts
@Entry
@Component
struct PageOne {
  build() {
    Column() {
      Row() {
        Text('文本');
        TextInput({ placeholder: '输入' })
          .maxLines(3)
          .type(InputType.Password)
          .height(40)
          .backgroundColor('#DFE1E3');
      }
      .height(60)
      .margin({ left: 16, right: 16 })
      .padding({ left: 20, right: 20 })
      .backgroundColor('#EBEDEF');
    }
    .width('100%')
    .height('100%');
  }
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/RM7IhLiMQMefXTb8EJbYaA/zh-cn_image_0000002658837245.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/kFIzd8mfTKmjqVQIe2UOCA/zh-cn_image_0000002628597982.png "点击放大")

## 背景知识

* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)：单行文本输入框组件。
* [layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)：设置组件的布局权重，使组件在父容器（[Row](../harmonyos-references/ts-container-row.md)/[Column](../harmonyos-references/ts-container-column.md)/[Flex](../harmonyos-references/ts-container-flex.md)）的主轴方向按照权重分配尺寸。

## 解决方案

针对padding属性未生效问题，给TextInput组件设置layoutWeight(1)属性即可。

```ts
@Entry
@Component
struct PageTwo {
  build() {
    Column() {
      Row() {
        Text('文本');
        TextInput({ placeholder: '输入' })
          .maxLines(3)
          .type(InputType.Password)
          .height(40)
          .backgroundColor('#DFE1E3')
          .layoutWeight(1);
      }
      .height(60)
      .margin({ left: 16, right: 16 })
      .padding({ left: 20, right: 20 })
      .backgroundColor('#EBEDEF');
    }
    .width('100%')
    .height('100%');
  }
}
```
