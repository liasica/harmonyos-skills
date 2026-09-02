---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-808
title: 如何解决Text组件无法根据内容自动拉伸背景图片的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Text组件无法根据内容自动拉伸背景图片的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:119e1e10bfe235f0b3d3da07a43d09e963fd0203d29eafb7222da52501b761e0
---

## 问题现象

给Text组件设置一个点九图的聊天气泡背景，聊天气泡根据内容自动拉伸，聊天气泡边上会变形、失真。

## 背景知识

* NinePatch图形：NinePatchDrawable图形是一种可拉伸的位图，可用作视图的背景。其他平台会自动调整图形的大小以适应视图的内容。NinePatch图形是标准PNG图片，包含一个额外的1像素边框。主要使用于内容长度自适应背景图。点九图是其他系统特有的一种图片格式，HarmonyOS上不支持.9资源文件进行安全拉伸。
* CSS实现点九图border-image：CSS不能直接使用点九图文件，但可以通过border-image属性结合border-image-slice来实现类似点九图的效果。这种方法可以在不失真的情况下对图片进行缩放。

## 解决方案

* **方案一**：通过设置Image组件的[resizable](../harmonyos-references/ts-basic-components-image.md#resizable11)属性实现图片的安全拉伸效果。
  + 通过@Builder装饰器封装容器背景样式，根据点九图设置合适的Image组件拉伸属性resizable。

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
  + 给容器组件Column/Row设置background属性为bubbleBackground函数，Text作为其子组件。

    ```ts
    Column() {
      Text('200减30券')
        .fontColor('#0A59F7')
    }
    .padding(3)
    .background(bubbleBackground)
    ```
* **方案二**：HarmonyOS支持[图片边框设置](../harmonyos-references/ts-universal-attributes-border-image.md)，通过给Text组件设置[borderImage](../harmonyos-references/ts-universal-attributes-border-image.md#borderimage)属性，实现图片自适应拉伸的效果，实现类似点九图的效果。

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/_HWNK3tRTwe4n5DjYf6RBQ/zh-cn_image_0000002658797163.png "点击放大")

## 总结

HarmonyOS上不支持.9资源文件进行安全拉伸，应通过Image组件resizable属性达到图片拉伸的效果。同理，要实现类似的边框拉伸效果，均可参照以上两种方案。
