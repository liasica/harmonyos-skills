---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audiovivid-audiodecoder
title: Audio Vivid解码
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > Audio Vivid能力 > Audio Vivid解码
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:15+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:82e91db3c6886b48a1d2b60f57a1e568c35f816e6df3682e0db779982a878069
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
#include <string>

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

## 定义相关实例

**定义CodecBufferInfo**

解码码流的属性定义，为后面传给播放的码流数据封装。

```
struct CodecBufferInfo {
    uint32_t bufferIndex = 0;
    uintptr_t *buffer = nullptr;
    uint8_t *bufferAddr = nullptr;
    OH_AVCodecBufferAttr attr = {0, 0, 0, AVCODEC_BUFFER_FLAGS_NONE};

    CodecBufferInfo(uint8_t *addr) : bufferAddr(addr){};
    CodecBufferInfo(uint8_t *addr, int32_t bufferSize)
        : bufferAddr(addr), attr({0, bufferSize, 0, AVCODEC_BUFFER_FLAGS_NONE}){};
    CodecBufferInfo(uint32_t argBufferIndex, OH_AVMemory *argBuffer, OH_AVCodecBufferAttr argAttr)
        : bufferIndex(argBufferIndex), buffer(reinterpret_cast<uintptr_t *>(argBuffer)), attr(argAttr){};
    CodecBufferInfo(uint32_t argBufferIndex, OH_AVMemory *argBuffer)
        : bufferIndex(argBufferIndex), buffer(reinterpret_cast<uintptr_t *>(argBuffer)){};
    CodecBufferInfo(uint32_t argBufferIndex, OH_AVBuffer *argBuffer)
        : bufferIndex(argBufferIndex), buffer(reinterpret_cast<uintptr_t *>(argBuffer)) {
        OH_AVBuffer_GetBufferAttr(argBuffer, &attr);
    };
};
```

**定义解码工作队列**

```
class CodecUserData {
public:
    SampleInfo *sampleInfo = nullptr;

    // 输入帧数
    uint32_t inputFrameCount_ = 0;
    // 输入队列锁，防止多线程同时操作输入队列
    std::mutex inputMutex_;
    // 输入线程的条件变量，当输入队列为空时用于阻塞输入线程
    std::condition_variable inputCond_;
    // 输入buffer队列，存放编解码器传给用户用来写入输入数据的buffer
    std::queue<CodecBufferInfo> inputBufferInfoQueue_;

    // 输出帧数
    uint32_t outputFrameCount_ = 0;
    // 输出队列锁，防止多线程同时操作输出队列
    std::mutex outputMutex_;
    // 输出线程的条件变量，当输出队列为空时用于阻塞输出线程
    std::condition_variable outputCond_;
    std::mutex renderMutex_;
    std::condition_variable renderCond_;
    // 输出buffer队列，存放编解码器传给用户用来存放输出数据的buffer
    std::queue<CodecBufferInfo> outputBufferInfoQueue_;

    std::shared_ptr<AudioDecoder> audioCodec_;
    std::queue<unsigned char> renderQueue_;

    void ClearQueue() {
        {
            std::unique_lock<std::mutex> lock(inputMutex_);
            auto emptyQueue = std::queue<CodecBufferInfo>();
            inputBufferInfoQueue_.swap(emptyQueue);
        }
        {
            std::unique_lock<std::mutex> lock(outputMutex_);
            auto emptyQueue = std::queue<CodecBufferInfo>();
            outputBufferInfoQueue_.swap(emptyQueue);
        }
    }
};
```

**定义回调函数**

```
class SampleCallback {
public:
    // 报错回调函数，当编解码器内部报错时调用，返回给用户相应错误码
    static void OnCodecError(OH_AVCodec *codec, int32_t errorCode, void *userData);
    // 参数修改回调函数，当编解码器参数被修改时调用，返回给用户被修改后的format参数
    static void OnCodecFormatChange(OH_AVCodec *codec, OH_AVFormat *format, void *userData);
    // 输入回调函数，当编解码器需要输入时调用，返回给用户用来写入输入数据的buffer及其对应的index
    static void OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData);
    // 输出回调函数，当编解码器生成新的输出数据时调用，返回给用户用来存放输出数据的buffer及其对应的index
    static void OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData);
};
void SampleCallback::OnCodecError(OH_AVCodec *codec, int32_t errorCode, void *userData) {
    (void)codec;
    (void)errorCode;
    (void)userData;
}
void SampleCallback::OnCodecFormatChange(OH_AVCodec *codec, OH_AVFormat *format, void *userData) {
}
void SampleCallback::OnNeedInputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData) {
    if (userData == nullptr) {
        return;
    }
    (void)codec;
    CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
    std::unique_lock<std::mutex> lock(codecUserData->inputMutex_);
    // 将输入buffer存放到输入队列中
    codecUserData->inputBufferInfoQueue_.emplace(index, buffer);
    // 通知输入线程开始运行
    codecUserData->inputCond_.notify_all();
}

void SampleCallback::OnNewOutputBuffer(OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData) {
    if (userData == nullptr) {
        return;
    }
    (void)codec;
    CodecUserData *codecUserData = static_cast<CodecUserData *>(userData);
    std::unique_lock<std::mutex> lock(codecUserData->outputMutex_);
    // 将输出buffer存放到输出队列中
    codecUserData->outputBufferInfoQueue_.emplace(index, buffer);
    // 通知输出线程开始运行
    codecUserData->outputCond_.notify_all();
}
```

## 开发步骤

1. 创建解码实例。

   ```
   // 创建解码器
   OH_AVCodec * decoder = OH_AudioCodec_CreateByMime(info.audioCodecMime,false);

   // 参数配置
   OH_AVFormat *format = OH_AVFormat_Create();
   OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_S16LE); //或者S24LE
   OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_CHANNEL_COUNT, sampleInfo.audioChannelCount);
   OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, sampleInfo.audioSampleRate);
   OH_AVFormat_SetIntValue(format, OH_MD_KEY_AAC_IS_ADTS, 1);
   OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, 96422);//码率，当前作为参考，解封装也可以获取到
   OH_AVFormat_SetBuffer(format, OH_MD_KEY_CODEC_CONFIG, sampleInfo.audioCodecConfig, sampleInfo.audioCodecSize);
   bool res = OH_AVFormat_SetLongValue(format, OH_MD_KEY_CHANNEL_LAYOUT, sampleInfo.audioChannelLayout);
   ret = OH_AudioCodec_Configure(decoder, format);
   OH_AVFormat_Destroy(format);
   format = nullptr;

   // 设置回调，用于输入输出buffer准备完毕后由系统回调出来
   int32_t ret = OH_AudioCodec_RegisterCallback(decoder,
       {SampleCallback::OnCodecError, SampleCallback::OnCodecFormatChange,
        SampleCallback::OnNeedInputBuffer, SampleCallback::OnNewOutputBuffer},codecUserData);
   // 准备回调和参数设置完毕后通知系统解码器准备好了，下一步准备启动。
   ret = OH_AudioCodec_Prepare(decoder)
   ```
2. 音频写入解码器。

   ```
   int32_t PushInputData(CodecBufferInfo &info)
   {
       int32_t  ret = OH_AVBuffer_SetBufferAttr(reinterpret_cast<OH_AVBuffer *>(info.buffer), &info.attr);
       ret = OH_AudioCodec_PushInputBuffer(decoder, info.bufferIndex);
       return 0;
   }
   ```
3. 释放使用过的输出码流。

   ```
   int32_t AudioDecoder::FreeOutputData(uint32_t bufferIndex)
   {
       int32_t ret = 0;
       ret = OH_AudioCodec_FreeOutputBuffer(decoder, bufferIndex);
       return ret ;
   }
   ```
4. 音频写入线程。

   ```
   CodecUserData*audioDecContext_ = new CodecUserData;
   void AudioDecInputThread()
   {
       while (true) {
           if(!isStarted_){
              return;
           }
           std::unique_lock<std::mutex> lock(audioDecContext_->inputMutex_);
           // 阻塞输入线程，直到程序运行结束，或者输入队列不为空
           bool condRet = audioDecContext_->inputCond_.wait_for(
               lock, 5s, [this]() { return !isStarted_ || !audioDecContext_->inputBufferInfoQueue_.empty(); });
           if(!isStarted_ || audioDecContext_->inputBufferInfoQueue_.empty()){
              return;
           }
           // 获取输入buffer
           CodecBufferInfo bufferInfo = audioDecContext_->inputBufferInfoQueue_.front();
           audioDecContext_->inputBufferInfoQueue_.pop();
           audioDecContext_->inputFrameCount_++;
           lock.unlock();
           // 从解封装器中读取一帧数据写入输入buffer
           demuxer_->ReadSample(demuxer_->GetAudioTrackId(), reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer), bufferInfo.attr);
           int32_t ret = audioDecoder_->PushInputData(bufferInfo);
           if(ret != 0){
               return;
           }
           if(bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS){
               return;
           }
       }
       // StartRelease();
   }
   ```
5. 音频解码输出线程。

   ```
   void AudioDecOutputThread()
   {
       while (true) {
           if(!isStarted_){
              return;
           }
           std::unique_lock<std::mutex> lock(audioDecContext_->outputMutex_);
           // 阻塞输出线程，直到程序运行结束，或者输出队列不为空
           bool condRet = audioDecContext_->outputCond_.wait_for(
               lock, 5s, [this]() { return !isStarted_ || !audioDecContext_->outputBufferInfoQueue_.empty(); });
           if(!isStarted_ || audioDecContext_->outputBufferInfoQueue_.empty()){
              return;
           }
           // 获取输出buffer
           CodecBufferInfo bufferInfo = audioDecContext_->outputBufferInfoQueue_.front();
           audioDecContext_->outputBufferInfoQueue_.pop();
           if(bufferInfo.attr.flags & AVCODEC_BUFFER_FLAGS_EOS){
              return;
           }
           audioDecContext_->outputFrameCount_++;
           // 获取解码后的pcm数据
           uint8_t *source = OH_AVBuffer_GetAddr(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer));
           OH_AVFormat * format = OH_AVBuffer_GetParameter(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer));
           uint8_t * metadata;
           size_t size;
           // 获取元数据
           OH_AVFormat_GetBuffer(format, OH_MD_KEY_AUDIO_VIVID_METADATA, &metadata, &size);
   #ifdef DEBUG_DECODE
           if (audioOutputFile_.is_open()) {
               audioOutputFile_.write((const char*)OH_AVBuffer_GetAddr(reinterpret_cast<OH_AVBuffer *>(bufferInfo.buffer)), bufferInfo.attr.size);
           }
   #endif
           lock.unlock();
           int32_t ret = audioDecoder_->FreeOutputData(bufferInfo.bufferIndex);
           if(ret != 0){
               return;
           }
       }
   }
   ```
6. 启动解码。

   ```
   int ret = OH_AudioCodec_Start(decoder);
   ```
7. 停止和释放实例。

   ```
   OH_AudioCodec_Stop(decoder);
   OH_AudioCodec_Destroy(decoder);
   decoder = nullptr;
   ```
