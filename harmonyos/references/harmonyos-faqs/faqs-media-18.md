---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-18
title: 音频切出页面重新进入无法播放
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 音频切出页面重新进入无法播放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a34990d0e19966f2f3060e7cd9dd94ec967a1e85baf468c191b36833d8ae2cac
---

## 问题现象

应用首页内点击某一个音频作品，应用跳转进该音频作品页面，同时开始播放音频，点击返回按钮到首页后，音频停止播放，再次点击该音频作品，应用跳转进音频作品页面后，不再播放音频。

## 背景知识

* [AVPlayer](../harmonyos-guides/media-kit-intro.md#avplayer)：支持将Audio/Video媒体资源（比如mp4/mp3/mkv/mpeg-ts等）转码为可供渲染的图像和可听见的音频模拟信号，并通过输出设备进行播放。
* [aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)：组件生命周期函数，即用@Component装饰的自定义组件的生命周期，在创建自定义组件的新实例后回调该接口，只会回调一次该接口。
* [aboutToDisappear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttodisappear)：组件生命周期函数，即用@Component装饰的自定义组件的生命周期，在自定义组件析构销毁时回调该接口，只会回调一次该接口。

## 问题定位

根据问题现象初次进入音频作品页面，音频可以正常播放，判断此时应用使用的AVPlayer播放器状态正常，而在返回首页后再次进入音频页面，音频无法播放，判断此时AVPlayer播放器状态异常导致无法播放，通过以下步骤逐步定位：

1. 应用中尝试搜索[createAVPlayer](../harmonyos-references/arkts-apis-media-f.md#mediacreateavplayer9)，查看应用创建AVPlayer实例的时机，是否在aboutToAppear函数中创建的AVPlayer实例，而aboutToAppear函数只会在组件创建时调用一次。
2. 应用中尝试搜索AVPlayer实例的[release](../harmonyos-references/arkts-apis-media-avplayer.md#release9)销毁接口，查看应用什么时机销毁的AVPlayer播放器的实例，是否在aboutToDisappear函数中销毁的AVPlayer实例，该函数会在组件销毁时调用一次。
3. 应用中尝试排查音频页面流程，查看其是否有创建AVPlayer实例的代码。

## 分析结论

1. 应用中AVPlayer实例是在首页的aboutToAppear函数中创建的，应用首页在组件创建时调用了该函数，AVPlayer实例成功创建，所以第一次进入音频作品页面时，音频正常播放。
2. 应用返回到首页，子页面销毁时在aboutToDisappear函数中调用release，销毁了AVPlayer实例。
3. 应用再次进入音频作品页面，流程中并没有重新创建AVPlayer实例，导致音频播放失败。

## 修改建议

将应用中创建AVPlayer实例的代码，从首页的aboutToAppear函数中，调整到音频播放页的aboutToAppear函数中，这样在退出页面销毁AVPlayer实例后，再次进入音频播放页面后可以重新创建AVPlayer实例，保证音频的正常播放，示例如下：

```screen
async aboutToAppear() {
  this.windowWidth = display.getDefaultDisplaySync().width;
  this.windowHeight = display.getDefaultDisplaySync().height;
  this.surfaceW = this.windowWidth * SURFACE_W;
  this.surfaceH = this.surfaceW / SURFACE_H;
  this.context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  // 通过UIAbilityContext的resourceManager成员的getRawFd接口获取媒体资源播放地址。
  if (this.context === undefined) {
    return;
  }
  // this.fileName需根据应用实际情况配置对应的资源，否则会导致程序无法正常运行
  let fileDescriptorVideo = await this.context.resourceManager.getRawFd(this.fileName);
  let avFileDescriptor: media.AVFileDescriptor =
    { fd: fileDescriptorVideo.fd, offset: fileDescriptorVideo.offset, length: fileDescriptorVideo.length };

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
  });
  // 为fdSrc赋值触发initialized状态机上报
  this.avPlayer.fdSrc = avFileDescriptor;
}
```

完整示例如下：

1. 工程配置文件module.json5中配置{"routerMap": "$profile:route\_map"}。

   ```screen
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
       "routerMap": "$profile:route_map",
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
2. 在工程resources/base/profile中创建route\_map.json文件，添加如下配置信息。

   ```screen
   {
     "routerMap": [
       {
         "name": "PageOne",
         "pageSourceFile": "src/main/ets/pages/PageOne.ets",
         "buildFunction": "PageOneBuilder",
         "data": {
           "description" : "this is PageOne"
         }
       }
     ]
   }
   ```
3. 应用首页，点击子页面音频会跳转到音频播放子页面。

   ```screen
   @Entry
   @Component
   struct Index {
     pathStack: NavPathStack = new NavPathStack();

     build() {
       Navigation(this.pathStack) {
         Row() {
           Column() {
             Text('首页')
               .fontSize(50)
               .fontWeight(FontWeight.Bold);
             // 添加按钮，以响应用户onClick事件
             Button() {
               Text('子页面音频')
                 .fontSize(20)
                 .fontWeight(FontWeight.Bold);
             }
             .type(ButtonType.Capsule)
             .margin({
               top: 50
             })
             .backgroundColor('#0D9FFB')
             .width('40%')
             .height('5%')
             .onClick(() => {
               this.pathStack.pushPathByName('PageOne', null);
             });
           }
           .width('100%');
         }
         .height('100%');
       }
       .title('Navigation')
       .mode(NavigationMode.Stack);
     }
   }
   ```
4. 音频播放页面在组件初始化aboutToAppear中创建AVPlayer实例，播放音频，返回首页时在aboutToDisappear函数中调用release，销毁了AVPlayer实例，后续再次进入会重新创建AVPlayer实例并播放音频。

   ```screen
   import display from '@ohos.display';
   import { common } from '@kit.AbilityKit';
   import media from '@ohos.multimedia.media';
   import { fileIo } from '@kit.CoreFileKit';

   const PROPORTION = 0.99; // 占屏幕比例
   const SURFACE_W = 0.9; // 表面宽比例
   const SURFACE_H = 1.78; // 表面高比例

   @Builder
   export function PageOneBuilder() {
     PageOne();
   }

   @Component
   struct PageOne {
     pathStack: NavPathStack = new NavPathStack();
     tag: string = 'AVPlayManager';
     private xComponentController: XComponentController = new XComponentController();
     private avPlayer: media.AVPlayer | null = null;
     private subFile: fileIo.File | null = null;
     private surfaceId: string = '';
     private intervalID: number = -1;
     private context: common.UIAbilityContext | undefined = undefined;
     private fileName: string = '3463094780.mp3'; // 资源需替换成用户自己的资源，否则无法成功运行
     private isSwiping: boolean = false; // 用户滑动过程中
     private xComponentFlag: boolean = false;
     @State surfaceW: number | null = null;
     @State surfaceH: number | null = null;
     private percent: number = 0;
     private windowWidth: number = 300;
     private windowHeight: number = 200;

     async msleepAsync(ms: number): Promise<boolean> {
       return new Promise((resolve) => {
         setTimeout(() => {
           resolve(true);
         }, ms);
       });
     }

     async avSetupVideoAndSubtitle() {
       // 通过UIAbilityContext的resourceManager成员的getRawFd接口获取媒体资源播放地址。
       if (this.context === undefined) {
         return;
       }
       // this.fileName需根据应用实际情况配置对应的资源，否则会导致程序无法正常运行
       let fileDescriptorVideo = await this.context.resourceManager.getRawFd(this.fileName);
       let avFileDescriptor: media.AVFileDescriptor =
         { fd: fileDescriptorVideo.fd, offset: fileDescriptorVideo.offset, length: fileDescriptorVideo.length };

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
           case 'initialized': // avplayer设置播放源后触发该状态上报
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
               console.info(`${this.tag}: bufferingUpdate called, infoType value: ${infoType}, value:${value}}`);
             });
             this.avPlayer.play(); // 调用播放接口开始播放
             callback(this.avPlayer);
             break;
           case 'playing': // play成功调用后触发该状态机上报
             console.info(`${this.tag}: setAVPlayerCallback AVPlayer state playing called.`);
             if (this.intervalID !== -1) {
               clearInterval(this.intervalID);
             }
             break;
           case 'completed': // 播放结束后触发该状态机上报
             console.info(`${this.tag}: setAVPlayerCallback AVPlayer state completed called.`);
             if (this.intervalID !== -1) {
               clearInterval(this.intervalID);
             }
             this.avPlayer.off('bufferingUpdate');
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
     }

     async aboutToAppear() {
       this.windowWidth = display.getDefaultDisplaySync().width;
       this.windowHeight = display.getDefaultDisplaySync().height;
       this.surfaceW = this.windowWidth * SURFACE_W;
       this.surfaceH = this.surfaceW / SURFACE_H;
       this.context = this.getUIContext().getHostContext() as common.UIAbilityContext;
       // 通过UIAbilityContext的resourceManager成员的getRawFd接口获取媒体资源播放地址。
       if (this.context === undefined) {
         return;
       }
       // this.fileName需根据应用实际情况配置对应的资源，否则会导致程序无法正常运行
       let fileDescriptorVideo = await this.context.resourceManager.getRawFd(this.fileName);
       let avFileDescriptor: media.AVFileDescriptor =
         { fd: fileDescriptorVideo.fd, offset: fileDescriptorVideo.offset, length: fileDescriptorVideo.length };

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
       });
       // 为fdSrc赋值触发initialized状态机上报
       this.avPlayer.fdSrc = avFileDescriptor;
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
       if (this.subFile) {
         try {
           fileIo.closeSync(this.subFile);
         } catch (err) {
           console.error(`failed to close subtitle file, ${JSON.stringify(err)}`);
         }
       }
     }

     onPageShow(): void {
       console.info(`Succeeded in clicking the 'Next' button.`);
     }

     onPageHide() {
       this.avPause();
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
         })
         .height(`${this.surfaceH}px`)
         .width(`${this.surfaceW}px`);
     }

     build() {
       NavDestination() {
         Column() {
           Row() {
             Button() {
               Text('返回首页')
                 .fontSize(30)
                 .fontWeight(FontWeight.Bold);
             }
             .type(ButtonType.Capsule)
             .margin({
               top: 20
             })
             .backgroundColor('#0D9FFB')
             .width('40%')
             .height('5%')
             .onClick(() => {
               this.pathStack.clear();
             });
           };

           Stack() {
             Column() {
               this.CoverXComponent();
             }
             .align(Alignment.TopStart)
             .margin({ top: 80 })
             .id('VideoView')
             .justifyContent(FlexAlign.Center);

             Text()
               .height(`${this.surfaceH}px`)
               .width(`${this.surfaceW}px`)
               .margin({ top: 80 })
               .backgroundColor(Color.Black)
               .visibility(this.isSwiping ? Visibility.Visible : Visibility.Hidden);
           }
           .backgroundColor(Color.Black)
           .height('90%')
           .width('100%');

         }.backgroundColor(Color.Black)
         .height('100%')
         .width('100%');
       }.title('PageOne')
       .onReady((context: NavDestinationContext) => {
         this.pathStack = context.pathStack;
       });
     }
   }
   ```
