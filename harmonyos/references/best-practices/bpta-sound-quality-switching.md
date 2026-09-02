---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-sound-quality-switching
title: 音质切换开发实践
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 音质切换开发实践
category: best-practices
scraped_at: 2026-09-02T15:03:17+08:00
doc_updated_at: 2026-04-01
content_hash: sha256:f84918a8de8cb2e518761e73b795764da330d88b46b3664f07b261f16330c86f
---

## 概述

在音乐播放应用中，同一首歌曲在不同音质间的切换是一种常见功能，而音频文件的压缩方式是影响音质的关键因素之一。下表展示了不同压缩方式对应的音质对比：

| 类型 | 代表格式 | 播放能力支持 | 特点 |
| --- | --- | --- | --- |
| 未压缩 | PCM/WAV | PCM：AudioRenderer  WAV：AVPlayer | 高保真、体积大 |
| 无损压缩 | FLAC/APE | AVPlayer | 可还原原始数据 |
| 有损压缩 | MP3/AAC | AVPlayer | 体积小、音质损失 |

音质可以在未压缩、无损压缩和有损压缩之间切换，根据上述播放能力支持范围可以看出，音质切换的本质为[AudioRenderer](../harmonyos-references/arkts-apis-audio-audiorenderer.md)与[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)的播放切换，以及AVPlayer与AVPlayer的播放切换（即使用AVPlayer在不同音频格式间的播放切换）。

本文将介绍以下两种音质切换场景的实现：

* [AudioRenderer与AVPlayer播放切换](bpta-sound-quality-switching.md#section1718774317213)
* [AVPlayer与AVPlayer播放切换](bpta-sound-quality-switching.md#section198441182235)

## AudioRenderer与AVPlayer播放切换

### 场景描述

本场景以同一音频文件的PCM格式与MP3格式之间进行切换播放为例，切换后保持音频播放进度一致，即无缝衔接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/CQogdDMsT7e4kJK62qw3GQ/zh-cn_image_0000002490682592.gif "点击放大")

### 实现原理

1. 使用AudioRenderer播放PCM文件，即MP3音质（标清）切换到无损未压缩的PCM音质时，通过跳转的时间戳计算出新的offset偏移位置，待下次读取音频数据时，从该offset偏移位置开始读取，AudioRenderer即可实现跳转至指定位置播放。
2. 使用AVPlayer播放MP3文件，即无损未压缩的PCM音质切换到MP3音质（标清）时，通过AVPlayer的[seek()](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)接口可直接跳转到对应时间戳位置播放。

### 开发步骤

1. 在MediaTools类中，定义如下方法：
   * msToCountdownTime()：根据当前毫秒数转换为分钟格式。
   * getMsFromByteLength()：根据字节长度转化为播放时间长度。
   * getOffsetFromTime()：根据播放时间长度转化为字节长度。

   ```typescript
   export class MediaTools {
     // ...

     static msToCountdownTime(ms: number): string {
       if (!ms) {
         return '00:00';
       }
       const days = Math.floor(ms / (1000 * 60 * 60 * 24));
       const hours = Math.floor((ms % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
       const minutes = Math.floor((ms % (1000 * 60 * 60)) / (1000 * 60));
       const seconds = Math.floor((ms % (1000 * 60)) / 1000);
       return `${(days ? MediaTools.fill(days) + ':' : '')}${(hours ? MediaTools.fill(hours) + ':' : '')}
         ${MediaTools.fill(minutes)}:${MediaTools.fill(seconds)} `.trim();
     }

     static getMsFromByteLength(byteLength: number): number {
       return 1000 * (byteLength / SECOND_BUFFER_WALK);
     }

     static getOffsetFromTime(curMs: number) {
       return (curMs / 1000) * SECOND_BUFFER_WALK;
     }
   }
   ```
2. 在AVPlayerController类中，定义如下方法：
   * reset()：在其中调用AVPlayer实例的[reset()](../harmonyos-references/arkts-apis-media-avplayer.md#reset9)方法，重置播放。
   * pause()：在其中调用AVPlayer实例的[pause()](../harmonyos-references/arkts-apis-media-avplayer.md#pause9-1)方法，暂停播放。
   * seek()：在其中调用AVPlayer实例的[seek()](../harmonyos-references/arkts-apis-media-avplayer.md#seek9)，跳转播放。

   ```typescript
   export class AVPlayerController {
     // ...

     reset(fd: number, offset: number, length: number): void {
       this.currentTime = AppStorage.get('progress') as number;
       this.isReset = true;
       this.avPlayer?.reset(() => {
         if (this.avPlayer != undefined) {
           this.avPlayer.fdSrc = { fd: fd, offset: offset, length: length };
         }
       })
     }
     // ...

     // Pause playback
     pause(): void {
       this.avPlayer?.pause().catch(() => {
         Logger.error('AVPlayerController pause error!');
       })
     }

     // Jump to playback
     seek(currentTime: number): void {
       this.avPlayer?.seek(currentTime, media.SeekMode.SEEK_NEXT_SYNC);
     }
     // ...
   }
   ```
3. 在AudioRendererController类中，定义如下方法：
   * initAudioRenderer()：初始化，获取AudioRenderer实例。
   * setWriteDataCallback()：写入音频数据。
   * start()：在其中调用AudioRenderer的[start()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#start8)方法，启动音频渲染器。
   * pause()：在其中调用AudioRenderer的[pause()](../harmonyos-references/arkts-apis-audio-audiorenderer.md#pause8)方法，暂停音频渲染。
   * seek()：自定义seek()方法保存当前播放进度、时间的转换和字节长度，用于AudioRenderer跳转播放。

   ```typescript
   export class AudioRendererController {
     // ...
     // Initialization AudioRenderer
     public async initAudioRenderer(fd: number, offset: number, length: number): Promise<void> {
       this.fd = fd; // File descriptor
       this.offset = offset; // Start offset
       this.currentOffset = offset; // Current offset
       this.length = length; // File length
       // Audio stream information
       let audioStreamInfo: audio.AudioStreamInfo = {
         samplingRate: audio.AudioSamplingRate.SAMPLE_RATE_48000, // Audio file sampling rate
         channels: audio.AudioChannel.CHANNEL_2, // Number of audio file channels
         sampleFormat: audio.AudioSampleFormat.SAMPLE_FORMAT_S16LE, // Audio sampling format
         encodingType: audio.AudioEncodingType.ENCODING_TYPE_RAW // Audio encoding format
       };
       // AudioRenderer information
       let audioRendererInfo: audio.AudioRendererInfo = {
         usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // Audio stream usage type
         rendererFlags: 0 // Audio renderer flag
       };
       // AudioRenderer options information
       let audioRendererOptions: audio.AudioRendererOptions = {
         streamInfo: audioStreamInfo,
         rendererInfo: audioRendererInfo
       };
       // Get audio renderer
       await audio.createAudioRenderer(audioRendererOptions).then((data) => {
         this.audioRenderer = data;
         if (this.audioRenderer !== undefined) {
           try {
             // Set the focus model to independent focus mode
             this.audioRenderer.setInterruptMode(audio.InterruptMode.INDEPENDENT_MODE);
             this.setWriteDataCallback(); // Write audio data
           } catch (error) {
             Logger.error('createAudioRenderer is calling.');
           }
         }
       });
       // Convert the file length to the corresponding number of milliseconds and store it in AppStorage.
       AppStorage.setOrCreate('progressMax', MediaTools.getMsFromByteLength(this.length));
       // Convert the file length to the corresponding number of milliseconds, then convert it to a timestamp and store it in AppStorage.
       AppStorage.setOrCreate('totalTime', MediaTools.msToCountdownTime(MediaTools.getMsFromByteLength(this.length)));
     }

     // Write audio data
     private setWriteDataCallback(): void {
       try {
         // Listening for audio data writing
         this.audioRenderer?.on('writeData', (buffer) => {
           if (this.currentOffset - this.offset >= this.length) {
             this.currentOffset = this.offset;
             this.seek(0);
           }
           let options: ReadOptions = {
             offset: this.currentOffset,
             length: buffer.byteLength
           };
           let bufferLength = fileIo.readSync(this.fd, buffer, options);
           this.currentOffset += buffer.byteLength;
           let processOffset = this.currentOffset - this.offset;

           if (this.offset + this.length <= this.currentOffset) {
             let view = new DataView(buffer);
             Logger.info('currentOffset ：' + this.currentOffset + '  endOffset:' + (this.offset + this.length) +
               ' bufferLength:' + bufferLength);
             for (let i = bufferLength - 1; i > processOffset - this.length; i--) {
               view.setUint8(i, 0);
             }
           }

           let curMs = MediaTools.getMsFromByteLength(processOffset);
           AppStorage.setOrCreate('progress', curMs);
           AppStorage.setOrCreate('currentTime', MediaTools.msToCountdownTime(curMs));
         })
       } catch (error) {
         Logger.error('setWriteDataCallback is failed. ' + error);
       }
     }

     public async start(): Promise<void> {
       if (this.audioRenderer !== undefined) {
         // Audio state
         let stateGroup = [audio.AudioState.STATE_PREPARED, audio.AudioState.STATE_PAUSED, audio.AudioState.STATE_STOPPED];
         if (stateGroup.indexOf(this.audioRenderer.state.valueOf()) === -1) {
           return;
         }
         // Starting the AudioRenderer
         this.audioRenderer.start((err: BusinessError) => {
           // ...
         });
       }
     }

     public pause(): void {
       if (this.audioRenderer !== undefined) {
         if (this.audioRenderer.state.valueOf() !== audio.AudioState.STATE_RUNNING) {
           return;
         }
        // Pause Audio rendering
         this.audioRenderer.pause((err: BusinessError) => {
           // ...
         });
       }
     }
     // Jump to playback
     public seek(ms: number): void {
       this.curMs = ms;
       AppStorage.setOrCreate('progress', this.curMs);
       AppStorage.setOrCreate('currentTime', MediaTools.msToCountdownTime(this.curMs));
       this.currentOffset = this.offset + MediaTools.getOffsetFromTime(this.curMs);
     }
     // ...
   }
   ```
4. 在PlayerController类中，定义如下方法：
   * changeType()：传入[RawFileDescriptor](../harmonyos-references/js-apis-resource-manager.md#rawfiledescriptor9)音频资源描述符，并通过audioType的值，判断使用AudioRenderer或AVPlayer播放音频。
   * seek()：通过判断isAVPlayer()返回值，调用AVPlayerController或AudioRendererController对应的seek()方法，用于跳转指定位置播放音频资源。
   * isAVPlayer()：用于判断是否使用AVPlayer播放音频资源。

   ```typescript
   export class PlayerController {
     // ...
     // Modifying the audio format
     changeType(rawFileDescriptor: resourceManager.RawFileDescriptor, audioType: AudioType) {
       try {
         this.rawFileDescriptor = rawFileDescriptor;
         if (audioType === 1 || audioType === 2) {
           this.audioRendererController?.pause(); // Pause AudioRenderer playback
           // Reset AVPlayer playback
           this.avPlayerController?.reset(this.rawFileDescriptor.fd, this.rawFileDescriptor.offset,
             this.rawFileDescriptor.length);
         } else {
           this.avPlayerController?.pause(); // Pause AVPlayer playback
           if (this.audioRendererController === undefined) {
             this.audioRendererController = new AudioRendererController();
           }
           // Create an AudioRenderer instance and listen for audio data writing
           this.audioRendererController.initAudioRenderer(this.rawFileDescriptor.fd, this.rawFileDescriptor.offset,
             this.rawFileDescriptor.length).then(() => {
             this.audioRendererController?.start(); // Start AudioRenderer audio render
           });
         }
         this.currentType = audioType;
       } catch (error) {
         Logger.error('changeType error!');
       }
     }
     // ...
     // Determine the return value of isAVPlayer() and call the corresponding seek() method
     seek(currentTime: number): void {
       if (this.isAVPlayer()) {
         this.avPlayerController?.seek(currentTime);
       } else {
         this.audioRendererController?.seek(currentTime);
       }
     }
     // ...
     // Determine whether to use AVPlayer for playback
     isAVPlayer(): boolean {
       return this.currentType === 1 || this.currentType === 2;
     }
   }
   ```
5. 在页面中自定义changeType()事件，通过[getRawfd()](../harmonyos-references/js-apis-resource-manager.md#getrawfd9-1)获取resources/rawfile目录下的音频资源，将获取到的数据传入PlayerController的changeType()方法，调用playerController的seek()方法传入当前Slider进度的值，用于跳转播放。

   ```typescript
   private changeType(songSrc: string, audioType: AudioType): void {
     let current: number = this.value;
     this.getUIContext().getHostContext()?.resourceManager.getRawFd(songSrc).then((rawFileDescriptor) => {
       this.playerController.changeType(rawFileDescriptor, audioType);
       this.playerController.seek(current);
     }).catch((error: BusinessError) => {
       Logger.error(`resourceManager error code ${error.code} message ${error.message}`);
     });
   }
   ```

   通过给对应MenuItem子组件添加对应点击事件，在其中调用changeType()方法传入音频资源文件路径和对应音频格式audioType，实现音频资源PCM格式与MP3格式的切换播放，即AudioRenderer与AVPlayer切换播放。

   ```typescript
   Menu() {
     MenuItem({
       content: $r('app.string.standard_quality'),
     }).onClick(() => {
       if (this.index === 0) {
         return;
       }
       this.text = $r('app.string.standard_quality');
       this.index = 0;
       this.changeType(this.songData.src + AudioName.MP3, AudioType.MP3);
       this.isPlay = true;
     })
     // ...
     MenuItem({
       content: $r('app.string.pcm_high_quality'),
     })
       .onClick(() => {
         if (this.index === 2) {
           return;
         }
         this.text = $r('app.string.pcm_high_quality');
         this.index = 2;
         this.changeType(this.songData.src + AudioName.PCM, AudioType.PCM);
         this.isPlay = true;
       })
   }
   // ...
   ```

## AVPlayer与AVPlayer播放切换

### 场景描述

本场景以同一音频文件的FLAC格式与MP3格式之间进行切换播放为例，切换后保持音频播放进度一致，即无缝衔接。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/lFmQcSYlRFuBePZ4m8urNA/zh-cn_image_0000002522762335.gif "点击放大")

### 实现原理

使用同一个AVPlayer实例播放FLAC文件和MP3文件，每次切换后对AVPlayer进行重置，重新设置音频资源url，然后通过AVPlayer的seek()接口直接跳转到对应时间戳位置播放。

### 开发步骤

1. 在MenuItem组件的点击事件中调用自定义changeType()方法，传入音频资源文件路径和对应音频格式audioType。

   ```typescript
   Menu() {
     MenuItem({
       content: $r('app.string.standard_quality'),
     }).onClick(() => {
       if (this.index === 0) {
         return;
       }
       this.text = $r('app.string.standard_quality');
       this.index = 0;
       this.changeType(this.songData.src + AudioName.MP3, AudioType.MP3);
       this.isPlay = true;
     })
     MenuItem({
       content: $r('app.string.flac_high_quality'),
     })
       .onClick(() => {
         if (this.index === 1) {
           return;
         }
         this.text = $r('app.string.flac_high_quality');
         this.index = 1;
         this.changeType(this.songData.src + AudioName.FLAC, AudioType.FLAC);
         this.isPlay = true;
       })
     // ...
   }
   // ...
   ```
2. 同样的，在页面自定义changeType()事件中，通过getRawfd()获取音频资源，将获取到的数据传入PlayerController的changeType()方法，调用playerController的seek()方法传入当前Slider进度值，用于跳转播放。

   ```typescript
   private changeType(songSrc: string, audioType: AudioType): void {
     let current: number = this.value;
     this.getUIContext().getHostContext()?.resourceManager.getRawFd(songSrc).then((rawFileDescriptor) => {
       this.playerController.changeType(rawFileDescriptor, audioType);
       this.playerController.seek(current);
     }).catch((error: BusinessError) => {
       Logger.error(`resourceManager error code ${error.code} message ${error.message}`);
     });
   }
   ```
3. 在PlayerController的changeType()方法中：
   1. 通过传入的audioType的值，判断音频是否为MP3或FLAC格式。
   2. 调用audioRendererController的pause()方法，暂停AudioRenderer音频渲染。
   3. 通过avPlayerController的reset()方法重置音频资源的描述符、偏移量和文件长度，实现音频资源FLAC格式与MP3格式的切换播放，即AVPlayer与AVPlayer切换播放。

   ```typescript
   export class PlayerController {
     // ...
     // Modifying the audio format
     changeType(rawFileDescriptor: resourceManager.RawFileDescriptor, audioType: AudioType) {
       try {
         this.rawFileDescriptor = rawFileDescriptor;
         if (audioType === 1 || audioType === 2) {
           this.audioRendererController?.pause(); // Pause AudioRenderer playback
           // Reset AVPlayer playback
           this.avPlayerController?.reset(this.rawFileDescriptor.fd, this.rawFileDescriptor.offset,
             this.rawFileDescriptor.length);
         } else {
           // ...
         }
         this.currentType = audioType;
       } catch (error) {
         Logger.error('changeType error!');
       }
     }
     // ...
     // Determine the return value of isAVPlayer() and call the corresponding seek() method
     seek(currentTime: number): void {
       if (this.isAVPlayer()) {
         this.avPlayerController?.seek(currentTime);
       } else {
         // ...
       }
     }
     // ...
   }
   ```

## 示例代码

* [实现音质切换](https://gitcode.com/harmonyos_samples/audio-format-switch)
