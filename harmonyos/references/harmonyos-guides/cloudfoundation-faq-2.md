---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-2
title: 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ec47d65d66d42f0790691b647d48d6a3ccbef80c99c00fbdbec991323244ef24
---

**问题现象**

使用云存储上传文件失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/e-HpEm-DSKiuz4VpOxM0OQ/zh-cn_image_0000002742124047.png)
* upload进程的日志提示“403 Forbidden”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/q5G8w9fhQOKGo7KHGn5CVA/zh-cn_image_0000002712245140.png)

**解决措施**

出现此问题，可按照如下步骤排查和解决：

1. 请确认应用的签名方式正确。当前Cloud Foundation Kit支持[关联注册应用进行自动签名](ide-signing-auto.md#section6333421192714)和[手动签名](ide-signing-manual.md)两种方式。
2. 请确认已通过[AuthProvider](../harmonyos-references/cloudfoundation-cloudcommon.md#authprovider)获取用户凭据。未配置用户凭据的情况下，服务端会返回“403 Forbidden”错误。
