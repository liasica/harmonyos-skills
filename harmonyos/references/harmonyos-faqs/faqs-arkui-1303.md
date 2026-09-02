---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1303
title: Text组件设置装饰线透明色不生效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Text组件设置装饰线透明色不生效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:047e49c8806a94d8f2e22ac490bef718c86e2626b6c08caba13a6e523c218ca8
---

## 问题现象

将Text组件的装饰线颜色设置为透明色Color.Transparent，用于控制装饰线的显示或隐藏，但实际显示与文本颜色相同，未达到预期效果。

问题代码如下：

```ts
@Entry
@Component
struct TextExample {
  @State selected: boolean = false

  build() {
    Column() {
      Row() {
        Text('中文')
          .fontSize('36fp')
          .decoration({
            type: TextDecorationType.LineThrough,
            color: this.selected ? Color.Red : Color.Transparent,
          })
          .onClick(() => {
            this.selected = !this.selected
          })
          .textAlign(TextAlign.Center)
          .layoutWeight(1)
      }
      .width('100%')
      .height(100)
      .justifyContent(FlexAlign.Center)
    }
    .width('100%')
    .padding({ top: 100 })
    .justifyContent(FlexAlign.Center)
  }
}
```

问题效果图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/j_RAx4ShSeSVPmR5VfmLdQ/zh-cn_image_0000002658958229.gif "点击放大")

## 背景知识

[Text组件](../harmonyos-references/ts-basic-components-text.md)用于显示一段文本，可以通过[decoration](../harmonyos-references/ts-basic-components-text.md#decoration)属性设置和调整文本装饰线的颜色和样式，其中样式包括单实线、双实线、点线、虚线和波浪线等5种。

## 解决方案

decoration属性中color的默认值为Color.Transparent，此时装饰线颜色跟随文本颜色。若期望设置装饰线为透明，需要设置装饰线颜色值为字符串格式，即透明色16进制对应值“#00FFFFFF”。

```ts
@Entry
@Component
struct TextDecorationExample {
  @State selected: boolean = false;

  build() {
    Column() {
      Text(' 点击显示或取消删除线 ')
        .width('100%')
        .fontSize('30fp')
        .textAlign(TextAlign.Center)
        .decoration({
          type: TextDecorationType.LineThrough,
          // 状态为false时，设置装饰线颜色为透明
          color: this.selected ? Color.Black : '#00FFFFFF',
        })
        .onClick(() => {
          this.selected = !this.selected;
        })
        .textAlign(TextAlign.Center)
        .layoutWeight(1);
    }
    .height('60%')
    .width('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
