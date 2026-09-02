---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-playback-stream-management
title: 音频播放流管理
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频播放 > 音频播放流管理
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:42+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e916b999464573f12074994b39945544cd0b65a102f1307a16ab3fe497b014f7
---

对于播放音频类的应用，开发者需要关注该应用的音频流的状态以做出相应的操作，比如监听到状态为播放中/暂停时，及时改变播放按钮的UI显示。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioRendererSampleJS)。

## 读取或监听应用内音频流状态变化

参考[使用AudioRenderer开发音频播放功能(ArkTS)](using-audiorenderer-for-playback.md)或[audio.createAudioRenderer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)，先完成AudioRenderer的创建，再通过以下两种方法查看音频流状态的变化。

* 方法1：直接查看AudioRenderer的[属性](../harmonyos-references/arkts-apis-audio-audiorenderer.md#属性)state：

  ```typescript
  import { audio } from '@kit.AudioKit';
  // ...
      let audioRendererState: audio.AudioState = audioRenderer.state;
      console.info(`Current state is: ${audioRendererState}`);
  ```
* 方法2：注册stateChange监听AudioRenderer的状态变化：

  ```typescript
  import { audio } from '@kit.AudioKit';
  // ...
      audioRenderer.on('stateChange', (rendererState: audio.AudioState) => {
        console.info(`Succeeded in using on function, state change to: ${rendererState}`);
        // ...
      });
  ```

获取state后可对照[AudioState](../harmonyos-references/arkts-apis-audio-e.md#audiostate8)来进行相应的操作，比如更改暂停播放按钮的显示等。

## 读取或监听所有音频流的变化

如果部分应用需要查询获取所有音频流的变化信息，可以通过AudioStreamManager读取或监听所有音频流的变化。

如下为音频流管理调用关系图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/813FJQSuQkyoLmJuKJhr6g/zh-cn_image_0000002736313581.png)

在进行应用开发的过程中，开发者需要先调用[getStreamManager](../harmonyos-references/arkts-apis-audio-audiomanager.md#getstreammanager9)创建AudioStreamManager实例，进而通过该实例管理音频流。

详细API含义可参考[AudioStreamManager](../harmonyos-references/arkts-apis-audio-audiostreammanager.md)。

## 开发步骤及注意事项

1. 创建AudioStreamManager实例。

   ```typescript
   import { audio } from '@kit.AudioKit';
   // ...
   let audioManager = audio.getAudioManager();
   // ...
   let audioStreamManager = audioManager.getStreamManager();
   ```
2. 使用[on('audioRendererChange')](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#onaudiorendererchange9)监听音频播放流的变化。如果音频流监听应用需要在音频播放流状态变化、设备变化时获取通知，可以订阅该事件。

   ```typescript
   import { audio } from '@kit.AudioKit';
   // ...
     audioStreamManager.on('audioRendererChange',  (audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
       console.info(`Succeeded in using on function. AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}`);
       globalLogUpdate(`Succeeded in using on function. AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}`, false);
     });
   ```
3. （可选）使用[off('audioRendererChange')](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#offaudiorendererchange9)取消监听音频播放流变化。

   ```typescript
   audioStreamManager.off('audioRendererChange');
   console.info('Succeeded in using off function.');
   ```
4. （可选）使用[getCurrentAudioRendererInfoArray](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#getcurrentaudiorendererinfoarray9)获取所有音频播放流的信息。该接口可获取音频播放流唯一ID、音频渲染器信息以及音频播放设备信息。

   **说明** 

   对所有音频流状态进行监听的应用需要[声明权限](declare-permissions.md) ohos.permission.USE\_BLUETOOTH，否则无法获得实际的设备名称和设备地址信息，查询到的设备名称和设备地址（蓝牙设备的相关属性）将为空字符串。

   ```typescript
   import { audio } from '@kit.AudioKit';
   // ...
   import { BusinessError } from '@kit.BasicServicesKit';
   // ...
   async function getCurrentAudioRendererInfoArray(): Promise<void> {
     await audioStreamManager.getCurrentAudioRendererInfoArray()
       .then((audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
         console.info(`Succeeded in getting current audio renderer info array. AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}`);
         globalLogUpdate(`Succeeded in getting current audio renderer info array. AudioRendererChangeInfoArray: ${JSON.stringify(audioRendererChangeInfoArray)}`, false);
       }).catch((err: BusinessError ) => {
         console.error(`Failed to get current audio renderer info array. Code: ${err.code}, message: ${err.message}`);
         // ...
       });
   }
   ```
