---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-input-device-switcher
title: 实现音频输入设备路由切换
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频设备路由管理 > 实现音频输入设备路由切换
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ae4c840e85c456ccec6f3556658b78d5f4dcb564724459bcc2e8357cb2268876
---

从API version 21开始，支持音频输入设备路由切换。

当应用进行音频输入时，系统会根据音频流类型选择对应的输入设备（SOURCE\_TYPE\_MIC：内置MIC录音；SOURCE\_TYPE\_VOICE\_COMMUNICATION：跟随当前输出设备）。若默认输入设备不满足应用需求，应用可通过[setBluetoothAndNearlinkPreferredRecordCategory](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setbluetoothandnearlinkpreferredrecordcategory21)或[selectMediaInputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#selectmediainputdevice21)实现音频输入设备路由切换。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioRoutingManagerSampleJS)。

## 选择使用蓝牙或者星闪设备进行录音

应用可使用AudioSessionManager的[setBluetoothAndNearlinkPreferredRecordCategory](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setbluetoothandnearlinkpreferredrecordcategory21)设置应用程序的输入设备选择偏好，当蓝牙或星闪设备上线时生效。

说明

通话场景下，如果蓝牙或星闪设备在线，系统默认使用蓝牙或星闪设备作为输入设备。

```
1. import { audio } from '@kit.AudioKit';  // 导入audio模块。
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let audioManager = audio.getAudioManager();  // 需要先创建AudioManager实例。

6. let audioSessionManager = audioManager.getSessionManager();  // 再调用AudioManager的方法创建AudioSessionManager实例.

8. // ...
9. audioSessionManager.setBluetoothAndNearlinkPreferredRecordCategory(audio.BluetoothAndNearlinkPreferredRecordCategory
10. .PREFERRED_LOW_LATENCY).then(() => {
11. console.info('Succeeded in setting bluetooth and nearlink preferred record category.');
12. // ...
13. }).catch((err: BusinessError) => {
14. console.error(`Failed to set bluetooth and nearlink preferred record category. Code: ${err.code},
15. message: ${err.message}`);
16. // ...
17. });
```

## 选择任意设备进行录音

应用可使用AudioSessionManager的[selectMediaInputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#selectmediainputdevice21)选择输入设备。

说明

通话场景下，输入设备跟随当前输出设备，此时其他与通话并发的录音流也会跟随通话输入设备。

```
1. import { audio } from '@kit.AudioKit';  // 导入audio模块。
2. import { BusinessError } from '@kit.BasicServicesKit';

4. let audioManager = audio.getAudioManager();  // 需要先创建AudioManager实例。

6. let audioSessionManager = audioManager.getSessionManager();  // 再调用AudioManager的方法创建AudioSessionManager实例.

8. // ...
9. // 监听音频可选输入设备连接状态变化事件,当有输入设备上下线时会收到回调通知。
10. let availableDeviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
11. let data: audio.AudioDeviceDescriptors = deviceChanged.deviceDescriptors;
12. console.info(`Succeeded in using on or off function, AudioDeviceDescriptors: ${data}.`);
13. // ...
14. };

16. // 监听当前输入设备变化事件,当选择输入设备成功后会触发该回调。
17. let currentInputDeviceChangedCallback = (currentInputDeviceChangedEvent: audio.CurrentInputDeviceChangedEvent) => {
18. console.info(`Succeeded in using on or off function, CurrentInputDeviceChangedEvent:
19. ${currentInputDeviceChangedEvent}.`);
20. // ...
21. };

23. // ...
24. audioSessionManager.on('availableDeviceChange', audio.DeviceUsage.MEDIA_INPUT_DEVICES, availableDeviceChangeCallback);
25. // ...
26. audioSessionManager.on('currentInputDeviceChanged', currentInputDeviceChangedCallback);
27. // ...
28. // 取消监听音频可选输入设备连接状态变化事件
29. audioSessionManager.off('availableDeviceChange', availableDeviceChangeCallback);
30. // ...
31. // 取消监听当前输入设备变化事件
32. audioSessionManager.off('currentInputDeviceChanged', currentInputDeviceChangedCallback);
33. // ...
34. try {
35. // 获取当前可选的音频输入设备列表。
36. let data: audio.AudioDeviceDescriptors =
37. audioSessionManager.getAvailableDevices(audio.DeviceUsage.MEDIA_INPUT_DEVICES);
38. console.info(`Succeeded in getting available devices, AudioDeviceDescriptors: ${data}.`);

40. // ...

42. // 当前可选音频输入设备列表不为空时,可进行选择。
43. if (data[0]) {
44. // 选择输入设备。
45. await audioSessionManager.selectMediaInputDevice(data[0]).then(() => {
46. console.info('Succeeded in selecting media input device.');
47. // ...
48. }).catch((err: BusinessError) => {
49. console.error(`Failed to select media input device. Code: ${err.code}, message: ${err.message}`);
50. // ...
51. });
52. }
53. } catch (err) {
54. let error = err as BusinessError;
55. console.error(`Failed to select media input device. Code: ${err.code}, message: ${err.message}`);
56. // ...
57. }
58. // ...
59. // 可通过该接口查询选择输入设备是否成功。
60. try {
61. let device: audio.AudioDeviceDescriptor = audioSessionManager.getSelectedMediaInputDevice();
62. console.info(`Succeeded in getting selected media input device: ${JSON.stringify(device)}`);

64. // ...
65. } catch (err) {
66. let error = err as BusinessError;
67. console.error(`Failed to get selected media input device. Code: ${error.code}, message: ${error.message}`);
68. // ...
69. }
70. // ...
71. // 清空通过selectMediaInputDevice选择的输入设备。
72. audioSessionManager.clearSelectedMediaInputDevice().then(() => {
73. console.info('Succeeded in clearing selected media input device.');
74. // ...
75. }).catch((err: BusinessError) => {
76. console.error(`Failed to clear selected media input device. Code: ${err.code}, message: ${err.message}`);
77. // ...
78. });
```
