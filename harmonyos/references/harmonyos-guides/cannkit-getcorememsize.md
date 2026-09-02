---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcorememsize
title: GetCoreMemSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 平台信息获取PlatformAscendC > GetCoreMemSize
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f287255737f809b092319f759d17e60a5243e0b9d9d0433e486aa94b9889a34e
---

## 函数功能

获取硬件平台存储空间的内存大小，例如L1、L0\_A、L0\_B、L2等，支持的存储空间类型定义如下。

```cpp
enum class CoreMemType {
L0_A = 0,
L0_B = 1,
L0_C = 2,
L1 = 3,
L2 = 4,
UB = 5,
HBM = 6,
RESERVED
};
```

## 函数原型

```cpp
void GetCoreMemSize(const CoreMemType &memType, uint64_t &size) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| memType | 输入 | 硬件存储空间类型。 |
| size | 输出 | 对应类型的存储空间大小，单位：字节。 |

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
ge::graphStatus TilingXXX(gert::TilingContext* context) {
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
    uint64_t ub_size, l1_size;
    ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, ub_size);
    ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::L1, l1_size);
    // ...
    return ret;
}
```
