---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audiovivid-audiodecoder
title: Audio Vivid解码
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > Audio Vivid能力 > Audio Vivid解码
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:46+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:7f44943390ebfe869522ee94298c146f63a385aacd3c1942c9c93e23e37f10a0
---

获取解封装后的数据，送入解码器中，使用解码器获取PCM和Metadata元数据。详细的API请参考[AudioCodec模块](../harmonyos-references/capi-audiocodec.md)。

Audio Vivid解码当前支持的规格如下表所示。

| 规格项 | 支持范围 |
| --- | --- |
| 支持采样率 | 32000，44100，48000，96000，192000 |
| 支持码率范围 | 16000~3075000 |
| 支持声道数 | 1~16 |
| 支持的位深 | S16，S24 |

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
3. #include <string>

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

## 定义相关实例

**定义CodecBufferInfo**

解码码流的属性定义，为后面传给播放的码流数据封装。

```
1. struct CodecBufferInfo {
2. uint32_t bufferIndex = 0;
3. uintptr_t *buffer = nullptr;
4. uint8_t *bufferAddr = nullptr;
5. OH_AVCodecBufferAttr attr = {0, 0, 0, AVCODEC_BUFFER_FLAGS_NONE};

7. CodecBufferInfo(uint8_t *addr) : bufferAddr(addr){};
8. CodecBufferInfo(uint8_t *addr, int32_t bufferSize)
9. : bufferAddr(addr), attr({0, bufferSize, 0, AVCODEC_BUFFER_FLAGS_NONE}){};
10. CodecBufferInfo(uint32_t argBufferIndex, OH_AVMemory *argBuffer, OH_AVCodecBufferAttr argAttr)
11. : bufferIndex(argBufferIndex), buffer(reinterpret_cast<uintptr_t *>(argBuffer)), attr(argAttr){};
12. CodecBufferInfo(uint32_t argBufferIndex, OH_AVMemory *argBuffer)
13. : bufferIndex(argBufferIndex), buffer(reinterpret_cast<uintptr_t *>(argBuffer)){};
14. CodecBufferInfo(uint32_t argBufferIndex, OH_AVBuffer *argBuffer)
15. : bufferIndex(argBufferIndex), buffer(reinterpret_cast<uintptr_t *>(argBuffer)) {
16. OH_AVBuffer_GetBufferAttr(argBuffer, &attr);
17. };
18. };
```

**定义解码工作队列**

```
1. class CodecUserData {
2. public:
3. SampleInfo *sampleInfo = nullptr;

5. // 输入帧数
6. uint32_t inputFrameCount_ = 0;
7. // 输入队列锁，防止多线程同时操作输入队列
8. std::mutex inputMutex_;
9. // 输入线程的条件变量，当输入队列为空时用于阻塞输入线程
10. std::condition_variable inputCond_;
11. // 输入buffer队列，存放编解码器传给用户用来写入输入数据的buffer
12. std::queue<CodecBufferInfo> inputBufferInfoQueue_;

14. // 输出帧数
15. uint32_t outputFrameCount_ = 0;
16. // 输出队列锁，防止多线程同时操作输出队列
17. std::mutex outputMutex_;
18. // 输出线程的条件变量，当输出队列为空时用于阻塞输出线程
19. std::condition_variable outputCond_;
20. std::mutex renderMutex_;
21. std::condition_variable renderCond_;
22. // 输出buffer队列，存放编解码器传给用户用来存放输出数据的buffer
23. std::queue<CodecBufferInfo> outputBufferInfoQueue_;

25. std::shared_ptr<AudioDecoder> audioCodec_;
26. std::queue<unsigned char> renderQueue_;

28. void ClearQueue() {
29. {
30. std::unique_lock<std::mutex> lock(inputMutex_);
31. auto emptyQueue = std::queue<CodecBufferInfo>();
32. inputBufferInfoQueue_.swap(emptyQueue);
33. }
34. {
35. std::unique_lock<std::mutex> lock(outputMutex_);
36. auto emptyQueue = std::queue<CodecBufferInfo>();
37. outputBufferInfoQueue_.swap(emptyQueue);
38. }
39. }
40. };
```

**定义回调函数**

```
1. class SampleCallback {
2. public:
3. // 报错回调函数，当编解码器内部报错时调用，返回给用户相应错误码
4. static void OnCodecError(OH_AVCodec *codec, int32_t errorCode, void *userData);
5. // 参数修改回调函数，当编解码器参数被修改时调用，返回给用户被修改后的format参数
6. static void OnCodecFormatChange(OH_AVCodec *codec, OH_AVFormat *format, void *userData);
7. // 输入回调函数，当编解码器需要输入时调用，返回给用户用来写入输入数据的buffer及其对应的index
8. static void OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData);
9. // 输出回调函数，当编解码器生成新的输出数据时调用，返回给用户用来存放输出数据的buffer及其对应的index
10. static void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData);
11. };
12. void SampleCallback::OnCodecError(OH_AVCodec *codec, int32_t errorCode, void *userData) {
13. (void)codec;
14. (void)errorCode;
15. (void)userData;
16. }
17. void SampleCallback::OnCodecFormatChange(OH_AVCodec *codec, OH_AVFormat *format, void *userData) {
18. }
19. void SampleCallback::OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData) {
20. if (userData == nullptr) {
21. return;
22. }
23. (void)codec;
24. CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
25. std::unique_lock<std::mutex> lock(codecUserData->inputMutex_);
26. // 将输入buffer存放到输入队列中
27. codecUserData->inputBufferInfoQueue_.emplace(index, buffer);
28. // 通知输入线程开始运行
29. codecUserData->inputCond_.notify_all();
30. }

32. void SampleCallback::OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData) {
33. if (userData == nullptr) {
34. return;
35. }
36. (void)codec;
37. CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
38. std::unique_lock<std::mutex> lock(codecUserData->outputMutex_);
39. // 将输出buffer存放到输出队列中
40. codecUserData->outputBufferInfoQueue_.emplace(index, buffer);
41. // 通知输出线程开始运行
42. codecUserData->outputCond_.notify_all();
43. }
```

## 开发步骤

1. 创建解码实例。

   ```
   1. // 创建解码器
   2. OH_AVCodec * decoder = OH_AudioCodec_CreateByMime(info.audioCodecMime,false);

   4. // 参数配置
   5. OH_AVFormat *format = OH_AVFormat_Create();
   6. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_S16LE); //或者S24LE
   7. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, sampleInfo.audioChannelCount);
   8. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, sampleInfo.audioSampleRate);
   9. OH_AVFormat_SetIntValue(format, OH_MD_KEY_AAC_IS_ADTS, 1);
   10. OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, 96422);//码率，当前作为参考，解封装也可以获取到
   11. OH_AVFormat_SetBuffer(format, OH_MD_KEY_CODEC_CONFIG, sampleInfo.audioCodecConfig, sampleInfo.audioCodecSize);
   12. bool res = OH_AVFormat_SetLongValue(format, OH_MD_KEY_CHANNEL_LAYOUT, sampleInfo.audioChannelLayout);
   13. ret = OH_AudioCodec_Configure(decoder, format);
   14. OH_AVFormat_Destroy(format);
   15. format = nullptr;

   17. // 设置回调，用于输入输出buffer准备完毕后由系统回调出来
   18. int32_t ret = OH_AudioCodec_RegisterCallback(decoder,
   19. {SampleCallback::OnCodecError, SampleCallback::OnCodecFormatChange,
   20. SampleCallback::OnNeedInputBuffer, SampleCallback::OnNewOutputBuffer},codecUserData);
   21. // 准备回调和参数设置完毕后通知系统解码器准备好了，下一步准备启动。
   22. ret = OH_AudioCodec_Prepare(decoder)
   ```
2. 音频写入解码器。

   ```
   1. int32_t PushInputData(CodecBufferInfo &info)
   2. {
   3. int32_t  ret = OH_AVBuffer_SetBufferAttr(reinterpret_cast<OH_AVBuffer *>(info.buffer), &info.attr);
   4. ret = OH_AudioCodec_PushInputBuffer(decoder, info.bufferIndex);
   5. return 0;
   6. }
   ```
3. 释放使用过的输出码流。

   ```
   1. int32_t AudioDecoder::FreeOutputData(uint32_t bufferIndex)
   2. {
   3. int32_t ret = 0;
   4. ret = OH_AudioCodec_FreeOutputBuffer(decoder, bufferIndex);
   5. return ret ;
   6. }
   ```
4. 音频写入线程。

   ```
   1. CodecUserData*audioDecContext_ = new CodecUserData;
   2. void AudioDecInputThread()
   3. {
   4. while (true) {
   5. if(!isStarted_){
   6. return;
   7. }
   8. std::unique_lock<std::mutex> lock(audioDecContext_->inputMutex_);
   9. // 阻塞输入线程，直到程序运行结束，或者输入队列不为空
   10. bool condRet = audioDecContext_->inputCond_.wait_for(
   11. lock, 5s, [this]() { return !isStarted_ || !audioDecContext_->inputBufferInfoQueue_.empty(); });
   12. if(!isStarted_ || audioDecContext_->inputBufferInfoQueue_.empty()){
   13. return;
   14. }
   15. // 获取输入buffer
   16. CodecBufferInfo bufferInfo = audioDecContext_->inputBufferInfoQueue_.front();
   17. audioDecContext_->inputBufferInfoQueue_.pop();
   18. audioDecContext_->inputFrameCount_++;
   19. lock.unlock();
   20. // 从解封装器中读取一帧数据写入输入buffer
   21. demuxer_->ReadSample(demuxer_->GetAudioTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer), bufferInfo.attr);
   22. int32_t ret = audioDecoder_->PushInputData(bufferInfo);
   23. if(ret != 0){
   24. return;
   25. }
   26. if(bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS){
   27. return;
   28. }
   29. }
   30. // StartRelease();
   31. }
   ```
5. 音频解码输出线程。

   ```
   1. void AudioDecOutputThread()
   2. {
   3. while (true) {
   4. if(!isStarted_){
   5. return;
   6. }
   7. std::unique_lock<std::mutex> lock(audioDecContext_->outputMutex_);
   8. // 阻塞输出线程，直到程序运行结束，或者输出队列不为空
   9. bool condRet = audioDecContext_->outputCond_.wait_for(
   10. lock, 5s, [this]() { return !isStarted_ || !audioDecContext_->outputBufferInfoQueue_.empty(); });
   11. if(!isStarted_ || audioDecContext_->outputBufferInfoQueue_.empty()){
   12. return;
   13. }
   14. // 获取输出buffer
   15. CodecBufferInfo bufferInfo = audioDecContext_->outputBufferInfoQueue_.front();
   16. audioDecContext_->outputBufferInfoQueue_.pop();
   17. if(bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS){
   18. return;
   19. }
   20. audioDecContext_->outputFrameCount_++;
   21. // 获取解码后的pcm数据
   22. uint8_t *source = OH_AVBuffer_GetAddr(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer));
   23. OH_AVFormat * format = OH_AVBuffer_GetParameter(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer));
   24. uint8_t * metadata;
   25. size_t size;
   26. // 获取元数据
   27. OH_AVFormat_GetBuffer(format, OH_MD_KEY_AUDIO_VIVID_METADATA, &metadata, &size);
   28. #ifdef DEBUG_DECODE
   29. if (audioOutputFile_.is_open()) {
   30. audioOutputFile_.write((const char*)OH_AVBuffer_GetAddr(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer)), bufferInfo.attr.size);
   31. }
   32. #endif
   33. lock.unlock();
   34. int32_t ret = audioDecoder_->FreeOutputData(bufferInfo.bufferIndex);
   35. if(ret != 0){
   36. return;
   37. }
   38. }
   39. }
   ```
6. 启动解码。

   ```
   1. int ret = OH_AudioCodec_Start(decoder);
   ```
7. 停止和释放实例。

   ```
   1. OH_AudioCodec_Stop(decoder);
   2. OH_AudioCodec_Destroy(decoder);
   3. decoder = nullptr;
   ```
