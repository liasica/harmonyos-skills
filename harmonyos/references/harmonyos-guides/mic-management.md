---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/mic-management
title: 管理麦克风静音状态
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频录制 > 管理麦克风静音状态
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9c5c552c3cd37e6e7b62efc2c2af362010eb9ed67ace2236684446fbbc5ce27c
---

因为在录制过程中需要使用麦克风录制相关音频数据，所以建议开发者在调用录制接口前查询麦克风状态，并在录制过程中监听麦克风的状态变化，避免影响录制效果。

在音频录制过程中，用户可以将麦克风静音，此时录音过程正常进行，录制生成的数据文件的大小随录制时长递增，但写入文件的数据均为0，即无声数据（空白数据）。

录音不支持音量调节。

## 开发步骤及注意事项

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioCaptureSampleJS)。

在AudioVolumeGroupManager中提供了管理麦克风状态的方法，接口的详细说明请参考音量API文档[AudioVolumeGroupManager](../harmonyos-references/arkts-apis-audio-audiovolumegroupmanager.md)。

1. 创建audioVolumeGroupManager对象。

   ```typescript
   import { audio } from '@kit.AudioKit';

   let audioVolumeGroupManager: audio.AudioVolumeGroupManager;
   // 创建audioVolumeGroupManager对象。
   async function loadVolumeGroupManager(updateCallback?: (msg: string, isError: boolean) => void): Promise<void> {
     const groupid = audio.DEFAULT_VOLUME_GROUP_ID;
     audioVolumeGroupManager = await audio.getAudioManager().getVolumeManager().getVolumeGroupManager(groupid);
     console.info('audioVolumeGroupManager create success.');
     // ...
   }
   ```
2. 调用[on('micStateChange')](../harmonyos-references/arkts-apis-audio-audiovolumegroupmanager.md#onmicstatechange9)监听麦克风状态变化，当麦克风静音状态发生变化时将通知应用。

   目前此订阅接口在单进程多[AudioManager](../harmonyos-references/arkts-apis-audio-audiomanager.md)实例的使用场景下，仅最后一个实例的订阅生效，其他实例的订阅会被覆盖（即使最后一个实例未订阅），因此推荐使用单一AudioManager实例进行开发。

   ```typescript
   // 监听麦克风状态变化。
   async function on() {
     audioVolumeGroupManager.on('micStateChange', (micStateChange: audio.MicStateChangeEvent) => {
       console.info(`Current microphone status is: ${micStateChange.mute} `);
     });
   }
   ```
3. 调用[isMicrophoneMute](../harmonyos-references/arkts-apis-audio-audiovolumegroupmanager.md#ismicrophonemute9)查询麦克风当前静音状态，返回true为静音，false为非静音。

   ```typescript
   // 查询麦克风是否静音。
   async function isMicrophoneMute(updateCallback?: (msg: string, isError: boolean) => void): Promise<void> {
     await audioVolumeGroupManager.isMicrophoneMute().then((value: boolean) => {
       console.info(`isMicrophoneMute is: ${value}.`);
       // ...
     });
   }
   ```
