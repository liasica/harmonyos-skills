---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-record-overview
title: 概述
breadcrumb: 最佳实践 > 媒体 > 音频和视频 > 音频录制系列开发实践 > 概述
category: best-practices
scraped_at: 2026-04-28T08:20:38+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:9905408cb53ad58be329a7729577584b8b50bc878c8ecb9d83b945c3dbbb28ba
---

音频录制是媒体开发的常见场景，在系统中，根据不同的音频格式和业务场景，提供了多样化的音频录制方式。为了帮助开发者快速了解音频录制功能，并且根据不同的音频格式和业务场景快速选型，提供了音频录制开发实践的系列文章。共有如下五篇：

* [基于AudioCapturer录制PCM音频（ArkTS）](bpta-audio-record-base-on-audiocapturer.md)：AudioCapturer是用于音频录制的ArkTS API，仅支持录制PCM格式，需要开发者具备音频处理的基础知识，适用于更专业、更多样化的音频录制开发。此文指导开发者使用AudioCapturer接口实现录制PCM音频的功能，主要涉及音频基础录制。
* [基于OHAudio录制PCM音频（C++）](bpta-audio-record-base-on-ohaudio.md)：在C/C++侧，OHAudio提供音频模块相关能力，包含音频采集OH\_AudioCapturer、音频管理、音频播放等能力。OH\_AudioCapturer仅支持录制PCM格式，适用于在C/C++层实现音频输入功能的场景，可以实现普通音频通路录制和低时延通路录制。此文指导开发者在C/C++侧使用OHAudio接口实现录制PCM音频的功能。
* [基于AVRecorder录制格式化音频（ArkTS）](bpta-audio-record-base-on-avrecorder-arkts.md)：AVRecorder集成了音频输入录制、音频编码和媒体封装的功能，可以用于音频录制，输出文件格式支持m4a、mp3等格式。AVRecorder提供了ArkTS API和Native API，便于快速实现音频录制。例如，开发者可以直接调用设备硬件如麦克风录音，并生成m4a音频文件。此文指导开发者使用AVRecorder接口实现录制格式化音频的功能。
* [基于AVRecorder录制格式化音频（C++）](bpta-audio-record-base-on-avrecorder.md)：此文指导开发者使用AVRecorder的Native API实现录制格式化音频的功能。例如，开发者可以直接调用设备硬件如麦克风录音，并生成m4a音频文件。
* [基于AVScreenCapture录制音频](bpta-audio-record-base-on-avscreencapture.md)：AVScreenCapture用于设备的屏幕录制，同时具备采集设备内、麦克风音频的能力。在录制音频文件时，仅支持录制m4a的音频格式。此文指导开发者使用AVScreenCapture接口实现录制格式化音频的功能。

各方案音频录制支持的能力对比如下所示：

|  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| **开发方式** | **录制文件格式** | **是否支持低时延** | **是否支持静音打断模式** | **是否支持回声消除** | **如何获取音频振幅** |
| **AudioCapturer（ArkTS）** | 仅支持PCM格式 | 不支持 | 通过调用setWillMuteWhenInterrupted接口设置是否开启静音打断模式 | 通过将audio.AudioCapturerInfo中SourceType值指定为SOURCE\_TYPE\_VOICE\_COMMUNICATION、SOURCE\_TYPE\_LIVE即可 | 通过调用AudioVolumeGroupManager中的getMaxAmplitudeForInputDevice接口获取输入设备音频流的最大电平值 |
| **OHAudio（C++）** | 仅支持PCM格式 | 通过调用OH\_AudioStreamBuilder\_SetLatencyMode()设置低时延模式 | 通过调用OH\_AudioStreamBuilder\_SetCapturerWillMuteWhenInterrupted接口设置是否开启静音打断模式 | 通过将OH\_AudioStream\_SourceType值指定为AUDIOSTREAM\_SOURCE\_TYPE\_VOICE\_COMMUNICATION、AUDIOSTREAM\_SOURCE\_TYPE\_LIVE即可 | 通过采样深度（采样格式）计算最大采样值，然后将每个采样值与最大采样值做归一化处理计算可获得类似振幅大小数据 |
| **AVRecorder（ArkTS）** | 格式化音频文件 | 不支持 | 通过调用setWillMuteWhenInterrupted接口设置是否开启静音打断模式 | 通过将AudioSourceType值指定为AUDIO\_SOURCE\_TYPE\_VOICE\_COMMUNICATION即可 | 通过调用getAudioCapturerMaxAmplitude接口获取当前音频最大振幅 |
| **AVRecorder（C++）** | 格式化音频文件 | 不支持 | 通过调用OH\_AVRecorder\_SetWillMuteWhenInterrupted接口设置是否开启静音打断模式 | 通过将OH\_AVRecorder\_AudioSourceType值指定为AVRECORDER\_VOICE\_COMMUNICATION即可 | 通过采样深度（采样格式）计算最大采样值，然后将每个采样值与最大采样值做归一化处理计算可获得类似振幅大小数据 |
| **AVScreenCapture（C++）** | 在录制音频文件时，仅支持录制m4a的音频格式 | 不支持 | 不支持 | 不支持 | 通过调用AudioVolumeGroupManager中的getMaxAmplitudeForInputDevice接口获取输入设备音频流的最大电平值 |

说明

* 应用可以调用麦克风录制音频，但该行为属于隐私敏感行为，在调用麦克风前，需要先[向用户申请授权](../harmonyos-guides/request-user-authorization.md)：ohos.permission.MICROPHONE。如何使用和管理麦克风请参考[管理麦克风静音状态](../harmonyos-guides/mic-management.md)。
* 如果需要持续录制或后台录制，请申请长时任务避免进入挂起（Suspend）状态。具体参考[长时任务开发指导](../harmonyos-guides/continuous-task.md)。录制需要在前台启动，启动后可以退后台。在后台启动录制将会失败。
* 应用录制音频时需要使用合适的录制流类型，请参考[使用合适的音频流类型](../harmonyos-guides/using-right-streamusage-and-sourcetype.md)。
