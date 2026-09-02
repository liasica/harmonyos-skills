---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-cloudfoundation-4
title: 认证服务登录状态是否有时效
breadcrumb: FAQ > 应用服务开发 > 云开发服务（Cloud Foundation Kit） > 认证服务登录状态是否有时效
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:0fea381a455fec0cb0ce7e74d7ca923b26a72ae585d01d52f02549e4a63d612a
---

## 问题现象

1. AGC云开发认证服务的华为账号登录，登录后如果没有登出，登录的状态是不是有时效的？
2. 如果登录状态是有时效的，失效后是不是就不能对云数据库数据进行更新操作？
3. 如果登录状态是有时效的，该如何去判断已失效，并重新登录？

## 解决方案

1. 即使未主动登出，通过AGC云开发认证服务进行的华为账号登录状态也是有时效的。

   详细信息请参考[官方文档](../App/agc-help-auth-login-hwaccount-0000002236337010.md#section187031033123020)。
2. 一旦AGC认证信息失效，端侧用户将暂时失去“认证用户”身份，此时对云数据库的更新（upsert）权限会立即被收回，无法再执行任何需要“认证用户”身份的数据更新操作。详细请参考[权限管理](../AppGallery-connect-Guides/agc-clouddb-aboutclouddb-0000001080975612.md#section13972247121)。
3. 判断失效的核心方法推荐“主动+被动”双保险做法。

   主动检测：（App启动或写库前）先取currentUser，再调silentSignIn()拉起华为帐号授权页。

   被动兜底：（调用云端接口时）捕获executeUpsert()等接口返回的401/403或PERMISSION\_DENIED。
