---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-530
title: 视频播放出现闪屏
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 视频播放出现闪屏
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:12+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c96289577388045ccc52c4186ea1b44756afb71fde3247160e55c8c75048a55c
---

## 问题现象

当视频播放组件的生命周期开始时，界面短暂闪烁，出现其他视频中不期望出现的颜色。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/N-YgC5HgRQa1MMLbRx20Ug/zh-cn_image_0000002658790425.png "点击放大")

## 背景知识

* [Video](../harmonyos-references/ts-media-components-video.md)：用于播放视频文件并控制其播放状态的组件。其previewUri参数可设置视频未播放时的预览图片。
* [backgroundcolor](../harmonyos-references/ts-universal-attributes-background.md#backgroundcolor)属性：通用属性，为组件添加背景颜色，默认为白色。

## 问题定位

1. 使用DevEco Testing查看问题组件，该组件为Video组件。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/n-8oAzKNS_-qfGmJ2ZGpyA/zh-cn_image_0000002628551064.png "点击放大")
2. 查看该Video组件的设置，该Video组件未设置previewUri参数显示预览图。

   ```ts
   @Entry
   @Component
   export struct Index {
     @State videoSrc: ResourceStr = '';
     controller: VideoController = new VideoController();

     build() {
       Stack({ alignContent: Alignment.Start }) {
         Video({
           // 未设置previewUri参数显示预览图
           src: this.videoSrc,
           controller: this.controller
         })
       }
     }
   }
   ```

## 分析结论

使用Video组件时，未通过previewUri参数设置预览图，在Video组件的加载过程中界面显示Video组件背景。这会导致在视频播放的过程中出现预期之外的色彩，引发闪屏问题。

## 修改建议

使用Video组件时，通过previewUri参数设置预览图，避免短暂黑屏、白屏、彩屏的出现。

```ts
import { window } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

interface DurationObject {
  duration: number;
}

interface TimeObject {
  time: number;
}

@Entry
@Component
struct Index {
  private imgSrc: ResourceStr = $r('app.media.myposter1'); // $r('app.media.myposter1')需要替换为开发者需要的图片资源文件
  @State videoSrc: ResourceStr = '';
  controller: VideoController = new VideoController();
  @State isPlay: boolean = false;
  @State durationTime: number = 0;
  @State currentTime: number = 0;
  @State sliderWidth: number = 230;
  @State @Watch('changeOrientation') isFull: boolean = false;
  context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

  aboutToAppear(): void {
    // 模拟视频加载
    setTimeout(() => {
      this.videoSrc = $rawfile('video1.mp4'); // $rawfile('video1.mp4')需要替换为开发者需要的视频资源文件
    }, 1000);
    window.getLastWindow(this.context).then((lastWindow) => {
      lastWindow.setWindowLayoutFullScreen(true);
      let systemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#00000000',
        statusBarContentColor: '#ffffff'
      };
      lastWindow.setWindowSystemBarProperties(systemBarProperties);
    });
  }

  timeConvert(time: number): string {
    let min: number = Math.floor(time / 60);
    let second: string = (time % 60).toFixed(0);
    second = second.padStart(2, '0');
    return `${min}:${second}`;
  }

  changeOrientation() {
    let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(context).then((lastWindow) => {
      lastWindow.setPreferredOrientation(this.isFull ? window.Orientation.AUTO_ROTATION_LANDSCAPE :
        window.Orientation.PORTRAIT);
      // 进入全屏时进入沉浸式，退出全屏时再显示状态栏和导航栏
      lastWindow.setWindowLayoutFullScreen(this.isFull);
      lastWindow.setWindowSystemBarEnable(this.isFull ? [] : ['status', 'navigation']);
    });
  }

  onPageHide(): void {
    // 应用退到后台时暂停视频
    this.controller.pause();
  }

  onPageShow(): void {
    // 应用返回时播放视频
    this.controller.start();
  }

  build() {
    Stack({ alignContent: Alignment.Start }) {
      Video({
        previewUri: this.imgSrc, // 设置previewUri参数显示预览图
        src: this.videoSrc,
        controller: this.controller
      })
        .width('100%')
        .objectFit(ImageFit.Contain)
        .controls(false)
        .loop(true)
        .autoPlay(true)
        .backgroundColor(Color.Black)
        .onPrepared((e?: DurationObject) => {
          this.isPlay = true;
          if (e !== undefined) {
            this.durationTime = e.duration;
          }
        })
        .onUpdate((e?: TimeObject) => {
          if (e !== undefined) {
            this.currentTime = e.time;
          }
        })
        .onSizeChange(() => {
          this.sliderWidth = this.isFull ? 650 : 230;
        });

      Stack() {
        Row() {
          // $r('app.media.ic_video_play')和$r('app.media.ic_video_pause')需要替换为开发者需要的图片资源文件
          Image(this.isPlay ? $r('app.media.ic_video_play') : $r('app.media.ic_video_pause'))
            .width(25)
            .height(25)
            .onClick(() => {
              if (this.isPlay) {
                this.controller.pause();
                this.isPlay = false;
              } else {
                this.controller.start();
                this.isPlay = true;
              }
            });

          // 左侧时间
          Text(this.timeConvert(this.currentTime))
            .fontColor(Color.White)
            .textAlign(TextAlign.End)
            .fontWeight(FontWeight.Regular)
            .margin({ left: 10 });

          Slider({
            value: this.currentTime,
            min: 0,
            max: this.durationTime,
            style: SliderStyle.OutSet
          })
            .blockColor(Color.White)
            .trackColor(Color.Gray)
            .selectedColor('#007DFF')
            .showTips(false)
            .width(this.sliderWidth)
            .onChange((value: number, mode: SliderChangeMode) => {
              if (mode === SliderChangeMode.Begin) {
                this.controller.pause();
              } else if (mode === SliderChangeMode.Moving) {
                this.controller.setCurrentTime(value);
              } else if (mode === SliderChangeMode.End) {
                this.controller.start();
              }
            });

          // 右侧时间
          Text(this.timeConvert(this.durationTime))
            .id('durationTimeText')
            .fontColor(Color.White)
            .fontWeight(FontWeight.Regular);

          // $r('app.media.out')和$r('app.media.full')需要替换为开发者需要的图片资源文件
          Image(this.isFull ? $r('app.media.out') : $r('app.media.full'))
            .width(20)
            .height(20)
            .objectFit(ImageFit.Contain)
            .onClick(() => {
              this.isFull = !this.isFull; // 进入全屏或退出全屏
            })
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
    }
    .height('100%')
    .width('100%')
    .backgroundColor(Color.Black)
    .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]); // 扩展页面区域到导航栏和状态栏
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/ccCtrN6HQt-eSWKINPfCWw/zh-cn_image_0000002658910381.png "点击放大")
