---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-serialddk-usbserial-params
title: UsbSerial_Params
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbSerial_Params
category: harmonyos-references
scraped_at: 2026-04-28T08:10:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2b074a519ed379028eae16209e53b6dc2f29647639ab5c4f3c09a9781584b900
---

```
1. typedef struct UsbSerial_Params {...} __attribute__((aligned(8))) UsbSerial_Params
```

## 概述

PC/2in1

定义USB Serial DDK使用的USB串口参数.

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
