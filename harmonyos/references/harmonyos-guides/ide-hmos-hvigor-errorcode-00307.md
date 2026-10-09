---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-errorcode-00307
title: 权限错误码
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 构建报错排查 > 编译构建错误码 > 权限错误码
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:36+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:10bb2ad79c7cd0d4795b7ac1f695558c4f5a16191e1ce8e11fde49d5e61a1bba
---

## 00307001 创建或写文件失败

**错误信息**

EPERM: operation not permitted,create XXX failed.

**错误描述**

创建或写文件XXX失败。

**可能原因**

缺少创建或写文件的权限。

**处理步骤**

确保用户具有创建文件、写文件的权限。

## 00307003 HSP依赖包的bundleType不正确

**错误信息**

The currentBundleType is shared, but the Package XXX bundleType is not shared.

**错误描述**

当前的bundleType为shared，但是包XXX的bundleType不是shared。

**可能原因**

当前工程app.json5中的bundleType设置为shared，但是依赖包的bundleType不是shared。

**处理步骤**

移除依赖包XXX。
