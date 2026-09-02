---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-media-40
title: 如何获得音频比特率
breadcrumb: FAQ > 媒体开发 > 音频和视频 > 媒体（Media ） > 如何获得音频比特率
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:45+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:81ef6b5b22d091da6a2396292fdea6e2609d4f2afed53d8998846070188bb411
---

## 问题现象

如何获得多个音频轨道里每一个音频轨的比特率。

## 背景知识

* [AVMetadataExtractor](../harmonyos-references/arkts-apis-media-avmetadataextractor.md)可以实现从原始媒体资源中获取元数据[AVMetadata](../harmonyos-references/arkts-apis-media-i.md#avmetadata11)。其中[AVMetadata](../harmonyos-references/arkts-apis-media-i.md#avmetadata11).tracks为媒体资源的轨道信息。
* [AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)用于实现端到端播放原始媒体资源。[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md).[getTrackDescription](../harmonyos-references/arkts-apis-media-avplayer.md#gettrackdescription9)用于获得音视频媒体资源的轨道信息。
* 媒体资源的轨道信息使用[MediaDescription](../harmonyos-references/arkts-apis-media-i.md#mediadescription8)表示，通过key-value方式获取媒体信息。[MediaDescriptionKey](../harmonyos-references/arkts-apis-media-e.md#mediadescriptionkey8).MD\_KEY\_TRACK\_TYPE表示轨道类型，[MediaDescriptionKey](../harmonyos-references/arkts-apis-media-e.md#mediadescriptionkey8).MD\_KEY\_BITRATE表示比特率。

## 解决方案

方案一：使用[AVMetadataExtractor](../harmonyos-references/arkts-apis-media-avmetadataextractor.md)调用[fetchMetadata](../harmonyos-references/arkts-apis-media-avmetadataextractor.md#fetchmetadata11)接口获得元数据[AVMetadata](../harmonyos-references/arkts-apis-media-i.md#avmetadata11)。通过[AVMetadata](../harmonyos-references/arkts-apis-media-i.md#avmetadata11).tracks属性获得媒体资源的轨道信息，遍历轨道信息，从音频轨信息中获得对应比特率。

```ts
try {
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  avMetadataExtractor.fdSrc = await context.resourceManager.getRawFd('video.mp4');
  let metadata: media.AVMetadata = await avMetadataExtractor.fetchMetadata();
  if (metadata.tracks) {
    for (const track of metadata.tracks) {
      if (track[media.MediaDescriptionKey.MD_KEY_TRACK_TYPE] === media.MediaType.MEDIA_TYPE_AUD) {
        let trackIdx: number = track[media.MediaDescriptionKey.MD_KEY_TRACK_INDEX] as number;
        let bitrate: number = track[media.MediaDescriptionKey.MD_KEY_BITRATE] as number;
        console.info(`Audio Track ${trackIdx} bitrate is ${bitrate}`);
      }
    }
  }
  await avMetadataExtractor.release();
} catch (error) {
  console.error(`failed to get audio bitrate by AVMetadataExtractor: ${JSON.stringify(error)}`);
}
```

方案二：使用[AVPlayer](../harmonyos-references/arkts-apis-media-avplayer.md)在prepared/playing/paused状态下调用[getTrackDescription](../harmonyos-references/arkts-apis-media-avplayer.md#gettrackdescription9)接口获得音视频的轨道信息，遍历轨道信息，从音频轨信息中获得对应比特率。

```ts
try {
  let avPlayer: media.AVPlayer = await media.createAVPlayer();
  avPlayer.on('stateChange', async (state: media.AVPlayerState) => {
    switch (state) {
      case 'initialized':
        await avPlayer.prepare();
        break;
      case 'prepared':
        let tracks: Array<media.MediaDescription> = await avPlayer.getTrackDescription();
        for (const track of tracks) {
          if (track[media.MediaDescriptionKey.MD_KEY_TRACK_TYPE] === media.MediaType.MEDIA_TYPE_AUD) {
            let trackIdx: number = track[media.MediaDescriptionKey.MD_KEY_TRACK_INDEX] as number;
            let bitrate: number = track[media.MediaDescriptionKey.MD_KEY_BITRATE] as number;
            console.info(`Audio Track ${trackIdx} bitrate is ${bitrate}`);
          }
        }
        await avPlayer.release();
        break;
      case 'error':
        await avPlayer.release();
        break;
    }
  });
  let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
  avPlayer.fdSrc = await context.resourceManager.getRawFd('video.mp4');
} catch (error) {
  console.error(`failed to get audio bitrate by AVMetadataExtractor: ${JSON.stringify(error)}`);
}
```

完成参考代码如下：

```ts
import { media } from '@kit.MediaKit';
import { common } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  build() {
    Column({ space: 20 }) {
      Button('AVMetadataExtractor')
        .padding(5)
        .fontSize(30)
        .onClick(async () => {
          try {
            let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
            let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            avMetadataExtractor.fdSrc = await context.resourceManager.getRawFd('video.mp4');
            let metadata: media.AVMetadata = await avMetadataExtractor.fetchMetadata();
            if (metadata.tracks) {
              for (const track of metadata.tracks) {
                if (track[media.MediaDescriptionKey.MD_KEY_TRACK_TYPE] === media.MediaType.MEDIA_TYPE_AUD) {
                  let trackIdx: number = track[media.MediaDescriptionKey.MD_KEY_TRACK_INDEX] as number;
                  let bitrate: number = track[media.MediaDescriptionKey.MD_KEY_BITRATE] as number;
                  console.info(`Audio Track ${trackIdx} bitrate is ${bitrate}`);
                }
              }
            }
            await avMetadataExtractor.release();
          } catch (error) {
            console.error(`failed to get audio bitrate by AVMetadataExtractor: ${JSON.stringify(error)}`);
          }
        });

      Button('AVPlayer')
        .padding(5)
        .fontSize(30)
        .onClick(async () => {
          try {
            let avPlayer: media.AVPlayer = await media.createAVPlayer();
            avPlayer.on('stateChange', async (state: media.AVPlayerState) => {
              switch (state) {
                case 'initialized':
                  await avPlayer.prepare();
                  break;
                case 'prepared':
                  let tracks: Array<media.MediaDescription> = await avPlayer.getTrackDescription();
                  for (const track of tracks) {
                    if (track[media.MediaDescriptionKey.MD_KEY_TRACK_TYPE] === media.MediaType.MEDIA_TYPE_AUD) {
                      let trackIdx: number = track[media.MediaDescriptionKey.MD_KEY_TRACK_INDEX] as number;
                      let bitrate: number = track[media.MediaDescriptionKey.MD_KEY_BITRATE] as number;
                      console.info(`Audio Track ${trackIdx} bitrate is ${bitrate}`);
                    }
                  }
                  await avPlayer.release();
                  break;
                case 'error':
                  await avPlayer.release();
                  break;
              }
            });
            let context: Context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            avPlayer.fdSrc = await context.resourceManager.getRawFd('video.mp4');
          } catch (error) {
            console.error(`failed to get audio bitrate by AVMetadataExtractor: ${JSON.stringify(error)}`);
          }
        });
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
