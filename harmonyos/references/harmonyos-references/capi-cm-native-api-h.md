---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-cm-native-api-h
title: cm_native_api.h
breadcrumb: API参考 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > C API > 头文件 > cm_native_api.h
category: harmonyos-references
scraped_at: 2026-04-28T08:07:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:f6926072f32d003a1eb7ba4ce2d3f1112d00cc35c7513fc72faf412e33f97e96
---

## 概述

PhonePC/2in1TabletTVWearable

声明用于获取特定类型证书详情的接口。

**引用文件：** <device\_certificate/certmanager/cm\_native\_api.h>

**库：** libohcert\_manager.so

**系统能力：** SystemCapability.Security.CertificateManager

**起始版本：** 22

**相关模块：** [CertManager](capi-certmanager.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [int32\_t OH\_CertManager\_GetUkeyCertificate(const OH\_CM\_Blob \*keyUri, const OH\_CM\_UkeyInfo \*ukeyInfo, OH\_CM\_CredentialDetailList \*certificateList)](capi-cm-native-api-h.md#oh_certmanager_getukeycertificate) | 获取USB证书凭据的详情信息列表。 |
| [int32\_t OH\_CertManager\_GetPrivateCertificate(const OH\_CM\_Blob \*keyUri, OH\_CM\_Credential \*certificate)](capi-cm-native-api-h.md#oh_certmanager_getprivatecertificate) | 获取特定应用私有证书凭据详细信息。 |
| [int32\_t OH\_CertManager\_GetPublicCertificate(const OH\_CM\_Blob \*keyUri, OH\_CM\_Credential \*certificate)](capi-cm-native-api-h.md#oh_certmanager_getpubliccertificate) | 获取特定用户公共证书凭据详细信息。 |
| [void OH\_CertManager\_FreeUkeyCertificate(OH\_CM\_CredentialDetailList \*certificateList)](capi-cm-native-api-h.md#oh_certmanager_freeukeycertificate) | 销毁证书详情信息列表。 |
| [void OH\_CertManager\_FreeCredential(OH\_CM\_Credential \*certificate)](capi-cm-native-api-h.md#oh_certmanager_freecredential) | 销毁证书详情。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_CertManager\_GetUkeyCertificate()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_CertManager_GetUkeyCertificate(const OH_CM_Blob *keyUri, const OH_CM_UkeyInfo *ukeyInfo, OH_CM_CredentialDetailList *certificateList)
```

**描述**

获取USB证书凭据的详情信息列表。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_CM\_Blob](capi-certmanagertype-oh-cm-blob.md) \*keyUri | 存放USB证书凭据的唯一标识符（字符串格式）。 |
| [const OH\_CM\_UkeyInfo](capi-certmanagertype-oh-cm-ukeyinfo.md) \*ukeyInfo | USB证书凭据属性信息。 |
| [OH\_CM\_CredentialDetailList](capi-certmanagertype-oh-cm-credentialdetaillist.md) \*certificateList | 获取到的USB证书凭据详情列表。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_CM\_ErrorCode](capi-cm-native-type-h.md#oh_cm_errorcode)：  OH\_CM\_SUCCESS = 0 ：操作成功。  OH\_CM\_HAS\_NO\_PERMISSION = 201 ：权限校验失败。  OH\_CM\_CAPABILITY\_NOT\_SUPPORTED = 801 ：设备不支持。  OH\_CM\_PARAMETER\_VALIDATION\_FAILED = 17500011 ：入参校验失败。可能原因：  1.参数格式错误。  2.参数范围无效。  OH\_CM\_INNER\_FAILURE = 17500001 ：内部错误。可能原因：  1.IPC通讯失败。  2.内存操作错误。  3.文件操作错误。  OH\_CM\_NOT\_FOUND = 17500002 ：证书不存在。  OH\_CM\_ACCESS\_UKEY\_SERVICE\_FAILED = 17500010 ：USB证书凭据访问失败。 |

### OH\_CertManager\_GetPrivateCertificate()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_CertManager_GetPrivateCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)
```

**描述**

获取特定应用私有证书凭据详细信息。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_CM\_Blob](capi-certmanagertype-oh-cm-blob.md) \*keyUri | 存放应用私有证书凭据的唯一标识符（字符串格式）。 |
| [OH\_CM\_Credential](capi-certmanagertype-oh-cm-credential.md) \*certificate | 获取到的应用私有凭据的详情。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_CM\_ErrorCode](capi-cm-native-type-h.md#oh_cm_errorcode)：  OH\_CM\_SUCCESS = 0 ：操作成功。  OH\_CM\_HAS\_NO\_PERMISSION = 201 ：权限校验失败。  OH\_CM\_PARAMETER\_VALIDATION\_FAILED = 17500011 ：入参校验失败。可能原因：  1.参数格式错误。  2.参数范围无效。  OH\_CM\_INNER\_FAILURE = 17500001 ：内部错误。可能原因：  1.IPC通讯失败。  2.内存操作错误。  3.文件操作错误。  OH\_CM\_NOT\_FOUND = 17500002 ：证书不存在。 |

### OH\_CertManager\_GetPublicCertificate()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_CertManager_GetPublicCertificate(const OH_CM_Blob *keyUri, OH_CM_Credential *certificate)
```

**描述**

获取特定用户公共证书凭据详细信息。

**需要权限：** ohos.permission.ACCESS\_CERT\_MANAGER

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const OH\_CM\_Blob](capi-certmanagertype-oh-cm-blob.md) \*keyUri | 存放用户公共证书凭据的唯一标识符（字符串格式）。 |
| [OH\_CM\_Credential](capi-certmanagertype-oh-cm-credential.md) \*certificate | 获取到的用户公共证书凭据的详情。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | [OH\_CM\_ErrorCode](capi-cm-native-type-h.md#oh_cm_errorcode)：  OH\_CM\_SUCCESS = 0 ：操作成功。  OH\_CM\_HAS\_NO\_PERMISSION = 201 ：权限校验失败。  OH\_CM\_PARAMETER\_VALIDATION\_FAILED = 17500011 ：入参校验失败。可能原因：  1.参数格式错误。  2.参数范围无效。  OH\_CM\_INNER\_FAILURE = 17500001 ：内部错误。可能原因：  1.IPC通讯失败。  2.内存操作错误。  3.文件操作错误。  OH\_CM\_NOT\_FOUND = 17500002 ：证书不存在。  OH\_CM\_NO\_AUTHORIZATION = 17500005 ：应用未经用户授权。 |

### OH\_CertManager\_FreeUkeyCertificate()

PhonePC/2in1TabletTVWearable

```
1. void OH_CertManager_FreeUkeyCertificate(OH_CM_CredentialDetailList *certificateList)
```

**描述**

销毁证书详情信息列表。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CM\_CredentialDetailList](capi-certmanagertype-oh-cm-credentialdetaillist.md) \*certificateList | 待销毁的证书凭据详细列表。 |

### OH\_CertManager\_FreeCredential()

PhonePC/2in1TabletTVWearable

```
1. void OH_CertManager_FreeCredential(OH_CM_Credential *certificate)
```

**描述**

销毁证书详情。

**起始版本：** 22

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [OH\_CM\_Credential](capi-certmanagertype-oh-cm-credential.md) \*certificate | 待销毁的证书凭据详情。 |
