---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-createvmoptions
title: JSVM_CreateVMOptions
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_CreateVMOptions
category: harmonyos-references
scraped_at: 2026-04-28T08:19:24+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:0c272a1930376cdf6fde3b2c7122961a53435431feee79b4824216c77d08f86c
---

```
1. typedef struct {...} JSVM_CreateVMOptions
```

## 概述

PhonePC/2in1TabletWearable

创建JavaScript虚拟机的选项。

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

PhonePC/2in1TabletWearable

### 成员变量

PhonePC/2in1TabletWearable

| 名称 | 描述 |
| --- | --- |
| size\_t maxOldGenerationSize | 老年代内存大小上限。 |
| size\_t maxYoungGenerationSize | 年轻代内存大小上限。 |
| size\_t initialOldGenerationSize | 老年代内存大小初始值。 |
| size\_t initialYoungGenerationSize | 年轻代内存大小初始值。 |
| const char\* snapshotBlobData | 启动快照数据。 |
| size\_t snapshotBlobSize | 启动快照数据的大小。 |
| bool isForSnapshotting | 虚拟机是否用于创建快照，为true，则虚拟机用于创建快照，为false，则虚拟机不用于创建快照。 |
