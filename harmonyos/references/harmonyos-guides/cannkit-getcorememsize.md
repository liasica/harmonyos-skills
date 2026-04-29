---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getcorememsize
title: GetCoreMemSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > Host API > 平台信息获取PlatformAscendC > GetCoreMemSize
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a527dca2e0829abe35ebc5884e82d8265d84bee5c94ddff394643c2af9d33a9d
---

## 函数功能

获取硬件平台存储空间的内存大小，例如L1、L0\_A、L0\_B、L2等，支持的存储空间类型定义如下。

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
1. void GetCoreMemSize(const CoreMemType &memType, uint64_t &size) const;
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

```
1. ge::graphStatus TilingXXX(gert::TilingContext* context) {
2. auto ascendcPlatform = platform_ascendc::PlatformAscendC(context->GetPlatformInfo());
3. uint64_t ub_size, l1_size;
4. ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::UB, ub_size);
5. ascendcPlatform.GetCoreMemSize(platform_ascendc::CoreMemType::L1, l1_size);
6. // ...
7. return ret;
8. }
```
