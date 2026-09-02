---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio
title: 模块描述
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > 模块描述
category: harmonyos-references
scraped_at: 2026-09-02T15:02:18+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:e156239c1c7e85d4efc8b20da08da65ccfb7207dd94a0fafed8d4f55d90c5b7e
---

音频管理提供基础的音频控制能力，包括音量调节、设备管理、数据采集及渲染。

本模块提供以下音频相关的常用功能：

* [AudioManager](arkts-apis-audio-audiomanager.md)：音频管理器。
* [AudioDeviceEnhanceManager](arkts-apis-audio-audiodeviceenhancemanager.md)：音频设备增强管理器。
* [AudioRenderer](arkts-apis-audio-audiorenderer.md)：音频渲染器，用于播放PCM（Pulse Code Modulation）音频数据。
* [AudioCapturer](arkts-apis-audio-audiocapturer.md)：音频采集器，用于录制PCM音频数据。

**说明** 

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { audio } from '@kit.AudioKit';
```
