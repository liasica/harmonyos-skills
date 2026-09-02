---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-654
title: 实现横屏分栏模式下视频全屏播放
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现横屏分栏模式下视频全屏播放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:25+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:4cc25a605c6640e1a64a7a5f97bce472e8d6e3dd2cc993bf916bb1699274f059
---

## 问题现象

平板在横屏分栏模式下，利用XComponent设置宽高100%只能实现当前页面全屏，无法实现整个页面全屏，如何解决？

## 背景知识

* [Navigation组件](../harmonyos-references/ts-basic-components-navigation.md)的分栏模式由[mode](../harmonyos-references/ts-basic-components-navigation.md#mode9)属性控制，包括单栏（Stack）、分栏（Split）和自适应（Auto）三个属性。当为折叠屏或平板时，默认分栏显示，在折叠状态或普通手机时可为单栏显示。
* [XComponent组件](../harmonyos-guides/napi-xcomponent-guidelines.md)可以结合[AVPlayer](../harmonyos-guides/video-playback.md)播放视频，通过设置XComponent宽高100%以及窗口沉浸式即可实现视频全屏播放。

## 解决方案

1. 利用Navigation的[navBarWidth](../harmonyos-references/ts-basic-components-navigation.md#navbarwidth9)属性来控制横屏模式下导航栏的宽度。

   ```screen
   Navigation(this.navPathStack) {
     Column() {
       VideoComponent({ source: this.source });
       Button('跳转SubPage')
         .margin({ top: 20 })
         .onClick(() => {
           this.navPathStack.pushPath({ name: 'SubPage' });
         });
     }
     .width('100%')
     .height('100%');
   }
   // 先判断是否是分栏模式，如果不是则代表需要全屏，可根据来源区分是哪个页面全屏
   .navBarWidth(this.isSplit ? '40%' : this.source === 'Index' ? '100%' : '0.00001%')
   .hideToolBar(true)
   .hideTitleBar(true)
   .height('100%')
   .width('100%');
   ```
2. 利用Button按钮点击来设置是否全屏以及页面来源。

   ```screen
   Row() {
     Button('Source=' + this.source).width(200);
     Button('全屏').width(100)
       .onClick(() => {
         this.xh = '100%';
         this.setFullScreen(true);
         AppStorage.set('isSplit', false);
         AppStorage.set('source', this.source);
       });
     Button('退出全屏').width(100)
       .onClick(() => {
         this.xh = '80%';
         this.setFullScreen(false);
         AppStorage.set('isSplit', true);
       });
   };
   ```

完整示例参考如下：

1. 在EntryAbility里面声明MainPage，MainPage主页面代码如下：

   ```screen
   import { VideoComponent } from './VideoComponent';

   @Entry
   @Component
   struct MainPage {
     navPathStack: NavPathStack = new NavPathStack();
     @StorageLink('isSplit') isSplit: boolean = true;
     @StorageLink('source') source: string = 'Index';

     aboutToAppear(): void {
       AppStorage.set('isSplit', true);
       AppStorage.set('source', 'Index');
     }

     build() {
       Navigation(this.navPathStack) {
         Column() {
           VideoComponent({ source: this.source });
           Button('跳转SubPage')
             .margin({ top: 20 })
             .onClick(() => {
               this.navPathStack.pushPath({ name: 'SubPage' });
             });
         }
         .width('100%')
         .height('100%');
       }
       // 先判断是否是分栏模式，如果不是则代表需要全屏，可根据来源区分是哪个页面全屏
       .navBarWidth(this.isSplit ? '40%' : this.source === 'Index' ? '100%' : '0.00001%')
       .hideToolBar(true)
       .hideTitleBar(true)
       .height('100%')
       .width('100%');
     }
   }
   ```
2. SubPage子页面：

   ```screen
   import { VideoComponent } from './VideoComponent';

   @Component
   struct SubPage {
     navPathStack: NavPathStack = new NavPathStack();
     @StorageLink('isSplit') isSplit: boolean = true;
     @StorageLink('source') source: string = 'SubPage';

     aboutToAppear(): void {
       AppStorage.set('source', 'SubPage');
     }

     build() {
       NavDestination() {
         Column() {
           VideoComponent({ source: this.source });
           Button('跳转主页')
             .margin({ top: 20 })
             .onClick(() => {
               this.navPathStack.clear();
             });
         }
         .height('100%')
         .width('100%');
       }.onReady((ctx: NavDestinationContext) => {
         this.navPathStack = ctx.pathStack;
       })
       .height('100%')
       .width('100%');
     }
   }

   @Builder
   export function SubPageBuilder() {
     SubPage();
   }
   ```
3. VideoComponent播放器页面：

   ```screen
   import { media } from '@kit.MediaKit';
   import { common } from '@kit.AbilityKit';
   import { window } from '@kit.ArkUI';
   import { resourceManager } from '@kit.LocalizationKit';

   class AVPlayerManager {
     private avPlayer?: media.AVPlayer;
     private surfaceId: string = '';
     private context: Context;

     constructor(context: Context) {
       this.context = context;
     }

     async init() {
       try {
         this.avPlayer = await media.createAVPlayer();
       } catch (err) {
         console.error(`create avplayer failed: ${err}`);
         return;
       }
       this.setEventListening();
     }

     setSurfaceId(surfaceId: string) {
       this.surfaceId = surfaceId;
     }

     async setMediaAssetRF(fileName: string) {
       if (this.avPlayer === undefined) {
         console.error(`set media asset, avplayer is undefined`);
         return;
       }
       let resourceMgr: resourceManager.ResourceManager = this.context.resourceManager;
       let videoFD: resourceManager.RawFileDescriptor | undefined = undefined;
       try {
         videoFD = await resourceMgr.getRawFd(fileName);
       } catch (err) {
         console.error(`get raw file description failed: ${err}}`);
         return;
       }
       let avFD: media.AVFileDescriptor = {
         fd: videoFD.fd,
         offset: videoFD.offset,
         length: videoFD.length,
       };
       this.avPlayer.fdSrc = avFD;
     }

     async release() {
       if (this.avPlayer !== undefined) {
         try {
           await this.avPlayer.release();
           this.avPlayer = undefined;
         } catch (err) {
           console.error(`failed to invoke avplayer release, error is ${err}`);
         }
       }
     }

     private setEventListening() {
       this.avPlayer?.on('stateChange', async (state: media.AVPlayerState) => {
         console.info(`AVPlayer state change to ${state}`);
         if (this.avPlayer === undefined) {
           console.error('AVPlayer is undefined when state change');
           return;
         }
         switch (state) {
           case 'idle':
             break;
           case 'initialized':
             this.avPlayer.surfaceId = this.surfaceId;
             try {
               await this.avPlayer.prepare();
             } catch (err) {
               console.error(`failed to invoke avplayer prepare, error is ${err}`);
             }
             break;
           case 'prepared':
             try {
               let trackList = await this.avPlayer.getTrackDescription();
               console.info(`Tracks Info: ${JSON.stringify(trackList)}`);
               await this.avPlayer.play();
             } catch (err) {
               console.error(`failed to invoke avplayer play, error is ${err}`);
             }
             break;
           case 'playing':
             break;
           case 'completed':
             await this.release();
             break;
           case 'paused':
             break;
           case 'stopped':
             break;
           case 'released':
             break;
           case 'error':
             await this.release();
             break;
           default:
             console.info(`AVPlayer change to unknown state: ${state}`);
             break;
         }
       });
     };
   }

   @Component
   export struct VideoComponent {
     // 区分页面来源
     source: string = '';
     xComponentController: XComponentController = new XComponentController();
     private avPlayerMgr?: AVPlayerManager;
     @State xh: string = '80%';

     build() {
       Stack({ alignContent: Alignment.BottomEnd }) {
         XComponent({
           type: XComponentType.SURFACE,
           controller: this.xComponentController
         })
           .width('100%')
           .height(this.xh)
           .onLoad(async () => {
             let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
             this.avPlayerMgr = new AVPlayerManager(context);
             await this.avPlayerMgr.init();
             this.avPlayerMgr!.setSurfaceId(this.xComponentController.getXComponentSurfaceId());
             this.avPlayerMgr!.setMediaAssetRF('video.mp4');
           })
           .align(Alignment.TopStart);

         Row() {
           Button('Source=' + this.source).width(200);
           Button('全屏').width(100)
             .onClick(() => {
               this.xh = '100%';
               this.setFullScreen(true);
               AppStorage.set('isSplit', false);
               AppStorage.set('source', this.source);
             });
           Button('退出全屏').width(100)
             .onClick(() => {
               this.xh = '80%';
               this.setFullScreen(false);
               AppStorage.set('isSplit', true);
             });
         };
       };
     }

     // 设置沉浸式窗口
     setFullScreen(isLayoutFullScreen: boolean) {
       window.getLastWindow(this.getUIContext().getHostContext()).then((win) => {
         win.setWindowLayoutFullScreen(isLayoutFullScreen);
       }).catch((err: string) => {
         console.info(`setWindowOrientation： Failed to obtain the top window. Cause: ${JSON.stringify(err)}`);
       });
     }
   }
   ```
4. 在src/main目录下的module.json5配置文件中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下：

   ```screen
   {
     "routerMap": [
       {
         "name": "SubPage",
         "pageSourceFile": "src/main/ets/pages/SubPage.ets",
         "buildFunction": "SubPageBuilder",
         "data": {
           "description": "this is SubPage"
         }
       }
     ]
   }
   ```
