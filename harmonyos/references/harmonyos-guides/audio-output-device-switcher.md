---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-output-device-switcher
title: 实现音频输出设备路由切换
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频设备路由管理 > 实现音频输出设备路由切换
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:154d10c4f65426c33835a7550b735a672ec332195b29304721d77476e62fb24d
---

当应用进行音频输出时，系统会根据音频流类型选择对应的输出设备（[STREAM\_USAGE\_MUSIC](../harmonyos-references/arkts-apis-audio-e.md#streamusage)：扬声器发声；[STREAM\_USAGE\_VOICE\_COMMUNICATION](../harmonyos-references/arkts-apis-audio-e.md#streamusage)：听筒发声）。如果系统提供的默认输出设备不满足应用需求，应用可通过AVCastPicker或setDefaultOutputDevice实现音频输出设备路由切换。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioRoutingManagerSampleJS)。

## 媒体类应用实现输出设备路由切换

应用可使用[AVCastPicker](../harmonyos-references/ohos-multimedia-avcastpicker.md#avcastpicker)投播组件进行媒体类应用输出设备路由切换。

## 通话类应用实现输出设备路由切换

### 外接设备路由切换

应用可[使用通话设备切换组件](using-switch-call-devices.md)进行通话类应用外接输出设备路由切换。

### 内置听筒和扬声器路由切换

如果未连接外设，语音通话场景系统默认听筒发声，其他场景系统默认扬声器发声；如果连接了外设，系统默认通过外接设备发声。

调用setDefaultOutputDevice设置音频输出设备后，如需取消，可将参数设为audio.DeviceType.DEFAULT，将音频输出设备选择权交还给系统。

1. 从API version 12开始，应用可使用AudioRenderer的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setdefaultoutputdevice12)设置听筒和扬声器路由切换，调用前需要先获取[AudioRenderer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)实例。

   说明

   * 由于AudioRenderer是流级别，调用本接口设置的默认音频输出设备仅对当前流生效。
   * 本接口优先级低于AudioSessionManager的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)。如果使用AudioSessionManager的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)设置了默认音频输出设备，本接口的设置将不会生效。

   ```
   1. import { audio } from '@kit.AudioKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. // ...
   4. // 设置默认输出设备为本机扬声器。
   5. audioRenderer.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
   6. console.info('Succeeded in setting default output device.');
   7. // ...
   8. }).catch((err: BusinessError) => {
   9. console.error(`Failed to set default output device. Code: ${err.code}, message: ${err.message}`);
   10. // ...
   11. });
   12. // ...
   13. // 设置默认输出设备为系统默认输出设备,即取消应用设置的默认设备,交由系统选择设备。
   14. audioRenderer.setDefaultOutputDevice(audio.DeviceType.DEFAULT).then(() => {
   15. console.info('Succeeded in setting default output device.');
   16. // ...
   17. }).catch((err: BusinessError) => {
   18. console.error(`Failed to set default output device. Code: ${err.code}, message: ${err.message}`);
   19. // ...
   20. });
   ```
2. 从API version 20开始，应用可使用AudioSessionManager的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)设置听筒和扬声器路由切换。

   说明

   由于AudioSessionManager是应用级设置，调用本接口设置默认音频输出设备，会对当前应用所有适用范围内的音频流生效，且会覆盖AudioRenderer的[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiorenderer.md#setdefaultoutputdevice12)接口设置的默认音频输出设备信息。

   ```
   1. import { audio } from '@kit.AudioKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';
   3. // ...

   5. let audioManager = audio.getAudioManager();
   6. // 创建音频会话管理器。
   7. let audioSessionManager: audio.AudioSessionManager = audioManager.getSessionManager();
   8. // ...

   10. // 设置音频并发模式。
   11. let strategy: audio.AudioSessionStrategy = {
   12. concurrencyMode: audio.AudioConcurrencyMode.CONCURRENCY_MIX_WITH_OTHERS
   13. };

   15. // 激活音频会话。
   16. audioSessionManager.activateAudioSession(strategy).then(() => {
   17. console.info('Succeeded in activating audio session.');
   18. // ...
   19. }).catch((err: BusinessError) => {
   20. console.error(`Failed to activate audio session. Code: ${err.code}, message: ${err.message}`);
   21. // ...
   22. });

   24. // ...
   25. // 设置默认输出设备为听筒。
   26. audioSessionManager.setDefaultOutputDevice(audio.DeviceType.EARPIECE).then(() => {
   27. console.info('Succeeded in setting default output device.');
   28. // ...
   29. }).catch((err: BusinessError) => {
   30. console.error(`Failed to set default output device. Code: ${err.code}, message: ${err.message}`);
   31. // ...
   32. });
   33. // ...

   35. // 设置默认输出设备为默认设备,即取消应用设置的默认设备,交由系统选择设备。
   36. audioSessionManager.setDefaultOutputDevice(audio.DeviceType.DEFAULT).then(() => {
   37. console.info('Succeeded in setting default output device.');
   38. }).catch((err: BusinessError) => {
   39. console.error(`Failed to set default output device. Code: ${err.code}, message: ${err.message}`);
   40. });
   ```
