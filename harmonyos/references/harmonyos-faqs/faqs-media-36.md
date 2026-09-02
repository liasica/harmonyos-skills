---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-36
title: AVPlayer播放4KHDR视频时与周围UI样式不协调
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > AVPlayer播放4KHDR视频时与周围UI样式不协调
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3c7f7927acbbf006c77ee61e73533b0bd46863bcdb624b1dd4868b217a532961
---

## 问题现象

使用AVPlayer播放4K的HDR视频时播放器明显变亮，超过周围UI颜色，使周围UI显得暗淡。

## 背景知识

* [AVPlayer](../harmonyos-guides/media-kit-intro.md#avplayer)：功能较完善的音视频播放API，集成了流媒体和本地资源解析，媒体资源解封装，视频解码和渲染功能，适用于对媒体资源进行端到端播放的场景，可直接播放mp4、mkv等格式的视频文件。
* [XComponent](../harmonyos-guides/napi-xcomponent-guidelines.md)：作为一种渲染组件，可用于EGL/OpenGLES和媒体数据写入，通常用于满足开发者较为复杂的自定义渲染需求。
* [XComponentType](../harmonyos-references/ts-appendix-enums.md#xcomponenttype10)：XComponent组件可通过指定type字段来实现不同的渲染方式，分别为XComponentType.SURFACE和XComponentType.TEXTURE。
* [XComponentType.SURFACE](../harmonyos-references/ts-appendix-enums.md#xcomponenttype10)：用于EGL/OpenGLES和媒体数据写入，开发者定制的绘制内容单独展示到屏幕上。
* [XComponentType.TEXTURE](../harmonyos-references/ts-appendix-enums.md#xcomponenttype10)：用于EGL/OpenGLES和媒体数据写入，开发者定制的绘制内容会和XComponent组件的内容合成后展示到屏幕上，保持帧同步，保持在同一帧将图形处理器（GPU）纹理和ArkUI其他的绘制指令统一发给渲染服务。

## 问题定位

根据问题现象，排查应用中XComponent渲染组件的渲染方式，查看XComponentType类型是SURFACE还是TEXTURE。问题代码示例参考如下：

```ts
Column() {
  XComponent({
    type: XComponentType.SURFACE,
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
}
```

## 分析结论

应用中XComponent渲染组件的渲染方式使用的SURFACE类型，该类型支持绘制内容单独展示到屏幕上，但不能和ArkUI的绘制保持帧同步，导致播放器周围UI样式暗淡。

## 修改建议

应用中XComponent渲染组件的渲染方式修改为TEXTURE，保证播放器绘制内容和ArkUI的绘制保持帧同步。

```ts
import media from '@ohos.multimedia.media';
import { BusinessError } from '@ohos.base';

@Entry
@Component
struct Index {
  @State isFullScreen: boolean = false;
  private isLandscape: boolean = false;
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
  private avPlayer: media.AVPlayer | undefined = undefined;
  private xComponentController = new XComponentController();
  private surfaceID: string = '';
  private readonly OPERATE_STATE: Array<string> = ['prepared', 'playing', 'paused', 'completed'];

  aboutToAppear(): void {
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
              .margin({ top: 17, bottom: 7 })
            Divider()
              .strokeWidth(2)
              .color('#007DFF')
              .opacity(this.isVideo ? 1 : 0)
          }
          .onClick(() => {
            this.isVideo = true;
            this.reset(true);
          })
        }
        .margin({ bottom: '8vp' })
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
      .backgroundColor(this.isFullScreen ? Color.Black : Color.White)
    }
    .width('100%')
    .height('100%')
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
          }
          GridCol({ span: 1, offset: 0, order: 0 }) {
            Button('暂停').width(140).onClick(() => {
              this.isPlay = false;
              if (this.avPlayer) {
                this.avPlayer.pause();
              }
            });
          }
        }
        .margin({ bottom: 20, top: 20 })
        .borderRadius(20)
      }
      .scrollBar(BarState.Off)
    }
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
        }
        .zIndex(1)
        .onClick(() => {
          this.playOrPause();
        })
      }
      .width('100%')
      .height(this.isFullScreen ? (this.isLandscape ? '100%' : 260) : '100%')
      this.PlayControl();
    }
    .height(this.isFullScreen ? '100%' : 260)
    .backgroundColor(Color.Black)
    .width('100%')
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
        .margin({ left: '2vp' })
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
        .trackThickness(this.isOpacity ? 2 : 4)
      Text(this.durationStringTime)
        .fontSize('14vp')
        .fontColor(Color.White)
        .margin({ left: '2vp', right: '2vp' })
    }
    .zIndex(2)
    .padding({ right: '2vp' })
    .opacity(this.isOpacity ? 0.7 : 1)
    .width('100%')
    .offset({ x: 0, y: this.isFullScreen ? (this.isLandscape ? 0 : 110) : 0 })
    .backgroundBlurStyle(BlurStyle.Thin, { colorMode: ThemeColorMode.DARK })
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
              console.info('Succeeded in doing getTrackDescription：'+JSON.stringify(arrList));
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
    if (!this.avPlayer || this.OPERATE_STATE.indexOf(this.avPlayer.state) === -1 || this.OPERATE_STATE.indexOf(this.avPlayer.state) === 1) {
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
