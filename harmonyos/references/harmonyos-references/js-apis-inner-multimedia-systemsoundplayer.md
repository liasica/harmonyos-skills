---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-inner-multimedia-systemsoundplayer
title: SystemSoundPlayer (音效播放器)
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > multimedia > SystemSoundPlayer (音效播放器)
category: harmonyos-references
scraped_at: 2026-04-28T08:11:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:411c7f88b62ba10d1b9d8e4363c7a7a920c4f34c5c24eff96f2d1a39bfd54be3
---

音效播放器提供了加载、卸载和播放系统声音的功能。

SystemSoundPlayer需要和[@ohos.multimedia.systemSoundManager](js-apis-systemsoundmanager.md)配合使用，才能完成管理系统音效的功能。

说明

本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { systemSoundManager } from '@kit.AudioKit';
```

## SystemSoundPlayer

PhonePC/2in1TabletTVWearable

系统音效播放器提供了拍照和录制视频音效的播放功能。在调用SystemSoundPlayer的接口前，需要先通过[createSystemSoundPlayer](js-apis-systemsoundmanager.md#systemsoundmanagercreatesystemsoundplayer)创建系统音效播放器对象。

### load

PhonePC/2in1TabletTVWearable

load(soundType: systemSoundManager.SystemSoundType): Promise<void>

加载系统音效。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| soundType | [systemSoundManager.SystemSoundType](js-apis-systemsoundmanager.md#systemsoundtype) | 是 | 系统音效类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | I/O error. |
| 5400105 | Crash or blocking occurs in system process. |
| 5400108 | Parameter check failed. Returned by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. systemSoundPlayer?.load(systemSoundManager.SystemSoundType.PHOTO_SHUTTER).then(() => {
4. console.info('Succeeded in calling the load method.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to call the load method. Code: ${err.code}, message: ${err.message}`);
7. });
```

### play

PhonePC/2in1TabletTVWearable

play(soundType: systemSoundManager.SystemSoundType): Promise<void>

播放系统音效。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| soundType | [systemSoundManager.SystemSoundType](js-apis-systemsoundmanager.md#systemsoundtype) | 是 | 系统音效类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400103 | I/O error. |
| 5400105 | Crash or blocking occurs in system process. |
| 5400108 | Parameter check failed. Returned by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. systemSoundPlayer?.play(systemSoundManager.SystemSoundType.PHOTO_SHUTTER).then(() => {
4. console.info('Succeeded in calling the play method.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to call the play method. Code: ${err.code}, message: ${err.message}`);
7. });
```

### unload

PhonePC/2in1TabletTVWearable

unload(soundType: systemSoundManager.SystemSoundType): Promise<void>

卸载之前已加载的系统音效。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| soundType | [systemSoundManager.SystemSoundType](js-apis-systemsoundmanager.md#systemsoundtype) | 是 | 系统音效类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400105 | Crash or blocking occurs in system process. |
| 5400108 | Parameter check failed. Returned by promise. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. systemSoundPlayer?.unload(systemSoundManager.SystemSoundType.PHOTO_SHUTTER).then(() => {
4. console.info('Succeeded in calling the unload method.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to call the unload method. Code: ${err.code}, message: ${err.message}`);
7. });
```

### release

PhonePC/2in1TabletTVWearable

release(): Promise<void>

释放系统音效播放器。使用Promise异步回调。

**模型约束**：此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.SystemSound.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[Media错误码](errorcode-media.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 5400105 | Crash or blocking occurs in system process. |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';

3. systemSoundPlayer?.release().then(() => {
4. console.info('Succeeded in calling the release method.');
5. }).catch((err: BusinessError) => {
6. console.error(`Failed to call the release method. Code: ${err.code}, message: ${err.message}`);
7. });
```
