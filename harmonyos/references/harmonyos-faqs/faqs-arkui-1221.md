---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1221
title: setCurrentTime方法指定Video组件开始播放位置偶现其它帧闪烁的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > setCurrentTime方法指定Video组件开始播放位置偶现其它帧闪烁的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:07+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0e42a954c890c6351fd4f73a204d446ba391810e04c188c6de263f193d810309
---

## 问题现象

进入一个页面时想让Video组件从一个指定的时间开始播放，比如第10秒，设置了参数this.controller.setCurrentTime(AppStorage.get('currentTime'),SeekMode.ClosestKeyframe)偶尔会出现定位不准，展示了视频第一帧的情况。已知在onStart中调用setCurrentTime一定会出现第一帧，在onPrepare中开始调用setCurrentTime偶尔会出现第一帧。是什么原因造成的该情况，如何避免？

问题代码示例参考如下：

```screen
@Entry
@Component
struct VideoExamplePage {
  previewUri: Resource = $r('app.media.startIcon');
  curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  isAutoPlay: boolean = true;
  showControls: boolean = true;
  controller: VideoController = new VideoController();
  @State totalTime: number = 0;

  build() {
    Column() {
      Video({
        src: $rawfile('videoTest.mp4'), // 替换已有视频资源
        currentProgressRate: this.curRate,
        controller: this.controller
      })
        .width('100%')
        .height(600)
        .autoPlay(this.isAutoPlay)
        .controls(this.showControls)
        .onPrepared((error?: DurationObject) => {
          if (error != undefined) {
            console.error(`onPrepared is ${error.duration}`);
            this.totalTime = error.duration;
            this.controller.setCurrentTime(10, SeekMode.Accurate); // 从第十秒开始播放
          }
        });
      Row() {
        Button('setTime')
          .onClick(() => {
            this.controller.setCurrentTime(10, SeekMode.Accurate); // 精准跳转到视频的10s位置
          })
          .margin(2);
      };
    };
  }
}

interface DurationObject {
  duration: number;
}
```

问题效果预览：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/yjlbN-ovRH-ttrtEV6i_Jg/zh-cn_image_0000002658953229.gif "点击放大")

## 背景知识

* [Video组件](../harmonyos-references/ts-media-components-video.md#video-1)中[onPrepared事件](../harmonyos-references/ts-media-components-video.md#onprepared)是视频准备完成时触发的事件，[onStart事件](../harmonyos-references/ts-media-components-video.md#onstart)是视频开始播放时触发的事件。
* [VideoController](../harmonyos-references/ts-media-components-video.md#videocontroller)是Video组件的控制器，其中[setCurrentTime方法](../harmonyos-references/ts-media-components-video.md#setcurrenttime8)可以指定视频播放的进度位置，并指定跳转模式。

## 问题定位

由于Video组件的跳转和播放都是在后台线程里进行，所以当视频自动播放时与跳转事件存在执行先后顺序的冲突。

## 分析结论

视频的play播放和seek跳转都是在后台线程里进行，由于冲突导致定位跳转过程中会偶现原位置的下一帧图片。

## 修改建议

取消自动播放，在onPrepare事件里先设置跳转，再进行播放，来代替[autoPlay(true)](../harmonyos-references/ts-media-components-video.md#autoplay)自动播放。

1. 设置autoPlay(true)修改为autoPlay(false)。
2. onPrepared事件修改参考如下：

   ```screen
   .onPrepared((error?: DurationObject) => {
     if (error != undefined) {
       console.info(`onPrepared is ${error.duration}`);
       this.totalTime = error.duration;
       this.controller.setCurrentTime(10, SeekMode.Accurate); // 从第十秒开始播放
       this.controller.start();
     }
   })
   ```

完整示例参考如下：

```screen
@Entry
@Component
struct VideoExamplePage {
  previewUri: Resource = $r('app.media.startIcon');
  curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  isAutoPlay: boolean = false;
  showControls: boolean = true;
  controller: VideoController = new VideoController();
  @State totalTime: number = 0;

  build() {
    Column() {
      Video({
        src: $rawfile('example.mp4'), // 替换已有视频资源
        currentProgressRate: this.curRate,
        controller: this.controller
      })
        .width('100%')
        .height(600)
        .controls(this.showControls)
        .onPrepared((error?: DurationObject) => {
          if (error != undefined) {
            console.info(`onPrepared is ${error.duration}`);
            this.totalTime = error.duration;
            this.controller.setCurrentTime(10, SeekMode.Accurate); // 从第十秒开始播放
            this.controller.start();
          }
        })
        .autoPlay(this.isAutoPlay);
      Row() {
        Button('setTime')
          .onClick(() => {
            this.controller.setCurrentTime(10, SeekMode.Accurate); // 精准跳转到视频的10s位置
          })
          .margin(2);
      };
    };
  }
}

interface DurationObject {
  duration: number;
}
```
