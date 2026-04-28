---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-audio-c
title: Constants
breadcrumb: API参考 > 媒体 > Audio Kit（音频服务） > ArkTS API > @ohos.multimedia.audio (音频管理) > Constants
category: harmonyos-references
scraped_at: 2026-04-28T08:11:42+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f675de1d0fd14e754d0020d97618f2994afd984bd12a9de05810f52cccc60757
---

说明

本模块首批接口从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

| 名称 | 类型 | 只读 | 说明 |
| --- | --- | --- | --- |
| DEFAULT\_VOLUME\_GROUP\_ID9+ | number | 是 | 默认音量组id。  **系统能力：** SystemCapability.Multimedia.Audio.Volume |
| DEFAULT\_INTERRUPT\_GROUP\_ID9+ | number | 是 | 默认音频中断组id。  **系统能力：** SystemCapability.Multimedia.Audio.Interrupt |

**示例：**

```
1. import { audio } from '@kit.AudioKit';

3. const defaultVolumeGroupId = audio.DEFAULT_VOLUME_GROUP_ID;
4. const defaultInterruptGroupId = audio.DEFAULT_INTERRUPT_GROUP_ID;
```
