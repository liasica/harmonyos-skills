---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/nearlink-preparations
title: 开发准备
breadcrumb: 指南 > 系统 > 网络 > NearLink Kit（星闪服务） > 开发准备
category: harmonyos-guides
scraped_at: 2026-04-28T07:43:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:914b46246a30c51ee3a7e3b5ef3bcc010098ede9511c9e6d1d61f2ca64e5939b
---

1. 请先确认设备支持星闪功能。确认方法：进入“设置 > 多设备协同”界面（不同产品或系统版本可能为“设置 > 星闪和蓝牙”），确认“星闪”选项存在。若选项不存在，则设备不支持星闪功能。
2. 请参考“[应用开发准备](application-dev-overview.md)”完成开发者注册、创建应用、安装开发环境、配置签名信息等基本准备工作，再继续进行以下开发活动。
3. 开发者需要在应用中动态申请星闪权限ohos.permission.ACCESS\_NEARLINK，包括在应用配置文件中声明此权限，并向用户申请授权。具体申请方式请参考[向用户申请授权](request-user-authorization.md)。
