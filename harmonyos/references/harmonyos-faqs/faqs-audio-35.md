---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-audio-35
title: 如何播放PCM格式的音频数据
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 音频（Audio） > 如何播放PCM格式的音频数据
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:43+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:119a189efdb07f3c078844c6d34cd84414b6a490da6373f2df80b51d652897b9
---

## 问题现象

使用AudioCapturer录制了一段PCM格式的音频数据，请问该如何播放，不同播放方式之间有何差异。

## 背景知识

AudioRenderer用于播放PCM音频数据，相比AVPlayer而言，可以在输入前添加数据预处理，以实现更灵活的播放功能，详情可以参考[AudioRenderer开发步骤](../harmonyos-guides/using-audiorenderer-for-playback.md#开发步骤及注意事项)。

AVPlayer可以实现音频解码和音频输出功能。可用于直接播放MP3、M4A、WAV等格式的音频文件，不支持直接播放PCM格式文件，详情可以参考[AVPlayer开发步骤](../harmonyos-guides/using-avplayer-for-playback.md#开发步骤及注意事项)。

## 解决方案

对于PCM格式的音频数据，有如下两种方案来进行处理：

**方案一：直接播放PCM格式的音频数据。**

1. 使用AudioRenderer直接播放PCM数据，具体开发步骤以及完整代码可以参考[AudioRenderer开发步骤及注意事项](../harmonyos-guides/using-audiorenderer-for-playback.md#开发步骤及注意事项)。
2. 使用OHAudio直接播放PCM数据，具体开发步骤以及完整示例代码可以参考[使用OHAudio开发音频播放功能](../harmonyos-guides/using-ohaudio-for-playback.md)。

**方案二：对PCM数据进行音频转码后使用AVPlayer播放。**

AVPlayer无法直接播放PCM格式的音频数据，需要将音频数据转码封装成AVPlayer支持的格式。

以WAV格式为例，WAV格式是一种无损的格式，可以最好地保存音频质量，如果对音频大小或者格式有其他要求，可以参考[音频编码](../harmonyos-guides/audio-encoding.md)和[媒体数据封装](../harmonyos-guides/audio-video-muxer.md)进行其他的音频编码格式转化。

将PCM数据转码封装成完整的WAV文件再用AVPlayer播放步骤如下：

1. 定义PCM转WAV的方法，获取源文件路径和目标文件路径，分别写入WAV文件头和PCM数据。
2. 定义写入WAV头部信息的方法，创建一个大小为44字节的缓冲区，用于存储WAV文件的头部信息，再将其写入输出文件。
3. 定义读取PCM数据的方法，将PCM数据从输入文件写入输出文件。

   ```screen
   async pcmToWav(pcmFilePath: string) {
     let fileSize = 0;
     try {
       fileSize = fileIo.statSync(pcmFilePath).size;
     } catch (err) {
       console.error(`failed to get file size, ${JSON.stringify(err)}`);
     }
     this.waveHeader.fileSize = fileSize + 44 - 8;
     this.waveHeader.dataSize = fileSize;

     let idx: number = 0;
     let buffer: ArrayBuffer = new ArrayBuffer(44);
     let bufferView: DataView = new DataView(buffer);
     // riff
     this.setString(idx, this.waveHeader.riff, bufferView);
     idx += 4;
     // file size
     bufferView.setInt32(idx, this.waveHeader.fileSize, true);
     idx += 4;
     // wave
     this.setString(idx, this.waveHeader.wave, bufferView);
     idx += 4;
     // fmt
     this.setString(idx, this.waveHeader.fmtChunkMarker, bufferView);
     idx += 4;
     // fmt size
     bufferView.setInt32(idx, this.waveHeader.fmtSize, true);
     idx += 4;
     // format type
     bufferView.setInt16(idx, this.waveHeader.formatType, true);
     idx += 2;
     // channels
     bufferView.setInt16(idx, this.waveHeader.channels, true);
     idx += 2;
     // sample rate
     bufferView.setInt32(idx, this.waveHeader.sampleRate, true);
     idx += 4;
     // byte rate
     bufferView.setInt32(idx, this.waveHeader.byteRate, true);
     idx += 4;
     // block align
     bufferView.setInt16(idx, this.waveHeader.blockAlign, true);
     idx += 2;
     // bits per sample
     bufferView.setInt16(idx, this.waveHeader.bitsPerSample, true);
     idx += 2;
     // data
     this.setString(idx, this.waveHeader.dataChunkMarker, bufferView);
     idx += 4;
     // data size
     bufferView.setInt32(idx, this.waveHeader.dataSize, true);

     let path = this.context.filesDir + '/output.wav'; // output wav file path
     let inputFile: fileIo.File | undefined;
     let outputFile: fileIo.File | undefined;
     try {
       inputFile = fileIo.openSync(pcmFilePath, fileIo.OpenMode.READ_ONLY);
       outputFile = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC | fileIo.OpenMode.WRITE_ONLY);
       // write wav header
       fileIo.writeSync(outputFile.fd, buffer);
       // write pcm data
       let readSize = 0;
       let readBuf = new ArrayBuffer(1024 * 1024);
       do {
         readSize = fileIo.readSync(inputFile.fd, readBuf);
         fileIo.writeSync(outputFile.fd, readBuf, { length: readSize });
       } while (readSize > 0);
     } catch (err) {
       console.error(`Failed to write file, ${JSON.stringify(err)}`);
     } finally {
       if (inputFile) {
         fileIo.closeSync(inputFile);
       }
       if (outputFile) {
         fileIo.closeSync(outputFile);
       }
     }
   }
   ```
4. 完成转码后使用AVPlayer进行播放，AVPlayer的具体开发流程可以参考[AVPlayer播放音频完整示例](../harmonyos-guides/using-avplayer-for-playback.md#运行完整示例)。

   ```screen
   async avPlayerUrlDemo() {
     this.avPlayer = await media.createAVPlayer();
     // 创建状态机变化回调函数
     this.setAVPlayerCallback(this.avPlayer!);
     let fdPath = 'fd://';
     // 通过UIAbilityContext获取沙箱地址filesDir，以Stage模型为例。
     let path = this.context.filesDir + '/output.wav';
     // 打开相应的资源文件地址获取fd，并为url赋值触发initialized状态机上报。
     let file = await fs.open(path);
     fdPath = fdPath + '' + file.fd;
     this.avPlayer.url = fdPath;
   }
   ```

完整示例代码如下：

```screen
import { fileIo } from '@kit.CoreFileKit';
import { media } from '@kit.MediaKit';
import { audio } from '@kit.AudioKit';
import { common } from '@kit.AbilityKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo as fs } from '@kit.CoreFileKit';

let audioRenderer: audio.AudioRenderer;
let audioStreamInfo: audio.AudioStreamInfo = {
  samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_8000, // 采样率。
  channels: audio.AudioChannel.CHANNEL_1, // 通道。
  sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // 采样格式。
  encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // 编码格式。
};
let audioRendererInfo: audio.AudioRendererInfo = {
  usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage。
  rendererFlags: 0 // 音频渲染器标志。
};
let audioRendererOptions: audio.AudioRendererOptions = {
  streamInfo: audioStreamInfo,
  rendererInfo: audioRendererInfo
};

@Entry
@Component
struct PlayPcmDataDemo {
  context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  audioData: Uint8Array = generateTestPCM(); // 测试PCM数据，按需替换为其他音频数据源
  writeOffset = 0;
  private transcoder = new pcmTranscoder(this.context);
  private avplayer = new AVPlayerDemo(this.context);

  async aboutToAppear(): Promise<void> {
    audioRenderer = await audio.createAudioRenderer(audioRendererOptions);
    await this.init(); // 初始化
    this.writePCMData();
  }

  async aboutToDisappear(): Promise<void> {
    await audioRenderer.release();
    await this.avplayer.release();
  }

  build() {
    Column({ space: 10 }) {
      Button('AudioRenderer播放')
        .width('100%')
        .onClick(async () => {
          await audioRenderer.start();
        });
      Button('AudioRenderer停止播放')
        .width('100%')
        .onClick(async () => {
          console.info('renderer status' + audioRenderer.state);
          this.stopAndFlush();
        });
      Button('PCM转码WAV')
        .width('100%')
        .onClick(async () => {
          let filepath = this.context.filesDir + '/testpcm.pcm';
          await this.transcoder.pcmToWav(filepath);
        });
      Button('AVPlayer播放')
        .width('100%')
        .onClick(async () => {
          this.avplayer.avPlayerUrlDemo();
        });
    }
    .padding(20)
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }

  async init() {
    audioRenderer.on('writeData', (buffer: ArrayBuffer) => {
      if (!this.audioData) {
        return audio.AudioDataCallbackResult.INVALID;
      }
      let bufferView = new Uint8Array(buffer);
      let writeLen = Math.min(buffer.byteLength, this.audioData.byteLength - this.writeOffset);
      if (writeLen <= 0) {
        this.writeOffset = 0;
        console.info('Play Done');
        return audio.AudioDataCallbackResult.INVALID;
      }
      bufferView.set(this.audioData.slice(this.writeOffset, this.writeOffset + writeLen));
      this.writeOffset += writeLen;
      return audio.AudioDataCallbackResult.VALID;
    });
  }

  async stopAndFlush() {
    console.info('renderer status' + audioRenderer.state);
    audioRenderer.stop().then(() => {
      console.error('Renderer stop ok.');
    }).catch((err: BusinessError) => {
      console.error('Renderer stop failed. ', err);
    });
    audioRenderer.flush().then(() => {
      console.error('Renderer flush ok.');
    }).catch((err: BusinessError) => {
      console.error('renderer flush err. ' + err);
    });
    this.writeOffset = 0;
  }

  async writePCMData() {
    let filesDir = this.context.filesDir;
    let file = fs.openSync(filesDir + '/testpcm.pcm', fs.OpenMode.READ_WRITE | fs.OpenMode.CREATE);
    let bufferView = new Uint8Array(this.audioData);
    fs.writeSync(file.fd, bufferView.buffer);
  }
}

function generateTestPCM(): Uint8Array {
  const sampleRate = 8000;
  const noteDuration = 0.3;
  const amplitude = 0.35;

  const freqMap: Record<number, number> = {
    1: 523.25, // C5
    2: 587.33, // D5
    3: 659.25, // E5
    4: 698.46, // F5
    5: 783.99, // G5
    6: 880.00, // A6
    7: 987, // B6
    8: 392, // A5
    9: 439, // B5
  };

  const melody = [
    3, 5, 6, 5, 6, 6, 3, 3, 2, 2, 3, 5, 5, 5, 5, 0,
    1, 2, 3, 2, 3, 3, 8, 8, 9, 9, 1, 2, 2, 2, 2, 0,
    3, 5, 6, 5, 6, 6, 6, 7, 5, 5, 3, 2, 1, 1, 1, 0,
    1, 9, 1, 9, 1, 1, 3, 3, 2, 2, 2, 0
  ];

  const samplesPerNote = Math.floor(sampleRate * noteDuration); // 4000
  const totalSamples = samplesPerNote * melody.length; // 96,000
  const buffer = new ArrayBuffer(totalSamples * 2); // 192,000 bytes
  const view = new DataView(buffer);

  let idx = 0;
  for (const note of melody) {
    const freq = note ? freqMap[note] : 0;
    for (let i = 0; i < samplesPerNote; i++) {
      const t = i / sampleRate;
      const wave = freq ? amplitude * Math.sin(2 * Math.PI * freq * t) : 0;
      const sample = Math.round(wave * 32767);
      const clamped = Math.max(-32768, Math.min(32767, sample));
      view.setInt16(idx * 2, clamped, true);
      idx++;
    }
  }
  return new Uint8Array(buffer);
}

interface WavHeader {
  riff: string,
  fileSize: number,
  wave: string,
  fmtChunkMarker: string,
  fmtSize: number,
  formatType: number,
  channels: number,
  sampleRate: number,
  byteRate: number,
  blockAlign: number,
  bitsPerSample: number,
  dataChunkMarker: string,
  dataSize: number
};

class pcmTranscoder {
  private context: Context;

  constructor(context: Context) {
    this.context = context;
  }

  waveHeader: WavHeader = {
    riff: 'RIFF', // "RIFF"
    fileSize: 0, // 文件大小减去8
    wave: 'WAVE', // ”WAVE“
    fmtChunkMarker: 'fmt ', // "fmt "
    fmtSize: 16, // 16
    formatType: 1, // 1（表示PCM）
    channels: 1, // 声道数
    sampleRate: 8000, // 采样率
    byteRate: 8000 * 2 * 2, // 每秒字节数(SampleRate * Channels * BitsPerSample / 8)
    blockAlign: 2 * 2, // 帧大小(channels * BitsPerSample / 8)
    bitsPerSample: 16, // 采样位数
    dataChunkMarker: 'data', // ”data“
    dataSize: 0, // 数据大小
  };

  setString(idx: number, str: string, view: DataView) {
    for (let i = 0; i < str.length; i++) {
      view.setInt8(idx++, str.charCodeAt(i));
    }
  }

  /**
   * 为pcm文件封装wav头
   * @param pcmFilePath 保存录制的pcm数据的沙箱文件路径
   */
  async pcmToWav(pcmFilePath: string) {
    let fileSize = 0;
    try {
      fileSize = fileIo.statSync(pcmFilePath).size;
    } catch (err) {
      console.error(`failed to get file size, ${JSON.stringify(err)}`);
    }
    this.waveHeader.fileSize = fileSize + 44 - 8;
    this.waveHeader.dataSize = fileSize;

    let idx: number = 0;
    let buffer: ArrayBuffer = new ArrayBuffer(44);
    let bufferView: DataView = new DataView(buffer);
    // riff
    this.setString(idx, this.waveHeader.riff, bufferView);
    idx += 4;
    // file size
    bufferView.setInt32(idx, this.waveHeader.fileSize, true);
    idx += 4;
    // wave
    this.setString(idx, this.waveHeader.wave, bufferView);
    idx += 4;
    // fmt
    this.setString(idx, this.waveHeader.fmtChunkMarker, bufferView);
    idx += 4;
    // fmt size
    bufferView.setInt32(idx, this.waveHeader.fmtSize, true);
    idx += 4;
    // format type
    bufferView.setInt16(idx, this.waveHeader.formatType, true);
    idx += 2;
    // channels
    bufferView.setInt16(idx, this.waveHeader.channels, true);
    idx += 2;
    // sample rate
    bufferView.setInt32(idx, this.waveHeader.sampleRate, true);
    idx += 4;
    // byte rate
    bufferView.setInt32(idx, this.waveHeader.byteRate, true);
    idx += 4;
    // block align
    bufferView.setInt16(idx, this.waveHeader.blockAlign, true);
    idx += 2;
    // bits per sample
    bufferView.setInt16(idx, this.waveHeader.bitsPerSample, true);
    idx += 2;
    // data
    this.setString(idx, this.waveHeader.dataChunkMarker, bufferView);
    idx += 4;
    // data size
    bufferView.setInt32(idx, this.waveHeader.dataSize, true);

    let path = this.context.filesDir + '/output.wav'; // output wav file path
    let inputFile: fileIo.File | undefined;
    let outputFile: fileIo.File | undefined;
    try {
      inputFile = fileIo.openSync(pcmFilePath, fileIo.OpenMode.READ_ONLY);
      outputFile = fileIo.openSync(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.TRUNC | fileIo.OpenMode.WRITE_ONLY);
      // write wav header
      fileIo.writeSync(outputFile.fd, buffer);
      // write pcm data
      let readSize = 0;
      let readBuf = new ArrayBuffer(1024 * 1024);
      do {
        readSize = fileIo.readSync(inputFile.fd, readBuf);
        fileIo.writeSync(outputFile.fd, readBuf, { length: readSize });
      } while (readSize > 0);
    } catch (err) {
      console.error(`Failed to write file, ${JSON.stringify(err)}`);
    } finally {
      if (inputFile) {
        fileIo.closeSync(inputFile);
      }
      if (outputFile) {
        fileIo.closeSync(outputFile);
      }
    }
  }
}

class AVPlayerDemo {
  private context: Context;
  private avPlayer: media.AVPlayer | undefined;

  constructor(context: Context) {
    this.context = context;
    media.createAVPlayer((error: BusinessError, video: media.AVPlayer) => {
      if (video != null) {
        this.avPlayer = video;
        console.info('Succeeded in creating AVPlayer');
      } else {
        console.error(`Failed to create AVPlayer, error message:${error.message}`);
      }
    });
  }

  // 注册avplayer回调函数
  setAVPlayerCallback(avPlayer: media.AVPlayer) {
    // seek操作结果回调函数
    avPlayer.on('seekDone', (seekDoneTime: number) => {
      console.info(`AVPlayer seek succeeded, seek time is ${seekDoneTime}`);
    });
    // error回调监听函数,当avPlayer在操作过程中出现错误时调用 reset接口触发重置流程
    avPlayer.on('error', (err: BusinessError) => {
      console.error(`Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`);
      avPlayer.reset(); // 调用reset重置资源，触发idle状态
    });
    // 状态机变化回调函数
    avPlayer.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
      switch (state) {
        case 'idle': // 成功调用reset接口后触发该状态机上报
          console.info('AVPlayer state idle called.');
          console.info(`${reason}`);
          avPlayer.release(); // 调用release接口销毁实例对象
          break;
        case 'initialized': // avplayer 设置播放源后触发该状态上报
          console.info('AVPlayer state initialized called.');
          let rendererInfo: audio.AudioRendererInfo = {
            usage: audio.StreamUsage.STREAM_USAGE_VOICE_COMMUNICATION, // 音频流使用类型
            rendererFlags: 0 // 音频渲染器标志
          };
          this.avPlayer!.audioRendererInfo = rendererInfo;
          avPlayer.prepare();
          break;
        case 'prepared': // prepare调用成功后上报该状态机
          console.info('AVPlayer state prepared called.');
          avPlayer.play(); // 调用播放接口开始播放
          break;
        case 'playing': // play成功调用后触发该状态机上报
          console.info('AVPlayer state playing called.');
          break;
        case 'paused': // pause成功调用后触发该状态机上报
          console.info('AVPlayer state paused called.');
          // avPlayer.play(); // 再次播放接口开始播放
          break;
        case 'completed': // 播放结束后触发该状态机上报
          console.info('AVPlayer state completed called.');
          // avPlayer.stop(); // 调用播放结束接口
          break;
        case 'stopped': // stop接口成功调用后触发该状态机上报
          console.info('AVPlayer state stopped called.');
          // avPlayer.reset(); // 调用reset接口初始化avplayer状态
          break;
        case 'released':
          console.info('AVPlayer state released called.');
          this.avPlayer = await media.createAVPlayer();
          this.avPlayer.prepare();
          break;
        default:
          console.info('AVPlayer state unknown called.');
          break;
      }
    });
  }

  async avPlayerUrlDemo() {
    this.avPlayer = await media.createAVPlayer();
    // 创建状态机变化回调函数
    this.setAVPlayerCallback(this.avPlayer!);
    let fdPath = 'fd://';
    // 通过UIAbilityContext获取沙箱地址filesDir，以Stage模型为例。
    let path = this.context.filesDir + '/output.wav';
    // 打开相应的资源文件地址获取fd，并为url赋值触发initialized状态机上报。
    let file = await fs.open(path);
    fdPath = fdPath + '' + file.fd;
    this.avPlayer.url = fdPath;
  }
  async release() {
    this.avPlayer?.release();
  }
}
```

## 常见FAQ

Q：AVPlayer支持多种播放格式，为什么转码的时候会优先转为WAV格式？

A：WAV是一种无损的格式，转码方式简单，并且本身的支持度高，可以达到较高的质量要求，而MP3等是有损的格式，会牺牲音频文件质量来换取较小的体积，为尽量保证音频质量，一般会选择转码为WAV格式。
