---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/graphics-accelerate-assetdownload-faq-8
title: 是否可以终止已发布的下载任务，例如游戏出现问题时是否能够及时关闭？
breadcrumb: 指南 > 图形 > Graphics Accelerate Kit（图形加速服务） > Graphics Accelerate Kit常见问题 > 游戏资源加速服务 > 是否可以终止已发布的下载任务，例如游戏出现问题时是否能够及时关闭？
category: harmonyos-guides
scraped_at: 2026-04-28T07:47:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ee80a0af6edbd5e9072ca8cae9a58bcbf340998bd5bd54183049366474b5b460
---

能够及时关闭。

若在发布下载任务后发现资源包存在问题，可以前往AppGallery Connect终止资源包下载任务，具体操作请参见[发布下载任务](graphics-accelerate-assetdownload-release.md#发布下载任务)。下载任务终止后，在安装游戏后/大版本更新后/设备满足闲时条件时，均不再拉起该应用的ExtensionAbility进行资源包后台下载。
