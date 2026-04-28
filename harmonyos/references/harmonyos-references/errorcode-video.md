---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-video
title: Video组件错误码
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > 错误码 > UI界面 > Video组件错误码
category: harmonyos-references
scraped_at: 2026-04-28T08:04:57+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:b7ed0506ebc0cb4c7385940d5238df261183c09c0d4ebf9ae2b2874e16c7569f
---

说明

以下仅介绍本模块特有错误码，媒体错误码请参考[Media错误码](errorcode-media.md)，通用错误码请参考[通用错误码](errorcode-universal.md)。

## 103601 播放器创建失败

**错误信息**

Failed to create the media player.

**错误描述**

播放器创建失败。

**可能原因**

媒体服务不存在，或因内存不足导致创建失败。

**处理步骤**

销毁当前实例，并重新创建，如果重新创建失败，则停止相关操作。

## 103602 视频资源设置无效

**错误信息**

Not a valid source.

**错误描述**

视频资源设置无效。

**可能原因**

系统找不到资源文件，或资源文件异常。

**处理步骤**

确保资源文件存在且正常，再重新设置Video组件的视频源。
