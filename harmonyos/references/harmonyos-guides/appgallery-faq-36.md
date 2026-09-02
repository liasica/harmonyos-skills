---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/appgallery-faq-36
title: 按需加载成功后，跳转动态模块页面失败？
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > AppGallery Kit常见问题 > 按需加载成功后，跳转动态模块页面失败？
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:24+08:00
doc_updated_at: 2026-04-30
content_hash: sha256:cafd0cac3955edc168cd2e27e524aabc55cab987718002f02d6513e798e936e4
---

**问题现象**

按需加载成功后，开发者业务需要跳转到动态模块的页面，使用Navigation跨包路由时返回100005错误码。

**可能原因**

6.0.2(22)及之前版本，不支持Navigation跨包路由方式，从6.1.0(23)开始，[支持开发者使用Navigation跨包路由跳转到动态安装的HSP中的页面](arkts-navigation-cross-package.md#系统路由表)，建议检查升级HarmonyOS版本。
