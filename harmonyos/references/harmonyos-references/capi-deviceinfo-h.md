---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-deviceinfo-h
title: deviceinfo.h
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 头文件 > deviceinfo.h
category: harmonyos-references
scraped_at: 2026-04-28T08:09:47+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:757e854d31e19e6a48619600a0031d923e3e37614bcfaf31212359a9f629fa06
---

## 概述

PhonePC/2in1TabletTVWearable

声明用于查询终端设备信息的API。

**引用文件：** <deviceinfo.h>

**库：** libdeviceinfo\_ndk.z.so

**系统能力：** SystemCapability.Startup.SystemInfo

**起始版本：** 10

**相关模块：** [DeviceInfo](capi-deviceinfo.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [const char \*OH\_GetDeviceType(void)](capi-deviceinfo-h.md#oh_getdevicetype) | 获取设备类型。 |
| [const char \*OH\_GetManufacture(void)](capi-deviceinfo-h.md#oh_getmanufacture) | 获取设备制造商。 |
| [const char \*OH\_GetBrand(void)](capi-deviceinfo-h.md#oh_getbrand) | 获取设备品牌。 |
| [const char \*OH\_GetMarketName(void)](capi-deviceinfo-h.md#oh_getmarketname) | 获取外部产品系列。 |
| [const char \*OH\_GetProductSeries(void)](capi-deviceinfo-h.md#oh_getproductseries) | 获取产品系列。 |
| [const char \*OH\_GetProductModel(void)](capi-deviceinfo-h.md#oh_getproductmodel) | 获取认证型号。 |
| [const char \*OH\_GetSoftwareModel(void)](capi-deviceinfo-h.md#oh_getsoftwaremodel) | 获取内部软件子型号。 |
| [const char \*OH\_GetHardwareModel(void)](capi-deviceinfo-h.md#oh_gethardwaremodel) | 获取硬件版本号。 |
| [const char \*OH\_GetBootloaderVersion(void)](capi-deviceinfo-h.md#oh_getbootloaderversion) | 获取Bootloader版本号。 |
| [const char \*OH\_GetAbiList(void)](capi-deviceinfo-h.md#oh_getabilist) | 获取应用二进制接口（Abi）。 |
| [const char \*OH\_GetSecurityPatchTag(void)](capi-deviceinfo-h.md#oh_getsecuritypatchtag) | 获取安全补丁级别。 |
| [const char \*OH\_GetDisplayVersion(void)](capi-deviceinfo-h.md#oh_getdisplayversion) | 获取产品版本。 |
| [const char \*OH\_GetIncrementalVersion(void)](capi-deviceinfo-h.md#oh_getincrementalversion) | 获取差异版本。 |
| [const char \*OH\_GetOsReleaseType(void)](capi-deviceinfo-h.md#oh_getosreleasetype) | 获取系统的发布类型。 |
| [const char \*OH\_GetOSFullName(void)](capi-deviceinfo-h.md#oh_getosfullname) | 获取完整的系统版本名。 |
| [int OH\_GetSdkApiVersion(void)](capi-deviceinfo-h.md#oh_getsdkapiversion) | 获取系统软件API版本。 |
| [int OH\_GetFirstApiVersion(void)](capi-deviceinfo-h.md#oh_getfirstapiversion) | 获取首个版本系统软件API版本。 |
| [const char \*OH\_GetVersionId(void)](capi-deviceinfo-h.md#oh_getversionid) | 获取版本ID。 |
| [const char \*OH\_GetBuildType(void)](capi-deviceinfo-h.md#oh_getbuildtype) | 获取系统的构建类型。 |
| [const char \*OH\_GetBuildUser(void)](capi-deviceinfo-h.md#oh_getbuilduser) | 获取系统的构建用户。 |
| [const char \*OH\_GetBuildHost(void)](capi-deviceinfo-h.md#oh_getbuildhost) | 获取系统的构建主机。 |
| [const char \*OH\_GetBuildTime(void)](capi-deviceinfo-h.md#oh_getbuildtime) | 获取系统的构建时间。 |
| [const char \*OH\_GetBuildRootHash(void)](capi-deviceinfo-h.md#oh_getbuildroothash) | 获取系统的构建版本Hash。 |
| [const char \*OH\_GetDistributionOSName(void)](capi-deviceinfo-h.md#oh_getdistributionosname) | 获取ISV发行系统版本名称。独立软件供应商（ISV）可以使用自己定义的系统名称。 |
| [const char \*OH\_GetDistributionOSVersion(void)](capi-deviceinfo-h.md#oh_getdistributionosversion) | 获取ISV发行版系统版本号。 |
| [int OH\_GetDistributionOSApiVersion(void)](capi-deviceinfo-h.md#oh_getdistributionosapiversion) | 获取ISV发行版系统api版本。 |
| [const char \*OH\_GetDistributionOSReleaseType(void)](capi-deviceinfo-h.md#oh_getdistributionosreleasetype) | 获取ISV发行版系统类型。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_GetDeviceType()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetDeviceType(void)
```

**描述**

获取设备类型。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char | "phone"(或"default")  "wearable",  "liteWearable",  "tablet",  "tv",  "car",  "smartVision"。 |

### OH\_GetManufacture()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetManufacture(void)
```

**描述**

获取设备制造商。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的设备制造商。 |

### OH\_GetBrand()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetBrand(void)
```

**描述**

获取设备品牌。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的设备品牌。 |

### OH\_GetMarketName()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetMarketName(void)
```

**描述**

获取外部产品系列。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的外部产品系列。 |

### OH\_GetProductSeries()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetProductSeries(void)
```

**描述**

获取产品系列。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的产品系列。 |

### OH\_GetProductModel()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetProductModel(void)
```

**描述**

获取认证型号。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的认证型号。 |

### OH\_GetSoftwareModel()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetSoftwareModel(void)
```

**描述**

获取内部软件子型号。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的内部软件子型号。 |

### OH\_GetHardwareModel()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetHardwareModel(void)
```

**描述**

获取硬件版本号。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的硬件版本号。 |

### OH\_GetBootloaderVersion()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetBootloaderVersion(void)
```

**描述**

获取Bootloader版本号。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的Bootloader版本号。 |

### OH\_GetAbiList()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetAbiList(void)
```

**描述**

获取应用二进制接口（Abi）。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的应用二进制接口（Abi）。 |

### OH\_GetSecurityPatchTag()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetSecurityPatchTag(void)
```

**描述**

获取安全补丁级别。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的安全补丁级别。 |

### OH\_GetDisplayVersion()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetDisplayVersion(void)
```

**描述**

获取产品版本。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的产品版本。 |

### OH\_GetIncrementalVersion()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetIncrementalVersion(void)
```

**描述**

获取差异版本。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的获取差异版本。 |

### OH\_GetOsReleaseType()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetOsReleaseType(void)
```

**描述**

获取系统的发布类型。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 操作系统发布类别包括"release"、"Beta"和"Canary"。  具体的发布类型可能是"release"，"Beta1"，或其他类似的。 |

### OH\_GetOSFullName()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetOSFullName(void)
```

**描述**

获取完整的系统版本名。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的完整的系统版本名。 |

### OH\_GetSdkApiVersion()

PhonePC/2in1TabletTVWearable

```
1. int OH_GetSdkApiVersion(void)
```

**描述**

获取系统软件API版本。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 系统软件API版本。 |

### OH\_GetFirstApiVersion()

PhonePC/2in1TabletTVWearable

```
1. int OH_GetFirstApiVersion(void)
```

**描述**

获取首个版本系统软件API版本。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 首个版本系统软件API版本。 |

### OH\_GetVersionId()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetVersionId(void)
```

**描述**

获取版本ID。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的版本ID。 |

### OH\_GetBuildType()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetBuildType(void)
```

**描述**

获取系统的构建类型。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的系统的构建类型。 |

### OH\_GetBuildUser()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetBuildUser(void)
```

**描述**

获取系统的构建用户。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的系统的构建用户。 |

### OH\_GetBuildHost()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetBuildHost(void)
```

**描述**

获取系统的构建主机。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的系统的构建主机。 |

### OH\_GetBuildTime()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetBuildTime(void)
```

**描述**

获取系统的构建时间。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的系统的构建时间。 |

### OH\_GetBuildRootHash()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetBuildRootHash(void)
```

**描述**

获取系统的构建版本Hash。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 字符串类型的系统的构建版本Hash。 |

### OH\_GetDistributionOSName()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetDistributionOSName(void)
```

**描述**

获取ISV发行系统版本名称。独立软件供应商（ISV）可以使用自己定义的系统名称。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | ISV发行系统版本名称。  如果没有指定ISV，它将返回一个空字符串。 |

### OH\_GetDistributionOSVersion()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetDistributionOSVersion(void)
```

**描述**

获取ISV发行版系统版本号。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | ISV发行版系统版本号。  如果没有指定ISV，它将返回与[OH\_GetOSFullName](capi-deviceinfo-h.md#oh_getosfullname)相同的值。 |

### OH\_GetDistributionOSApiVersion()

PhonePC/2in1TabletTVWearable

```
1. int OH_GetDistributionOSApiVersion(void)
```

**描述**

获取ISV发行版系统api版本。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | ISV发行版系统api版本。  如果没有指定ISV，它将返回与[OH\_GetOSFullName](capi-deviceinfo-h.md#oh_getosfullname)相同的值。 |

### OH\_GetDistributionOSReleaseType()

PhonePC/2in1TabletTVWearable

```
1. const char *OH_GetDistributionOSReleaseType(void)
```

**描述**

获取ISV发行版系统类型。

**起始版本：** 10

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char | ISV发行版系统类型。  如果没有指定ISV，它将返回与[OH\_GetOsReleaseType](capi-deviceinfo-h.md#oh_getosreleasetype)相同的值。 |
