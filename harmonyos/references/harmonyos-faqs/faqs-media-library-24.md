---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-library-24
title: AVPlayer播放相册中的视频
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 媒体文件管理（Media Library） > AVPlayer播放相册中的视频
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:31+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:d9915d952ae6656ef211b20abc9e8faf74406e3498d6ab3120872c12b8594ea3
---

## 问题现象

如何使用AVPlayer播放用户从系统图库中选择的视频文件。

## 背景知识

* [AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)：AVPlayer可将音视频媒体资源转码为可供渲染的图像和可听见的音频模拟信号，并通过输出设备进行播放。AVPlayer提供功能完善一体化播放能力，应用只需要提供流媒体来源，不负责数据解析和解码就可以达成播放效果。
* [PhotoViewPicker](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md)：PhotoViewPicker用于拉起系统图库，供用户选择媒体库中的图片/视频，返回对应的只读媒体文件uri。

## 解决方案

1. 创建PhotoViewPicker实例，调用[PhotoViewPicker.select](../harmonyos-references/arkts-apis-photoaccesshelper-photoviewpicker.md#select)接口拉起系统图库界面供用户选择需要播放的视频文件，用户选择完成后，返回图库视频文件的uri。
2. 使用[fileIo.openSync](../harmonyos-references/js-apis-file-fs.md#fileioopensync)接口，通过返回的uri以只读方式打开视频文件，得到文件描述符fd。拼接得到字符串fd://${fd}，用于设置AVPlayer的uri，播放系统图库中的视频。

   参考代码如下：

   ```ts
   import { photoAccessHelper } from '@kit.MediaLibraryKit';
   import { BusinessError } from '@kit.BasicServicesKit';
   import { fileIo } from '@kit.CoreFileKit';
   import { media } from '@kit.MediaKit';

   class AVPlayerManager {
     private avPlayer?: media.AVPlayer;
     private surfaceId: string = '';

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

     async getTrack() {
       if (this.avPlayer === undefined) {
         console.error(`get audio track while avplayer is undefined`);
         return;
       }
       let tracks = await this.avPlayer.getTrackDescription();
       console.info(`Video Track: ${JSON.stringify(tracks)}`);
     }

     async setMediaAsset(filePath: string) {
       if (this.avPlayer === undefined) {
         console.error(`set media asset, avplayer is undefined`);
         return;
       }
       let videoFd = -1;
       try {
         let videoFile = fileIo.openSync(filePath, fileIo.OpenMode.READ_ONLY);
         videoFd = videoFile.fd;
       } catch (err) {
         console.error(`failed to open file: ${filePath}`);
         return;
       }
       this.avPlayer.url = `fd://${videoFd}`;
     }

     async release() {
       if (this.avPlayer !== undefined) {
         await this.avPlayer.release();
         this.avPlayer = undefined;
       }
     }

     private setEventListening() {
       this.avPlayer?.on('error', async (err: BusinessError) => {
         console.error(`AVPlayer error: ${JSON.stringify(err)}`);
         await this.avPlayer?.reset();
       });
       this.avPlayer?.on('stateChange', async (state: media.AVPlayerState) => {
         console.info(`AVPlayer state change to ${state}`);
         if (this.avPlayer === undefined) {
           console.error('AVPlayer is undefined when state change');
           return;
         }
         // AVPlayer状态机
         switch (state) {
           case 'idle':
             break;
           case 'initialized':
             this.avPlayer.surfaceId = this.surfaceId;
             await this.avPlayer.prepare();
             break;
           case 'prepared':
             await this.avPlayer.play();
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

   @Entry
   @Component
   struct Index {
     private videoUri: string = '';
     private avPlayerMgr: AVPlayerManager | undefined = undefined;
     private mXComponentController: XComponentController = new XComponentController();

     build() {
       Column({ space: 20 }) {
         XComponent({
           type: XComponentType.SURFACE,
           controller: this.mXComponentController,
         })
           .width('100%')
           .aspectRatio(1)
           .renderFit(RenderFit.RESIZE_CONTAIN)

         Button('Pick Video')
           .padding(5)
           .fontSize(30)
           .onClick(() => {
             // 从相册选择视频
             let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
             photoSelectOptions.maxSelectNumber = 1;
             photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.VIDEO_TYPE;
             let uris: Array<string> = [];
             let photoViewPicker = new photoAccessHelper.PhotoViewPicker();
             photoViewPicker.select(photoSelectOptions)
               .then((photoSelectResult: photoAccessHelper.PhotoSelectResult) => {
                 uris = photoSelectResult.photoUris;
                 console.info(`photoViewPicker.select to file succeed and uris are: ` + uris);
                 if (uris.length > 0) {
                   this.videoUri = uris[0];
                 } else {
                   console.error(`failed to get media video uri`);
                 }
               })
               .catch((err: BusinessError) => {
                 console.error(`Invoke photoViewPicker.select failed, code is ${err.code}, message is ${err.message}`);
               });
           })

         Button('Play Video')
           .padding(5)
           .fontSize(30)
           .onClick(async () => {
             this.avPlayerMgr = new AVPlayerManager();
             this.avPlayerMgr.setSurfaceId(this.mXComponentController.getXComponentSurfaceId());
             await this.avPlayerMgr.init();
             await this.avPlayerMgr.setMediaAsset(this.videoUri);
           })
       }
       .width('100%')
       .height('100%')
       .justifyContent(FlexAlign.Center)
       .alignItems(HorizontalAlign.Center)
     }
   }
   ```
