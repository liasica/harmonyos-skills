---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-systemsoundmanager
title: @ohos.multimedia.systemSoundManager (系统声音管理)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.systemSoundManager (系统声音管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fc131a4e8dac83d1b495c44fc3dfeaca25ebf8823edfeb4bd4244a5cad02e01f
---

系统声音管理提供管理系统声音的基础能力，包括对系统音效类型的定义、获取系统音效播放器等。

说明

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { systemSoundManager } from '@kit.AudioKit';
```

## SystemSoundType

PhonePC/2in1TabletTVWearable

枚举，表示系统音效类型。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PHOTO\_SHUTTER | 0 | 拍照音效。 |
| VIDEO\_RECORDING\_BEGIN | 1 | 视频录制开始音效。 |
| VIDEO\_RECORDING\_END | 2 | 视频录制结束音效。 |

## systemSoundManager.createSystemSoundPlayer

PhonePC/2in1TabletTVWearable

createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>

创建系统音效播放器对象。使用Promise异步回调。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SystemSoundPlayer](js-apis-inner-multimedia-systemsoundplayer.md#systemsoundplayer) | null> | 成功返回系统音效播放器对象，失败返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Return by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. let systemSoundPlayer: systemSoundManager.SystemSoundPlayer | null = null;

5. systemSoundManager.createSystemSoundPlayer().then((systemSoundPlayerInstance) => {
6. console.info('Succeeded in creating the system sound player.');
7. systemSoundPlayer = systemSoundPlayerInstance;
8. }).catch((err: BusinessError) => {
9. console.error(`Failed to create the system sound player. Code: ${err.code}, message: ${err.message}`);
10. });
```

## SystemSoundPlayer

PhonePC/2in1TabletTVWearable

type SystemSoundPlayer = \_SystemSoundPlayer

系统音效播放器对象。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

| 类型 | 说明 |
| --- | --- |
| [\_SystemSoundPlayer](js-apis-inner-multimedia-systemsoundplayer.md#systemsoundplayer) | 系统音效播放器对象。 |
