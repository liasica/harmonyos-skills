---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-17
title: 一键登录场景下，应用已展示一键登录页，此时用户退出、切换或注销华为账号应该如何处理
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 一键登录场景下，应用已展示一键登录页，此时用户退出、切换或注销华为账号应该如何处理
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:05+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:1f3898f3707a6a630a079997f9026e8a3b231e20918ac2e52fa20882f833ff41
---

应用通过[订阅华为账号的登录/登出事件](account-login-state.md)监听当前设备华为账号的登录状态，若监听到华为账号登出事件，则需跳转至其他登录页面；若监听到华为账号登录事件，则需重新获取匿名手机号并刷新一键登录页。示例代码详见[华为账号一键登录SampleCode](https://gitcode.com/HarmonyOS_Samples/accountkit-samplecode-clientdemo-arkts)。
