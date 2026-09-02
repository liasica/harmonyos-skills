---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbcontrolrequestsetup
title: UsbControlRequestSetup
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbControlRequestSetup
category: harmonyos-references
scraped_at: 2026-09-02T15:02:12+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:50b61d3ff95a6c70ecf6c47fbe2284311b3ef4af6dd77868272cce79437c1f74
---

```c
typedef struct UsbControlRequestSetup {...} __attribute__((aligned(8))) UsbControlRequestSetup
```

## 概述

控制传输setup包，对应USB协议中的Setup Data。

**起始版本：** 10

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint8\_t bmRequestType | 请求类型。 |
| uint8\_t bRequest | 具体的请求。 |
| uint16\_t wValue | 具体的请求不同，其代表的含义不一样。 |
| uint16\_t wIndex | 具体的请求不同，其代表的含义不一样，通常用来传递索引或者偏移量。 |
| uint16\_t wLength | 如果有数据阶段的传输，其代表传输的字节个数。 |
