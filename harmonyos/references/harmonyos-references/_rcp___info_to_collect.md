---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___info_to_collect
title: Rcp_InfoToCollect
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_InfoToCollect
category: harmonyos-references
scraped_at: 2026-09-02T15:01:59+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8ef5f9b102216c37df10487802f4a071a3bf720e5bfe252fec673db8fa17e1cc
---

## 概述

指定要收集的请求处理事件。可以通过响应对象检查收集的事件。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| bool [textual](_rcp___info_to_collect.md#textual) | 是否收集文本信息事件。true表示收集文本信息事件，false表示不收集文本信息事件。默认值为false。 |
| bool [incomingHeader](_rcp___info_to_collect.md#incomingheader) | 是否收集传入的header信息事件。true表示收集传入的header信息事件，false表示不收集传入的header信息事件。默认值为false。 |
| bool [outgoingHeader](_rcp___info_to_collect.md#outgoingheader) | 是否收集传出的header信息事件。true表示收集传出的header信息事件，false表示不收集传出的header信息事件。默认值为false。 |
| bool [incomingData](_rcp___info_to_collect.md#incomingdata) | 是否收集传入的数据信息事件。true表示收集传入的数据信息事件，false表示不收集传入的数据信息事件。默认值为false。 |
| bool [outgoingData](_rcp___info_to_collect.md#outgoingdata) | 是否收集传出的数据信息事件。true表示收集传出的数据信息事件，false表示不收集传出的数据信息事件。默认值为false。 |
| bool [incomingSslData](_rcp___info_to_collect.md#incomingssldata) | 是否收集传入的SSL/TLS数据信息事件。true表示收集传入的SSL/TLS数据信息事件，false表示不收集传入的SSL/TLS数据信息事件。默认值为false。 |
| bool [outgoingSslData](_rcp___info_to_collect.md#outgoingssldata) | 是否收集传出的SSL/TLS数据信息事件。true表示收集传出的SSL/TLS数据信息事件，false表示不收集传出的SSL/TLS数据信息事件。默认值为false。 |

## 结构体成员变量说明

### incomingData

```cpp
bool Rcp_InfoToCollect::incomingData
```

**描述**

是否收集传入的数据信息事件。true表示收集传入的数据信息事件，false表示不收集传入的数据信息事件。默认值为false。

### incomingHeader

```cpp
bool Rcp_InfoToCollect::incomingHeader
```

**描述**

是否收集传入HTTP标头事件。true表示收集传入的header信息事件，false表示不收集传入的header信息事件。默认值为false。

### incomingSslData

```cpp
bool Rcp_InfoToCollect::incomingSslData
```

**描述**

是否收集传入的SSL/TLS数据信息事件。true表示收集传入的SSL/TLS数据信息事件，false表示不收集传入的SSL/TLS数据信息事件。默认值为false。

### outgoingData

```cpp
bool Rcp_InfoToCollect::outgoingData
```

**描述**

是否收集传出的数据信息事件。true表示收集传出的数据信息事件，false表示不收集传出的数据信息事件。默认值为false。

### outgoingHeader

```cpp
bool Rcp_InfoToCollect::outgoingHeader
```

**描述**

是否收集传出的header信息事件。true表示收集传出的header信息事件，false表示不收集传出的header信息事件。默认值为false。

### outgoingSslData

```cpp
bool Rcp_InfoToCollect::outgoingSslData
```

**描述**

是否收集传出的SSL/TLS数据信息事件。true表示收集传出的SSL/TLS数据信息事件，false表示不收集传出的SSL/TLS数据信息事件。默认值为false。

### textual

```cpp
bool Rcp_InfoToCollect::textual
```

**描述**

是否收集文本信息事件。true表示收集文本信息事件，false表示不收集文本信息事件。默认值为false。
