---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wearengine_faq-6
title: 手机和轻量级智能穿戴设备通信，提示错误码206
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > Wear Engine常见问题 > 手机和轻量级智能穿戴设备通信，提示错误码206
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:10+08:00
doc_updated_at: 2026-08-24
content_hash: sha256:fca78dfadc59133ca43c7db589d158781b6f944837c3a29560e3ba759f1d234e
---

* 手机和穿戴设备的包名或证书指纹不匹配。

  + 轻量级智能穿戴设备侧：需要把手机的包名和[指纹信息](wearengine_faq-9.md#harmonyos-50及之后版本设备的应用)放到允许清单中。
  + 手机侧：需要把轻量级智能穿戴设备侧应用的包名和[指纹信息](wearengine_faq-9.md#harmonyos-50及之后版本设备的应用)配置正确。
* 轻量级智能穿戴设备侧应用不在前台。
* 手机或轻量级智能穿戴设备侧应用没有注册消息接收器。
* 发送的消息为空。
* 蓝牙未连接。
