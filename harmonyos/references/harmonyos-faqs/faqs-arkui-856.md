---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-856
title: 视频播放界面下拉状态栏时，会误触发音量或亮度调节
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 视频播放界面下拉状态栏时，会误触发音量或亮度调节
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6b24029a214843a87fc9f46cfc85facbee3a44e42a65222389a3c4fd5aa844f5
---

## 问题现象

应用中视频播放时，用户下拉状态栏有一定概率会触发音量或亮度调节功能，体验不好。

## 背景知识

* [gesture](../harmonyos-guides/arkts-gesture-events-binding.md)：通过给各个组件绑定不同的手势事件，并设计事件的响应方式，当手势识别成功时，ArkUI框架将通过事件回调通知组件手势识别的结果。
* [单一手势](../harmonyos-guides/arkts-gesture-events-single-gesture.md)：手势的基本单元，是所有复杂手势的组成部分，包含点击、长按、拖动、捏合、旋转、滑动六种手势。
* [组合手势](../harmonyos-guides/arkts-gesture-events-combined-gestures.md)：组合手势由多种单一手势组合而成，通过在GestureGroup中使用不同的[GestureMode](../harmonyos-references/ts-combined-gestures.md#gesturemode枚举说明)来声明该组合手势的类型，支持[顺序识别](../harmonyos-guides/arkts-gesture-events-combined-gestures.md#顺序识别)、[并行识别](../harmonyos-guides/arkts-gesture-events-combined-gestures.md#并行识别)和[互斥识别](../harmonyos-guides/arkts-gesture-events-combined-gestures.md#互斥识别)三种类型。

## 问题定位

在视频播放界面轻轻滑动时，就会触发音量和亮度调节，判断应用中控制音量和亮度调节的手势事件，使用了单一手势中的滑动手势，在视频播放页面代码中搜索[SwipeGesture](../harmonyos-guides/arkts-gesture-events-single-gesture.md#快滑手势swipegesture)，查看是否使用的单一滑动手势。

## 分析结论

视频播放界面，触发音量和亮度调节功能的手势事件，使用的单一滑动手势，导致用户在下拉状态栏时，容易误触发音量和亮度调节。

## 修改建议

修改触发音量和亮度调节功能的手势事件，改为由长按手势和拖动手势组合而成的顺序识别手势，这样用户需要同时执行长按和拖动手势才能触发音量和亮度调节功能，滑动下拉状态栏时就不会误触发此功能，示例如下。

```screen
import media from '@ohos.multimedia.media';
import { BusinessError } from '@ohos.base';
import { AVVolumePanel } from '@kit.AudioKit';
import { window } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State isFullScreen: boolean = false;
  @State isLandscape: boolean = false;
  @State isVideo: boolean = true;
  @State isOpacity: boolean = false;
  @State isPlay: boolean = false;
  @State currentTime: number = 0;
  @State durationTime: number = 0;
  @State durationStringTime: string = '00:00';
  @State currentStringTime: string = '00:00';
  @State flag: boolean = false;
  @State videoFiles: media.AVFileDescriptor[] = [];
  @State audioFiles: media.AVFileDescriptor[] = [];
  @State sourceFiles: media.AVFileDescriptor[] = [];
  @State currentIndex: number = 0;
  @State volume: number = 0;
  @State visible: boolean = false;
  @State screenBrightness: number = 0;
  @State speed: number = media.PlaybackSpeed.SPEED_FORWARD_1_00_X;
  private avPlayer: media.AVPlayer | undefined = undefined;
  private xComponentController = new XComponentController();
  private surfaceID: string = '';
  private readonly OPERATE_STATE: Array<string> = ['prepared', 'playing', 'paused', 'completed'];
  private screenHeight: number = 0;
  private mainWin?: window.Window;
  private windowStage: window.WindowStage = AppStorage.get('windowStage') as window.WindowStage;

  aboutToAppear(): void {
    try {
      this.mainWin = this.windowStage.getMainWindowSync();
    } catch (err) {
      console.error(`mainWin  failed, err.code:${err.code}, err.message:${err.message}`);
    }

    let windowClass: window.Window | undefined = undefined;
    window.getLastWindow(this.getUIContext().getHostContext()).then((window: window.Window) => {
      windowClass = window;
      this.screenHeight = windowClass.getWindowProperties().windowRect.height;
    }).catch((err: BusinessError) => {
      console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
    });

    // 初始化AVPlayer
    this.createAVPlayer();
    this.reset(true);
  }

  aboutToDisappear(): void {
    if (this.avPlayer) {
      this.avPlayer.off('timeUpdate');
      this.avPlayer.off('seekDone');
      this.avPlayer.off('error');
      this.avPlayer.off('stateChange');
      this.avPlayer.release();
    }
  }

  build() {
    Column() {
      if (!this.isFullScreen) {
        Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceAround }) {
          Column() {
            Text('视频播放')
              .fontColor(this.isVideo ? Color.Blue : Color.Black)
              .fontSize(16)
              .fontWeight(this.isVideo ? 500 : 400)
              .lineHeight(22)
              .margin({ top: 17, bottom: 7 });
            Divider()
              .strokeWidth(2)
              .color('#007DFF')
              .opacity(this.isVideo ? 1 : 0);
          }
          .onClick(() => {
            this.isVideo = true;
            this.reset(true);
          });
        }
        .margin({ bottom: '8vp' });
      }

      Flex({
        direction: FlexDirection.Column,
        justifyContent: this.isFullScreen ? FlexAlign.Center : FlexAlign.Start
      }) {
        if (this.isVideo) {
          this.VideoPlayer();
        }
        if (!this.isFullScreen) {
          this.Buttons();
        }
      }
      .width('100%')
      .height('100%')
      .backgroundColor(this.isFullScreen ? Color.Black : Color.White);
    }
    .width('100%')
    .height('100%');
  }

  @Builder
  Buttons() {
    Column() {
      Scroll() {
        GridRow({
          columns: 2,
          gutter: { x: 5, y: 10 },
          direction: GridRowDirection.Row
        }) {
          GridCol({ span: 1, offset: 0, order: 0 }) {
            Button('播放').width(140).onClick(() => {
              this.play();
            });
          };

          GridCol({ span: 1, offset: 0, order: 0 }) {
            Button('暂停').width(140).onClick(() => {
              this.isPlay = false;
              if (this.avPlayer) {
                this.avPlayer.pause();
              }
            });
          };
        }
        .margin({ bottom: 20, top: 20 })
        .borderRadius(20);
      }
      .scrollBar(BarState.Off);
    };
  }

  @Builder
  VideoPlayer() {
    Stack({
      alignContent: this.isFullScreen ? (this.isLandscape ? Alignment.Bottom : Alignment.Center) : Alignment.Bottom
    }) {
      Stack() {
        if (!this.isPlay) {
          Image($r('app.media.ic_public_play'))
            .width(50)
            .height(50)
            .zIndex(2)
            .onClick(() => {
              this.play();
            });
        }
        Column() {
          XComponent({
            type: XComponentType.TEXTURE,
            controller: this.xComponentController
          })
            .onLoad(() => {
              // 设置Surface宽高（1920*1080）
              let surfaceRect: SurfaceRect = {
                surfaceWidth: 1920,
                surfaceHeight: 1080
              };
              this.xComponentController.setXComponentSurfaceRect(surfaceRect);
              this.surfaceID = this.xComponentController.getXComponentSurfaceId();
            })
            .width('100%')
            .height('100%');

          Row() {
            Column() {
              AVVolumePanel({
                volumeLevel: this.volume,
                volumeParameter: {
                  position: {
                    x: 150,
                    y: 300
                  }
                }
              });
            }
            .width('50%');

            Column() {
              Stack() {
                Slider({
                  value: this.screenBrightness,
                  min: 0,
                  max: 1,
                  step: 0.1,
                  style: SliderStyle.NONE,
                  direction: Axis.Vertical,
                  reverse: true
                })
                  .visibility(this.visible ? Visibility.Visible : Visibility.Hidden)
                  .height(160)
                  .selectedColor(Color.White)
                  .trackColor(Color.Black)
                  .trackThickness(40);
              }
              .margin({
                top: 0,
                right: 0
              })
              .position({ bottom: 150, right: 20 });
            }
            .padding({
              right: 30,
              bottom: 30
            })
            .width('50%');
          }
          .height('50%');
        }
        .zIndex(1)
        .onClick(() => {
          this.playOrPause();
        });
      }
      .width('100%')
      .height(this.isFullScreen ? (this.isLandscape ? '100%' : 260) : '100%')
      .gesture(
        // 声明该组合手势的类型为Sequence类型
        GestureGroup(GestureMode.Sequence,
          // 该组合手势第一个触发的手势为长按手势，且长按手势可多次响应
          LongPressGesture({ repeat: true })
            .onAction((event: GestureEvent | undefined) => {
              if (event) {
                if (event.repeat) {
                }
              }
              console.info('LongPress onAction');
            })
            .onActionEnd(() => {
              console.info('LongPress end');
            }),
          // 当长按之后进行拖动，PanGesture手势被触发
          PanGesture({ direction: PanDirection.Vertical })
            .onActionStart(() => {
            })
            .onActionUpdate((event: GestureEvent) => {
              if (event.fingerList[0].globalX > 200) {
                this.visible = true;
                let curBrightness: number = this.screenBrightness -
                  this.getUIContext().vp2px(event.offsetY) / this.getUIContext().vp2px(this.screenHeight);
                curBrightness = Math.max(0, Math.min(1.0, curBrightness));
                this.screenBrightness = curBrightness;
                console.info(`this brightness is: ${this.screenBrightness}`);
                try {
                  this.mainWin?.setWindowBrightness(this.screenBrightness, (err) => {
                    if (err) {
                      console.error(`Failed to set the brightness. Cause: ${err.message}`);
                      return;
                    }
                    console.info(`Succeeded in setting the brightness.`);
                  });
                } catch (exception) {
                  console.error(`Failed to set the brightness.`);
                }
              } else {
                this.visible = false;
                let curVolume: number = this.volume - this.getUIContext().vp2px(event.offsetY) / this.screenHeight;
                curVolume = curVolume >= 15.0 ? 15.0 : curVolume;
                curVolume = curVolume <= 0.0 ? 0.0 : curVolume;
                this.volume = curVolume;
                console.info(`this volume is: ${this.volume}`);
              }
            })
            .onActionEnd(() => {
              setTimeout(() => {
                this.visible = false;
              }, 3000);
            })
        )
      );
      this.PlayControl();
    }
    .height(this.isFullScreen ? '100%' : 260)
    .backgroundColor(Color.Black)
    .width('100%');
  }

  @Builder
  PlayControl() {
    Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Image(this.isPlay ? $r('app.media.ic_pause') : $r('app.media.ic_play'))
        .width('20vp')
        .height('20vp')
        .onClick(() => {
          this.iconOnclick();
        });
      Text(this.currentStringTime)
        .fontSize('14vp')
        .fontColor(Color.White)
        .margin({ left: '2vp' });
      Slider({
        value: this.currentTime,
        step: 1,
        min: 0,
        max: this.durationTime,
        style: SliderStyle.OutSet
      })
        .blockColor(Color.White)
        .width('50%')
        .trackColor(Color.Gray)
        .selectedColor(Color.White)
        .showSteps(false)
        .showTips(false)
        .trackThickness(this.isOpacity ? 2 : 4);
      Text(this.durationStringTime)
        .fontSize('14vp')
        .fontColor(Color.White)
        .margin({ left: '2vp', right: '2vp' });
    }
    .zIndex(2)
    .padding({ right: '2vp' })
    .opacity(this.isOpacity ? 0.7 : 1)
    .width('100%')
    .offset({ x: 0, y: this.isFullScreen ? (this.isLandscape ? 0 : 110) : 0 })
    .backgroundBlurStyle(BlurStyle.Thin, { colorMode: ThemeColorMode.DARK });
  }

  // 注册avplayer回调函数
  setAVPlayerCallback(avPlayer: media.AVPlayer) {
    avPlayer.on('timeUpdate', (time: number) => {
      console.info(`AVPlayerDemo AVPlayer timeUpdate. time is ${time}`);
      this.currentTime = Math.floor(time * this.durationTime / avPlayer.duration);
      console.info(`AVPlayerDemo this.currentTime. time is ${this.currentTime}`);
      this.currentStringTime = this.secondToTime(Math.floor(time / 1000));
    });

    // seek操作结果回调函数
    avPlayer.on('seekDone', (seekDoneTime: number) => {
      console.info(`AVPlayerDemo AVPlayer seekDone succeeded, seek time is ${seekDoneTime}`);
    });

    // 监听setSpeed生效的事件
    avPlayer.on('speedDone', (speed: number) => {
      console.info(`AVPlayerDemo AVPlayer speedDone succeeded, speed is ${speed}`);
    });

    // error回调监听函数,当avPlayer在操作过程中出现错误时调用 reset接口触发重置流程
    avPlayer.on('error', (err: BusinessError) => {
      console.error(`AVPlayerDemo Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`);
      avPlayer.reset(); // 调用reset重置资源，触发idle状态
    });

    // 状态机变化回调函数
    avPlayer.on('stateChange', async (state: string) => {
      switch (state) {
        case 'idle': // 成功调用reset接口后触发该状态机上报
          console.info('AVPlayerDemo AVPlayer state idle called.');
          if (avPlayer && this.sourceFiles.length > this.currentIndex) {
          }
          break;
        case 'initialized': // avplayer 设置播放源后触发该状态上报
          console.info('AVPlayerDemo AVPlayer state initialized called.');
          this.reset();
          if (this.isVideo) {
            avPlayer.surfaceId = this.surfaceID;
          }
          avPlayer.prepare();
          break;
        case 'prepared': // prepare调用成功后上报该状态机
          console.info('AVPlayerDemo AVPlayer state prepared called.');
          this.flag = true;
          avPlayer.getTrackDescription((error: BusinessError, arrList: Array<media.MediaDescription>) => {
            if ((arrList) != null) {
              console.info('Succeeded in doing getTrackDescription：' + JSON.stringify(arrList));
            } else {
              console.error(`Failed to do getTrackDescription, error:${error}`);
            }
          });
          this.durationTime = Math.floor(avPlayer.duration / 1000);
          this.durationStringTime = this.secondToTime(this.durationTime);
          avPlayer.setSpeed(media.PlaybackSpeed.SPEED_FORWARD_1_00_X);
          avPlayer.seek(1, media.SeekMode.SEEK_PREV_SYNC);
          break;
        case 'completed': // prepare调用成功后上报该状态机
          console.info('AVPlayerDemo AVPlayer state completed called.');
          this.isPlay = false;
          break;
        case 'playing': // play成功调用后触发该状态机上报
          console.info('AVPlayerDemo AVPlayer state playing called.');
          break;
        case 'paused': // pause成功调用后触发该状态机上报
          console.info('AVPlayerDemo AVPlayer state paused called.');
          break;
        case 'stopped': // stop接口成功调用后触发该状态机上报
          console.info('AVPlayerDemo AVPlayer state stopped called.');
          break;
        case 'released':
          console.info('AVPlayerDemo AVPlayer state released called.');
          break;
        default:
          console.info('AVPlayerDemo AVPlayer state unknown called.');
          break;
      }
    });
  }

  reset(sourceFlag?: boolean) {
    this.isPlay = false;
    this.currentTime = 0;
    this.durationTime = 0;
    this.durationStringTime = '00:00';
    this.currentStringTime = '00:00';
    this.flag = false;
    if (sourceFlag) {
      this.currentIndex = 0;
      this.isFullScreen = false;
      if (this.isVideo) {
        this.sourceFiles = this.videoFiles;
      } else {
        this.sourceFiles = this.audioFiles;
      }
      if (this.avPlayer) {
        this.avPlayer.reset();
      }
    }
  }

  async play() {
    if (!this.avPlayer || this.OPERATE_STATE.indexOf(this.avPlayer.state) === -1 ||
      this.OPERATE_STATE.indexOf(this.avPlayer.state) === 1) {
      console.error('AVPlayerDemo play failed. no avPlayer or state is not prepared/paused/completed');
      return;
    }
    this.isPlay = true;
    if (this.avPlayer.state === 'completed') {
      this.currentTime = 0;
      this.currentStringTime = '00:00';
      this.avPlayer.seek(1, media.SeekMode.SEEK_PREV_SYNC);
    }
    this.avPlayer.play();
  }

  iconOnclick() {
    if (this.isPlay === true) {
      this.isPlay = false;
      this.isOpacity = false;
      return;
    }
    if (this.flag === true) {
      this.isPlay = true;
      this.isOpacity = true;
    } else {
      let intervalFlag = setInterval(() => {
        if (this.flag === true) {
          this.isPlay = true;
          this.isOpacity = true;
          clearInterval(intervalFlag);
        }
      }, 100);
    }
  }

  /**
   *时间转换
   */
  secondToTime(seconds: number): string {
    let hourUnit = 60 * 60;
    let hour: number = Math.floor(seconds / hourUnit);
    let minute: number = Math.floor((seconds - hour * hourUnit) / 60);
    let second: number = seconds - hour * hourUnit - minute * 60;
    let hourStr: string = hour < 10 ? `0${hour.toString()}` : `${hour.toString()}`;
    let minuteStr: string = minute < 10 ? `0${minute.toString()}` : `${minute.toString()}`;
    let secondStr: string = second < 10 ? `0${second.toString()}` : `${second.toString()}`;
    if (hour > 0) {
      return `${hourStr}:${minuteStr}:${secondStr}`;
    }
    if (minute > 0) {
      return `${minuteStr}:${secondStr}`;
    } else {
      return `00:${secondStr}`;
    }
  }

  playOrPause() {
    if (this.avPlayer) {
      if (this.isPlay) {
        this.isPlay = false;
        this.avPlayer.pause();
      } else {
        this.play();
      }
    }
  }

  createAVPlayer() {
    media.createAVPlayer().then((video: media.AVPlayer) => {
      if (video != null) {
        this.avPlayer = video;
        this.setAVPlayerCallback(this.avPlayer);
        if (this.avPlayer) {
          // 网络链接根据实际情况替换成用户自己的链接，否则无法正常运行
          this.avPlayer.url = '';
        }
        console.info('AVPlayerDemo createAVPlayer success');
      } else {
        console.error('AVPlayerDemo createAVPlayer fail');
      }
    }).catch((error: BusinessError) => {
      console.error(`AVPlayerDemo AVPlayer catchCallback, error message:${error.message}`);
    });
  }
}
```
