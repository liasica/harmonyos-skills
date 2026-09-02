---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-51
title: AudioRenderer创建多个实例并轮询其状态来并发播放音乐
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > AudioRenderer创建多个实例并轮询其状态来并发播放音乐
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:0c4364aacfdea2facec2d6134bb788868cf454b7f7fa87be6af200fe00a85d25
---

## 问题现象

AudioRenderer支持低时延播放。可以通过创建多个实例并轮询其状态来管理多个音频的播放。在一个实例空闲时使用它来播放下一个音效，从而有效地处理大量的短音频并发播放请求。

## 背景知识

[AudioRenderer](../harmonyos-guides/using-audiorenderer-for-playback.md)是音频渲染器，用于播放PCM音频数据，需要应用持续写入音频数据进行工作，应用可以在输入前添加数据预处理，如设定音频文件的采样率、位宽等，要求开发者具备音频处理的基础知识，适用于更专业、更多样化的媒体播放应用开发。

## 解决方案

通过循环创建多个AudioRenderer实例，通过周期性定时器不断轮询所有AudioRenderer实例的状态，取其中空闲状态的实例作为当前实例，用来播放当前音乐，当播放下一首音乐时，使用的是从所有AudioRenderer实例轮询出来的空闲实例，不影响当前音乐的播放，从而有效地处理大量的音频并发播放请求。

1. 循环创建多个AudioRenderer实例。

   ```ts
   // 循环创建多个实例
       for (let num = 0; num < 4; num++) {
         audio.createAudioRenderer(this.audioRendererOptions, (err, data) => {
           if (err) {
             console.error(TAG, `Invoke createAudioRenderer failed, code is ${err.code}, message is ${err.message}`);
             return;
           } else {
             console.info(TAG, 'Invoke createAudioRenderer succeeded.');
             this.audioRendererList.push(data); // 创建的实例放到数组中
           }
         });
       }
   ```
2. 通过周期性定时器不断轮询所有AudioRenderer实例的状态，取其中空闲状态的实例作为当前实例。

   ```ts
   // 轮询audioRenderer实例数组中，空闲的实例，并设为当前实例，为后续播放做准备
       setInterval(() => {
         for (let num = 0; num < 4; num++) {
           let renderModelTemp = this.audioRendererList[num];
           // 当数组中audioRenderer实例状态为prepared时，将该实例赋给当前实例
           if ((renderModelTemp as audio.AudioRenderer).state.valueOf() == 1) {
             this.renderModel = renderModelTemp;
             console.info(TAG + `AudioRenderer state: ${renderModelTemp.state}`);
           } else {
             console.info(TAG + `AudioRenderer state: ${renderModelTemp.state}`);
           }
         }
       }, 10);
   ```
3. 调用当前AudioRenderer实例来播放音乐。

   ```ts
   // 开始一次音频渲染。
     start() {
       if (this.renderModel !== undefined) {
         let stateGroup = [audio.AudioState.STATE_PREPARED, audio.AudioState.STATE_PAUSED, audio.AudioState.STATE_STOPPED];
         if (stateGroup.indexOf((this.renderModel as audio.AudioRenderer).state.valueOf()) ===
           -1) { // 当前状态为prepared、paused和stopped之一时才能启动渲染。
           console.error(TAG + 'start failed');
           return;
         }
         // 启动渲染。
         (this.renderModel as audio.AudioRenderer).start((err: BusinessError) => {
           if (err) {
             console.error('Renderer start failed.');
           } else {
             console.info('Renderer start success.');
           }
         });
       }
     }
   ```

完整示例如下：

```ts
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

const TAG = 'AudioRendererDemo';

class Options {
  offset?: number;
  length?: number;
}

@Entry
@Component
struct Index {
  context: Context = this.getUIContext().getHostContext() as Context;
  @State renderModel: audio.AudioRenderer | undefined = undefined;
  @State file: fs.File | undefined = undefined;
  // 此处仅作示例，如下pcm资源，实际使用时需要将文件替换为应用要播放的PCM文件，否则无法成功运行。
  private fileStr: string[] = ['XXXX.pcm', 'XXXX.pcm'];
  private bufferSize: number = 0;
  private audioRendererList: Array<audio.AudioRenderer> = [];
  public audioStreamInfo: audio.AudioStreamInfo = {
    samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000,
    channels: audio.AudioChannel.CHANNEL_2,
    sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE,
    encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW
  };
  public audioRendererInfo: audio.AudioRendererInfo = {
    usage: audio.StreamUsage.STREAM_USAGE_MUSIC,
    rendererFlags: 0
  };
  public audioRendererOptions: audio.AudioRendererOptions = {
    streamInfo: this.audioStreamInfo,
    rendererInfo: this.audioRendererInfo
  };

  aboutToAppear(): void {

    // 循环创建多个实例
    for (let num = 0; num < 4; num++) {
      audio.createAudioRenderer(this.audioRendererOptions, (err, data) => {
        if (err) {
          console.error(TAG, `Invoke createAudioRenderer failed, code is ${err.code}, message is ${err.message}`);
          return;
        } else {
          console.info(TAG, 'Invoke createAudioRenderer succeeded.');
          this.audioRendererList.push(data); // 创建的实例放到数组中
        }
      });
    }

    // 轮询audioRenderer实例数组中，空闲的实例，并设为当前实例，为后续播放做准备
    setInterval(() => {
      for (let num = 0; num < 4; num++) {
        let renderModelTemp = this.audioRendererList[num];
        // 当数组中audioRenderer实例状态为prepared时，将该实例赋给当前实例
        if ((renderModelTemp as audio.AudioRenderer).state.valueOf() == 1) {
          this.renderModel = renderModelTemp;
          console.info(TAG + `AudioRenderer state: ${renderModelTemp.state}`);
        } else {
          console.info(TAG + `AudioRenderer state: ${renderModelTemp.state}`);
        }
      }
    }, 10);

  }

  // 开始一次音频渲染。
  start() {
    if (this.renderModel !== undefined) {
      let stateGroup = [audio.AudioState.STATE_PREPARED, audio.AudioState.STATE_PAUSED, audio.AudioState.STATE_STOPPED];
      if (stateGroup.indexOf((this.renderModel as audio.AudioRenderer).state.valueOf()) ===
        -1) { // 当前状态为prepared、paused和stopped之一时才能启动渲染。
        console.error(TAG + 'start failed');
        return;
      }
      // 启动渲染。
      (this.renderModel as audio.AudioRenderer).start((err: BusinessError) => {
        if (err) {
          console.error('Renderer start failed.');
        } else {
          console.info('Renderer start success.');
        }
      });
    }
  }

  // 暂停渲染。
  pause() {
    if (this.renderModel !== undefined) {
      // 只有渲染器状态为running的时候才能暂停。
      if ((this.renderModel as audio.AudioRenderer).state.valueOf() !== audio.AudioState.STATE_RUNNING) {
        console.info('Renderer is not running');
        return;
      }
      // 暂停渲染。
      (this.renderModel as audio.AudioRenderer).pause((err: BusinessError) => {
        if (err) {
          console.error('Renderer pause failed.');
        } else {
          console.info('Renderer pause success.');
        }
      });
    }
  }

  // 停止渲染。
  async stop() {
    if (this.renderModel !== undefined) {
      // 只有渲染器状态为running或paused的时候才可以停止。
      if ((this.renderModel as audio.AudioRenderer).state.valueOf() !== audio.AudioState.STATE_RUNNING &&
        (this.renderModel as audio.AudioRenderer).state.valueOf() !== audio.AudioState.STATE_PAUSED) {
        console.info('Renderer is not running or paused.');
        return;
      }
      // 停止渲染。
      (this.renderModel as audio.AudioRenderer).stop((err: BusinessError) => {
        if (err) {
          console.error('Renderer stop failed.');
        } else {
          fs.close(this.file);
          console.info('Renderer stop success.');
        }
      });
    }
  }

  // 销毁实例，释放资源。
  async release() {
    if (this.renderModel !== undefined) {
      // 渲染器状态不是released状态，才能release。
      if (this.renderModel.state.valueOf() === audio.AudioState.STATE_RELEASED) {
        console.info('Renderer already released');
        return;
      }
      // 释放资源。
      (this.renderModel as audio.AudioRenderer).release((err: BusinessError) => {
        if (err) {
          console.error('Renderer release failed.');
        } else {
          console.info('Renderer release success.');
        }
      });
    }
  }

  build() {
    Column({ space: 20 }) {
      Button('播放音乐1').onClick(() => {
        let path = this.context.cacheDir;

        let filePath = path + '/' + this.fileStr[0];
        let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
        this.file = file;
        let writeDataCallback = (buffer: ArrayBuffer) => {
          let options: Options = {
            offset: this.bufferSize,
            length: buffer.byteLength
          };
          try {
            fs.readSync(file.fd, buffer, options);
            this.bufferSize += buffer.byteLength;
            return audio.AudioDataCallbackResult.VALID;
          } catch (error) {
            console.error(`Error reading file`);
            return audio.AudioDataCallbackResult.INVALID;
          }
        };
        if (this.renderModel !== undefined) {
          (this.renderModel as audio.AudioRenderer).on('writeData', writeDataCallback);
          this.start();
        }
      });

      Button('播放音乐2').onClick(() => {
        let path = this.context.cacheDir;
        let filePath = path + '/' + this.fileStr[1];
        let file: fs.File = fs.openSync(filePath, fs.OpenMode.READ_ONLY);
        this.file = file;
        let writeDataCallback = (buffer: ArrayBuffer) => {
          let options: Options = {
            offset: this.bufferSize,
            length: buffer.byteLength
          };

          try {
            fs.readSync(file.fd, buffer, options);
            this.bufferSize += buffer.byteLength;
            return audio.AudioDataCallbackResult.VALID;
          } catch (error) {
            console.error(`Error reading file`);
            return audio.AudioDataCallbackResult.INVALID;
          }
        };
        if (this.renderModel !== undefined) {
          (this.renderModel as audio.AudioRenderer).on('writeData', writeDataCallback);
          this.start();
        }
      });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```

## 常见FAQ

Q：使用AudioRenderer播放多路音频时如何实现混音效果？

A：创建多个AudioRenderer实例并行写入音频数据，系统会自动将多路音频混合输出。两个Renderer使用不同的usage或相同usage，系统都会自动混音。
