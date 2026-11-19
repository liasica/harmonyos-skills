---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/password-shared-apps-web-pages
title: 应用与网页共用账号密码
breadcrumb: 指南 > 系统 > 安全 > 密码自动填充服务 > 应用与网页共用账号密码
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:01+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:19323c0c932a40060ccff74862b339b75b58f8a8ef1b447621ec97f2bf108ee8
---

## 简介

密码保险箱支持在应用和网页中保存和填充账号密码，为了提供更好的密码管理体验，提供了应用和网页共用账号数据的能力。

当接入本能力后，触发填充能力将优先推荐当前应用/网页的保存的账号，如当前应用/网页没有保存的账号时，则会推荐关联网页/应用的账号。

同时，选择密码时也会将关联网站/应用的密码展示为推荐密码。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/2JIPZ5dvSAqd8NvVDdzPvg/zh-cn_image_0000002820525657.png?HW-CC-KV=V1&HW-CC-Date=20261119T014800Z&HW-CC-Expire=31536000000&HW-CC-Sign=C32722B16D108745B29E2BAAB92CE41420FFE36AA47E75C181DC2481D19F77A1)

## 适用场景

当应用和网页均存在账号密码登录场景，且已经接入密码保险箱能力的情况下，期望其中一方保存密码之后，能够直接在另一方进行使用时，可以通过本能力进行实现。

## 接入方式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/bHrYPomeSjSBNpQ3oU9AKA/zh-cn_image_0000002820405657.png?HW-CC-KV=V1&HW-CC-Date=20261119T014800Z&HW-CC-Expire=31536000000&HW-CC-Sign=4839D8406A648CD431FC9A34946DD0AD3A21CFA2102A925238F1CF3613283FF9)

应用及网页接入App Linking后绑定关联关系，密码保险箱将基于这个关系完成识别。

完成如下配置，即可实现共用密码的能力：

1. 应用和网页均已接入密码保险箱自动填充能力。

   接入参考：[应用接入密码保险箱](passwordvault-quick-adaptation.md)、[网页接入密码保险箱](arkweb-access-password-safe.md)
2. 应用和网页通过App Linking完成关联关系的绑定。

   接入需完成三步：[开通App Linking服务](applinking-enable-applinking.md) > [建立域名与应用关联关系](app-linking-startupapp.md#建立域名与应用关联关系) > [在HarmonyOS 开发者中心为应用创建关联的网址域名](app-linking-startupapp.md#在harmonyos-开发者中心为应用创建关联的网址域名)
