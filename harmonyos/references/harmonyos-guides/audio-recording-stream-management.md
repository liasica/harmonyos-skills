---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-recording-stream-management
title: 查询和监听其他应用录制状态
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频录制 > 查询和监听其他应用录制状态
category: harmonyos-guides
scraped_at: 2026-04-29T13:34:33+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fd34dcf4a66c39efa52e358afa16788361676865704c52f9e32bcaa500f5ac5f
---

对于录制音频类的应用，开发者需要关注该应用的音频流的状态以做出相应的操作，比如监听到状态为结束时，及时提示用户录制已结束。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioCaptureSampleJS)。

## 读取或监听应用内音频流状态变化

参考[使用AudioCapturer开发音频录制功能(ArkTs)](using-audiocapturer-for-recording.md)或[audio.createAudioCapturer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiocapturer8)，先完成AudioCapturer的创建，再通过以下两种方法查看音频流状态的变化。

* 方法1：直接查看AudioCapturer的[属性](../harmonyos-references/arkts-apis-audio-audiocapturer.md#属性)state：

  ```
  1. let audioCapturerState: audio.AudioState = audioCapturer.state;
  2. console.info(`Current state is: ${audioCapturerState }`)
  ```
* 方法2：注册stateChange监听AudioCapturer的状态变化：

  ```
  1. audioCapturer.on('stateChange', (capturerState: audio.AudioState) => {
  2. console.info(`State change to: ${capturerState}`)
  3. // ...
  4. });
  ```

获取state后可对照[AudioState](../harmonyos-references/arkts-apis-audio-e.md#audiostate8)来进行相应的操作，比如显示录制结束的提示等。

## 读取或监听所有录制流的变化

如果部分应用需要查询获取所有音频流的变化信息，可以通过AudioStreamManager读取或监听所有音频流的变化。

如下为音频流管理调用关系图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/16p8jeDeTWK-yE3QtymJeA/zh-cn_image_0000002589324901.png?HW-CC-KV=V1&HW-CC-Date=20260429T053432Z&HW-CC-Expire=86400&HW-CC-Sign=C46DF5945BC362602AB8C8A532BE67060855C595408073226D25BE3CAB02A0A0)

在进行应用开发的过程中，开发者需要先调用[getStreamManager](../harmonyos-references/arkts-apis-audio-audiomanager.md#getstreammanager9)创建AudioStreamManager实例，进而通过该实例管理音频流。

详细API含义可参考[AudioStreamManager](../harmonyos-references/arkts-apis-audio-audiostreammanager.md)。

## 开发步骤及注意事项

1. 创建AudioStreamManager实例。

   ```
   1. import { audio } from '@kit.AudioKit';
   2. import { BusinessError } from '@kit.BasicServicesKit';

   4. let audioManager = audio.getAudioManager();
   5. let audioStreamManager = audioManager.getStreamManager();
   ```
2. 使用[on('audioCapturerChange')](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#onaudiocapturerchange9)监听音频录制流更改事件。 如果音频流监听应用需要在音频录制流状态变化、设备变化时获取通知，可以订阅该事件。

   ```
   1. audioStreamManager.on('audioCapturerChange', (audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) =>  {
   2. // ...
   3. for (let i = 0; i < audioCapturerChangeInfoArray.length; i++) {
   4. console.info(`## CapChange on is called for element ${i} ##`);
   5. console.info(`StreamId for ${i} is: ${audioCapturerChangeInfoArray[i].streamId}`);
   6. console.info(`Source for ${i} is: ${audioCapturerChangeInfoArray[i].capturerInfo.source}`);
   7. console.info(`Flag  ${i} is: ${audioCapturerChangeInfoArray[i].capturerInfo.capturerFlags}`);

   9. // ...

   11. let devDescriptor: audio.AudioDeviceDescriptors = audioCapturerChangeInfoArray[i].deviceDescriptors;
   12. for (let j = 0; j < audioCapturerChangeInfoArray[i].deviceDescriptors.length; j++) {
   13. console.info(`Id: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].id}`);
   14. console.info(`Type: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].deviceType}`);
   15. console.info(`Role: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].deviceRole}`);
   16. console.info(`Name: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].name}`);
   17. console.info(`Address: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].address}`);
   18. console.info(`SampleRates: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].sampleRates[0]}`);
   19. console.info(`ChannelCounts ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].channelCounts[0]}`);
   20. console.info(`ChannelMask: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].channelMasks}`);
   21. }
   22. }
   23. // ...
   24. });
   ```
3. （可选）使用[off('audioCapturerChange')](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#offaudiocapturerchange9)取消监听音频录制流变化。

   ```
   1. audioStreamManager.off('audioCapturerChange');
   2. console.info('CapturerChange Off is called');
   ```
4. （可选）使用[getCurrentAudioCapturerInfoArray](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#getcurrentaudiocapturerinfoarray9)获取当前音频录制流的信息。该接口可获取音频录制流唯一ID、音频采集器信息以及音频录制设备信息。

   说明

   对所有音频流状态进行监听的应用需要[声明权限](declare-permissions.md)ohos.permission.USE\_BLUETOOTH，否则无法获得实际的设备名称和设备地址信息，查询到的设备名称和设备地址（蓝牙设备的相关属性）将为空字符串。

   从API version 20开始，通常在音频录制启动前调用[isRecordingAvailable](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isrecordingavailable20)，判断当前传入的音频采集器信息中音源类型的录制是否可以启动成功。

   ```
   1. async function getCurrentAudioCapturerInfoArray(updateCallback?:
   2. (msg: string, isError: boolean) => void): Promise<void>{
   3. // ...

   5. await audioStreamManager.getCurrentAudioCapturerInfoArray()
   6. .then((audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) => {
   7. console.info('getCurrentAudioCapturerInfoArray Get Promise Called');
   8. let detailInfo = 'getCurrentAudioCapturerInfoArray Get Promise Called\n';
   9. if (audioCapturerChangeInfoArray != null) {
   10. for (let i = 0; i < audioCapturerChangeInfoArray.length; i++) {
   11. console.info(`StreamId for ${i} is: ${audioCapturerChangeInfoArray[i].streamId}`);
   12. console.info(`Source for ${i} is: ${audioCapturerChangeInfoArray[i].capturerInfo.source}`);
   13. console.info(`Flag  ${i} is: ${audioCapturerChangeInfoArray[i].capturerInfo.capturerFlags}`);

   15. detailInfo += `StreamId for ${i} is: ${audioCapturerChangeInfoArray[i].streamId}\n`;
   16. detailInfo += `Source for ${i} is: ${audioCapturerChangeInfoArray[i].capturerInfo.source}\n`;
   17. detailInfo += `Flag ${i} is: ${audioCapturerChangeInfoArray[i].capturerInfo.capturerFlags}\n`;

   19. for (let j = 0; j < audioCapturerChangeInfoArray[i].deviceDescriptors.length; j++) {
   20. console.info(`Id: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].id}`);
   21. console.info(`Type: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].deviceType}`);
   22. console.info(`Role: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].deviceRole}`);
   23. console.info(`Name: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].name}`);
   24. console.info(`Address: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].address}`);
   25. console.info(`SampleRates: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].sampleRates[0]}`);
   26. console.info(`ChannelCounts ${i} : ${audioCapturerChangeInfoArray[i]
   27. .deviceDescriptors[j].channelCounts[0]}`);
   28. console.info(`ChannelMask: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].channelMasks}`);
   29. }
   30. }
   31. }
   32. if (updateCallback) {
   33. updateCallback(detailInfo, false);
   34. }
   35. }).catch((err: BusinessError) => {
   36. console.error(`Invoke getCurrentAudioCapturerInfoArray failed, code is ${err.code}, message is ${err.message}`);
   37. const errorMsg = `Invoke getCurrentAudioCapturerInfoArray failed, code is ${err.code}, message is ${err.message}`;
   38. if (updateCallback) {
   39. updateCallback(errorMsg, true);
   40. }
   41. });
   42. // 获取后取消监听
   43. cancelListenAudioStreamManager();
   44. }
   ```
