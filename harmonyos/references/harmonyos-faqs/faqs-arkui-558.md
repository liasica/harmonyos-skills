---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-558
title: 视频扩散播放效果实现
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 视频扩散播放效果实现
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9923c61bfe05a8223b4cb72b93f7629673b75eda68ad65984a71fb18638d4038
---

## 问题现象

在播放视频时，如何实现以下的画中画扩散播放效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/5ZiX-TmjQ9C5i8fh1gmaMQ/zh-cn_image_0000002628552012.png "点击放大")

## 背景知识

* [clipShape](../harmonyos-references/ts-universal-attributes-sharp-clipping.md#clipshape12)是HarmonyOS提供的一种组件通用属性，该属性可按指定的形状对当前组件进行裁剪。
* [setInterval](../harmonyos-references/js-apis-timer.md#setinterval)可用于重复调用一个函数，在每次调用之间具有固定的时间延迟，删除该定时器需手动调用clearInterval接口。
* [Video](../harmonyos-references/ts-media-components-video.md)组件是一种用于播放视频文件并控制其播放状态的组件。
* [Stack](../harmonyos-references/ts-container-stack.md)是堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

## 解决方案

1. 在Column容器中添加Stack组件，该组件依次设置了Button子组件以及由该Button组件控制显隐的Video组件。
2. 给Video组件添加clipShape属性，裁剪部分是一个Circle圆形区域，其宽度和高度为circleWidth且初始值为0，并通过circleWidth和xy坐标值设置好相应的偏移量。

   ```ts
   // 按指定的形状对当前组件进行裁剪
   .clipShape(new Circle({
     width: this.circleWidth.toString() + '%',
     height: this.circleWidth.toString() + '%'
   })
     .offset({
       x: (45 - this.circleWidth * 0.5 + this.clickX * 10).toString() + '%',
       y: (45 - this.circleWidth * 0.5 + this.clickY * 10).toString() + '%'
     }))
   ```
3. 点击Button按钮，将isShow的值设置为true，并获取屏幕的宽高，以及点击位置的xy坐标值，其中boolean类型的isShow变量可用于控制Video组件的显隐。

   ```ts
   .onClick((event: ClickEvent) => {
     window.getLastWindow(this.getUIContext().getHostContext(),
       (err: BusinessError, windowObj) => {
         if (err.code) {
           console.error(`Failed to getLastWindow. Code：${err.code}，message：${err.message}`);
         }
         let windowClass = windowObj;
         windowClass.setWindowSystemBarEnable([]); // 隐藏系统导航栏
       });
     this.isShow = true;
     let displayClass = display.getDefaultDisplaySync();
     let width: number = this.getUIContext().px2vp(displayClass.width);
     let height: number = this.getUIContext().px2vp(displayClass.height);
     this.clickX = event.displayX / width;
     this.clickY = event.displayY / height;
     // 该段代码的核心部分，重复执行circleWidth++，实现画面扩散播放效果
     this.intervalID = setInterval(() => {
       this.circleWidth++;
       if (this.isShow && this.circleWidth === 1000) {
         // 清除该定时器接口
         clearInterval(this.intervalID);
       }
     }, 30);
     setTimeout(() => {
       this.isAutoPlay = true;
     }, 1000);
   });
   ```
4. onClick事件还会调用setInterval方法，以30毫秒的间隔重复执行circleWidth自增1的操作，当isShow的值为true并且circleWidth的值达到1000时，使用clearInterval方法清除该定时器接口，即可实现扩散播放的效果。

   ```ts
   // 该段代码的核心部分，重复执行circleWidth++，实现画面扩散播放效果
   this.intervalID = setInterval(() => {
     this.circleWidth++;
     if (this.isShow && this.circleWidth === 1000) {
       // 清除该定时器接口
       clearInterval(this.intervalID);
     }
   }, 30);
   ```

完整代码如下所示：

```ts
import { display, window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Diffusion {
  @State circleWidth: number = 0;
  @State clickX: number = 0;
  @State clickY: number = 0;
  @State isShow: boolean = false;
  @State videoSrc: Resource = $rawfile('video.mp4'); // 开发者可在这自定义视频资源
  @State curRate: PlaybackSpeed = PlaybackSpeed.Speed_Forward_1_00_X;
  @State isAutoPlay: boolean = false;
  @State intervalID: number = 0;

  @Builder
  show() {
    Column() {
      Column() {
        Stack() {
          // video组件
          Video({
            previewUri: $r('app.media.img1'), // 开发者可在这自定义图片
            src: this.videoSrc,
            currentProgressRate: this.curRate
          })
            .autoPlay(this.isAutoPlay)
            .height('100%')
            .onClick(() => {
              this.isAutoPlay = false;
              clearInterval(this.intervalID);
              this.isShow = false;
              this.circleWidth = 0;
              this.clickX = 0;
              this.clickY = 0;
            })
            .padding({
              top: 40,
              bottom: 40,
              left: 20,
              right: 20
            });
        };
      }
      .width('10%')
      .height('10%');
    }
    .clip(true)
    // 按指定的形状对当前组件进行裁剪
    .clipShape(new Circle({
      width: this.circleWidth.toString() + '%',
      height: this.circleWidth.toString() + '%'
    })
      .offset({
        x: (45 - this.circleWidth * 0.5 + this.clickX * 10).toString() + '%',
        y: (45 - this.circleWidth * 0.5 + this.clickY * 10).toString() + '%'
      }))
    .height('1000%')
    .width('1000%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center);
  }

  build() {
    Column() {
      Stack() {
        Button('点击播放视频')
          .onClick((event: ClickEvent) => {
            window.getLastWindow(this.getUIContext().getHostContext(),
              (err: BusinessError, windowObj) => {
                if (err.code) {
                  console.error(`Failed to getLastWindow. Code：${err.code}，message：${err.message}`);
                }
                let windowClass = windowObj;
                windowClass.setWindowSystemBarEnable([]); // 隐藏系统导航栏
              });
            this.isShow = true;
            let displayClass = display.getDefaultDisplaySync();
            let width: number = this.getUIContext().px2vp(displayClass.width);
            let height: number = this.getUIContext().px2vp(displayClass.height);
            this.clickX = event.displayX / width;
            this.clickY = event.displayY / height;
            // 该段代码的核心部分，重复执行circleWidth++，实现画面扩散播放效果
            this.intervalID = setInterval(() => {
              this.circleWidth++;
              if (this.isShow && this.circleWidth === 1000) {
                // 清除该定时器接口
                clearInterval(this.intervalID);
              }
            }, 30);
            setTimeout(() => {
              this.isAutoPlay = true;
            }, 1000);
          });
        if (this.isShow) {
          this.show();
        }
      }
      .width('100%')
      .height('100%');
    }
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```

## 总结

通过clipShape和setInterval两个核心方法相互配合使用，实现特殊的视频播放效果。
