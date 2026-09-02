---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1633
title: Rating组件自定义图片资源
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Rating组件自定义图片资源
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3b02df9e121ea36328c318b1d74c99c91f7b2273c55940b4e60f7f649ba3605f
---

## 问题现象

使用Rating组件实现自定义评分样式时，获取不到自定义图片资源文件。

## 背景知识

* [Rating](../harmonyos-references/ts-basic-components-rating.md)是选择评分组件，组件中的[starStyle](../harmonyos-references/ts-basic-components-rating.md#starstyle)属性可以设置评分的样式。通过[StarStyleOptions](../harmonyos-references/ts-basic-components-rating.md#starstyleoptions18对象说明)对象设置对应的评分图片，可以实现自定义评分样式。
* 评分的样式支持加载本地图片和网络图片，暂不支持[PixelMap](../harmonyos-references/ts-image-common.md#pixelmap)类型。从API version 20开始，StarStyleOptions中的属性支持设置[Resource](../harmonyos-references/ts-types.md#resource)资源。

## 解决方案

有如下方式可以实现自定义Rating组件评分的图片资源：

* 方案一：通过Resource资源设置评分的样式（需要API20及以上），可以参考[通过Resource资源设置评分的样式](../harmonyos-references/ts-basic-components-rating.md#示例3通过resource资源设置评分的样式)。
* 方案二：通过string格式设置评分的样式，可用于加载网络图片和本地图片，加载网络图片需要配置网络权限。加载本地图片需要在src/main/ets目录下面新建一个文件夹（和pages目录同级），将图片放在文件夹中，并在当前模块下build-profile.json5文件中设置copyCodeResource参数中enable为true。

示例代码如下：

```ts
// 方案二：通过string的方式访问项目资源
@Entry
@Component
struct RatingExample1 {
  @State rating: number = 3.5;

  build() {
    Column() {
      Rating({ rating: this.rating, indicator: false })
        .stars(5)
        .stepSize(0.5)
        .starStyle({
          // common目录与pages同级，文件名根据实际情况
          backgroundUri: 'common/star1.png',
          foregroundUri: 'common/star2.png',
          secondaryUri: 'common/star3.png'
        })
        .margin({ top: 24 })
        .onChange((value: number) => {
          this.rating = value;
        });
      Text(`current score is ${this.rating}`)
        .fontSize(16)
        .fontColor('#99182431')
        .margin({ top: 16 });
    }.width('100%').height('100%');
  }
}
```

build-profile.json5文件中copyCodeResource的字段配置如下：

```json
"copyCodeResource": {
  "enable": true
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/M_FSi7-YSqSeBLpwZQbjUA/zh-cn_image_0000002628617650.png "点击放大")

## 常见FAQ

Q：在entry模块跳转到HSP模块时，HSP模块中Rating组件通过starStyle属性设置的评分样式显示空白，如何解决？

A：在API version 20版本之前，Rating组件的starStyle属性存在一些规格限制：不支持使用PixelMap类型或Resource资源。在HSP模块中，这种引用方式实际上指向的是HSP调用方**entry模块下的图片资源目录**，需要将图片资源存放在entry模块中。

Q：如何设置Rating组件星星之间的间距？

A：可以参考以下两种方法：

方法一：通过contentModifier定制Rating内容区（参考[自定义评分条](../harmonyos-references/ts-basic-components-rating.md#示例2自定义评分条)），自定义星星的间距。

方法二：直接增加图片本身的宽度，不改变星星图形的尺寸，左右两边增加透明白边，即通过增加图片本身的宽度从而实现增加星星之间的间距。
