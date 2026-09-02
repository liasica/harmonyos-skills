---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audiovivid-audioencoder
title: Audio Vivid编码
breadcrumb: 指南 > 媒体 > AVCodec Kit（音视频编解码服务） > 音视频编解码 > Audio Vivid能力 > Audio Vivid编码
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:15+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:f9fd53cec542558fa3228ed1496740dcb2249c34761644da26354e63c277e9d8
---

Audio Vivid格式的码流可以保存音频对象的位置、增益等信息，针对可以提供改变音频对象的位置、音量增益体验的Audio Vivid音源，从API版本26.0.0开始支持使用Audio Vivid编码技术实现高清空间音频编码。此处的音频对象是指被感知为一个整体的声音或由一个声源发出的独立于环境的声音。

详细的API请参考[AudioCodec模块](../harmonyos-references/capi-audiocodec.md)。

Audio Vivid编码当前支持的规格如下表所示。

| 规格项 | 支持范围 |
| --- | --- |
| 支持采样率（Hz） | 32000，44100，48000 |
| 支持码率范围（bps） | 32000~832000 |
| 支持声道数 | 1~16 |
| 支持的位深 | SAMPLE\_S16LE，SAMPLE\_S24LE |

不同声道布局，支持的码率如下表所示：

| 声道布局 | 支持码率（bps） |
| --- | --- |
| CH\_LAYOUT\_MONO | 32000，44000，56000，64000，72000，80000，96000，128000，144000，164000，192000 |
| CH\_LAYOUT\_STEREO | 32000，48000，64000，80000，96000，128000，144000，192000，256000，320000 |
| CH\_LAYOUT\_5POINT1 | 96000，128000，144000，160000，192000，256000，320000，384000，448000，512000，640000，720000 |
| CH\_LAYOUT\_5POINT1POINT2 | 152000，320000，480000，576000 |
| CH\_LAYOUT\_5POINT1POINT4 | 176000，256000，384000，448000，576000，704000 |
| CH\_LAYOUT\_7POINT1 | 128000，160000，192000，256000，384000，480000，576000，640000 |
| CH\_LAYOUT\_7POINT1POINT2 | 216000，384000，480000，576000，768000 |
| CH\_LAYOUT\_7POINT1POINT4 | 240000，384000，512000，608000，832000 |

如果传入的码率与表格的对不上，则会向下自适应为表格的码率。如果小于最低码率，则自适应为最低码率。

## 在CMake脚本中链接到动态库

```cmake
target_link_libraries(sample PUBLIC
libnative_media_codecbase.so libnative_media_core.so
libnative_media_acodec.so libnative_media_avdemuxer.so libnative_media_avsource.so
)
```

## 添加头文件

```
// 头文件。
#include <multimedia/player_framework/native_avcodec_audiocodec.h>
#include <multimedia/native_audio_channel_layout.h>
#include <multimedia/player_framework/native_avcapability.h>
#include <multimedia/player_framework/native_avcodec_base.h>
#include <multimedia/player_framework/native_avformat.h>
#include <multimedia/player_framework/native_avbuffer.h>
```

## 定义相关实例

* 定义编码输出数据结构体，该结构体会在[AudioVividEncoder类](audiovivid-audioencoder.md#audiovividencoder类)里使用，用于传递编码输出的数据、数据长度、pts信息。

```
struct AudioVividEncoderOutputData {
    uint8_t *encodedData = nullptr;
    int32_t encodedSize = 0;
    int64_t presentationTimeUs = 0;
    bool eos = false;
};
```

* 定义编码数据队列结构体，该结构体会在[AudioVividEncoder类](audiovivid-audioencoder.md#audiovividencoder类)里使用，用于保存编码器的输入buffer和输出buffer。

```
struct AudioVividEncoderContext {
    std::mutex inputMutex;
    std::condition_variable inputCond;
    std::queue<uint32_t> inputBufferIndices;
    std::queue<OH_AVBuffer *> inputBufferQueue;
    std::mutex outputMutex;
    std::condition_variable outputCond;
    std::queue<AudioVividEncoderOutputData> outputQueue;
    bool eos = false;
    int32_t errorCode = 0;
};
```

## AudioVividEncoder类

* 该类调用Audio Vivid编码的ndk接口，使用该类调用Audio Vivid编码流程更加简便。具体参考[开发步骤](audiovivid-audioencoder.md#开发步骤)。

```
class AudioVividEncoder {
public:
    AudioVividEncoder() = default;
    ~AudioVividEncoder();
    int32_t Create();
    int32_t Config(int32_t sampleRate, int32_t channelCount, int64_t channelLayout, int32_t bitrate);
    int32_t Start();
    int32_t PushInputBuffer(
        uint8_t *pcmData, int32_t pcmSize, uint8_t *metadata, int32_t metadataSize, int64_t presentationTimeUs);
    AudioVividEncoderOutputData *GetOutputBuffer();
    void FreeOutputBuffer();
    int32_t Stop();
    int32_t Release();
    AudioVividEncoderContext *GetContext()
    {
        return &context_;
    }
    void UpdateMetadata(uint8_t *metadata, int32_t metadataSize);

private:
    int32_t SetCallback();
    int32_t Configure();
    void AttachMetadataToBuffer(OH_AVBuffer *buffer, uint8_t *metadata, int32_t metadataSize);
    OH_AVCodec *encoder_ = nullptr;
    AudioVividEncoderContext context_;
    int32_t sampleRate_ = AudioConfig::SAMPLE_RATE;
    int32_t channelCount_ = AudioConfig::CHANNEL_COUNT;
    int64_t channelLayout_ = AudioConfig::CHANNEL_LAYOUT;
    int32_t bitrate_ = AudioConfig::BITRATE;
    uint8_t *currentMetadata_ = nullptr;
    int32_t currentMetadataSize_ = 0;
    std::mutex metadataMutex_;
};
```

* Create()函数实现，该函数创建Audio Vivid编码器。

```
int32_t AudioVividEncoder::Create()
{
    encoder_ = OH_AudioCodec_CreateByMime(OH_AVCODEC_MIMETYPE_AUDIO_VIVID, true);
    if (encoder_ == nullptr) {
        AVCODEC_SAMPLE_LOGE("Create AudioVivid encoder failed");
        return -1;
    }
    AVCODEC_SAMPLE_LOGI("Create AudioVivid encoder success");
    return 0;
}
```

* Config()函数实现，该函数用于配置Audio Vivid编码的采样率、声道数、声道布局以及编码码流。

```
int32_t AudioVividEncoder::Config(int32_t sampleRate, int32_t channelCount, int64_t channelLayout, int32_t bitrate)
{
    sampleRate_ = sampleRate;
    channelCount_ = channelCount;
    channelLayout_ = channelLayout;
    bitrate_ = bitrate;
    int32_t ret = Configure();
    if (ret != 0) {
        AVCODEC_SAMPLE_LOGE("Configure failed");
        return ret;
    }
    ret = SetCallback();
    if (ret != 0) {
        AVCODEC_SAMPLE_LOGE("SetCallback failed");
        return ret;
    }
    ret = OH_AudioCodec_Prepare(encoder_);
    if (ret != AV_ERR_OK) {
        AVCODEC_SAMPLE_LOGE("Prepare failed, ret: %{public}d", ret);
        return -1;
    }
    AVCODEC_SAMPLE_LOGI("Config AudioVivid encoder: sampleRate=%{public}d, channelCount=%{public}d, bitrate=%{public}d",
        sampleRate_,
        channelCount_,
        bitrate_);
    return 0;
}

int32_t AudioVividEncoder::Configure()
{
    OH_AVFormat *format = OH_AVFormat_Create();
    if (format == nullptr) {
        AVCODEC_SAMPLE_LOGE("AVFormat create failed");
        return -1;
    }
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_VIVID_SIGNAL_FORMAT, OH_AUDIO_VIVID_SIGNAL_FORMAT_MIX);
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_S24LE);
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, sampleRate_);
    OH_AVFormat_SetLongValue(format, OH_MD_KEY_AUDIO_SOUNDBED_LAYOUT, channelLayout_);
    // 声床比特率设置为128000 bps。此处为举例，按实际情况设置。
    OH_AVFormat_SetLongValue(format, OH_MD_KEY_AUDIO_SOUNDBED_BITRATE, 128000);
    // 对象格式设置为2个。
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_OBJECT_NUMBER, 2);
    // 声床比特率设置为64000 bps。此处为举例，按实际情况设置。
    OH_AVFormat_SetLongValue(format, OH_MD_KEY_AUDIO_OBJECT_BITRATE, 64000);
    int32_t ret = OH_AudioCodec_Configure(encoder_, format);
    OH_AVFormat_Destroy(format);
    if (ret != AV_ERR_OK) {
        AVCODEC_SAMPLE_LOGE("Configure encoder failed, ret: %{public}d", ret);
        return -1;
    }
    return 0;
}
```

* 不同信号格式设参示例，信号格式详细参考OH\_AudioVividSignalFormat。

```
    // mono模式下，以下key必填。
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_VIVID_SIGNAL_FORMAT, OH_AUDIO_VIVID_SIGNAL_FORMAT_MONO);
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_S24LE);
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, sampleRate_);
    OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, 128000);

    // stero模式下，以下key必填。
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_VIVID_SIGNAL_FORMAT, OH_AUDIO_VIVID_SIGNAL_FORMAT_STEREO);
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_S24LE);
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, sampleRate_);
    OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, 128000);

    // mc模式下（声道数 > 2 且 声道数 <= 16），以下key必填。
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_VIVID_SIGNAL_FORMAT, OH_AUDIO_VIVID_SIGNAL_FORMAT_MC);
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_S24LE);
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, sampleRate_);
    OH_AVFormat_SetLongValue(format, OH_MD_KEY_CHANNEL_LAYOUT, channelLayout_);
    OH_AVFormat_SetLongValue(format, OH_MD_KEY_BITRATE, 128000);

    // mix模式（对象数 > 0 且 声道数 + 对象数 <= 16）。
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_VIVID_SIGNAL_FORMAT, OH_AUDIO_VIVID_SIGNAL_FORMAT_MIX);  // 必填
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_SAMPLE_FORMAT, SAMPLE_S24LE);  // 必填
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUD_SAMPLE_RATE, sampleRate_);  // 必填
    OH_AVFormat_SetLongValue(format, OH_MD_KEY_AUDIO_SOUNDBED_LAYOUT, channelLayout_);  // 选填，有声床时填
    OH_AVFormat_SetLongValue(format, OH_MD_KEY_AUDIO_SOUNDBED_BITRATE, 128000);  // 选填，有声床时填
    OH_AVFormat_SetIntValue(format, OH_MD_KEY_AUDIO_OBJECT_NUMBER, 2);  // 选填，有对象时填
    OH_AVFormat_SetLongValue(format, OH_MD_KEY_AUDIO_OBJECT_BITRATE, 64000);  // 选填，有对象时填
```

* SetCallback()函数实现，该函数用于设置Audio Vivid编码器获取输入buffer、输出buffer的回调函数。当Audio Vivid有输入空buffer时会调用onNeedInputBuffer回调函数，Audio Vivid有输出数据的时候调用onNewOutputBuffer回调函数。

```
int32_t AudioVividEncoder::SetCallback()
{
    auto onError = [](OH_AVCodec *codec, int32_t errorCode, void *userData) {
        AudioVividEncoderContext *context = static_cast<AudioVividEncoderContext *>(userData);
        context->errorCode = errorCode;
        context->outputCond.notify_all();
        AVCODEC_SAMPLE_LOGE("Encoder error: %{public}d", errorCode);
    };
    auto onFormatChange = [](OH_AVCodec *codec, OH_AVFormat *format, void *userData) {
        AVCODEC_SAMPLE_LOGI("Encoder format change");
    };
    auto onNeedInputBuffer = [](OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData) {
        AudioVividEncoderContext *context = static_cast<AudioVividEncoderContext *>(userData);
        std::unique_lock<std::mutex> lock(context->inputMutex);
        context->inputBufferIndices.push(index);
        context->inputBufferQueue.push(buffer);
        context->inputCond.notify_all();
    };
    auto onNewOutputBuffer = [](OH_AVCodec *codec, uint32_t index, OH_AVBuffer *buffer, void *userData) {
        AudioVividEncoderContext *context = static_cast<AudioVividEncoderContext *>(userData);
        AudioVividEncoderOutputData outputData;
        OH_AVCodecBufferAttr attr;
        OH_AVBuffer_GetBufferAttr(buffer, &attr);
        outputData.encodedSize = attr.size;
        outputData.presentationTimeUs = attr.pts;
        outputData.eos = (attr.flags & AVCODEC_BUFFER_FLAGS_EOS) != 0;
        outputData.encodedData = nullptr;
        uint8_t *encodedAddr = OH_AVBuffer_GetAddr(buffer);
        if (encodedAddr && attr.size > 0) {
            outputData.encodedData = new uint8_t[attr.size];
            memcpy(outputData.encodedData, encodedAddr, attr.size);
        }
        {
            std::unique_lock<std::mutex> lock(context->outputMutex);
            context->outputQueue.push(outputData);
            context->outputCond.notify_all();
        }
        OH_AudioCodec_FreeOutputBuffer(codec, index);
    };

    int32_t ret = OH_AudioCodec_RegisterCallback(
        encoder_, {onError, onFormatChange, onNeedInputBuffer, onNewOutputBuffer}, &context_);
    if (ret != AV_ERR_OK) {
        AVCODEC_SAMPLE_LOGE("RegisterCallback failed, ret: %{public}d", ret);
        return -1;
    }
    return 0;
}
```

* Start()函数实现，设置Audio Vivid编码参数后，调用Start()函数，调用Start()函数后开始输入编码数据。

```
int32_t AudioVividEncoder::Start()
{
    if (encoder_ == nullptr) {
        AVCODEC_SAMPLE_LOGE("Encoder is null");
        return -1;
    }
    int32_t ret = OH_AudioCodec_Start(encoder_);
    if (ret != AV_ERR_OK) {
        AVCODEC_SAMPLE_LOGE("Start encoder failed, ret: %{public}d", ret);
        return -1;
    }
    AVCODEC_SAMPLE_LOGI("AudioVivid encoder started");
    return 0;
}
```

* UpdateMetadata()函数实现，该函数用于设置Metadata元数据。

```
void AudioVividEncoder::UpdateMetadata(uint8_t *metadata, int32_t metadataSize)
{
    std::lock_guard<std::mutex> lock(metadataMutex_);
    if (currentMetadata_) {
        delete[] currentMetadata_;
    }
    if (metadataSize > 10485760) { // 10485760：10MB 异常过大的输入大小。
        return;
    }
    currentMetadata_ = new uint8_t[metadataSize];
    memcpy(currentMetadata_, metadata, metadataSize);
    currentMetadataSize_ = metadataSize;
}
```

* PushInputBuffer()函数实现，该函数用于往Audio Vivid编码器输入音频pcm数据与Metadata元数据。

```
int32_t AudioVividEncoder::PushInputBuffer(
    uint8_t *pcmData, int32_t pcmSize, uint8_t *metadata, int32_t metadataSize, int64_t presentationTimeUs)
{
    if (encoder_ == nullptr || pcmData == nullptr || pcmSize <= 0) {
        AVCODEC_SAMPLE_LOGE("Invalid parameters: encoder=%{public}s, pcmData=%{public}s, pcmSize=%{public}d",
            encoder_ ? "valid" : "null",
            pcmData ? "valid" : "null",
            pcmSize);
        return -1;
    }
    std::unique_lock<std::mutex> lock(context_.inputMutex);
    if (context_.inputBufferIndices.empty()) {
        context_.inputCond.wait_for(lock, std::chrono::milliseconds(100), [this] { // 等100ms输入。
            return !context_.inputBufferIndices.empty() || context_.eos;
        });
    }
    if (context_.inputBufferIndices.empty()) {
        AVCODEC_SAMPLE_LOGE("No input buffer available");
        return -1;
    }
    uint32_t index = context_.inputBufferIndices.front();
    context_.inputBufferIndices.pop();
    OH_AVBuffer *buffer = context_.inputBufferQueue.front();
    context_.inputBufferQueue.pop();
    lock.unlock();
    uint8_t *bufferAddr = OH_AVBuffer_GetAddr(buffer);
    int32_t capacity = OH_AVBuffer_GetCapacity(buffer);
    if (pcmSize > capacity) {
        AVCODEC_SAMPLE_LOGW("PCM size %{public}d exceeds capacity %{public}d, truncating", pcmSize, capacity);
        pcmSize = capacity;
    }
    memcpy(bufferAddr, pcmData, pcmSize);
    OH_AVCodecBufferAttr attr = {static_cast<int32_t>(presentationTimeUs), pcmSize, 0, AVCODEC_BUFFER_FLAGS_NONE};
    OH_AVBuffer_SetBufferAttr(buffer, &attr);
    if (metadata && metadataSize > 0) {
        AttachMetadataToBuffer(buffer, metadata, metadataSize);
    } else {
        AVCODEC_SAMPLE_LOGE("no meta");
    }
    int32_t ret = OH_AudioCodec_PushInputBuffer(encoder_, index);
    if (ret != AV_ERR_OK) {
        AVCODEC_SAMPLE_LOGE("Push input buffer failed, ret: %{public}d", ret);
        return -1;
    }
    return 0;
}

void AudioVividEncoder::AttachMetadataToBuffer(OH_AVBuffer *buffer, uint8_t *metadata, int32_t metadataSize)
{
    if (metadata && metadataSize > 0) {
        OH_AVFormat *meta = OH_AVFormat_Create();
        if (meta) {
            OH_AVFormat_SetBuffer(meta, OH_MD_KEY_AUDIO_VIVID_METADATA, metadata, metadataSize);
            OH_AVBuffer_SetParameter(buffer, meta);
        }
        OH_AVFormat_Destroy(meta);
    }
}
```

* GetOutputBuffer()函数实现，该函数用于获取Audio Vivid编码输出的码流。

```
AudioVividEncoderOutputData *AudioVividEncoder::GetOutputBuffer()
{
    std::unique_lock<std::mutex> lock(context_.outputMutex);
    // 等待100ms。
    context_.outputCond.wait_for(lock, std::chrono::milliseconds(100),
        [this] { return !context_.outputQueue.empty() || context_.eos; });
    if (context_.outputQueue.empty()) {
        return nullptr;
    }
    AudioVividEncoderOutputData *data = new AudioVividEncoderOutputData(context_.outputQueue.front());
    return data;
}
```

* FreeOutputBuffer()函数实现，该函数用于释放Audio Vivid编码输出buffer。

```
void AudioVividEncoder::FreeOutputBuffer()
{
    std::unique_lock<std::mutex> lock(context_.outputMutex);
    if (!context_.outputQueue.empty()) {
        AudioVividEncoderOutputData &data = context_.outputQueue.front();
        if (data.encodedData) {
            delete[] data.encodedData;
            data.encodedData = nullptr;
        }
        context_.outputQueue.pop();
    }
}
```

* Stop()函数实现，该函数在编码结束后调用。

```
int32_t AudioVividEncoder::Stop()
{
    if (encoder_ == nullptr) {
        return -1;
    }
    context_.eos = true;
    context_.inputCond.notify_all();
    context_.outputCond.notify_all();
    int32_t ret = OH_AudioCodec_Stop(encoder_);
    if (ret != AV_ERR_OK) {
        AVCODEC_SAMPLE_LOGE("Stop encoder failed, ret: %{public}d", ret);
        return -1;
    }
    context_.inputBufferIndices = std::queue<uint32_t>();
    context_.inputBufferQueue = std::queue<OH_AVBuffer *>();
    AVCODEC_SAMPLE_LOGI("AudioVivid encoder stopped");
    return 0;
}
```

* Release()函数实现，该函数在Stop()后调用，用于销毁Audio Vivid编码器。

```
int32_t AudioVividEncoder::Release()
{
    if (encoder_ != nullptr) {
        OH_AudioCodec_Flush(encoder_);
        OH_AudioCodec_Destroy(encoder_);
        encoder_ = nullptr;
    }
    {
        std::unique_lock<std::mutex> lock(context_.outputMutex);
        while (!context_.outputQueue.empty()) {
            AudioVividEncoderOutputData &data = context_.outputQueue.front();
            if (data.encodedData) {
                delete[] data.encodedData;
            }
            context_.outputQueue.pop();
        }
    }
    if (currentMetadata_) {
        delete[] currentMetadata_;
        currentMetadata_ = nullptr;
    }
    currentMetadataSize_ = 0;
    context_.eos = false;
    context_.errorCode = 0;
    return 0;
}
```

## 开发步骤

1. 创建Audio Vivid编码器。

   ```
       // 创建编码器。
       int32_t ret = 0;
       AudioVividEncoder encoder_;
       ret = encoder_.Create();
       if (ret != 0) {
           AVCODEC_SAMPLE_LOGE("Failed to create encoder");
           return -1;
       }
       ret = encoder_.Config(SAMPLE_RATE, PCM_CHANNEL_COUNT, CHANNEL_LAYOUT, BITRATE);
       if (ret != 0) {
           AVCODEC_SAMPLE_LOGE("Failed to config encoder");
           return -1;
       }
       ret = encoder_.Start();
       if (ret != 0) {
           AVCODEC_SAMPLE_LOGE("Failed to start encoder");
           return -1;
       }
       // 创建编码输入输出线程。
       encoderInputThread_ = std::thread(&AudioVividPlaybackManager::EncoderInputThread, this);
       encoderOutputThread_ = std::thread(&AudioVividPlaybackManager::EncoderOutputThread, this);
   ```
2. 配置Audio Vivid编码参数。

   ```
       ret = encoder_.Config(SAMPLE_RATE, PCM_CHANNEL_COUNT, CHANNEL_LAYOUT, BITRATE);
       if (ret != 0) {
           AVCODEC_SAMPLE_LOGE("Failed to config encoder");
           return -1;
       }
   ```
3. 开始Audio Vivid编码。

   ```
       ret = encoder_.Start();
       if (ret != 0) {
           AVCODEC_SAMPLE_LOGE("Failed to start encoder");
           return -1;
       }
   ```
4. 创建Audio Vivid编码的输入线程。

   ```
       // 创建编码输入输出线程。
       encoderInputThread_ = std::thread(&AudioVividPlaybackManager::EncoderInputThread, this);
   ```

   编码输入程的实现。该线程从文件里面读取pcm数据放到pcmBuffer，然后送给Audio Vivid编码器。实际使用时可以把写入pcmBuffer的数据换成需要的。

   ```
   void AudioVividPlaybackManager::EncoderInputThread()
   {
       uint8_t *pcmBuffer = new uint8_t[BYTES_PER_PCM_FRAME];
       uint8_t *encoderBuffer = new uint8_t[BYTES_PER_FRAME];
       while (!shouldStop_.load()) {
           size_t queueSize = 0;
           {
               std::lock_guard<std::mutex> lock(decodedQueueMutex_);
               queueSize = decodedDataQueue_.size();
           }
           if (queueSize >= MAX_DECODED_QUEUE_SIZE) {
               std::this_thread::sleep_for(std::chrono::milliseconds(20)); // 等待20ms再读取数据，未消耗的buffer较多。
               continue;
           }
           int32_t bytesRead = pcmReader_.Read(pcmBuffer, BYTES_PER_PCM_FRAME);
           if (bytesRead <= 0) {
               if (pcmReader_.IsEOF()) {
                   pcmReader_.Reset();
                   AVCODEC_SAMPLE_LOGI("PCM file looped, restarting from beginning");
               }
               continue;
           }
           memset(encoderBuffer, 0, BYTES_PER_FRAME);
           memcpy(encoderBuffer, pcmBuffer, bytesRead);
           int64_t pts = presentationTimeUs_.fetch_add(FRAME_SIZE * 1000000 / SAMPLE_RATE); // 1000000：1s转为us。
           uint8_t *metadata = nullptr;
           int32_t metadataSize = 0;
           {
               std::lock_guard<std::mutex> lock(metadataMutex_);
               if (currentMetadata_ && currentMetadataSize_ > 0) {
                   metadata = currentMetadata_;
                   metadataSize = currentMetadataSize_;
               }
           }
           int32_t ret = encoder_.PushInputBuffer(encoderBuffer, BYTES_PER_FRAME, metadata, metadataSize, pts);
           if (ret != 0) {
               AVCODEC_SAMPLE_LOGE("Failed to push input buffer to encoder");
           }
       }
       delete[] pcmBuffer;
       delete[] encoderBuffer;
       AVCODEC_SAMPLE_LOGI("EncoderInputThread exited");
   }
   ```
5. 创建Audio Vivid编码的输出线程。

   ```
       encoderOutputThread_ = std::thread(&AudioVividPlaybackManager::EncoderOutputThread, this);
   ```

   编码输出线程的实现。当Audio Vivid有编码输出时，该线程会获取编码输出的数据，放入outputData里。

   ```
   void AudioVividPlaybackManager::EncoderOutputThread()
   {
       while (!shouldStop_.load()) {
           AudioVividEncoderOutputData *outputData = encoder_.GetOutputBuffer();
           if (outputData == nullptr) {
               std::this_thread::sleep_for(std::chrono::milliseconds(10)); // 等10ms输入。
               continue;
           }
           if (outputData->eos) {
               delete outputData;
               break;
           }
           int32_t ret = decoder_.PushInputBuffer(outputData->encodedData, outputData->encodedSize);
           if (ret != 0) {
               AVCODEC_SAMPLE_LOGE("Failed to push input buffer to decoder");
           }
           delete outputData;
           encoder_.FreeOutputBuffer();
       }
       AVCODEC_SAMPLE_LOGI("EncoderOutputThread exited");
   }
   ```
6. 停止和释放实例。

   ```
       encoder_.GetContext()->inputCond.notify_all();
       encoder_.GetContext()->outputCond.notify_all();
       if (encoderInputThread_.joinable()) {
           encoderInputThread_.join();
       }
       if (encoderOutputThread_.joinable()) {
           encoderOutputThread_.join();
       }
       encoder_.Stop();
   ```
