---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-cloudfoundation-6
title: 元服务使用云数据库是否需要获取用户凭据
breadcrumb: FAQ > 应用服务开发 > 云开发服务（Cloud Foundation Kit） > 元服务使用云数据库是否需要获取用户凭据
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:47+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:c3529b14bf01862e352cc93cc94cf627b053bbbb7a55b62eba8ab49dca820a6d
---

## 问题现象

在元服务开发中，需要使用到云数据库，实现用户写入数据，该功能是否需要获取用户凭据？

## 背景知识

[Cloud Foundation Kit（云开发服务）](../harmonyos-guides/cloud-foundation-kit-guide.md)可以按需为应用提供[云函数](../harmonyos-guides/cloudfoundation-function-service.md)、[云数据库](../harmonyos-guides/cloudfoundation-database-service.md)、[云存储](../harmonyos-guides/cloudfoundation-storage-service.md)、[预加载](../harmonyos-guides/cloudfoundation-prefetch-service.md)等云端服务。应用运行所需的服务器和环境可以皆由云端平台提供，开发者只需关注应用的业务逻辑，而无需关心基础设施（例如：服务器、操作系统、容器等）。

应用/元服务后端构建典型场景：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/gvJPQdGCQ1G_vjHO4r8xag/zh-cn_image_0000002658794005.png "点击放大")

## 解决方案

应用/元服务使用[云数据库服务](../harmonyos-guides/cloudfoundation-storage-config.md)，需要获取用户凭据。当前支持通过HarmonyOS 开发者中心认证服务SDK、或者华为账号服务Access Token接口两种方式获取，具体请参见[AuthProvider](../harmonyos-references/cloudfoundation-cloudcommon.md#authprovider)。

* 请检查失败的账号是否进行[认证服务](../app/agc-help-auth-0000002236336998.md)。
* 如果已完成认证，请检查是否在使用云存储服务上传文件前获取AuthProvider。

## 常见FAQ

Q：云数据库除了在端云一体化的应用中使用之外，能否在其他普通应用中使用？

A：云数据库非常适合端云一体化的应用，但是却不局限于此，所有通过认证的应用/元服务均可使用云数据库，认证及使用方式请参考上述方案内容。

Q：云存储计费说明中免费额度是基于每个账号还是每个项目进行统计的？

A：基于每个项目进行统计。

Q：如果存在多个HarmonyOS NEXT应用，是否需要为每个应用分别申请云数据库？

A：云数据库的开通与项目有关，如果希望多个应用共用一个云数据库，可以将这些应用添加到同一个项目。不同项目间需要分别申请云数据库。
