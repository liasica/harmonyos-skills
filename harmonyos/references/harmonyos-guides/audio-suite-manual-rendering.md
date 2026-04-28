---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-suite-manual-rendering
title: 离线编辑(C/C++)
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频编创 > 离线编辑(C/C++)
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:39+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d72a7da53fbd82fee01ed3ccd8a5a5759aba4fe25965a81c8363873270a05ba9
---

从API version 22开始，[OHAudioSuite](../harmonyos-references/capi-ohaudiosuite.md)给开发者提供音频离线编辑能力，允许在非实时播放场景下对音频数据进行处理，开发者可以组合多个音频节点实现复杂的音频处理流程。

## 开发基础配置

开发者使用[OHAudioSuite](../harmonyos-references/capi-ohaudiosuite.md)提供的离线编辑能力，添加对应的头文件。

### 在CMake脚本中链接动态库

```
1. target_link_libraries(sample PUBLIC libohaudiosuite.so)
```

### 添加头文件

开发者通过引入头文件<[native\_audio\_suite\_base.h](../harmonyos-references/capi-native-audio-suite-base-h.md)>和<[native\_audio\_suite\_engine.h](../harmonyos-references/capi-native-audio-suite-engine-h.md)>，使用音频编创相关API。

```
1. #include <ohaudiosuite/native_audio_suite_base.h>
2. #include <ohaudiosuite/native_audio_suite_engine.h>
```

## 开发步骤

详细的API说明请参考：[OHAudioSuite](../harmonyos-references/capi-ohaudiosuite.md)。

开发者参考本节内容实现音频离线编辑功能。

### 指定音频节点类型

开发者需要根据业务场景，调用[OH\_AudioSuiteNodeBuilder\_SetNodeType()](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_setnodetype)接口，指定对应的[OH\_AudioNode\_Type](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audionode_type)。

### 指定音频节点格式

开发者需要根据业务场景，调用[OH\_AudioSuiteNodeBuilder\_SetFormat()](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_setformat)或者[OH\_AudioSuiteEngine\_SetAudioFormat()](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_setaudioformat)接口，设置音频格式（[位深](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_sampleformat)、[采样率](../harmonyos-references/capi-native-audio-suite-base-h.md#oh_audio_samplerate)、[声道数](../harmonyos-references/capi-native-audio-channel-layout-h.md#oh_audiochannellayout)等）。

### 基础离线编辑

使用效果节点（如均衡器效果节点）处理输入的PCM（Pulse Code Modulation）音频数据，输出带有该音效的PCM音频数据。

**图1**：基础离线编辑示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/cgbbGA7BTFa5yHCRU3M0Tg/zh-cn_image_0000002583478537.png?HW-CC-KV=V1&HW-CC-Date=20260427T234538Z&HW-CC-Expire=86400&HW-CC-Sign=7266CC07DB44B584EBCFFFC6D4F8B836EDC90FB7010B24AE406A9A3BCA4047D0)

1. 创建引擎和管线。

   ```
   1. // 创建引擎。
   2. OH_AudioSuiteEngine *audioSuiteEngine = nullptr;
   3. OH_AudioSuiteEngine_Create(&audioSuiteEngine);

   5. // 创建管线。
   6. OH_AudioSuitePipeline *audioSuitePipeline = nullptr;
   7. OH_AudioSuiteEngine_CreatePipeline(
   8. audioSuiteEngine, &audioSuitePipeline, OH_AudioSuite_PipelineWorkMode::AUDIOSUITE_PIPELINE_EDIT_MODE);
   ```
2. 创建输入、输出、均衡器节点并连接组网。

   创建输入节点需要实现自定义回调函数InputNodeWriteDataCallBack，函数类型为[OH\_InputNode\_RequestDataCallback()](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_inputnode_requestdatacallback)，调用[OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback()](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_setrequestdatacallback)接口设置回调函数。

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

   34. // 创建节点构造器。
   35. OH_AudioNodeBuilder *nodeBuilder = nullptr;
   36. OH_AudioSuiteNodeBuilder_Create(&nodeBuilder);
   37. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::INPUT_NODE_TYPE_DEFAULT);

   39. // 配置音频数据格式，开发者根据要处理的音频数据格式设置采样率、声道分布、声道数、位深、编码格式参数。
   40. OH_AudioFormat audioFormatInput;
   41. audioFormatInput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   42. audioFormatInput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   43. audioFormatInput.channelCount = 2;
   44. audioFormatInput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   45. audioFormatInput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   46. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatInput);
   47. // 设置音频流的回调。
   48. struct AudioDataInfo audioInfo;
   49. audioInfo.buffer = nullptr; // 开发者根据业务场景存放要处理的音频数据。
   50. audioInfo.bufferSize = 0; // 开发者根据业务场景存放要处理的音频数据大小。
   51. audioInfo.totalWriteSize = 0;
   52. void *userData = static_cast<void *>(&audioInfo);
   53. OH_AudioSuiteNodeBuilder_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);
   54. // 创建输入节点。
   55. OH_AudioNode *inputNode = nullptr;
   56. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &inputNode);

   58. // 重置构造器配置并设置为均衡器节点类型。
   59. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   60. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::EFFECT_NODE_TYPE_EQUALIZER);
   61. // 创建均衡器节点。
   62. OH_AudioNode *eqNode = nullptr;
   63. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &eqNode);
   64. // 设置均衡器节点效果为默认。
   65. OH_AudioSuiteEngine_SetEqualizerFrequencyBandGains(eqNode, OH_EQUALIZER_PARAM_DEFAULT);

   67. // 重置构造器配置并设置为输出节点类型。
   68. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   69. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::OUTPUT_NODE_TYPE_DEFAULT);
   70. // 配置音频数据格式，开发者根据预期输出的音频格式设置采样率、声道分布、声道数、位深、编码格式参数。
   71. OH_AudioFormat audioFormatOutput;
   72. audioFormatOutput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   73. audioFormatOutput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   74. audioFormatOutput.channelCount = 2;
   75. audioFormatOutput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   76. audioFormatOutput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   77. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatOutput);
   78. // 创建输出节点。
   79. OH_AudioNode *outputNode = nullptr;
   80. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &outputNode);

   82. // 销毁节点构造器。
   83. OH_AudioSuiteNodeBuilder_Destroy(nodeBuilder);

   85. // 连接各个节点组成组网。
   86. OH_AudioSuiteEngine_ConnectNodes(inputNode, eqNode);
   87. OH_AudioSuiteEngine_ConnectNodes(eqNode, outputNode);
   ```
3. 渲染音频数据。

   开发者调用[OH\_AudioSuiteEngine\_RenderFrame()](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_renderframe)接口渲染并获取PCM音频数据。

   ```
   1. int32_t byteSize = 2; // OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE格式对应的字节大小。
   2. // 根据输出节点的格式计算单帧处理数据大小。
   3. // 1000是时间转换单位，20表示的是20ms的音频采样数据，如果samplingRate为11025请使用40ms来计算。
   4. int32_t frameSize = 20 * audioFormatOutput.samplingRate * audioFormatOutput.channelCount * byteSize / 1000;
   5. // 用于接收渲染后的输出音频数据。
   6. uint8_t *audioData = (uint8_t *)malloc(frameSize);
   7. int32_t responseSize = 0;
   8. bool finished = false;

   10. // 渲染。
   11. OH_AudioSuiteEngine_StartPipeline(audioSuitePipeline);
   12. do {
   13. OH_AudioSuite_Result result = OH_AudioSuiteEngine_RenderFrame(
   14. audioSuitePipeline, static_cast<void *>(audioData), frameSize, &responseSize, &finished);
   15. if ((result != OH_AudioSuite_Result::AUDIOSUITE_SUCCESS) || (responseSize <= 0)) {
   16. // 本次音频编创渲染失败。
   17. break;
   18. } else {
   19. // audioData是渲染过后的音频数据，音频数据长度为responseSize，开发者根据业务场景自行使用或者保存。
   20. }
   21. } while (!finished);
   22. OH_AudioSuiteEngine_StopPipeline(audioSuitePipeline);
   23. free(audioData);
   24. audioData = nullptr;
   ```
4. 资源销毁。

   ```
   1. // 销毁节点。
   2. OH_AudioSuiteEngine_DestroyNode(inputNode);
   3. OH_AudioSuiteEngine_DestroyNode(eqNode);
   4. OH_AudioSuiteEngine_DestroyNode(outputNode);

   6. // 销毁管线。
   7. OH_AudioSuiteEngine_DestroyPipeline(audioSuitePipeline);

   9. // 销毁引擎。
   10. OH_AudioSuiteEngine_Destroy(audioSuiteEngine);
   ```

### 音源分离场景

使用音源分离节点分离输入的PCM音频数据为人声和背景声，然后通过输出节点分别输出这两路数据。

**图2**：音源分离编辑示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/xdXxS53NQnusjRh7u5Ywtg/zh-cn_image_0000002552798888.png?HW-CC-KV=V1&HW-CC-Date=20260427T234538Z&HW-CC-Expire=86400&HW-CC-Sign=49DAD30CA4D8F3D9D39B2A22619A836250AB0A0E734FBA6A70FE305A25F016C5)

示例代码如下：

1. 创建引擎和管线。

   ```
   1. // 创建引擎。
   2. OH_AudioSuiteEngine *audioSuiteEngine = nullptr;
   3. OH_AudioSuiteEngine_Create(&audioSuiteEngine);

   5. // 创建管线。
   6. OH_AudioSuitePipeline *audioSuitePipeline = nullptr;
   7. OH_AudioSuiteEngine_CreatePipeline(
   8. audioSuiteEngine, &audioSuitePipeline, OH_AudioSuite_PipelineWorkMode::AUDIOSUITE_PIPELINE_EDIT_MODE);
   ```
2. 创建输入、输出、音源分离节点并连接。

   创建输入节点需要实现自定义回调函数InputNodeWriteDataCallBack，函数类型为[OH\_InputNode\_RequestDataCallback()](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_inputnode_requestdatacallback)，调用[OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback()](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuitenodebuilder_setrequestdatacallback)接口设置回调函数。

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

   34. // 创建节点构造器。
   35. OH_AudioNodeBuilder *nodeBuilder = nullptr;
   36. OH_AudioSuiteNodeBuilder_Create(&nodeBuilder);
   37. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::INPUT_NODE_TYPE_DEFAULT);

   39. // 配置音频数据格式，开发者根据要处理的音频数据格式设置采样率、声道分布、声道数、位深、编码格式参数。
   40. OH_AudioFormat audioFormatInput;
   41. audioFormatInput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   42. audioFormatInput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   43. audioFormatInput.channelCount = 2;
   44. audioFormatInput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   45. audioFormatInput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   46. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatInput);

   48. struct AudioDataInfo audioInfo;
   49. audioInfo.buffer = nullptr; // 开发者根据业务场景存放要处理的音频数据。
   50. audioInfo.bufferSize = 0; // 开发者根据业务场景存放要处理的音频数据大小。
   51. audioInfo.totalWriteSize = 0;
   52. void *userData = static_cast<void *>(&audioInfo);
   53. // 设置音频流的回调。
   54. OH_AudioSuiteNodeBuilder_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);

   56. // 创建输入节点。
   57. OH_AudioNode *inputNode = nullptr;
   58. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &inputNode);

   60. // 重置构造器配置并设置为音源分离节点类型。
   61. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   62. OH_AudioSuiteNodeBuilder_SetNodeType(
   63. nodeBuilder, OH_AudioNode_Type::EFFECT_MULTII_OUTPUT_NODE_TYPE_AUDIO_SEPARATION);

   65. // 创建音源分离节点。
   66. OH_AudioNode *aissNode = nullptr;
   67. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &aissNode);

   69. // 重置构造器配置并设置为输出节点类型。
   70. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   71. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::OUTPUT_NODE_TYPE_DEFAULT);
   72. // 配置音频数据格式，开发者根据预期输出的音频格式设置采样率、声道分布、声道数、位深、编码格式参数。
   73. OH_AudioFormat audioFormatOutput;
   74. audioFormatOutput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   75. audioFormatOutput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   76. audioFormatOutput.channelCount = 2;
   77. audioFormatOutput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   78. audioFormatOutput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   79. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatOutput);

   81. // 创建输出节点。
   82. OH_AudioNode *outputNode = nullptr;
   83. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &outputNode);

   85. // 销毁节点构造器。
   86. OH_AudioSuiteNodeBuilder_Destroy(nodeBuilder);

   88. // 连接各个节点组成组网。
   89. OH_AudioSuiteEngine_ConnectNodes(inputNode, aissNode);
   90. OH_AudioSuiteEngine_ConnectNodes(aissNode, outputNode);
   ```
3. 渲染音频数据。

   包含音源分离节点的管线使用[OH\_AudioSuiteEngine\_MultiRenderFrame()](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_multirenderframe)接口渲染并获取两路PCM音频数据。

   ```
   1. int32_t byteSize = 2; // OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE格式对应的字节大小。
   2. // 根据输出节点的格式计算单帧处理数据大小。
   3. // 1000是时间转换单位，20表示的是20ms的音频采样数据，如果samplingRate为11025请使用40ms来计算。
   4. int32_t frameSize = 20 * audioFormatOutput.samplingRate * audioFormatOutput.channelCount * byteSize / 1000;
   5. // 用于接收渲染后的输出音频数据。
   6. OH_AudioDataArray audioDataArray;
   7. int32_t outPutNum = 2;
   8. audioDataArray.audioDataArray = (void **)malloc(outPutNum * sizeof(void *));
   9. for(int32_t i = 0; i < outPutNum; i++) {
   10. audioDataArray.audioDataArray[i] = (void *)malloc(frameSize);
   11. }
   12. audioDataArray.arraySize = outPutNum;
   13. audioDataArray.requestFrameSize = frameSize;
   14. int32_t responseSize = 0;
   15. bool finished = false;

   17. // 渲染。
   18. OH_AudioSuiteEngine_StartPipeline(audioSuitePipeline);
   19. do {
   20. OH_AudioSuite_Result result = OH_AudioSuiteEngine_MultiRenderFrame(
   21. audioSuitePipeline, &audioDataArray, &responseSize, &finished);
   22. if ((result != OH_AudioSuite_Result::AUDIOSUITE_SUCCESS) || (responseSize <= 0)) {
   23. // 本次音频编创渲染失败。
   24. break;
   25. } else {
   26. // audioDataArray.audioDataArray[0]是提取的人声。
   27. // audioDataArray.audioDataArray[1]是提取的背景声。
   28. // 音频数据长度为responseSize，开发者根据业务场景自行使用或者保存。
   29. }
   30. } while (!finished);
   31. OH_AudioSuiteEngine_StopPipeline(audioSuitePipeline);

   33. for(int32_t i = 0; i < outPutNum; i++) {
   34. free(audioDataArray.audioDataArray[i]);
   35. audioDataArray.audioDataArray[i] = nullptr;
   36. }
   37. free(audioDataArray.audioDataArray);
   38. audioDataArray.audioDataArray = nullptr;
   ```
4. 资源销毁。

   ```
   1. // 销毁节点。
   2. OH_AudioSuiteEngine_DestroyNode(inputNode);
   3. OH_AudioSuiteEngine_DestroyNode(aissNode);
   4. OH_AudioSuiteEngine_DestroyNode(outputNode);

   6. // 销毁管线。
   7. OH_AudioSuiteEngine_DestroyPipeline(audioSuitePipeline);

   9. // 销毁引擎。
   10. OH_AudioSuiteEngine_Destroy(audioSuiteEngine);
   ```

### 混音与级联

输入多路PCM音频数据，使用混音节点进行混音，输出混音后的PCM音频数据。

**图3**：级联编辑示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/1tUejXEKQcWd-vivlUe-EA/zh-cn_image_0000002583438583.png?HW-CC-KV=V1&HW-CC-Date=20260427T234538Z&HW-CC-Expire=86400&HW-CC-Sign=AC9AE7A8ECBB04BC96A662CE4E9308DFF0FE4C30D0ED693FA532FCE91D5E83D6)

示例代码如下：

1. 创建引擎和管线。

   ```
   1. // 创建引擎。
   2. OH_AudioSuiteEngine *audioSuiteEngine = nullptr;
   3. OH_AudioSuiteEngine_Create(&audioSuiteEngine);

   5. // 创建管线。
   6. OH_AudioSuitePipeline *audioSuitePipeline = nullptr;
   7. OH_AudioSuiteEngine_CreatePipeline(
   8. audioSuiteEngine, &audioSuitePipeline, OH_AudioSuite_PipelineWorkMode::AUDIOSUITE_PIPELINE_EDIT_MODE);
   ```
2. 创建输入、输出、效果类节点并连接。

   由于混音功能有多个输入节点，需单独设置回调函数InputNodeWriteDataCallBack中的userData参数来区分多个输入节点，从而实现多个PCM音频数据的输入。InputNodeWriteDataCallBack函数类型为[OH\_InputNode\_RequestDataCallback()](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_inputnode_requestdatacallback)。

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

   34. // 创建节点构造器。
   35. OH_AudioNodeBuilder *nodeBuilder = nullptr;
   36. OH_AudioSuiteNodeBuilder_Create(&nodeBuilder);
   37. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::INPUT_NODE_TYPE_DEFAULT);
   38. // 配置音频数据格式，开发者根据要处理的音频数据格式设置采样率、声道分布、声道数、位深、编码格式参数。
   39. OH_AudioFormat audioFormatInput;
   40. audioFormatInput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   41. audioFormatInput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   42. audioFormatInput.channelCount = 2;
   43. audioFormatInput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   44. audioFormatInput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   45. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatInput);
   46. // 设置第一个音频流的回调。
   47. struct AudioDataInfo audioInfoForField;
   48. audioInfoForField.buffer = nullptr; // 开发者根据业务场景存放要处理的音频数据。
   49. audioInfoForField.bufferSize = 0; // 开发者根据业务场景存放要处理的音频数据大小。
   50. audioInfoForField.totalWriteSize = 0;
   51. void *userData = static_cast<void *>(&audioInfoForField);
   52. OH_AudioSuiteNodeBuilder_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);
   53. // 创建第一个输入节点。
   54. OH_AudioNode *inputNodeForField = nullptr;
   55. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &inputNodeForField);

   57. // 重置构造器配置并设置为输入节点类型。
   58. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   59. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::INPUT_NODE_TYPE_DEFAULT);
   60. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatInput);
   61. // 设置第二个音频流的回调。
   62. struct AudioDataInfo audioInfoForMix;
   63. audioInfoForMix.buffer = nullptr; // 开发者根据业务场景存放要处理的音频数据。
   64. audioInfoForMix.bufferSize = 0; // 开发者根据业务场景存放要处理的音频数据大小。
   65. audioInfoForMix.totalWriteSize = 0;
   66. userData = static_cast<void *>(&audioInfoForMix);
   67. OH_AudioSuiteNodeBuilder_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);
   68. // 创建第二个输入节点。
   69. OH_AudioNode *inputNodeForMix = nullptr;
   70. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &inputNodeForMix);

   72. // 重置构造器配置并设置为输入节点类型。
   73. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   74. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::EFFECT_NODE_TYPE_SOUND_FIELD);
   75. // 创建声场节点并设置声场模式为聆听。
   76. OH_AudioNode *fieldNode = nullptr;
   77. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &fieldNode);
   78. OH_AudioSuiteEngine_SetSoundFieldType(fieldNode, SOUND_FIELD_FRONT_FACING);

   80. // 重置构造器配置并设置为输入节点类型。
   81. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   82. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::EFFECT_NODE_TYPE_AUDIO_MIXER);
   83. OH_AudioNode *mixerNode = nullptr;
   84. // 创建混音节点。
   85. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &mixerNode);

   87. // 重置构造器配置并设置为输入节点类型。
   88. OH_AudioSuiteNodeBuilder_Reset(nodeBuilder);
   89. OH_AudioSuiteNodeBuilder_SetNodeType(nodeBuilder, OH_AudioNode_Type::OUTPUT_NODE_TYPE_DEFAULT);
   90. // 配置音频数据格式，开发者根据预期输出的音频格式设置采样率、声道分布、声道数、位深、编码格式参数。
   91. OH_AudioFormat audioFormatOutput;
   92. audioFormatOutput.samplingRate = OH_Audio_SampleRate::SAMPLE_RATE_48000;
   93. audioFormatOutput.channelLayout = OH_AudioChannelLayout::CH_LAYOUT_STEREO;
   94. audioFormatOutput.channelCount = 2;
   95. audioFormatOutput.sampleFormat = OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE;
   96. audioFormatOutput.encodingType = OH_Audio_EncodingType::AUDIO_ENCODING_TYPE_RAW;
   97. OH_AudioSuiteNodeBuilder_SetFormat(nodeBuilder, audioFormatOutput);
   98. // 创建输出节点。
   99. OH_AudioNode *outputNode = nullptr;
   100. OH_AudioSuiteEngine_CreateNode(audioSuitePipeline, nodeBuilder, &outputNode);

   102. // 销毁输出节点构造器。
   103. OH_AudioSuiteNodeBuilder_Destroy(nodeBuilder);

   105. // 连接各个节点组成组网。
   106. OH_AudioSuiteEngine_ConnectNodes(inputNodeForField, fieldNode);
   107. OH_AudioSuiteEngine_ConnectNodes(fieldNode, mixerNode);
   108. OH_AudioSuiteEngine_ConnectNodes(inputNodeForMix, mixerNode);
   109. OH_AudioSuiteEngine_ConnectNodes(mixerNode, outputNode);
   ```
3. 渲染音频数据。

   开发者调用[OH\_AudioSuiteEngine\_RenderFrame()](../harmonyos-references/capi-native-audio-suite-engine-h.md#oh_audiosuiteengine_renderframe)接口渲染并获取PCM音频数据。

   ```
   1. int32_t byteSize = 2; // OH_Audio_SampleFormat::AUDIO_SAMPLE_S16LE格式对应的字节大小。
   2. // 根据输出节点的格式计算单帧处理数据大小。
   3. // 1000是时间转换单位，20表示的是20ms的音频采样数据，如果samplingRate为11025请使用40ms来计算。
   4. int32_t frameSize = 20 * audioFormatOutput.samplingRate * audioFormatOutput.channelCount * byteSize / 1000;
   5. // 用于接收渲染后的输出音频数据。
   6. uint8_t *audioData = (uint8_t *)malloc(frameSize);
   7. int32_t responseSize = 0;
   8. bool finished = false;

   10. // 渲染。
   11. OH_AudioSuiteEngine_StartPipeline(audioSuitePipeline);
   12. do {
   13. OH_AudioSuite_Result result = OH_AudioSuiteEngine_RenderFrame(
   14. audioSuitePipeline, static_cast<void *>(audioData), frameSize, &responseSize, &finished);
   15. if ((result != OH_AudioSuite_Result::AUDIOSUITE_SUCCESS) || (responseSize <= 0)) {
   16. // 本次音频编创渲染失败。
   17. break;
   18. } else {
   19. // audioData是渲染过后的音频数据，音频数据长度为responseSize，开发者根据业务场景自行使用或者保存。
   20. }
   21. } while (!finished);
   22. OH_AudioSuiteEngine_StopPipeline(audioSuitePipeline);
   23. free(audioData);
   24. audioData = nullptr;
   ```
4. 资源销毁。

   ```
   1. // 销毁节点。
   2. OH_AudioSuiteEngine_DestroyNode(inputNodeForMix);
   3. OH_AudioSuiteEngine_DestroyNode(inputNodeForField);
   4. OH_AudioSuiteEngine_DestroyNode(fieldNode);
   5. OH_AudioSuiteEngine_DestroyNode(mixerNode);
   6. OH_AudioSuiteEngine_DestroyNode(outputNode);

   8. // 销毁管线。
   9. OH_AudioSuiteEngine_DestroyPipeline(audioSuitePipeline);

   11. // 销毁引擎。
   12. OH_AudioSuiteEngine_Destroy(audioSuiteEngine);
   ```
