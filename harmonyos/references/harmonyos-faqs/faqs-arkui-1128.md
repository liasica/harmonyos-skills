---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1128
title: Text组件如何实现文字垂直方向显示效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Text组件如何实现文字垂直方向显示效果
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:17+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:124348ecaf1266f18a74f3797e88918248d8b006cbd01dfae9cbe5619e16cb8e
---

## 问题现象

页面文字需要垂直方向显示，使用Text组件怎样实现这种效果？

## 背景知识

* [Text](../harmonyos-references/ts-basic-components-text.md)：显示一段文本的组件。
* [@BuilderParam装饰器](../harmonyos-guides/arkts-builderparam.md)：引用@Builder函数。

## 解决方案

针对Text组件如何实现文字垂直方向显示，有以下解决方案：

* 方案一：可通过封装样式方法实现，使用ForEach()方法对Text组件文本内容进行遍历，再使用.split('')属性对文本内容进行分割然后各行显示。详情请参考如下示例代码：

  ```ts
  class Tmp {
    label: string = '';
  }

  // 封装一个方法
  @Builder
  function overBuilder(params: Tmp) {
    // 用ForEach()方法对Text组件文本内容进行遍历，再使用.split('')属性对文本内容进行分割
    ForEach(params.label.split(''), (item: string) => {
      Text(item)
        .fontSize(30);
    });
  }

  @Entry
  @Component
  struct VerticalDemo {
    @BuilderParam customOverBuilderParam: (params: Tmp) => void = overBuilder;

    build() {
      Column() {
        this.customOverBuilderParam({ label: '设置页面文字垂直方向显示' });
      }
      .height('100%')
      .width('100%')
      .alignItems(HorizontalAlign.Center);
    }
  }
  ```
* 方案二：通过设置Text组件宽度width与字号一致的方式实现，可参考[如何实现文本竖向排列](faqs-arkui-91.md)。效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/NYgFQO5sRt2KFERssN7Usg/zh-cn_image_0000002628569422.png "点击放大")
