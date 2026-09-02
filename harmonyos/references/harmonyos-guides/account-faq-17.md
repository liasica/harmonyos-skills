---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-17
title: 一键登录场景下，应用已展示一键登录页，此时用户退出、切换或注销华为账号应该如何处理
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 一键登录场景下，应用已展示一键登录页，此时用户退出、切换或注销华为账号应该如何处理
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:23+08:00
doc_updated_at: 2026-07-28
content_hash: sha256:ac94a292794662bfcfa4677cf623aad533167b0c9a803dfe7af4b4889f90f8df
---

应用通过订阅[华为账号登录/登出事件](account-notification-events.md#事件说明)监听当前设备华为账号的登录状态，若监听到华为账号登出事件，则需跳转至其他登录页面；若监听到华为账号登录事件，则需重新获取匿名手机号并刷新一键登录页。示例代码详见[华为账号一键登录SampleCode](https://gitcode.com/HarmonyOS_Samples/accountkit-samplecode-clientdemo-arkts)。
