---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/appendix-osaccount-authorization-privileges
title: 系统账号特权列表
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > ArkTS API > 账号管理 > 系统账号特权列表
category: harmonyos-references
scraped_at: 2026-11-12T09:55:50+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:06bf9527253faef312cdf88fa0d19ffde8d300cca703e544eaf093be74ece0e7
---

下表内容为系统账号授权模块可授权的特权。

**说明** 

特权的可用性取决于当前系统版本是否已部署该特权的配置。若系统版本未包含该特权配置，调用[authorization.getAuthorizationManager().requestAuthorization](js-apis-osaccount-authorization.md#requestauthorization)时将返回[AUTHORIZATION\_NOT\_SUPPORTED](js-apis-osaccount-authorization.md#authorizationresultcode)。

| 特权 | 特权值 | 说明 | 有效期 | 关联的权限 |
| --- | --- | --- | --- | --- |
| ohos.privilege.operate\_raw\_net\_packets | PRIVILEGE\_OPERATE\_RAW\_NET\_PACKETS | 操作原始网络包的特权。 | 与被授权进程的生命周期相绑定 | ohos.permission.kernel.NET\_RAW |
| ohos.privilege.monitor\_raw\_usb\_packets | PRIVILEGE\_MONITOR\_RAW\_USB\_PACKETS | 监听USB数据包的特权。 | 与被授权进程的生命周期相绑定 | ohos.permission.kernel.USB\_CAPTURE |
