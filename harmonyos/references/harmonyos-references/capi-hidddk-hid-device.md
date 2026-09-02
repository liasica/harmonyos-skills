---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-hidddk-hid-device
title: Hid_Device
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > Hid_Device
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c1dd698d90d3b319f3b8a9bc22a9f142f943107c1ae3dda285c7d8aad49bfc28
---

```c
typedef struct Hid_Device {...} Hid_Device
```

## 概述

设备基本信息，用于表示HID设备的名称、厂商ID、产品ID等基本属性，在创建和操作HID设备时作为设备标识使用。

**起始版本：** 11

**相关模块：** [HidDdk](capi-hidddk.md)

**所在头文件：** [hid\_ddk\_types.h](capi-hid-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| const char\* deviceName | 设备名称，最大长度128字符，不能为NULL。超出长度或为NULL时返回错误。 |
| uint16\_t vendorId | 厂商ID。 |
| uint16\_t productId | 产品ID。 |
| uint16\_t version | 版本号。 |
| uint16\_t bustype | 总线类型，取值含义参考标准HID协议的总线类型定义。 |
| Hid\_DeviceProp\* properties | 设备特性。使用前应检查指针是否为空；该指针仅在Hid\_Device对象有效期间有效，不应手动释放。 |
| uint16\_t propLength | 设备特性数量，表示properties数组的有效元素个数。注意：遍历数组时应以该值为边界条件；该值可能为0。 |
