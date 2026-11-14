---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-2
title: 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
category: harmonyos-guides
scraped_at: 2026-11-14T08:48:16+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:52c67d2a37b6194ba4cd90727f410fe02a0034293e907785326ca58d3d3fe06e
---

**问题现象**

使用云存储上传文件失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/SJCvfu_4SUSaA0FCB7iJXQ/zh-cn_image_0000002817507435.png?HW-CC-KV=V1&HW-CC-Date=20261114T004632Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF45D5F9172D2F5DE8B8C76981884DCC6F5526BB1F708D240A475DB2DC760D17)
* upload进程的日志提示“403 Forbidden”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/SL4chfl-RV6qyOF_2_noMg/zh-cn_image_0000002788308004.png?HW-CC-KV=V1&HW-CC-Date=20261114T004632Z&HW-CC-Expire=31536000000&HW-CC-Sign=2A215B9E128B82FCEEF65EE94CB51FE3618EE01FB8916889A84DAF22B31A7F5A)

**解决措施**

出现此问题，可按照如下步骤排查和解决：

1. 请确认应用的签名方式正确。当前Cloud Foundation Kit支持[关联注册应用进行自动签名](ide-signing-auto.md#section6333421192714)和[手动签名](ide-signing-manual.md)两种方式。
2. 请确认已通过[AuthProvider](../harmonyos-references/cloudfoundation-cloudcommon.md#authprovider)获取用户凭据。未配置用户凭据的情况下，服务端会返回“403 Forbidden”错误。
