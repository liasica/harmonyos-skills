---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-video-demuxer
title: 媒体数据解析
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 媒体数据封装与解析 > 媒体数据解析
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:55aa043d53e4b051d0f28563a2c518dd0324423c9ec9b0d0b11ddba374827a7b
---

开发者可以调用本模块的Native API接口，完成媒体数据的解封装相关操作，即从比特流数据中取出音频、视频、字幕等媒体sample，获得DRM相关信息。

当前支持的数据输入类型有：远程连接(http协议)和文件描述符(fd)。

当前支持的解封装格式请参考[AVCodec支持的格式](avcodec-support-formats.md#媒体数据解析)。

**适用场景**：

* 播放

  播放媒体文件时，需要先对媒体流进行解封装，然后使用解封装获取的sample进行解码和播放。
* 音视频编辑

  编辑媒体文件时，需要先对媒体流进行解封装，获取到指定sample进行编辑。
* 媒体文件格式转换（转封装）

  媒体文件格式转换时，需要先对媒体流进行解封装，然后按需将媒体流封装至新的格式文件内。

## 开发指导

详细的API说明参考[AVDemuxer](../harmonyos-references/capi-avdemuxer.md)和[AVSource](../harmonyos-references/capi-avsource.md)

说明

* 调用解封装能力解析网络播放路径，需要[声明权限](declare-permissions.md)：ohos.permission.INTERNET
* 调用解封装能力解析本地文件，需要[向用户申请授权](request-user-authorization.md)：ohos.permission.READ\_MEDIA
* 如果使用ResourceManager.getRawFd打开HAP资源文件描述符，使用方法请参考[ResourceManager API参考](../harmonyos-references/js-apis-resource-manager.md#getrawfd9)

### 在 CMake 脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libnative_media_codecbase.so)
2. target_link_libraries(sample PUBLIC libnative_media_avdemuxer.so)
3. target_link_libraries(sample PUBLIC libnative_media_avsource.so)
4. target_link_libraries(sample PUBLIC libnative_media_core.so)
```

说明

上述'sample'字样仅为示例，此处由开发者根据实际工程目录自定义。

### 开发步骤

1. 添加头文件。

   ```
   1. #include <multimedia/player_framework/native_avdemuxer.h>
   2. #include <multimedia/player_framework/native_avsource.h>
   3. #include <multimedia/player_framework/native_avcodec_base.h>
   4. #include <multimedia/player_framework/native_avformat.h>
   5. #include <multimedia/player_framework/native_avbuffer.h>
   6. #include <fcntl.h>
   7. #include <sys/stat.h>
   8. #include <string>
   ```
2. 创建资源管理实例。

   开发者HAP中使用open获取fd时，filepath需要转换为[沙箱路径](app-sandbox-directory.md#应用沙箱路径和真实物理路径的对应关系)，才能获取沙盒资源。

   ```
   1. // 创建文件操作符 fd，打开时对文件实例必须有读权限（filePath 为待解封装文件路径，需预置文件，保证路径指向的文件存在）。
   2. std::string filePath = "test.mp4";
   3. int32_t fd = open(filePath.c_str(), O_RDONLY);
   4. struct stat fileStatus {};
   5. int64_t fileSize = 0;
   6. if (stat(filePath.c_str(), &fileStatus) == 0) {
   7. fileSize = static_cast<int64_t>(fileStatus.st_size);
   8. } else {
   9. printf("get stat failed");
   10. return;
   11. }
   12. // 注意：offset（文件起始偏移）、fileSize（文件大小）需与待解析文件匹配。
   13. // fd 指向单个资源文件时，offset为0、fileSize为资源文件大小。
   14. // fd 指向多个连续拼接的资源文件时（如多个mp3二进制拼接）：offset、fileSize 按待解析文件实际偏移和大小设置。
   15. OH_AVSource *source = OH_AVSource_CreateWithFD(fd, 0, fileSize);
   16. if (source == nullptr) {
   17. printf("create source failed");
   18. return;
   19. }
   20. // 为 uri 资源文件创建 source 资源实例（可选）。
   21. // OH_AVSource *source = OH_AVSource_CreateWithURI(uri);

   23. // 为自定义数据源创建 source 资源实例（可选）。使用该方式前，需要先实现AVSourceReadAt接口函数实现。
   24. // 当使用OH_AVSource_CreateWithDataSource时需要补充g_filePath。
   25. // g_filePath = filePath ;
   26. // OH_AVDataSource dataSource = {fileSize, AVSourceReadAt};
   27. // OH_AVSource *source = OH_AVSource_CreateWithDataSource(&dataSource);
   ```

   AVSourceReadAt接口函数，需要放在创建资源管理实例前实现：

   ```
   1. // 添加头文件。
   2. #include <fstream>
   ```

   ```
   1. static std::string g_filePath;

   3. enum MediaDataSourceError : int32_t {
   4. SOURCE_ERROR_IO = -2,
   5. SOURCE_ERROR_EOF = -1
   6. };

   8. int32_t AVSourceReadAt(OH_AVBuffer *data, int32_t length, int64_t pos)
   9. {
   10. if (data == nullptr) {
   11. printf("AVSourceReadAt : data is nullptr!\n");
   12. return MediaDataSourceError::SOURCE_ERROR_IO;
   13. }

   15. std::ifstream infile(g_filePath, std::ofstream::binary);
   16. if (!infile.is_open()) {
   17. printf("AVSourceReadAt : open file failed! file:%s\n", g_filePath.c_str());
   18. return MediaDataSourceError::SOURCE_ERROR_IO;  // 打开文件失败。
   19. }

   21. infile.seekg(0, std::ios::end);
   22. int64_t fileSize = infile.tellg();
   23. if (pos >= fileSize) {
   24. printf("AVSourceReadAt : pos over or equals file size!\n");
   25. return MediaDataSourceError::SOURCE_ERROR_EOF;  // pos已经是文件末尾位置，无法读取。
   26. }

   28. if (pos + length > fileSize) {
   29. length = fileSize - pos;    // pos+length长度超过文件大小时，读取从pos到文件末尾的数据。
   30. }

   32. infile.seekg(pos, std::ios::beg);
   33. if (length <= 0) {
   34. printf("AVSourceReadAt : read length less than zero!\n");
   35. return MediaDataSourceError::SOURCE_ERROR_IO;
   36. }
   37. char* buffer = new char[length];
   38. infile.read(buffer, length);
   39. infile.close();

   41. memcpy(reinterpret_cast<char *>(OH_AVBuffer_GetAddr(data)),
   42. buffer, length);
   43. delete[] buffer;

   45. return length;
   46. }
   ```
3. 创建解封装器实例。

   ```
   1. // 为资源实例创建对应的解封装器。
   2. OH_AVDemuxer *demuxer = OH_AVDemuxer_CreateWithSource(source);
   3. if (demuxer == nullptr) {
   4. printf("create demuxer failed");
   5. return;
   6. }
   ```
4. 注册[DRM信息监听函数](../harmonyos-references/capi-native-avdemuxer-h.md#demuxer_mediakeysysteminfocallback)（可选，若非DRM码流或已获得[DRM信息](../harmonyos-references/capi-drm-drm-mediakeysysteminfo.md)，可跳过此步）。

   设置DRM信息监听的接口，回调函数支持返回解封装器实例，适用于多个解封装器场景。

   ```
   1. // DRM信息监听回调OnDrmInfoChangedWithObj实现。
   2. static void OnDrmInfoChangedWithObj(OH_AVDemuxer *demuxer, DRM_MediaKeySystemInfo *drmInfo)
   3. {
   4. // 解析DRM信息，包括数量、DRM类型及对应pssh。
   5. }

   7. Demuxer_MediaKeySystemInfoCallback callback = &OnDrmInfoChangedWithObj;
   8. Drm_ErrCode ret = OH_AVDemuxer_SetDemuxerMediaKeySystemInfoCallback(demuxer, callback);
   ```

   在监听到DRM信息后，也可主动调用获取DRM信息(uuid及对应pssh)接口。

   ```
   1. DRM_MediaKeySystemInfo mediaKeySystemInfo;
   2. OH_AVDemuxer_GetMediaKeySystemInfo(demuxer, &mediaKeySystemInfo);
   ```

   在获取、解析DRM信息后，需创建对应DRM解决方案的[MediaKeySystem、MediaKeySession](drm-c-dev-guide.md)，获取DRM许可证等。并根据需要设置音频解密配置(详见[音频解码开发指南开发步骤](audio-decoding.md#开发步骤)第4步)、设置视频解密配置（详见[视频解码开发指南开发步骤Surface模式](video-decoding.md#surface模式)第5步或[Buffer模式](video-decoding.md#buffer模式)第4步），实现DRM内容解密。
5. 获取文件信息。

   ```
   1. // 获取文件用户自定义属性（可选，若用户无需获取自定义属性，可跳过此步）。
   2. // 从文件 source 获取用户自定义属性信息。
   3. OH_AVFormat *customMetadataFormat = OH_AVSource_GetCustomMetadataFormat(source);
   4. if (customMetadataFormat == nullptr) {
   5. // 需释放前置流程资源，参考第10步。
   6. printf("get custom metadata format failed");
   7. return;
   8. }
   9. // 注意事项：
   10. // 1. customKey需与封装时写入的key完全一致（含完整命名层级），
   11. // 示例key仅为演示，实际应替换为用户自定义的字符串。
   12. // 例：封装时写入key为"com.openharmony.custom.meta.abc.efg"，
   13. // 获取时必须使用完整key，截断使用"com.openharmony.custom.meta.abc"会失败。
   14. // 2. value类型需与封装时数据类型匹配，示例为string类型。其余类型需调用对应接口，支持int/float类型；API version 20起，支持buffer类型。
   15. const char *customKey = "com.openharmony.custom.meta.string"; // 替换为实际封装时使用的完整key。
   16. const char *customValue;
   17. if (!OH_AVFormat_GetStringValue(customMetadataFormat, customKey, &customValue)) {
   18. printf("get custom metadata from custom metadata format failed");
   19. }
   20. OH_AVFormat_Destroy(customMetadataFormat);
   21. customMetadataFormat = nullptr;

   23. // 获取文件轨道数（可选，若用户已知轨道信息，可跳过此步）。
   24. // 从文件 source 信息获取文件轨道数，用户可通过该接口获取文件级别属性，具体支持信息参考附表 1。
   25. OH_AVFormat *sourceFormat = OH_AVSource_GetSourceFormat(source);
   26. if (sourceFormat == nullptr) {
   27. // 需释放前置流程资源，参考第10步。
   28. printf("get source format failed");
   29. return;
   30. }
   31. int32_t trackCount = 0;
   32. if (!OH_AVFormat_GetIntValue(sourceFormat, OH_MD_KEY_TRACK_COUNT, &trackCount)) {
   33. printf("get track count from source format failed");
   34. }
   35. if (trackCount == 0) {
   36. // 文件中无轨道，需根据业务做其他处理。
   37. printf("no track");
   38. }
   39. OH_AVFormat_Destroy(sourceFormat);
   40. sourceFormat = nullptr;
   ```
6. 获取轨道index及信息（可选，若用户已知轨道信息，可跳过此步）。

   ```
   1. uint32_t audioTrackIndex = 0;
   2. uint32_t videoTrackIndex = 0;
   3. int32_t w = 0;
   4. int32_t h = 0;
   5. int64_t bitRate = 0; // 配置比特率，单位为bps。
   6. double frameRate = 0.0;
   7. const char* mimetype = nullptr;
   8. uint8_t *codecConfig = nullptr;
   9. size_t bufferSize = 0;
   10. int32_t trackType = -1;
   11. for (uint32_t index = 0; index < (static_cast<uint32_t>(trackCount)); index++) {
   12. // 获取轨道信息，用户可通过该接口获取对应轨道级别属性，具体支持信息参考附表 2。
   13. OH_AVFormat *trackFormat = OH_AVSource_GetTrackFormat(source, index);
   14. if (trackFormat == nullptr) {
   15. printf("get track format failed");
   16. return;
   17. }
   18. // 获取轨道类型, 不支持的类型不会修改trackType的值。
   19. // 注意trackType初始值建议设为非有效值（如-1），避免误用。
   20. if (!OH_AVFormat_GetIntValue(trackFormat, OH_MD_KEY_TRACK_TYPE, &trackType)) {
   21. printf("get track type from track format failed");
   22. return;
   23. }
   24. if (trackType == OH_MediaType::MEDIA_TYPE_AUXILIARY) {
   25. const char *referenceType;
   26. if (!OH_AVFormat_GetStringValue(trackFormat, OH_MD_KEY_TRACK_REFERENCE_TYPE, &referenceType)) {
   27. printf("get reference type from auxiliary track failed");
   28. }
   29. int32_t* referenceIds;
   30. size_t referenceIdsCount;
   31. if (!OH_AVFormat_GetIntBuffer(trackFormat, OH_MD_KEY_TRACK_REFERENCE_TYPE, &referenceIds, &referenceIdsCount)) {
   32. printf("get reference track ids from auxiliary track failed");
   33. }
   34. // 根据辅助轨类型处理轨道参考关系。
   35. }
   36. static_cast<OH_MediaType>(trackType) == OH_MediaType::MEDIA_TYPE_AUD ? audioTrackIndex = index : videoTrackIndex = index;
   37. // 获取视频轨宽高。
   38. if (trackType == OH_MediaType::MEDIA_TYPE_VID) {
   39. if (!OH_AVFormat_GetIntValue(trackFormat, OH_MD_KEY_WIDTH, &w)) {
   40. printf("get track width from track format failed");
   41. return;
   42. }
   43. if (!OH_AVFormat_GetIntValue(trackFormat, OH_MD_KEY_HEIGHT, &h)) {
   44. printf("get track height from track format failed");
   45. return;
   46. }
   47. if (!OH_AVFormat_GetLongValue(trackFormat, OH_MD_KEY_BITRATE, &bitRate)) {
   48. printf("get track bitRate from track format failed");
   49. return;
   50. }
   51. if (!OH_AVFormat_GetDoubleValue(trackFormat, OH_MD_KEY_FRAME_RATE, &frameRate)) {
   52. printf("get track frameRate from track format failed");
   53. return;
   54. }
   55. if (!OH_AVFormat_GetStringValue(trackFormat, OH_MD_KEY_CODEC_MIME, &mimetype)) {
   56. printf("get track mimetype from track format failed");
   57. return;
   58. }
   59. if (!OH_AVFormat_GetBuffer(trackFormat, OH_MD_KEY_CODEC_CONFIG, &codecConfig, &bufferSize)) {
   60. printf("get track codecConfig from track format failed");
   61. return;
   62. }
   63. printf(" track width%d, track height：%d, track bitRate：%ld, track frameRate：%f, track mimetype：%s\n", w, h, bitRate, frameRate, mimetype);
   64. }
   65. OH_AVFormat_Destroy(trackFormat);
   66. trackFormat = nullptr;
   67. }
   ```
7. 添加解封装轨道。

   ```
   1. if(OH_AVDemuxer_SelectTrackByID(demuxer, audioTrackIndex) != AV_ERR_OK){
   2. printf("select audio track failed: %d", audioTrackIndex);
   3. return;
   4. }
   5. if(OH_AVDemuxer_SelectTrackByID(demuxer, videoTrackIndex) != AV_ERR_OK){
   6. printf("select video track failed: %d", videoTrackIndex);
   7. return;
   8. }
   9. // 取消选择轨道（可选）。
   10. // OH_AVDemuxer_UnselectTrackByID(demuxer, audioTrackIndex);
   ```
8. 调整轨道到指定时间点（可选）。

   ```
   1. // 调整轨道到指定时间点，后续从该时间点进行解封装。
   2. // 注意：
   3. // 1. mpegts、mpg 格式文件使用OH_AVDemuxer_SeekToTime功能时，跳转到的位置可能为非关键帧。可在跳转后调用OH_AVDemuxer_ReadSampleBuffer，通过获取到的OH_AVCodecBufferAttr判断当前帧是否为关键帧。若非关键帧影响应用侧显示等功能，可在跳转后循环读取，获取到后续第一帧关键帧后，再进行解码等处理。
   4. // 2. ogg格式文件使用OH_AVDemuxer_SeekToTime功能时，会跳转到传入时间millisecond所在时间间隔(秒)的起始处，可能会导致一定数量的帧误差。
   5. // 3. demuxer的seek处理只针对解码行为一致的码流进行处理，如果seek后需要解码器重新配置参数，或者需要重新送入参数集的数据才可以正确解码的码流，seek后可能会出现花屏、解码卡死等问题。
   6. OH_AVDemuxer_SeekToTime(demuxer, 0, OH_AVSeekMode::SEEK_MODE_CLOSEST_SYNC);
   ```
9. 开始解封装，循环获取sample（以含音频、视频两轨的文件为例）。

   BufferAttr包含的属性：

   * size：sample尺寸；
   * offset：数据在AVBuffer中的偏移，一般为0；
   * pts：文件封装的显示时间戳；
   * flags：sample属性。

   | flag | 描述 |
   | --- | --- |
   | AVCODEC\_BUFFER\_FLAGS\_NONE | 默认。 |
   | AVCODEC\_BUFFER\_FLAGS\_EOS | 结尾sample，数据为空。 |
   | AVCODEC\_BUFFER\_FLAGS\_SYNC\_FRAME | IDR帧或I帧。 |
   | AVCODEC\_BUFFER\_FLAGS\_INCOMPLETE\_FRAME | 非完整的sample，一般由于buffer过小，无法拷贝完整的sample。 |
   | AVCODEC\_BUFFER\_FLAGS\_CODEC\_DATA | 含参数集信息的帧。 |
   | AVCODEC\_BUFFER\_FLAGS\_DISCARD | 可丢弃的帧。 |

   OH\_AVDemuxer\_ReadSampleBuffer接口本身可能存在耗时久，取决于文件IO，建议以异步方式进行调用。

   ```
   1. // 为每个线程定义处理函数。
   2. void ReadTrackSamples(OH_AVDemuxer *demuxer, uint32_t trackIndex, int32_t buffer_size,
   3. std::atomic<bool>& isEnd, std::atomic<bool>& threadFinished)
   4. {
   5. // 创建缓冲区。
   6. OH_AVBuffer *buffer = OH_AVBuffer_Create(buffer_size);
   7. if (buffer == nullptr) {
   8. printf("Create buffer failed for track %d\n", trackIndex);
   9. threadFinished.store(true);
   10. return;
   11. }
   12. OH_AVCodecBufferAttr info;
   13. int32_t ret;

   15. while (!isEnd.load()) {
   16. // 在调用OH_AVDemuxer_ReadSampleBuffer接口获取数据前，需要先调用OH_AVDemuxer_SelectTrackByID选中需要获取数据的轨道。
   17. // 注意：
   18. // 在avi、mpg、wmv格式下，由于容器标准不支持封装时间戳信息，所以demuxer解出的帧中不含pts信息，需要调用方根据帧率及解码出帧后的显示顺序自行计算显示时间戳信息。
   19. ret = OH_AVDemuxer_ReadSampleBuffer(demuxer, trackIndex, buffer);
   20. if (ret == AV_ERR_OK) {
   21. OH_AVBuffer_GetBufferAttr(buffer, &info);
   22. printf("Track %d sample size: %d\n", trackIndex, info.size);
   23. // 检查EOS标志。
   24. if (info.flags == OH_AVCodecBufferFlags::AVCODEC_BUFFER_FLAGS_EOS) {
   25. isEnd.store(true);
   26. }
   27. // 处理缓冲区数据（这里可以根据需要实现解码逻辑）。
   28. } else {
   29. printf("Read sample failed for track %d\n", trackIndex);
   30. break;
   31. }
   32. }
   33. // 销毁缓冲区。
   34. OH_AVBuffer_Destroy(buffer);
   35. buffer = nullptr;
   36. threadFinished.store(true);
   37. }

   39. // 根据需求计算合适的缓冲区大小。
   40. int32_t audioBufferSize = 4096;  // 典型音频缓冲区大小。
   41. int32_t videoBufferSize = w * h * 3 >> 1;  // 原始视频缓冲区大小。

   43. // 创建原子变量用于线程通信。
   44. std::atomic<bool> audioIsEnd{false}, videoIsEnd{false}; // 表示流是否结束。
   45. std::atomic<bool> audioThreadFinished{false}, videoThreadFinished{false}; // 表示线程是否暂停。

   47. // 创建线程。
   48. std::thread audioThread(ReadTrackSamples, demuxer, audioTrackIndex, audioBufferSize,
   49. std::ref(audioIsEnd), std::ref(audioThreadFinished));
   50. std::thread videoThread(ReadTrackSamples, demuxer, videoTrackIndex, videoBufferSize,
   51. std::ref(videoIsEnd), std::ref(videoThreadFinished));
   52. audioThread.join();
   53. videoThread.join();
   ```
10. 销毁解封装实例。

    ```
    1. // 需要用户调用 OH_AVSource_Destroy 接口成功后，手动将实例置为nullptr，对同一实例重复调用 OH_AVSource_Destroy 会导致程序错误。
    2. if (OH_AVSource_Destroy(source) != AV_ERR_OK) {
    3. printf("destroy source pointer error");
    4. }
    5. source = nullptr;
    6. // 需要用户调用 OH_AVDemuxer_Destroy 接口成功后，手动将实例置为nullptr，对同一实例重复调用 OH_AVDemuxer_Destroy 会导致程序错误。
    7. if (OH_AVDemuxer_Destroy(demuxer) != AV_ERR_OK) {
    8. printf("destroy demuxer pointer error");
    9. }
    10. demuxer = nullptr;
    11. close(fd);
    ```

## 附表

### 文件级别属性支持范围

说明

* 正常解析时才可以获取对应属性数据，如果文件信息错误或缺失，将导致解析异常，无法获取数据。
* 当前GBK格式字符集数据会转换为UTF8提供，其他类型字符集如果需要转换为UTF8格式使用，需要调用方自行转换，参考[icu4c](../harmonyos-references/icu4c.md)。
* 从API version 23开始，部分OGG格式资源，如OH\_MD\_KEY\_TITLE、OH\_MD\_KEY\_ARTIST和OH\_MD\_KEY\_ALBUM存在于轨道属性中，可从轨道级别属性中获取。
* 数据类型及详细取值范围参考[媒体数据键值对](../harmonyos-references/capi-codecbase.md#媒体数据键值对)。

**表1** 文件级别属性支持范围

| 名称 | 描述 |
| --- | --- |
| OH\_MD\_KEY\_TITLE | 文件标题的键 |
| OH\_MD\_KEY\_ARTIST | 文件艺术家的键 |
| OH\_MD\_KEY\_ALBUM | 文件专辑的键 |
| OH\_MD\_KEY\_ALBUM\_ARTIST | 文件专辑艺术家的键 |
| OH\_MD\_KEY\_DATE | 文件日期的键 |
| OH\_MD\_KEY\_COMMENT | 文件注释的键 |
| OH\_MD\_KEY\_GENRE | 文件流派的键 |
| OH\_MD\_KEY\_COPYRIGHT | 文件版权的键 |
| OH\_MD\_KEY\_LANGUAGE | 文件语言的键 |
| OH\_MD\_KEY\_DESCRIPTION | 文件描述的键 |
| OH\_MD\_KEY\_LYRICS | 文件歌词的键 |
| OH\_MD\_KEY\_TRACK\_COUNT | 文件轨道数量的键 |
| OH\_MD\_KEY\_DURATION | 文件时长的键 |
| OH\_MD\_KEY\_START\_TIME | 文件起始时间的键 |

### 轨道级别属性支持范围

说明

正常解析时才可以获取对应属性数据；如果文件信息错误或缺失，将导致解析异常，无法获取数据。

辅助轨属性范围与实际媒体类型（音频、视频）保持一致。

数据类型及详细取值范围参考[媒体数据键值对](../harmonyos-references/capi-codecbase.md#媒体数据键值对)。

**表2** 轨道级别属性支持范围

| 名称 | 描述 | 视频轨支持 | 音频轨支持 | 字幕轨支持 | 辅助轨支持 |
| --- | --- | --- | --- | --- | --- |
| OH\_MD\_KEY\_CODEC\_MIME | 码流编解码器类型的键。 | √ | √ | √ | √ |
| OH\_MD\_KEY\_TRACK\_TYPE | 码流媒体类型的键。 | √ | √ | √ | √ |
| OH\_MD\_KEY\_TRACK\_START\_TIME | 码流起始时间的键。 | √ | √ | √ | √ |
| OH\_MD\_KEY\_BITRATE | 码流比特率的键。 | √ | √ | - | √ |
| OH\_MD\_KEY\_LANGUAGE | 码流语言类型的键。 | √ | √ | - | √ |
| OH\_MD\_KEY\_CODEC\_CONFIG | 编解码器特定数据的键，视频中表示传递参数集，音频中表示传递解码器的参数配置信息。 | √ | √ | - | √ |
| OH\_MD\_KEY\_WIDTH | 视频流宽度的键。 | √ | - | - | √ |
| OH\_MD\_KEY\_HEIGHT | 视频流高度的键。 | √ | - | - | √ |
| OH\_MD\_KEY\_FRAME\_RATE | 视频流帧率的键。 | √ | - | - | √ |
| OH\_MD\_KEY\_ROTATION | 视频流旋转角度的键。 | √ | - | - | √ |
| OH\_MD\_KEY\_VIDEO\_SAR | 视频流样本长宽比的键。 | √ | - | - | √ |
| OH\_MD\_KEY\_PROFILE | 视频流编码档次，只针对h265码流使用。 | √ | - | - | √ |
| OH\_MD\_KEY\_RANGE\_FLAG | 视频流视频YUV值域标志的键，只针对h265码流使用。 | √ | - | - | √ |
| OH\_MD\_KEY\_COLOR\_PRIMARIES | 视频流视频色域的键，只针对h265码流使用。 | √ | - | - | √ |
| OH\_MD\_KEY\_TRANSFER\_CHARACTERISTICS | 视频流视频传递函数的键，只针对h265码流使用。 | √ | - | - | √ |
| OH\_MD\_KEY\_MATRIX\_COEFFICIENTS | 视频矩阵系数的键，只针对h265码流使用。 | √ | - | - | √ |
| OH\_MD\_KEY\_VIDEO\_IS\_HDR\_VIVID | 视频流标记是否为HDR Vivid的键，只针对HDR Vivid码流使用。 | √ | - | - | √ |
| OH\_MD\_KEY\_AUD\_SAMPLE\_RATE | 音频流采样率的键。 | - | √ | - | √ |
| OH\_MD\_KEY\_AUD\_CHANNEL\_COUNT | 音频流通道数的键。 | - | √ | - | √ |
| OH\_MD\_KEY\_CHANNEL\_LAYOUT | 音频流所需编码通道布局的键。 | - | √ | - | √ |
| OH\_MD\_KEY\_AUDIO\_SAMPLE\_FORMAT | 音频流样本格式的键。 | - | √ | - | √ |
| OH\_MD\_KEY\_AAC\_IS\_ADTS | aac格式的键，只针对aac码流使用。 | - | √ | - | √ |
| OH\_MD\_KEY\_BITS\_PER\_CODED\_SAMPLE | 音频流每个编码样本位数的键。 | - | √ | - | √ |
| OH\_MD\_KEY\_REFERENCE\_TRACK\_IDS | 媒体文件轨道间参考、被参考关系。 | √ | √ | √ | √ |
| OH\_MD\_KEY\_TRACK\_REFERENCE\_TYPE | 媒体文件辅助轨类型。 | - | - | - | √ |
| OH\_MD\_KEY\_TRACK\_DESCRIPTION | 媒体文件辅助轨描述信息。 | - | - | - | √ |
