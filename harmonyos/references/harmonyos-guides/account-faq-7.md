---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-7
title: HarmonyOS APK应用和HarmonyOS应用在一键登录场景下的用户数据如何互通
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > HarmonyOS APK应用和HarmonyOS应用在一键登录场景下的用户数据如何互通
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:16+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:9543ca31b3c4e2f2ea28cc7a088734924162775488dad4f41799e6ad21078a11
---

终端设备从HarmonyOS 3.x/4.x（简称HarmonyOS）升级到HarmonyOS NEXT/5.0.x及之后版本（简称HarmonyOS NEXT）。

1. HarmonyOS APK应用使用OpenID关联用户数据时，将用户数据关系切换成UnionID，具体切换指导可以参考：[通过OpenID获取UnionID](../harmonyos-references/account-api-get-unionid.md)。
2. HarmonyOS APK应用使用UnionID关联用户数据时，在HarmonyOS NEXT/5.0.x上接入华为账号一键登录获取手机号后，应用需要同时将UnionID和手机号与用户信息进行关联，最终实现应用使用华为账号一键登录和手机号登录数据互通。详细流程可以参考：[用户场景设计](account-phone-unionid-login.md#用户场景设计)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/vwXIiGrLTBy0QS2HnZdxZQ/zh-cn_image_0000002821837775.png?HW-CC-KV=V1&HW-CC-Date=20261121T011049Z&HW-CC-Expire=31536000000&HW-CC-Sign=4C4F5FA8AD3D0BB4E2039A527D61AA4CDE8368579D89D32A0A88F10D6839EC61)
