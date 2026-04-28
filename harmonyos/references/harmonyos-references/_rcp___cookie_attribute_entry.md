---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/_rcp___cookie_attribute_entry
title: Rcp_CookieAttributeEntry
breadcrumb: API参考 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > C API > 结构体 > Rcp_CookieAttributeEntry
category: harmonyos-references
scraped_at: 2026-04-28T08:09:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e126a4b913567f8ee41ac9576e9853a93acbe3f2f4d8e47d505e1364c4d9ce21
---

## 概述

PhonePC/2in1TabletTVWearable

响应Cookie属性条目。

**起始版本：** 5.0.0(12)

**相关模块：** [RemoteCommunication](remote-communication-overview.md)

**所在头文件：** [rcp.h](rcp_8h.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 成员变量

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| const char \* [key](_rcp___cookie_attribute_entry.md#key) | 键。 |
| const char \* [value](_rcp___cookie_attribute_entry.md#value) | 值。 |
| struct [Rcp\_CookieAttributeEntry](_rcp___cookie_attribute_entry.md) \* [next](_rcp___cookie_attribute_entry.md#next) | 链式存储。指向下一个[Rcp\_CookieAttributeEntry](_rcp___cookie_attribute_entry.md)的指针。 |

## 结构体成员变量说明

PhonePC/2in1TabletTVWearable

### key

PhonePC/2in1TabletTVWearable

```
1. const char* Rcp_CookieAttributeEntry::key
```

**描述**

键。

### next

PhonePC/2in1TabletTVWearable

```
1. struct Rcp_CookieAttributeEntry* Rcp_CookieAttributeEntry::next
```

**描述**

链式存储。指向下一个[Rcp\_CookieAttributeEntry](_rcp___cookie_attribute_entry.md)的指针。

### value

PhonePC/2in1TabletTVWearable

```
1. const char* Rcp_CookieAttributeEntry::value
```

**描述**

值。
