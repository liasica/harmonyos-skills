---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1437
title: Text嵌套Span组件maxFontSize失效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Text嵌套Span组件maxFontSize失效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:ce7e6ae3bde039c64f08fb69af1fc65a0f1cff40298555ab3a1e360acd8a6df5
---

## 问题现象

Span导致maxFontSize/minFontSize失效了，如何处理？

代码如下：

```ts
Text() {
  Span("机构最近7天调研")
  Span(this.value.count ?? '--')
    .fontColor($r('app.color.standard_eb3c3c'))
  Span("次")
}
.fontSize(12)
.fontColor($r('app.color.standard_999999'))
.maxLines(1)
.margin({ top: 5 })
.maxFontSize(30)
.minFontSize(20)
.width('100%')
.textAlign(TextAlign.Start)
```

## 背景知识

[Span](../harmonyos-references/ts-basic-components-span.md)是[Text](../harmonyos-references/ts-basic-components-text.md)、[ContainerSpan](../harmonyos-references/ts-basic-components-containerspan.md)组件的子组件，用于显示行内文本的组件。支持继承父组件Text的部分属性，仅包括：fontColor、fontSize、fontStyle、fontWeight、decoration、letterSpacing、textCase、fontFamily、textShadow。

## 解决方案

由于Span不能继承Text的maxFontSize和minFontSize属性，需要定义一个方法来判断Span的fontSize，实现最大最小fontSize设置。

代码如下：

```ts
@Entry
@Component
struct TextMaxFontSizeFile {
  @State sizeNum: number = 0;

  test(num: number) {
    if (num > 30) {
      this.sizeNum = 30;
    } else if (num < 20) {
      this.sizeNum = 20;
    } else {
      this.sizeNum = num;
    }
    return this.sizeNum;
  }

  build() {
    Column({ space: 10 }) {
      Text() {
        Span('机构最近7天调研');
        Span('--').fontColor('#f3a2c8');
        Span('次');
      }
      .fontSize(this.test(this.sizeNum))
      .fontColor('#c3c3c3')
      .maxLines(1)
      .margin({ top: 5, bottom: 20 })
      .width('100%')
      .textAlign(TextAlign.Center);

      Button('修改sizeNum>30')
        .onClick(() => {
          this.sizeNum = 100;
        });

      Button('修改sizeNum<15')
        .onClick(() => {
          this.sizeNum = 10;
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

代码运行展示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/7KgTIWaZQLOvOuTlFRYyzg/zh-cn_image_0000002633800272.png "点击放大")

## 常见FAQ

Q：ContainerSpan作为Text组件的子组件，可以使用类似Flex布局排列样式吗？

A：ContainerSpan的子组件仅包含Span和ImageSpan组件。其属性仅支持textBackgroundStyle，attributeModifier，无法做到类似Flex布局排列样式。
