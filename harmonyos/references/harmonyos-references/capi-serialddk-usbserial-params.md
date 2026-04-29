---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-serialddk-usbserial-params
title: UsbSerial_Params
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbSerial_Params
category: harmonyos-references
scraped_at: 2026-04-29T14:01:33+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:c2a67c64a8674b863a7544a3d2682ea4ee9e3384081f4424ce759af1975b118d
---

```
1. typedef struct UsbSerial_Params {...} __attribute__((aligned(8))) UsbSerial_Params
```

## 概述

PC/2in1

定义USB Serial DDK使用的USB串口参数。

**起始版本：** 18

**相关模块：** [USBSerialDDK](capi-serialddk.md)

**所在头文件：** [usb\_serial\_types.h](capi-usb-serial-types-h.md)

## 汇总

PC/2in1

### 成员变量

PC/2in1

| 名称 | 描述 |
| --- | --- |
| uint32\_t baudRate | 波特率，单位为波特。 |
| uint8\_t nDataBits | 数据位比特数。 |
| uint8\_t nStopBits | 停止位比特数。 |
| uint8\_t parity | 校验参数设置（0：无校验；1：奇校验；2：偶校验；3：1校验；4：0校验；）。 |
