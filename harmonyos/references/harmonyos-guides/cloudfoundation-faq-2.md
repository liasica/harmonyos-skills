---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-faq-2
title: 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > Cloud Foundation Kit常见问题 > 云存储 > 使用云存储上传文件失败，app日志提示“"state":65”，upload进程日志提示“403 Forbidden”
category: harmonyos-guides
scraped_at: 2026-11-21T09:12:22+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:e108b0497365cec48411e5b076dfe5ef1b7ade29b54d54409310fc111e996ce5
---

**问题现象**

使用云存储上传文件失败，出现如下错误提示：

* app日志提示“"state":65”

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/Lz-VJXulRCWUH9muuNNc_Q/zh-cn_image_0000002793037956.png?HW-CC-KV=V1&HW-CC-Date=20261121T011222Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C2EFE914FAEB1D080295821F0E1E9D5036C3F64B4EB3491336BBBE12D4B973C)
* upload进程的日志提示“403 Forbidden”（通过设置“No filters”模式、过滤“C01C50”关键字查找）

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/4im7sm7tSvCKr8UVmVyCJg/zh-cn_image_0000002792877986.png?HW-CC-KV=V1&HW-CC-Date=20261121T011222Z&HW-CC-Expire=31536000000&HW-CC-Sign=363FA84726E1165074651A710038A4492675C62CF6408735395442B75354FF6D)

**解决措施**

出现此问题，可按照如下步骤排查和解决：

1. 请确认应用的签名方式正确。当前Cloud Foundation Kit支持[关联注册应用进行自动签名](ide-signing-auto.md#section6333421192714)和[手动签名](ide-signing-manual.md)两种方式。
2. 请确认已通过[AuthProvider](../harmonyos-references/cloudfoundation-cloudcommon.md#authprovider)获取用户凭据。未配置用户凭据的情况下，服务端会返回“403 Forbidden”错误。
