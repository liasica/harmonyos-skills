---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wearengine_faq-6
title: 手机和轻量级智能穿戴设备通信，提示错误码206
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > Wear Engine常见问题 > 手机和轻量级智能穿戴设备通信，提示错误码206
category: harmonyos-guides
scraped_at: 2026-11-12T09:51:52+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:1d9f731afa897ba461c85af6103b0e16b2c6e67c57f8f3833939c289c56e86ef
---

* 手机侧应用与轻量级智能穿戴设备侧应用的包名或证书指纹不匹配。

  + 针对轻量级智能穿戴设备侧应用：请将手机应用的包名及[指纹信息](wearengine_faq-9.md#harmonyos-50及之后版本设备的应用)添加至允许清单中。
  + 针对手机侧应用：请确保已正确配置轻量级智能穿戴设备侧应用的包名及[指纹信息](wearengine_faq-9.md#harmonyos-50及之后版本设备的应用)。
* 轻量级智能穿戴设备侧应用不在前台。
* 手机或轻量级智能穿戴设备侧应用没有注册消息接收器。
* 发送的消息为空。
* 蓝牙未连接。
