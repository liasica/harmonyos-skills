---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-13
title: 平板上视频显示不全
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板上视频显示不全
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:db073e067b85c67e774702e5ecf4594b7a0d9e72e0edef17011a76574e2889f6
---

## 问题现象

当用户在平板上播放视频时，出现视频显示不全、画面被截断的情况。

## 背景知识

[Video](../harmonyos-references/ts-media-components-video.md)组件的[objectFit](../harmonyos-references/ts-media-components-video.md#objectfit)属性用于控制视频的填充效果，[ImageFit](../harmonyos-references/ts-appendix-enums.md#imagefit).Cover表示保持宽高比进行缩小或者放大，使得视频两边都大于或等于显示边界，对齐方式为水平居中，当视频源的宽高比与Video组件的宽高比不一致，就会导致视频显示不全，被截断，如果想要宽高比与组件宽高比不一致的视频完全显示，需要使用ImageFit.Contain。

## 问题定位

检查代码中Video组件objectFit属性的内容是否为ImageFit.Cover，例如下面代码。

```ts
@Entry
@Component
struct VideoPage {
  @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  controller: VideoController = new VideoController();

  build() {
    RelativeContainer() {
      Video({
        src: $rawfile('example.mp4'),
        currentProgressRate: this.curRate,
        controller: this.controller
      })
        .width('80%')
        .height('100%')
        // 检查objectFit设置值
        .objectFit(ImageFit.Cover)
    }
    .height('100%')
    .width('100%')
  }
}
```

## 分析结论

代码中Video组件objectFit属性配置成了ImageFit.Cover，随着设备的变化，屏幕宽高比发生变化，视频播放页面的组件宽高比也随之变化，导致视频宽高比与组件宽高比不一致时，播放的视频会出现显示不全或被截断的情况。

## 修改建议

将代码中Video组件的objectFit属性设置为ImageFit.Contain，保证视频完全显示的情况下自动适配屏幕。代码如下：

```ts
@Entry
@Component
struct VideoPageDemo {
  @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  controller: VideoController = new VideoController();

  build() {
    RelativeContainer() {
      Video({
        src: $rawfile('example.mp4'), // 实际开发替换为实际资源
        currentProgressRate: this.curRate,
        controller: this.controller
      })
        .width('80%')
        .height('100%')
        .objectFit(ImageFit.Contain)
    }
    .height('100%')
    .width('100%')
  }
}
```
