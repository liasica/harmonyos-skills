---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/wearengine_faq-6
title: 手机和轻量级智能穿戴设备通信，提示错误码206
breadcrumb: 指南 > 系统 > 硬件 > Wear Engine Kit（穿戴服务） > Wear Engine常见问题 > 手机和轻量级智能穿戴设备通信，提示错误码206
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:55+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:756906c797b2d9ec1ed291e94a401b06e5ed395ff55d5d2f31e413fd8410a500
---

* 手机和穿戴设备的包名或证书指纹不匹配

  + 轻量级智能穿戴设备侧：需要把手机的包名和指纹信息放到白名单中
  + 手机侧：需要把轻量级智能穿戴设备侧应用的包名和指纹信息配置正确
* 轻量级智能穿戴设备侧应用不在前台
* 手机或轻量级智能穿戴设备侧应用没有注册消息接收器
* 发送的消息为空
* 蓝牙未连接
