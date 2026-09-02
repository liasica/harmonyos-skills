---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audiovivid-avdemuxer
title: Audio Vivid解封装
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > Audio Vivid能力 > Audio Vivid解封装
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5dc7cb9682263b53e7f162686fa8818957c7fd3362dfab8f6b57ae20e9206b9e
---

获取到Audio Vivid封装的mp4文件后，先调用解封装相关接口，选中音频轨，读取每一帧Audio Vivid，送入解码器中（可参考[Audio Vivid解码](audiovivid-audiodecoder.md)）。详细的API请参考[AVDemuxer模块](../harmonyos-references/capi-avdemuxer.md)。

## 在CMake脚本中链接到动态库

```cmake
target_link_libraries(sample PUBLIC
libnative_media_codecbase.so libnative_media_core.so
libnative_media_acodec.so libnative_media_avdemuxer.so libnative_media_avsource.so
)
```

## 添加头文件

```
//解封装头文件
#include "multimedia/player_framework/native_avdemuxer.h"
#include <string.h>

// 解封装解码传递信息结构体
struct AudioSampleInfo {
std::string audioCodecMime = "";
int32_t audioSampleFormat = 0;
int32_t audioSampleRate = 0;
int32_t audioChannelCount = 0;
int64_t audioChannelLayout = 0;
uint8_t audioCodecConfig[100] = {0};
size_t audioCodecSize = 0;
};

AudioSampleInfo  info;
```

## 开发步骤

1. 创建解封装实例。

   ```ts
   // ts code获取fd和size
   let inputFile = fs.openSync(filepath,fs.OpenMode.READ_ONLY);
   if (inputFile) {
       let inputFileState = fs.statSync(inputFile.fd);
       let inputFileSize = inputFileState.size;
   }
   ```

   ```
   //C++ code
   OH_AVSource *source = OH_AVSource_CreateWithFD(inputFd,0,inputFileSize);
   OH_AVDemuxer *demuxer = OH_AVDemuxer_CreateWithSource(source);
   auto sourceFormat = std::shared_ptr<OH_AVFormat>(OH_AVSource_GetSourceFormat(source_), OH_AVFormat_Destroy);
   int32_t trackCount = 0;
   OH_AVFormat_GetIntValue(sourceFormat.get(), OH_MD_KEY_TRACK_COUNT, &trackCount);
   ```
2. 选中音频轨。

   ```
   int32_t trackCount = 0;
   OH_AVFormat_GetIntValue(sourceFormat.get(), OH_MD_KEY_TRACK_COUNT, &trackCount);
   for (int32_t index = 0; index < trackCount; index++) {
   int trackType = -1;
   auto trackFormat =
       std::shared_ptr<OH_AVFormat>(OH_AVSource_GetTrackFormat(source_, index), OH_AVFormat_Destroy);
   // 获取轨道类型
   OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_TRACK_TYPE, &trackType);
   // 判断当前轨道为音频轨
   if (trackType == MEDIA_TYPE_AUD) {
       // 选中音频轨
       OH_AVDemuxer_SelectTrackByID(demuxer, index);
       // 获取位深
       OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_AUDIO_SAMPLE_FORMAT, &info.audioSampleFormat);
       // 获取声道数
       OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_AUD_CHANNEL_COUNT, &info.audioChannelCount);
       // 获取声道布局
       OH_AVFormat_GetLongValue(trackFormat.get(), OH_MD_KEY_CHANNEL_LAYOUT, &info.audioChannelLayout);
       // 获取采样率
       OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_AUD_SAMPLE_RATE, &info.audioSampleRate);
       // 获取额外配置信息
       uint8_t *addr = nullptr;
       OH_AVFormat_GetBuffer(trackFormat.get(), OH_MD_KEY_CODEC_CONFIG, &addr, &info.audioCodecSize);
       memcpy((void *)info.audioCodecConfig, (void *)addr, info.audioCodecSize);
       // 获取解码器类型
       char *audioCodecMime;
       OH_AVFormat_GetStringValue(trackFormat.get(), OH_MD_KEY_CODEC_MIME, const_cast<char const **>(&audioCodecMime));
       info.audioCodecMime = audioCodecMime;
       int32_t trackId = index;
       break;
       }
   }
   ```
3. 读取每一帧数据。

   ```
   OH_AVBuffer *buffer;
   int32_t ret = OH_AVDemuxer_ReadSampleBuffer(demuxer, trackId, buffer);
   ```
4. 释放解封装实例。

   ```
   int32_t Release()
   {
       if (demuxer != nullptr) {
           OH_AVDemuxer_Destroy(demuxer);
           demuxer = nullptr;
       }
       if (source != nullptr) {
           OH_AVSource_Destroy(source);
           source = nullptr;
       }
       return AVCODEC_SAMPLE_ERR_OK;
   }
   ```
