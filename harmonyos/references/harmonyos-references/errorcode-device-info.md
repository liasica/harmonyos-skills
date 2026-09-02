---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/errorcode-device-info
title: deviceInfo错误码
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > 错误码 > deviceInfo错误码
category: harmonyos-references
scraped_at: 2026-09-02T15:02:06+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:39120fb100dcac4744e2ba5b19c1a1338b0538030341bd11fb2f51e583371ba2
---

**说明** 

以下仅介绍本模块特有错误码，通用错误码请参考[通用错误码说明文档](errorcode-universal.md)。

## 14700103 操作因权限被拒绝

**错误信息**

The operation on the system permission is denied.

**错误描述**

应用没有对应字段的权限时，系统会报此错误码。比如ohos.permission.sec.ACCESS\_UDID权限。

**可能原因**

应用没有配置需要的权限，比如ohos.permission.sec.ACCESS\_UDID。

**处理步骤**

在配置文件中添加相应的权限，例如：{"name": "ohos.permission.sec.ACCESS\_UDID"}。不同字段可能需要不同权限，请参考[@ohos.deviceInfo (设备信息)](js-apis-device-info.md)。
