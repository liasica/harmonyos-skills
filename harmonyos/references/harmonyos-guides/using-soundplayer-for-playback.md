---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/using-soundplayer-for-playback
title: 使用SoundPlayer开发系统音效播放功能
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频播放 > 使用SoundPlayer开发系统音效播放功能
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:743637c045175a237787a7198968c2b50d1d9923c2cd795254a9b147bf93b468
---

从API version 23开始，支持系统音效播放。

SoundPlayer提供系统音效播放功能，适用于拍照或录像提示音，比如在开始拍照、开始录像或结束录像时播放提示音。

## 支持的音效类型

支持的音效类型[SystemSoundType](../harmonyos-references/js-apis-systemsoundmanager.md#systemsoundtype)信息如下表所示。可通过systemSoundManager.SystemSoundType.PHOTO\_SHUTTER等具体类型，作为[load](../harmonyos-references/js-apis-inner-multimedia-systemsoundplayer.md#load)、[play](../harmonyos-references/js-apis-inner-multimedia-systemsoundplayer.md#play)或[unload](../harmonyos-references/js-apis-inner-multimedia-systemsoundplayer.md#unload)方法的入参。

| 播放音效类型 | 值 | 说明 |
| --- | --- | --- |
| PHOTO\_SHUTTER | 0 | 拍照音效。 |
| VIDEO\_RECORDING\_BEGIN | 1 | 视频录制开始音效。 |
| VIDEO\_RECORDING\_END | 2 | 视频录制结束音效。 |

## 开发步骤

以下各步骤示例为片段代码，可通过点击示例代码右下方的链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/SystemSoundPlayer)。

1. 在调用SystemSoundPlayer的接口前，需要先通过[createSystemSoundPlayer](../harmonyos-references/js-apis-systemsoundmanager.md#systemsoundmanagercreatesystemsoundplayer)创建实例。

   ```
   1. import { systemSoundManager } from '@kit.AudioKit';
   2. // ...

   4. // SystemSoundPlayer对象。
   5. let systemSoundPlayer: systemSoundManager.SystemSoundPlayer | null = null;

   7. // ...
   8. systemSoundManager.createSystemSoundPlayer().then((systemSoundPlayerInstance) => {
   9. console.info('Succeeded in creating the system sound player.');
   10. systemSoundPlayer = systemSoundPlayerInstance;
   11. }).catch((err: BusinessError) => {
   12. console.error(`Failed to create the system sound player. Code: ${err.code}, message: ${err.message}`);
   13. });
   ```

   [SoundPlayer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Audio/SystemSoundPlayer/entry/src/main/ets/pages/SoundPlayer.ets#L17-L52)
2. 调用[load](../harmonyos-references/js-apis-inner-multimedia-systemsoundplayer.md#load)接口，加载指定类型音效资源。

   ```
   1. import { systemSoundManager } from '@kit.AudioKit';
   2. // ...

   4. // 音效类型。
   5. let systemSoundType: systemSoundManager.SystemSoundType = systemSoundManager.SystemSoundType.PHOTO_SHUTTER;

   7. // ...
   8. systemSoundPlayer?.load(systemSoundType).then(() => {
   9. console.info('Succeeded in calling the load method.');
   10. }).catch((err: BusinessError) => {
   11. console.error(`Failed to call the load method. Code: ${err.code}, message: ${err.message}`);
   12. });
   ```

   [SoundPlayer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Audio/SystemSoundPlayer/entry/src/main/ets/pages/SoundPlayer.ets#L18-L63)
3. 调用[play](../harmonyos-references/js-apis-inner-multimedia-systemsoundplayer.md#play)接口，播放已加载的音效资源。

   ```
   1. import { systemSoundManager } from '@kit.AudioKit';
   2. // ...

   4. // 音效类型。
   5. let systemSoundType: systemSoundManager.SystemSoundType = systemSoundManager.SystemSoundType.PHOTO_SHUTTER;

   7. // ...
   8. systemSoundPlayer?.play(systemSoundType).then(() => {
   9. console.info('Succeeded in calling the play method.');
   10. }).catch((err: BusinessError) => {
   11. console.error(`Failed to call the play method. Code: ${err.code}, message: ${err.message}`);
   12. });
   ```

   [SoundPlayer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Audio/SystemSoundPlayer/entry/src/main/ets/pages/SoundPlayer.ets#L19-L74)
4. 调用[unload](../harmonyos-references/js-apis-inner-multimedia-systemsoundplayer.md#unload)接口，卸载之前已加载的音效资源。

   ```
   1. import { systemSoundManager } from '@kit.AudioKit';
   2. // ...

   4. // 音效类型。
   5. let systemSoundType: systemSoundManager.SystemSoundType = systemSoundManager.SystemSoundType.PHOTO_SHUTTER;

   7. // ...
   8. systemSoundPlayer?.unload(systemSoundType).then(() => {
   9. console.info('Succeeded in calling the unload method.');
   10. }).catch((err: BusinessError) => {
   11. console.error(`Failed to call the unload method. Code: ${err.code}, message: ${err.message}`);
   12. });
   ```

   [SoundPlayer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Audio/SystemSoundPlayer/entry/src/main/ets/pages/SoundPlayer.ets#L20-L85)
5. 调用[release](../harmonyos-references/js-apis-inner-multimedia-systemsoundplayer.md#release)接口，释放系统音效播放器。

   ```
   1. systemSoundPlayer?.release().then(() => {
   2. console.info('Succeeded in calling the release method.');
   3. }).catch((err: BusinessError) => {
   4. console.error(`Failed to call the release method. Code: ${err.code}, message: ${err.message}`);
   5. });
   ```

   [SoundPlayer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/Media/Audio/SystemSoundPlayer/entry/src/main/ets/pages/SoundPlayer.ets#L90-L96)
