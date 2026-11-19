---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-2
title: 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
category: harmonyos-guides
scraped_at: 2026-11-19T09:48:56+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:e69b9000fafd972882041568de878fad5087f27c2339a2283f4323c4e9df4f2d
---

**问题现象**

使用云存储上传文件失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/2OIyLqzOSB2Ffp13hG0e2w/zh-cn_image_0000002820526285.png?HW-CC-KV=V1&HW-CC-Date=20261119T014802Z&HW-CC-Expire=31536000000&HW-CC-Sign=B63F8630E45A93AFFC4F76FB80435FBAF2279C6A5518649D5277859B056FF2C7)
* upload进程的日志提示“403 Forbidden”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/bgT8bNE-SKi5Kk8RAU4xEw/zh-cn_image_0000002820406285.png?HW-CC-KV=V1&HW-CC-Date=20261119T014802Z&HW-CC-Expire=31536000000&HW-CC-Sign=30F5224B2991A061CD9DAA5D26425D10D2F2DB4435D42B596628B720F852A250)

**解决措施**

出现此问题，可按照如下步骤排查和解决：

1. 请确认应用的签名方式正确。当前Cloud Foundation Kit支持[关联注册应用进行自动签名](ide-signing-auto.md#section6333421192714)和[手动签名](ide-signing-manual.md)两种方式。
2. 请确认已通过[AuthProvider](../harmonyos-references/cloudfoundation-cloudcommon.md#authprovider)获取用户凭据。未配置用户凭据的情况下，服务端会返回“403 Forbidden”错误。
