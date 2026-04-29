---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/password-shared-apps-web-pages
title: 应用与网页共用账号密码
breadcrumb: 指南 > 系统 > 安全 > 密码自动填充服务 > 应用与网页共用账号密码
category: harmonyos-guides
scraped_at: 2026-04-29T13:30:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:1b6005fda5fe4d054158f96cc1b97a4a7732d8f99bf78dc1fc2a745429b7e1cd
---

## 简介

密码保险箱支持在应用和网页中保存和填充账号密码，为了提供更好的密码管理体验，提供了应用和网页共用账号数据的能力。

当接入本能力后，触发填充能力将优先推荐当前应用/网页的保存的账号，如当前应用/网页没有保存的账号时，则会推荐关联网页/应用的账号。

同时，选择密码时也会将关联网站/应用的密码展示为推荐密码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/oLcanldoRzaqoaNAu02LxQ/zh-cn_image_0000002558764872.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=80EAFDF7C7928CB14D3E49CB7FFA0EC593A8E20C8656BE5D6B4B261804E73734)

## 适用场景

当应用和网页均存在账号密码登录场景，且已经接入密码保险箱能力的情况下，期望其中一方保存密码之后，能够直接在另一方进行使用时，可以通过本能力进行实现。

## 接入方式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/LMbpOm5dQcqSoiBtTDSf0Q/zh-cn_image_0000002558605216.png?HW-CC-KV=V1&HW-CC-Date=20260429T053040Z&HW-CC-Expire=86400&HW-CC-Sign=37CD7DCF6FF298B17A070DE1CFC5514CE23F74EA7D3648E746BF94FB9712BB61)

应用及网页接入App Linking后绑定关联关系，密码保险箱将基于这个关系完成识别。

完成如下配置，即可实现共用密码的能力：

1. 应用和网页均已接入密码保险箱自动填充能力。

   接入参考：[应用接入密码保险箱](passwordvault-quick-adaptation.md)、[网页接入密码保险箱](arkweb-access-password-safe.md)
2. 应用和网页通过App Linking完成关联关系的绑定。

   接入需完成三步：[在AGC控制台开通App Linking服务](applinking-enable-applinking.md) > [建立域名与应用关联关系](app-linking-startupapp.md#建立域名与应用关联关系) > [在AGC为应用创建关联的网址域名](app-linking-startupapp.md#在agc为应用创建关联的网址域名)
