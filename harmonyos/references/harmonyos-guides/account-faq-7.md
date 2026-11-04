---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-7
title: HarmonyOS APK应用和HarmonyOS应用在一键登录场景下的用户数据如何互通
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > HarmonyOS APK应用和HarmonyOS应用在一键登录场景下的用户数据如何互通
category: harmonyos-guides
scraped_at: 2026-11-04T08:30:23+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:b52716b4bbb15013ce45bd6d73b13ee6507ff40fc3668ab94c15711410b51564
---

终端设备从HarmonyOS 3.x/4.x（简称HarmonyOS）升级到HarmonyOS NEXT/5.0.x及之后版本（简称HarmonyOS NEXT）。

1. HarmonyOS APK应用使用OpenID关联用户数据时，将用户数据关系切换成UnionID，具体切换指导可以参考：[通过OpenID获取UnionID](../harmonyos-references/account-api-get-unionid.md)。
2. HarmonyOS APK应用使用UnionID关联用户数据时，在HarmonyOS NEXT/5.0.x上接入华为账号一键登录获取手机号后，应用需要同时将UnionID和手机号与用户信息进行关联，最终实现应用使用华为账号一键登录和手机号登录数据互通。详细流程可以参考：[用户场景设计](account-phone-unionid-login.md#用户场景设计)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/h9QENgcAQ9eo_DPPyX3UPw/zh-cn_image_0000002779691238.png)
