---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/audio-input-device-management
title: 查询和监听音频输入设备
breadcrumb: 指南 > 媒体 > Audio Kit（音频服务） > 音频设备路由管理 > 查询和监听音频输入设备
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0e0dc932880351417720e02013e81505d0e39c162ae611abb4d64f57af1f0c36
---

本模块提供音频输入设备管理能力，包括查询输入设备信息、监听设备连接状态变化等。具体API说明可参考文档[AudioRoutingManager](../harmonyos-references/arkts-apis-audio-audioroutingmanager.md)。

以下各步骤示例为片段代码，可通过示例代码右下方链接获取[完整示例](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/AudioRoutingAndVolumeSample)。

## 创建AudioRoutingManager实例

在使用AudioRoutingManager管理音频设备前，需要先导入模块并创建实例。

```typescript
import { audio } from '@kit.AudioKit';
// ...

let audioManager = audio.getAudioManager();
let audioRoutingManager = audioManager.getRoutingManager();
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

```typescript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

  audioRoutingManager.getDevices(audio.DeviceFlag.INPUT_DEVICES_FLAG).then((audioDeviceDescriptors: audio.
    AudioDeviceDescriptors) => {
    console.info(`Succeeded in getting devices. AudioDeviceDescriptors: ${JSON.stringify(audioDeviceDescriptors)}`);
    // ...
  }).catch((err: BusinessError) => {
    console.error(`Failed to get devices. Code: ${err.code}, message: ${err.message}`);
    // ...
  });
```

## 监听设备连接状态变化

可以设置监听事件来监听设备连接状态的变化，当有设备连接或断开时触发回调：

```typescript
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...

let deviceChangeCallback = (deviceChanged: audio.DeviceChangeAction) => {
  console.info(`Succeeded in using on function. DeviceChangeAction: ${JSON.stringify(deviceChanged)}`);
  // ...
}
// ...

  try {
    // 监听音频设备状态变化。
    audioRoutingManager.on('deviceChange', audio.DeviceFlag.INPUT_DEVICES_FLAG, deviceChangeCallback);
  } catch (err) {
    let error = err as BusinessError;
    console.error(`Failed to use on function. Code: ${error.code}, message: ${error.message}`);
    // ...
  }
```
