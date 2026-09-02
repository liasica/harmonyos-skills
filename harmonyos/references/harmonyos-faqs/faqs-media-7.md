---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-7
title: 如何获取视频首帧画面
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 如何获取视频首帧画面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:bd378606277872d83a79e8ba895da0f247880b32df920d0d91c45277987fcb20
---

获取视频首帧分为从本地视频获取视频首帧和从网络视频获取视频首帧。

**本地视频获取首帧**

从本地视频获取首帧有两种方案，分别是通过[PhotoAsset](../harmonyos-references/js-apis-sendablephotoaccesshelper.md#photoasset)类的[getThumbnail()](../harmonyos-references/js-apis-sendablephotoaccesshelper.md#getthumbnail)方法获取首帧；通过[AVImageGenerator](../harmonyos-references/arkts-apis-media-avimagegenerator.md)选取视频开始时间获取首帧，详细内容请参考[选取视频帧作为缩略图](../harmonyos-guides/video-thumbnail-system.md#选取视频帧作为缩略图)。

此外，如果是从沙箱路径获取视频首帧，需要获取视频文件的文件描述符fd，详细内容请参考[应用文件访问(ArkTS)](../harmonyos-guides/app-file-access.md)。

```ts
// Create AVImageGenerator object
let avImageGenerator: media.AVImageGenerator = await media.createAVImageGenerator();
// Configure avImageGenerator.fdSrc attributes based on album video URI
let fileINT = fileIo.openSync(this.filesDir + '/test1.mp4', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
let avFileDescriptor: media.AVFileDescriptor = { fd: fileINT.fd };
// Configuration parameter
avImageGenerator.fdSrc = avFileDescriptor;
```

**网络视频获取首帧**

在网络视频获取首帧的情况下，需要先将网络视频下载到沙箱，使用avImageGenerator.fetchFrameByTime方式获取首帧图片。

参考代码如下所示：

```ts
import { media } from '@kit.MediaKit'
import image from '@ohos.multimedia.image';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError, request } from '@kit.BasicServicesKit';

@Component
struct GetFirstFrameAnimation {
  @State isPlaying: boolean = false;
  @State pixelMap: image.PixelMap | undefined = undefined;
  @State filesDir: string = '';
  private count: number = 0;
  // The surfaceID is used for displaying the playback image and needs to be obtained through the XComponent interface.
  private surfaceID: string = '';
  // Used to distinguish whether a pattern supports seek operation.
  private isSeek: boolean = true;
  xComponentController: XComponentController = new XComponentController();
  private uiContext: Context = this.getUIContext().getHostContext() as Context;

  aboutToAppear() {
    this.filesDir = this.uiContext.filesDir;
    this.fetchFrameByTimeFromWeb();
  }

  fetchFrameByTimeFromWeb() {
    let path = this.filesDir + 'test1.mp4';
    if (fileIo.accessSync(path)) {
      fileIo.unlinkSync(path);
    }
    // Network Video
    try {
      request.downloadFile(this.uiContext, {
        enableMetered: true,
        // Some online video formats are not supported, which makes it impossible to parse and read the thumbnail of a certain frame of the video.
        url: 'xxx.mp4',
        filePath: this.filesDir + 'test1.mp4'
      })
        .then((downloadTask: request.DownloadTask) => {
          downloadTask.on('fail', (err: number) => {
            console.error(`Failed to download the task. Code: ${err}`);
          })
          downloadTask.on('progress', (receivedSize: number, totalSize: number) => {
            console.log('download', 'receivedSize:' + (receivedSize / 1024) + 'totalSize:' + (totalSize / 1024));
          })
          downloadTask.on('complete', async () => {
            // Create AVImageGenerator object
            let avImageGenerator: media.AVImageGenerator = await media.createAVImageGenerator();
            // Configure avImageGenerator.fdSrc attributes based on album video URI
            let fileINT = fileIo.openSync(this.filesDir + '/test1.mp4', fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
            let avFileDescriptor: media.AVFileDescriptor = { fd: fileINT.fd };
            // Configuration parameter
            avImageGenerator.fdSrc = avFileDescriptor;
            // Initialize input parameters
            let timeUs = 0;
            let queryOption = media.AVImageQueryOptions.AV_IMAGE_QUERY_NEXT_SYNC;
            let param: media.PixelMapParams = {
              width: 300,
              height: 300
            };
            // Get thumbnail(Promise mode)
            this.pixelMap = await avImageGenerator.fetchFrameByTime(timeUs, queryOption, param);
            // Release resources(Promise mode)
            avImageGenerator.release();
            fileIo.closeSync(fileINT);
          })
        })
        .catch((err: BusinessError) => {
          console.error(`Invoke downloadTask failed, code is ${err.code}, message is ${err.message}`);
        })
    } catch (error) {
      let err = error as BusinessError;
      console.error(`Invoke downloadFile failed, code is ${err.code}, message is ${err.message}`);
    }
  }

  // Registering Callbacks
  setAVPlayerCallback(avPlayer: media.AVPlayer) {
    // SetAVPlayerCallback first frame rendering callback function.
    avPlayer.on('startRenderFrame', () => {
      console.log(`AVPlayer start render frame`);
    })
    // Seek operation result callback function.
    avPlayer.on('seekDone', (seekDoneTime: number) => {
      console.log(`AVPlayer seek succeed, seek time is ${seekDoneTime}`);
    })
    // Error callback listening function, when avPlayer encounters an error during operation, call the reset interface to trigger the reset process.
    avPlayer.on('error', (err: BusinessError) => {
      console.error(`Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`);
      avPlayer.reset(); // Call reset to reset resources and trigger idle status.
    })
    // State change callback function
    avPlayer.on('stateChange', async (state: string, _reason: media.StateChangeReason) => {
      switch (state) {
        case 'idle': // Successfully called reset to reset resources, triggering idle status.
          avPlayer.release();
          break;
        case 'initialized': // AVPlayer triggers this status report after setting the playback resource.
          avPlayer.surfaceId = this.surfaceID; // Set display screen, no need to set when playing pure audio resources.
          avPlayer.prepare();
        case 'prepared': // Report this status after successful preparation call.
          avPlayer.play(); // Call the playback interface to start playing.
          this.isPlaying = true;
          break;
        case 'playing': // Trigger this status report after successful play call.
          if (this.count !== 0) {
            if (this.isSeek) {
              avPlayer.seek(avPlayer.duration); // Seek to the end of the video.
            } else {
              // When the playback mode does not support seek operation, continue playing until the end.
              console.log('AVPlayer wait to play end.')
            }
          } else {
            avPlayer.pause(); // Call the pause interface to pause playback.
          }
          this.count++;
          break;
        case 'paused': // Call to trigger the status report after pause succeeds.
          avPlayer.play();
          break;
        case 'completed': // Trigger the status report after the playback ends.
          avPlayer.stop();
          break;
        case 'stopped': // Trigger the status report after the stop interface is successfully called.
          avPlayer.reset(); // Call the reset interface to initialize the avplayer state.
          break;
        case 'released':
          console.log('AVPlayer state released called.');
          break;
        default:
          console.log('AVPlayer state unknown called.');
          break;
      }
    })
  }

  async avPlayerLiveDemo() {
    // Create an avPlayer instance object.
    let avPlayer: media.AVPlayer = await media.createAVPlayer();
    // Create a state change callback function.
    this.setAVPlayerCallback(avPlayer);
    this.isSeek = false; // SEEK operation is not supported.
    avPlayer.url = 'xxx.mp4';
    // avPlayer.url = 'xxx.m3u8'; // Play the HLS live streaming stream.
  }

  build() {
    Column() {
      Stack({ alignContent: Alignment.TopStart }) {
        if (!this.isPlaying && this.pixelMap) {
          Image(this.pixelMap)
            .width('640px')
            .height('480px')
            .zIndex(10)
        }
        XComponent({
          id: 'XComponent',
          type: XComponentType.SURFACE,
          controller: this.xComponentController
        })
          .width('640px')
          .height('480px')
          .zIndex(9)
          .onLoad(() => {
            this.surfaceID = this.xComponentController.getXComponentSurfaceId();
          })
      }
      .position({ x: 0, y: 48 })

      Button('点击播放')
        .onClick(() => {
          this.avPlayerLiveDemo();
        })
    }
  }
}
```
