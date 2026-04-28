---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-avsession
title: 模块描述
breadcrumb: API参考 > 媒体 > AVSession Kit（音视频播控服务） > ArkTS API > @ohos.multimedia.avsession (媒体会话管理) > 模块描述
category: harmonyos-references
scraped_at: 2026-04-28T08:12:14+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5f6425375ac211533ddd4f0b59128e448d4b72fb9e46078504b71f6be756f12a
---

媒体会话管理提供媒体播控相关功能的接口，目的是让应用接入播控中心。

该模块提供以下媒体会话相关的常用功能：

* [AVSession](arkts-apis-avsession-avsession.md) : 会话，可用于设置元数据、播放状态信息等操作。
* [AVSessionController](arkts-apis-avsession-avsessioncontroller.md): 会话控制器，可用于查看会话ID，完成对会话发送命令及事件，获取会话元数据、播放状态信息等操作。
* [AVCastController](arkts-apis-avsession-avcastcontroller.md): 投播控制器，可用于投播场景下，完成播放控制、远端播放状态监听、远端播放状态信息获取等操作。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```
1. import { avSession } from '@kit.AVSessionKit';
```
