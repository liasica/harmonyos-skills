---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-850
title: 实现Image组件的渐变模糊效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现Image组件的渐变模糊效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:55b21565b2b3047dd15200d2834bd36569b27aea4799ae3efba5da93b2155bad
---

## 问题现象

Image组件如何基于图片内容实现模糊渐变和纯颜色遮罩渐变效果。

## 背景知识

* [linearGradientBlur](../harmonyos-references/ts-universal-attributes-image-effect.md#lineargradientblur12)为组件添加内容线性渐变模糊效果。
* [linearGradient](../harmonyos-references/ts-universal-attributes-gradient-color.md#lineargradient)设置组件的颜色渐变效果，支持方向控制和多颜色配置。
* [Stack](../harmonyos-references/ts-container-stack.md)：堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

## 解决方案

方案一：可以通过linearGradientBlur设置组件的内容线性渐变模糊效果，具体可以参考官网案例[设置组件线性渐变模糊效果](../harmonyos-references/ts-universal-attributes-image-effect.md#示例2设置组件线性渐变模糊效果)。

方案二：通过视觉叠加效果，使用Stack组件将线性渐变遮罩层叠加于图片之上，实现底部透明至不透明的视觉融合效果（可叠加多个渐变层）。

示例代码如下：

```ts
@Entry
@Component
struct demo {
  build() {
    Column({ space: 5 }) {
      Column() {
        Text('原始图片')
          .fontSize(30);
        // 本地资源，需自行替换
        Image($r('app.media.startIcon'))
          .width('100%')
          .height(300)
          .objectFit(ImageFit.Auto);
      };

      Text('渐变图片')
        .fontSize(30);
      Stack() {
        // 本地资源，需自行替换
        Image($r('app.media.startIcon'))
          .width('100%')
          .height(300)
          .objectFit(ImageFit.Auto);
        Row()
          .width('100%')
          .height(300)
          .linearGradient({
            direction: GradientDirection.Bottom,
            colors: [
              [0x1000000, 0],
              [0x1000000, 0.2],
              [0x2000000, 0.3],
              [0x2000000, 0.4],
              [0x2000000, 0.5],
              [0x2000000, 0.6],
              [0x0100000, 0.9],
              [0x0000000, 1.0]
            ]
          });
      }
      .alignContent(Alignment.Bottom);
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

运行效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/Cp5-Fv4cRjqGln_xfhkxOQ/zh-cn_image_0000002628398642.png "点击放大")

## 总结

方案一可以为组件添加内容线性渐变模糊效果，实现类似毛玻璃的景深效果（如近实远虚、半透明模糊背景）；方案二为纯颜色渐变效果，实现两种或多种颜色的平滑过渡（如从白色渐变到黑色）。
