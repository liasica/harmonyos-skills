---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-1
title: 使用云存储上传文件失败，提示“404:Product does not exist”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 使用云存储上传文件失败，提示“404:Product does not exist”
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:22+08:00
doc_updated_at: 2026-03-19
content_hash: sha256:4a543bc517232d090accecd4715d4f469cd333f13362b35c1b800120433ad20b
---

**问题现象**

使用云存储上传文件失败，HiLog提示“404:Product does not exist”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/Abi1PAunTGykIWkGCMPFbg/zh-cn_image_0000002821757893.png?HW-CC-KV=V1&HW-CC-Date=20261121T011054Z&HW-CC-Expire=31536000000&HW-CC-Sign=039AD09DE1A7BDA56DC56122D7F7A9FDAA296ECA9090B0F1DC4E15F1D2D89B57)

**解决措施**

此错误由云存储服务端返回，原因是云存储服务未开通。请[开通云存储服务](cloudfoundation-enable-storage.md)。
