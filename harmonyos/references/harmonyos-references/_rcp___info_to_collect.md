---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___info_to_collect
title: Rcp_InfoToCollect
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_InfoToCollect
category: harmonyos-references
scraped_at: 2026-04-28T08:09:04+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:41a023880ec689d3ed24f04c351a0c7aafa5e7c62f148d1abafbb53b362dd554
---

## 概述

PhonePC/2in1TabletTVWearable

指定要收集的请求处理事件。可以通过响应对象检查收集的事件。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| bool [textual](_rcp___info_to_collect.md#textual) | 是否收集未分类的文本事件。默认值为false。 |
| bool [incomingHeader](_rcp___info_to_collect.md#incomingheader) | 是否收集传入HTTP标头事件。默认值为false。 |
| bool [outgoingHeader](_rcp___info_to_collect.md#outgoingheader) | 是否收集传出HTTP标头事件。默认值为false。 |
| bool [incomingData](_rcp___info_to_collect.md#incomingdata) | 是否收集有关传入HTTP数据的事件。默认值为false。 |
| bool [outgoingData](_rcp___info_to_collect.md#outgoingdata) | 是否收集有关传出HTTP数据的事件。默认值为false。 |
| bool [incomingSslData](_rcp___info_to_collect.md#incomingssldata) | 是否收集传入的SSL/TLS事件。默认值为false。 |
| bool [outgoingSslData](_rcp___info_to_collect.md#outgoingssldata) | 是否收集传出的SSL/TLS事件。默认值为false。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### incomingData

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_InfoToCollect::incomingData
```

**描述**

是否收集有关传入HTTP数据的事件。默认值为false。

### incomingHeader

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_InfoToCollect::incomingHeader
```

**描述**

是否收集传入HTTP标头事件。默认值为false。

### incomingSslData

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_InfoToCollect::incomingSslData
```

**描述**

是否收集传入的SSL/TLS事件。默认值为false。

### outgoingData

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_InfoToCollect::outgoingData
```

**描述**

是否收集有关传出HTTP数据的事件。默认值为false。

### outgoingHeader

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_InfoToCollect::outgoingHeader
```

**描述**

是否收集传出HTTP标头事件。默认值为false。

### outgoingSslData

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_InfoToCollect::outgoingSslData
```

**描述**

是否收集传出的SSL/TLS事件。默认值为false。

### textual

PhonePC/2in1TabletTVWearable

```
1. bool Rcp_InfoToCollect::textual
```

**描述**

是否收集未分类的文本事件。默认值为false。
