---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-certmanagertype-oh-cm-credential
title: OH_CM_Credential
breadcrumb: API参考 > 系统 > 安全 > Device Certificate Kit（设备证书服务） > C API > 结构体 > OH_CM_Credential
category: harmonyos-references
scraped_at: 2026-04-28T08:07:41+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9a0d3994488e39aa510e95daa70d7625f03a4c438b519dd87f6afc801e4ca4eb
---

```
1. typedef struct {...} OH_CM_Credential
```

## 概述

PhonePC/2in1TabletTVWearable

定义证书凭据详情的结构体类型。

**起始版本：** 22

**相关模块：** [CertManagerType](capi-certmanagertype.md)

**所在头文件：** [cm\_native\_type.h](capi-cm-native-type-h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| uint32\_t isExist | 表示证书数据是否存在。 |
| char type[OH\_CM\_MAX\_LEN\_TYPE\_NAME] | 表示凭据的类型，最大长度为8字节，数据包含终止符'\0'字符。 |
| char alias[OH\_CM\_MAX\_LEN\_CERT\_ALIAS] | 表示凭据的别名，最大长度为128字节，数据包含终止符'\0'字符。 |
| char keyUri[OH\_CM\_MAX\_LEN\_URI] | 表示凭据的唯一标识，最大长度为256字节，数据包含终止符'\0'字符。 |
| uint32\_t certNum | 表示凭据中包含的证书个数。 |
| uint32\_t keyNum | 表示凭据中包含的秘钥个数。 |
| [OH\_CM\_Blob](capi-certmanagertype-oh-cm-blob.md) credData | 表示凭据二进制数据，最大长度为20480字节。 |
| [OH\_CM\_CertificatePurpose](capi-cm-native-type-h.md#oh_cm_certificatepurpose) certPurpose | 表示证书凭据的用途。 |
