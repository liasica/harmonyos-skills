---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-1
title: 使用云存储上传文件失败，提示“404:Product does not exist”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 使用云存储上传文件失败，提示“404:Product does not exist”
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:16+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:a9ab9c3b590ea59fb1682c90025a373a6856c84981aeb172c340956b268edb9f
---

**问题现象**

使用云存储上传文件失败，HiLog提示“404:Product does not exist”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/07/v3/VzD0Fr-_Qpe268_u08EDCQ/zh-cn_image_0000002788467946.png?HW-CC-KV=V1&HW-CC-Date=20261114T004632Z&HW-CC-Expire=31536000000&HW-CC-Sign=6E12CE00BE039FA6797BDDE606BA06AA01F1925764721973A4BA7A8E9877E224)

**解决措施**

此错误由云存储服务端返回，原因是云存储服务未开通。请[开通云存储服务](cloudfoundation-enable-storage.md)。
