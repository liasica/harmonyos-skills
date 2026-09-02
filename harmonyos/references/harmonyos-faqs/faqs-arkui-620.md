---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-620
title: 视频加载完成前会出现短暂黑屏现象
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 视频加载完成前会出现短暂黑屏现象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ee81f8662ae37cfa67beb1f49d4857a9b9886f112f51725bd142da8031d60c19
---

## 问题现象

视频在加载完成前会存在短暂黑屏的问题，黑屏一会儿后才加载对应的视频。

## 背景知识

* [Video](../harmonyos-guides/arkts-common-components-video-player.md)：用于播放视频文件并控制其播放状态的组件。
* [VideoOptions](../harmonyos-references/ts-media-components-video.md#videooptions对象说明)的previewUri配置项：即视频未播放时的预览图片路径，默认不显示图片。如果不指定预览图片，则会出现开始播放前，黑屏的现象。

## 问题定位

* 排查Video组件相关的代码，排查是否设置预览图，即在Video中是否配置了previewUri。

  ```ts
  Video({   
    src: $rawfile('app.media.videoTest'),
    controller: this.controller
    // Video中未配置previewUri
  })
    .autoPlay(false)
    .objectFit(ImageFit.Cover)
    .onPrepared(()=>{
      this.playVideo(this.isActive);
    })
    .onClick(()=>{
      // ...
    })
  ```
* 排查是否使用Visibility控制显隐，并在onStart中添加setTimeout方法，延迟显示Video组件。

  ```ts
  @Entry
  @Component
  struct VideoCreateComponent {
    controller: VideoController = new VideoController();

    build() {
      Column() {
        Video({
          src: $rawfile('longVideo.mp4'),
          controller: this.controller
        })
          .autoPlay(true)
          .controls(true)
          .width('100%')
          .height('200vp')
      }
    }
  }
  ```

## 分析结论

* 视频没有设置预览图，导致Video组件短暂显示黑。
* 未使用Visibility控制显隐，并未在onStart中添加setTimeout方法，延迟显示Video组件，导致Video组件短暂显示黑屏。

## 修改建议

* 方案一：给视频配置预览图。
* 方案二：使用Visibility控制显隐，并在onStart中添加setTimeout方法，延迟显示Video组件。

  ```ts
  @Entry
  @Component
  struct VideoCreateComponent {
    controller: VideoController = new VideoController();
    @State isVisible:Visibility = Visibility.Hidden;

    build() {
      Column() {
        Video({
          // 此处仅为样例，请开发者更换为可用视频资源地址
          src: $rawfile('example.mp4'),
          // 此处仅为样例，请开发者更换为可用图片资源地址
          previewUri: $r('app.media.img1'),
          controller: this.controller
        })
          .autoPlay(true)
          .controls(true)
          .width('100%')
          .height('200vp')
          .margin({bottom:16})

        Video({
          // 此处仅为样例，请开发者更换为可用视频资源地址
          src: $rawfile('example.mp4'),
          controller: this.controller
        })
          .visibility(this.isVisible)
          .autoPlay(true)
          .controls(true)
          .width('100%')
          .height('200vp')
          .onStart(() => {
            // 使用setTimeout设置延迟跳过黑屏阶段
            setTimeout(() => {
              this.controller.setCurrentTime(1, SeekMode.PreviousKeyframe);
              this.isVisible = Visibility.Visible;
            }, 150);
          })
      }
    }
  }
  ```
