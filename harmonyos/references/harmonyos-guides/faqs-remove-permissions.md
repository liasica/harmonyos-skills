---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/faqs-remove-permissions
title: 移除已申请的权限
breadcrumb: 指南 > 系统 > 安全 > 程序访问控制 > 应用权限管控 > 程序访问控制常见问题 > 移除已申请的权限
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:27+08:00
doc_updated_at: 2026-06-05
content_hash: sha256:d44df96ff8f29dbbd48ef9e7166d888efdaefc8d89437d0ed26d91c6ae4dc7cd
---

因应用功能调整或有其他变动时，如需移除应用已获取的某个权限，可参照下述方式执行操作。

1. 在工程的module.json5中删除该权限的使用声明。
2. 重新打包应用。

构建出来的应用将不包含该权限。

**说明** 

对于受控开放权限、企业类应用可用权限、MDM应用可用权限这三类权限，应用重新打包后，Profile文件仍留存原有权限，不影响应用上架。平台审核将以module.json5中的权限设置为准。
