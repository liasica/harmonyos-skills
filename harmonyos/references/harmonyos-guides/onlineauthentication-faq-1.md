---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/onlineauthentication-faq-1
title: IFAA常见问题
breadcrumb: 指南 > 系统 > 安全 > Online Authentication Kit（在线认证服务） > Online Authentication Kit常见问题 > IFAA常见问题
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:56b05cbebc33c80d161c3e4450921c13577290739cb0353209539d6ec0247ff3
---

## 开通IFAA免密认证失败

**问题现象**

开通IFAA免密认证失败。

**可能原因**

移动端设备没有联网。

**解决措施**

移动端设备连接Wi-Fi或热点，再次尝试。

## IFAA认证超时失败

**问题现象**

IFAA认证报错The service is abnormal。

**可能原因**

IFAA进程是非常驻进程，拉起后有时间限制。只有[preAuth](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaapreauth)接口拉起IFAA进程时有1分钟的保活时间，其余接口拉起IFAA进程的保活时间均为10秒。如果在preAuth和auth之间调用了[getAnonymousId](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaagetanonymousid)等其他接口，会将保活时间刷新为10秒，导致preAuth和auth之间的时间间隔超出10秒后IFAA进程退出，auth调用超时失败。

**解决措施**

确保[preAuth](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaapreauth)和[auth](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaaauth)连续调用，在preAuth和auth之间不要调用其他IFAA接口，如[getAnonymousId](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaagetanonymousid)，避免保活时间被刷新为10秒导致超时。

可通过hilog日志辅助排查：

* 查看日志中“ifaa delay unload time is”确认当前IFAA进程的保活时间。
* 若日志中出现“Service unloaded successfully.”，表示IFAA进程已退出，后续调用[auth](../harmonyos-references/onlineauthentication-ifaa-api.md#ifaaauth)接口会失败。
