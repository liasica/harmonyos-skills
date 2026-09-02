---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-29
title: 应用从后台切换至前台，播放音频无声音
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 应用从后台切换至前台，播放音频无声音
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2dc0875ad9fe9d369e72b3f65b1f1e96dfbc8e2dba429f74a6ee60c44cb71728
---

## 问题现象

首次打开应用可以正常播放音频，将应用切换到后台后再切换至前台，点击播放音频按钮无声音。

## 背景知识

* [AVPlayer](../harmonyos-guides/using-avplayer-for-playback.md)：AVPlayer主要工作是将视频、音频媒体资源转码为可供渲染的图像和可听见的音频模拟信号，并通过输出设备进行播放。
* AVPlayerState：AVPlayerState是AVPlayer的状态机，包含以下几个状态：
  + idle：闲置状态。
  + initialized：资源初始化。
  + prepared：已准备状态。
  + playing：正在播放状态。
  + paused：暂停状态。
  + completed：播放至结尾状态。
  + stopped：停止状态。
  + released：销毁状态。
  + error：错误状态。
* 当播放处于prepared/playing/paused/completed状态时，播放引擎处于工作状态，这需要占用系统较多的运行内存。当客户端暂时不使用播放器时，调用[reset](../harmonyos-references/arkts-apis-media-avplayer.md#reset9)或[release](../harmonyos-references/arkts-apis-media-avplayer.md#release9)回收内存资源，做好资源利用。
* Media错误码[5400102](../harmonyos-references/errorcode-media.md#section5400102-当前状态不支持此操作)：当前状态机不支持此操作。

## 问题定位

1. 在日志中查找错误码“5400102”，找到相关错误信息：

   ```txt
   OnErrorCb:errorCode 5400102, errorMsg Operate Not Permit: current state is not prepared/playing/paused/completed, unsupport speed operation
   ```

   日志表示当前AVPlayer组件状态不处于工作状态（prepared、playing、paused或completed），却执行了更改播放速度的操作，当前状态不允许执行该操作，导致播放失败。
2. 将应用从前台切换到后台，输出日志：“AVPlayer state released called.”，说明AVPlayer组件被销毁，状态变更为released。查看切换到后台时的设置，退到后台后销毁AVPlayer组件，且返回到前台时未重新使AVPlayer组件处于工作状态，导致播放失败。

   ```typescript
   onPageHide() {
     // 应用退到后台后销毁该组件
     this.avPlayer.release((err) => {
       if (err == null) {
         console.info(`${this.tag}: videoRelease release success`);
       }
     });
   }

   onPageShow() {
     // AVPlayer组件未处于工作状态
   }
   ```

## 分析结论

应用退到后台后销毁AVPlayer组件，且返回到前台时未重新使AVPlayer组件处于工作状态，导致播放失败。

## 修改建议

返回到前台时重新启动AVPlayer组件，使组件处于工作状态。

```ts
import display from '@ohos.display';
import emitter from '@ohos.events.emitter';
import { common } from '@kit.AbilityKit';
import media from '@ohos.multimedia.media';
import { window } from '@kit.ArkUI';

const PROPORTION = 0.99; // 占屏幕比例
const SURFACE_W = 0.9; // 表面宽比例
const SURFACE_H = 1.78; // 表面高比例
const SET_INTERVAL = 100; // interval间隔时间
const TIME_ONE = 60000;
const TIME_TWO = 1000;
const SPEED_ZERO = 0;
const SPEED_ONE = 1;
const SPEED_TWO = 2;
const SPEED_THREE = 3;
const SPEED_COUNT = 4;
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
struct ChangeStatus {
  tag: string = 'AVPlayManager';
  private xComponentController: XComponentController = new XComponentController();
  private avPlayer: media.AVPlayer | null = null;
  private surfaceId: string = '';
  private intervalID: number = -1;
  private seekTime: number = -1;
  private context: common.UIAbilityContext | undefined = undefined;
  private count: number = 0;
  private lastTime: number = 0;
  fileName: string = 'test_01.mp3'; // 'test_01.mp3'需要在src/main/resources/rawfile中替换为开发者需要的音频文件
  isSwiping: boolean = false; // 用户滑动过程中
  @State isPlay: boolean = false; // 暂停播放
  @State xComponentFlag: boolean = false;
  @State speedSelect: number = 0; // 倍速选择
  speedList: string[] = ['1.0X', '1.25X', '1.75X', '2.0X'];
  @StorageLink('durationTime') durationTime: number = 0; // 视频总时长
  @StorageLink('currentTime') currentTime: number = 0; // 视频当前时间
  @StorageLink('speedName') speedName: string = '1.0X';
  @StorageLink('speedIndex') speedIndex: number = 0; // 倍速索引
  surfaceW: number | null = null;
  surfaceH: number | null = null;
  percent: number = 0;
  windowWidth: number = 300;
  windowHeight: number = 200;

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

  async avSetupAudio() {
    // 通过UIAbilityContext的resourceManager成员的getRawFd接口获取媒体资源播放地址。
    // 返回类型为{fd,offset,length},fd为HAP包fd地址，offset为媒体资源偏移量，length为播放长度。
    if (this.context === undefined) {
      return;
    }
    let fileDescriptor = await this.context.resourceManager.getRawFd(this.fileName);
    let avFileDescriptor: media.AVFileDescriptor =
      { fd: fileDescriptor.fd, offset: fileDescriptor.offset, length: fileDescriptor.length };

    if (!this.avPlayer) {
      // 创建avPlayer实例对象
      this.avPlayer = await media.createAVPlayer();
    }
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
      this.avPlayer.play();
    }
  }

  avPause(): void {
    if (this.avPlayer) {
      this.avPlayer.pause();
    }
  }

  async avSeek(seekTime: number): Promise<void> {
    if (this.avPlayer) {
      this.avPlayer.seek(seekTime, 2);
      this.currentTime = seekTime;
    }
  }

  avSetSpeed(speed: number): void {
    if (this.avPlayer) {
      this.avPlayer.setSpeed(speed);
    }
  }

  // 注册avplayer回调函数
  async setAVPlayerCallback(callback: (avPlayer: media.AVPlayer) => void): Promise<void> {
    // seek操作结果回调函数
    if (this.avPlayer == null) {
      return;
    }
    // error回调监听函数,当avPlayer在操作过程中出现错误时调用reset接口触发重置流程
    this.avPlayer.on('error', () => {
      if (this.avPlayer == null) {
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
          break;
        case 'initialized': // avplayer设置播放源后触发该状态上报
          if (this.surfaceId) {
            this.avPlayer.surfaceId = this.surfaceId; // 设置显示画面，当播放的资源为纯音频时无需设置
            this.avPlayer.prepare();
          }
          break;
        case 'prepared': // prepare调用成功后上报该状态机
          console.info(`${this.tag}: setAVPlayerCallback AVPlayer state prepared called.`);
          this.avPlayer.on('bufferingUpdate', (infoType: media.BufferingInfoType, value: number) => {
            console.info(`${this.tag}: bufferingUpdate called, infoType value: ${infoType}, value:${value}}`);
          });
          this.durationTime = this.avPlayer.duration;
          this.currentTime = this.avPlayer.currentTime;
          this.avPlayer.pause();
          console.info(`${this.tag}:
            setAVPlayerCallback speedSelect: ${this.speedSelect}, duration: ${this.durationTime}`);
          if (this.speedSelect !== -1) {
            switch (this.speedSelect) {
              case SPEED_ZERO:
                this.avSetSpeed(media.PlaybackSpeed.SPEED_FORWARD_1_00_X);
                break;
              case SPEED_ONE:
                this.avSetSpeed(media.PlaybackSpeed.SPEED_FORWARD_1_25_X);
                break;
              case SPEED_TWO:
                this.avSetSpeed(media.PlaybackSpeed.SPEED_FORWARD_1_75_X);
                break;
              case SPEED_THREE:
                this.avSetSpeed(media.PlaybackSpeed.SPEED_FORWARD_2_00_X);
                break;
            }
          }
          callback(this.avPlayer);
          break;
        case 'playing': // play成功调用后触发该状态机上报
          console.info(`${this.tag}: setAVPlayerCallback AVPlayer state playing called.`);
          if (this.count !== 0) {
            if (this.intervalID !== -1) {
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
          }
          this.count++;
          break;
        case 'completed': // 播放结束后触发该状态机上报
          this.avPlayer.off('bufferingUpdate');
          this.isPlay = false; // 改变播放状态
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
    this.windowWidth = display.getDefaultDisplaySync().width;
    this.windowHeight = display.getDefaultDisplaySync().height;
    this.surfaceW = this.windowWidth * SURFACE_W;
    this.surfaceH = this.surfaceW / SURFACE_H;
    this.isPlay = false;
    this.context = this.getUIContext().getHostContext() as common.UIAbilityContext;
    window.getLastWindow(this.context).then((lastWindow) => {
      lastWindow.setWindowLayoutFullScreen(true);
      let systemBarProperties: window.SystemBarProperties = {
        statusBarColor: '#00000000',
        statusBarContentColor: '#ffffff'
      };
      lastWindow.setWindowSystemBarProperties(systemBarProperties);
    });
  }

  aboutToDisappear() {
    if (this.avPlayer === null) {
      console.info(`${this.tag}: avPlayer has not init aboutToDisappear`);
      return;
    }
    this.avPlayer.release((err) => {
      if (err === null) {
        console.info(`${this.tag}: videoRelease release success`);
      }
    });
    emitter.off(innerEventFalse.eventId);
  }

  onPageHide() {
    this.lastTime = this.currentTime;
    // 应用退到后台后销毁该组件
    this.avPlayer?.release((err) => {
      if (err === null) {
        console.info(`${this.tag}: videoRelease release success`);
      }
    });
    this.avPlayer = null;
    this.isPlay = false;
  }

  onPageShow() {
    if (this.surfaceId.length !== 0) {
      this.avSetupAudio(); // 设置AVPlayer组件处于工作状态
      // 恢复到上次播放的位置
      setTimeout(() => {
        this.avPlayer?.seek(this.lastTime);
      }, 100);
    }
    emitter.on(innerEventTrue, (res: emitter.EventData) => {
      if (res.data) {
        this.isPlay = res.data.flag;
        this.xComponentFlag = res.data.flag;
      }
    });
    emitter.on(innerEventFalse, (res: emitter.EventData) => {
      if (res.data) {
        this.isPlay = res.data.flag;
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
      .visibility(this.xComponentFlag ? Visibility.Visible : Visibility.Hidden)
      .onLoad(() => {
        this.surfaceId = this.xComponentController.getXComponentSurfaceId();
        this.avSetupAudio();
      })
      .height(`${this.surfaceH}px`)
      .width(`${this.surfaceW}px`);
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
        .justifyContent(FlexAlign.Center);

        Column() {
          Blank();
          Column() {
            // 进度条
            Row() {
              Row() {
                // $r("app.media.ic_pause")和$r("app.media.ic_play"))需要替换为开发者需要的图片资源文件
                Image(this.isPlay ? $r('app.media.ic_pause') : $r('app.media.ic_play')) // 暂停/播放
                  .width(40)
                  .height(40)
                  .onClick(() => {
                    if (this.isPlay) {
                      this.avPause();
                      this.isPlay = false;
                    } else {
                      this.avPlay();
                      this.isPlay = true;
                    }
                  });
                // 左侧时间
                Text(this.timeConvert(this.currentTime))
                  .id('currentTimeText')
                  .fontColor(Color.White)
                  .textAlign(TextAlign.End)
                  .fontWeight(FontWeight.Regular)
                  .margin({ left: 10 });
              };

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
                  .selectedColor('#007DFF')
                  .showTips(false)
                  .onChange((value: number) => {
                    if (this.seekTime !== value) {
                      this.seekTime = value;
                      this.avSeek(Number.parseInt(value.toFixed(0)));
                    }
                  });
              }
              .layoutWeight(1);

              Row() {
                // 右侧时间
                Text(this.timeConvert(this.durationTime))
                  .id('durationTimeText')
                  .fontColor(Color.White)
                  .fontWeight(FontWeight.Regular);

                // 倍速按钮
                Button(this.speedName, { type: ButtonType.Normal })
                  .border({ width: 1, color: Color.White })
                  .width(75)
                  .height(40)
                  .fontSize(15)
                  .borderRadius(24)
                  .fontColor(Color.White)
                  .backgroundColor(Color.Black)
                  .margin({ left: 10 })
                  .id('Speed')
                  .onClick(() => {
                    this.speedIndex = (this.speedIndex + 1) % SPEED_COUNT;
                    this.speedSelect = this.speedIndex;
                    this.speedName = this.speedList[this.speedIndex];
                    if (!this.avPlayer) {
                      return;
                    }
                    switch (this.speedSelect) {
                      case 0:
                        this.avSetSpeed(media.PlaybackSpeed.SPEED_FORWARD_1_00_X);
                        break;
                      case 1:
                        this.avSetSpeed(media.PlaybackSpeed.SPEED_FORWARD_1_25_X);
                        break;
                      case 2:
                        this.avSetSpeed(media.PlaybackSpeed.SPEED_FORWARD_1_75_X);
                        break;
                      case 3:
                        this.avSetSpeed(media.PlaybackSpeed.SPEED_FORWARD_2_00_X);
                        break;
                    }
                  });
              };
            }
            .justifyContent(FlexAlign.Center)
            .padding({ left: 25, right: 30 })
            .width('100%');
          }
          .width('100%')
          .justifyContent(FlexAlign.Center);
        }
        .width('100%')
        .height('100%');
      }
      .backgroundColor(Color.Black)
      .height('90%')
      .width('100%');

    }.backgroundColor(Color.Black)
    .height('100%')
    .width('100%');
  }
}
```
