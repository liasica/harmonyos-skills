---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h
title: oh_commonevent.h
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 头文件 > oh_commonevent.h
category: harmonyos-references
scraped_at: 2026-09-02T15:02:05+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:0768d03289786671594880b4aa24bca79710cc29146101f14fd4db81da44626d
---

## 概述

本模块定义了发布、订阅/取消订阅公共事件、事件回调数据访问、有序事件控制等关键操作函数，以及错误码枚举与核心数据类型定义。

**API 组合使用关系说明：**

本模块存在三条明确的API调用流程：订阅流程、发布流程、有序事件处理流程。

**组合一：订阅并处理公共事件**

1. 通过OH\_CommonEvent\_CreateSubscribeInfo创建订阅者信息，声明需要订阅的事件名称，可选设置发布方权限与包名，用于过滤事件来源。
2. 通过OH\_CommonEvent\_CreateSubscriber创建订阅者并注册接收事件回调函数，再通过OH\_CommonEvent\_Subscribe发起事件订阅，订阅生效后即可在回调中等待事件投递。
3. 事件到达时，从回调参数CommonEvent\_RcvData中获取事件名、code数据、data数据以及发布方包名等信息，然后进行业务逻辑处理。
4. 不再需要订阅时，调用OH\_CommonEvent\_UnSubscribe取消订阅，并释放相关资源。

**组合二：发布带附加信息的公共事件**

1. 通过OH\_CommonEvent\_CreatePublishInfo创建公共事件属性对象，并按需设置code数据、data数据、订阅者包名、订阅者权限与附加信息等属性。
2. 通过OH\_CommonEvent\_PublishWithInfo发布携带属性的事件。

若无需附加属性，可直接调用便捷接口OH\_CommonEvent\_Publish(event)发布事件。

**组合三：[有序公共事件](../harmonyos-guides/common-event-glossary.md#ordered-common-event有序公共事件)处理**

有序公共事件在订阅回调内通过订阅者句柄进行控制，订阅者句柄需在创建订阅者时保存，以便在回调中使用。

1. 发布公共事件时，通过OH\_CommonEvent\_CreatePublishInfo(true)创建有序事件属性，事件将按订阅者优先级依次投递。
2. 订阅者可在回调中通过OH\_CommonEvent\_SetCodeToSubscriber、OH\_CommonEvent\_SetDataToSubscriber设置传递给后续订阅者的code与data数据；通过OH\_CommonEvent\_AbortCommonEvent可标记事件为中止状态，终止其向后续订阅者投递。
3. 回调处理完成后，必须调用OH\_CommonEvent\_FinishCommonEvent结束处理，否则事件无法继续投递给后续订阅者。

需注意本模块遵循典型的"创建—使用—释放"生命周期：

* **订阅侧对象**：CommonEvent\_SubscribeInfo→CommonEvent\_Subscriber。创建后订阅生效，取消订阅后需依次销毁订阅者和订阅信息，避免内存泄漏。
* **发布侧对象**：CommonEvent\_PublishInfo与CommonEvent\_Parameters。发布完成后需分别销毁，二者相互独立。

**库：** libohcommonevent.so

**引用文件：** <BasicServicesKit/oh\_commonevent.h>

**系统能力：** SystemCapability.Notification.CommonEvent

**起始版本：** 12

**相关模块：** [OH\_CommonEvent](capi-oh-commonevent.md)

## 汇总

### 结构体

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CommonEvent\_SubscribeInfo](capi-oh-commonevent-commonevent-subscribeinfo.md) | CommonEvent\_SubscribeInfo | 提供CommonEvent\_SubscribeInfo订阅者信息结构体声明。 |
| [CommonEvent\_PublishInfo](capi-oh-commonevent-commonevent-publishinfo.md) | CommonEvent\_PublishInfo | 发布公共事件时使用的公共事件属性对象。 |
| [CommonEvent\_RcvData](capi-oh-commonevent-commonevent-rcvdata.md) | CommonEvent\_RcvData | 提供CommonEvent\_RcvData公共事件回调数据结构体声明。 |

### 变量

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| void | CommonEvent\_Subscriber | 提供CommonEvent\_Subscriber订阅者声明。 |
| void | CommonEvent\_Parameters | 提供CommonEvent\_Parameters公共事件附加信息声明。 |

### 枚举

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | CommonEvent\_ErrCode | 枚举错误码。 |

### 函数

| 名称 | typedef关键字 | 描述 |
| --- | --- | --- |
| [typedef void (\*CommonEvent\_ReceiveCallback)(const CommonEvent\_RcvData \*data)](capi-oh-commonevent-h.md#commonevent_receivecallback) | CommonEvent\_ReceiveCallback | 提供CommonEvent\_ReceiveCallback回调函数声明。 |
| [CommonEvent\_SubscribeInfo\* OH\_CommonEvent\_CreateSubscribeInfo(const char\* events[], int32\_t eventsNum)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_createsubscribeinfo) | - | 创建订阅者信息。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublisherPermission(CommonEvent\_SubscribeInfo\* info, const char\* permission)](capi-oh-commonevent-h.md#oh_commonevent_setpublisherpermission) | - | 设置发布方权限。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublisherBundleName(CommonEvent\_SubscribeInfo\* info, const char\* bundleName)](capi-oh-commonevent-h.md#oh_commonevent_setpublisherbundlename) | - | 设置发布方包名称。 |
| [void OH\_CommonEvent\_DestroySubscribeInfo(CommonEvent\_SubscribeInfo\* info)](capi-oh-commonevent-h.md#oh_commonevent_destroysubscribeinfo) | - | 释放订阅者信息。 |
| [CommonEvent\_Subscriber\* OH\_CommonEvent\_CreateSubscriber(const CommonEvent\_SubscribeInfo\* info,CommonEvent\_ReceiveCallback callback)](capi-oh-commonevent-h.md#oh_commonevent_createsubscriber) | - | 创建订阅者。 |
| [void OH\_CommonEvent\_DestroySubscriber(CommonEvent\_Subscriber\* subscriber)](capi-oh-commonevent-h.md#oh_commonevent_destroysubscriber) | - | 释放订阅者。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_Subscribe(const CommonEvent\_Subscriber\* subscriber)](capi-oh-commonevent-h.md#oh_commonevent_subscribe) | - | 订阅公共事件。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_UnSubscribe(const CommonEvent\_Subscriber\* subscriber)](capi-oh-commonevent-h.md#oh_commonevent_unsubscribe) | - | 退订公共事件。 |
| [const char\* OH\_CommonEvent\_GetEventFromRcvData(const CommonEvent\_RcvData\* rcvData)](capi-oh-commonevent-h.md#oh_commonevent_geteventfromrcvdata) | - | 获取当前接收的公共事件名称。 |
| [int32\_t OH\_CommonEvent\_GetCodeFromRcvData(const CommonEvent\_RcvData\* rcvData)](capi-oh-commonevent-h.md#oh_commonevent_getcodefromrcvdata) | - | 获取公共事件传递的Code数据，整数类型。 |
| [const char\* OH\_CommonEvent\_GetDataStrFromRcvData(const CommonEvent\_RcvData\* rcvData)](capi-oh-commonevent-h.md#oh_commonevent_getdatastrfromrcvdata) | - | 获取公共事件传递的数据，字符串类型。 |
| [const char\* OH\_CommonEvent\_GetBundleNameFromRcvData(const CommonEvent\_RcvData\* rcvData)](capi-oh-commonevent-h.md#oh_commonevent_getbundlenamefromrcvdata) | - | 获取接收到的公共事件的包名称信息。 |
| [const CommonEvent\_Parameters\* OH\_CommonEvent\_GetParametersFromRcvData(const CommonEvent\_RcvData\* rcvData)](capi-oh-commonevent-h.md#oh_commonevent_getparametersfromrcvdata) | - | 获取公共事件附加信息。 |
| [CommonEvent\_PublishInfo\* OH\_CommonEvent\_CreatePublishInfo(bool ordered)](capi-oh-commonevent-h.md#oh_commonevent_createpublishinfo) | - | 创建公共事件属性对象。 |
| [void OH\_CommonEvent\_DestroyPublishInfo(CommonEvent\_PublishInfo\* info)](capi-oh-commonevent-h.md#oh_commonevent_destroypublishinfo) | - | 销毁公共事件属性对象。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoBundleName(CommonEvent\_PublishInfo\* info, const char\* bundleName)](capi-oh-commonevent-h.md#oh_commonevent_setpublishinfobundlename) | - | 设置公共事件订阅者包名称。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoPermissions(CommonEvent\_PublishInfo\* info,const char\* permissions[], int32\_t num)](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-commonevent-h#oh_commonevent_setpublishinfopermissions) | - | 设置公共事件订阅者权限。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoCode(CommonEvent\_PublishInfo\* info, int32\_t code)](capi-oh-commonevent-h.md#oh_commonevent_setpublishinfocode) | - | 设置公共事件传递的数据，整数类型。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoData(CommonEvent\_PublishInfo\* info,const char\* data, size\_t length)](capi-oh-commonevent-h.md#oh_commonevent_setpublishinfodata) | - | 设置公共事件传递的数据，字符串类型。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetPublishInfoParameters(CommonEvent\_PublishInfo\* info,CommonEvent\_Parameters\* param)](capi-oh-commonevent-h.md#oh_commonevent_setpublishinfoparameters) | - | 设置公共事件附加信息。 |
| [CommonEvent\_Parameters\* OH\_CommonEvent\_CreateParameters()](capi-oh-commonevent-h.md#oh_commonevent_createparameters) | - | 创建公共事件附加信息对象。 |
| [void OH\_CommonEvent\_DestroyParameters(CommonEvent\_Parameters\* param)](capi-oh-commonevent-h.md#oh_commonevent_destroyparameters) | - | 销毁公共事件附加信息对象。 |
| [bool OH\_CommonEvent\_HasKeyInParameters(const CommonEvent\_Parameters\* para, const char\* key)](capi-oh-commonevent-h.md#oh_commonevent_haskeyinparameters) | - | 检查附加信息中是否包含键值对信息。 |
| [int OH\_CommonEvent\_GetIntFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const int defaultValue)](capi-oh-commonevent-h.md#oh_commonevent_getintfromparameters) | - | 获取公共事件附加信息中键为key的int类型内容。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetIntToParameters(CommonEvent\_Parameters\* param, const char\* key, int value)](capi-oh-commonevent-h.md#oh_commonevent_setinttoparameters) | - | 设置公共事件附加信息的int类型内容。 |
| [int32\_t OH\_CommonEvent\_GetIntArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, int\*\* array)](capi-oh-commonevent-h.md#oh_commonevent_getintarrayfromparameters) | - | 获取公共事件附加信息中键为key的int数组数据。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetIntArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const int\* value, size\_t num)](capi-oh-commonevent-h.md#oh_commonevent_setintarraytoparameters) | - | 设置公共事件附加信息的int数组内容。 |
| [long OH\_CommonEvent\_GetLongFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const long defaultValue)](capi-oh-commonevent-h.md#oh_commonevent_getlongfromparameters) | - | 获取公共事件附加信息中键为key的long类型数据。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetLongToParameters(CommonEvent\_Parameters\* param, const char\* key, long value)](capi-oh-commonevent-h.md#oh_commonevent_setlongtoparameters) | - | 设置公共事件附加信息的long类型内容。 |
| [int32\_t OH\_CommonEvent\_GetLongArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, long\*\* array)](capi-oh-commonevent-h.md#oh_commonevent_getlongarrayfromparameters) | - | 获取公共事件附加信息的long数组内容。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetLongArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const long\* value, size\_t num)](capi-oh-commonevent-h.md#oh_commonevent_setlongarraytoparameters) | - | 设置公共事件附加信息的long数组内容。 |
| [bool OH\_CommonEvent\_GetBoolFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const bool defaultValue)](capi-oh-commonevent-h.md#oh_commonevent_getboolfromparameters) | - | 获取公共事件附加信息中键为key的布尔类型数据。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetBoolToParameters(CommonEvent\_Parameters\* param, const char\* key, bool value)](capi-oh-commonevent-h.md#oh_commonevent_setbooltoparameters) | - | 设置公共事件附加信息的布尔类型内容。 |
| [int32\_t OH\_CommonEvent\_GetBoolArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, bool\*\* array)](capi-oh-commonevent-h.md#oh_commonevent_getboolarrayfromparameters) | - | 获取公共事件附加信息的布尔数组内容。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetBoolArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const bool\* value, size\_t num)](capi-oh-commonevent-h.md#oh_commonevent_setboolarraytoparameters) | - | 设置公共事件附加信息的布尔数组内容。 |
| [char OH\_CommonEvent\_GetCharFromParameters(const CommonEvent\_Parameters\* para, const char\* key, const char defaultValue)](capi-oh-commonevent-h.md#oh_commonevent_getcharfromparameters) | - | 获取公共事件附加信息中键为key的字符类型数据。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetCharToParameters(CommonEvent\_Parameters\* param, const char\* key, char value)](capi-oh-commonevent-h.md#oh_commonevent_setchartoparameters) | - | 设置公共事件附加信息的字符类型内容。 |
| [int32\_t OH\_CommonEvent\_GetCharArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key, char\*\* array)](capi-oh-commonevent-h.md#oh_commonevent_getchararrayfromparameters) | - | 获取公共事件附加信息的字符数组内容。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetCharArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const char\* value, size\_t num)](capi-oh-commonevent-h.md#oh_commonevent_setchararraytoparameters) | - | 设置公共事件附加信息的字符数组内容。 |
| [double OH\_CommonEvent\_GetDoubleFromParameters(const CommonEvent\_Parameters\* para, const char\* key,const double defaultValue)](capi-oh-commonevent-h.md#oh_commonevent_getdoublefromparameters) | - | 获取公共事件附加信息的double类型内容。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetDoubleToParameters(CommonEvent\_Parameters\* param, const char\* key,double value)](capi-oh-commonevent-h.md#oh_commonevent_setdoubletoparameters) | - | 设置公共事件附加信息的double类型内容。 |
| [int32\_t OH\_CommonEvent\_GetDoubleArrayFromParameters(const CommonEvent\_Parameters\* para, const char\* key,double\*\* array)](capi-oh-commonevent-h.md#oh_commonevent_getdoublearrayfromparameters) | - | 获取公共事件附加信息中键为key的double数组数据。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_SetDoubleArrayToParameters(CommonEvent\_Parameters\* param, const char\* key,const double\* value, size\_t num)](capi-oh-commonevent-h.md#oh_commonevent_setdoublearraytoparameters) | - | 设置公共事件附加信息的double数组内容。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_Publish(const char\* event)](capi-oh-commonevent-h.md#oh_commonevent_publish) | - | 发布公共事件。 |
| [CommonEvent\_ErrCode OH\_CommonEvent\_PublishWithInfo(const char\* event, const CommonEvent\_PublishInfo\* info)](capi-oh-commonevent-h.md#oh_commonevent_publishwithinfo) | - | 发布带有指定属性的公共事件。 |
| [bool OH\_CommonEvent\_IsOrderedCommonEvent(const CommonEvent\_Subscriber\* subscriber)](capi-oh-commonevent-h.md#oh_commonevent_isorderedcommonevent) | - | 查询当前公共事件是否为[有序公共事件](../harmonyos-guides/common-event-glossary.md#ordered-common-event有序公共事件)。 |
| [bool OH\_CommonEvent\_FinishCommonEvent(CommonEvent\_Subscriber\* subscriber)](capi-oh-commonevent-h.md#oh_commonevent_finishcommonevent) | - | 用于订阅者结束对当前有序公共事件的处理。 |
| [bool OH\_CommonEvent\_GetAbortCommonEvent(const CommonEvent\_Subscriber\* subscriber)](capi-oh-commonevent-h.md#oh_commonevent_getabortcommonevent) | - | 获取当前有序公共事件是否处于中止状态。 |
| [bool OH\_CommonEvent\_AbortCommonEvent(CommonEvent\_Subscriber\* subscriber)](capi-oh-commonevent-h.md#oh_commonevent_abortcommonevent) | - | 该接口与[OH\_CommonEvent\_FinishCommonEvent](capi-oh-commonevent-h.md#oh_commonevent_finishcommonevent)配合使用，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。 |
| [bool OH\_CommonEvent\_ClearAbortCommonEvent(CommonEvent\_Subscriber\* subscriber)](capi-oh-commonevent-h.md#oh_commonevent_clearabortcommonevent) | - | 该接口与[OH\_CommonEvent\_FinishCommonEvent](capi-oh-commonevent-h.md#oh_commonevent_finishcommonevent)配合使用，可以取消当前有序公共事件的中止状态，使该公共事件继续向下一个订阅者传递。 |
| [int32\_t OH\_CommonEvent\_GetCodeFromSubscriber(const CommonEvent\_Subscriber\* subscriber)](capi-oh-commonevent-h.md#oh_commonevent_getcodefromsubscriber) | - | 获取有序公共事件传递的数据，整数类型。 |
| [bool OH\_CommonEvent\_SetCodeToSubscriber(CommonEvent\_Subscriber\* subscriber, int32\_t code)](capi-oh-commonevent-h.md#oh_commonevent_setcodetosubscriber) | - | 设置有序公共事件传递的数据，整数类型。 |
| [const char\* OH\_CommonEvent\_GetDataFromSubscriber(const CommonEvent\_Subscriber\* subscriber)](capi-oh-commonevent-h.md#oh_commonevent_getdatafromsubscriber) | - | 获取有序公共事件传递的数据，字符串类型。 |
| [bool OH\_CommonEvent\_SetDataToSubscriber(CommonEvent\_Subscriber\* subscriber, const char\* data, size\_t length)](capi-oh-commonevent-h.md#oh_commonevent_setdatatosubscriber) | - | 设置有序公共事件传递的数据，字符串类型。 |

## 枚举类型说明

### CommonEvent\_ErrCode

```c
enum CommonEvent_ErrCode
```

**描述**

枚举错误码。

**起始版本：** 12

| 枚举项 | 描述 |
| --- | --- |
| COMMONEVENT\_ERR\_OK = 0 | 成功。 |
| COMMONEVENT\_ERR\_PERMISSION\_ERROR = 201 | 权限错误。 |
| COMMONEVENT\_ERR\_INVALID\_PARAMETER = 401 | 参数错误。参数不合法，请检查参数类型、取值范围或参数是否为空。 |
| COMMONEVENT\_ERR\_SENDING\_LIMIT\_EXCEEDED = 1500003 | 事件发送频率过高。请检查应用是否过于频繁地发送公共事件，如发送频率超过每5毫秒20个，请降低公共事件发送频率或增加发送间隔后重新尝试。  **起始版本：** 20 |
| COMMONEVENT\_ERR\_NOT\_SYSTEM\_SERVICE = 1500004 | 三方应用无法发送[系统公共事件](../harmonyos-guides/common-event-glossary.md#system-common-event系统公共事件)。请检查当前应用是否为系统应用，或当前服务是否为系统服务。 |
| COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED = 1500007 | IPC发送失败。请勿频繁建立连接，稍后重新尝试。 |
| COMMONEVENT\_ERR\_INIT\_UNDONE = 1500008 | 服务未初始化。请稍后重新尝试。 |
| COMMONEVENT\_ERR\_OBTAIN\_SYSTEM\_PARAMS = 1500009 | 系统错误。请稍后重新尝试。 |
| COMMONEVENT\_ERR\_SUBSCRIBER\_NUM\_EXCEEDED = 1500010 | 进程内订阅者数量超过系统限制（200个）。请检查应用内是否存在订阅者未取消订阅，如存在则取消订阅后重新尝试；不存在请稍后重新尝试。 |
| COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED = 1500011 | 内存分配失败。请稍后重新尝试。 |

## 函数说明

### CommonEvent\_ReceiveCallback()

```c
typedef void (*CommonEvent_ReceiveCallback)(const CommonEvent_RcvData *data)
```

**描述**

提供CommonEvent\_ReceiveCallback回调函数声明。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_RcvData](capi-oh-commonevent-commonevent-rcvdata.md) \*data | 公共事件回调数据。 |

### OH\_CommonEvent\_CreateSubscribeInfo()

```c
CommonEvent_SubscribeInfo* OH_CommonEvent_CreateSubscribeInfo(const char* events[], int32_t eventsNum)
```

**描述**

创建订阅者信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* events[] | 订阅的公共事件，实际订阅的数量为eventsNum与events数组长度的最小值。 |
| int32\_t eventsNum | 订阅的公共事件数量，非负整数，取值为events数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_SubscribeInfo](capi-oh-commonevent-commonevent-subscribeinfo.md)\* | 成功则返回订阅者信息，失败则返回NULL。该指针由内部管理，在[OH\_CommonEvent\_DestroySubscribeInfo()](capi-oh-commonevent-h.md#oh_commonevent_destroysubscribeinfo)时释放。 |

### OH\_CommonEvent\_SetPublisherPermission()

```c
CommonEvent_ErrCode OH_CommonEvent_SetPublisherPermission(CommonEvent_SubscribeInfo* info, const char* permission)
```

**描述**

设置发布方权限。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_SubscribeInfo](capi-oh-commonevent-commonevent-subscribeinfo.md)\* info | 待设置发布方权限的订阅者信息对象。 |
| const char\* permission | 权限名称。取值为系统已定义的权限名，订阅方将只能接收到具有该权限的发送方发布的事件。不设置时，可接收所有发送方发布的事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。 |

### OH\_CommonEvent\_SetPublisherBundleName()

```c
CommonEvent_ErrCode OH_CommonEvent_SetPublisherBundleName(CommonEvent_SubscribeInfo* info, const char* bundleName)
```

**描述**

设置发布方包名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_SubscribeInfo](capi-oh-commonevent-commonevent-subscribeinfo.md)\* info | 待设置发布方权限的订阅者信息对象。 |
| const char\* bundleName | 包名称。用于限制订阅方只接收该bundleName的发布者发布的公共事件。不设置时，可接收所有应用发布的公共事件。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。 |

### OH\_CommonEvent\_DestroySubscribeInfo()

```c
void OH_CommonEvent_DestroySubscribeInfo(CommonEvent_SubscribeInfo* info)
```

**描述**

释放订阅者信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_SubscribeInfo](capi-oh-commonevent-commonevent-subscribeinfo.md)\* info | 订阅者信息。 |

### OH\_CommonEvent\_CreateSubscriber()

```c
CommonEvent_Subscriber* OH_CommonEvent_CreateSubscriber(const CommonEvent_SubscribeInfo* info,CommonEvent_ReceiveCallback callback)
```

**描述**

创建订阅者。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_SubscribeInfo](capi-oh-commonevent-commonevent-subscribeinfo.md)\* info | 订阅者信息。 |
| [CommonEvent\_ReceiveCallback](capi-oh-commonevent-h.md#commonevent_receivecallback) callback | 公共事件回调函数。当公共事件订阅成功后，事件触发时通过data返回公共事件数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_Subscriber](capi-oh-commonevent-h.md#变量)\* | 成功则返回订阅者，失败则返回NULL。该指针由内部管理，在[OH\_CommonEvent\_DestroySubscriber()](capi-oh-commonevent-h.md#oh_commonevent_destroysubscriber)时释放。 |

### OH\_CommonEvent\_DestroySubscriber()

```c
void OH_CommonEvent_DestroySubscriber(CommonEvent_Subscriber* subscriber)
```

**描述**

释放订阅者。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Subscriber](capi-oh-commonevent-h.md#变量)\* subscriber | 订阅者。 |

### OH\_CommonEvent\_Subscribe()

```c
CommonEvent_ErrCode OH_CommonEvent_Subscribe(const CommonEvent_Subscriber* subscriber)
```

**描述**

订阅公共事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Subscriber](capi-oh-commonevent-h.md#变量)\* subscriber | 订阅者。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数subscriber无效。  返回[COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED](capi-oh-commonevent-h.md#commonevent_errcode)表示IPC请求发送失败。  返回[COMMONEVENT\_ERR\_INIT\_UNDONE](capi-oh-commonevent-h.md#commonevent_errcode)表示[公共事件服务](../harmonyos-guides/common-event-glossary.md#common-event-service-ces公共事件服务)未初始化。  返回[COMMONEVENT\_ERR\_SUBSCRIBER\_NUM\_EXCEEDED](capi-oh-commonevent-h.md#commonevent_errcode)表示进程内订阅者数量超过系统限制（200个）。  返回[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](capi-oh-commonevent-h.md#commonevent_errcode)表示系统分配内存失败。 |

### OH\_CommonEvent\_UnSubscribe()

```c
CommonEvent_ErrCode OH_CommonEvent_UnSubscribe(const CommonEvent_Subscriber* subscriber)
```

**描述**

退订公共事件。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Subscriber](capi-oh-commonevent-h.md#变量)\* subscriber | 订阅者。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数subscriber无效。  返回[COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED](capi-oh-commonevent-h.md#commonevent_errcode)表示IPC请求发送失败。  返回[COMMONEVENT\_ERR\_INIT\_UNDONE](capi-oh-commonevent-h.md#commonevent_errcode)表示公共事件服务未初始化。 |

### OH\_CommonEvent\_GetEventFromRcvData()

```c
const char* OH_CommonEvent_GetEventFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取接收到的公共事件名称。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_RcvData](capi-oh-commonevent-commonevent-rcvdata.md)\* rcvData | 公共事件回调数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 返回公共事件名称。该指针由系统产生，回调函数[CommonEvent\_ReceiveCallback](capi-oh-commonevent-h.md#commonevent_receivecallback)结束后即刻释放，不可在回调函数外部使用。 |

### OH\_CommonEvent\_GetCodeFromRcvData()

```c
int32_t OH_CommonEvent_GetCodeFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取接收到的公共事件Code数据，整数类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_RcvData](capi-oh-commonevent-commonevent-rcvdata.md)\* rcvData | 公共事件回调数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回接收到的公共事件Code数据，整数类型。 |

### OH\_CommonEvent\_GetDataStrFromRcvData()

```c
const char* OH_CommonEvent_GetDataStrFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取接收到的公共事件数据，字符串类型。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_RcvData](capi-oh-commonevent-commonevent-rcvdata.md)\* rcvData | 公共事件回调数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 返回接收到的公共事件数据，字符串类型。该指针由系统产生，回调函数[CommonEvent\_ReceiveCallback](capi-oh-commonevent-h.md#commonevent_receivecallback)结束后即刻释放，不可在回调函数外部使用。 |

### OH\_CommonEvent\_GetBundleNameFromRcvData()

```c
const char* OH_CommonEvent_GetBundleNameFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取接收到的公共事件的包名称信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_RcvData](capi-oh-commonevent-commonevent-rcvdata.md)\* rcvData | 公共事件回调数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 返回公共事件的包名称。该指针由系统产生，回调函数[CommonEvent\_ReceiveCallback](capi-oh-commonevent-h.md#commonevent_receivecallback)结束后即刻释放，不可在回调函数外部使用。 |

### OH\_CommonEvent\_GetParametersFromRcvData()

```c
const CommonEvent_Parameters* OH_CommonEvent_GetParametersFromRcvData(const CommonEvent_RcvData* rcvData)
```

**描述**

获取公共事件附加信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_RcvData](capi-oh-commonevent-commonevent-rcvdata.md)\* rcvData | 公共事件回调数据。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* | 返回公共事件附加信息。 |

### OH\_CommonEvent\_CreatePublishInfo()

```c
CommonEvent_PublishInfo* OH_CommonEvent_CreatePublishInfo(bool ordered)
```

**描述**

创建公共事件属性对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| bool ordered | 是否为[有序公共事件](../harmonyos-guides/common-event-glossary.md#ordered-common-event有序公共事件)。  - true：有序公共事件。  - false：[无序公共事件](../harmonyos-guides/common-event-glossary.md#unordered-common-event无序公共事件)。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_PublishInfo](capi-oh-commonevent-commonevent-publishinfo.md)\* | 创建的公共事件属性对象，创建失败时，返回NULL。该指针由内部管理，在[OH\_CommonEvent\_DestroyPublishInfo()](capi-oh-commonevent-h.md#oh_commonevent_destroypublishinfo)时释放。 |

### OH\_CommonEvent\_DestroyPublishInfo()

```c
void OH_CommonEvent_DestroyPublishInfo(CommonEvent_PublishInfo* info)
```

**描述**

销毁公共事件属性对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_PublishInfo](capi-oh-commonevent-commonevent-publishinfo.md)\* info | 要销毁的公共事件属性对象。 |

### OH\_CommonEvent\_SetPublishInfoBundleName()

```c
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoBundleName(CommonEvent_PublishInfo* info, const char* bundleName)
```

**描述**

设置公共事件订阅者包名称。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_PublishInfo](capi-oh-commonevent-commonevent-publishinfo.md)\* info | 公共事件属性对象。 |
| const char\* bundleName | 设置的订阅者包名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。 |

### OH\_CommonEvent\_SetPublishInfoPermissions()

```c
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoPermissions(CommonEvent_PublishInfo* info,const char* permissions[], int32_t num)
```

**描述**

设置公共事件订阅者权限。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_PublishInfo](capi-oh-commonevent-commonevent-publishinfo.md)\* info | 公共事件属性对象。 |
| const char\* permissions[] | 订阅者权限名称数组，只有具备这些权限的订阅者才能收到该公共事件。生效数量为num与permissions数组长度的最小值。 |
| int32\_t num | 权限名称的数量，取值为permissions数组长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。 |

### OH\_CommonEvent\_SetPublishInfoCode()

```c
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoCode(CommonEvent_PublishInfo* info, int32_t code)
```

**描述**

设置公共事件传递的数据，整数类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_PublishInfo](capi-oh-commonevent-commonevent-publishinfo.md)\* info | 公共事件属性对象。 |
| int32\_t code | 公共事件传递的数据，整数类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。 |

### OH\_CommonEvent\_SetPublishInfoData()

```c
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoData(CommonEvent_PublishInfo* info, const char* data, size_t length)
```

**描述**

设置公共事件传递的数据，字符串类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_PublishInfo](capi-oh-commonevent-commonevent-publishinfo.md)\* info | 公共事件属性对象。 |
| const char\* data | 公共事件传递的数据，字符串类型，实际有效数据长度为length与data字符串长度的最小值。 |
| size\_t length | 结果数据的长度，取值为data数据字符串长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。 |

### OH\_CommonEvent\_SetPublishInfoParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetPublishInfoParameters(CommonEvent_PublishInfo* info,CommonEvent_Parameters* param)
```

**描述**

设置公共事件附加信息。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_PublishInfo](capi-oh-commonevent-commonevent-publishinfo.md)\* info | 公共事件属性对象。 |
| [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* param | 设置的附加信息。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。 |

### OH\_CommonEvent\_CreateParameters()

```c
CommonEvent_Parameters* OH_CommonEvent_CreateParameters()
```

**描述**

创建公共事件附加信息对象。

**起始版本：** 18

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* | 返回公共事件附加信息，创建失败时，返回NULL。该指针由内部管理，在[OH\_CommonEvent\_DestroyParameters()](capi-oh-commonevent-h.md#oh_commonevent_destroyparameters)时释放。 |

### OH\_CommonEvent\_DestroyParameters()

```c
void OH_CommonEvent_DestroyParameters(CommonEvent_Parameters* param)
```

**描述**

销毁公共事件附加信息对象。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* param | 公共事件附加信息。 |

### OH\_CommonEvent\_HasKeyInParameters()

```c
bool OH_CommonEvent_HasKeyInParameters(const CommonEvent_Parameters* para, const char* key)
```

**描述**

检查附加信息中是否包含键值对信息。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回数据键是否存在。  - true：存在。  - false：不存在。 |

### OH\_CommonEvent\_GetIntFromParameters()

```c
int OH_CommonEvent_GetIntFromParameters(const CommonEvent_Parameters* para, const char* key, const int defaultValue)
```

**描述**

获取公共事件附加信息中键为key的int类型内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const int defaultValue | 默认值，当指定key不存在时返回此默认值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int | 返回查询的int类型数据。 |

### OH\_CommonEvent\_SetIntToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetIntToParameters(CommonEvent_Parameters* param, const char* key, int value)
```

**描述**

设置公共事件附加信息的int类型内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| int value | 设置的int类型内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。 |

### OH\_CommonEvent\_GetIntArrayFromParameters()

```c
int32_t OH_CommonEvent_GetIntArrayFromParameters(const CommonEvent_Parameters* para, const char* key, int** array)
```

**描述**

获取公共事件附加信息中键为key的int数组数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| int\*\* array | 输出参数，用于接收查询到的int数组数据。该数组内存由函数内部分配，调用者无需预先分配。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回查询的数组长度，默认值为0。 |

### OH\_CommonEvent\_SetIntArrayToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetIntArrayToParameters(CommonEvent_Parameters* param, const char* key,const int* value, size_t num)
```

**描述**

设置公共事件附加信息的int数组内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const int\* value | 设置的int数组内容。实际设置的数量为num，value数组长度需大于num，否则会有越界访问风险。 |
| size\_t num | 设置的int数组内容中元素的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。  返回[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](capi-oh-commonevent-h.md#commonevent_errcode)表示内存分配失败。 |

### OH\_CommonEvent\_GetLongFromParameters()

```c
long OH_CommonEvent_GetLongFromParameters(const CommonEvent_Parameters* para, const char* key, const long defaultValue)
```

**描述**

获取公共事件附加信息中键为key的long类型数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const long defaultValue | 默认值，当指定key不存在时返回此默认值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| long | 返回查询的long类型数据。 |

### OH\_CommonEvent\_SetLongToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetLongToParameters(CommonEvent_Parameters* param, const char* key, long value)
```

**描述**

设置公共事件附加信息的long类型内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| long value | 设置的long类型内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。 |

### OH\_CommonEvent\_GetLongArrayFromParameters()

```c
int32_t OH_CommonEvent_GetLongArrayFromParameters(const CommonEvent_Parameters* para, const char* key, long** array)
```

**描述**

获取公共事件附加信息的long数组内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| long\*\* array | 输出参数，用于接收查询到的long数组数据。该数组内存由函数内部分配，调用者无需预先分配。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回查询的数组长度，默认值为0。 |

### OH\_CommonEvent\_SetLongArrayToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetLongArrayToParameters(CommonEvent_Parameters* param, const char* key,const long* value, size_t num)
```

**描述**

设置公共事件附加信息的long数组内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const long\* value | 设置的long数组内容。实际设置的数量为num，value数组长度需大于num，否则会有越界访问风险。 |
| size\_t num | 设置的long数组内容中元素的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。  返回[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](capi-oh-commonevent-h.md#commonevent_errcode)表示内存分配失败。 |

### OH\_CommonEvent\_GetBoolFromParameters()

```c
bool OH_CommonEvent_GetBoolFromParameters(const CommonEvent_Parameters* para, const char* key, const bool defaultValue)
```

**描述**

获取公共事件附加信息中键为key的布尔类型数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const bool defaultValue | 默认值，当指定key不存在时返回此默认值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回查询的bool类型数据。 |

### OH\_CommonEvent\_SetBoolToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetBoolToParameters(CommonEvent_Parameters* param, const char* key, bool value)
```

**描述**

设置公共事件附加信息的布尔类型内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| bool value | 设置的布尔类型内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。 |

### OH\_CommonEvent\_GetBoolArrayFromParameters()

```c
int32_t OH_CommonEvent_GetBoolArrayFromParameters(const CommonEvent_Parameters* para, const char* key, bool** array)
```

**描述**

获取公共事件附加信息的布尔数组内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| bool\*\* array | 输出参数，用于接收查询到的bool数组数据。该数组内存由函数内部分配，调用者无需预先分配。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回查询的数组长度，默认值为0。 |

### OH\_CommonEvent\_SetBoolArrayToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetBoolArrayToParameters(CommonEvent_Parameters* param, const char* key,const bool* value, size_t num)
```

**描述**

设置公共事件附加信息的布尔数组内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const bool\* value | 设置的布尔数组内容。实际设置的数量为num，value数组长度需大于num，否则会有越界访问风险。 |
| size\_t num | 设置的布尔数组内容中元素的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。  返回[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](capi-oh-commonevent-h.md#commonevent_errcode)表示内存分配失败。 |

### OH\_CommonEvent\_GetCharFromParameters()

```c
char OH_CommonEvent_GetCharFromParameters(const CommonEvent_Parameters* para, const char* key, const char defaultValue)
```

**描述**

获取公共事件附加信息中键为key的字符类型数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const char defaultValue | 默认值，当指定key不存在时返回此默认值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| char | 返回查询的char类型数据。 |

### OH\_CommonEvent\_SetCharToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetCharToParameters(CommonEvent_Parameters* param, const char* key, char value)
```

**描述**

设置公共事件附加信息的字符类型内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| char value | 设置的字符类型内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。 |

### OH\_CommonEvent\_GetCharArrayFromParameters()

```c
int32_t OH_CommonEvent_GetCharArrayFromParameters(const CommonEvent_Parameters* para, const char* key, char** array)
```

**描述**

获取公共事件附加信息的字符数组内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| char\*\* array | 输出参数，用于接收查询到的char数组数据。该数组内存由函数内部分配，调用者无需预先分配。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回查询的数组长度，默认值为0。 |

### OH\_CommonEvent\_SetCharArrayToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetCharArrayToParameters(CommonEvent_Parameters* param, const char* key,const char* value, size_t num)
```

**描述**

设置公共事件附加信息的字符数组内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const char\* value | 设置的字符数组内容。实际设置的数量为num与value数组长度的最小值。 |
| size\_t num | 设置的字符数组内容中元素的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。 |

### OH\_CommonEvent\_GetDoubleFromParameters()

```c
double OH_CommonEvent_GetDoubleFromParameters(const CommonEvent_Parameters* para, const char* key, const double defaultValue)
```

**描述**

获取公共事件附加信息的double类型内容。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const double defaultValue | 默认值，当指定key不存在时返回此默认值。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| double | 返回查询的double类型数据。 |

### OH\_CommonEvent\_SetDoubleToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetDoubleToParameters(CommonEvent_Parameters* param, const char* key,double value)
```

**描述**

设置公共事件附加信息的double类型内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| double value | 设置的double类型内容。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。 |

### OH\_CommonEvent\_GetDoubleArrayFromParameters()

```c
int32_t OH_CommonEvent_GetDoubleArrayFromParameters(const CommonEvent_Parameters* para, const char* key,double** array)
```

**描述**

获取公共事件附加信息中键为key的double数组数据。

**起始版本：** 12

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* para | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| double\*\* array | 输出参数，用于接收查询到的double数组数据。该数组内存由函数内部分配，调用者无需预先分配。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回查询的数组长度，默认值为0。 |

### OH\_CommonEvent\_SetDoubleArrayToParameters()

```c
CommonEvent_ErrCode OH_CommonEvent_SetDoubleArrayToParameters(CommonEvent_Parameters* param, const char* key,const double* value, size_t num)
```

**描述**

设置公共事件附加信息的double数组内容。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Parameters](capi-oh-commonevent-h.md#变量)\* param | 公共事件附加信息。 |
| const char\* key | 数据键。 |
| const double\* value | 设置的double数组内容。实际设置的数量为num，value数组长度需大于num，否则会有越界访问风险。 |
| size\_t num | 设置的double数组内容中元素的个数。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。  返回[COMMONEVENT\_ERR\_ALLOC\_MEMORY\_FAILED](capi-oh-commonevent-h.md#commonevent_errcode)表示内存分配失败。 |

### OH\_CommonEvent\_Publish()

```c
CommonEvent_ErrCode OH_CommonEvent_Publish(const char* event)
```

**描述**

发布公共事件。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* event | 公共事件名称。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。  返回[COMMONEVENT\_ERR\_SENDING\_LIMIT\_EXCEEDED](capi-oh-commonevent-h.md#commonevent_errcode)表示事件发送频率过高。  返回[COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED](capi-oh-commonevent-h.md#commonevent_errcode)表示IPC请求发送失败。  返回[COMMONEVENT\_ERR\_INIT\_UNDONE](capi-oh-commonevent-h.md#commonevent_errcode)表示公共事件服务未初始化。 |

### OH\_CommonEvent\_PublishWithInfo()

```c
CommonEvent_ErrCode OH_CommonEvent_PublishWithInfo(const char* event, const CommonEvent_PublishInfo* info)
```

**描述**

发布带有指定属性的公共事件。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const char\* event | 公共事件名称。 |
| const [CommonEvent\_PublishInfo](capi-oh-commonevent-commonevent-publishinfo.md)\* info | 设置的公共事件属性。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| [CommonEvent\_ErrCode](capi-oh-commonevent-h.md#commonevent_errcode) | 返回错误码。  返回[COMMONEVENT\_ERR\_OK](capi-oh-commonevent-h.md#commonevent_errcode)表示成功。  返回[COMMONEVENT\_ERR\_INVALID\_PARAMETER](capi-oh-commonevent-h.md#commonevent_errcode)表示参数错误。  返回[COMMONEVENT\_ERR\_SENDING\_LIMIT\_EXCEEDED](capi-oh-commonevent-h.md#commonevent_errcode)表示事件发送频率过高。  返回[COMMONEVENT\_ERR\_SENDING\_REQUEST\_FAILED](capi-oh-commonevent-h.md#commonevent_errcode)表示IPC请求发送失败。  返回[COMMONEVENT\_ERR\_INIT\_UNDONE](capi-oh-commonevent-h.md#commonevent_errcode)表示公共事件服务未初始化。 |

### OH\_CommonEvent\_IsOrderedCommonEvent()

```c
bool OH_CommonEvent_IsOrderedCommonEvent(const CommonEvent_Subscriber* subscriber)
```

**描述**

查询当前公共事件是否为有序公共事件。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Subscriber](capi-oh-commonevent-h.md#变量)\* subscriber | 公共事件的订阅者对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示有序公共事件；返回false表示无序公共事件。 |

### OH\_CommonEvent\_FinishCommonEvent()

```c
bool OH_CommonEvent_FinishCommonEvent(CommonEvent_Subscriber* subscriber)
```

**描述**

用于订阅者结束对当前有序公共事件的处理。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Subscriber](capi-oh-commonevent-h.md#变量)\* subscriber | 公共事件的订阅者对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示操作成功；返回false表示操作失败。 |

### OH\_CommonEvent\_GetAbortCommonEvent()

```c
bool OH_CommonEvent_GetAbortCommonEvent(const CommonEvent_Subscriber* subscriber)
```

**描述**

获取当前有序公共事件是否处于中止状态。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Subscriber](capi-oh-commonevent-h.md#变量)\* subscriber | 公共事件的订阅者对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示当前有序公共事件处于中止状态；返回false表示当前有序公共事件没有处于中止状态。 |

### OH\_CommonEvent\_AbortCommonEvent()

```c
bool OH_CommonEvent_AbortCommonEvent(CommonEvent_Subscriber* subscriber)
```

**描述**

该接口与[OH\_CommonEvent\_FinishCommonEvent](capi-oh-commonevent-h.md#oh_commonevent_finishcommonevent)配合使用，可以中止当前的有序公共事件，使该公共事件不再向下一个订阅者传递。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Subscriber](capi-oh-commonevent-h.md#变量)\* subscriber | 公共事件的订阅者对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示操作成功；返回false表示操作失败。 |

### OH\_CommonEvent\_ClearAbortCommonEvent()

```c
bool OH_CommonEvent_ClearAbortCommonEvent(CommonEvent_Subscriber* subscriber)
```

**描述**

该接口与[OH\_CommonEvent\_FinishCommonEvent](capi-oh-commonevent-h.md#oh_commonevent_finishcommonevent)配合使用，可以取消当前有序公共事件的中止状态，使该公共事件继续向下一个订阅者传递。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Subscriber](capi-oh-commonevent-h.md#变量)\* subscriber | 公共事件的订阅者对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示操作成功；返回false表示操作失败。 |

### OH\_CommonEvent\_GetCodeFromSubscriber()

```c
int32_t OH_CommonEvent_GetCodeFromSubscriber(const CommonEvent_Subscriber* subscriber)
```

**描述**

获取有序公共事件传递的数据，整数类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Subscriber](capi-oh-commonevent-h.md#变量)\* subscriber | 公共事件的订阅者对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| int32\_t | 返回有序公共事件传递的数据，整数类型，无法获取时返回0。 |

### OH\_CommonEvent\_SetCodeToSubscriber()

```c
bool OH_CommonEvent_SetCodeToSubscriber(CommonEvent_Subscriber* subscriber, int32_t code)
```

**描述**

设置有序公共事件传递的数据，整数类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Subscriber](capi-oh-commonevent-h.md#变量)\* subscriber | 公共事件的订阅者对象。 |
| int32\_t code | 有序公共事件传递的数据，整数类型。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示操作成功；返回false表示操作失败。 |

### OH\_CommonEvent\_GetDataFromSubscriber()

```c
const char* OH_CommonEvent_GetDataFromSubscriber(const CommonEvent_Subscriber* subscriber)
```

**描述**

获取有序公共事件传递的数据，字符串类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| const [CommonEvent\_Subscriber](capi-oh-commonevent-h.md#变量)\* subscriber | 公共事件的订阅者对象。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| const char\* | 返回有序公共事件传递的数据，字符串类型，无法获取时返回NULL。 |

### OH\_CommonEvent\_SetDataToSubscriber()

```c
bool OH_CommonEvent_SetDataToSubscriber(CommonEvent_Subscriber* subscriber, const char* data, size_t length)
```

**描述**

设置有序公共事件传递的数据，字符串类型。

**起始版本：** 18

**参数：**

| 参数项 | 描述 |
| --- | --- |
| [CommonEvent\_Subscriber](capi-oh-commonevent-h.md#变量)\* subscriber | 公共事件的订阅者对象。 |
| const char\* data | 有序公共事件传递的数据，字符串类型，实际有效数据长度为length与data字符串长度的最小值。 |
| size\_t length | 传递的数据字节长度，取值为data字符串长度。 |

**返回：**

| 类型 | 说明 |
| --- | --- |
| bool | 返回true表示操作成功；返回false表示操作失败。 |
