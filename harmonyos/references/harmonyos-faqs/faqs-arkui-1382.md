---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1382
title: 子组件的压缩优先级
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 子组件的压缩优先级
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:09+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f4812ee7fe758eeb0323f2e44ce5c34e822c5dd15b16beb26a3606323c9d4cc0
---

## 问题现象

Row内有多个Text文本，需要压缩其中一个。如下代码，Row是自适应的，里面有多个文本，第二个文本不能压缩要全部显示，在第二个文本展示不下的时候，压缩第一个文本，让其换行，如何实现？

```ts
@Entry
@Component
struct Index {
  build() {
    Column() {
      Row(){
        Image($r('app.media.startIcon'))
          .width(40).height(40)

        Text('text1')
          .maxLines(2)

        Text('text2')
      }
      .layoutWeight(1)
    }
    .height('100%')
    .width('100%');
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/2YyrrnXLSjm8tNH-eNvWbA/zh-cn_image_0000002658961871.png "点击放大")

## 背景知识

* 线性布局是开发中最常用的布局，通过线性容器[Row](../harmonyos-references/ts-container-row.md)和[Column](../harmonyos-references/ts-container-column.md)构建。线性布局是其他布局的基础，其子元素在线性方向上（水平方向和垂直方向）依次排列。线性布局的排列方向由所选容器组件决定，Row容器内子元素按照水平方向排列。
* [flexShrink](../harmonyos-references/ts-universal-attributes-flex-layout.md#flexshrink)设置父容器压缩尺寸分配给此属性所在组件的比例。当父容器为Column、Row时，需设置主轴方向的尺寸。
* [layoutWeight](../harmonyos-references/ts-universal-attributes-size.md#layoutweight)设置组件的布局权重，使组件在父容器（Row/Column/[Flex](../harmonyos-references/ts-container-flex.md)）的主轴方向按照权重分配尺寸。
* [Text](../harmonyos-references/ts-basic-components-text.md)显示一段文本的组件。

## 解决方案

实现原理说明：

1. 布局权重分配：通过.layoutWeight(1)让第一个Text组件占据Row剩余空间，当空间不足时优先触发该组件的压缩换行。
2. 压缩控制：
   * 第一个Text设置.flexShrink(1)（默认值可省略），允许内容压缩换行。
   * 第二个Text设置.flexShrink(0)，禁止压缩行为。
3. 容器约束：建议给Row设置具体宽度（如.width('100%')），确保布局系统能正确计算可用空间。

参考以下示例控制Row内子组件的压缩优先级：

```ts
@Entry
@Component
struct FlexShrink {
  build() {
    Column() {
      Row() {
        Image($r('app.media.startIcon'))
          .width(40).height(40);

        Text('text1text1text1text1text1text1text1text1text1text1text1text1text1text1text1text1text1text1text1text1text1text1text1text1text1')
          .maxLines(2)
          .flexShrink(1) // 允许压缩换行
          .layoutWeight(1); // 设置权重分配剩余空间

        Text('text2')
          .flexShrink(0); // 禁止压缩
      }
      .padding({ left: 16, right: 16 })
      .width('100%'); // 确保Row宽度受约束
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%');
  }
}
```

## 常见FAQ

Q：如何确定flexShrink的值。

A：flexShrink的计算逻辑就是将不足的空间除以带有flexShrink的组件占用的空间，然后再进行对应的缩放。压缩的权重为flexShrink\*带有flexShrink的组件所设置的长度。以计算不同Text实际宽度为例：

```ts
Flex() {
  Text('X').flexShrink(1).width(180) // 运行得到实际宽度：【150】180-30=150
  Text('Y').flexShrink(3).width(60) // 运行得到实际宽度：【30】60-30=30
  Text('Z').flexShrink(4).width(60) // 运行得到实际宽度：【20】60-40=20
}.width(200)
```

子组件原始总宽度300，压缩后实际总宽度200，需要压缩100，X压缩权重为1\*180=180，Y压缩权重为3\*60=180，Z压缩权重为4\*60=240，总压缩权重为180+180+240=600，因此X,Y,Z压缩长度分别为180/600\*100=30，180/600\*100=30，240/600\*100=40，压缩后实际宽度分别为150，30，20。
