---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-23
title: 视频播放时无法通过手势调节音量和亮度
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 视频播放时无法通过手势调节音量和亮度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:78ce78c01516e92f6fc7741ce3755781e9f6d37cab6e8ac917a5a0b4a90b03b7
---

## 问题现象

用户在使用某视频软件时，在播放视频时，无法通过手势的上下滑动来调节当前播放视频的亮度和音量。

用户期望在视频播放界面左侧上下滑动可以调节亮度，在右侧上下滑动可以调节音量。

## 背景知识

* [AVPlayer](../harmonyos-guides/media-kit-intro.md#avplayer)：AVPlayer主要工作是将Audio/Video媒体资源（比如mp4/mp3/mkv/mpeg-ts等）转码为可供渲染的图像和可听见的音频模拟信号，并通过输出设备进行播放。
* [gesture（常规手势绑定方法）](../harmonyos-guides/arkts-gesture-events-binding.md#gesture常规手势绑定方法)：gesture为通用的一种手势绑定方法，可以将手势绑定到对应的组件上。
* [滑动手势（PanGesture）](../harmonyos-guides/arkts-gesture-events-single-gesture.md#滑动手势pangesture)：滑动手势用于触发滑动手势事件，滑动达到最小滑动距离（默认值为5vp）时滑动手势识别成功。

## 问题定位

* 检索代码，在代码中检索视频播放的逻辑代码页面中，是否有绑定手势（关键字：gesture）。如果绑定了手势，在检索该页面是否有绑定拖动手势（关键字：PanGesture）。
* 检索日志，是否有关键字：Pan accepted，如下所示：

  ```shell
  08-07 09:27:11.504   59734-59821   C02805/com.exam...InputKeyFlow  com.examp...eoPlayer  I     [][OnPointerEvent:216] ac: move: 86420
  08-07 09:27:11.813   59734-59734   C03951/com.exam...InputKeyFlow  com.examp...eoPlayer  I     [(100000:100000:scope)] Pan accepted, tag = Stack
  ```

如果日志中不存在，则说明未绑定手势。

## 分析结论

视频播放界面的相关组件未绑定手势，实现通过拖动手势调节音量和亮度。

## 修改建议

在视频播放界面的组件上，如Stack、Column等绑定拖动手势，并实现上下滑动调节音量和亮度，示例代码如下：

1. 构建音量条组件：

   ```ts
   Column() {
     AVVolumePanel({
       volumeLevel: this.volume,
       volumeParameter: {
         position: {
           x: 150,
           y: 300
         }
       }
     })
   }.width('50%')
   ```
2. 通过手势触发音量调节：

   ```ts
   // 手势触发，当在屏幕上下滑动时，触发音量调节
   .gesture(
     PanGesture({ direction: PanDirection.Vertical })
       .onActionUpdate((event: GestureEvent) => {
         console.info('screenHeight: ' + this.screenHeight);
         console.info('offsetY: ' + this.getUIContext().vp2px(event.offsetY));
         let curVolume = this.volume - this.getUIContext().vp2px(event.offsetY) / this.screenHeight;
         curVolume = curVolume;
         console.info('curVolume 1:' + curVolume);
         curVolume = curVolume >= 15.0 ? 15.0 : curVolume;
         console.info('curVolume 2:' + curVolume);
         curVolume = curVolume <= 0.0 ? 0.0 : curVolume;
         console.info('curVolume 3:' + curVolume);
         this.volume = curVolume;
       })
   )
   .backgroundColor(Color.Black)
   .height('90%')
   .width('100%')
   ```

完整示例如下：

```screen
import display from '@ohos.display';
import emitter from '@ohos.events.emitter';
import { common } from '@kit.AbilityKit';
import media from '@ohos.multimedia.media';
import { ComponentUtils, window } from '@kit.ArkUI';
import { AVVolumePanel } from '@kit.AudioKit';

export class Constants {
  /**
   * 100%
   */
  static readonly FULL_PERCENT: string = '100%';
  /**
   * 70%
   */
  static readonly SEVENTY_PERCENT: string = '70%';
  /**
   * Operate state list
   */
  static readonly OPERATE_STATE: Array<string> = ['prepared', 'playing', 'paused', 'completed'];
  /**
   * BufferInfoType list
   */
  static readonly BUFFER_INFO_TYPE: media.BufferingInfoType[] = [
    media.BufferingInfoType.BUFFERING_START,
    media.BufferingInfoType.BUFFERING_END,
    media.BufferingInfoType.BUFFERING_PERCENT,
    media.BufferingInfoType.CACHED_DURATION
  ];
  /**
   * zIndex list
   */
  static readonly Z_INDEX: number[] = [0, 1, 2, 3, 4, 5];
  /**
   * XComponent surface rect
   */
  static readonly SURFACE_WIDTH_AND_HEIGHT: number[] = [1920, 1080];
  /**
   * Delay time
   */
  static readonly DELAY_TIME: number = 100;
  /**
   * Describes the maximum time stamp that the buffer can be paused
   */
  static readonly CUT_OFF_VALUE: number = 600;
}

const PROPORTION = 0.99; // 占屏幕比例
const SURFACE_W = 0.9; // 表面宽比例
const SURFACE_H = 1.78; // 表面高比例
const SET_INTERVAL = 100; // interval间隔时间
const TIME_ONE = 60000;
const TIME_TWO = 1000;

let innerEventFalse: emitter.InnerEvent = {
  eventId: 1,
  priority: emitter.EventPriority.HIGH
};
let innerEventTrue: emitter.InnerEvent = {
  eventId: 2,
  priority: emitter.EventPriority.HIGH
};
let innerEventWH: emitter.InnerEvent = {
  eventId: 3,
  priority: emitter.EventPriority.HIGH
};

@Entry
@Component
struct PanGestureDemo {
  currentBufferTime: number = 0;
  tag: string = 'AVPlayManager';
  private xComponentController: XComponentController = new XComponentController();
  private avPlayer: media.AVPlayer | null = null;
  private surfaceId: string = '';
  private intervalID: number = -1;
  private seekTime: number = -1;
  private context: common.UIAbilityContext | undefined = undefined;

  @State title: Resource = $r('app.string.EntryAbility_label');
  fileName: string = 'video.mp4';
  isSwiping: boolean = false; // 用户滑动过程中
  @State isPaused: boolean = true; // 暂停播放
  @State XComponentFlag: boolean = false;
  speedSelect: number = 0; // 倍速选择
  speedList: Resource[] = [$r('app.string.video_speed_1_0X'), $r('app.string.video_speed_1_25X'), $r('app.string.video_speed_1_75X'), $r('app.string.video_speed_2_0X')];
  @StorageLink('durationTime') durationTime: number = 0; // 视频总时长
  @StorageLink('currentTime') currentTime: number = 0; // 视频当前时间
  @StorageLink('speedName') speedName: Resource = $r('app.string.video_speed_1_0X');
  @StorageLink('speedIndex') speedIndex: number = 0; // 倍速索引
  @State surfaceW: number | null = null;
  @State surfaceH: number | null = null;
  @State percent: number = 0;
  windowWidth: number = 300;
  windowHeight: number = 200;

  isSliderGesture: boolean = false;
  panEndTime: number = 0;
  @State beginX: number = 0;
  private slideWidth: number = 130;
  private screenHeight: number = 0;

  @State volume: number = 0;

  getDurationTime(): number {
    return this.durationTime;
  }

  getCurrentTime(): number {
    return this.currentTime;
  }

  timeConvert(time: number): string {
    let min: number = Math.floor(time / TIME_ONE);
    let second: string = ((time % TIME_ONE) / TIME_TWO).toFixed(0);
    second = second.padStart(2, '0');
    return `${min}:${second}`;
  }

  async msleepAsync(ms: number): Promise<boolean> {
    return new Promise((resolve) => {
      setTimeout(() => {
        resolve(true);
      }, ms);
    });
  }

  async avSetupVideo() {
    // 通过UIAbilityContext的resourceManager成员的getRawFd接口获取媒体资源播放地址。
    // 返回类型为{fd,offset,length},fd为HAP包fd地址，offset为媒体资源偏移量，length为播放长度。
    if (this.context == undefined) { return; }
    let fileDescriptor = await this.context.resourceManager.getRawFd(this.fileName);
    let avFileDescriptor: media.AVFileDescriptor =
      { fd: fileDescriptor.fd, offset: fileDescriptor.offset, length: fileDescriptor.length };

    if (this.avPlayer) {
      console.info(`${this.tag}: init avPlayer release2createNew`);
      this.avPlayer.release();
      await this.msleepAsync(1500);
    }
    // 创建avPlayer实例对象
    this.avPlayer = await media.createAVPlayer();

    // 创建状态机变化回调函数
    await this.setAVPlayerCallback((avPlayer: media.AVPlayer) => {
      this.percent = avPlayer.width / avPlayer.height;
      this.setVideoWH();
      this.durationTime = this.getDurationTime();
      setInterval(() => { // 更新当前时间
        if (!this.isSwiping) {
          this.currentTime = this.getCurrentTime();
        }
      }, SET_INTERVAL);
    });

    // 为fdSrc赋值触发initialized状态机上报
    this.avPlayer.fdSrc = avFileDescriptor;
  }

  avPlay(): void {
    if (this.avPlayer) {
      try {
        this.avPlayer.play();
      } catch (e) {
        console.error(`${this.tag}: avPlay = ${JSON.stringify(e)}`);
      }
    }
  }

  avPause(): void {
    if (this.avPlayer) {
      try {
        this.avPlayer.pause();
        console.info(`${this.tag}: avPause==`);
      } catch (e) {
        console.error(`${this.tag}: avPause== ${JSON.stringify(e)}`);
      }
    }
  }

  async avSeek(seekTime: number): Promise<void> {
    if (this.avPlayer) {
      try {
        console.info(`${this.tag}: videoSeek  seekTime== ${seekTime}`);
        this.avPlayer.seek(seekTime, 2);
        this.currentTime = seekTime;
      } catch (e) {
        console.error(`${this.tag}: videoSeek== ${JSON.stringify(e)}`);
      }
    }
  }

  avSetSpeed(speed: number): void {
    if (this.avPlayer) {
      try {
        this.avPlayer.setSpeed(speed);
        console.info(`${this.tag}: avSetSpeed enum ${speed}`);
      } catch (e) {
        console.error(`${this.tag}: avSetSpeed == ${JSON.stringify(e)}`);
      }
    }
  }

  // 注册avplayer回调函数
  async setAVPlayerCallback(callback: (avPlayer: media.AVPlayer) => void): Promise<void> {
    // seek操作结果回调函数
    if (this.avPlayer == null) {
      console.error(`${this.tag}: avPlayer has not init!`);
      return;
    }
    this.avPlayer.on('seekDone', (seekDoneTime) => {
      console.info(`${this.tag}: setAVPlayerCallback AVPlayer seek succeeded, seek time is ${seekDoneTime}`);
    });
    this.avPlayer.on('speedDone', (speed) => {
      console.info(`${this.tag}: setAVPlayerCallback AVPlayer speedDone, speed is ${speed}`);
    });
    // error回调监听函数,当avPlayer在操作过程中出现错误时调用reset接口触发重置流程
    this.avPlayer.on('error', (err) => {
      console.error(`${this.tag}: setAVPlayerCallback Invoke avPlayer failed ${JSON.stringify(err)}`);
      if (this.avPlayer == null) {
        console.error(`${this.tag}: avPlayer has not init on error`);
        return;
      }
      this.avPlayer.reset();
    });
    // 状态机变化回调函数
    this.avPlayer.on('stateChange', async (state) => {
      if (this.avPlayer == null) {
        console.info(`${this.tag}: avPlayer has not init on state change`);
        return;
      }
      switch (state) {
        case 'idle': // 成功调用reset接口后触发该状态机上报
          console.info(`${this.tag}: setAVPlayerCallback AVPlayer state idle called.`);
          break;
        case 'initialized': // avplayer 设置播放源后触发该状态上报
          console.info(`${this.tag}: setAVPlayerCallback AVPlayer state initialized called.`);
          if (this.surfaceId) {
            this.avPlayer.surfaceId = this.surfaceId; // 设置显示画面，当播放的资源为纯音频时无需设置
            console.info(`${this.tag}: setAVPlayerCallback this.avPlayer.surfaceId = ${this.avPlayer.surfaceId}`);
            this.avPlayer.prepare();
          }
          break;
        case 'prepared': // prepare调用成功后上报该状态机
          console.info(`${this.tag}: setAVPlayerCallback AVPlayer state prepared called.`);
          this.avPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
            if (infoType === Constants.BUFFER_INFO_TYPE[3]) {
              this.currentBufferTime += value / 1000;
            }
            console.info(`${this.tag}: bufferingUpdate called, infoType value: ${infoType}, value:${value}}`);
          });
          this.durationTime = this.avPlayer.duration;
          this.currentTime = this.avPlayer.currentTime;
          this.avPlayer.play(); // 调用播放接口开始播放
          callback(this.avPlayer);
          break;
        case 'playing': // play成功调用后触发该状态机上报
          console.info(`${this.tag}: setAVPlayerCallback AVPlayer state playing called.`);
          if (this.intervalID != -1) {
            clearInterval(this.intervalID);
          }
          this.intervalID = setInterval(() => { // 更新当前时间
            AppStorage.setOrCreate('durationTime', this.durationTime);
            AppStorage.setOrCreate('currentTime', this.currentTime);
          }, 100);
          let eventDataTrue: emitter.EventData = {
            data: {
              'flag': true
            }
          };
          let innerEventTrue: emitter.InnerEvent = {
            eventId: 2,
            priority: emitter.EventPriority.HIGH
          };
          emitter.emit(innerEventTrue, eventDataTrue);
          break;
        case 'completed': // 播放结束后触发该状态机上报
          console.info(`${this.tag}: setAVPlayerCallback AVPlayer state completed called.`);
          let eventDataFalse: emitter.EventData = {
            data: {
              'flag': false
            }
          };
          let innerEvent: emitter.InnerEvent = {
            eventId: 1,
            priority: emitter.EventPriority.HIGH
          };
          emitter.emit(innerEvent, eventDataFalse);
          if (this.intervalID != -1) {
            clearInterval(this.intervalID);
          }
          this.avPlayer.off('bufferingUpdate');
          AppStorage.setOrCreate('currentTime', this.durationTime);
          break;
        case 'released':
          console.info(`${this.tag}: setAVPlayerCallback released called.`);
          break;
        case 'stopped':
          console.info(`${this.tag}: setAVPlayerCallback AVPlayer state stopped called.`);
          break;
        case 'error':
          console.error(`${this.tag}: setAVPlayerCallback AVPlayer state error called.`);
          break;
        case 'paused':
          console.info(`${this.tag}: setAVPlayerCallback AVPlayer state paused called.`);
          break;
        default:
          console.info(`${this.tag}: setAVPlayerCallback AVPlayer state unknown called.`);
          break;
      }
    });
    // 时间上报监听函数
    this.avPlayer.on('timeUpdate', (time: number) => {
      this.currentTime = time;
    });
  }

  aboutToAppear() {
    let windowClass: window.Window | undefined = undefined;
    this.windowWidth = display.getDefaultDisplaySync().width;
    this.windowHeight = display.getDefaultDisplaySync().height;
    this.surfaceW = this.windowWidth * SURFACE_W;
    this.surfaceH = this.surfaceW / SURFACE_H;
    this.isPaused = true;
    this.context = this.getUIContext()?.getHostContext() as common.UIAbilityContext;
    try {
      window.getLastWindow(this.context, (err, data) => {
        if (err) {
          console.error('AVPlayer', `Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
        }
        windowClass = data;
        this.screenHeight = windowClass.getWindowProperties().windowRect.height;
      });
    } catch (exception) {
      console.error('AVPlayer', `Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`);
    }
  }

  aboutToDisappear() {
    if (this.avPlayer == null) {
      console.info(`${this.tag}: avPlayer has not init aboutToDisappear`);
      return;
    }
    this.avPlayer.release((err) => {
      if (err == null) {
        console.info(`${this.tag}: videoRelease release success`);
      } else {
        console.error(`${this.tag}: videoRelease release failed, error message is = ${JSON.stringify(err.message)}`);
      }
    });
    emitter.off(innerEventFalse.eventId);
  }

  onPageHide() {
    this.avPause();
    this.isPaused = false;
  }

  onPageShow() {
    emitter.on(innerEventTrue, (res: emitter.EventData) => {
      if (res.data) {
        this.isPaused = res.data.flag;
        this.XComponentFlag = res.data.flag;
      }
    });
    emitter.on(innerEventFalse, (res: emitter.EventData) => {
      if (res.data) {
        this.isPaused = res.data.flag;
      }
    });
    emitter.on(innerEventWH, (res: emitter.EventData) => {
      if (res.data) {
        this.windowWidth = res.data.width;
        this.windowHeight = res.data.height;
        this.setVideoWH();
      }
    });
  }

  setVideoWH(): void {
    if (this.percent >= 1) { // 横向视频
      this.surfaceW = Math.round(this.windowWidth * PROPORTION);
      this.surfaceH = Math.round(this.surfaceW / this.percent);
    } else { // 纵向视频
      this.surfaceH = Math.round(this.windowHeight * PROPORTION);
      this.surfaceW = Math.round(this.surfaceH * this.percent);
    }
  }

  @Builder
  CoverXComponent() {
    XComponent({
      // 装载视频容器
      id: 'xComponent',
      type: XComponentType.SURFACE,
      controller: this.xComponentController
    })
      .id('VideoView')
      .visibility(this.XComponentFlag ? Visibility.Visible : Visibility.Hidden)
      .onLoad(() => {
        this.surfaceId = this.xComponentController.getXComponentSurfaceId();
        this.avSetupVideo();
      })
      .height(`${this.surfaceH}px`)
      .width(`${this.surfaceW}px`)
  }

  build() {
    Column() {
      Stack() {
        Column() {
          this.CoverXComponent();
        }
        .align(Alignment.TopStart)
        .margin({ top: 80 })
        .id('VideoView')
        .justifyContent(FlexAlign.Center)

        Text()
          .height(`${this.surfaceH}px`)
          .width(`${this.surfaceW}px`)
          .margin({ top: 80 })
          .backgroundColor(Color.Black)
          .opacity($r('app.float.size_zero_five'))
          .visibility(this.isSwiping ? Visibility.Visible : Visibility.Hidden)

        Row() {
          Text(this.timeConvert(this.currentTime))
            .id('currentTime')
            .fontSize($r('app.float.size_24'))
            .opacity($r('app.float.size_1'))
            .fontColor($r('app.color.slider_selected'))
          Text('/' + this.timeConvert(this.durationTime))
            .id('durationTime')
            .fontSize($r('app.float.size_24'))
            .opacity($r('app.float.size_1'))
            .fontColor(Color.White)
        }
        .margin({ top: 80 })
        .visibility(this.isSwiping ? Visibility.Visible : Visibility.Hidden)

        Column() {
          Blank()
          Column() {
            // 进度条
            Row() {
              Row() {
                // 播放、暂停键
                Image(this.isPaused ? $r('app.media.ic_play') : $r('app.media.ic_pause')) // 暂停/播放
                  .id(this.isPaused ? 'pause' : 'play')
                  .width($r('app.float.size_40'))
                  .height($r('app.float.size_40'))
                  .onClick(() => {
                    if (this.isPaused) {
                      this.avPause();
                      this.isPaused = false;
                    } else {
                      this.avPlay();
                      this.isPaused = true;
                    }
                  })
                // 左侧时间
                Text(this.timeConvert(this.currentTime))
                  .id('currentTimeText')
                  .fontColor(Color.White)
                  .textAlign(TextAlign.End)
                  .fontWeight(FontWeight.Regular)
                  .margin({ left: $r('app.float.size_10') })
              }

              // 进度条
              Row() {
                Slider({
                  value: this.currentTime,
                  min: 0,
                  max: this.durationTime,
                  style: SliderStyle.OutSet
                })
                  .id('Slider')
                  .blockColor(Color.White)
                  .trackColor(Color.Gray)
                  .selectedColor($r('app.color.slider_selected'))
                  .showTips(false)
                  .onChange((value: number) => {
                    if (this.seekTime !== value) {
                      this.seekTime = value;
                      this.avSeek(Number.parseInt(value.toFixed(0)));
                    }
                  })
                  .onAreaChange(() => {
                    let componentUtils: ComponentUtils = this.getUIContext().getComponentUtils();
                    let videoSlider = componentUtils.getRectangleById('Slider');
                    this.slideWidth = this.getUIContext().px2vp(videoSlider.size.width);
                    this.beginX = this.getUIContext().px2vp(videoSlider.localOffset.x);
                  })
              }
              .layoutWeight(1)
              Row() {
                // 右侧时间
                Text(this.timeConvert(this.durationTime))
                  .id('durationTimeText')
                  .fontColor(Color.White)
                  .fontWeight(FontWeight.Regular)
              }
            }
            .justifyContent(FlexAlign.Center)
            .padding({ left: $r('app.float.size_25'), right: $r('app.float.size_30') })
            .width('100%')
          }
          .width('100%')
          .justifyContent(FlexAlign.Center)
        }
        .width('100%')
        .height('100%')

        Column() {
          AVVolumePanel({
            volumeLevel: this.volume,
            volumeParameter: {
              position: {
                x: 150,
                y: 300
              }
            }
          })
        }.width('50%')
      }
      // 手势触发，当在屏幕上下滑动时，触发音量调节
      .gesture(
        PanGesture({ direction: PanDirection.Vertical })
          .onActionUpdate((event: GestureEvent) => {
            console.info('screenHeight: ' + this.screenHeight);
            console.info('offsetY: ' + this.getUIContext().vp2px(event.offsetY));
            let curVolume = this.volume - this.getUIContext().vp2px(event.offsetY) / this.screenHeight;
            curVolume = curVolume;
            console.info('curVolume 1:' + curVolume);
            curVolume = curVolume >= 15.0 ? 15.0 : curVolume;
            console.info('curVolume 2:' + curVolume);
            curVolume = curVolume <= 0.0 ? 0.0 : curVolume;
            console.info('curVolume 3:' + curVolume);
            this.volume = curVolume;
          })
      )
      .backgroundColor(Color.Black)
      .height('90%')
      .width('100%')

      Row() {
        Text(this.title)
          .fontSize($r('app.float.size_20'))
          .fontColor(Color.White)
          .opacity($r('app.float.size_zero_six'))
          .fontWeight(FontWeight.Regular)
          .textAlign(TextAlign.Center)
      }
    }.backgroundColor(Color.Black)
    .height('100%')
    .width('100%')
  }
}
```
