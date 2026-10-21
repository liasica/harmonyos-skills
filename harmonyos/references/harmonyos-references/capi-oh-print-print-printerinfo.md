---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-oh-print-print-printerinfo
title: Print_PrinterInfo
breadcrumb: API参考 > 系统 > 基础功能 > Basic Services Kit（基础服务） > C API > 结构体 > Print_PrinterInfo
category: harmonyos-references
scraped_at: 2026-10-22T07:09:23+08:00
doc_updated_at: 2026-10-21
content_hash: sha256:5a8106d6a5452311596aafc2dfd162d7ac279709495aa3991e3b85732cf63cd8
---

```cpp
typedef struct {...} Print_PrinterInfo
```

## 概述

Print\_PrinterInfo表示打印机信息，包含打印机的状态、能力、默认属性以及标识信息（如打印机ID、名称、描述、位置、品牌型号、URI等），适用于应用在打印场景中获取和展示打印机详细信息的场景，帮助开发者根据打印机能力与属性选择合适的打印设备。可通过 [OH\_Print\_StartPrinterDiscovery](capi-ohprint-h.md#oh_print_startprinterdiscovery) 或 [OH\_Print\_QueryPrinterInfo](capi-ohprint-h.md#oh_print_queryprinterinfo) 获取。

**起始版本：** 12

**相关模块：** [OH\_Print](capi-oh-print.md)

**所在头文件：** [ohprint.h](capi-ohprint-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| [Print\_PrinterState](capi-ohprint-h.md#print_printerstate) printerState | 打印机的当前运行状态。 |
| [Print\_PrinterCapability](capi-oh-print-print-printercapability.md) capability | 打印机支持的能力集合，如支持的纸张尺寸、色彩模式等。 |
| [Print\_DefaultValue](capi-oh-print-print-defaultvalue.md) defaultValue | 打印机默认属性，如默认纸张尺寸、色彩模式等。 |
| bool isDefaultPrinter | 是否为默认打印机。true表示是默认打印机，false表示不是默认打印机。 |
| char \*printerId | 打印机ID。 |
| char \*printerName | 打印机名称。 |
| char \*description | 打印机描述。 |
| char \*location | 打印机位置。 |
| char \*makeAndModel | 打印机品牌和型号信息。 |
| char \*printerUri | 打印机URI，用于定位和访问打印机。格式形如scheme://[user@]host[:port]/resource。 |
| char \*detailInfo | JSON格式的详细信息。  支持的键包括：  - **printerAlias**：string类型，表示打印机别名，**起始版本：** 24。  - **vendorId**：int类型，表示USB打印机的VID，取值范围 [0, 65535]，**起始版本：** 12。  - **productId**：int类型，表示USB打印机的PID，取值范围 [0, 65535]，**起始版本：** 12。  - **protocol**：string数组，表示探测到的打印机支持的协议列表，取值包括ipp、ipps、lpd、socket，**起始版本：** 24。  - **ipp**：string类型，表示探测到的IPP协议对应的打印机URI，**起始版本：** 24。  - **ipps**：string类型，表示探测到的IPPS协议对应的打印机URI，**起始版本：** 24。  - **lpd**：string类型，表示探测到的LPD协议对应的打印机URI，**起始版本：** 24。  - **socket**：string类型，表示探测到的Socket协议对应的打印机URI，**起始版本：** 24。 |
