---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1420
title: 如何给视频背景添加高斯模糊
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何给视频背景添加高斯模糊
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:19+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bfc7ddf353ebba5931d16a1bc967c158c91055c95d7827e9a8f824341c1a501f
---

## 问题现象

当视频的尺寸未能占满整个容器，如何实现将同一视频资源进行高斯模糊处理后，作为背景填充至空白区域？

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/oRVOFegbQ5-MlfPvhFTyQA/zh-cn_image_0000002658962957.png "点击放大")

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/VM5pakloQt604u2I-81eDQ/zh-cn_image_0000002628603742.png "点击放大")

## 背景知识

* [模糊](../harmonyos-guides/arkts-blur-effect.md)可以用来体现界面空间的纵深感，区分前后元素的层级关系。[blur](../harmonyos-references/ts-universal-attributes-image-effect.md#blur)方法可以为组件添加内容模糊效果。当模糊内容和模糊半径都不需要变化时，建议使用静态模糊接口blur。

  而高斯模糊属于模糊的一种，能够更好地保留边缘，使模糊效果更平滑自然，在[BlurStyle](../harmonyos-references/ts-universal-attributes-background.md#blurstyle9)中选择景深模糊即为高斯模糊，包括BACKGROUND\_THIN、BACKGROUND\_REGULAR、BACKGROUND\_THICK等。
* [Stack](../harmonyos-references/ts-container-stack.md)堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

## 解决方案

如效果图所示，页面采用两个视频叠加播放，其中背景视频添加了高斯模糊效果。可通过[foregroundBlurStyle](../harmonyos-references/ts-universal-attributes-foreground-blur-style.md#foregroundblurstyle)属性设置高斯模糊，并结合Stack布局实现该效果。

```ts
@Entry
@Component
struct AddGaussianBlurToVideoBackground {
  // 此处'videoHW.mov'仅作示例，请开发者自行替换
  @State previewUri: Resource = $rawfile('videoHW.mov');
  isAutoPlay: boolean = true;
  showControls: boolean = false;
  controller: VideoController = new VideoController();
  controller1: VideoController = new VideoController();

  build() {
    Column() {
      Stack() {
        Video({
          src: this.previewUri,
          previewUri: this.previewUri,
          controller: this.controller
        })
          .width('100%')
          .height(300)
          .autoPlay(this.isAutoPlay)
          .controls(this.showControls) // 设置控制视频播放的控制栏是否显示
          .loop(true); // 设置是否单个视频循环播放
        Row() {
        }
        .width('100%')
        .height(300)
        // 实现高斯模糊核心代码
        .foregroundBlurStyle(BlurStyle.BACKGROUND_ULTRA_THICK, // 选择模糊类型
          {
            colorMode: ThemeColorMode.DARK, // 建议根据背景模式选择，暗色推荐dark
            adaptiveColor: AdaptiveColor.DEFAULT,
            scale: 0.05 // 范围0~1。若阴影边缘过于明显，可以调高；若阴影过于不可见，可以调低。
          });

        Row() {
          Video({
            src: this.previewUri,
            previewUri: this.previewUri,
            controller: this.controller1
          })
            .autoPlay(this.isAutoPlay)
            .controls(this.showControls)
            .loop(true)
            .objectFit(ImageFit.Fill);
        }
        .width('80%')
        .height(200);
      };
    }.justifyContent(FlexAlign.Center).height('100%');
  }
}
```

## 常见FAQ

Q：两个播放器叠加的话，对于性能有多大的影响？

A：视频叠加播放实际上是由布局来控制两个播放器组件，对整个页面来说只是增加了一个播放器组件，实际上对性能并不会有什么影响。

Q：若使用AVPlayer播放视频，XComponent组件进行界面渲染，如何实现类似的高斯模糊效果？

A：无论是Video组件还是XComponent组件，都可以参考示例代码，使用foregroundBlurStyle属性设置高斯模糊效果，结合Stack布局实现。由于该方案需要2个XComponent组件，会生成2个surfaceId，所以需要创建2个AVPlayer实例去接收不同的surfaceId，从而实现视频的同步播放。
