---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-jsvm-jsvm-createvmoptions
title: JSVM_CreateVMOptions
breadcrumb: API参考 > 公共基础能力 > C API > 结构体 > JSVM_CreateVMOptions
category: harmonyos-references
scraped_at: 2026-09-02T15:03:14+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:02c5a5b44cf4462f2a13d85188b92f8a2cd020157e311de69cfacf9743e59280
---

```c
typedef struct {...} JSVM_CreateVMOptions
```

## 概述

创建JavaScript虚拟机的选项。

**使用场景：** 需要自定义JavaScript虚拟机内存配置的应用，需要使用快照功能加速虚拟机启动的场景，对虚拟机内存使用有特殊要求的嵌入式或资源受限环境。

**系统能力：** SystemCapability.ArkCompiler.JSVM

**起始版本：** 11

**相关模块：** [JSVM](capi-jsvm.md)

**所在头文件：** [jsvm\_types.h](capi-jsvm-types-h.md)

## 汇总

### 成员变量

| 名称 | 描述 |
| --- | --- |
| size\_t maxOldGenerationSize | 老年代内存大小上限。 |
| size\_t maxYoungGenerationSize | 年轻代内存大小上限。 |
| size\_t initialOldGenerationSize | 老年代内存大小初始值。 |
| size\_t initialYoungGenerationSize | 年轻代内存大小初始值。 |
| const char\* snapshotBlobData | 启动快照数据。 |
| size\_t snapshotBlobSize | 启动快照数据的大小。 |
| bool isForSnapshotting | 虚拟机是否用于创建快照，为true，则虚拟机用于创建快照，为false，则虚拟机不用于创建快照。 |
