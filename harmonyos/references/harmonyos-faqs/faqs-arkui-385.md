---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-385
title: 如何实现字体渐变效果
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现字体渐变效果
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:59+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:22c37225797b775f140c98ea37a2d8ee92982259c8e4d3cb47c44ccebcff2d3e
---

**问题现象**

当通过linearGradient设置渐变时，默认是背景色的渐变，而非文字渐变的效果。应该如何实现文字渐变？

**可能原因**

由于linearGradient颜色渐变属于组件内容且绘制在背景上方，若仅对文本应用渐变，效果将作用于背景而非文字本身，其效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/YhxsmSHbQxOafhO0B4HFlQ/zh-cn_image_0000002654835245.png)

**解决措施**

要实现作用在字体上，目前以下实现方式：

1、API20之前

* ArkTS侧可以结合blendMode将背景色裁掉。通过**混合模式（BlendMode）**可以指定当前像素如何与其下方的像素混合，可以用来实现裁切、蒙版、提亮等效果。关于BlendMode的具体使用可以参考：[BlendMode](../harmonyos-references/arkts-apis-graphics-drawing-e.md#blendmode)。

  实现文字渐变的示例如下：

  ```typescript
  @Entry
  @Component
  struct Index {
    @State message: string = 'Hello World';

    build() {
      RelativeContainer() {
        Row() {
          Text(this.message)
            .fontSize(24)
            .fontWeight(FontWeight.Bold)
            .blendMode(BlendMode.DST_IN, BlendApplyType.OFFSCREEN)
        }
        .linearGradient({
          direction: GradientDirection.Right,
          colors: [['#ff0631f5', 0.0], ['#ff922626', 1]]
        })
        .blendMode(BlendMode.SRC_OVER, BlendApplyType.OFFSCREEN)
      }
      .width('100%')
      .height('100%')
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/aKiHPO9zRYSG3L91lAWaOg/zh-cn_image_0000002654795307.png)
* C-API侧，使用方案同上，使用[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)的NODE\_BLEND\_MODE，以及NODE\_LINEAR\_GRADIENT进行设置；

2、API20及以上

* 采用ArkTS实现文字渐变，可以使用Text的[shaderStyle](../harmonyos-references/ts-basic-components-text.md#shaderstyle20)属性，直接设置字体的渐变，示例如下：

  ```typescript
  @Entry
  @Component
  struct Index {
    @State message: string = 'Hello World';

    build() {
      RelativeContainer() {
        Text(this.message)
          .fontSize(24)
          .fontWeight(FontWeight.Bold)
          .shaderStyle({
            direction: GradientDirection.Right,
            colors: [['#ff0631f5', 0.0], ['#ff922626', 1]]
          })
      }
      .width('100%')
      .height('100%')
    }
  }
  ```
* 对于使用C-API开发的应用，可以使用[ArkUI\_NodeAttributeType](../harmonyos-references/capi-native-node-h.md#arkui_nodeattributetype)的 NODE\_TEXT\_LINEAR\_GRADIENT属性，实现文字渐变。

更多文字效果请参考：[基于Text组件及通用属性实现文字特效](https://gitcode.com/harmonyos_samples/text-effects)。
