---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-41
title: AVPlayer如何播放smb、ftp协议的视频
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > AVPlayer如何播放smb、ftp协议的视频
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7ba878356e9b6d4a61161552ef75d7d4dc83a85881ab2291509782e9c842f8ed
---

## 问题现象

AVPlayer是否支持smb、ftp协议的视频播放？如果不支持，如何播放smb、ftp协议的视频？

## 背景知识

* ftp协议：文件传输协议（File Transfer Protocol）是在计算机网络的客户端和服务器间传输文件的应用层协议。
* smb协议：服务器消息块（Server Message Block），主要功能是使网络上的机器能够共享计算机文件、打印机、串行端口和通讯等资源。
* [AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)将音视频媒体资源转码为可供渲染的图像和可听见的音频模拟信号，并通过输出设备进行播放。AVPlayer提供功能完善一体化播放能力，应用只需要提供流媒体来源，不负责数据解析和解码就可达成播放效果。AVPlayer支持的格式与协议可参考：[支持的格式与协议](../harmonyos-guides/media-kit-intro.md#支持的格式与协议)。

## 解决方案

AVPlayer在网络点播场景下支持的协议为：http/https/hls/dash协议，smb、ftp协议不在AVPlayer支持的范围内。具体可参考：[支持的格式与协议](../harmonyos-guides/media-kit-intro.md#支持的格式与协议)。

针对smb、ftp协议的网络视频点播，需要自行实现网络视频数据的拉取，然后通过AVPlayer的流式媒体资源描述方式实现视频播放。

创建音视频文件资源描述符[AVDataSrcDescriptor](../harmonyos-references/arkts-apis-media-i.md#avdatasrcdescriptor10)，在[AVDataSrcDescriptor](../harmonyos-references/arkts-apis-media-i.md#avdatasrcdescriptor10)的callback回调中持续写入通过smb、ftp拉取的网络视频数据。最后，在AVPlayer设置资源时，将[AVDataSrcDescriptor](../harmonyos-references/arkts-apis-media-i.md#avdatasrcdescriptor10)设置给AVPlayer[属性](../harmonyos-references/arkts-apis-media-avplayer.md#属性)的流式媒体资源描述dataSrc实现smb、ftp视频资源播放。

使用流式媒体资源描述播放视频需要注意，如果播放的是mp4/m4a格式用户需要保证moov字段（媒体信息字段）在mdat字段（媒体数据字段）之前，或者moov之前的字段小于10M，否则会导致解析失败无法播放。

使用AVPlayer流式媒体资源描述播放视频参考如下：

```ts
import { media } from '@kit.MediaKit';
import { Context } from '@kit.AbilityKit';

class AVPlayerManager {
  private surfaceId: string = ''; // 视频surfaceId
  private readOffset: number = 0; // 读取字节偏移量
  private videoBuffer?: Uint8Array; // 保存视频数据Buffer
  private avPlayer?: media.AVPlayer; // AVPlayer

  async initPlayer(context: Context, rawPath: string) {
    // 创建AVPlayer
    try {
      this.avPlayer = await media.createAVPlayer();
      this.setEventListening();
    } catch (err) {
      console.error(`create avplayer failed: ${err}`);
      return;
    }

    try {
      this.readOffset = 0;
      // 获取视频文件长度和数据Buffer，实际应该从网络获取，这里使用Rawfile模拟
      let rawFd = await context.resourceManager.getRawFd(rawPath);
      this.videoBuffer = await context.resourceManager.getRawFileContent(rawPath);
      // 数据写入回调，实际从网络读取视频数据，写入buffer用于AVPlayer播放。这里使用Rawfile模拟
      let callback = (buffer: ArrayBuffer, length: number): number => {
        if (this.videoBuffer === undefined) {
          return 0;
        }
        // 计算读取数据字节数
        let remainSize = this.videoBuffer.length - this.readOffset;
        let readSize = Math.min(length, remainSize);
        // 写入buffer
        let bufferView = new Uint8Array(buffer);
        bufferView.set(this.videoBuffer.slice(this.readOffset, this.readOffset + readSize));
        // 更新写入偏移量
        this.readOffset += readSize;
        return readSize;
      };
      // 设置AVPlayer流式媒体资源描述
      this.avPlayer.dataSrc = { fileSize: rawFd.length, callback: callback };
    } catch (err) {
      console.error(`Failed to set avPlayer.dataSrc, Cause: ${JSON.stringify(err)}`);
    }
  }

  setSurfaceId(surfaceId: string) {
    this.surfaceId = surfaceId;
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
      if (this.avPlayer === undefined) {
        return;
      }
      switch (state) {
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
            await this.avPlayer.play();
          } catch (err) {
            console.error(`failed to invoke avplayer play, error is ${err}`);
          }
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
  private xComponentCtl: XComponentController = new XComponentController();
  private avPlayerMgr: AVPlayerManager = new AVPlayerManager();

  build() {
    Column({ space: 20 }) {
      XComponent({
        type: XComponentType.SURFACE,
        controller: this.xComponentCtl,
      })
        .width('100%')
        .aspectRatio(1)
        .renderFit(RenderFit.RESIZE_CONTAIN)
        .onLoad(() => {
          let context = this.getUIContext().getHostContext() as Context;
          let surfaceId = this.xComponentCtl.getXComponentSurfaceId();
          this.avPlayerMgr.setSurfaceId(surfaceId);
          // 播放AVPlayer视频
          this.avPlayerMgr.initPlayer(context, 'input.mp4');
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center);
  }
}
```
