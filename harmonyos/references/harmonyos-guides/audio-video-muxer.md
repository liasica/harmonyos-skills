---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-video-muxer
title: 媒体数据封装
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 媒体数据封装与解析 > 媒体数据封装
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:caee16dfe515e98a9956eef1f298aedf557065108d553eca88c20ac9c5665469
---

开发者可以调用本模块的Native API接口，完成音视频封装，即将音频、视频等编码后的媒体数据，按一定的格式存储到文件里。

当前支持的封装能力请参考[AVCodec支持的格式](avcodec-support-formats.md#媒体数据封装)。

如果需要对HDRVivid视频码流进行封装，需要配置MimeType为H265 (OH\_AVCODEC\_MIMETYPE\_VIDEO\_HEVC)，本功能从API version 11开始支持。

**适用场景**

* 录像、录音

  保存录像、录音文件时，需要先对音视频流进行编码，再封装为文件。
* 音视频编辑

  完成编辑后的音视频，需要封装为文件。
* 音视频转码

  转码后，保存文件时需要封装。

## 开发指导

详细的API说明请参考[native\_avmuxer.h](../harmonyos-references/capi-native-avmuxer-h.md)。

说明

如果调用封装模块写本地文件，需要[向用户申请授权](request-user-authorization.md)：ohos.permission.READ\_MEDIA, ohos.permission.WRITE\_MEDIA。

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libnative_media_avmuxer.so)
2. target_link_libraries(sample PUBLIC libnative_media_core.so)
```

### 开发步骤

参考以下示例代码，完成音视频封装的全流程。以封装mp4格式的音视频文件为例。

不同的封装格式需要配置的key请参考[AVCodec支持的格式](avcodec-support-formats.md#媒体数据封装)。

1. 添加头文件。

   ```
   1. #include <multimedia/player_framework/native_avmuxer.h>
   2. #include <multimedia/player_framework/native_avcodec_base.h>
   3. #include <multimedia/player_framework/native_avformat.h>
   4. #include <multimedia/player_framework/native_avbuffer.h>
   5. #include <fcntl.h>
   ```
2. 调用OH\_AVMuxer\_Create()创建封装器实例对象。

   ```
   1. // 设置封装格式为mp4。
   2. OH_AVOutputFormat format = AV_OUTPUT_FORMAT_MPEG_4;
   3. // 以读写方式创建fd。
   4. int32_t fd = open("test.mp4", O_CREAT | O_RDWR | O_TRUNC, S_IRUSR | S_IWUSR);
   5. OH_AVMuxer *muxer = OH_AVMuxer_Create(fd, format);
   ```
3. （可选）调用OH\_AVMuxer\_SetRotation()设置旋转角度。

   ```
   1. // 旋转角度，视频画面需要旋转的时候设置。
   2. OH_AVMuxer_SetRotation(muxer, 0);
   ```
4. 添加文件级数据。

   文件级数据已定义的key详见[AVCodec支持的格式](avcodec-support-formats.md#媒体数据封装)。

   用户自定义的key必须以"com.openharmony."为开头。值类型可以为int32\_t、float、string，从API20开始增加支持uint8\_t\*。

   说明

   已定义的key必须在OH\_AVMuxer\_Start()前设置，用户自定义的key可以在OH\_AVMuxer\_Stop()前设置。

   ```
   1. OH_AVFormat *format = OH_AVFormat_Create(); // 用OH_AVFormat_Create创建format。

   3. // 设置已定义的key。
   4. OH_AVFormat_SetStringValue(format, OH_MD_KEY_CREATION_TIME, "2024-12-28T00:00:00:000000Z"); // 从API14开始支持设置创建时间（使用ISO 8601标准的时间格式且为UTC时间）。
   5. OH_AVFormat_SetStringValue(format, OH_MD_KEY_COMMENT, "comment test"); // 从API20开始支持设置评论。值类型为string。
   6. OH_AVFormat_SetIntValue(format, OH_MD_KEY_ENABLE_MOOV_FRONT, 1); // 从API20开始支持设置moov元数据是否前置。默认值为0，设置1代表前置。

   8. // 设置用户自定义key（需要com.openharmony.开头）。
   9. OH_AVFormat_SetIntValue(format, "com.openharmony.testInt", 1024); // 值类型为int32_t。
   10. OH_AVFormat_SetFloatValue(format, "com.openharmony.testFloat", 1.024); // 值类型为float。
   11. OH_AVFormat_SetStringValue(format, "com.openharmony.testString", "string test"); // 值类型为string，长度不超过256。
   12. uint8_t testData[] = {1, 2, 3};
   13. OH_AVFormat_SetBuffer(format, "com.openharmony.testBuffer", testData, sizeof(testData)); // 从API20开始支持值类型为uint8_t*。

   15. int ret = OH_AVMuxer_SetFormat(muxer, format); // 设置封装的format。
   16. if (ret != AV_ERR_OK) {
   17. // 设置format失败，未找到有效待写入的key数据。
   18. }
   19. OH_AVFormat_Destroy(format); // 销毁。
   ```
5. 添加音频轨。

   **方法一：用OH\_AVFormat\_Create创建format**

   ```
   1. int audioTrackId = -1;
   2. uint8_t *buffer = ...; // 编码config data，如果没有可以不传。
   3. size_t size = ...;  // 编码config data的长度，根据实际情况配置。
   4. OH_AVFormat *formatAudio = OH_AVFormat_Create(); // 用OH_AVFormat_Create创建format，这里以封装44100Hz采样率、2声道的AAC-LC音频为例。
   5. OH_AVFormat_SetStringValue(formatAudio, OH_MD_KEY_CODEC_MIME, OH_AVCODEC_MIMETYPE_AUDIO_AAC); // 必填。
   6. OH_AVFormat_SetIntValue(formatAudio, OH_MD_KEY_AUD_SAMPLE_RATE, 44100); // 必填。
   7. OH_AVFormat_SetIntValue(formatAudio, OH_MD_KEY_AUD_CHANNEL_COUNT, 2); // 必填。
   8. OH_AVFormat_SetIntValue(formatAudio, OH_MD_KEY_PROFILE, AAC_PROFILE_LC); // 选填。
   9. OH_AVFormat_SetBuffer(formatAudio, OH_MD_KEY_CODEC_CONFIG, buffer, size); // 选填。

   11. int ret = OH_AVMuxer_AddTrack(muxer, &audioTrackId, formatAudio);
   12. if (ret != AV_ERR_OK || audioTrackId < 0) {
   13. // 音频轨添加失败。
   14. }
   15. OH_AVFormat_Destroy(formatAudio); // 销毁。
   ```

   **方法二：用OH\_AVFormat\_CreateAudioFormat创建format**

   ```
   1. int audioTrackId = -1;
   2. uint8_t *buffer = ...; // 编码config data，如果没有可以不传。
   3. size_t size = ...;  // 编码config data的长度，根据实际情况配置。
   4. OH_AVFormat *formatAudio = OH_AVFormat_CreateAudioFormat(OH_AVCODEC_MIMETYPE_AUDIO_AAC, 44100, 2);
   5. OH_AVFormat_SetIntValue(formatAudio, OH_MD_KEY_PROFILE, AAC_PROFILE_LC); // 选填。
   6. OH_AVFormat_SetBuffer(formatAudio, OH_MD_KEY_CODEC_CONFIG, buffer, size); // 选填。

   8. int ret = OH_AVMuxer_AddTrack(muxer, &audioTrackId, formatAudio);
   9. if (ret != AV_ERR_OK || audioTrackId < 0) {
   10. // 音频轨添加失败。
   11. }
   12. OH_AVFormat_Destroy(formatAudio); // 销毁。
   ```
6. 添加视频轨。

   说明

   * 当开发者需要设置色彩信息时，必须保证OH\_MD\_KEY\_COLOR\_PRIMARIES、OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS、OH\_MD\_KEY\_MATRIX\_COEFFICIENTS三个key设置的值都在其各自的参数范围内，系统才会识别这是有效色彩信息数据。参数设置范围可参考[OH\_ColorPrimary](../harmonyos-references/capi-native-avcodec-base-h.md#oh_colorprimary)、[OH\_TransferCharacteristic](../harmonyos-references/capi-native-avcodec-base-h.md#oh_transfercharacteristic)和[OH\_MatrixCoefficient](../harmonyos-references/capi-native-avcodec-base-h.md#oh_matrixcoefficient)。
   * 当开发者输入的色彩信息与视频码流的参数集中的色彩信息不一致时，系统以视频码流中的色彩信息为准。

   **方法一：用OH\_AVFormat\_Create创建format**

   ```
   1. int videoTrackId = -1;
   2. uint8_t *buffer = ...; // 编码config data，如果没有可以不传。
   3. size_t size = ...;  // 编码config data的长度，根据实际情况配置。
   4. OH_AVFormat *formatVideo = OH_AVFormat_Create();
   5. OH_AVFormat_SetStringValue(formatVideo, OH_MD_KEY_CODEC_MIME, OH_AVCODEC_MIMETYPE_VIDEO_AVC); // 必填。
   6. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_WIDTH, 1280); // 必填。
   7. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_HEIGHT, 720); // 必填。
   8. OH_AVFormat_SetBuffer(formatVideo, OH_MD_KEY_CODEC_CONFIG, buffer, size); // 选填。
   9. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_COLOR_PRIMARIES, OH_ColorPrimary::COLOR_PRIMARY_BT709); // 色彩信息，选填。
   10. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_TRANSFER_CHARACTERISTICS, OH_TransferCharacteristic::TRANSFER_CHARACTERISTIC_BT709); // 色彩信息，选填。
   11. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_MATRIX_COEFFICIENTS, OH_MatrixCoefficient::MATRIX_COEFFICIENT_BT709); // 色彩信息，选填。
   12. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_RANGE_FLAG, 1); // 色彩信息，选填。值为0代表limited range，值为1代表full range。

   14. int ret = OH_AVMuxer_AddTrack(muxer, &videoTrackId, formatVideo);
   15. if (ret != AV_ERR_OK || videoTrackId < 0) {
   16. // 视频轨添加失败。
   17. }
   18. OH_AVFormat_Destroy(formatVideo); // 销毁。
   ```

   **方法二：用OH\_AVFormat\_CreateVideoFormat创建format**

   ```
   1. int videoTrackId = -1;
   2. uint8_t *buffer = ...; // 编码config data，如果没有可以不传。
   3. size_t size = ...;  // 编码config data的长度，根据实际情况配置。
   4. OH_AVFormat *formatVideo = OH_AVFormat_CreateVideoFormat(OH_AVCODEC_MIMETYPE_VIDEO_AVC, 1280, 720);
   5. OH_AVFormat_SetBuffer(formatVideo, OH_MD_KEY_CODEC_CONFIG, buffer, size); // 选填。
   6. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_COLOR_PRIMARIES, OH_ColorPrimary::COLOR_PRIMARY_BT709); // 色彩信息，选填。
   7. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_TRANSFER_CHARACTERISTICS, OH_TransferCharacteristic::TRANSFER_CHARACTERISTIC_BT709); // 色彩信息，选填。
   8. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_MATRIX_COEFFICIENTS, OH_MatrixCoefficient::MATRIX_COEFFICIENT_BT709); // 色彩信息，选填。
   9. OH_AVFormat_SetIntValue(formatVideo, OH_MD_KEY_RANGE_FLAG, 1); // 色彩信息，选填。值为0代表limited range，值为1代表full range。

   11. int ret = OH_AVMuxer_AddTrack(muxer, &videoTrackId, formatVideo);
   12. if (ret != AV_ERR_OK || videoTrackId < 0) {
   13. // 视频轨添加失败。
   14. }
   15. OH_AVFormat_Destroy(formatVideo); // 销毁。
   ```
7. 添加辅助轨。

   说明

   设置OH\_MD\_KEY\_TRACK\_TYPE时，值为MEDIA\_TYPE\_AUXILIARY代表添加辅助轨。

   设置OH\_MD\_KEY\_TRACK\_REFERENCE\_TYPE时，值必须为"hint"、"cdsc"、"font"、"hind"、"vdep"、"vplx"、"subt"、"thmb"、"auxl"、"cdtg"、"shsc"或"aest"其中一项。

   设置OH\_MD\_KEY\_TRACK\_DESCRIPTION时，值必须为"com.openharmony."开头且长度不超过256的字符串。

   设置OH\_MD\_KEY\_REFERENCE\_TRACK\_IDS时，track id值必须大于等于0，且必须是已经存在的track id。

   **添加音频辅助轨**

   ```
   1. int32_t audioAuxlTrackId = -1;
   2. std::vector<int32_t> audioTrackIDsVector = {0}; // 根据实际情况设置被辅助音频轨的编号，可填写多个值。
   3. int32_t *audioAuxlTrackIDs = audioTrackIDsVector.data();
   4. OH_AVFormat *audioAuxlFormat = OH_AVFormat_Create();
   5. OH_AVFormat_SetStringValue(audioAuxlFormat, OH_MD_KEY_CODEC_MIME, OH_AVCODEC_MIMETYPE_AUDIO_AAC); // 必填。
   6. OH_AVFormat_SetIntValue(audioAuxlFormat, OH_MD_KEY_AUD_SAMPLE_RATE, 44100); // 必填。
   7. OH_AVFormat_SetIntValue(audioAuxlFormat, OH_MD_KEY_AUD_CHANNEL_COUNT, 2); // 必填。
   8. OH_AVFormat_SetIntValue(audioAuxlFormat, OH_MD_KEY_PROFILE, AAC_PROFILE_LC); // 选填。
   9. OH_AVFormat_SetIntValue(audioAuxlFormat, OH_MD_KEY_TRACK_TYPE, static_cast<int32_t>(OH_MediaType::MEDIA_TYPE_AUXILIARY)); // 必填。
   10. OH_AVFormat_SetStringValue(audioAuxlFormat, OH_MD_KEY_TRACK_REFERENCE_TYPE, "auxl"); // 必填。
   11. OH_AVFormat_SetStringValue(audioAuxlFormat, OH_MD_KEY_TRACK_DESCRIPTION, "com.openharmony.audiomode.auxiliary"); // 必填。
   12. OH_AVFormat_SetIntBuffer(audioAuxlFormat, OH_MD_KEY_REFERENCE_TRACK_IDS, audioAuxlTrackIDs, audioTrackIDsVector.size()); // 必填。

   14. int ret = OH_AVMuxer_AddTrack(muxer, &audioAuxlTrackId, audioAuxlFormat);
   15. if (ret != AV_ERR_OK || audioAuxlTrackId < 0) {
   16. // 音频辅助轨添加失败。
   17. }
   ```

   **添加视频辅助轨**

   ```
   1. int32_t videoAuxlTrackId = -1;
   2. std::vector<int32_t> videoTrackIDsVector = {0}; // 根据实际情况设置被辅助视频轨的编号，可填写多个值。
   3. int32_t *videoAuxlTrackIDs = videoTrackIDsVector.data();
   4. OH_AVFormat *videoAuxlFormat = OH_AVFormat_Create();
   5. OH_AVFormat_SetStringValue(videoAuxlFormat, OH_MD_KEY_CODEC_MIME, OH_AVCODEC_MIMETYPE_VIDEO_AVC); // 必填。
   6. OH_AVFormat_SetIntValue(videoAuxlFormat, OH_MD_KEY_WIDTH, 1280); // 必填。
   7. OH_AVFormat_SetIntValue(videoAuxlFormat, OH_MD_KEY_HEIGHT, 720); // 必填。
   8. OH_AVFormat_SetIntValue(videoAuxlFormat, OH_MD_KEY_TRACK_TYPE, static_cast<int32_t>(OH_MediaType::MEDIA_TYPE_AUXILIARY)); // 必填。
   9. OH_AVFormat_SetStringValue(videoAuxlFormat, OH_MD_KEY_TRACK_REFERENCE_TYPE, "vdep"); // 必填。
   10. OH_AVFormat_SetStringValue(videoAuxlFormat, OH_MD_KEY_TRACK_DESCRIPTION, "com.openharmony.moviemode.depth"); // 必填。
   11. OH_AVFormat_SetIntBuffer(videoAuxlFormat, OH_MD_KEY_REFERENCE_TRACK_IDS, videoAuxlTrackIDs, videoTrackIDsVector.size()); // 必填。

   13. int ret = OH_AVMuxer_AddTrack(muxer, &videoAuxlTrackId, videoAuxlFormat);
   14. if (ret != AV_ERR_OK || videoAuxlTrackId < 0) {
   15. // 视频辅助轨添加失败。
   16. }
   ```
8. 添加封面轨。

   **方法一：用OH\_AVFormat\_Create创建format**

   ```
   1. int coverTrackId = -1;
   2. OH_AVFormat *formatCover = OH_AVFormat_Create();
   3. OH_AVFormat_SetStringValue(formatCover, OH_MD_KEY_CODEC_MIME, OH_AVCODEC_MIMETYPE_IMAGE_JPG);
   4. OH_AVFormat_SetIntValue(formatCover, OH_MD_KEY_WIDTH, 1280);
   5. OH_AVFormat_SetIntValue(formatCover, OH_MD_KEY_HEIGHT, 720);

   7. int ret = OH_AVMuxer_AddTrack(muxer, &coverTrackId, formatCover);
   8. if (ret != AV_ERR_OK || coverTrackId < 0) {
   9. // 添加封面失败。
   10. }
   11. OH_AVFormat_Destroy(formatCover); // 销毁。
   ```

   **方法二：用OH\_AVFormat\_CreateVideoFormat创建format**

   ```
   1. int coverTrackId = -1;
   2. OH_AVFormat *formatCover = OH_AVFormat_CreateVideoFormat(OH_AVCODEC_MIMETYPE_IMAGE_JPG, 1280, 720);

   4. int ret = OH_AVMuxer_AddTrack(muxer, &coverTrackId, formatCover);
   5. if (ret != AV_ERR_OK || coverTrackId < 0) {
   6. // 添加封面失败。
   7. }
   8. OH_AVFormat_Destroy(formatCover); // 销毁。
   ```
9. 调用OH\_AVMuxer\_Start()开始封装。

   ```
   1. // 调用start，写封装文件头。start后，不能设置媒体参数、不能添加音视频轨。
   2. if (OH_AVMuxer_Start(muxer) != AV_ERR_OK) {
   3. // 异常处理。
   4. }
   ```
10. 调用OH\_AVMuxer\_WriteSampleBuffer()，写入封装数据。

    封装数据包括视频、音频、封面等数据。

    ```
    1. // start后，才能开始写入数据。
    2. int size = ...;
    3. OH_AVBuffer *sample = OH_AVBuffer_Create(size); // 创建AVBuffer。
    4. // 通过OH_AVBuffer_GetAddr(sample)往sampleBuffer里写入数据参考OH_AVBuffer的使用方法。
    5. // 封装封面，必须一次写完一张图片。

    7. // 创建buffer info。
    8. OH_AVCodecBufferAttr info = {0};
    9. info.pts = ...; // 当前数据的开始播放的时间，单位微秒，相对时间。
    10. info.size = size; // 当前数据的长度。
    11. info.offset = 0; // 偏移，一般为0。
    12. info.flags |= AVCODEC_BUFFER_FLAGS_SYNC_FRAME; // 当前数据的标志。具体参考OH_AVCodecBufferFlags。
    13. info.flags |= AVCODEC_BUFFER_FLAGS_CODEC_DATA; // 当annex-b格式的avc包含codec config的标志。
    14. OH_AVBuffer_SetBufferAttr(sample, &info); // 设置buffer的属性。
    15. int trackId = audioTrackId; // 选择写的音视频轨。

    17. int ret = OH_AVMuxer_WriteSampleBuffer(muxer, trackId, sample);
    18. if (ret != AV_ERR_OK) {
    19. // 异常处理。
    20. }
    ```
11. 调用OH\_AVMuxer\_Stop()，停止封装。

    ```
    1. // 调用stop，写封装文件尾。stop后不能写入媒体数据。
    2. if (OH_AVMuxer_Stop(muxer) != AV_ERR_OK) {
    3. // 异常处理。
    4. }
    ```
12. 调用OH\_AVMuxer\_Destroy()销毁实例，释放资源。

    注意不能重复销毁，否则将会导致程序崩溃。

    ```
    1. if (OH_AVMuxer_Destroy(muxer) != AV_ERR_OK) {
    2. // 异常处理。
    3. }
    4. muxer = NULL;
    5. close(fd); // 关闭文件描述符。
    ```
