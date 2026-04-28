---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audiovivid-avdemuxer
title: Audio Vivid解封装
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > Audio Vivid能力 > Audio Vivid解封装
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ac6c54f7fbe8a9227172b368f5ec49ef969e43a97424c070d84277e4c9ed7320
---

获取到Audio Vivid封装的mp4文件后，先调用解封装相关接口，选中音频轨，读取每一帧Audio Vivid，送入解码器中（可参考[Audio Vivid解码](audiovivid-audiodecoder.md)）。详细的API请参考[AVDemuxer模块](../harmonyos-references/capi-avdemuxer.md)。

## 在CMake脚本中链接到动态库

```
1. target_link_libraries(sample PUBLIC
2. libnative_media_codecbase.so libnative_media_core.so
3. libnative_media_acodec.so libnative_media_avdemuxer.so libnative_media_avsource.so
4. )
```

## 添加头文件

```
1. //解封装头文件
2. #include "multimedia/player_framework/native_avdemuxer.h"
3. #include <string.h>

5. // 解封装解码传递信息结构体
6. struct AudioSampleInfo {
7. std::string audioCodecMime = "";
8. int32_t audioSampleFormat = 0;
9. int32_t audioSampleRate = 0;
10. int32_t audioChannelCount = 0;
11. int64_t audioChannelLayout = 0;
12. uint8_t audioCodecConfig[100] = {0};
13. size_t audioCodecSize = 0;
14. };

16. AudioSampleInfo  info;
```

## 开发步骤

1. 创建解封装实例。

   ```
   1. // ts code获取fd和size
   2. let inputFile = fs.openSync(filepath,fs.OpenMode.READ_ONLY);
   3. if (inputFile) {
   4. let inputFileState = fs.statSync(inputFile.fd);
   5. let inputFileSize = inputFileState.size;
   6. }
   ```

   ```
   1. //C++ code
   2. OH_AVSource *source = OH_AVSource_CreateWithFD(inputFd,0,inputFileSize);
   3. OH_AVDemuxer *demuxer = OH_AVDemuxer_CreateWithSource(source);
   4. auto sourceFormat = std::shared_ptr<OH_AVFormat>(OH_AVSource_GetSourceFormat(source_), OH_AVFormat_Destroy);
   5. int32_t trackCount = 0;
   6. OH_AVFormat_GetIntValue(sourceFormat.get(), OH_MD_KEY_TRACK_COUNT, &trackCount);
   ```
2. 选中音频轨。

   ```
   1. int32_t trackCount = 0;
   2. OH_AVFormat_GetIntValue(sourceFormat.get(), OH_MD_KEY_TRACK_COUNT, &trackCount);
   3. for (int32_t index = 0; index < trackCount; index++) {
   4. int trackType = -1;
   5. auto trackFormat =
   6. std::shared_ptr<OH_AVFormat>(OH_AVSource_GetTrackFormat(source_, index), OH_AVFormat_Destroy);
   7. // 获取轨道类型
   8. OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_TRACK_TYPE, &trackType);
   9. // 判断当前轨道为音频轨
   10. if (trackType == MEDIA_TYPE_AUD) {
   11. // 选中音频轨
   12. OH_AVDemuxer_SelectTrackByID(demuxer, index);
   13. // 获取位深
   14. OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_AUDIO_SAMPLE_FORMAT, &info.audioSampleFormat);
   15. // 获取声道数
   16. OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_AUD_CHANNEL_COUNT, &info.audioChannelCount);
   17. // 获取声道布局
   18. OH_AVFormat_GetLongValue(trackFormat.get(), OH_MD_KEY_CHANNEL_LAYOUT, &info.audioChannelLayout);
   19. // 获取采样率
   20. OH_AVFormat_GetIntValue(trackFormat.get(), OH_MD_KEY_AUD_SAMPLE_RATE, &info.audioSampleRate);
   21. // 获取额外配置信息
   22. uint8_t *addr = nullptr;
   23. OH_AVFormat_GetBuffer(trackFormat.get(), OH_MD_KEY_CODEC_CONFIG, &addr, &info.audioCodecSize);
   24. memcpy((void *)info.audioCodecConfig, (void *)addr, info.audioCodecSize);
   25. // 获取解码器类型
   26. char *audioCodecMime;
   27. OH_AVFormat_GetStringValue(trackFormat.get(), OH_MD_KEY_CODEC_MIME, const_cast<char const **>(&audioCodecMime));
   28. info.audioCodecMime = audioCodecMime;
   29. int32_t trackId = index;
   30. break;
   31. }
   32. }
   ```
3. 读取每一帧数据。

   ```
   1. OH_AVBuffer *buffer;
   2. int32_t ret = OH_AVDemuxer_ReadSampleBuffer(demuxer, trackId, buffer);
   ```
4. 释放解封装实例。

   ```
   1. int32_t Release()
   2. {
   3. if (demuxer != nullptr) {
   4. OH_AVDemuxer_Destroy(demuxer);
   5. demuxer = nullptr;
   6. }
   7. if (source != nullptr) {
   8. OH_AVSource_Destroy(source);
   9. source = nullptr;
   10. }
   11. return AVCODEC_SAMPLE_ERR_OK;
   12. }
   ```
