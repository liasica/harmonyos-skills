---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-45
title: AudioRenderer如何根据进度条位置跳转播放
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > AudioRenderer如何根据进度条位置跳转播放
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ae8243824e3908dc8a9fa88a7eef8793ae54b4364d496205a3994674a778c70f
---

## 问题现象

使用AudioRenderer播放音频时，不支持类似AVPlayer的seek接口，无法直接跳转到指定播放位置。如何实现拖动进度条，AudioRenderer跳转到对应位置播放？

## 背景知识

* [AudioRenderer](../harmonyos-references/arkts-apis-audio-audiorenderer.md)是音频渲染器，用于播放PCM（Pulse Code Modulation）音频数据。
* 可以通过[onChange](../harmonyos-references/ts-basic-components-slider.md#onchange)事件监听[Slider](../harmonyos-references/ts-basic-components-slider.md)组件滑动时的进度值变化。

## 解决方案

1. 在Slider拖动过程中，通过[onChange](../harmonyos-references/ts-basic-components-slider.md#onchange)事件监听滑动的进度值value，根据value计算对齐字节后的播放偏移量offset。

   ```ts
   Slider({
     min: 0,
     max: this.fileSize,
     value: this.readOffset,
     style: SliderStyle.OutSet
   })
     .height(4)
     .width('80%')
     .trackThickness(4)
     .margin({ bottom: 2 })
     .padding({ left: 6, right: 6 })
     .blockSize({ width: 15, height: 15 })
     .onChange((value: number) => {
       let offset = Math.floor(value);
       if (offset % 2 !== 0) {
         offset -= 1;
       }
       this.setReadOffset(offset);
     });
   ```
2. 调用setReadOffset函数，更新音频读取位置readOffset，调用[flush](../harmonyos-references/arkts-apis-audio-audiorenderer.md#flush11)接口清空数据缓冲区，AudioRenderer会通过on('writeData')回调重新读取数据。

   ```ts
   setReadOffset(offset: number) {
     this.readOffset = offset;
     this.renderer?.flush();
   }
   ```
3. 在[on('writeData')](../harmonyos-references/arkts-apis-audio-audiorenderer.md#onwritedata11)回调中，offset为读取文件的起点，通过将readOffset赋值给offset，实现从进度条拖动位置开始播放音频的功能。

   ```ts
   this.renderer.on('writeData', (buffer: ArrayBuffer) => {
     let lastLen = this.fileSize - this.readOffset;
     let readLen = lastLen >= buffer.byteLength ? buffer.byteLength : lastLen;
     // 读取数据
     fileIo.readSync(this.playFile?.fd, buffer, { offset: this.readOffset, length: readLen });
     this.readOffset += readLen;
     if (this.readOffset >= this.fileSize) {
       this.readOffset = 0;
     }
   });
   ```

完整示例如下：

```ts
import { audio } from '@kit.AudioKit';
import { fileIo } from '@kit.CoreFileKit';

@Entry
@Component
struct DragSlider {
  @State readOffset: number = 0;
  @State fileSize: number = 0;
  @State isPlaying: boolean = false;
  private playFile?: fileIo.File;
  private renderer?: audio.AudioRenderer;

  build() {
    Scroll() {
      Column() {
        Column() {
          Slider({
            min: 0,
            max: this.fileSize,
            value: this.readOffset,
            style: SliderStyle.OutSet
          })
            .height(4)
            .width('80%')
            .trackThickness(4)
            .margin({ bottom: 2 })
            .padding({ left: 6, right: 6 })
            .blockSize({ width: 15, height: 15 })
            .onChange((value: number) => {
              let offset = Math.floor(value);
              if (offset % 2 !== 0) {
                offset -= 1;
              }
              this.setReadOffset(offset);
            });
        }
        .width('100%')
        .height(40)
        .margin({ top: 40 });

        Row() {
          Column() {
            Text('初始化')
              .fontColor(Color.Black)
              .fontSize(16)
              .width('100%')
              .height('100%')
              .textAlign(TextAlign.Center);
          }
          .backgroundColor(Color.White)
          .borderRadius(30)
          .width(100)
          .height(100)
          .margin({ right: 12, bottom: 12 })
          .onClick(async () => {
            await this.initRenderer();
          });

          Column() {
            Text('开始播放')
              .fontColor(Color.Black)
              .fontSize(16)
              .width('100%')
              .height('100%')
              .textAlign(TextAlign.Center);
          }
          .backgroundColor(Color.White)
          .borderRadius(30)
          .width(100)
          .height(100)
          .margin({ right: 12, bottom: 12 })
          .onClick(async () => {
            this.isPlaying = true;
            await this.startRenderer(this.getUIContext());
          });
        };

        Row() {
          Column() {
            Text('暂停播放')
              .fontColor(Color.Black)
              .fontSize(16)
              .width('100%')
              .height('100%')
              .textAlign(TextAlign.Center);
          }
          .id('audio_effect_manager_card')
          .backgroundColor(Color.White)
          .borderRadius(30)
          .width(100)
          .height(100)
          .margin({ right: 12, bottom: 12 })
          .onClick(async () => {
            this.pauseRenderer();
            this.isPlaying = false;
          });

          Column() {
            Text('释放资源')
              .fontColor(Color.Black)
              .fontSize(16)
              .width('100%')
              .height('100%')
              .textAlign(TextAlign.Center);
          }
          .id('audio_volume_card')
          .backgroundColor(Color.White)
          .borderRadius(30)
          .width(100)
          .height(100)
          .margin({ right: 12, bottom: 12 })
          .onClick(async () => {
            this.releaseRenderer();
            this.isPlaying = false;
            this.readOffset = 0;
          });
        };
      }
      .height('100%')
      .width('100%')
      .backgroundColor('#F1F3F5');
    };
  }

  setReadOffset(offset: number) {
    this.readOffset = offset;
    this.renderer?.flush();
  }

  rendererState(): audio.AudioState | undefined {
    if (this.renderer !== undefined) {
      return this.renderer.state;
    }
    return undefined;
  }

  async initRenderer() {
    let audioStreamInfo: audio.AudioStreamInfo = {
      channels: audio.AudioChannel.CHANNEL_1,
      samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_16000,
      sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
      encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW,
    };
    let audioRendererInfo: audio.AudioRendererInfo = {
      rendererFlags: 0,
      usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
    };
    let audioRendererOptions: audio.AudioRendererOptions = {
      streamInfo: audioStreamInfo,
      rendererInfo: audioRendererInfo,
    };

    this.renderer = await audio.createAudioRenderer(audioRendererOptions);

    this.renderer.on('writeData', (buffer: ArrayBuffer) => {
      let lastLen = this.fileSize - this.readOffset;
      let readLen = lastLen >= buffer.byteLength ? buffer.byteLength : lastLen;
      // 读取数据
      fileIo.readSync(this.playFile?.fd, buffer, { offset: this.readOffset, length: readLen });
      this.readOffset += readLen;
      if (this.readOffset >= this.fileSize) {
        this.readOffset = 0;
      }
    });
  }

  async startRenderer(context: UIContext) {
    if (this.renderer === undefined) {
      throw new Error(`AudioRenderer undefined`);
    }
    let state = this.renderer.state;
    if (state === audio.AudioState.STATE_INVALID) {
      this.renderer = undefined;
      throw new Error(`Start AudioRenderer at invalid state.`);
    }
    let contact = context.getHostContext() as Context;
    let pathDir = contact.filesDir;
    // 需确保沙箱中有此文件
    let filePath = pathDir + `/test.pcm`;
    if (this.playFile?.path !== filePath) {
      if (this.playFile) {
        await fileIo.close(this.playFile);
        await this.renderer.flush();
      }
      this.playFile = await fileIo.open(filePath, fileIo.OpenMode.READ_ONLY);
    }
    this.fileSize = fileIo.statSync(filePath).size;
    await this.renderer.start();
  }

  async pauseRenderer() {
    if (this.renderer === undefined) {
      throw new Error(`AudioRenderer undefined`);
    }
    let state = this.renderer.state;
    if (state === audio.AudioState.STATE_INVALID) {
      this.renderer = undefined;
      throw new Error(`Pause AudioRenderer at invalid state.`);
    }

    await this.renderer.pause();
  }

  async stopRenderer() {
    if (this.renderer === undefined) {
      throw new Error(`AudioRenderer undefined`);
    }
    let state = this.renderer.state;
    if (state === audio.AudioState.STATE_INVALID) {
      this.renderer = undefined;
      throw new Error(`Stop AudioRenderer at invalid state.`);
    }

    await this.renderer.stop();

    fileIo.closeSync(this.playFile?.fd);
  }

  async releaseRenderer() {
    if (this.renderer === undefined) {
      throw new Error(`AudioRenderer undefined`);
    }
    let state = this.renderer.state;
    if (state === audio.AudioState.STATE_INVALID) {
      this.renderer = undefined;
      throw new Error(`Release AudioRenderer at invalid state.`);
    }
    await this.renderer.release();
  }
}
```
