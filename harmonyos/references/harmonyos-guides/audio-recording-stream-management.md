---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-recording-stream-management
title: 查询和监听其他应用录制状态
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频录制 > 查询和监听其他应用录制状态
category: harmonyos-guides
scraped_at: 2026-09-05T06:14:44+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:529397bdfc305b9c2a18bfaaf5021e04ad8e9dd077500f438e6820f5c94b7150
---

对于录制音频类的应用，开发者需要关注该应用的音频流的状态以做出相应的操作，比如监听到状态为结束时，及时提示用户录制已结束。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioCaptureSampleJS)。

## 读取或监听应用内音频流状态变化

参考[使用AudioCapturer开发音频录制功能(ArkTS)](using-audiocapturer-for-recording.md)或[audio.createAudioCapturer](../harmonyos-references/arkts-apis-audio-f.md#audiocreateaudiocapturer8)，先完成AudioCapturer的创建，再通过以下两种方法查看音频流状态的变化。

* 方法1：直接查看AudioCapturer的[属性](../harmonyos-references/arkts-apis-audio-audiocapturer.md#属性)state：

  ```typescript
  let audioCapturerState: audio.AudioState = audioCapturer.state;
  console.info(`Current state is: ${audioCapturerState }`)
  ```
* 方法2：注册stateChange监听AudioCapturer的状态变化：

  ```typescript
  audioCapturer.on('stateChange', (capturerState: audio.AudioState) => {
    console.info(`State change to: ${capturerState}`)
    // ...
  });
  ```

获取state后可根据[AudioState](../harmonyos-references/arkts-apis-audio-e.md#audiostate8)来进行相应的操作，比如显示录制结束的提示等。

## 读取或监听所有录制流的变化

如果部分应用需要查询所有音频流的变化信息，可以通过AudioStreamManager读取或监听所有音频流的变化。

### 判断麦克风是否被占用

录音、语音识别、实时语音通话、短语音消息、直播连麦等业务在启动音频采集前，通常需要先判断麦克风是否被占用。若麦克风已被其他录制流占用，新录音流可能无法正常启动；或者在启动成功后，也可能在运行过程中受系统音频焦点或录音并发策略影响而被中断、进入静音录制状态，进而导致录音文件不完整、语音识别结果缺失等问题。

可根据业务场景，任选其中一种方法进行判断：

* 查询当前采集器和输入设备电平：如果需要主动查询当前是否有输入设备正在采集声音，可联合使用[getCurrentAudioCapturerInfoArray](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#getcurrentaudiocapturerinfoarray9)和[getMaxAmplitudeForInputDevice](../harmonyos-references/arkts-apis-audio-audiovolumegroupmanager.md#getmaxamplitudeforinputdevice12)。先调用getCurrentAudioCapturerInfoArray获取当前音频采集器信息，再遍历每个采集器使用的输入设备并调用getMaxAmplitudeForInputDevice获取音频流最大电平值，取值范围为[0, 1]。当最大电平值大于0时，说明该设备采集到声音，设备正在录音，可判断麦克风正在被占用。
* 判断指定录制请求是否可启动：如果需要在启动录音前判断指定音源类型的录制请求是否可以启动，可调用[isRecordingAvailable](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isrecordingavailable20)，传入业务要使用的[AudioCapturerInfo](../harmonyos-references/arkts-apis-audio-i.md#audiocapturerinfo8)。如果返回true，表明可以使用麦克风进行录制；如果返回false，表明麦克风可能已被占用。示例代码可参考[isRecordingAvailable](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isrecordingavailable20)。

**说明** 

* isRecordingAvailable用于判断指定录制请求是否可以启动，不返回当前录制流详情。
* getMaxAmplitudeForInputDevice需配合getCurrentAudioCapturerInfoArray使用，先获取音频采集器使用的输入设备信息，再查询对应设备的最大电平值。
* getCurrentAudioCapturerInfoArray返回的信息可能包含系统内部录制流。开发者可结合capturerInfo.source和业务场景，判断录制流是否属于当前业务需要识别的麦克风占用场景。

如下为音频流管理调用关系图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/lncHvTyJRkuiqx1qCkZj6A/zh-cn_image_0000002742003665.png)

在进行应用开发的过程中，开发者需要先调用[getStreamManager](../harmonyos-references/arkts-apis-audio-audiomanager.md#getstreammanager9)创建AudioStreamManager实例，进而通过该实例管理音频流。

详细API含义可参考[AudioStreamManager](../harmonyos-references/arkts-apis-audio-audiostreammanager.md)。

## 开发步骤及注意事项

1. 创建AudioStreamManager实例。

   ```typescript
   import { audio } from '@kit.AudioKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   let audioManager = audio.getAudioManager();
   let audioStreamManager = audioManager.getStreamManager();
   ```
2. 使用[on('audioCapturerChange')](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#onaudiocapturerchange9)监听音频录制流变化事件。如果应用需要在音频录制流状态变化、设备变化时获取通知，可以订阅该事件。

   ```typescript
   audioStreamManager.on('audioCapturerChange', (audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) =>  {
     // ...
     for (let i = 0; i < audioCapturerChangeInfoArray.length; i++) {
       console.info(`## CapChange on is called for element ${i} ##`);
       console.info(`StreamId for ${i} is: ${audioCapturerChangeInfoArray[i].streamId}`);
       console.info(`Source for ${i} is: ${audioCapturerChangeInfoArray[i].capturerInfo.source}`);
       console.info(`Flag  ${i} is: ${audioCapturerChangeInfoArray[i].capturerInfo.capturerFlags}`);

       // ...

       let devDescriptor: audio.AudioDeviceDescriptors = audioCapturerChangeInfoArray[i].deviceDescriptors;
       for (let j = 0; j < audioCapturerChangeInfoArray[i].deviceDescriptors.length; j++) {
         console.info(`Id: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].id}`);
         console.info(`Type: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].deviceType}`);
         console.info(`Role: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].deviceRole}`);
         console.info(`Name: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].name}`);
         console.info(`Address: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].address}`);
         console.info(`SampleRates: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].sampleRates[0]}`);
         console.info(`ChannelCounts ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].channelCounts[0]}`);
         console.info(`ChannelMask: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].channelMasks}`);
       }
     }
     // ...
   });
   ```
3. （可选）使用[off('audioCapturerChange')](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#offaudiocapturerchange9)取消监听音频录制流变化。

   ```typescript
   audioStreamManager.off('audioCapturerChange');
   console.info('CapturerChange Off is called');
   ```
4. （可选）使用[getCurrentAudioCapturerInfoArray](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#getcurrentaudiocapturerinfoarray9)获取当前音频录制流的信息。该接口可获取音频录制流唯一ID、音频采集器信息以及音频录制设备信息。

   **说明** 

   对所有音频流状态进行监听的应用需要[声明权限](declare-permissions.md)ohos.permission.USE\_BLUETOOTH，否则无法获得实际的设备名称和设备地址信息，查询到的设备名称和设备地址（蓝牙设备的相关属性）将为空字符串。

   从API version 20开始，通常在音频录制启动前调用[isRecordingAvailable](../harmonyos-references/arkts-apis-audio-audiostreammanager.md#isrecordingavailable20)，判断当前传入的音频采集器信息中音源类型的录制是否可以启动成功。

   ```typescript
   async function getCurrentAudioCapturerInfoArray(updateCallback?:
     (msg: string, isError: boolean) => void): Promise<void>{
     // ...

     await audioStreamManager.getCurrentAudioCapturerInfoArray()
       .then((audioCapturerChangeInfoArray: audio.AudioCapturerChangeInfoArray) => {
         console.info('getCurrentAudioCapturerInfoArray Get Promise Called');
         // ...
         if (audioCapturerChangeInfoArray != null) {
           for (let i = 0; i < audioCapturerChangeInfoArray.length; i++) {
             console.info(`StreamId for ${i} is: ${audioCapturerChangeInfoArray[i].streamId}`);
             console.info(`Source for ${i} is: ${audioCapturerChangeInfoArray[i].capturerInfo.source}`);
             console.info(`Flag  ${i} is: ${audioCapturerChangeInfoArray[i].capturerInfo.capturerFlags}`);

             // ...

             for (let j = 0; j < audioCapturerChangeInfoArray[i].deviceDescriptors.length; j++) {
               console.info(`Id: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].id}`);
               console.info(`Type: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].deviceType}`);
               console.info(`Role: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].deviceRole}`);
               console.info(`Name: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].name}`);
               console.info(`Address: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].address}`);
               console.info(`SampleRates: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].sampleRates[0]}`);
               console.info(`ChannelCounts ${i} : ${audioCapturerChangeInfoArray[i]
                 .deviceDescriptors[j].channelCounts[0]}`);
               console.info(`ChannelMask: ${i} : ${audioCapturerChangeInfoArray[i].deviceDescriptors[j].channelMasks}`);
             }
           }
         }
         // ...
       }).catch((err: BusinessError) => {
         console.error(`Invoke getCurrentAudioCapturerInfoArray failed, code is ${err.code}, message is ${err.message}`);
         // ...
       });
     // ...
   }
   ```
