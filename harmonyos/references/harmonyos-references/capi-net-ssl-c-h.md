---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-net-ssl-c-h
title: net_ssl_c.h
breadcrumb: API参考 > 系统 > 网络 > Network Kit（网络服务） > C API > 头文件 > net_ssl_c.h
category: harmonyos-references
scraped_at: 2026-04-28T08:08:31+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:eb87520f3df3ddf575f0aaf281dcf312cd44f6f1ff3524569e81e502e009b0c9
---

## 概述

PhonePC/2in1TabletTVWearable

定义SSL/TLS证书链校验模块C接口数据结构。

**引用文件：** <network/netstack/net\_ssl/net\_ssl\_c.h>

**库：** libnet\_ssl.so

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 11

**相关模块：** [netstack](capi-netstack.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [uint32\_t OH\_NetStack\_CertVerification(const struct NetStack\_CertBlob \*cert, const struct NetStack\_CertBlob \*caCert)](capi-net-ssl-c-h.md#oh_netstack_certverification) | 证书链校验接口。 |
| [int32\_t OH\_NetStack\_GetPinSetForHostName(const char \*hostname, NetStack\_CertificatePinning \*pin)](capi-net-ssl-c-h.md#oh_netstack_getpinsetforhostname) | 获取证书锁定信息。 |
| [int32\_t OH\_NetStack\_GetCertificatesForHostName(const char \*hostname, NetStack\_Certificates \*certs)](capi-net-ssl-c-h.md#oh_netstack_getcertificatesforhostname) | 获取证书信息。 |
| [void OH\_Netstack\_DestroyCertificatesContent(NetStack\_Certificates \*certs)](capi-net-ssl-c-h.md#oh_netstack_destroycertificatescontent) | 释放证书内容。 |
| [int32\_t OH\_Netstack\_IsCleartextPermitted(bool \*isCleartextPermitted)](capi-net-ssl-c-h.md#oh_netstack_iscleartextpermitted) | 整体明文HTTP是否允许。 |
| [int32\_t OH\_Netstack\_IsCleartextPermittedByHostName(const char \*hostname, bool \*isCleartextPermitted)](capi-net-ssl-c-h.md#oh_netstack_iscleartextpermittedbyhostname) | 按域名明文HTTP是否允许。 |
| [int32\_t OH\_Netstack\_IsCleartextCfgByComponent(const char \*component, bool \*componentCfg)](capi-net-ssl-c-h.md#oh_netstack_iscleartextcfgbycomponent) | 检查组件是否已配置开启明文HTTP拦截功能。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_NetStack\_CertVerification()

PhonePC/2in1TabletTVWearable

```
1. uint32_t OH_NetStack_CertVerification(const struct NetStack_CertBlob *cert, const struct NetStack_CertBlob *caCert)
```

**描述**

对外暴露的证书链校验接口。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 11

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [const struct NetStack\_CertBlob](capi-netstack-netstack-certblob.md) \*cert | 用户传入的待校验证书。 |
| [const struct NetStack\_CertBlob](capi-netstack-netstack-certblob.md) \*caCert | 用户指定的证书，若为空则以系统预置证书进行校验。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| uint32\_t | 0 - 成功。  2305001 - 未指定的错误。  2305002 - 无法获取颁发者证书。  2305003 - 无法获取证书吊销列表（CRL）。  2305004 - 无法解密证书签名。  2305005 - 无法解密CRL签名。  2305006 - 无法解码颁发者公钥。  2305007 - 证书签名失败。  2305008 - CRL签名失败。  2305009 - 证书尚未生效。  2305010 - 证书已过期。  2305011 - CRL尚未有效。  2305012 - CRL已过期。  2305023 - 证书已被吊销。  2305024 - 证书颁发机构（CA）无效。  2305027 - 证书不受信任。 |

### OH\_NetStack\_GetPinSetForHostName()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetStack_GetPinSetForHostName(const char *hostname, NetStack_CertificatePinning *pin)
```

**描述**

获取证书锁定信息。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*hostname | 主机名。 |
| [NetStack\_CertificatePinning](capi-netstack-netstack-certificatepinning.md) \*pin | 证书锁定信息的结构体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  401 - 参数设置错误。  2305999 - 内存错误。 |

### OH\_NetStack\_GetCertificatesForHostName()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_NetStack_GetCertificatesForHostName(const char *hostname, NetStack_Certificates *certs)
```

**描述**

获取证书信息。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*hostname | 主机名。 |
| [NetStack\_Certificates](capi-netstack-netstack-certificates.md) \*certs | 证书信息的结构体。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  401 - 参数设置错误。  2305999 - 内存错误。 |

### OH\_Netstack\_DestroyCertificatesContent()

PhonePC/2in1TabletTVWearable

```
1. void OH_Netstack_DestroyCertificatesContent(NetStack_Certificates *certs)
```

**描述**

释放证书内容。

**系统能力：** SystemCapability.Communication.NetStack

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [NetStack\_Certificates](capi-netstack-netstack-certificates.md) \*certs | 证书信息。 |

### OH\_Netstack\_IsCleartextPermitted()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Netstack_IsCleartextPermitted(bool *isCleartextPermitted)
```

**描述**

整体明文HTTP是否允许。

**需要权限：** ohos.permission.INTERNET

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool \*isCleartextPermitted | 输出参数，如果允许明文流量，则true，否则false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  201 - 权限被拒。  401 - 参数错误。 |

### OH\_Netstack\_IsCleartextPermittedByHostName()

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Netstack_IsCleartextPermittedByHostName(const char *hostname, bool *isCleartextPermitted)
```

**描述**

按域名明文HTTP是否允许。

**需要权限：** ohos.permission.INTERNET

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*hostname | 主机名。 |
| bool \*isCleartextPermitted | 输出参数，如果允许指定主机名的明文流量，则true，否则false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  201 - 权限被拒。  401 - 参数错误。 |

### OH\_Netstack\_IsCleartextCfgByComponent

PhonePC/2in1TabletTVWearable

```
1. int32_t OH_Netstack_IsCleartextCfgByComponent(const char *component, bool *componentCfg);
```

**描述**

检查组件是否已配置开启明文HTTP拦截功能。

**起始版本：** 20

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char \*component | 组件名称，当前支持的组件：Network Kit、ArkWeb。 |
| bool \*componentCfg | 输出参数，组件是否配置开启明文HTTP拦截功能，如果开启则为true，否则为false。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 0 - 成功。  2100001 - 无效的参数值。 |
