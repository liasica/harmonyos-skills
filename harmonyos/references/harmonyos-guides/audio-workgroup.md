---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-workgroup
title: 音频工作组管理
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频性能调优 > 音频工作组管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:c319925763751fad3cccd9d7e4051753d01d32a63ca7f40d9e7b0ed69149137b
---

音频工作组是一套通过标记来帮助系统识别应用内音频关键线程的接口，系统通过应用提供的关键音频线程以及工作组运行信息可以让音频线程的运行状态更加健康。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioRendererSampleC)。

## 使用说明

对于播放音频类应用，开发者需要先创建音频工作组，再将工作组运行信息的周期性告知系统。当工作结束后，需要对音频工作组进行清理。

### 创建音频工作组示例

开发者在使用OH\_AudioWorkgroup的API前，需要先用[OH\_AudioManager\_GetAudioResourceManager](../harmonyos-references/capi-native-audio-resource-manager-h.md#oh_audiomanager_getaudioresourcemanager)获取OH\_AudioResourceManager实例。

```
1. #include <ohaudio/native_audio_resource_manager.h>
2. // ...
3. OH_AudioResourceManager *resMgr;
4. // ...
5. OH_AudioManager_GetAudioResourceManager(&resMgr);
```

### 创建音频工作组并将关键线程加入音频工作组

开发者先使用[OH\_AudioResourceManager\_CreateWorkgroup](../harmonyos-references/capi-native-audio-resource-manager-h.md#oh_audioresourcemanager_createworkgroup)创建一个新的音频工作组，再使用[OH\_AudioWorkgroup\_AddCurrentThread](../harmonyos-references/capi-native-audio-resource-manager-h.md#oh_audioworkgroup_addcurrentthread)将关键线程加入音频工作组。

```
1. #include <chrono>
2. // ...
3. int32_t g_tokenId;
4. OH_AudioWorkgroup *grp = nullptr;
5. // ...
6. OH_AudioResourceManager_CreateWorkgroup(resMgr, "workgroup", &grp);
7. OH_AudioWorkgroup_AddCurrentThread(grp, &g_tokenId);
```

### 通知系统音频工作组的开始与结束

当音频工作组开始一个工作周期时，开发者可以通知系统任务的开始时间和预期完成时间。在音频工作组完成当前周期内的工作时，开发者应再次通知系统任务已结束。

```
1. constexpr static uint64_t intervalMs = 20;
2. bool threadShouldRun = true;

4. while (threadShouldRun) {
5. auto now = std::chrono::system_clock::now().time_since_epoch();
6. auto startTimeMs = std::chrono::duration_cast<std::chrono::milliseconds>(now).count();
7. OH_AudioWorkgroup_Start(grp, startTimeMs, startTimeMs + intervalMs);
8. threadShouldRun = false;
9. // 应用音频数据处理。
10. OH_AudioWorkgroup_Stop(grp);
11. }
```

### 工作组任务结束后进行清理

```
1. // 当线程已经不需要接入分组时，将其从工作组中移除。
2. OH_AudioWorkgroup_RemoveThread(grp, g_tokenId);

4. OH_AudioResourceManager_ReleaseWorkgroup(resMgr, grp);
5. grp = nullptr;
```
