---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-624
title: 短视频开启自动连播失败
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 短视频开启自动连播失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:e3f47980626b11570d76b3f51d5b8a29e860cb682ce731a7cdd61cb66a41a891
---

## 问题现象

进入短视频播放页，设置自动播放，播完一集后跳转下一集，仍需要手动点击才能播放。

## 背景知识

* [Video组件](../harmonyos-guides/arkts-common-components-video-player.md)用于播放视频文件并控制其播放状态，常用于短视频和应用内部视频的列表页面。
* [Swiper组件](../harmonyos-guides/arkts-layout-development-create-looping.md)提供滑动轮播显示的能力，可以用于实现短视频切换功能。

## 问题定位

1. 使用DevEco Testing中的UIViewer工具，查看短视频播放页的布局：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/biRzkMNtTNWLDFDwmO0pZg/zh-cn_image_0000002628394268.png "点击放大")

   发现页面使用Video、Swiper组件搭配实现短视频播放功能，不涉及与H5页面的交互。
2. 可以通过调用Swiper组件的showNext()事件主动跳转下一页，而页面切换时则会触发[onChange](../harmonyos-references/ts-container-swiper.md#onchange)、[onAnimationStart](../harmonyos-references/ts-container-swiper.md#onanimationstart9)、[onAnimationEnd](../harmonyos-references/ts-container-swiper.md#onanimationend9)这三个回调。排查代码，查看是否有在Swiper的页面切换回调里设置视频播放。

## 分析结论

在上个视频播放完后，只调用了showNext()跳转到下个视频，但没有调用Video组件的start()事件开始视频播放，导致切换下个视频后仍需手动点击开始。

## 修改建议

首个视频播放完后，调用showNext()跳转下个视频，同时在Swiper的页面切换回调里调用Video组件的start()事件播放视频。以onChange事件为例：

```ts
class VideoSet {
  controller: VideoController = new VideoController();
  videoSrc: Resource = $rawfile('videoTest.mp4'); // 需替换为实际资源
}

@Entry
@Component
struct VideoListAutoPlayPage {
  private swiperController: SwiperController = new SwiperController();
  private videoList: Array<VideoSet> = [];
  @State isShow: boolean = true;

  aboutToAppear(): void {
    for (let i = 0; i < 10; i++) {
      this.videoList.push(new VideoSet());
    }
  }

  build() {
    Column() {
      Swiper(this.swiperController) {
        ForEach(this.videoList, (item: VideoSet) => {
          Stack() {
            Video({
              src: item.videoSrc,
              controller: item.controller
            })
              .height('100%')
              .width('100%')
              .controls(false)
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
                // 需替换为实际资源
                Image($r('app.media.love'))
                  .width(30)
                  .height(30);
                // 需替换为实际资源
                Image($r('app.media.comment'))
                  .width(30)
                  .height(30);
                // 需替换为实际资源
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
            // 需替换为实际资源
            Image($r('app.media.play'))
              .width(30)
              .height(30)
              .visibility(this.isShow ? Visibility.Visible : Visibility.None);
          }
          .onClick(() => {
            if (this.isShow) {
              item.controller.start();
            } else {
              item.controller.pause();
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
      .onChange((index: number) => {
        this.videoList[index].controller.start(); // 启动视频播放
      });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
