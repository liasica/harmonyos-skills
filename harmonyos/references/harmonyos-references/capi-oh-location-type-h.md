---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-location-type-h
title: oh_location_type.h
breadcrumb: API参考 > 应用服务 > Location Kit（位置服务） > C API > 头文件 > oh_location_type.h
category: harmonyos-references
scraped_at: 2026-04-28T08:17:07+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8b626fcb8c51225687f532a2d7fc7f1a6b7eaa3a157ed0197484d440b108dacd
---

## 概述

PhonePC/2in1TabletTVWearable

定义位置服务常用的属性。

**引用文件：** <LocationKit/oh\_location\_type.h>

**库：** liblocation\_ndk.so

**系统能力：** SystemCapability.Location.Location.Core

**起始版本：** 13

**相关模块：** [Location](capi-location.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 结构体

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Location\_BasicInfo](capi-location-location-basicinfo.md) | Location\_BasicInfo | 定义位置基本信息的结构体。 |
| [Location\_Info](capi-location-location-info.md) | Location\_Info | 定义位置信息的结构体。 |
| [Location\_RequestConfig](capi-location-location-requestconfig.md) | Location\_RequestConfig | 定义位置请求参数的结构体。 |

### 枚举

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Location\_ResultCode](capi-oh-location-type-h.md#location_resultcode) | Location\_ResultCode | 定义位置服务的错误码。 |
| [Location\_UseScene](capi-oh-location-type-h.md#location_usescene) | Location\_UseScene | 定义位置请求中的用户活动场景类型。 |
| [Location\_PowerConsumptionScene](capi-oh-location-type-h.md#location_powerconsumptionscene) | Location\_PowerConsumptionScene | 定义位置请求中的功耗场景类型。 |
| [Location\_SourceType](capi-oh-location-type-h.md#location_sourcetype) | Location\_SourceType | 定义位置信息的来源。 |

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [Location\_BasicInfo OH\_LocationInfo\_GetBasicInfo(Location\_Info\* location)](capi-oh-location-type-h.md#oh_locationinfo_getbasicinfo) | - | 获取位置基本信息。 |
| [Location\_ResultCode OH\_LocationInfo\_GetAdditionalInfo(Location\_Info\* location, char\* additionalInfo, uint32\_t length)](capi-oh-location-type-h.md#oh_locationinfo_getadditionalinfo) | - | 获取位置信息中的附加信息。 |
| [typedef void (\*Location\_InfoCallback)(Location\_Info\* location, void\* userData)](capi-oh-location-type-h.md#location_infocallback) | Location\_InfoCallback | 用于接收位置上报的回调函数。 |
| [Location\_RequestConfig\* OH\_Location\_CreateRequestConfig(void)](capi-oh-location-type-h.md#oh_location_createrequestconfig) | - | 创建一个位置请求参数结构体实例。 |
| [void OH\_Location\_DestroyRequestConfig(Location\_RequestConfig\* requestConfig)](capi-oh-location-type-h.md#oh_location_destroyrequestconfig) | - | 销毁位置请求参数实例并回收内存。 |
| [void OH\_LocationRequestConfig\_SetUseScene(Location\_RequestConfig\* requestConfig, Location\_UseScene useScene)](capi-oh-location-type-h.md#oh_locationrequestconfig_setusescene) | - | 设置位置请求参数中的用户活动场景。  位置请求参数[Location\_RequestConfig](capi-location-location-requestconfig.md)中以useScene优先。  如果设置了useScene，则powerConsumptionScene参数无效。  如果未设置useScene，设置了powerConsumptionScene则该参数生效。  如果两个参数都未设置，则默认useScene为[LOCATION\_USE\_SCENE\_DAILY\_LIFE\_SERVICE](capi-oh-location-type-h.md#location_usescene)，powerConsumptionScene参数无效。 |
| [void OH\_LocationRequestConfig\_SetPowerConsumptionScene(Location\_RequestConfig\* requestConfig, Location\_PowerConsumptionScene powerConsumptionScene)](capi-oh-location-type-h.md#oh_locationrequestconfig_setpowerconsumptionscene) | - | 设置位置请求参数中的功耗场景。 |
| [void OH\_LocationRequestConfig\_SetInterval(Location\_RequestConfig\* requestConfig, int interval)](capi-oh-location-type-h.md#oh_locationrequestconfig_setinterval) | - | 设置位置请求参数中的位置上报间隔。 |
| [void OH\_LocationRequestConfig\_SetCallback(Location\_RequestConfig\* requestConfig, Location\_InfoCallback callback, void\* userData)](capi-oh-location-type-h.md#oh_locationrequestconfig_setcallback) | - | 设置回调函数。 |

## 枚举类型说明

PhonePC/2in1TabletTVWearable

### Location\_ResultCode

PhonePC/2in1TabletTVWearable

```
1. enum Location_ResultCode
```

**描述**

定义位置服务的错误码。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| LOCATION\_SUCCESS = 0 | 操作成功。 |
| LOCATION\_PERMISSION\_DENIED = 201 | 权限校验失败。 |
| LOCATION\_INVALID\_PARAM = 401 | 参数错误。  可能原因：1.输入参数为空指针；2.参数数值超出定义范围。 |
| LOCATION\_NOT\_SUPPORTED = 801 | 该功能不支持。由于设备能力有限，无法调用该函数。 |
| LOCATION\_SERVICE\_UNAVAILABLE = 3301000 | 位置服务不可用。 |
| LOCATION\_SWITCH\_OFF = 3301100 | 位置开关处于关闭状态。 |

### Location\_UseScene

PhonePC/2in1TabletTVWearable

```
1. enum Location_UseScene
```

**描述**

定义位置请求中的用户活动场景类型。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| LOCATION\_USE\_SCENE\_NAVIGATION = 0x0401 | 导航场景。  适用于在户外获取设备实时位置的场景，如车载、步行导航。  主要使用GNSS定位技术提供定位服务，功耗较高。 |
| LOCATION\_USE\_SCENE\_SPORT = 0x0402 | 表示运动场景。  适用于记录用户位置轨迹的场景，如运动类应用记录轨迹功能。  主要使用GNSS定位技术提供定位服务，功耗较高。 |
| LOCATION\_USE\_SCENE\_TRANSPORT = 0x0403 | 表示出行场景。  适用于用户出行场景，如打车、乘坐公共交通等场景。  主要使用GNSS定位技术提供定位服务，功耗较高。 |
| LOCATION\_USE\_SCENE\_DAILY\_LIFE\_SERVICE = 0x0404 | 表示日常服务使用场景。  适用于不需要定位用户精确位置的使用场景，如新闻资讯、网购、点餐类应用。  该场景仅使用网络定位技术提供定位服务，功耗较低。 |

### Location\_PowerConsumptionScene

PhonePC/2in1TabletTVWearable

```
1. enum Location_PowerConsumptionScene
```

**描述**

定义位置请求中的功耗场景类型。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| LOCATION\_HIGH\_POWER\_CONSUMPTION = 0x0601 | 高功耗。  以GNSS定位技术为主。在GNSS提供稳定位置结果之前会使用网络定位技术提供服务。  在持续定位时，如果超过30秒无法获取GNSS定位结果则会使用网络定位技术获取位置。  对设备的硬件资源消耗较大，功耗较大。 |
| LOCATION\_LOW\_POWER\_CONSUMPTION = 0x0602 | 低功耗。  适用于对用户位置精度要求不高的使用场景，如新闻资讯、网购、点餐类应用。  该场景仅使用网络定位技术提供定位服务，功耗较低。 |
| LOCATION\_NO\_POWER\_CONSUMPTION = 0x0603 | 无功耗。  这种场景下不会主动触发定位，会在其他应用定位时，才给当前应用返回位置。 |

### Location\_SourceType

PhonePC/2in1TabletTVWearable

```
1. enum Location_SourceType
```

**描述**

定义位置信息的来源。

**起始版本：** 13

| 枚举项 | 描述 |
| --- | --- |
| LOCATION\_SOURCE\_TYPE\_GNSS = 1 | 表示定位结果来自于GNSS定位技术。 |
| LOCATION\_SOURCE\_TYPE\_NETWORK = 2 | 表示定位结果来自于网络定位技术。 |
| LOCATION\_SOURCE\_TYPE\_INDOOR = 3 | 表示定位结果来自于室内高精度定位技术。 |
| LOCATION\_SOURCE\_TYPE\_RTK = 4 | 表示定位结果来自于室外高精度定位技术。 |

## 函数说明

PhonePC/2in1TabletTVWearable

### OH\_LocationInfo\_GetBasicInfo()

PhonePC/2in1TabletTVWearable

```
1. Location_BasicInfo OH_LocationInfo_GetBasicInfo(Location_Info* location)
```

**描述**

获取位置基本信息。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Location\_Info](capi-location-location-info.md)\* location | 指向位置信息结构体的指针。  需要传入非空指针，该指针可以在[Location\_InfoCallback](capi-oh-location-type-h.md#location_infocallback)中获取。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Location\_BasicInfo](capi-location-location-basicinfo.md) | 返回位置基本信息结构体。详细定义请参考[Location\_BasicInfo](capi-location-location-basicinfo.md)。 |

### OH\_LocationInfo\_GetAdditionalInfo()

PhonePC/2in1TabletTVWearable

```
1. Location_ResultCode OH_LocationInfo_GetAdditionalInfo(Location_Info* location, char* additionalInfo, uint32_t length)
```

**描述**

获取位置信息中的附加信息。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Location\_Info](capi-location-location-info.md)\* location | 指向位置信息结构体的指针。  需要传入非空指针，该指针可以在[Location\_InfoCallback](capi-oh-location-type-h.md#location_infocallback)中获取。 |
| char\* additionalInfo | char类型的非空指针；该变量用于保存附加信息字符串，该字符串是JSON格式。  该指针和对应的内存由调用者创建，建议申请大于等于256字节的内存。  如果传入空指针，会返回错误码。 |
| uint32\_t length | 表示additionalInfo的内存大小。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Location\_ResultCode](capi-oh-location-type-h.md#location_resultcode) | 返回操作结果，详细定义参见[Location\_ResultCode](capi-oh-location-type-h.md#location_resultcode)。  [LOCATION\_SUCCESS](capi-oh-location-type-h.md#location_resultcode) 获取附加信息成功。  [LOCATION\_INVALID\_PARAM](capi-oh-location-type-h.md#location_resultcode) 1. 入参location或additionalInfo是空指针。  2. 入参length太小，也就是additionalInfo指向的内存太小导致无法保存完整的附加信息字符串。 |

### Location\_InfoCallback()

PhonePC/2in1TabletTVWearable

```
1. typedef void (*Location_InfoCallback)(Location_Info* location, void* userData)
```

**描述**

用于接收位置上报的回调函数。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Location\_Info](capi-location-location-info.md)\* location | 指向[Location\_Info](capi-location-location-info.md)实例的指针，携带最新的位置信息。  location实例的内存会在[Location\_InfoCallback](capi-oh-location-type-h.md#location_infocallback)结束时回收，请在此之前调用[OH\_LocationInfo\_GetBasicInfo](capi-oh-location-type-h.md#oh_locationinfo_getbasicinfo)等接口获取位置信息。 |
| void\* userData | 指向调用者数据结构或对象的指针，该参数是通过[OH\_LocationRequestConfig\_SetCallback](capi-oh-location-type-h.md#oh_locationrequestconfig_setcallback)传入的。 |

### OH\_Location\_CreateRequestConfig()

PhonePC/2in1TabletTVWearable

```
1. Location_RequestConfig* OH_Location_CreateRequestConfig(void)
```

**描述**

创建一个位置请求参数结构体实例。

**起始版本：** 13

**返回：**

| 类型 | 说明 |
| --- | --- |
| [Location\_RequestConfig\*](capi-location-location-requestconfig.md) | 返回指向[Location\_RequestConfig](capi-location-location-requestconfig.md)实例的指针。  如果返回NULL表示创建失败，可能的原因是应用地址空间满，导致空间分配不出来。 |

### OH\_Location\_DestroyRequestConfig()

PhonePC/2in1TabletTVWearable

```
1. void OH_Location_DestroyRequestConfig(Location_RequestConfig* requestConfig)
```

**描述**

销毁位置请求参数实例并回收内存。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Location\_RequestConfig](capi-location-location-requestconfig.md)\* requestConfig | 指向[Location\_RequestConfig](capi-location-location-requestconfig.md)实例的指针。  该实例是由[OH\_Location\_CreateRequestConfig](capi-oh-location-type-h.md#oh_location_createrequestconfig)创建的。 |

### OH\_LocationRequestConfig\_SetUseScene()

PhonePC/2in1TabletTVWearable

```
1. void OH_LocationRequestConfig_SetUseScene(Location_RequestConfig* requestConfig, Location_UseScene useScene)
```

**描述**

设置位置请求参数中的用户活动场景。

位置请求参数[Location\_RequestConfig](capi-location-location-requestconfig.md)中以useScene优先。

如果设置了useScene，则powerConsumptionScene参数无效。

如果未设置useScene，设置了powerConsumptionScene则该参数生效。

如果两个参数都未设置，则默认useScene为[LOCATION\_USE\_SCENE\_DAILY\_LIFE\_SERVICE](capi-oh-location-type-h.md#location_usescene)，powerConsumptionScene参数无效。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Location\_RequestConfig](capi-location-location-requestconfig.md)\* requestConfig | 指向[Location\_RequestConfig](capi-location-location-requestconfig.md)实例的指针。  该实例是由[OH\_Location\_CreateRequestConfig](capi-oh-location-type-h.md#oh_location_createrequestconfig)创建的。 |
| [Location\_UseScene](capi-oh-location-type-h.md#location_usescene) useScene | 表示位置请求时的用户活动场景。  默认值是[LOCATION\_USE\_SCENE\_DAILY\_LIFE\_SERVICE](capi-oh-location-type-h.md#location_usescene)。  详细定义见[Location\_UseScene](capi-oh-location-type-h.md#location_usescene)。 |

### OH\_LocationRequestConfig\_SetPowerConsumptionScene()

PhonePC/2in1TabletTVWearable

```
1. void OH_LocationRequestConfig_SetPowerConsumptionScene(Location_RequestConfig* requestConfig, Location_PowerConsumptionScene powerConsumptionScene)
```

**描述**

设置位置请求参数中的功耗场景。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Location\_RequestConfig](capi-location-location-requestconfig.md)\* requestConfig | 指向[Location\_RequestConfig](capi-location-location-requestconfig.md)实例的指针。  该实例是由[OH\_Location\_CreateRequestConfig](capi-oh-location-type-h.md#oh_location_createrequestconfig)创建的。 |
| [Location\_PowerConsumptionScene](capi-oh-location-type-h.md#location_powerconsumptionscene) powerConsumptionScene | 表示位置请求的功耗场景。  默认值是[LOCATION\_LOW\_POWER\_CONSUMPTION](capi-oh-location-type-h.md#location_powerconsumptionscene)。  详细定义见[Location\_PowerConsumptionScene](capi-oh-location-type-h.md#location_powerconsumptionscene)。 |

### OH\_LocationRequestConfig\_SetInterval()

PhonePC/2in1TabletTVWearable

```
1. void OH_LocationRequestConfig_SetInterval(Location_RequestConfig* requestConfig, int interval)
```

**描述**

设置位置请求参数中的位置上报间隔。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Location\_RequestConfig](capi-location-location-requestconfig.md)\* requestConfig | 指向[Location\_RequestConfig](capi-location-location-requestconfig.md)实例的指针。  该实例是由[OH\_Location\_CreateRequestConfig](capi-oh-location-type-h.md#oh_location_createrequestconfig)创建的。 |
| int interval | 表示位置上报时间间隔，单位是“秒”。取值范围为大于等于1，默认值为1。 |

### OH\_LocationRequestConfig\_SetCallback()

PhonePC/2in1TabletTVWearable

```
1. void OH_LocationRequestConfig_SetCallback(Location_RequestConfig* requestConfig, Location_InfoCallback callback, void* userData)
```

**描述**

设置回调函数。

**起始版本：** 13

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [Location\_RequestConfig](capi-location-location-requestconfig.md)\* requestConfig | 指向[Location\_RequestConfig](capi-location-location-requestconfig.md)实例的指针。  该实例是由[OH\_Location\_CreateRequestConfig](capi-oh-location-type-h.md#oh_location_createrequestconfig)创建的。 |
| [Location\_InfoCallback](capi-oh-location-type-h.md#location_infocallback) callback | 指向回调函数的指针，该回调函数用于接收位置信息变化。  详细定义请参考[Location\_InfoCallback](capi-oh-location-type-h.md#location_infocallback)。 |
| void\* userData | 指向调用者数据结构或对象的指针。这个指针会在回调函数执行时作为入参回传给调用者。 |
