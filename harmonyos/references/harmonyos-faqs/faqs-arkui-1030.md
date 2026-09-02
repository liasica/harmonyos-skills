---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1030
title: 实现Text设置lineHeight属性后文本垂直居中显示
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现Text设置lineHeight属性后文本垂直居中显示
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e99ac01d24e4e767b342932d02c00eaa3deddb4bd772fb9dc488cf5546aab35a
---

## 问题现象

Text设置lineHeight属性后，导致文本无法垂直居中，如何实现文本垂直居中显示？

```ts
Text("测试Text设置lineHeight").lineHeight(100).backgroundColor(Color.Green)
```

问题展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/Lu5sJcpGTamRpyhczMq6Kw/zh-cn_image_0000002628564722.png "点击放大")

## 背景知识

* [lineHeight](../harmonyos-references/ts-basic-components-text.md#lineheight)：设置文本的文本行高。设置值不大于0时，不限制文本行高，自适应字体大小，number类型时单位为fp。string类型支持number类型取值的字符串形式，可以附带单位，例如"10"、"10fp"。
* [halfLeading](../harmonyos-references/ts-basic-components-text.md#halfleading12)：设置文本是否将行间距平分至行的顶部与底部。组件侧设置halfLeading优先级高于module.json5配置文件中的halfLeading配置项，仅支持API12以上版本。
* [baselineOffset](../harmonyos-references/ts-basic-components-text.md#baselineoffset)：设置文本基线的偏移量。
* [textVerticalAlign](../harmonyos-references/ts-basic-components-text.md#textverticalalign20)：设置文本段落在垂直方向的对齐方式。仅支持API20以上版本。

## 解决方案

实现文本垂直居中显示方式及其适用场景内容如下：

| 实现场景 | 实现方式 | 适用场景 |
| --- | --- | --- |
| 方案一 | 设置halfLeading属性。 | 仅支持API12+，适合单行文本。 |
| 方案二 | module.json5中配置half\_leading参数。 | 生效范围整个HAP，可能影响通过lineHeight和padding实现居中效果的组件。 |
| 方案三 | 设置baselineOffset属性。 | 需要明确组件的高度，计算基线位置。 |
| 方案四 | attributeModifier属性设置padding。 | 繁琐，适合需动态修改属性的场景。 |
| 方案五 | 设置textVerticalAlign。 | 简单方便，仅支持API20+。 |

* 方案一：通过组件侧设置halfLeading属性，将行间距平分至行的顶部与底部。仅支持API12以上版本。

  组件侧设置halfLeading优先级高于module.json5配置文件中的half\_leading配置项。

  ```ts
  @Entry
  @Component
  struct Index {
    build() {
      Column() {
        Text('lineHeight设置过高，不设置padding调整，通过设置halfLeading为true')
          .fontSize(15)
          .fontColor(Color.Black)
          .textOverflow({
            overflow: TextOverflow.Ellipsis
          })
          .lineHeight(60)
          .maxLines(1)
          .halfLeading(true)
      }
      .borderWidth(1)
      .backgroundColor('#f1f3f5')
      .borderRadius(24)
      .margin(16)
    }
  }
  ```
* 方案二：通过配置module.json5中的half\_leading参数。

  在module.json5文件中，将half\_leading配置为true，可以改变文本的默认绘制行为，从而避免因lineHeight过大而导致的文本偏移问题。

  ```json
  "metadata": [
    {
      "name": "half_leading",
      "value": "true"
    }
  ],
  ```

  对应的Text组件代码如下：

  ```ts
  @Entry
  @Component
  struct TextLineHeight {
    build() {
      Column() {
        Text('通过设置module.json5中配置half_leading为true实现垂直居中')
          .fontSize(15)
          .fontColor(Color.Black)
          .textOverflow({
            overflow: TextOverflow.Ellipsis
          })
          .maxLines(1)
          .lineHeight(60)
      }
      .borderWidth(1)
      .borderRadius(24)
      .backgroundColor('#f1f3f5')
      .margin(16)
    }
  }
  ```

  **说明** 

  设置half\_leading为true会对整个HAP生效，可能会影响其他已正常显示Text组件。如果已有Text组件通过lineHeight和padding实现了居中效果，启用half\_leading后，这些组件的显示可能会发生偏移，需谨慎使用。
* 方案三：使用baselineOffset属性可以设置Text、Span组件的对准基线，实现内部文本垂直居中对齐。

  ```ts
  @Entry
  @Component
  struct TextLineHeightTwo {
    build() {
      Column() {
        Text('通过设置baselineOffset属性来调整基线，实现垂直居中')
          .fontSize(16)
          .fontColor(Color.Black)
          .textOverflow({
            overflow: TextOverflow.Ellipsis
          })
          .maxLines(1)
          .lineHeight(60)
          .baselineOffset(22)
      }
      .borderWidth(1)
      .borderRadius(24)
      .backgroundColor('#f1f3f5')
      .margin(16)
    }
  }
  ```
* 方案四：使用Text结合动态属性attributeModifier设置内边距padding解决问题。可参考官网[设置和修改组件属性](../harmonyos-guides/arkts-user-defined-extension-attributemodifier.md#设置和修改组件属性)。
* 方案五：使用textVerticalAlign（API Version 20+）设置文本段落在垂直方向居中对齐。使用该方案同时还可以设置textOverflow文本超长时隐藏。

  ```ts
  @Entry
  @Component
  struct TextLineHeightThree {
    build() {
      Column() {
        Text('通过设置属性为TextVerticalAlign.CENTER，实现垂直居中')
          .fontSize(16)
          .fontColor(Color.Black)
          .textOverflow({
            overflow: TextOverflow.Ellipsis
          })
          .maxLines(1)
          .lineHeight(60)
          .textVerticalAlign(TextVerticalAlign.CENTER)
      }
      .borderWidth(1)
      .borderRadius(24)
      .backgroundColor('#f1f3f5')
      .margin(16)
    }
  }
  ```

## 常见FAQ

Q：当Text内包含多个Span且各Span设置了不同的字体大小时，默认渲染为基线对齐，如何实现多字号Span在Text容器内的垂直居中对齐？

A：将Row容器组件包含多个Text组件后设置对齐方式为VerticalAlign.Center。代码如下：

```ts
@Entry
@Component
struct FAQ {
  build() {
    Column() {
      Row() {
        Text() {
          Span('message').fontSize(16).fontColor(0x000000)
        }
        .maxLines(1)

        Text() {
          Span('message').fontSize(30).fontColor(0x0080FF)
        }
        .maxLines(1)

        Text() {
          Span('message').fontSize(20).fontColor(0x000000)
        }
        .maxLines(1)
      }
      .alignItems(VerticalAlign.Center)
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
  }
}
```
