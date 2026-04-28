---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-ohavsession-developer
title: 媒体会话提供方(C/C++)
breadcrumb: 指南 > 媒体 > AVSession Kit（音视频播控服务） > 本地媒体会话 > 媒体会话提供方(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:36246ccabca527097dbab8c31edaca3ab7b2c2089c49760b73cee097c0a77277
---

OHAVSession系统提供的通过使用C API实现媒体会话提供方，从而在媒体会话控制方（例如播控中心）中展示媒体相关信息，及响应媒体会话控制方下发的播控命令。

## 使用入门

开发者使用[native\_avsession.h](../harmonyos-references/capi-native-avsession-h.md)实现媒体会话，需要添加对应的头文件。

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(entry PUBLIC libohavsession.so)
```

### 添加头文件

```
1. #include <multimedia/av_session/native_avmetadata.h>
2. #include <multimedia/av_session/native_avsession.h>
3. #include <multimedia/av_session/native_avsession_errors.h>
```

## 开发步骤及注意事项

开发者可以通过以下几个步骤在NDK接入本地会话。

1. 创建会话并激活媒体，需要传入会话类型AVSession\_Type，自定义的TAG，以及应用的包名、ability名字。

   ```
   1. OH_AVSession* avsession;
   2. OH_AVSession_Create(SESSION_TYPE_AUDIO, "testsession", "com.example.application", "MainAbility", &avsession);
   3. OH_AVSession_Activate(avsession);
   ```

   AVSession\_Type包含如下四种类型：

   * SESSION\_TYPE\_AUDIO
   * SESSION\_TYPE\_VIDEO
   * SESSION\_TYPE\_VOICE\_CALL
   * SESSION\_TYPE\_VIDEO\_CALL
2. 应用内播放对应的媒体资源时，同步设置媒体元数据信息。

   要设置元数据，需使用OH\_AVMetadataBuilder构造具体的数据，生成一个OH\_AVMetadata。生成OH\_AVMetadata后，使用OH\_AVMetadata的各个功能接口进行资源的设置。

   使用OH\_AVMetadataBuilder构造元数据示例：

   ```
   1. // 创建OH_AVMetadataBuilder构造器。
   2. OH_AVMetadataBuilder* builder;
   3. OH_AVMetadataBuilder_Create(&builder);

   5. OH_AVMetadata* ohMetadata;
   6. OH_AVMetadataBuilder_SetTitle(builder, "Anonymous title");
   7. OH_AVMetadataBuilder_SetArtist(builder, "Anonymous artist");
   8. OH_AVMetadataBuilder_SetAuthor(builder, "Anonymous author");
   9. OH_AVMetadataBuilder_SetAlbum(builder, "Anonymous album");
   10. OH_AVMetadataBuilder_SetWriter(builder, "Anonymous writer");
   11. OH_AVMetadataBuilder_SetComposer(builder, "Anonymous composer");
   12. OH_AVMetadataBuilder_SetDuration(builder, DURATION_TIME); // DURATION_TIME = 3600
   13. // MediaImageUri只支持网络地址。
   14. OH_AVMetadataBuilder_SetMediaImageUri(builder, "https://xxx.xxx.xx");
   15. OH_AVMetadataBuilder_SetSubtitle(builder, "Anonymous subtitle");
   16. OH_AVMetadataBuilder_SetDescription(builder, "For somebody");
   17. // Lyric只支持媒体歌词内容（应用需将歌词内容拼接为一个字符串传入）。
   18. OH_AVMetadataBuilder_SetLyric(builder, "balabala");
   19. OH_AVMetadataBuilder_SetAssetId(builder, "000");
   20. OH_AVMetadataBuilder_SetSkipIntervals(builder, SECONDS_30);
   21. OH_AVMetadataBuilder_SetDisplayTags(builder,  AVSESSION_DISPLAYTAG_AUDIO_VIVID);

   23. /**
   24. * generate an AVMetadata 构造AVMetadata对象
   25. */
   26. OH_AVMetadataBuilder_GenerateAVMetadata(builder, &ohMetadata);

   28. /**
   29. * set AVMetadata 设置AVMetadata对象
   30. */
   31. OH_AVSession_SetAVMetadata(avsession, ohMetadata);
   ```

   在不使用AVMetadata之后，开发者应该执行OH\_AVMetadataBuilder\_Destroy接口来销毁元数据，且不要继续使用。

   ```
   1. OH_AVMetadata_Destroy(ohMetadata);
   2. OH_AVMetadataBuilder_Destroy(builder);
   ```
3. 跟随媒体播放状态的变化，及时更新媒体播放状态。

   媒体播放状态，包含状态值、播放位置、播放速度、收藏状态等，可以按需使用对应的接口进行设置。

   ```
   1. AVSession_ErrCode ret = AV_SESSION_ERR_SUCCESS;

   3. // 设置播放状态，其中state范围应为[0,11]。
   4. AVSession_PlaybackState state = PLAYBACK_STATE_PREPARING;
   5. ret = OH_AVSession_SetPlaybackState(avsession, state);
   6. // ...

   8. // 设置播放位置。
   9. AVSession_PlaybackPosition* playbackPosition = new AVSession_PlaybackPosition;
   10. playbackPosition->elapsedTime = ELAPSED_TIME; // ELAPSED_TIME = 1000
   11. playbackPosition->updateTime = UPDATE_TIME; // UPDATE_TIME = 16111150
   12. ret = OH_AVSession_SetPlaybackPosition(avsession, playbackPosition);
   ```
4. 注册播控命令事件监听，便于响应用户通过媒体会话控制方，例如播控中心下发的播控命令。

   说明

   媒体会话提供方在注册相关固定播控命令事件监听时，监听的事件会在媒体会话控制方的getValidCommands()方法中体现，即媒体会话控制方认为该方法有效，因此在需要时会触发相应的事件。为了保证媒体会话控制方下发的播控命令可以被正常执行，媒体会话提供方请勿进行无逻辑的空实现监听。

   调用注册接口后，在业务结束时需要调用取消注册接口，避免出现异常。

   Session侧目前支持的播控命令包括：

   * 播放
   * 暂停
   * 停止
   * 上一首
   * 下一首
   * 快退
   * 快进
   * 设置进度
   * 设置收藏

   ```
   1. // 设置播放/暂停/停止/上一首/下一首回调。
   2. // CONTROL_CMD_PLAY = 0; 播放。
   3. // CONTROL_CMD_PAUSE = 1; 暂停。
   4. // CONTROL_CMD_STOP = 2;  停止。
   5. // CONTROL_CMD_PLAY_NEXT = 3; 下一首。
   6. // CONTROL_CMD_PLAY_PREVIOUS = 4; 上一首。
   7. AVSession_ControlCommand command = CONTROL_CMD_PLAY;
   8. OH_AVSessionCallback_OnCommand commandCallback = [](OH_AVSession* session, AVSession_ControlCommand command,
   9. void* userData) -> AVSessionCallback_Result {
   10. return AVSESSION_CALLBACK_RESULT_SUCCESS;
   11. };
   12. int userData = 0;
   13. OH_AVSession_RegisterCommandCallback(avsession, command, commandCallback, (void *)(&userData));

   15. // 设置快进回调。
   16. OH_AVSessionCallback_OnFastForward fastForwardCallback = [](OH_AVSession* session, uint32_t seekTime,
   17. void* userData) -> AVSessionCallback_Result {
   18. return AVSESSION_CALLBACK_RESULT_SUCCESS;
   19. };
   20. OH_AVSession_RegisterForwardCallback(avsession, fastForwardCallback, (void *)(&userData));
   ```

   相关回调接口如下：

   | 接口 | 说明 |
   | --- | --- |
   | OH\_AVSession\_RegisterCommandCallback(OH\_AVSession\* avsession, AVSession\_ControlCommand command, OH\_AVSessionCallback\_OnCommand callback, void\* userData) | 注册通用播控的回调，支持：播放、暂停、停止、上一首、下一首回调。 |
   | OH\_AVSession\_RegisterForwardCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnFastForward callback, void\* userData) | 注册快进的回调。 |
   | OH\_AVSession\_RegisterRewindCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnRewind callback, void\* userData) | 注册快退的回调。 |
   | OH\_AVSession\_RegisterSeekCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnSeek callback, void\* userData) | 注册跳转的回调。 |
   | OH\_AVSession\_RegisterToggleFavoriteCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnToggleFavorite callback, void\* userData) | 注册收藏的回调。 |
5. 音视频应用在退出，并且不需要继续播放时，及时取消监听以及销毁媒体会话释放资源。示例代码如下所示：

   ```
   1. OH_AVSession_Destroy(avsession);
   ```
