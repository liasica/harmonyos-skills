---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avmusictemplate-e
title: Enums
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avMusicTemplate (音频模板) > Enums
category: harmonyos-references
scraped_at: 2026-04-28T08:12:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:5b659be8b5bb09ea9380ea1169b74901a17098261e8a14cb9bd8782730693f42
---

说明

* 本模块首批接口从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块仅适用于API version 23及以上版本的Car设备。

## AVMusicTemplateType

表示音频模板类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DEFAULT | 'smartCar' | 音频模板类型的默认值。  用于标识当前音频模板应用的业务类型，用户创建模板时可根据自身业务修改此值。 |

## EntityType

表示媒体资源类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 未知的媒体资源类型。 |
| SINGLE | 1 | 单曲类型。 |
| SINGER | 2 | 歌手类型。 |
| ALBUM | 3 | 专辑类型。 |
| RANKING | 4 | 排行榜类型。 |
| BANNER | 5 | 海报类型。 |
| RADIO\_STATION | 6 | 电台类型。 |

## PlaybackState

表示媒体资源的播放状态的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PLAYBACK\_STATE\_PREPARE | 0 | 准备状态。  表示媒体文件尚未准备好播放，媒体正在加载或缓冲中。 |
| PLAYBACK\_STATE\_PLAY | 1 | 正在播放状态。 |
| PLAYBACK\_STATE\_PAUSE | 2 | 暂停状态。 |
| PLAYBACK\_STATE\_STOP | 3 | 停止状态。 |
| PLAYBACK\_STATE\_COMPLETED | 4 | 播放完成状态。 |
| PLAYBACK\_STATE\_ERROR | 5 | 播放错误状态。 |
| PLAYBACK\_STATE\_BUFFERING | 6 | 缓冲状态。 |

## Sort

表示查询到的列表数据排序类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NONE | 0 | 默认值，默认正序。 |
| ORDER | 1 | 正序。 |
| REVERSE\_ORDER | 2 | 倒序。 |

## SettingType

表示设置类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SWITCH | 0 | 开关设置，用于控制功能的开启或关闭状态。 |
| LIST | 1 | 列表设置，用于从多个选项中选择一个选项。 |
| JUMP | 2 | 跳转设置，用于跳转到另一个界面。 |

## DialogType

表示对话框类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 普通对话框。 |
| INTERNET | 1 | 联网对话框。 |
| FLOW | 2 | 流程对话框。 |
| PAID | 3 | 付费对话框。 |
| VIP | 4 | VIP对话框。 |
| LOGIN | 5 | 登录对话框。 |
| ERROR | 6 | 错误对话框。 |
| UNKNOWN | 7 | 未知对话框。 |

## ButtonType

表示按钮类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 0 | 普通按钮。 |
| EMPHASIZE | 1 | 强调按钮。 |

## MemberPurchaseType

表示会员购买类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

| 名称 | 值 | 说明 |
| --- | --- | --- |
| NORMAL | 'normal' | 常规购买。 |
| BANNER | 'banner' | 会员推广海报。 |

## SearchPlayInfoType

表示搜播信息类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

| 名称 | 值 | 说明 |
| --- | --- | --- |
| PLAY\_MUSIC | 'playMusic' | 播放音乐。 |
| PLAY\_VIDEO | 'playVideo' | 播放视频。 |

## DownloadStatus

表示下载状态类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

| 名称 | 值 | 说明 |
| --- | --- | --- |
| DOWNLOAD\_SUCCESS | 0 | 下载成功。 |
| DOWNLOADING | 1 | 下载中。 |
| DOWNLOAD\_FAIL | 2 | 下载失败。 |

## AVMusicTemplateErrorCode

表示错误码类型的枚举。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.Multimedia.AVSession.AVMusicTemplate

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ERR\_CODE\_CREATE\_AV\_MUSIC\_TEMPLATE\_FAILED | 35000001 | 音频模板创建失败。 |
| ERR\_CODE\_CREATE\_AV\_MUSIC\_TEMPLATE\_CONTROLLER\_FAILED | 35000002 | 音频模板控制器创建失败。 |
| ERR\_CODE\_TEMPLATE\_LISTENER\_NO\_EXIT | 35000003 | 模板监听未注册。 |
| ERR\_CODE\_CONTROLLER\_CALLBACK\_NO\_EXIT | 35000004 | 未注册模板控制器回调。 |
| ERR\_CODE\_AV\_MUSIC\_TEMPLATE\_NOT\_EXIST | 35000005 | 音频模板不存在。 |
| ERR\_CODE\_CONTROLLER\_NOT\_EXIST | 35000006 | 模板控制器不存在。 |
| ERR\_CODE\_CONTROLLER\_IS\_EXIST | 35000007 | 模板控制器已经存在。 |
| ERR\_CODE\_SERVICE\_NOT\_EXIST | 35000008 | 音频模板管理服务不存在。 |
| ERR\_CODE\_SERVICE\_EXCEPTION | 35000009 | 音频模板管理服务异常。 |
| ERR\_CODE\_EXCEED\_MAX\_DATA\_SIZE | 35000010 | 数据超过了允许的最大传输容量。 |
| ERR\_CODE\_WRITE\_RESULT\_EXCEPTION | 35000011 | 写数据失败，数据不可用。 |
| ERR\_CODE\_AV\_MUSIC\_TEMPLATE\_ERROR | 35000012 | 音频模板错误。 |
