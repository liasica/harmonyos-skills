---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0009
title: 组件背景拉伸常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > 组件背景拉伸常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:47:32+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:f248a4409e4215f5dc8eb3054e19734ae237f43c09dcda8ced695c769ac9115e
---

**Q：给Text组件设置一个点九图的聊天气泡背景，聊天气泡根据内容自动拉伸时，聊天气泡边上会变形、失真，如何解决？**

**A**：

方案一：通过设置Image组件的[resizable](../harmonyos-references/ts-basic-components-image.md#resizable11)属性实现图片的安全拉伸效果。

示例代码如下：

通过@Builder装饰器封装容器背景样式，根据点九图设置合适的Image组件拉伸属性resizable。

```ts
@Builder
function bubbleBackground() {
  // .9图地址
  Image($r('app.media.imageresizable_border'))
    .objectFit(ImageFit.Fill)
    .resizable({
      slice: {
        top: 3,
        bottom: 3,
        left: 5,
        right: 5
      }
    })
    .width('100%')
    .height('100%')
}
```

给容器组件Column/Row设置background属性为bubbleBackground函数，Text作为其子组件。

```ts
Column() {
        Text('200减30券')
          .fontColor('#0A59F7')
      }
      .padding(3)
      .background(bubbleBackground)
```

方案二：HarmonyOS支持[图片边框设置](../harmonyos-references/ts-universal-attributes-border-image.md)，通过给Text组件设置[borderImage](../harmonyos-references/ts-universal-attributes-border-image.md#borderimage)属性，实现图片自适应拉伸的效果，实现类似点九图的效果。

示例代码如下：

```ts
Text('满5000减4000')
        .fontColor('#0A59F7')
        .textAlign(TextAlign.Center)
        .margin({ top: 20 })
        .padding(3)
        .borderImage({
          source: $r('app.media.imageresizable_border'),
          slice: {
            top: 3,
            bottom: 3,
            left: 5,
            right: 5
          },
          width: {
            top: 3,
            bottom: 3,
            left: 5,
            right: 5
          },
          repeat: RepeatMode.Stretch,
          fill: true
        })
```

完整代码：

```ts
@Builder
function bubbleBackground() {
  // .9图地址
  Image($r('app.media.imageresizable_border'))
    .objectFit(ImageFit.Fill)
    .resizable({
      slice: {
        top: 3,
        bottom: 3,
        left: 5,
        right: 5
      }
    })
    .width('100%')
    .height('100%')
}

@Entry
@Component
struct NinePatchPage {
  build() {
    Column() {
      Column() {
        Text('200减30券')
          .fontColor('#0A59F7')
      }
      .padding(3)
      .background(bubbleBackground)

      Column() {
        Text('满减')
          .fontColor('#0A59F7')
      }
      .margin({ top: 20 })
      .padding(3)
      .background(bubbleBackground)

      Text('满5000减4000')
        .fontColor('#0A59F7')
        .textAlign(TextAlign.Center)
        .margin({ top: 20 })
        .padding(3)
        .borderImage({
          source: $r('app.media.imageresizable_border'),
          slice: {
            top: 3,
            bottom: 3,
            left: 5,
            right: 5
          },
          width: {
            top: 3,
            bottom: 3,
            left: 5,
            right: 5
          },
          repeat: RepeatMode.Stretch,
          fill: true
        })
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/PWvIrGExQ6qpbxoBCbQ37Q/zh-cn_image_0000002765916856.png "点击放大")
