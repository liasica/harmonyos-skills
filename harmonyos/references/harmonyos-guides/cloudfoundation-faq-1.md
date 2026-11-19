---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-1
title: 使用云存储上传文件失败，提示“404:Product does not exist”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 使用云存储上传文件失败，提示“404:Product does not exist”
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:56+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:9d31b23fbc9cb31444d00f4d88014c1fa6965af633c979aaf1f092b8dd755dfb
---

**问题现象**

使用云存储上传文件失败，HiLog提示“404:Product does not exist”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/2ODIx4TVQHqQ8doScu-Z6A/zh-cn_image_0000002791566332.png?HW-CC-KV=V1&HW-CC-Date=20261119T014856Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF4BE760D8DD832536C8360D66DA6B9DA00BDF40F7A44AC2B1D21125F46FAB2E)

**解决措施**

此错误由云存储服务端返回，原因是云存储服务未开通。请[开通云存储服务](cloudfoundation-enable-storage.md)。
