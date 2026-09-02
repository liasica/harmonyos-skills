---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-faq-4
title: 一键登录场景下无法获取到明文手机号如何解决
breadcrumb: 指南 > 应用服务 > Account Kit（华为账号服务） > Account Kit常见问题 > 一键登录场景下无法获取到明文手机号如何解决
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:23+08:00
doc_updated_at: 2026-05-12
content_hash: sha256:7fea4d3a5f96a7b215f8264ac876979f0617a235460449452d54b77683c12c05
---

阅读此章节前请先保证已在华为账号一键登录场景成功获取到匿名手机号。在华为账号一键登录场景下无法获取到明文手机号时，建议通过以下步骤排查解决：

1. 华为账号未绑定手机号，该异常场景应用需要展示其他登录方式。
2. 使用华为账号一键登录服务的账号必须是中国境内（香港特别行政区、澳门特别行政区、中国台湾除外）华为账号。
3. 应用用于向服务端获取手机号的authCode需要通过调用华为账号一键登录组件获取，详情可参考一键登录[客户端开发](account-phone-unionid-login.md#客户端开发)。
