---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-usbddk-usbrequestpipe
title: UsbRequestPipe
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbRequestPipe
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:77b1c72b7a567178ceeb9fec9d490db476fbb2286f0cf1940a471f0529641ebe
---

```c
typedef struct UsbRequestPipe {...} __attribute__((aligned(8))) UsbRequestPipe
```

## 概述

请求管道，是USB数据传输请求的抽象，用于描述USB数据传输的基本配置参数，包括接口句柄、端点地址和超时时间。适用于需要进行USB数据传输的场景。

**起始版本：** 10

**相关模块：** [UsbDdk](capi-usbddk.md)

**所在头文件：** [usb\_ddk\_types.h](capi-usb-ddk-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint64\_t interfaceHandle | 接口操作句柄，用于标识USB设备上的接口，由[OH\_Usb\_ClaimInterface](capi-usb-ddk-api-h.md#oh_usb_claiminterface)接口获取。 |
| uint32\_t timeout | 超时时间，单位：ms。值为0表示等待直到操作完成；非0值表示在指定毫秒数内未完成则超时。 |
| uint8\_t endpoint | 要通信的端点的地址。 |
