---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-547
title: 视频切换时闪屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 视频切换时闪屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:15+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fbd26916535c74799e549480667f1e4bf71b146b43772711fa79579bac8186a5
---

## 问题现象

视频切换后，视频页面会短暂黑屏，之后才播放视频。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/3iew-12tTvqYEGKuhhOpuQ/zh-cn_image_0000002628551522.png "点击放大")

## 背景知识

* 基础属性[visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。
* [Video](../harmonyos-references/ts-media-components-video.md)组件用于播放视频文件并控制其播放状态。
* [LoadingProgress](../harmonyos-references/ts-basic-components-loadingprogress.md)组件用于显示加载动效。
* [setTimeout](../harmonyos-references/js-apis-timer.md#settimeout)用于设置一个定时器，该定时器在定时器到期后执行一个函数。

## 问题定位

1. 使用DevEco Testing查看问题组件，该问题组件为Stack组件下的Video组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/geetfk13TcyTbK5ahv1mAQ/zh-cn_image_0000002628391626.png "点击放大")
2. 通过该Video组件查看该页面的设置，该页面还设置了Image组件，视频切换时使用预览图片进行展示，切换完成后视频加载完成前不显示该预览图片，视频页面无内容，出现短暂黑屏。

   ```ts
   @Entry
   @Component
   struct SwiperCustomAnimationExample {
   // $rawfile('video1.mp4')和$rawfile('video2.mp4')需要替换为开发者需要的视频资源文件
   // $r('app.media.myposter1')和$r('app.media.myposter2')需要替换为开发者需要的图片资源文件
   @State videos: MyVideo[] = [new MyVideo($rawfile('video1.mp4'), $r('app.media.myposter1')),
      new MyVideo($rawfile('video2.mp4'), $r('app.media.myposter2'))];
   @State currentIndex: number = 0;
   @State isPlay: boolean = false;

   build() {
      Stack() {
         Swiper() {
         ForEach(this.videos, (video: MyVideo, index: number) => {
            Stack() {
               Video({
               src: video.src,
               controller: video.controller
               })
               .autoPlay(index === 0 ? true : false)

               Stack() {
               // 控制栏
               }

               // 模拟视频加载完整前无内容显示
               Image($r('app.media.black')) // $r('app.media.black')需要替换为开发者需要的图片资源文件
               .width('100%')
               .height('100%')
               .objectFit(ImageFit.Fill)
               .visibility(this.isPlay ? Visibility.Hidden : Visibility.Visible);

               // 未显示的视频内容使用预览图片进行占位
               Image(video.previewUri)
               .width('100%')
               .objectFit(ImageFit.Contain)
               .visibility(index === this.currentIndex ? Visibility.Hidden : Visibility.Visible); // 切换完成后视频加载完成前不显示该预览图片
            }
            .width('100%')
            .height('100%')
            .backgroundColor(Color.Black);
         });
         }
         .onChange((index: number) => {
         this.currentIndex = index;
         })
         .onAnimationStart(() => {
         this.videos[this.currentIndex].controller.pause();
         })
         .onAnimationEnd(() => {
         // 模拟重新加载视频资源
         this.videos[this.currentIndex].src = '';
         this.isPlay = false;
         setTimeout(() => {
            let url = 'video' + this.currentIndex + '.mp4';
            this.videos[this.currentIndex].src = $rawfile(url);
            this.videos[this.currentIndex].controller.start();
         }, 1000);
         });
      }
      .width('100%')
      .height('100%');
   }
   }
   ```

## 分析结论

视频切换时使用预览图片进行展示，切换完成后视频加载完成前不显示该预览图片，视频页面无内容，出现短暂黑屏，导致视频切换时闪屏。

## 修改建议

视频加载完成前继续显示该预览图片，开始播放后再隐藏该图片。

```ts
Video({
  src: video.src,
  controller: video.controller
})
  .width('100%')
  .height('90%')
  .objectFit(ImageFit.Contain)
  .controls(false)
  .autoPlay(index === 0 ? true : false)
  .onStart(() => {
    this.isPlay = true;
  })
```

```ts
// 未显示的视频内容使用预览图片进行占位
Image(video.previewUri)
  .width('100%')
  .objectFit(ImageFit.Contain)
  .visibility(this.isPlay ? Visibility.Hidden : Visibility.Visible); // 视频加载完成后不显示该图片
```

完整示例如下：

```ts
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

class MyVideo {
  src: ResourceStr = '';
  previewUri: ResourceStr = '';
  controller: VideoController = new VideoController();

  constructor(src: ResourceStr, previewUri: ResourceStr) {
    this.src = src;
    this.previewUri = previewUri;
  }
}

interface DurationObject {
  duration: number;
}

interface TimeObject {
  time: number;
}

@Entry
@Component
struct SwiperCustomAnimationExample {
  // $rawfile('video1.mp4')和$rawfile('video2.mp4')需要替换为开发者需要的视频资源文件
  // $r('app.media.myposter1')和$r('app.media.myposter2')需要替换为开发者需要的图片资源文件
  @State videos: MyVideo[] = [new MyVideo($rawfile('video1.mp4'), $r('app.media.myposter1')),
    new MyVideo($rawfile('video2.mp4'), $r('app.media.myposter2'))];
  @State currentIndex: number = 0;
  @State isPlay: boolean = false;
  @State durationTime: number[] = [0, 0];
  @State currentTime: number[] = [0, 0];

  aboutToAppear(): void {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setWindowLayoutFullScreen(true);
      let systemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#00000000',
        statusBarContentColor: '#ffffff'
      };
      lastWindow.setWindowSystemBarProperties(systemBarProperties);
    });
  }

  // 格式化时间
  timeConvert(time: number): string {
    let min: number = Math.floor(time / 60);
    let second: string = (time % 60).toFixed(0);
    second = second.padStart(2, '0');
    return `${min}:${second}`;
  }

  build() {
    Stack() {
      Swiper() {
        ForEach(this.videos, (video: MyVideo, index: number) => {
          Stack() {
            Video({
              src: video.src,
              controller: video.controller
            })
              .width('100%')
              .height('90%')
              .objectFit(ImageFit.Contain)
              .controls(false)
              .autoPlay(index === 0 ? true : false)
              .onStart(() => {
                this.isPlay = true;
              })
              .onPause(() => {
                this.isPlay = false;
              })
              .onPrepared((e?: DurationObject) => {
                if (e !== undefined) {
                  this.durationTime[index] = e.duration;
                }
              })
              .onUpdate((e?: TimeObject) => {
                if (e !== undefined) {
                  this.currentTime[index] = e.time;
                }
              });

            // 控制栏
            Stack() {
              Row() {
                // $r('app.media.ic_video_play')和$r('app.media.ic_video_pause')需要替换为开发者需要的图片资源文件
                Image(this.isPlay ? $r('app.media.ic_video_play') : $r('app.media.ic_video_pause'))
                  .width(25)
                  .height(25)
                  .onClick(() => {
                    if (this.isPlay) {
                      video.controller.pause();
                      this.isPlay = false;
                    } else {
                      video.controller.start();
                      this.isPlay = true;
                    }
                  });

                // 左侧时间
                Text(this.timeConvert(this.currentTime[index]))
                  .fontColor(Color.White)
                  .textAlign(TextAlign.End)
                  .fontWeight(FontWeight.Regular)
                  .margin({ left: 10 });

                Slider({
                  value: this.currentTime[index],
                  min: 0,
                  max: this.durationTime[index],
                  style: SliderStyle.OutSet
                })
                  .blockColor(Color.White)
                  .trackColor(Color.Gray)
                  .selectedColor('#007DFF')
                  .showTips(false)
                  .width(230)
                  .onChange((value: number, mode: SliderChangeMode) => {
                    if (mode === SliderChangeMode.Begin) {
                      video.controller.pause();
                    } else if (mode === SliderChangeMode.Moving) {
                      video.controller.setCurrentTime(value);
                    } else if (mode === SliderChangeMode.End) {
                      video.controller.start();
                    }
                  });

                // 右侧时间
                Text(this.timeConvert(this.durationTime[index]))
                  .id('durationTimeText')
                  .fontColor(Color.White)
                  .fontWeight(FontWeight.Regular);

                // $r('app.media.full')需要替换为开发者需要的图片资源文件
                Image($r('app.media.full'))
                  .width(20)
                  .height(20)
                  .objectFit(ImageFit.Contain)
                  .margin({ left: 5 });
              }
              .width('100%')
              .justifyContent(FlexAlign.Center)
              .padding({ left: 10, right: 5 })
              .margin({ bottom: 5 });
            }
            .width('100%')
            .height('100%')
            .alignContent(Alignment.Bottom);

            // 模拟视频加载完整前无内容显示
            Image($r('app.media.black')) // $r('app.media.black')需要替换为开发者需要的图片资源文件
              .width('100%')
              .height('100%')
              .objectFit(ImageFit.Fill)
              .visibility(this.isPlay ? Visibility.Hidden : Visibility.Visible);

            // 未显示的视频内容使用预览图片进行占位
            Image(video.previewUri)
              .width('100%')
              .objectFit(ImageFit.Contain)
              .visibility(this.isPlay ? Visibility.Hidden : Visibility.Visible); // 视频加载完成后不显示该图片
          }
          .width('100%')
          .height('100%')
          .backgroundColor(Color.Black);
        });
      }
      .vertical(true)
      .loop(false)
      .width('100%')
      .height('100%')
      .indicator(false)
      .curve(Curve.EaseIn)
      .index(this.currentIndex)
      .onChange((index: number) => {
        this.currentIndex = index;
      })
      .onAnimationStart(() => {
        this.videos[this.currentIndex].controller.pause();
      })
      .onAnimationEnd(() => {
        // 模拟重新加载视频资源
        this.videos[this.currentIndex].src = '';
        this.isPlay = false;
        setTimeout(() => {
          let url = 'video' + this.currentIndex + '.mp4';
          this.videos[this.currentIndex].src = $rawfile(url);
          this.videos[this.currentIndex].controller.start();
        }, 1000);
      });
    }
    .width('100%')
    .height('100%');
  }
}
```
