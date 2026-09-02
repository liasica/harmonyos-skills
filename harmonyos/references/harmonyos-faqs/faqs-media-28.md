---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-28
title: 如何解决AVPlayer在List组件中无法实现全屏播放问题
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 如何解决AVPlayer在List组件中无法实现全屏播放问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:1b3322b60cd61b229e5e1bf14e6390221fe8fafaa289726116728381d63c1fba
---

## 问题现象

在List组件中，AVPlayer播放器作为ListItem的子元素，视频播放无法全屏显示。

## 背景知识

* [使用AVPlayer播放视频(ArkTS)](../harmonyos-guides/video-playback.md)：实现端到端播放原始媒体资源。
* [窗口沉浸式能力](../cangjie-guides/cj-application-window-stage.md#体验窗口沉浸式能力)：在看视频、玩游戏等场景下，隐藏状态栏、导航栏等不必要的系统窗口，从而获得更佳的沉浸式体验。
* [setPreferredOrientation](../harmonyos-references/arkts-apis-window-window.md#setpreferredorientation9)：设置主窗口的方向。

## 解决方案

AVPlayer只是把Surface画布绑定到AVPlayer上，不提供旋转、全屏接口，这些都要应用自己操作Surface全屏、旋转来实现，AVPlayer只是一个不带界面的播放器。所以实现全屏需要通过操作Surface实现全屏、旋转。

在点击全屏按钮时，隐藏其它ListItem，仅显示选中项；点击横屏按钮时，设置窗口方向，并设置XComponent组件宽高铺满屏幕，实现全屏播放效果。

1. 初始化视频列表数据源，示例代码如下：

   ```ts
   private data: MyVideoSourceDate = new MyVideoSourceDate([]);

   aboutToAppear(): void {
     let list: VideoSource[] = [
       new VideoSource('videoTest1', 'videoTest1.mp4'),
       new VideoSource('videoTest2', 'videoTest2.mp4'),
       new VideoSource('videoTest3', 'videoTest3.mp4'),
       new VideoSource('videoTest4', 'videoTest4.mp4')
     ];
     this.data = new MyVideoSourceDate(list);
   }
   ```
2. List + LazyForEach组件渲染视频列表，以及添加全屏、退出全屏、横屏等按钮，示例代码如下：

   ```ts
   build() {
     // 通过显隐控制控制其他listItem是否展示
     Column() {
       Text(this.item.text)
         .visibility(this.isLayoutFullScreen === false ? Visibility.Visible : Visibility.None)
       Stack() {
         XComponent({ id: 'video_player_id', type: XComponentType.SURFACE, controller: this.mXComponentController })
           .onLoad(() => {
             this.player = new AVPlayerDemo();
             this.player.setSurfaceID(this.mXComponentController.getXComponentSurfaceId());
           })
           .height(this.isLayoutFullScreen ? (this.isLandScape ? '100%' : 200) : '100%')
         // 视频按钮布局
         Flex() {
           Button(this.player && (this.player.getStage() === 'playing') ? '播放中' : '开始')
             .onClick(async () => {
               if (isPlaying.length !== 0) {
                 let play = isPlaying.pop();
                 await play?.release();
               }
               if (this.player) {
                 this.player.avPlayerLiveDemo(0, this.item.url,
                   this.getUIContext().getHostContext() as Context as common.UIAbilityContext);
                 isPlaying.push(this.player);
               }
             })
             .backgroundColor(this.bkColor)
           Button('点击全屏')
             .onClick(() => {
               this.fangDaIndex = this.index;
               this.isLayoutFullScreen = true;
               this.setFullScreen(this.isLayoutFullScreen);
             })
             .backgroundColor(this.bkColor)

           Button('退出全屏')
             .onClick(() => {
               this.setR(1);
               this.isLayoutFullScreen = false;
               this.isLandScape = false;
               this.setFullScreen(this.isLayoutFullScreen);
             })
             .backgroundColor(this.bkColor)

           Button('横屏')
             .onClick(() => {
               this.fangDaIndex = this.index;
               this.setR(2);
               this.isLandScape = true;
               this.isLayoutFullScreen = true;
               this.setFullScreen(this.isLayoutFullScreen);
             })
             .backgroundColor(this.bkColor)

           Button('退出横屏')
             .onClick(() => {
               this.setR(1);
               this.isLandScape = false;
             })
             .backgroundColor(this.bkColor)
         }
       }
       .backgroundColor(Color.Black)
       .height(this.isLayoutFullScreen ? '100%' : 200)
     }
     .onVisibleAreaChange([0.2, 1.0], async (isVisible: boolean, currentRatio: number) => {
       if (!isVisible && currentRatio < 0.2) {
         if (this.player && isPlaying.length !== 0 && this.player === isPlaying[0]) {
           console.info('onVisibleAreaChange');
           this.player.release();
           isPlaying[0].release();
           isPlaying.pop();
         }
       }
     })
     .width('100%')
   }
   ```
3. 窗口方向（横屏）、窗口沉浸式设置，示例代码如下：

   ```ts
   // 设置窗口方向
   setR(orientation: number) {
     window.getLastWindow(this.getUIContext().getHostContext()).then((win) => {
       if (orientation === 1) {
         win.disableLandscapeMultiWindow();
       } else if (orientation === 2) {
         win.enableLandscapeMultiWindow();
       }
       win.setPreferredOrientation(orientation).then(() => {
         console.info('setWindowOrientation Succeeded.');
       }).catch(() => {
         console.info('setWindowOrientation: Failed.');
       });
     }).catch(() => {
       console.info('setWindowOrientation： Failed to obtain the top window.');
     });
   }

   // 设置沉浸式窗口
   setFullScreen(isLayoutFullScreen: boolean) {
     window.getLastWindow(this.getUIContext().getHostContext()).then((win) => {
       win.setWindowLayoutFullScreen(isLayoutFullScreen);
     }).catch(() => {
       console.info('setWindowOrientation： Failed to obtain the top window.');
     });
   }
   ```
4. 在module.json5配置文件中abilities标签下的preferMultiWindowOrientation属性增加“landscape\_auto”，示例代码如下：

   ```json
   {
     "module": {
       "name": "entry",
       "type": "entry",
       "description": "$string:module_desc",
       "mainElement": "EntryAbility",
       "deviceTypes": [
         "phone"
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
           "preferMultiWindowOrientation": "landscape_auto",
           "exported": true,
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

完整示例代码如下：

XCAvplayer.ets：

```ts
import { MyVideoSourceDate, VideoSource } from './MyVideoSourceData';
import { VideoComponent } from './VideoComponent';

@Entry
@Component
struct XCAvplayer {
  @State isLayoutFullScreen: boolean = false;
  @State fangDaIndex: number = -1;
  private data: MyVideoSourceDate = new MyVideoSourceDate([]);

  aboutToAppear(): void {
    let list: VideoSource[] = [
      new VideoSource('videoTest1', 'videoTest1.mp4'),
      new VideoSource('videoTest2', 'videoTest2.mp4'),
      new VideoSource('videoTest3', 'videoTest3.mp4'),
      new VideoSource('videoTest4', 'videoTest4.mp4')
    ];
    this.data = new MyVideoSourceDate(list);
  }

  build() {
    Scroll() {
      Column() {
        List() {
          LazyForEach(this.data, (item: VideoSource, index: number) => {
            ListItem() {
              VideoComponent({
                item: item,
                isLayoutFullScreen: this.isLayoutFullScreen,
                index: index,
                fangDaIndex: this.fangDaIndex
              })
                .visibility(this.isLayoutFullScreen && this.fangDaIndex !== index ? Visibility.None :
                  Visibility.Visible)
            }
          }, (item: string) => item)
        }
        .cachedCount(5)
        .scrollBar(BarState.Off)
        .edgeEffect(this.isLayoutFullScreen ? EdgeEffect.None : EdgeEffect.Spring)
      }
    }
    .edgeEffect(this.isLayoutFullScreen ? EdgeEffect.None : EdgeEffect.Spring)
    .width('100%')
  }
}
```

VideoComponent.ets：

```ts
import window from '@ohos.window';
import { AVPlayerDemo } from './AVPlayerDemo';
import { VideoSource } from './MyVideoSourceData';
import { common } from '@kit.AbilityKit';

let isPlaying: AVPlayerDemo[] = [];

@Component
export struct VideoComponent {
  @ObjectLink item: VideoSource;
  index: number = -1;
  @Link isLayoutFullScreen: boolean;
  @Link fangDaIndex: number;
  bkColor: string = '#0A59F7';
  mXComponentController: XComponentController = new XComponentController();
  @State isLandScape: boolean = false;
  player?: AVPlayerDemo;

  // 设置窗口方向
  setR(orientation: number) {
    window.getLastWindow(this.getUIContext().getHostContext()).then((win) => {
      if (orientation === 1) {
        win.disableLandscapeMultiWindow();
      } else if (orientation === 2) {
        win.enableLandscapeMultiWindow();
      }
      win.setPreferredOrientation(orientation).then(() => {
        console.info('setWindowOrientation Succeeded.');
      }).catch(() => {
        console.info('setWindowOrientation: Failed.');
      });
    }).catch(() => {
      console.info('setWindowOrientation： Failed to obtain the top window.');
    });
  }

  // 设置沉浸式窗口
  setFullScreen(isLayoutFullScreen: boolean) {
    window.getLastWindow(this.getUIContext().getHostContext()).then((win) => {
      win.setWindowLayoutFullScreen(isLayoutFullScreen);
    }).catch(() => {
      console.info('setWindowOrientation： Failed to obtain the top window.');
    });
  }

  build() {
    // 通过显隐控制控制其他listItem是否展示
    Column() {
      Text(this.item.text)
        .visibility(this.isLayoutFullScreen === false ? Visibility.Visible : Visibility.None)
      Stack() {
        XComponent({ id: 'video_player_id', type: XComponentType.SURFACE, controller: this.mXComponentController })
          .onLoad(() => {
            this.player = new AVPlayerDemo();
            this.player.setSurfaceID(this.mXComponentController.getXComponentSurfaceId());
          })
          .height(this.isLayoutFullScreen ? (this.isLandScape ? '100%' : 200) : '100%')
        // 视频按钮布局
        Flex() {
          Button(this.player && (this.player.getStage() === 'playing') ? '播放中' : '开始')
            .onClick(async () => {
              if (isPlaying.length !== 0) {
                let play = isPlaying.pop();
                await play?.release();
              }
              if (this.player) {
                this.player.avPlayerLiveDemo(0, this.item.url,
                  this.getUIContext().getHostContext() as Context as common.UIAbilityContext);
                isPlaying.push(this.player);
              }
            })
            .backgroundColor(this.bkColor)
          Button('点击全屏')
            .onClick(() => {
              this.fangDaIndex = this.index;
              this.isLayoutFullScreen = true;
              this.setFullScreen(this.isLayoutFullScreen);
            })
            .backgroundColor(this.bkColor)

          Button('退出全屏')
            .onClick(() => {
              this.setR(1);
              this.isLayoutFullScreen = false;
              this.isLandScape = false;
              this.setFullScreen(this.isLayoutFullScreen);
            })
            .backgroundColor(this.bkColor)

          Button('横屏')
            .onClick(() => {
              this.fangDaIndex = this.index;
              this.setR(2);
              this.isLandScape = true;
              this.isLayoutFullScreen = true;
              this.setFullScreen(this.isLayoutFullScreen);
            })
            .backgroundColor(this.bkColor)

          Button('退出横屏')
            .onClick(() => {
              this.setR(1);
              this.isLandScape = false;
            })
            .backgroundColor(this.bkColor)
        }
      }
      .backgroundColor(Color.Black)
      .height(this.isLayoutFullScreen ? '100%' : 200)
    }
    .onVisibleAreaChange([0.2, 1.0], async (isVisible: boolean, currentRatio: number) => {
      if (!isVisible && currentRatio < 0.2) {
        if (this.player && isPlaying.length !== 0 && this.player === isPlaying[0]) {
          console.info('onVisibleAreaChange');
          this.player.release();
          isPlaying[0].release();
          isPlaying.pop();
        }
      }
    })
    .width('100%')
  }
}
```

MyVideoSourceData.ets：

```ts
export class MyVideoSourceDate implements IDataSource {
  videoList: VideoSource[] = [];

  constructor(videoList: VideoSource[]) {
    this.videoList = videoList;
  }

  totalCount(): number {
    return this.videoList.length;
  }

  getData(index: number): VideoSource {
    return this.videoList[index];
  }

  registerDataChangeListener(): void {
  }

  unregisterDataChangeListener(): void {
  }
}

@Observed
export class VideoSource {
  text: string;
  url: string;

  constructor(text: string, url: string) {
    this.text = text;
    this.url = url;
  }
}
```

AVPlayerDemo.ets：

```ts
import media from '@ohos.multimedia.media';
import { BusinessError } from '@ohos.base';
import { common } from '@kit.AbilityKit';

export class AVPlayerDemo {
  private count: number = 0;
  private surfaceID: string = ''; // surfaceID用于播放画面显示，具体的值需要通过Xcomponent接口获取，相关文档链接见上面Xcomponent创建方法。
  private avPlayer: media.AVPlayer | undefined = undefined;

  setSurfaceID(surfaceId: string) {
    this.surfaceID = surfaceId;
  }

  // 注册avplayer回调函数。
  setAVPlayerCallback(avPlayer: media.AVPlayer) {
    // seek操作结果回调函数。
    avPlayer.on('seekDone', (seekDoneTime: number) => {
      console.info(`AVPlayer seek succeeded, seek time is ${seekDoneTime}`);
    });
    // error回调监听函数，当avplayer在操作过程中出现错误时，调用reset接口触发重置流程。
    avPlayer.on('error', (err: BusinessError) => {
      console.error(`Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`);
      avPlayer.reset();
    });
    // 状态机变化回调函数。
    avPlayer.on('stateChange', async (state: string) => {
      switch (state) {
        case 'idle': // 成功调用reset接口后触发该状态机上报。
          console.info('AVPlayer state idle called.');
          avPlayer.release(); // 调用release接口销毁实例对象。
          break;
        case 'initialized': // avplayer设置播放源后触发该状态上报。
          console.info('AVPlayer state initialized called.');
          avPlayer.surfaceId = this.surfaceID; // 设置显示画面，当播放的资源为纯音频时无需设置。
          avPlayer.prepare();
          break;
        case 'prepared': // prepared调用成功后上报该状态机。
          avPlayer.play();
          break;
        case 'playing': // play成功调用后触发该状态机上报。
          break;
        case 'paused': // pause成功调用后触发该状态机上报。
          break;
        case 'completed': // 播放接口后触发该状态机上报。
          avPlayer.play(); // 调用播放接口接口。
          break;
        case 'stopped': // stop接口后触发该状态机上报。
          avPlayer.reset(); // 调用reset接口初始化avplayer状态。
          break;
        case 'released': // 播放接口后触发该状态机上报。
          break;
        default:
          break;
      }
    });
  }

  // 通过url设置网络地址来实现播放直播码流。
  async avPlayerLiveDemo(count: number, url: string, context: common.UIAbilityContext) {
    this.count = count;
    // 创建avPlayer实例对象
    this.avPlayer = await media.createAVPlayer();
    // 创建状态机变化回调函数。
    this.setAVPlayerCallback(this.avPlayer);
    let fileDescriptor = await context.resourceManager.getRawFd(url);
    let avFileDescriptor: media.AVFileDescriptor =
      { fd: fileDescriptor.fd, offset: fileDescriptor.offset, length: fileDescriptor.length };
    this.avPlayer.fdSrc = avFileDescriptor;
  }

  async release() {
    this.avPlayer?.reset();
  }

  getStage(): string {
    if (this.avPlayer !== undefined) {
      return this.avPlayer.state;
    }
    return 'undefined';
  }
}
```

## 总结

AVPlayer可以自定义全屏效果，当需要在List组件中实现AVPlayer全屏播放效果时，可以通过隐藏其它组件，设置窗口横屏、沉浸式，并且使XComponent组件铺满全屏，从而达到全屏播放的效果。
