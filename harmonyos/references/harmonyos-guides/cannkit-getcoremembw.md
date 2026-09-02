---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcoremembw
title: GetCoreMemBw
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 平台信息获取PlatformAscendC > GetCoreMemBw
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-08-07
content_hash: sha256:6633efead7c081660346d091e96aec44688c752192e9790f9b6297b69075fe08
---

## 函数功能

获取硬件平台存储空间的带宽大小，仅支持L2、HBM。硬件存储空间类型定义如下。

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
void GetCoreMemBw(const CoreMemType &memType, uint64_t &bwSize) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| memType | 输入 | 硬件存储空间类型，仅支持L2、HBM。 |
| bwSize | 输出 | 对应硬件的存储空间的带宽大小。单位是Byte/cycle，cycle代表时钟周期。 |

## 返回值

无

## 约束说明

memType输入仅支持L2、HBM。

## 调用示例

```cpp
ge::graphStatus TilingXXX(gert::TilingContext* context) {
    auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
    uint64_t l2_bw;
    ascendcPlatform.GetCoreMemBw(platform_ascendc::CoreMemType::L2, l2_bw);
    // ...
    return ret;
}
```
