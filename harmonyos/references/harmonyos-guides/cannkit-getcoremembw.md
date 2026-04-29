---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcoremembw
title: GetCoreMemBw
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 平台信息获取PlatformAscendC > GetCoreMemBw
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bbb3ebc51c9bb5a7f28a95eb3fddd986c5ea6e1e0652170f795fd0b1341c1584
---

## 函数功能

获取硬件平台存储空间的带宽大小，仅支持L2、HBM。硬件存储空间类型定义如下。

```
1. enum class CoreMemType {
2. L0_A = 0,
3. L0_B = 1,
4. L0_C = 2,
5. L1 = 3,
6. L2 = 4,
7. UB = 5,
8. HBM = 6,
9. RESERVED
10. };
```

## 函数原型

```
1. void GetCoreMemBw(const CoreMemType &memType, uint64_t &bwSize) const;
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| memType | 输入 | 硬件存储空间类型。 |
| bwSize | 输出 | 对应硬件的存储空间的带宽大小。单位是Byte/cycle，cycle代表时钟周期。 |

## 返回值

无

## 约束说明

memType输入仅支持L2、HBM。

## 调用示例

```
1. ge::graphStatus TilingXXX(gert::TilingContext* context) {
2. auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
3. uint64_t l2_bw;
4. ascendcPlatform.GetCoreMemBw(platform_ascendc::CoreMemType::L2, l2_bw);
5. // ...
6. return ret;
7. }
```
