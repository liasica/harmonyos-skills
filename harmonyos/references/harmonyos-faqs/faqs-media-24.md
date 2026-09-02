---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-24
title: SoundPool音频播放不完整不流畅
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > SoundPool音频播放不完整不流畅
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:44+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2662f230f95b72414b5bdb7e0ce705a857150e67b26a0a86e68e45633476139b
---

## 问题现象

SoundPool播放音频文件时会出现如下问题：

* 音频文件稍微大时会出现播放不完整。
* 触发音频播放后没立即播放或不流畅。
* 乐器等场景音频资源超过32个会播放失败。

## 背景知识

* [SoundPool](../harmonyos-guides/using-soundpool-for-playback.md)（音频池）接口可以实现低时延短音播放，如相机快门音效、系统通知音效等，实现一次加载，多次低时延播放。

* SoundPool支持的音频播放格式如下：

  | 音频容器规格 | 规格描述 |
  | --- | --- |
  | m4a | 音频格式：AAC。 |
  | aac | 音频格式：AAC。 |
  | mp3 | 音频格式：MP3。 |
  | ogg | 音频格式：VORBIS。 |
  | wav | 音频格式：PCM。 |
* 使用接口[createSoundPool](../harmonyos-references/arkts-apis-media-f.md#mediacreatesoundpool10)创建音频池实例，当API 18以下版本，创建的SoundPool对象底层为单实例模式，一个应用进程只能够创建1个SoundPool实例。当API 18及API 18以上版本，创建的SoundPool对象底层为多实例模式，一个应用进程最多能够创建128个SoundPool实例。

## 问题定位

* 检查音频资源的大小是否满足SoundPool接口要求。
  + SoundPool当前支持播放解码后1MB以下的音频资源，解码后大小超过1MB的长音频将截取前面的1MB大小数据进行播放，这相当于44.1kHz的16bit位深的立体声下约5.6秒的音频时长（在较低采样率或单声道配置下，持续时间会相应延长）。
  + 可通过如下日志计算解码后的播放时长。
  1. 搜索日志”CacheBuffer stream write finish, cacheDataFrameIndex\_:“，获取资源大小cacheDataFrameIndex\_，buffer大小length。
  2. 搜索日志”audioRenderer normal stop.|audioRenderer fast renderer pause.“。若出现”audioRenderer normal stop.“，表示普通通路，buffer写入间隔=20ms。若出现”audioRenderer fast renderer pause.“，表示低时延通路，buffer写入间隔=5ms。
  3. 计算播放时长，单位为ms：播放时长=资源大小/buffer大小\*buffer写入间隔。

  ```screen
  10-28 14:50:41.901   com.examp...graphics  I     [IncSoundData][[102076]RendererInClient] channel: 2, L=1630, R=1661, counts: 400
  10-28 14:50:43.905   com.examp...graphics  I     [IncSoundData][[102076]RendererInClient] channel: 2, L=3776, R=3873, counts: 500
  10-28 14:50:44.864   com.examp...graphics  I     #362 CacheBuffer stream write finish, cacheDataFrameIndex_:1050624, havePlayedCount_:0, loop:0, streamID_:1, length: 1920
  10-28 14:50:44.865   com.examp...graphics  I     #449 CacheBuffer::Stop soundID_:1, streamID:1
  10-28 14:50:44.866   com.examp...graphics  I     #463 audioRenderer normal stop.
  10-28 14:50:44.866   com.examp...graphics  I     StreamClientState for Renderer::Stop. id: 102076
  10-28 14:50:44.866   com.examp...graphics  I     [WriteUnderrunEvent]AudioRendererPrivate WriteUnderrunEvent!
  10-28 14:50:44.866   com.examp...graphics  I     [StopAudioStream]Stop begin for sessionId 102076 uid: 20020275
  ```

* 音频资源未加载完成。SoundPool是预解析的，播放前资源必须先[load](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#load)加载完毕，即收到[on('loadComplete')](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#onloadcomplete)回调之后再执行play操作。

  ```ts
  loadCallback(soundPool: media.SoundPool) {
    soundPool.on('loadComplete', (soundId: number) => {
      console.info('loadComplete, soundId: ' + soundId);
    });
  }
  ```
* SoundPool实例的最大播放流数是32个，预加载资源的数量放宽到了128个。
  + 当加载更多音频资源时会加载报错“5400102 load sound failed”。
  + 当需要加载更多音频时，可以将之前加载的空闲音频通过[unload](../harmonyos-references/js-apis-inner-multimedia-soundpool.md#unload)卸载掉（注意不是release释放实例），继续加载新的音频播放。以下代码示例展示了加载“rawfile/soundpool”目录下所有音频进行播放及卸载：

    ```ts
    import { media } from '@kit.MediaKit';
    import { audio } from '@kit.AudioKit';
    import { BusinessError } from '@kit.BasicServicesKit';

    let soundPool: media.SoundPool;

    @ObservedV2
    class SoundFile {
      @Trace
      filename: string = '';
      @Trace
      soundId: number = -1;

      constructor(filename: string, soundId: number) {
        this.filename = filename;
        this.soundId = soundId;
      }
    }

    @Builder
    export function PageBuilder() {
      TestPage();
    }

    @Entry
    @ComponentV2
    struct TestPage {
      private context: Context = this.getUIContext().getHostContext() as Context;
      @Local soundFilesArr: Array<SoundFile> = new Array();

      async aboutToAppear(): Promise<void> {
        await this.create();
      }

      build() {
        NavDestination() {
          Column({ space: 2 }) {
            List({ space: 2 }) {
              ForEach(this.soundFilesArr, (item: SoundFile, index: number) => {
                ListItem() {
                  Row({ space: 1 }) {
                    Text(index + 1 + '-' + item.filename);
                    Button('加载')
                      .onClick(async () => {
                        await this.load(item.filename);
                      })
                    Button(`播放${item.soundId > 0 ? 'Ready' : 'UnReady'}`)
                      .onClick(async () => {
                        await this.play(item.soundId);
                      })
                    Button('卸载')
                      .onClick(async () => {
                        await this.unload(item.filename, item.soundId);
                      })
                  }
                }
              })
            }
            .width('100%')
            .height('100%')
          }
          .width('100%')
          .height('100%')
        }
      }

      async create() {
        // 创建soundPool实例
        let audioRendererInfo: audio.AudioRendererInfo = {
          usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置，参考StreamUsage
          rendererFlags: 1 // 音频渲染器标志
        };
        try {
          soundPool = await media.createSoundPool(32, audioRendererInfo);
        } catch (error) {
          console.error('load raw file error ' + JSON.stringify(error));
        }

        this.loadCallback(soundPool); // 监听loadComplete
        await this.scanRawFile(); // 扫描rawfile音频资源
      }

      async scanRawFile() {
        try {
          let resourceManager = this.context.resourceManager;
          let files = await resourceManager.getRawFileList('soundpool/'); //确保目录存在，并包含音频文件
          for (let i = 0; i < files.length; i++) {
            let soundFile: SoundFile = new SoundFile(files[i], -1);
            this.soundFilesArr.push(soundFile);
          }
        } catch (error) {
          console.error('getRawFileList error' + JSON.stringify(error));
        }
      }

      async load(fileName: string) {
        try {
          let rowFd = await this.context.resourceManager.getRawFd('soundpool/' + fileName);
          console.info('file uri: ' + fileName + ',' + rowFd.fd);
          await soundPool.load(rowFd.fd, rowFd.offset, rowFd.length).then((soundId) => {
            this.updListArrSoundId(fileName, soundId);
          })
            .catch((e: BusinessError) => {
              console.error('load sound err: ', e.code, e.message);
            });
        } catch (error) {
          console.error('load raw file error' + JSON.stringify(error));
        }
      }

      async play(soundId: number) {
        // 开始播放，这边play也可带播放的参数PlayParameters，请在音频资源加载完毕，即收到loadComplete回调之后再执行play操作
        await soundPool.play(soundId).then(async (streamId: number) => {
          console.info('play sound success soundid:' + soundId, streamId);
        }, (err: BusinessError) => {
          console.info(`play sound Error: errCode is ${err.code}, errMessage is ${err.message}`);
        });
      }

      async unload(fileName: string, soundId: number) {
        soundPool.unload(soundId, (error: BusinessError) => {
          if (error) {
            console.error(`Failed to unload soundPool: errCode is ${error.code}, errMessage is ${error.message}`, soundId);
          } else {
            console.info('Succceeded in unload soundPool', soundId);
            this.updListArrSoundId(fileName, -1);
          }
        });
      }

      loadCallback(soundPool: media.SoundPool) {
        soundPool.on('loadComplete', (soundId: number) => {
          console.info('loadComplete, soundId: ' + soundId);
        });
      }

      updListArrSoundId(fileName: string, soundId: number) {
        // 更新list记录soundId
        this.soundFilesArr.forEach((soundFile) => {
          if (soundFile.filename == fileName) {
            soundFile.soundId = soundId;
          }
        });
      };
    }
    ```

## 分析结论

当音频不满足组件规格，或者未正确使用播放组件时，会造成SoundPool音频播放异常。

## 修改建议

使用SoundPool音频播放时，需正确按照组件规格进行调用，并遵守SoundPool播放顺序，详情参考官网[完整示例](../harmonyos-guides/using-soundpool-for-playback.md#运行示例工程)。

1. 创建SoundPool实例。
2. 加载音频资源。
3. 设置播放参数（循环模式/播放优先级等）。
4. 播放控制（播放/停止）。
5. 释放资源。

## 常见FAQ

Q：SoundPool支持暂停后继续播放吗？

A：目前不支持。

Q：SoundPool当前支持播放解码后1MB以下的音频资源，有个1MB以下的MP3音频播放时为什么被截取？

A：MP3是常见的压缩率优良的音频编码格式，可以使用FFmpeg工具将MP3文件解码为WAV格式（WAV是一种未压缩的音频格式），通过查看WAV文件大小获取MP3音频解码后的大小，从而判断MP3音频资源是否符合SoundPool的使用要求。
