---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-534
title: 视频预览图尺寸和视频的尺寸不一致
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 视频预览图尺寸和视频的尺寸不一致
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8f202b61a6d25f55555fdf721cc82305ae68d6f77c2ef0d67e29dc64339e1be0
---

## 问题现象

视频预览图尺寸和视频内容尺寸不一致，应该如何解决该问题？

## 背景知识

* [aspectRatio](../harmonyos-references/ts-universal-attributes-layout-constraints.md#aspectratio)：指定当前组件的宽高比，aspectRatio=width/height。设置aspectRatio属性后，组件宽高会受父组件内容区大小限制。不设置aspectRatio属性或者aspectRatio属性的值为非法值(小于等于0)时不生效。
  + 仅设置width、aspectRatio时，height=width/aspectRatio。
  + 仅设置height、aspectRatio时，width=height\*aspectRatio。
  + 同时设置width、height和aspectRatio时，height不生效，height=width/aspectRatio。
* [objectFit](../harmonyos-references/ts-basic-components-image.md#objectfit)(value:ImageFit)：设置填充效果。值为[ImageFit](../harmonyos-references/ts-appendix-enums.md#imagefit)枚举类型，默认值是ImageFit.Cover。
* [VideoOptions](../harmonyos-references/ts-media-components-video.md#videooptions对象说明)：定义Video组件的具体配置参数。其中的previewUri配置项可以指定视频未播放时的预览图片，默认不显示图片，值为预览图的路径。

## 问题定位

使用DevEco Testing工具查看UI结构，发现预览图是一个Image组件，显示预览图时只有Image组件，视频播放时视频播放组件覆盖了Image组件。

* 排查预览图和视频使用的填充模式，如果预览图采用contain模式，这会保持原比例，显示黑边。播放器从封面切换到视频流时，视频切换为cover或fill模式来填充容器，这会导致视频预览图尺寸和视频内容尺寸不一致。
* 排查播放容器和预览图是否设置宽高比约束（是否使用aspectRatio属性），没有设置约束的话，会导致视频预览图尺寸和视频内容尺寸不一致。

## 分析结论

使用了自行封装的视频播放组件，使用Image组件覆盖住视频播放组件作为预览图。

* 预览图和视频使用的填充模式不一致，导致视频预览图尺寸和视频内容尺寸不一致。
* 播放容器和预览图未正确设置宽高比约束，导致视频预览图尺寸和视频内容尺寸不一致。

## 修改建议

* 方案一：使用aspectRatio属性强制锁定图片和视频的宽高比。

  ```ts
  @Entry
  @Component
  struct OptionOne {
    @State ShowVideo: boolean = false;
    ratio: number = 16 / 9; // 根据需要调整宽高比
    controller: VideoController = new VideoController();

    build() {
      Stack() {
        Image($r('app.media.preview')) // 图片
          .width('100%')
          .aspectRatio(this.ratio)
          .onClick(() => {
            this.controller.start();
          });
        Video({
          controller: this.controller,
          src: $rawfile('videoTest.mp4')
        })
          .width('100%')
          .aspectRatio(this.ratio)
          .visibility(this.ShowVideo ? Visibility.Visible : Visibility.Hidden)
          .onStart(() => {
            // 开始播放视频时显示视频组件，覆盖预览图
            this.ShowVideo = true;
          });
      };
    }
  }
  ```
* 方案二：预览图推荐使用Video组件的previewUri配置项。

  ```ts
  @Entry
  @Component
  struct OptionTwo {
    ratio: number = 16 / 9; // 根据需要调整宽高比
    controller: VideoController = new VideoController();

    build() {
      Stack() {
        Video({
          previewUri: $r('app.media.preview'),
          controller: this.controller,
          src: $rawfile('videoTest.mp4')
        })
          .width('100%')
          .aspectRatio(this.ratio);
      };
    }
  }
  ```
