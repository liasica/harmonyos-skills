---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-input-device-management
title: 查询和监听音频输入设备
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频设备路由管理 > 查询和监听音频输入设备
category: harmonyos-guides
scraped_at: 2026-04-28T07:45:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ccf820c89ed07e26591bcdfc75684be48301a777c1728c80dd078ed922dddb4a
---

本模块提供音频输入设备管理能力，包括查询输入设备信息、监听设备连接状态变化等。具体API说明可参考文档[AudioRoutingManager](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md)。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/blob/master/code/DocsSample/Media/Audio/AudioRoutingManagerSampleJS)。

## 创建AudioRoutingManager实例

在使用AudioRoutingManager管理音频设备前，需要先导入模块并创建实例。

```
1. import { audio } from '@kit.AudioKit'; // 导入audio模块。

3. let audioManager = audio.getAudioManager(); // 需要先创建AudioManager实例。
4. let audioRoutingManager = audioManager.getRoutingManager(); // 再调用AudioManager的方法创建AudioRoutingManager实例。
```

## 支持的音频输入设备类型

目前支持的音频输入设备见下表：

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WIRED\_HEADSET | 3 | 有线耳机，带麦克风。 |
| BLUETOOTH\_SCO | 7 | 蓝牙设备SCO（Synchronous Connection Oriented）连接。 |
| MIC | 15 | 麦克风。 |
| USB\_HEADSET | 22 | USB耳机，带麦克风。 |
| NEARLINK | 31 | 星闪设备。 |

## 获取输入设备信息

使用[getDevices](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md#getdevices9)方法可以获取当前所有输入设备的信息。

```
1. import { audio } from '@kit.AudioKit'; // 导入audio模块。
2. // ...
3. audioRoutingManager.getDevices(audio.DeviceFlag.INPUT_DEVICES_FLAG).then((data: audio.AudioDeviceDescriptors) => {
4. console.info('Promise returned to indicate that the device list is obtained.');

6. // ...
7. });
```

## 监听设备连接状态变化

可以设置监听事件来监听设备连接状态的变化，当有设备连接或断开时触发回调：

```
1. import { audio } from '@kit.AudioKit';  // 导入audio模块。
2. // ...
3. // 监听音频设备状态变化。
4. audioRoutingManager.on('deviceChange', audio.DeviceFlag.INPUT_DEVICES_FLAG,
5. (deviceChanged: audio.DeviceChangeAction) => {
6. console.info('device change type : ' + deviceChanged.type);  // 设备连接状态变化,0为连接,1为断开连接。
7. console.info('device descriptor size : ' + deviceChanged.deviceDescriptors.length);
8. console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceRole);  // 设备角色。
9. console.info('device change descriptor : ' + deviceChanged.deviceDescriptors[0].deviceType);  // 设备类型。

11. // ...
12. });
13. // ...
14. // 取消监听音频设备状态变化。
15. audioRoutingManager.off('deviceChange', (deviceChanged: audio.DeviceChangeAction) => {
16. console.info('Should be no callback.');
17. });
```
