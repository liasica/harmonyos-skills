---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-systemsoundmanager
title: "@ohos.multimedia.systemSoundManager (系统声音管理)"
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.systemSoundManager (系统声音管理)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:20+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:b82016fb4981dab838ec825501e0e4fb7b8cecd03b9c2e560d422e54d08cc1b9
---

本模块提供系统声音管理能力，包括系统音效类型的定义、系统音效播放器的获取等。当需要在应用内播放系统音效以统一使用系统预设音效、带来一致的用户体验时，使用本模块接口完成相关操作。

**说明** 

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { systemSoundManager } from '@kit.AudioKit';
```

## SystemSoundType

枚举，表示系统音效类型。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PHOTO\_SHUTTER | 0 | 拍照音效。 |
| VIDEO\_RECORDING\_BEGIN | 1 | 视频录制开始音效。 |
| VIDEO\_RECORDING\_END | 2 | 视频录制结束音效。 |

## systemSoundManager.createSystemSoundPlayer

createSystemSoundPlayer(): Promise<SystemSoundPlayer | null>

创建系统音效播放器对象。使用Promise异步回调。

**说明** 

* 调用createSystemSoundPlayer()创建播放器后，必须在使用完毕后调用release()释放播放器资源。
* 详细的使用说明和方法关系请参见[SystemSoundPlayer (音效播放器)](js-apis-inner-multimedia-systemsoundplayer.md)。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[SystemSoundPlayer](js-apis-inner-multimedia-systemsoundplayer.md#systemsoundplayer) | null> | 成功返回系统音效播放器对象，用于播放拍照音效、视频录制音效等系统音效；失败返回null。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400101 | No memory. Return by promise. |

**示例：**

```ts
import { BusinessError } from '@kit.BasicServicesKit';

let systemSoundPlayer: systemSoundManager.SystemSoundPlayer | null = null;

systemSoundManager.createSystemSoundPlayer().then((systemSoundPlayerInstance) => {
  systemSoundPlayer = systemSoundPlayerInstance;
  console.info('Succeeded in creating the system sound player.');
}).catch((err: BusinessError) => {
  console.error(`Failed to create the system sound player. Code: ${err.code}, message: ${err.message}`);
});
```

## SystemSoundPlayer

type SystemSoundPlayer = \_SystemSoundPlayer

系统音效播放器对象，用于播放拍照音效、视频录制音效等系统音效。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

| 类型 | 说明 |
| --- | --- |
| [\_SystemSoundPlayer](js-apis-inner-multimedia-systemsoundplayer.md#systemsoundplayer) | 系统音效播放器对象。 |
