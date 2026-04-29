---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-2
title: 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
category: harmonyos-guides
scraped_at: 2026-04-29T13:37:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:127c731a53235c8c86233a8b3a5807195d3c9f54421e5c9d1310a2e8ea4e9451
---

**问题现象**

使用云存储上传文件失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/qbXAoiaVTCWe8Gue4Avhjw/zh-cn_image_0000002558765378.png?HW-CC-KV=V1&HW-CC-Date=20260429T053754Z&HW-CC-Expire=86400&HW-CC-Sign=1AF49ECB77E69DC4656EB08E012B3289A1F9CFB8B0E1416BE4D26B52FDA7112C)
* upload进程的日志提示“403 Forbidden”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/TS4AAPugTe-nkiJJosRPFw/zh-cn_image_0000002558605722.png?HW-CC-KV=V1&HW-CC-Date=20260429T053754Z&HW-CC-Expire=86400&HW-CC-Sign=E702F2A1A0BB6C115737859394EFFFF4111B9DB28306EBCE8B8AA95660C27E21)

**解决措施**

出现此问题，可按照如下步骤排查和解决：

1. 请确认应用的签名方式正确。当前Cloud Foundation Kit支持[关联注册应用进行自动签名](ide-signing.md#section20943184413328)和[手动签名](ide-signing.md#section297715173233)两种方式。
2. 请确认已通过[AuthProvider](../harmonyos-references/cloudfoundation-cloudcommon.md#authprovider)获取用户凭据。未配置用户凭据的情况下，服务端会返回“403 Forbidden”错误。
