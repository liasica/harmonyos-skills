---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1478
title: 如何实现视频自动播放下一集
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何实现视频自动播放下一集
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6f09f2809bc33de3fcc32441cbc7ea2329c1830b6500710f2b6d368b36a162dd
---

## 问题现象

如何实现当前视频播放完之后自动播放下条视频。

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/hA9W8MA6TMqe2ecx6AfsJw/zh-cn_image_0000002658965023.gif "点击放大")

## 背景知识

* [Video组件](../harmonyos-guides/arkts-common-components-video-player.md)用于播放视频文件并控制其播放状态，常用于短视频和应用内部视频的列表页面。
* [Swiper组件](../harmonyos-guides/arkts-layout-development-create-looping.md)提供滑动轮播显示的能力，可以用于实现短视频切换功能。

## 解决方案

实现思路如下：

1. 整体架构：使用Swiper嵌套Video组件实现短视频播放功能主体。
2. 视频播放完成后自动跳转下条视频：可以通过调用Swiper组件的[showNext](../harmonyos-references/ts-container-swiper.md#shownext)事件主动跳转下一页。
3. 页面切换后视频自动播放：Swiper组件切换页面时则会触发[onChange](../harmonyos-references/ts-container-swiper.md#onchange)回调，可以在该回调中调用Video组件的[start](../harmonyos-references/ts-media-components-video.md#start)事件开启视频播放。

完整示例代码如下：

```ts
class VideoClass { // 创建视频类
  controller: VideoController = new VideoController();
  videoSrc: Resource = $rawfile('videoTest.mp4');
}

@Entry
@Component
struct VideoAutomaticallyPlays {
  private swiperController: SwiperController = new SwiperController();
  private videoList: Array<VideoClass> = [];
  @State isShow: boolean = true; // 控制暂停按键的显隐
  @State lastShow: number = 0;

  aboutToAppear(): void {
    for (let i = 0; i < 10; i++) {
      this.videoList.push(new VideoClass()); // 创建视频实例
    }
  }

  build() {
    Column() {
      Swiper(this.swiperController) {
        ForEach(this.videoList, (item: VideoClass) => {
          Stack() {
            Video({
              src: item.videoSrc,
              controller: item.controller
            })
              .height('100%')
              .width('100%')
              .controls(false) // 关闭视频控制栏
              .onFinish(() => {
                this.swiperController.showNext(); // 跳转下个视频
              });
            Row() {
              Column() {
                Text('@XXX')
                  .fontColor(Color.White);
              }
              .height('100%')
              .justifyContent(FlexAlign.End)
              .padding({
                bottom: 60
              });

              Column({ space: 40 }) {
                Image($r('app.media.love'))
                  .width(30)
                  .height(30);
                Image($r('app.media.comment'))
                  .width(30)
                  .height(30);
                Image($r('app.media.share'))
                  .width(30)
                  .height(30);
              }
              .height('100%')
              .justifyContent(FlexAlign.End)
              .padding({
                bottom: 150
              });
            }
            .width('100%')
            .height('100%')
            .justifyContent(FlexAlign.SpaceBetween)
            .padding({
              left: 20,
              right: 20
            });

            Image($r('app.media.play'))
              .width(30)
              .height(30)
              .visibility(this.isShow ? Visibility.Visible : Visibility.None); // 是否显示暂停图标
          }
          .onClick(() => { // 点击切换视频播放状态
            if (this.isShow) {
              item.controller.start(); // 开始播放
            } else {
              item.controller.pause(); // 暂停播放
            }
            this.isShow = !this.isShow;
          });
        });
      }
      .width('100%')
      .height('100%')
      .indicator(false)
      .vertical(true)
      .loop(false)
      .autoPlay(false)
      .onChange((index: number) => { // 页面切换时触发的回调
        this.videoList[this.lastShow].controller.stop();
        this.videoList[index].controller.start(); // 启动视频播放
        this.lastShow = index;
        this.isShow = false;
      });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
