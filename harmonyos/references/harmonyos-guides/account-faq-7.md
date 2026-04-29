---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-7
title: HarmonyOS APK应用和HarmonyOS应用在一键登录场景下的用户数据如何互通
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > HarmonyOS APK应用和HarmonyOS应用在一键登录场景下的用户数据如何互通
category: harmonyos-guides
scraped_at: 2026-04-29T13:36:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:121b4440aac223d6399aa1d24babd1b155a1256f38c63a07a6a5393c7feda4d7
---

终端设备从HarmonyOS 3.x/4.x（简称HarmonyOS）升级到HarmonyOS NEXT/5.0.x及之后版本（简称HarmonyOS NEXT）。

1. HarmonyOS APK应用使用OpenID关联用户数据时，将用户数据关系切换成UnionID，具体切换指导可以参考：[通过OpenID获取UnionID](../harmonyos-references/account-api-get-unionid.md)。
2. HarmonyOS APK应用使用UnionID关联用户数据时，在HarmonyOS NEXT/5.0.x上接入华为账号一键登录获取手机号后，应用需要同时将UnionID和手机号与用户信息进行关联，最终实现应用使用华为账号一键登录和手机号登录数据互通。详细流程可以参考：[用户场景设计](account-phone-unionid-login.md#用户场景设计)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/_8q82nFzQxmHWOz76Yql3g/zh-cn_image_0000002558765264.png?HW-CC-KV=V1&HW-CC-Date=20260429T053657Z&HW-CC-Expire=86400&HW-CC-Sign=702A8E990BE19AF03024D29C25808831A714D20C632EF282FE325A102EE36214)
