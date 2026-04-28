---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-output-device-management
title: 查询和监听音频输出设备
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频设备路由管理 > 查询和监听音频输出设备
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:74f2aa07c87a42e3a0a861ce76e90b7afe2d6771edb978e4f4c54d6f94212793
---

应用可通过以下两种方式管理全局音频输出设备：

* 通常情况下，可以[通过AudioRoutingManager查询和监听音频输出设备](audio-output-device-management.md#通过audioroutingmanager查询和监听音频输出设备)。
* 从API version 20开始，AudioSessionManager提供了部分输出设备管理的接口，支持[通过AudioSession查询和监听音频输出设备](audio-output-device-management.md#通过audiosession查询和监听音频输出设备)，方便在使用AudioSession管理音频焦点的同时管理音频输出。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioRoutingManagerSampleJS)。

## 通过AudioRoutingManager查询和监听音频输出设备

本模块提供音频输出设备管理能力，包括查询设备信息和监听连接状态变化。具体API说明请参考文档[AudioRoutingManager](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md)。

### 创建AudioRoutingManager实例

在使用AudioRoutingManager管理音频设备前，需要先导入模块并创建实例。

```
1. import { audio } from '@kit.AudioKit';  // 导入audio模块。
2. // ...
3. let audioManager = audio.getAudioManager();  // 需要先创建AudioManager实例。
4. let audioRoutingManager = audioManager.getRoutingManager();  // 再调用AudioManager的方法创建AudioRoutingManager实例。
```

### 支持的音频输出设备类型

目前支持的输出设备如下表所示：

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EARPIECE | 1 | 听筒。 |
| SPEAKER | 2 | 扬声器。 |
| WIRED\_HEADSET | 3 | 有线耳机，带麦克风。 |
| WIRED\_HEADPHONES | 4 | 有线耳机，无麦克风。 |
| BLUETOOTH\_SCO | 7 | 蓝牙设备SCO（Synchronous Connection Oriented）连接。 |
| BLUETOOTH\_A2DP | 8 | 蓝牙设备A2DP（Advanced Audio Distribution Profile）连接。 |
| USB\_HEADSET | 22 | USB耳机，带麦克风。 |
| NEARLINK | 31 | 星闪设备。 |

### 获取输出设备信息

使用[getDevices](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getdevices9)方法可以获取当前所有输出设备的信息。

```
1. import { audio } from '@kit.AudioKit';  // 导入audio模块。
2. // ...
3. audioRoutingManager.getDevices(audio.DeviceFlag.OUTPUT_DEVICES_FLAG).then((data: audio.AudioDeviceDescriptors) => {
4. console.info('Promise returned to indicate that the device list is obtained.');
5. // ...
6. });
```

### 监听设备连接状态变化

设置监听事件以监控设备连接状态的变化，设备连接或断开时触发回调。

说明

监听设备连接状态变化可以监听到全部的设备连接状态变化，不建议作为应用处理自动暂停的依据。应用如需处理自动暂停相关业务，可参考[音频流输出设备变更原因](audio-output-device-change.md#音频流输出设备变更原因)。

```
1. import { audio } from '@kit.AudioKit';  // 导入audio模块。
2. // ...
3. // 监听音频设备状态变化。
4. audioRoutingManager.on('deviceChange', audio.DeviceFlag.OUTPUT_DEVICES_FLAG, (deviceChanged: audio.DeviceChangeAction) => {
5. console.info(`device change type : ${deviceChanged.type}`);  // 设备连接状态变化,0为连接,1为断开连接。
6. console.info(`device descriptor size : ${deviceChanged.deviceDescriptors.length}`);
7. console.info(`device change descriptor : ${deviceChanged.deviceDescriptors[0].deviceRole}`);  // 设备角色。
8. console.info(`device change descriptor : ${deviceChanged.deviceDescriptors[0].deviceType}`);  // 设备类型。

10. // ...
11. });
12. // ...
13. // 取消监听音频设备状态变化。
14. audioRoutingManager.off('deviceChange');
```

### 获取最高优先级输出设备信息

使用[getPreferOutputDeviceForRendererInfo](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getpreferoutputdeviceforrendererinfo10)方法, 可以获取当前最高优先级的输出设备。

说明

最高优先级输出设备表示声音将在此设备输出的设备。

```
1. import { audio } from '@kit.AudioKit';  // 导入audio模块。
2. import { BusinessError } from '@kit.BasicServicesKit';
3. // ...
4. let rendererInfo: audio.AudioRendererInfo = {
5. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,// 音频流使用类型:音乐。根据业务场景配置,参考StreamUsage。
6. rendererFlags: 0 // 音频渲染器标志。
7. };
8. // ...
9. async function getPreferOutputDeviceForRendererInfo() {
10. // ...
11. audioRoutingManager.getPreferOutputDeviceForRendererInfo(rendererInfo).then((desc: audio.AudioDeviceDescriptors) => {
12. console.info(`device descriptor: ${desc}`);

14. // ...
15. }).catch((err: BusinessError) => {
16. console.error(`Result ERROR: ${err}`);
17. // ...
18. });
19. // ...
20. }
```

### 监听最高优先级输出设备变化

```
1. import { audio } from '@kit.AudioKit';  // 导入audio模块。
2. // ...
3. let rendererInfo: audio.AudioRendererInfo = {
4. usage: audio.StreamUsage.STREAM_USAGE_MUSIC,// 音频流使用类型:音乐。根据业务场景配置,参考StreamUsage。
5. rendererFlags: 0 // 音频渲染器标志。
6. };
7. // ...
8. // 监听最高优先级输出设备变化。
9. audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', rendererInfo, (desc: audio.AudioDeviceDescriptors) => {
10. console.info(`device change descriptor : ${desc[0].deviceRole}`);  // 设备角色。
11. console.info(`device change descriptor : ${desc[0].deviceType}`);  // 设备类型。

13. // ...
14. });
15. // ...
16. // 取消监听最高优先级输出设备变化。
17. audioRoutingManager.off('preferOutputDeviceChangeForRendererInfo');
```

## 通过AudioSession查询和监听音频输出设备

应用使用播放器的SDK播放音频流，不持有[AudioRenderer](../harmonyos-references/arkts-apis-audio-audiorenderer.md)对象，因此无法灵活控制播放设备的选择和状态监听。从API version 20开始，AudioSession不仅增加了焦点管理功能，还提供了音频输出设备管理功能，包括设置默认输出设备和监听设备变化。请参考以下文档获取更多信息：

* ArkTS API：[AudioSessionManager](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md)
* C API：[native\_audio\_session\_manager.h](../harmonyos-references/capi-native-audio-session-manager-h.md)

### 创建AudioSession实例

在使用AudioSessionManager管理音频设备前，需要先导入模块并创建实例。

```
1. import { audio } from '@kit.AudioKit';  // 导入audio模块。
2. let audioManager = audio.getAudioManager();  // 需要先创建AudioManager实例。

4. let audioSessionManager = audioManager.getSessionManager();  // 再调用AudioManager的方法创建AudioSessionManager实例。
```

### 设置本机默认音频输出设备

[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)可以用于设置本机默认输出设备。

说明

* 由于AudioSession是应用级设置，调用本接口设置默认音频输出设备会覆盖AudioRenderer的setDefaultOutputDevice接口设置的音频输出设备信息。
* 调用setDefaultOutputDevice设置音频输出设备后，如需取消，可将参数设为audio.DeviceType.DEFAULT，将音频设备选择权交还给系统。否则，每次调用activateAudioSession时，应用选择的默认输出设备将生效。

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. // ...
3. // 设置默认输出设备为本机扬声器。
4. audioSessionManager.setDefaultOutputDevice(audio.DeviceType.SPEAKER).then(() => {
5. console.info('setDefaultOutputDevice Success!');
6. // ...
7. }).catch((err: BusinessError) => {
8. console.error(`setDefaultOutputDevice Fail: ${err}`);
9. // ...
10. });
11. // ...
12. // 设置默认输出设备为默认设备,即取消应用设置的默认设备,交由系统选择设备。
13. audioSessionManager.setDefaultOutputDevice(audio.DeviceType.DEFAULT).then(() => {
14. console.info('setDefaultOutputDevice Success!');
15. // ...
16. }).catch((err: BusinessError) => {
17. console.error(`setDefaultOutputDevice Fail: ${err}`);
18. // [Exclude setting_DefaultOutputDevice]

20. console.error(`Failed to set default output device. Code: ${err.code}, message: ${err.message}`);
21. // ...
22. });
```

### 查询本机默认音频输出设备

应用可以通过[getDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#getdefaultoutputdevice20)查询本机默认输出设备类型。

说明

本接口用于查询通过[setDefaultOutputDevice](../harmonyos-references/arkts-apis-audio-audiosessionmanager.md#setdefaultoutputdevice20)接口设置的输出设备。

```
1. let deviceType = audioSessionManager.getDefaultOutputDevice();
2. console.info(`getDefaultOutputDevice Success, deviceType: ${deviceType}`);
```

### 监听输出设备变化

应用可以通过注册[CurrentOutputDeviceChangedEvent](../harmonyos-references/arkts-apis-audio-i.md#currentoutputdevicechangedevent20)监听输出设备的连接状态变化。

说明

currentOutputDeviceChangedCallback包含设备变更的原因及推荐的后续操作。应用应根据不同的变更原因进行处理，并按系统推荐的操作继续或停止当前播放。

```
1. import { audio } from '@kit.AudioKit';  // 导入audio模块。
2. // ...
3. // 同一监听事件中,on方法和off方法传入callback参数一致,off方法取消对应on方法订阅的监听。
4. let currentOutputDeviceChangedCallback = (currentOutputDeviceChangedEvent: audio.CurrentOutputDeviceChangedEvent) => {
5. console.info(`reason of audioSessionStateChanged: ${currentOutputDeviceChangedEvent.changeReason} `);

7. // 为UI收集信息
8. let callbackMsg = `reason of audioSessionStateChanged: ${currentOutputDeviceChangedEvent.changeReason} `;
9. if (globalCallbackUpdate) {
10. globalCallbackUpdate(callbackMsg);
11. }

13. switch (currentOutputDeviceChangedEvent.changeReason) {
14. case audio.AudioStreamDeviceChangeReason.REASON_OLD_DEVICE_UNAVAILABLE:
15. // 响应设备不可用事件,如果应用处于播放状态,应暂停播放,更新UX界面。
16. break;
17. case audio.AudioStreamDeviceChangeReason.REASON_NEW_DEVICE_AVAILABLE:
18. // 应用根据业务情况响应设备可用事件。
19. break;
20. case audio.AudioStreamDeviceChangeReason.REASON_OVERRODE:
21. // 应用根据业务情况响应设备强选事件。
22. break;
23. case audio.AudioStreamDeviceChangeReason.REASON_SESSION_ACTIVATED:
24. // 应用根据业务情况响应audio session激活时的输出设备信息。
25. break;
26. case audio.AudioStreamDeviceChangeReason.REASON_STREAM_PRIORITY_CHANGED:
27. // 应用根据业务情况响应其它更高优先级的音频流触发的设备变更事件。
28. break;
29. case audio.AudioStreamDeviceChangeReason.REASON_UNKNOWN:
30. // 应用根据业务情况响应未知原因事件。
31. break;
32. }
33. };
34. // ...
35. audioSessionManager.on('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);
36. // ...
37. audioSessionManager.off('currentOutputDeviceChanged', currentOutputDeviceChangedCallback);
38. // ...
39. // 取消该事件的所有监听。
40. audioSessionManager.off('currentOutputDeviceChanged');
```
