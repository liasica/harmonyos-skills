---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-11
title: 平板全屏播放视频时四周有留白
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板全屏播放视频时四周有留白
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2681b7be8e37488df21ebbd73d58e08dd60ec491249249c570f8bad4fac706e4
---

## 问题现象

平板上横屏状态，应用全屏播放视频时，四周有空白边距，视频播放画面未充满屏幕。

## 背景知识

* [display](../harmonyos-references/js-apis-display.md)：屏幕属性提供管理设备屏幕的一些基础能力，例如获取显示设备的相关信息，应用可以根据对应的屏幕信息、屏幕状态变化、屏幕折叠状态等适配不同的UI界面显示。
* [on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)：方法可以监听窗口尺寸大小变化，获取到窗口最新尺寸。
* [setWindowLayoutFullScreen(true)](../harmonyos-references/arkts-apis-window-window.md#setwindowlayoutfullscreen9)：设置窗口为全屏模式，页面布局会拓展到顶部状态栏和底部导航栏。
* [RenderFit](../harmonyos-references/ts-appendix-enums.md#renderfit10)：表示宽高动画过程中组件内容的填充方式，可以控制视频画面的填充。

## 问题定位

1. 应用中排查display.getDefaultDisplaySync或者windowSizeChange方法，确定应用有无监听屏幕尺寸的变化，并对布局进行调整。
2. 应用中排查视频全屏播放时，有无通过setWindowLayoutFullScreen设置窗口为全屏模式。
3. 排查视频播放组件是否设置了RenderFit属性，对视频画面填充方式进行了设置。

## 分析结论

应用未调用display或者on('windowSizeChange')方法监听屏幕尺寸变化，对视频播放组件的布局进行调整，未设置RenderFit属性来控制视频画面的填充方式，导致应用视频未能全屏播放，四周出现留白的问题。

## 修改建议

1. module.json5配置文件中[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)下orientation设置为auto\_rotation，随传感器旋转，在设备横竖屏切换时，窗口会随之旋转，示例如下：

   ```ts
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "description": "$string:module_desc",
       "mainElement": "EntryAbility",
       "deviceTypes": [
         "phone",
         "tablet",
         "2in1"
       ],
       "deliveryWithInstall": true,
       "installationFree": false,
       "pages": "$profile:main_pages",
       "abilities": [
         {
           "name": "EntryAbility",
           "srcEntry": "./ets/entryability/EntryAbility.ets",
           "description": "$string:EntryAbility_desc",
           "icon": "$media:layered_image",
           "label": "$string:EntryAbility_label",
           "startWindowIcon": "$media:startIcon",
           "startWindowBackground": "$color:start_window_background",
           "exported": true,
           "orientation": "auto_rotation",
           "skills": [
             {
               "entities": [
                 "entity.system.home"
               ],
               "actions": [
                 "ohos.want.action.home"
               ]
             }
           ]
         }
       ],
       "requestPermissions": [
         {
           "name": "ohos.permission.INTERNET"
         }
       ],
       "extensionAbilities": [
         {
           "name": "EntryBackupAbility",
           "srcEntry": "./ets/entrybackupability/EntryBackupAbility.ets",
           "type": "backup",
           "exported": false,
           "metadata": [
             {
               "name": "ohos.extension.backup",
               "resource": "$profile:backup_config"
             }
           ],
         }
       ]
     }
   }
   ```
2. 通过display.getDefaultDisplaySync或者windowSizeChange方法监听屏幕最新的尺寸变化，对视频播放界面的布局进行调整，示例如下：

   ```ts
   // 监听窗口尺寸变化
   this.windowClass.on('windowSizeChange', (data) => {
     console.info(`AVPlayerDemo Succeeded in enabling the listener for window size changes. Data:${data}`);
     let orientation = display.getDefaultDisplaySync().orientation;
     // 横屏
     if (orientation == display.Orientation.LANDSCAPE || orientation == display.Orientation.LANDSCAPE_INVERTED) {
       this.isLandscape = true;
     }
     // 竖屏
     if (orientation == display.Orientation.PORTRAIT || orientation == display.Orientation.PORTRAIT_INVERTED) {
       this.isLandscape = false;
     }
   });
   ```
3. 视频全屏播放时，通过setWindowLayoutFullScreen设置窗口为全屏模式，示例如下：

   ```ts
   setWindowLayOut() {
     // 监听全屏事件，设置沉浸式窗口
     this.windowClass.setWindowLayoutFullScreen(this.isFullScreen);
   }
   ```
4. 视频播放组件设置RenderFit属性，对视频画面填充方式进行设置，避免四周有大量留白，示例如下：

   ```ts
   XComponent({
     type: XComponentType.SURFACE,
     controller: this.xComponentController
   })
     .onLoad(() => {
       this.surfaceID = this.xComponentController.getXComponentSurfaceId();
     })
     .width('100%')
     .height('100%')
     .renderFit(RenderFit.RESIZE_CONTAIN);
   ```

完整示例如下：

```ts
import media from '@ohos.multimedia.media';
import { BusinessError } from '@ohos.base';
import { display } from '@kit.ArkUI';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  @Watch('setWindowLayOut') @State isFullScreen: boolean = false;
  @State isLandscape: boolean = false;
  @State isVideo: boolean = true;
  @State isPlay: boolean = false;
  @State flag: boolean = false;
  @State videoFiles: media.AVFileDescriptor[] = [];
  @State audioFiles: media.AVFileDescriptor[] = [];
  @State sourceFiles: media.AVFileDescriptor[] = [];
  @State currentIndex: number = 0;
  private avPlayer: media.AVPlayer | undefined = undefined;
  private xComponentController = new XComponentController();
  private surfaceID: string = '';
  private readonly OPERATE_STATE: Array<string> = ['prepared', 'playing', 'paused', 'completed'];
  context = this.getUIContext();
  uiAbilityContext = this.context.getHostContext() as common.UIAbilityContext;
  private windowClass = this.uiAbilityContext.windowStage.getMainWindowSync();

  setWindowLayOut() {
    // 监听全屏事件，设置沉浸式窗口
    this.windowClass.setWindowLayoutFullScreen(this.isFullScreen);
  }

  aboutToAppear(): void {
    // 初始化AVPlayer
    this.createAVPlayer();
    this.reset(true);
    try {
      // 监听窗口尺寸变化
      this.windowClass.on('windowSizeChange', (data) => {
        console.info(`AVPlayerDemo Succeeded in enabling the listener for window size changes. Data:${data}`);
        let orientation = display.getDefaultDisplaySync().orientation;
        // 横屏
        if (orientation == display.Orientation.LANDSCAPE || orientation == display.Orientation.LANDSCAPE_INVERTED) {
          this.isLandscape = true;
        }
        // 竖屏
        if (orientation == display.Orientation.PORTRAIT || orientation == display.Orientation.PORTRAIT_INVERTED) {
          this.isLandscape = false;
        }
      });
    } catch (exception) {
      console.error(`AVPlayerDemo Failed to enable the listener for window size changes. Cause:${exception}`);
    }
  }

  aboutToDisappear(): void {
    if (this.avPlayer) {
      this.avPlayer.off('error');
      this.avPlayer.off('stateChange');
      this.avPlayer.release();
    }
    try {
      this.windowClass.off('windowSizeChange');
    } catch (exception) {
      console.error(`AVPlayerDemo Failed to disable the listener for window size changes. Cause:${exception}`);
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

          GridCol({ span: 1, offset: 0, order: 0 }) {
            Button('进入全屏').width(140).onClick(() => {
              this.isFullScreen = true;
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
          // $r('app.media.startIcon')指向资源文件，缺失该文件会编译报错，用户根据自身需求，自行替换。
          Image($r('app.media.startIcon'))
            .width(50)
            .height(50)
            .zIndex(2)
            .onClick(() => {
              this.play();
            });
        }
        Column() {
          XComponent({
            type: XComponentType.SURFACE,
            controller: this.xComponentController
          })
            .onLoad(() => {
              this.surfaceID = this.xComponentController.getXComponentSurfaceId();
            })
            .width('100%')
            .height('100%')
            .renderFit(RenderFit.RESIZE_CONTAIN);
        }
        .zIndex(1)
        .onClick(() => {
          this.playOrPause();
        });
      }
      .width('100%')
      .height(this.isFullScreen ? (this.isLandscape ? '100%' : 260) : '100%');
    }
    .height(this.isFullScreen ? '100%' : 260)
    .backgroundColor(Color.Black)
    .width('100%');
  }

  // 注册avplayer回调函数
  setAVPlayerCallback(avPlayer: media.AVPlayer) {
    avPlayer.on('timeUpdate', (time: number) => {
      console.info(`AVPlayerDemo AVPlayer timeUpdate. time is ${time}`);
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
      this.avPlayer.seek(1, media.SeekMode.SEEK_PREV_SYNC);
    }
    this.avPlayer.play();
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
          this.avPlayer.url = 'XXXX';
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
