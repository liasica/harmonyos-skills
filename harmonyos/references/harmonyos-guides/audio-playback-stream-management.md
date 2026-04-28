---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-playback-stream-management
title: 音频播放流管理
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频播放 > 音频播放流管理
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:354a390e133f6d85f9d1458a4271c93b0213ef03b6f9a04fa14ebc0beb3bca94
---

对于播放音频类的应用，开发者需要关注该应用的音频流的状态以做出相应的操作，比如监听到状态为播放中/暂停时，及时改变播放按钮的UI显示。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioRendererSampleJS)。

## 读取或监听应用内音频流状态变化

参考[使用AudioRenderer开发音频播放功能(ArkTs)](using-audiorenderer-for-playback.md)或[audio.createAudioRenderer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiorenderer8)，先完成AudioRenderer的创建，再通过以下两种方法查看音频流状态的变化。

* 方法1：直接查看AudioRenderer的[属性](../harmonyos-references/arkts-apis-audio-audiorenderer.md#属性)state：

  ```
  1. import { audio } from '@kit.AudioKit';
  2. // ...
  3. let audioRendererState: audio.AudioState = audioRenderer.state;
  4. console.info(`Current state is: ${audioRendererState }`);
  ```
* 方法2：注册stateChange监听AudioRenderer的状态变化：

  ```
  1. import { audio } from '@kit.AudioKit';
  2. // ...
  3. audioRenderer.on('stateChange', (rendererState: audio.AudioState) => {
  4. console.info(`State change to: ${rendererState}`);
  5. // ...
  6. });
  ```

获取state后可对照[AudioState](../harmonyos-references/arkts-apis-audio-e.md#audiostate8)来进行相应的操作，比如更改暂停播放按钮的显示等。

## 读取或监听所有音频流的变化

如果部分应用需要查询获取所有音频流的变化信息，可以通过AudioStreamManager读取或监听所有音频流的变化。

如下为音频流管理调用关系图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/e3ti_UwPRseDxTfODQkqlA/zh-cn_image_0000002583438575.png?HW-CC-KV=V1&HW-CC-Date=20260427T234532Z&HW-CC-Expire=86400&HW-CC-Sign=21A0D7F7F974EC2B105B082D835F077A55BDB2A656A47B1FDEBC0D0F12975E43)

在进行应用开发的过程中，开发者需要先调用[getStreamManager](../harmonyos-references/arkts-apis-audio-audiomanager.md#getstreammanager9)创建AudioStreamManager实例，进而通过该实例管理音频流。

详细API含义可参考[AudioStreamManager](../harmonyos-references/arkts-apis-audio-audiostreammanager.md)。

## 开发步骤及注意事项

1. 创建AudioStreamManager实例。

   ```
   1. import { audio } from '@kit.AudioKit';
   2. // ...
   3. let audioManager = audio.getAudioManager();
   4. // ...
   5. let audioStreamManager = audioManager.getStreamManager();
   ```
2. 使用[on('audioRendererChange')](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#onaudiorendererchange9)监听音频播放流的变化。如果音频流监听应用需要在音频播放流状态变化、设备变化时获取通知，可以订阅该事件。

   ```
   1. import { audio } from '@kit.AudioKit';
   2. // ...
   3. audioStreamManager.on('audioRendererChange',  (audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
   4. for (let i = 0; i < audioRendererChangeInfoArray.length; i++) {
   5. let audioRendererChangeInfo = audioRendererChangeInfoArray[i];
   6. console.info(`## RendererChange on is called for ${i} ##`);
   7. console.info(`StreamId for ${i} is: ${audioRendererChangeInfo.streamId}`);
   8. console.info(`Content ${i} is: ${audioRendererChangeInfo.rendererInfo.content}`);
   9. console.info(`Stream ${i} is: ${audioRendererChangeInfo.rendererInfo.usage}`);
   10. console.info(`Flag ${i} is: ${audioRendererChangeInfo.rendererInfo.rendererFlags}`);
   11. // ...
   12. for (let j = 0;j < audioRendererChangeInfo.deviceDescriptors.length; j++) {
   13. console.info(`Id: ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].id}`);
   14. console.info(`Type: ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].deviceType}`);
   15. console.info(`Role: ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].deviceRole}`);
   16. console.info(`Name: ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].name}`);
   17. console.info(`Address: ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].address}`);
   18. console.info(`SampleRates: ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].sampleRates[0]}`);
   19. console.info(`ChannelCount ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].channelCounts[0]}`);
   20. console.info(`ChannelMask: ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].channelMasks}`);
   21. }
   22. }
   23. });
   ```
3. （可选）使用[off('audioRendererChange')](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#offaudiorendererchange9)取消监听音频播放流变化。

   ```
   1. audioStreamManager.off('audioRendererChange');
   2. console.info('RendererChange Off is called ');
   ```
4. （可选）使用[getCurrentAudioRendererInfoArray](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#getcurrentaudiorendererinfoarray9)获取所有音频播放流的信息。该接口可获取音频播放流唯一ID、音频渲染器信息以及音频播放设备信息。

   说明

   对所有音频流状态进行监听的应用需要[声明权限](declare-permissions.md)ohos.permission.USE\_BLUETOOTH，否则无法获得实际的设备名称和设备地址信息，查询到的设备名称和设备地址（蓝牙设备的相关属性）将为空字符串。

   ```
   1. import { audio } from '@kit.AudioKit';
   2. // ...
   3. import { BusinessError } from '@kit.BasicServicesKit';
   4. // ...
   5. async function getCurrentAudioRendererInfoArray(): Promise<void> {
   6. await audioStreamManager.getCurrentAudioRendererInfoArray()
   7. .then((audioRendererChangeInfoArray: audio.AudioRendererChangeInfoArray) => {
   8. console.info(`getCurrentAudioRendererInfoArray  Get Promise is called `);
   9. // ...
   10. if (audioRendererChangeInfoArray != null) {
   11. for (let i = 0; i < audioRendererChangeInfoArray.length; i++) {
   12. let audioRendererChangeInfo = audioRendererChangeInfoArray[i];
   13. console.info(`StreamId for ${i} is: ${audioRendererChangeInfo.streamId}`);
   14. console.info(`Content ${i} is: ${audioRendererChangeInfo.rendererInfo.content}`);
   15. console.info(`Stream ${i} is: ${audioRendererChangeInfo.rendererInfo.usage}`);
   16. console.info(`Flag ${i} is: ${audioRendererChangeInfo.rendererInfo.rendererFlags}`);
   17. // ...
   18. for (let j = 0;j < audioRendererChangeInfo.deviceDescriptors.length; j++) {
   19. console.info(`Id: ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].id}`);
   20. console.info(`Type: ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].deviceType}`);
   21. console.info(`Role: ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].deviceRole}`);
   22. console.info(`Name: ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].name}`);
   23. console.info(`Address: ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].address}`);
   24. console.info(`SampleRates: ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].sampleRates[0]}`);
   25. console.info(`ChannelCount ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].channelCounts[0]}`);
   26. console.info(`ChannelMask: ${i} : ${audioRendererChangeInfo.deviceDescriptors[j].channelMasks}`);
   27. }
   28. }
   29. }
   30. }).catch((err: BusinessError ) => {
   31. console.error(`Invoke getCurrentAudioRendererInfoArray failed, code is ${err.code}, message is ${err.message}`);
   32. // ...
   33. });
   34. }
   ```
