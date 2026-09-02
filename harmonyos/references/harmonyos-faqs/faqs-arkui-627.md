---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-627
title: 如何解决Video组件播放前出现预览黑屏的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何解决Video组件播放前出现预览黑屏的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7a513acaf77e4b9a24df3cd519a3e5ee56a7e3957cf286108113389d4f2a17f1
---

## 问题现象

Video组件在未播放视频内容之前是黑色的，开始播放后，再点击暂停，才可以正常展示暂停时的视频内容。

问题现象效果如图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/Nxnh2CSpTKaOnWNqj6tGNA/zh-cn_image_0000002658913487.png "点击放大")

## 背景知识

[Video](../harmonyos-references/ts-media-components-video.md)：用于播放视频文件并控制其播放状态的组件。

## 问题定位

根据[VideoOptions对象说明](../harmonyos-references/ts-media-components-video.md#videooptions对象说明)，VideoOptions的previewUri属性（即视频未播放时的预览图片路径），默认不显示图片。如果不指定预览图片，则会出现开始播放前，黑屏的现象。

## 分析结论

针对这个问题，可以考虑以下两种方案：

* 给视频设置一个展示图片。
* 把视频设置成自动播放，再使用setTimeout设置延迟跳过黑屏阶段。

## 修改建议

根据问题定位可知，问题现象的根因在于没有手动为视频设置预览图片，因此可以参考以下代码进行修复：

* **方案一：给视频设置一个海报。**

  **代码示例如下：**

  ```ts
  Video({
    src: $r('app.media.videoTest'), // $r('app.media.videoTest')仅作展示，使用时请开发者自行替换
    previewUri: $r('app.media.example'), // $r('app.media.example')仅作展示，使用时请开发者自行替换
    controller: this.controller
  })
    .height('50%');
  ```

  在视频播放前显示预览图片，建议将视频的第一帧作为预览图片。
* **方案二：自动播放，跳过黑屏阶段。**

  部分场景，如上下滑动刷新不同视频，且要求视频自动播放的时候，可以考虑使用这个方案。

  **代码示例如下：**

  ```ts
  Video({
    src: $r('app.media.videoTest'), // $r('app.media.videoTest')仅作展示，使用时请开发者自行替换
    controller: this.controller
  })
    .visibility(this.isVisible)
    .autoPlay(true) // 设置自动播放
    .loop(true)
    .controls(true)
    .width('100%')
    .height('50%')
    .onStart(() => {
      setTimeout(() => { // 使用setTimeout设置延迟跳过黑屏阶段
        this.controller.setCurrentTime(1, SeekMode.PreviousKeyframe);
        this.isVisible = Visibility.Visible;
      }, 150);
    });
  ```

完整示例代码参考如下：

```ts
@Entry
@Component
struct video {
  controller: VideoController = new VideoController();
  @State isVisible: Visibility = Visibility.None;

  build() {
    Column() {
      Video({
        src: $r('app.media.videoTest'), // $r('app.media.videoTest')仅作展示，使用时请开发者自行替换
        previewUri: $r('app.media.example'), // $r('app.media.example')仅作展示，使用时请开发者自行替换
        controller: this.controller
      })
        .height('50%');

      Video({
        src: $r('app.media.videoTest'), // $r('app.media.videoTest')仅作展示，使用时请开发者自行替换
        controller: this.controller
      })
        .visibility(this.isVisible)
        .autoPlay(true) // 设置自动播放
        .loop(true)
        .controls(true)
        .width('100%')
        .height('50%')
        .onStart(() => {
          setTimeout(() => { // 使用setTimeout设置延迟跳过黑屏阶段
            this.controller.setCurrentTime(1, SeekMode.PreviousKeyframe);
            this.isVisible = Visibility.Visible;
          }, 150);
        });
    };
  }
}
```
