---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-serialddk-usbserial-params
title: UsbSerial_Params
breadcrumb: API参考 > 系统 > 硬件 > Driver Development Kit（驱动开发服务） > C API > 结构体 > UsbSerial_Params
category: harmonyos-references
scraped_at: 2026-09-02T15:02:13+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:74da02c0e39d16675708407c1b1b02222511ad9c2c2d7d37fe5d996d96fa792e
---

```c
typedef struct UsbSerial_Params {...} __attribute__((aligned(8))) UsbSerial_Params
```

## 概述

定义USB Serial DDK使用的USB串口参数，用于USB转串口设备的通信参数配置，需与目标通信设备的配置保持一致，否则可能无法正常通信。常见于工业控制设备、调试工具、传感器数据采集等需要通过USB串口与设备通信的场景。

**起始版本：** 18

**相关模块：** [USBSerialDDK](capi-serialddk.md)

**所在头文件：** [usb\_serial\_types.h](capi-usb-serial-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| uint32\_t baudRate | 波特率，单位：波特。 |
| uint8\_t nDataBits | 数据位比特数。 |
| uint8\_t nStopBits | 停止位比特数。 |
| uint8\_t parity | 校验参数设置（0：无校验；1：奇校验；2：偶校验）。 |
