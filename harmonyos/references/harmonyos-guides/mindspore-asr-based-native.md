---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mindspore-asr-based-native
title: 使用MindSpore Lite实现语音识别（C/C++）
breadcrumb: 指南 > AI > MindSpore Lite Kit（昇思推理框架服务） > 使用MindSpore Lite实现语音识别（C/C++）
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:567d45f144c3bfe464447f1e65ab1bff03e39cd6cf49f85059f248da34b5385b
---

## 场景说明

开发者可以使用[MindSpore](../harmonyos-references/capi-mindspore.md)，在UI代码中集成MindSpore Lite能力，快速部署AI算法，进行AI模型推理，实现语音识别的应用。

语音识别可以将一段音频信息转换为文本，在智能语音助手、语音输入、语音搜索等领域有广泛的应用。

## 环境配置

若需要使用模拟器运行该示例，请参考：[使用模拟器运行应用](ide-run-emulator.md)

## 基本概念

* N-API：用于构建ArkTS本地化组件的一套接口。可利用N-API，将C/C++开发的库封装成ArkTS模块。

## 开发流程

1. 选择语音识别模型。
2. 在端侧使用MindSpore Lite推理模型，实现对语音文件的语音识别。

## 开发步骤

本文以对语音识别模型进行推理为例，提供使用MindSpore Lite实现语音识别应用的开发指导。

### 选择模型

本示例程序中使用的语音识别模型文件为tiny-encoder.ms、tiny-decoder-main.ms、tiny-decoder-loop.ms，放置在entry/src/main/resources/rawfile工程目录下。

### 编写播放音频代码

调用[@ohos.multimedia.media](../harmonyos-references/arkts-apis-media.md)、[@ohos.multimedia.audio](../harmonyos-references/arkts-apis-audio.md)，实现播放音频的功能。

```
1. // player.ets
2. import { media } from '@kit.MediaKit';
3. import { common } from '@kit.AbilityKit';
4. import { BusinessError } from '@kit.BasicServicesKit';
5. import { audio } from '@kit.AudioKit';
6. import { UIContext } from '@kit.ArkUI';
7. import { hilog } from '@kit.PerformanceAnalysisKit';

9. const TAG = 'MindSporeLite';

11. export default class AVPlayerDemo {
12. private isSeek: boolean = false; // 用于区分模式是否支持seek操作。
13. // 注册avplayer回调函数。
14. setAVPlayerCallback(avPlayer: media.AVPlayer) {
15. // seek操作结果回调函数。
16. avPlayer.on('seekDone', (seekDoneTime: number) => {
17. hilog.info(0xFF00, TAG, '%{public}s', `MS_LITE_LOG: AVPlayer seek succeeded, seek time is ${seekDoneTime}`);
18. });
19. // error回调监听函数，当avPlayer在操作过程中出现错误时调用reset接口触发重置流程。
20. avPlayer.on('error', (err: BusinessError) => {
21. hilog.error(0xFF00, TAG, '%{public}s',
22. `MS_LITE_ERR: Invoke avPlayer failed, code is ${err.code}, message is ${err.message}`);
23. avPlayer.reset(); // 调用reset重置资源，触发idle状态。
24. });
25. // 状态机变化回调函数。
26. avPlayer.on('stateChange', async (state: string, reason: media.StateChangeReason) => {
27. switch (state) {
28. case 'idle': // 成功调用reset接口后触发该状态机上报。
29. hilog.info(0xFF00, TAG, '%{public}s', 'MS_LITE_LOG: AVPlayer state idle called.');
30. avPlayer.release(); // 调用release接口销毁实例对象。
31. break;
32. case 'initialized': // avplayer 设置播放源后触发该状态上报。
33. hilog.info(0xFF00, TAG, '%{public}s', 'MS_LITE_LOG: AVPlayer state initialized called.');
34. avPlayer.audioRendererInfo = {
35. usage: audio.StreamUsage.STREAM_USAGE_MUSIC, // 音频流使用类型：音乐。根据业务场景配置。
36. rendererFlags: 0 // 音频渲染器标志。
37. };
38. avPlayer.prepare();
39. break;
40. case 'prepared': // prepare调用成功后上报该状态机。
41. hilog.info(0xFF00, TAG, '%{public}s', 'MS_LITE_LOG: AVPlayer state prepared called.');
42. avPlayer.play(); // 调用播放接口开始播放。
43. break;
44. case 'playing': // play成功调用后触发该状态机上报。
45. hilog.info(0xFF00, TAG, '%{public}s', 'MS_LITE_LOG: AVPlayer state playing called.');
46. if (this.isSeek) {
47. hilog.info(0xFF00, TAG, '%{public}s', 'MS_LITE_LOG: AVPlayer start to seek.');
48. avPlayer.seek(0); // 将播放位置移动到音频的开始。
49. } else {
50. // 当播放模式不支持seek操作时继续播放到结尾。
51. hilog.info(0xFF00, TAG, '%{public}s', 'MS_LITE_LOG: AVPlayer wait to play end.');
52. }
53. break;
54. case 'paused': // pause成功调用后触发该状态机上报。
55. hilog.info(0xFF00, TAG, '%{public}s', 'MS_LITE_LOG: AVPlayer state paused called.');
56. setTimeout(() => {
57. hilog.info(0xFF00, TAG, '%{public}s', 'MS_LITE_LOG: AVPlayer paused wait to play again');
58. avPlayer.play(); // 暂停3s后再次调用播放接口开始播放。
59. }, 3000);
60. break;
61. case 'completed': // 播放结束后触发该状态机上报。
62. hilog.info(0xFF00, TAG, '%{public}s', 'MS_LITE_LOG: AVPlayer state completed called.');
63. avPlayer.stop(); // 调用播放结束接口。
64. break;
65. case 'stopped': // stop接口成功调用后触发该状态机上报。
66. hilog.info(0xFF00, TAG, '%{public}s', 'MS_LITE_LOG: AVPlayer state stopped called.');
67. avPlayer.reset(); // 调用reset接口初始化avplayer状态。
68. break;
69. case 'released':
70. hilog.info(0xFF00, TAG, '%{public}s', 'MS_LITE_LOG: AVPlayer state released called.');
71. break;
72. default:
73. hilog.info(0xFF00, TAG, '%{public}s', 'MS_LITE_LOG: AVPlayer state unknown called.');
74. break;
75. }
76. });
77. }

79. // 使用资源管理接口获取音频文件并通过fdSrc属性进行播放。
80. async avPlayerFdSrcDemo() {
81. // 创建avPlayer实例对象。
82. let avPlayer: media.AVPlayer = await media.createAVPlayer();
83. // 创建状态机变化回调函数。
84. this.setAVPlayerCallback(avPlayer);
85. // 通过UIAbilityContext的resourceManager成员的getRawFd接口获取媒体资源播放地址。
86. // 返回类型为{fd,offset,length},fd为HAP包fd地址，offset为媒体资源偏移量，length为播放长度。
87. let context = new UIContext().getHostContext() as common.UIAbilityContext;
88. let fileDescriptor = await context.resourceManager.getRawFd('zh.wav');
89. let avFileDescriptor: media.AVFileDescriptor =
90. { fd: fileDescriptor.fd, offset: fileDescriptor.offset, length: fileDescriptor.length };
91. this.isSeek = true; // 支持seek操作。
92. // 为fdSrc赋值触发initialized状态机上报。
93. avPlayer.fdSrc = avFileDescriptor;
94. }
95. }
```

[player.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/ets/pages/player.ets#L16-L111)

### 编写识别音频代码

在 entry/src/main/cpp/mslite\_napi.cpp，调用[MindSpore](../harmonyos-references/capi-mindspore.md)，依次对3个模型进行推理，推理代码流程如下。

1. 引用对应的头文件。说明：需要用户下载三方库，其中librosa来源是[LibrosaCpp](https://github.com/ewan-xu/LibrosaCpp)，libsamplerate来源是[libsamplerate](https://github.com/libsndfile/libsamplerate)，下载后置于entry/src/main/cpp/third\_party目录下。AudioFile.h的来源是[AudioFile](https://github.com/adamstark/AudioFile/blob/1.1.2/AudioFile.h)，base64.h、base64.cpp的来源是[whisper.axera](https://github.com/ml-inory/whisper.axera/tree/main/cpp/src)下载后置于entry/src/main/cpp/src目录下。

   ```
   1. #include "AudioFile.h"
   2. #include "base64.h"
   3. #include "napi/native_api.h"
   4. #include "utils.h"
   5. #include <algorithm>
   6. #include <cstdlib>
   7. #include <fstream>
   8. #include <hilog/log.h>
   9. #include <iostream>
   10. #include <librosa/librosa.h>
   11. #include <mindspore/context.h>
   12. #include <mindspore/model.h>
   13. #include <mindspore/status.h>
   14. #include <mindspore/tensor.h>
   15. #include <mindspore/types.h>
   16. #include <numeric>
   17. #include <rawfile/raw_file_manager.h>
   18. #include <sstream>
   19. #include <vector>
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L16-L36)
2. 读取音频文件、模型文件等，转换为buffer数据。

   ```
   1. #define LOGI(...) ((void)OH_LOG_Print(LOG_APP, LOG_INFO, LOG_DOMAIN, "[MSLiteNapi]", __VA_ARGS__))
   2. #define LOGD(...) ((void)OH_LOG_Print(LOG_APP, LOG_DEBUG, LOG_DOMAIN, "[MSLiteNapi]", __VA_ARGS__))
   3. #define LOGW(...) ((void)OH_LOG_Print(LOG_APP, LOG_WARN, LOG_DOMAIN, "[MSLiteNapi]", __VA_ARGS__))
   4. #define LOGE(...) ((void)OH_LOG_Print(LOG_APP, LOG_ERROR, LOG_DOMAIN, "[MSLiteNapi]", __VA_ARGS__))
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L38-L43)

   ```
   1. using BinBuffer = std::pair<void *, size_t>;
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L63-L65)

   ```
   1. BinBuffer ReadBinFile(NativeResourceManager *nativeResourceManager, const std::string &modelName)
   2. {
   3. auto rawFile = OH_ResourceManager_OpenRawFile(nativeResourceManager, modelName.c_str());
   4. if (rawFile == nullptr) {
   5. LOGE("MS_LITE_ERR: Open model file failed");
   6. return BinBuffer(nullptr, 0);
   7. }
   8. long fileSize = OH_ResourceManager_GetRawFileSize(rawFile);
   9. if (fileSize <= 0) {
   10. LOGE("MS_LITE_ERR: FileSize not correct");
   11. return BinBuffer(nullptr, 0);
   12. }
   13. void *buffer = malloc(fileSize);
   14. if (buffer == nullptr) {
   15. LOGE("MS_LITE_ERR: OH_ResourceManager_ReadRawFile failed");
   16. return BinBuffer(nullptr, 0);
   17. }
   18. int ret = OH_ResourceManager_ReadRawFile(rawFile, buffer, fileSize);
   19. if (ret == 0) {
   20. LOGE("MS_LITE_ERR: OH_ResourceManager_ReadRawFile failed");
   21. OH_ResourceManager_CloseRawFile(rawFile);
   22. return BinBuffer(nullptr, 0);
   23. }
   24. OH_ResourceManager_CloseRawFile(rawFile);
   25. return BinBuffer(buffer, fileSize);
   26. }

   28. BinBuffer ReadTokens(NativeResourceManager *nativeResourceManager, const std::string &modelName)
   29. {
   30. auto rawFile = OH_ResourceManager_OpenRawFile(nativeResourceManager, modelName.c_str());
   31. if (rawFile == nullptr) {
   32. LOGE("MS_LITE_ERR: Open model file failed");
   33. return BinBuffer(nullptr, 0);
   34. }
   35. long fileSize = OH_ResourceManager_GetRawFileSize(rawFile);
   36. if (fileSize <= 0) {
   37. LOGE("MS_LITE_ERR: FileSize not correct");
   38. return BinBuffer(nullptr, 0);
   39. }
   40. void *buffer = malloc(fileSize);
   41. if (buffer == nullptr) {
   42. LOGE("MS_LITE_ERR: OH_ResourceManager_ReadRawFile failed");
   43. return BinBuffer(nullptr, 0);
   44. }
   45. int ret = OH_ResourceManager_ReadRawFile(rawFile, buffer, fileSize);
   46. if (ret == 0) {
   47. LOGE("MS_LITE_ERR: OH_ResourceManager_ReadRawFile failed");
   48. OH_ResourceManager_CloseRawFile(rawFile);
   49. return BinBuffer(nullptr, 0);
   50. }
   51. OH_ResourceManager_CloseRawFile(rawFile);
   52. BinBuffer res(buffer, fileSize);
   53. return res;
   54. }
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L79-L134)
3. 创建上下文，设置设备类型，并加载模型。

   ```
   1. void DestroyModelBuffer(void **buffer)
   2. {
   3. if (buffer == nullptr) {
   4. return;
   5. }
   6. free(*buffer);
   7. *buffer = nullptr;
   8. }

   10. OH_AI_ModelHandle CreateMSLiteModel(BinBuffer &bin)
   11. {
   12. // 创建并配置上下文
   13. auto context = OH_AI_ContextCreate();
   14. if (context == nullptr) {
   15. DestroyModelBuffer(&bin.first);
   16. LOGE("MS_LITE_ERR: Create MSLite context failed.\n");
   17. return nullptr;
   18. }
   19. auto cpu_device_info = OH_AI_DeviceInfoCreate(OH_AI_DEVICETYPE_CPU);
   20. OH_AI_DeviceInfoSetEnableFP16(cpu_device_info, false);
   21. OH_AI_ContextAddDeviceInfo(context, cpu_device_info);

   23. // 创建模型
   24. auto model = OH_AI_ModelCreate();
   25. if (model == nullptr) {
   26. DestroyModelBuffer(&bin.first);
   27. LOGE("MS_LITE_ERR: Allocate MSLite Model failed.\n");
   28. return nullptr;
   29. }

   31. // 加载与编译模型，模型的类型为OH_AI_MODELTYPE_MINDIR
   32. auto build_ret = OH_AI_ModelBuild(model, bin.first, bin.second, OH_AI_MODELTYPE_MINDIR, context);
   33. DestroyModelBuffer(&bin.first);
   34. if (build_ret != OH_AI_STATUS_SUCCESS) {
   35. OH_AI_ModelDestroy(&model);
   36. LOGE("MS_LITE_ERR: Build MSLite model failed.\n");
   37. return nullptr;
   38. }
   39. LOGI("MS_LITE_LOG: Build MSLite model success.\n");
   40. return model;
   41. }
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L136-L178)
4. 设置模型输入数据，执行模型推理。

   ```
   1. constexpr int K_NUM_PRINT_OF_OUT_DATA = 20;
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L59-L61)

   ```
   1. int FillInputTensor(OH_AI_TensorHandle input, const BinBuffer &bin)
   2. {
   3. if (OH_AI_TensorGetDataSize(input) != bin.second) {
   4. return OH_AI_STATUS_LITE_INPUT_PARAM_INVALID;
   5. }
   6. char *data = (char *)OH_AI_TensorGetMutableData(input);
   7. memcpy(data, (const char *)bin.first, OH_AI_TensorGetDataSize(input));
   8. return OH_AI_STATUS_SUCCESS;
   9. }
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L67-L77)

   ```
   1. // 执行模型推理
   2. int RunMSLiteModel(OH_AI_ModelHandle model, std::vector<BinBuffer> inputBins)
   3. {
   4. // 设置模型的输入数据
   5. auto inputs = OH_AI_ModelGetInputs(model);
   6. for(int i = 0; i < inputBins.size(); i++)
   7. {
   8. auto ret = FillInputTensor(inputs.handle_list[i], inputBins[i]);
   9. if (ret != OH_AI_STATUS_SUCCESS) {
   10. LOGE("MS_LITE_ERR: set input %{public}d error.\n", i);
   11. return OH_AI_STATUS_LITE_ERROR;
   12. }
   13. }

   15. // 获取模型的输出张量
   16. auto outputs = OH_AI_ModelGetOutputs(model);

   18. // 模型推理
   19. auto predict_ret = OH_AI_ModelPredict(model, inputs, &outputs, nullptr, nullptr);
   20. if (predict_ret != OH_AI_STATUS_SUCCESS) {
   21. OH_AI_ModelDestroy(&model);
   22. LOGE("MS_LITE_ERR: MSLite Predict error.\n");
   23. return OH_AI_STATUS_LITE_ERROR;
   24. }
   25. LOGD("MS_LITE_LOG: Run MSLite model Predict success.\n");

   27. // 打印输出数据
   28. LOGD("MS_LITE_LOG: Get model outputs:\n");
   29. for (size_t i = 0; i < outputs.handle_num; i++) {
   30. auto tensor = outputs.handle_list[i];
   31. LOGD("MS_LITE_LOG: - Tensor %{public}d name is: %{public}s.\n", static_cast<int>(i),
   32. OH_AI_TensorGetName(tensor));
   33. LOGD("MS_LITE_LOG: - Tensor %{public}d size is: %{public}d.\n", static_cast<int>(i),
   34. (int)OH_AI_TensorGetDataSize(tensor));
   35. LOGD("MS_LITE_LOG: - Tensor data is:\n");
   36. auto out_data = reinterpret_cast<const float *>(OH_AI_TensorGetData(tensor));
   37. std::stringstream outStr;
   38. for (int i = 0; (i < OH_AI_TensorGetElementNum(tensor)) && (i <= K_NUM_PRINT_OF_OUT_DATA); i++) {
   39. outStr << out_data[i] << " ";
   40. }
   41. LOGD("MS_LITE_LOG: %{public}s", outStr.str().c_str());
   42. }
   43. return OH_AI_STATUS_SUCCESS;
   44. }
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L207-L251)
5. 调用以上方法，实现3个模型的推理流程。

   ```
   1. const float NEG_INF = -std::numeric_limits<float>::infinity();
   2. const int WHISPER_SOT = 50258;
   3. const int WHISPER_TRANSCRIBE = 50359;
   4. const int WHISPER_TRANSLATE = 50358;
   5. const int WHISPER_NO_TIMESTAMPS = 50363;
   6. const int WHISPER_EOT = 50257;
   7. const int WHISPER_BLANK = 220;
   8. const int WHISPER_NO_SPEECH = 50362;
   9. const int WHISPER_N_TEXT_CTX = 448;
   10. const int WHISPER_N_TEXT_STATE = 384;
   11. constexpr int WHISPER_SAMPLE_RATE = 16000;
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L45-L57)

   ```
   1. BinBuffer GetMSOutput(OH_AI_TensorHandle output)
   2. {
   3. float *outputData = reinterpret_cast<float *>(OH_AI_TensorGetMutableData(output));
   4. size_t size = OH_AI_TensorGetDataSize(output);
   5. return {outputData, size};
   6. }
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L263-L270)

   ```
   1. void SuppressTokens(BinBuffer &logits, bool isInitial)
   2. {
   3. auto logits_data = static_cast<float *>(logits.first);
   4. if (isInitial) {
   5. logits_data[WHISPER_EOT] = NEG_INF;
   6. logits_data[WHISPER_BLANK] = NEG_INF;
   7. }

   9. // 其他令牌的抑制
   10. logits_data[WHISPER_NO_TIMESTAMPS] = NEG_INF;
   11. logits_data[WHISPER_SOT] = NEG_INF;
   12. logits_data[WHISPER_NO_SPEECH] = NEG_INF;
   13. logits_data[WHISPER_TRANSLATE] = NEG_INF;
   14. }
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L280-L296)

   ```
   1. std::vector<int> LoopPredict(const OH_AI_ModelHandle model, const BinBuffer &n_layer_cross_k,
   2. const BinBuffer &n_layer_cross_v, const BinBuffer &logits_init,
   3. BinBuffer &out_n_layer_self_k_cache, BinBuffer &out_n_layer_self_v_cache,
   4. const BinBuffer &data_embedding, const int loop, const int offset_init)
   5. {
   6. BinBuffer logits{nullptr, 51865 * sizeof(float)};
   7. logits.first = malloc(logits.second);
   8. if (!logits.first) {
   9. LOGE("MS_LITE_ERR: Fail to malloc!\n");
   10. return {};
   11. }
   12. void *logits_init_src = static_cast<char *>(logits_init.first) + 51865 * 3 * sizeof(float);
   13. memcpy(logits.first, logits_init_src, logits.second);
   14. SuppressTokens(logits, true);

   16. std::vector<int> output_token;
   17. float *logits_data = static_cast<float *>(logits.first);
   18. int max_token_id = 0;
   19. float max_token = logits_data[0];
   20. for (int i = 0; i < logits.second / sizeof(float); i++) {
   21. if (logits_data[i] > max_token) {
   22. max_token_id = i;
   23. max_token = logits_data[i];
   24. }
   25. }

   27. int offset = offset_init;
   28. BinBuffer slice{nullptr, 0};
   29. slice.second = WHISPER_N_TEXT_STATE * sizeof(float);
   30. slice.first = malloc(slice.second);
   31. if (!slice.first) {
   32. LOGE("MS_LITE_ERR: Fail to malloc!\n");
   33. return {};
   34. }

   36. auto out_n_layer_self_k_cache_new = out_n_layer_self_k_cache;
   37. auto out_n_layer_self_v_cache_new = out_n_layer_self_v_cache;

   39. for (size_t i = 0; i < loop; i++) {
   40. if (max_token_id == WHISPER_EOT) {
   41. break;
   42. }
   43. output_token.push_back(max_token_id);
   44. std::vector<float> mask(WHISPER_N_TEXT_CTX, 0.0f);
   45. for (size_t i = 0; i < WHISPER_N_TEXT_CTX - offset - 1; ++i) {
   46. mask[i] = NEG_INF;
   47. }
   48. BinBuffer tokens{&max_token_id, sizeof(int)};

   50. void *data_embedding_src =
   51. static_cast<char *>(data_embedding.first) + offset * WHISPER_N_TEXT_STATE * sizeof(float);
   52. memcpy(slice.first, data_embedding_src, slice.second);
   53. BinBuffer mask_bin(mask.data(), mask.size() * sizeof(float));
   54. int ret = RunMSLiteModel(model, {tokens, out_n_layer_self_k_cache_new, out_n_layer_self_v_cache_new,
   55. n_layer_cross_k, n_layer_cross_v, slice, mask_bin});

   57. auto outputs = OH_AI_ModelGetOutputs(model);
   58. logits = GetMSOutput(outputs.handle_list[0]);
   59. out_n_layer_self_k_cache_new = GetMSOutput(outputs.handle_list[1]);
   60. out_n_layer_self_v_cache_new = GetMSOutput(outputs.handle_list[2]);
   61. offset++;
   62. SuppressTokens(logits, false);
   63. logits_data = static_cast<float *>(logits.first);
   64. max_token = logits_data[0];

   66. for (int j = 0; j < logits.second / sizeof(float); j++) {
   67. if (logits_data[j] > max_token) {
   68. max_token_id = j;
   69. max_token = logits_data[j];
   70. }
   71. }
   72. LOGI("MS_LITE_LOG: run decoder loop %{public}d ok!\n token = %{public}d", i, max_token_id);
   73. }
   74. return output_token;
   75. }

   77. std::vector<std::string> ProcessDataLines(const BinBuffer token_txt)
   78. {
   79. void *data_ptr = token_txt.first;
   80. size_t data_size = token_txt.second;
   81. std::vector<std::string> tokens;

   83. const char *char_data = static_cast<const char *>(data_ptr);
   84. std::stringstream ss(std::string(char_data, char_data + data_size));
   85. std::string line;
   86. while (std::getline(ss, line)) {
   87. size_t space_pos = line.find(' ');
   88. tokens.push_back(line.substr(0, space_pos));
   89. }
   90. return tokens;
   91. }

   93. static napi_value RunDemo(napi_env env, napi_callback_info info)
   94. {
   95. // 执行样例推理
   96. napi_value error_ret;
   97. napi_create_int32(env, -1, &error_ret);
   98. size_t argc = 1;
   99. napi_value argv[1] = {nullptr};
   100. napi_get_cb_info(env, info, &argc, argv, nullptr, nullptr);
   101. auto resourcesManager = OH_ResourceManager_InitNativeResourceManager(env, argv[0]);

   103. // 数据预处理
   104. AudioFile<float> audioFile;
   105. std::string filePath = "zh.wav";
   106. auto audioBin = ReadBinFile(resourcesManager, filePath);
   107. if (audioBin.first == nullptr) {
   108. LOGE("MS_LITE_ERR: Fail to read  %{public}s!", filePath.c_str());
   109. return error_ret;
   110. }
   111. size_t dataSize = audioBin.second;
   112. uint8_t *dataBuffer = (uint8_t *)audioBin.first;
   113. bool ok = audioFile.loadFromMemory(std::vector<uint8_t>(dataBuffer, dataBuffer + dataSize));
   114. if (!ok) {
   115. LOGE("MS_LITE_ERR: Fail to read  %{public}s!", filePath.c_str());
   116. return error_ret;
   117. }
   118. std::vector<float> data(audioFile.samples[0]);
   119. ResampleAudio(data, audioFile.getSampleRate(), WHISPER_SAMPLE_RATE, 1, SRC_SINC_BEST_QUALITY);
   120. std::vector<float> audio(data);

   122. int padding = 480000;
   123. int sr = 16000;
   124. int n_fft = 480;
   125. int n_hop = 160;
   126. int n_mel = 80;
   127. int fmin = 0; // 最小频率，默认值为0.0 Hz
   128. int fmax =
   129. sr /
   130. 2.0; // 最大频率，默认值为采样率（sr/2.0）的一半
   131. audio.insert(audio.end(), padding, 0.0f);
   132. std::vector<std::vector<float>> mels_T =
   133. librosa::Feature::melspectrogram(audio, sr, n_fft, n_hop, "hann", true, "reflect", 2.f, n_mel, fmin, fmax);
   134. std::cout << "mels: " << std::endl;

   136. std::vector<std::vector<float>> mels = TransposeMel(mels_T);
   137. ProcessMelSpectrogram(mels);

   139. std::vector<float> inputMels(mels.size() * mels[0].size(), 0);
   140. for (int i = 0; i < mels.size(); i++) {
   141. std::copy(mels[i].begin(), mels[i].end(), inputMels.begin() + i * mels[0].size());
   142. }

   144. BinBuffer inputMelsBin(inputMels.data(), inputMels.size() * sizeof(float));

   146. // tiny-encoder.ms模型推理
   147. auto encoderBin = ReadBinFile(resourcesManager, "tiny-encoder.ms");
   148. if (encoderBin.first == nullptr) {
   149. free(dataBuffer);
   150. dataBuffer = nullptr;
   151. return error_ret;
   152. }

   154. auto encoder = CreateMSLiteModel(encoderBin);

   156. int ret = RunMSLiteModel(encoder, {inputMelsBin});
   157. if (ret != OH_AI_STATUS_SUCCESS) {
   158. OH_AI_ModelDestroy(&encoder);
   159. return error_ret;
   160. }
   161. LOGI("MS_LITE_LOG: run encoder ok!\n");

   163. auto outputs = OH_AI_ModelGetOutputs(encoder);
   164. auto n_layer_cross_k = GetMSOutput(outputs.handle_list[0]);
   165. auto n_layer_cross_v = GetMSOutput(outputs.handle_list[1]);

   167. // tiny-decoder-main.ms模型推理
   168. std::vector<int> SOT_SEQUENCE = {WHISPER_SOT,
   169. WHISPER_SOT + 1 + 1,
   170. WHISPER_TRANSCRIBE, WHISPER_NO_TIMESTAMPS};
   171. BinBuffer sotSequence(SOT_SEQUENCE.data(), SOT_SEQUENCE.size() * sizeof(int));

   173. const std::string decoder_main_path = "tiny-decoder-main.ms";
   174. auto decoderMainBin = ReadBinFile(resourcesManager, decoder_main_path);
   175. if (decoderMainBin.first == nullptr) {
   176. OH_AI_ModelDestroy(&encoder);
   177. return error_ret;
   178. }
   179. auto decoder_main = CreateMSLiteModel(decoderMainBin);
   180. int ret2 = RunMSLiteModel(decoder_main, {sotSequence, n_layer_cross_k, n_layer_cross_v});

   182. if (ret2 != OH_AI_STATUS_SUCCESS) {
   183. OH_AI_ModelDestroy(&decoder_main);
   184. return error_ret;
   185. }
   186. LOGI("MS_LITE_LOG: run decoder_main ok!\n");

   188. auto decoderMainOut = OH_AI_ModelGetOutputs(decoder_main);
   189. auto logitsBin = GetMSOutput(decoderMainOut.handle_list[0]);
   190. auto out_n_layer_self_k_cache_Bin = GetMSOutput(decoderMainOut.handle_list[1]);
   191. auto out_n_layer_self_v_cache_Bin = GetMSOutput(decoderMainOut.handle_list[2]);

   193. // tiny-decoder-loop.ms模型推理
   194. const std::string modelName3 = "tiny-decoder-loop.ms";
   195. auto modelBuffer3 = ReadBinFile(resourcesManager, modelName3);
   196. auto decoder_loop = CreateMSLiteModel(modelBuffer3);

   198. const std::string dataName_embedding = "tiny-positional_embedding.bin"; // 获取输入数据
   199. auto data_embedding = ReadBinFile(resourcesManager, dataName_embedding);
   200. if (data_embedding.first == nullptr) {
   201. OH_AI_ModelDestroy(&encoder);
   202. OH_AI_ModelDestroy(&decoder_main);
   203. OH_AI_ModelDestroy(&decoder_loop);
   204. return error_ret;
   205. }

   207. int loop_times = WHISPER_N_TEXT_CTX - SOT_SEQUENCE.size();
   208. int offset_init = SOT_SEQUENCE.size();
   209. auto output_tokens =
   210. LoopPredict(decoder_loop, n_layer_cross_k, n_layer_cross_v, logitsBin, out_n_layer_self_k_cache_Bin,
   211. out_n_layer_self_v_cache_Bin, data_embedding, loop_times, offset_init);

   213. std::vector<std::string> token_tables = ProcessDataLines(ReadTokens(resourcesManager, "tiny-tokens.txt"));
   214. std::string result;
   215. for (const auto i : output_tokens) {
   216. char str[1024];
   217. base64_decode((const uint8 *)token_tables[i].c_str(), (uint32)token_tables[i].size(), str);
   218. result += str;
   219. }
   220. LOGI("MS_LITE_LOG: result is -> %{public}s", result.c_str());

   222. OH_AI_ModelDestroy(&encoder);
   223. OH_AI_ModelDestroy(&decoder_main);
   224. OH_AI_ModelDestroy(&decoder_loop);

   226. napi_value out_data;
   227. napi_create_string_utf8(env, result.c_str(), result.length(), &out_data);
   228. return out_data;
   229. }
   ```

   [mslite\_napi.cpp](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/mslite_napi.cpp#L374-L611)
6. 编写CMake脚本，链接MindSpore Lite动态库。

   ```
   1. # the minimum version of CMake.
   2. cmake_minimum_required(VERSION 3.5.0)
   3. project(test)
   4. # AudioFile.h
   5. set(CMAKE_CXX_STANDARD 17)
   6. set(CMAKE_CXX_STANDARD_REQUIRED TRUE)
   7. set(NATIVERENDER_PATH ${CMAKE_CURRENT_SOURCE_DIR})

   9. if(DEFINED PACKAGE_FIND_FILE)
   10. include(${PACKAGE_FIND_FILE})
   11. endif()

   13. include_directories(${NATIVERENDER_PATH}
   14. ${NATIVERENDER_PATH}/include)

   16. # libsamplerate
   17. set(LIBSAMPLERATE_DIR ${NATIVERENDER_PATH}/third_party/libsamplerate)
   18. include_directories(${LIBSAMPLERATE_DIR}/include)
   19. add_subdirectory(${LIBSAMPLERATE_DIR})

   21. include_directories(${NATIVERENDER_PATH}/third_party/opencc/include/opencc)
   22. # src
   23. aux_source_directory(src SRC_DIR)
   24. include_directories(${NATIVERENDER_PATH}/src)

   26. include_directories(${CMAKE_SOURCE_DIR}/third_party)

   28. file(GLOB SRC src/*.cc)

   30. add_library(entry SHARED mslite_napi.cpp ${SRC})
   31. target_link_libraries(entry PUBLIC samplerate)
   32. target_link_libraries(entry PUBLIC mindspore_lite_ndk)
   33. target_link_libraries(entry PUBLIC hilog_ndk.z)
   34. target_link_libraries(entry PUBLIC rawfile.z)
   35. target_link_libraries(entry PUBLIC ace_napi.z)
   ```

### 使用N-API将C++动态库封装成ArkTS模块

1. 在 entry/src/main/cpp/types/libentry/Index.d.ts，定义ArkTS接口runDemo() 。内容如下：

   ```
   1. export const runDemo: (a: Object) => string;
   ```

   [Index.d.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/cpp/types/libentry/Index.d.ts#L16-L18)
2. 在 oh-package.json5 文件，将API与so相关联，成为一个完整的ArkTS模块：

   ```
   1. {
   2. "name": "libentry.so",
   3. "types": "./Index.d.ts",
   4. "version": "1.0.0",
   5. "description": "MindSpore Lite inference module."
   6. }
   ```

### 调用封装的ArkTS模块进行推理并输出结果

在 entry/src/main/ets/pages/Index.ets 中，调用封装的ArkTS模块，最后对推理结果进行处理。若提示@nutpi/chinese\_transverter不存在，请参考[中文简繁体转换器三方库](https://developer.huawei.com/consumer/cn/forum/topic/0202169478029484501?fid=0109140870620153026)安装@nutpi/chinese\_transverter组件。

```
1. // Index.ets
2. import msliteNapi from 'libentry.so'
3. import AVPlayerDemo from './player';
4. import { transverter, TransverterType, TransverterLanguage } from "@nutpi/chinese_transverter"
5. import { hilog } from '@kit.PerformanceAnalysisKit';

7. const TAG = 'MindSporeLite';

9. @Entry
10. @Component
11. struct Index {
12. @State message: string = 'MSLite Whisper Demo';
13. @State wavName: string = 'zh.wav';
14. @State content: string = '';

16. build() {
17. Row() {
18. Column() {
19. Text(this.message)
20. .fontSize(30)
21. .fontWeight(FontWeight.Bold);
22. Button() {
23. Text('播放示例音频')
24. .fontSize(20)
25. .fontWeight(FontWeight.Medium)
26. }
27. .type(ButtonType.Capsule)
28. .margin({
29. top: 20
30. })
31. .backgroundColor('#0D9FFB')
32. .width('40%')
33. .height('5%')
34. .onClick(async () =>{
35. // 通过实例调用类中的函数
36. hilog.info(0xFF00, TAG, '%{public}s', `MS_LITE_LOG: begin to play wav.`);
37. let myClass = new AVPlayerDemo();
38. myClass.avPlayerFdSrcDemo();
39. })
40. Button() {
41. Text('识别示例音频')
42. .fontSize(20)
43. .fontWeight(FontWeight.Medium)
44. }
45. .type(ButtonType.Capsule)
46. .margin({
47. top: 20
48. })
49. .backgroundColor('#0D9FFB')
50. .width('40%')
51. .height('5%')
52. .onClick(() => {
53. let resMgr = this.getUIContext()?.getHostContext()?.getApplicationContext().resourceManager;
54. if (resMgr === undefined || resMgr === null) {
55. hilog.error(0xFF00, TAG, '%{public}s', `MS_LITE_ERR: get resourceManager failed.`);
56. return
57. }
58. // 调用封装的runDemo函数
59. hilog.info(0xFF00, TAG, '%{public}s', `MS_LITE_LOG: *** Start MSLite Demo ***`);
60. let output = msliteNapi.runDemo(resMgr);
61. if (output === null || output.length === 0) {
62. hilog.error(0xFF00, TAG, '%{public}s', `MS_LITE_ERR: runDemo failed.`);
63. return
64. }
65. hilog.info(0xFF00, TAG, '%{public}s',
66. `MS_LITE_LOG: output length = ${output.length}; value = ${output.slice(0, 20)}`);
67. this.content = output;
68. hilog.info(0xFF00, TAG, '%{public}s', `MS_LITE_LOG: *** Finished MSLite Demo ***`);
69. })

71. // 显示识别内容
72. if (this.content) {
73. Text('识别内容: \n' + transverter({
74. type: TransverterType.SIMPLIFIED,
75. str: this.content,
76. language: TransverterLanguage.ZH_CN
77. }) + '\n').focusable(true).fontSize(20).height('20%')
78. }
79. }.width('100%')
80. }
81. .height('100%')
82. }
83. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/MindSporeLiteKit/MindSporeLiteCDemoASR/entry/src/main/ets/pages/Index.ets#L16-L99)

### 调测验证

1. 在DevEco Studio中连接设备，点击Run entry，编译Hap，有如下显示：

   ```
   1. Launching com.samples.mindsporelitecdemoasr
   2. $ hdc shell aa force-stop com.samples.mindsporelitecdemoasr
   3. $ hdc shell mkdir data/local/tmp/xxx
   4. $ hdc file send E:\xxx\entry\build\default\outputs\default\entry-default-signed.hap "data/local/tmp/xxx"
   5. $ hdc shell bm install -p data/local/tmp/xxx
   6. $ hdc shell rm -rf data/local/tmp/xxx
   7. $ hdc shell aa start -a EntryAbility -b com.samples.mindsporelitecdemoasr
   8. com.samples.mindsporelitecdemoasr successfully launched...
   ```
2. 在设备屏幕点击播放示例音频按钮，会播放本示例音频文件。点击识别示例音频按钮，设备屏幕显示本示例音频文件的中文内容。在日志打印结果中，过滤关键字”MS\_LITE\_LOG“，可得到如下结果：

   ```
   1. 05-16 14:53:44.200   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: begin to play wav.
   2. 05-16 14:53:44.210   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     [a92ab1e0f831191, 0, 0] MS_LITE_LOG: AVPlayer state initialized called.
   3. 05-16 14:53:44.228   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     [a92ab1e0f831191, 0, 0] MS_LITE_LOG: AVPlayer state prepared called.
   4. 05-16 14:53:44.242   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: AVPlayer state playing called.
   5. 05-16 14:53:44.242   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: AVPlayer start to seek.
   6. 05-16 14:53:44.372   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: AVPlayer seek succeeded, seek time is 0
   7. 05-16 14:53:49.621   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: AVPlayer state completed called.
   8. 05-16 14:53:49.646   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: AVPlayer state stopped called.
   9. 05-16 14:53:49.647   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: AVPlayer state idle called.
   10. 05-16 14:53:49.649   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: AVPlayer state released called.
   11. 05-16 14:53:53.282   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: *** Start MSLite Demo ***
   12. 05-16 14:53:53.926   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  I     MS_LITE_LOG: Build MSLite model success.
   13. 05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: Run MSLite model Predict success.
   14. 05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: Get model outputs:
   15. 05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: - Tensor 0 name is: n_layer_cross_k.
   16. 05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: - Tensor 0 size is: 9216000.
   17. 05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: - Tensor data is:
   18. 05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: -1.14678 -2.30223 0.868679 0.284441 1.03233 -2.02062 0.688163 -0.732034 -1.10553 1.43459 0.083885 -0.116173 -0.772636 1.5466 -0.631993 -0.897929 -0.0501685 -1.62517 0.375988 -1.77772 -0.432178
   19. 05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: - Tensor 1 name is: n_layer_cross_v.
   20. 05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: - Tensor 1 size is: 9216000.
   21. 05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: - Tensor data is:
   22. 05-16 14:53:54.260   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: 0.0876085 -0.560317 -0.652518 -0.116969 -0.182608 -9.40531e-05 0.186293 0.123206 0.0127445 0.0708352 -0.489624 -0.226322 -0.0686949 -0.0341293 -0.0719619 0.103588 0.398025 -0.444261 0.396124 -0.347295 0.00541205
   23. 05-16 14:53:54.430   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  I     MS_LITE_LOG: Build MSLite model success.
   24. 05-16 14:53:54.462   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  D     MS_LITE_LOG: Run MSLite model Predict success.
   25. ......
   26. 05-16 14:53:55.272   1679-1679     A00000/[MSLiteNapi]             com.sampl...cdemoasr  I     MS_LITE_LOG: run decoder loop 16 ok!
   27. token = 50257
   28. 05-16 14:53:55.334   1679-1679     A03d00/JSAPP                    com.sampl...cdemoasr  I     MS_LITE_LOG: *** Finished MSLite Demo ***
   ```

### 效果示意

在设备上，点击**播放示例音频**按钮，会播放本示例音频文件。点击**识别示例音频**按钮，设备屏幕显示本示例音频文件的中文内容。

| 初始页面 | 点击识别示例音频按钮后 |
| --- | --- |
|  |  |

## 示例代码

* [基于MindSporeLite接口实现语音识别（C/C++）](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/MindSporeLiteKit/MindSporeLiteCDemoASR)
