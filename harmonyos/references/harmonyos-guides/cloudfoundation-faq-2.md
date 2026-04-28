---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-2
title: 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:30ec939a8baa476a19ca02a8ee20e90262ab3ca64d4b969974e349e180509463
---

**问题现象**

使用云存储上传文件失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/jWQ3cbydSSmlRQXlvsttRg/zh-cn_image_0000002552958878.png?HW-CC-KV=V1&HW-CC-Date=20260427T234848Z&HW-CC-Expire=86400&HW-CC-Sign=B4987A22E69E877F8ADCB506F095BA0EF7886018009E505C4CB41E846D2473F2)
* upload进程的日志提示“403 Forbidden”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/F3HNfsylQHSthqm_UmTK7g/zh-cn_image_0000002583478879.png?HW-CC-KV=V1&HW-CC-Date=20260427T234848Z&HW-CC-Expire=86400&HW-CC-Sign=2D48CBDAB061BD249D16159182793A117E1FE07CB67B6D159296172B841C084E)

**解决措施**

出现此问题，可按照如下步骤排查和解决：

1. 请确认应用的签名方式正确。当前Cloud Foundation Kit支持[关联注册应用进行自动签名](ide-signing.md#section20943184413328)和[手动签名](ide-signing.md#section297715173233)两种方式。
2. 请确认已通过[AuthProvider](../harmonyos-references/cloudfoundation-cloudcommon.md#authprovider)获取用户凭据。未配置用户凭据的情况下，服务端会返回“403 Forbidden”错误。
