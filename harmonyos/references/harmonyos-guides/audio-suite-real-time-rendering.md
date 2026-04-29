---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-suite-real-time-rendering
title: 实时渲染(C/C++)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频编创 > 实时渲染(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:37+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:c2f3f800dc3f0a47deabbaa6e36ee4a9af0e4cd4e2ab1531f5e42dfcb9f80c7d
---

从API version 22开始，[OHAudioSuite](../harmonyos-references/capi-ohaudiosuite.md)给开发者提供音频实时渲染能力，即音频实时播放时可进行自定义音效（仅支持均衡器节点）。例如，可以使用均衡器中预置的音效，改变音乐的风格。

## 开发基础配置

开发者使用[OHAudioSuite](../harmonyos-references/capi-ohaudiosuite.md)提供的实时渲染能力，添加对应的头文件。

### 在CMake脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libohaudio.so libohaudiosuite.so)
```

### 添加头文件

开发者通过引入头文件<[native\_audio\_suite\_base.h](../harmonyos-references/capi-native-audio-suite-base-h.md)>、<[native\_audio\_suite\_engine.h](../harmonyos-references/capi-native-audio-suite-engine-h.md)>、<[native\_audiostreambuilder.h](../harmonyos-references/capi-native-audiostreambuilder-h.md)>和<[native\_audiorenderer.h](../harmonyos-references/capi-native-audiorenderer-h.md)>使用音频编创和音频播放相关API。

```
1. #include <ohaudiosuite/native_audio_suite_base.h>
2. #include <ohaudiosuite/native_audio_suite_engine.h>
3. #include <ohaudio/native_audiorenderer.h>
4. #include <ohaudio/native_audiostreambuilder.h>
```

## 开发步骤

### 接口调用

详细的API说明请参考[OHAudioSuite](../harmonyos-references/capi-ohaudiosuite.md)。

### 均衡器效果

**图1**：实时播放示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/JnxoWRGUQWKKf2tCI8wILQ/zh-cn_image_0000002558765038.png?HW-CC-KV=V1&HW-CC-Date=20260429T053436Z&HW-CC-Expire=86400&HW-CC-Sign=79D0CF87103A39C66B56E6A7B68F1A1EC8C9941563EB0B56138FD75170078E97)

开发者可以通过以下步骤来实现一个简单的均衡器效果节点实时播放功能。

1. 在初始化时，创建[OHAudioSuite](../harmonyos-references/capi-ohaudiosuite.md)管线（包括输入节点、均衡器节点、输出节点）。

   ```
   1. struct AudioDataInfo {
   2. uint8_t *buffer = nullptr;  // 音频数据。
   3. int32_t bufferSize = 0;     // 音频数据总大小。
   4. int32_t totalWriteSize = 0; // 处理过的音频数据总大小。
   5. };

   7. // 输入节点请求数据的回调函数。
   8. static int32_t InputNodeWriteDataCallBack(
   9. OH_AudioNode *audioNode,
   10. void *userData,
   11. void *audioData,
   12. int32_t audioDataSize,
   13. bool *finished)
   14. {
   15. if ((audioNode == nullptr) || (userData == nullptr) ||
   16. (audioData == nullptr) || (audioDataSize <= 0) || (finished == nullptr)) {
   17. return -1;
   18. }

   20. struct AudioDataInfo *info = static_cast<struct AudioDataInfo *>(userData);
   21. // 要处理的音频大小。
   22. int32_t actualDataSize = std::min(audioDataSize, info->bufferSize - info->totalWriteSize);
   23. // 将PCM音频数据写入audioData。
   24. memcpy(static_cast<void *>(audioData), info->buffer + info->totalWriteSize, actualDataSize);
   25. info->totalWriteSize += actualDataSize;

   27. // 音频数据全部处理完。
   28. if (info->totalWriteSize >= info->bufferSize) {
   29. *finished = true;
   30. }
   31. return actualDataSize;
   32. }

   34. // 创建引擎。
   35. OH_AudioSuiteEngine *audioSuiteEngine = nullptr;
   36. OH_AudioSuiteEngine_Create(&audioSuiteEngine);

   38. // 创建实时渲染的管线。
   39. OH_AudioSuitePipeline *audioSuitePipeline;
   40. OH_AudioSuiteEngine_CreatePipeline(audioSuiteEngine, &audioSuitePipeline,
   41. OH_AudioSuite_PipelineWorkMode::AUDIOSUITE_PIPELINE_REALTIME_MODE);

   43. // 创建节点构造器。
   44. OH_AudioNodeBuilder *nodeBuilder = nullptr;
   45. OH_AudioSuiteNodeBuilder_Create(&nodeBuilder);
   46. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::INPUT_NODE_TYPE_DEFAULT);

   48. // 配置音频数据格式，开发者根据要处理的音频数据格式设置采样率、声道分布、声道数、位深、编码格式参数。
   49. OH_AudioFormat audioFormatInput;
   50. audioFormatInput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   51. audioFormatInput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   52. audioFormatInput.channelCount = 2;
   53. audioFormatInput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   54. audioFormatInput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   55. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatInput);
   56. // 设置音频流的回调。
   57. struct AudioDataInfo audioInfo;
   58. audioInfo.buffer = nullptr; // 开发者根据业务场景存放要处理的音频数据。
   59. audioInfo.bufferSize = 0; // 开发者根据业务场景存放要处理的音频数据大小。
   60. audioInfo.totalWriteSize = 0;
   61. void *userData = static_cast<void *>(&audioInfo);
   62. OH_AudioSuiteNodeBuilder_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);
   63. // 创建输入节点。
   64. OH_AudioNode *inputNode = nullptr;
   65. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &inputNode);

   67. // 重置构造器配置并设置为均衡器节点类型。
   68. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   69. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::EFFECT_NODE_TYPE_EQUALIZER);
   70. // 创建均衡器节点。
   71. OH_AudioNode *eqNode = nullptr;
   72. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &eqNode);
   73. // 设置均衡器节点效果为默认。
   74. OH_AudioSuiteEngine_SetEqualizerFrequencyBandGains(eqNode, OH_EQUALIZER_PARAM_DEFAULT);

   76. // 重置构造器配置并设置为输出节点类型。
   77. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   78. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::OUTPUT_NODE_TYPE_DEFAULT);
   79. // 配置音频数据格式，开发者根据预期输出的音频格式设置采样率、声道分布、声道数、位深、编码格式参数。
   80. OH_AudioFormat audioFormatOutput;
   81. audioFormatOutput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   82. audioFormatOutput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   83. audioFormatOutput.channelCount = 2;
   84. audioFormatOutput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   85. audioFormatOutput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   86. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatOutput);
   87. // 创建输出节点。
   88. OH_AudioNode *outputNode = nullptr;
   89. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &outputNode);

   91. // 销毁节点构造器。
   92. OH_AudioSuiteNodeBuilder_Destroy(nodeBuilder);

   94. // 连接各个节点组成组网。
   95. OH_AudioSuiteEngine_ConnectNodes(inputNode, eqNode);
   96. OH_AudioSuiteEngine_ConnectNodes(eqNode, outputNode);
   ```

   注意

   离线编辑和实时渲染在创建管线时有区别。

   * 实时渲染：OH\_AudioSuite\_PipelineWorkMode::AUDIOSUITE\_PIPELINE\_REALTIME\_MODE
   * 离线编辑：OH\_AudioSuite\_PipelineWorkMode::AUDIOSUITE\_PIPELINE\_EDIT\_MODE
2. 创建[OH\_AudioRendererStruct](../harmonyos-references/capi-ohaudio-oh-audiorendererstruct.md)实例，并在其AudioRendererOnWriteData()回调函数中调用[OHAudioSuite](../harmonyos-references/capi-ohaudiosuite.md)管线的[OH\_AudioSuiteEngine\_RenderFrame()](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_renderframe)接口来处理数据。

   请参考音频播放完成音频播放功能开发：[使用OHAudio开发音频播放功能(C/C++)](using-ohaudio-for-playback.md)。
3. 在播放器的回调函数中，将处理后的数据复制到OH\_AudioRenderer实例的缓冲区中，实现音频播放过程中实时渲染。

   ```
   1. static OH_AudioData_Callback_Result AudioRendererOnWriteData(
   2. OH_AudioRenderer* renderer,
   3. void* userData,
   4. void* audioData,
   5. int32_t audioDataSize)
   6. {
   7. bool finishedFlag = false;
   8. int32_t writeSize = 0;
   9. OH_AudioSuite_Result result = OH_AudioSuiteEngine_RenderFrame(
   10. static_cast<OH_AudioSuitePipeline *>(userData), audioData, audioDataSize, &writeSize, &finishedFlag);
   11. if (result != OH_AudioSuite_Result::AUDIOSUITE_SUCCESS) {
   12. // 音频编创渲染失败。
   13. return AUDIO_DATA_CALLBACK_RESULT_INVALID;
   14. }
   15. // 音频编创渲染完成。
   16. if (finishedFlag) {
   17. // 开发者自定义的行为。
   18. }

   20. return AUDIO_DATA_CALLBACK_RESULT_VALID;
   21. }

   23. // 创建构建器
   24. OH_AudioStreamBuilder *rendererBuilder = nullptr;
   25. OH_AudioStreamBuilder_Create(&rendererBuilder, OH_AudioStream_Type::AUDIOSTREAM_TYPE_RENDERER);
   26. OH_AudioStreamBuilder_SetSamplingRate(rendererBuilder, 48000);
   27. OH_AudioStreamBuilder_SetChannelCount(rendererBuilder, 2);
   28. OH_AudioStreamBuilder_SetSampleFormat(rendererBuilder, AUDIOSTREAM_SAMPLE_S16LE);
   29. OH_AudioStreamBuilder_SetEncodingType(rendererBuilder, AUDIOSTREAM_ENCODING_TYPE_RAW);
   30. OH_AudioStreamBuilder_SetRendererInfo(rendererBuilder, AUDIOSTREAM_USAGE_MUSIC);

   32. int32_t byteSize = 2; // AUDIOSTREAM_SAMPLE_S16LE格式对应的字节大小。
   33. // 1000是时间转换单位，20表示的是20ms的音频采样数据，如果samplingRate为11025请使用40ms来计算。
   34. int32_t frameSize = 20 * audioFormatOutput.samplingRate * audioFormatOutput.channelCount * byteSize / 1000;
   35. // 设置audioDataSize长度（待播放的数据大小）。
   36. OH_AudioStreamBuilder_SetFrameSizeInCallback(rendererBuilder, frameSize);
   37. // 配置写入音频数据回调函数。
   38. OH_AudioStreamBuilder_SetRendererWriteDataCallback(
   39. rendererBuilder, AudioRendererOnWriteData, static_cast<void *>(audioSuitePipeline));

   41. // 启动管线。
   42. OH_AudioSuiteEngine_StartPipeline(audioSuitePipeline);

   44. // 开发者可以自行创建renderer流，播放音频。
   45. // ...

   47. // 停止管线。
   48. OH_AudioSuiteEngine_StopPipeline(audioSuitePipeline);
   ```
4. 资源销毁。

   ```
   1. // 销毁流构造器。
   2. OH_AudioStreamBuilder_Destroy(rendererBuilder);

   4. // 销毁节点。
   5. OH_AudioSuiteEngine_DestroyNode(inputNode);
   6. OH_AudioSuiteEngine_DestroyNode(eqNode);
   7. OH_AudioSuiteEngine_DestroyNode(outputNode);

   9. // 销毁管线。
   10. OH_AudioSuiteEngine_DestroyPipeline(audioSuitePipeline);

   12. // 销毁引擎。
   13. OH_AudioSuiteEngine_Destroy(audioSuiteEngine);
   ```

## 注意事项

* 音频实时渲染过程中，不支持重新创建新的效果节点，只支持修改效果节点的参数。
* 音频编创错误码具体报错信息请参考：[OH\_AudioSuite\_Result](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audiosuite_result)。
