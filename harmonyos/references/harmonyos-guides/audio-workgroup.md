---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-workgroup
title: 音频工作组管理
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频性能调优 > 音频工作组管理
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:45+08:00
doc_updated_at: 2026-09-04
content_hash: sha256:dd6f45bfde5fd74b9a68d7af6dfa5a589640b2c4af792b63a17d5624f9b92934
---

音频工作组是一套通过标记来帮助系统识别应用内音频关键线程的接口，系统通过应用提供的关键音频线程以及工作组运行信息可以提升音频线程运行的稳定性。

以下各步骤示例为代码片段，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioRendererSampleC)。

## 使用说明

对于播放音频类应用，开发者需要先创建音频工作组，再将工作组运行信息周期性地告知系统。当工作结束后，需要对音频工作组进行清理。

### 创建音频工作组示例

开发者在使用OH\_AudioWorkgroup的API前，需要先用[OH\_AudioManager\_GetAudioResourceManager](../harmonyos-references/capi-native-audio-resource-manager-h.md#oh_audiomanager_getaudioresourcemanager)获取OH\_AudioResourceManager实例。

```
#include <ohaudio/native_audio_resource_manager.h>
// ...
OH_AudioResourceManager *resMgr;
// ...
    OH_AudioManager_GetAudioResourceManager(&resMgr);
```

### 创建音频工作组并将关键线程加入音频工作组

开发者先使用[OH\_AudioResourceManager\_CreateWorkgroup](../harmonyos-references/capi-native-audio-resource-manager-h.md#oh_audioresourcemanager_createworkgroup)创建一个新的音频工作组，再使用[OH\_AudioWorkgroup\_AddCurrentThread](../harmonyos-references/capi-native-audio-resource-manager-h.md#oh_audioworkgroup_addcurrentthread)将关键线程加入音频工作组。

```
#include <chrono>
// ...
int32_t g_tokenId;
OH_AudioWorkgroup *grp = nullptr;
// ...
    OH_AudioResourceManager_CreateWorkgroup(resMgr, "workgroup", &grp);
    OH_AudioWorkgroup_AddCurrentThread(grp, &g_tokenId);
```

### 通知系统音频工作组的开始与结束

当音频工作组开始一个工作周期时，开发者可以通知系统任务的开始时间和预期完成时间。在音频工作组完成当前周期内的工作时，开发者应再次通知系统任务已结束。

```
constexpr static uint64_t intervalMs = 20;
bool threadShouldRun = true;

while (threadShouldRun) {
    auto now = std::chrono::system_clock::now().time_since_epoch();
    auto startTimeMs = std::chrono::duration_cast<std::chrono::milliseconds>(now).count();
    OH_AudioWorkgroup_Start(grp, startTimeMs, startTimeMs + intervalMs);
    // 此处为示例逻辑，实际开发中应根据业务需求控制线程运行周期。
    threadShouldRun = false;
    // 应用音频数据处理。
    OH_AudioWorkgroup_Stop(grp);
}
```

### 工作组任务结束后进行清理

```
// 当线程不再需要参与工作组任务时，将其从工作组中移除。
OH_AudioWorkgroup_RemoveThread(grp, g_tokenId);

OH_AudioResourceManager_ReleaseWorkgroup(resMgr, grp);
grp = nullptr;
```
