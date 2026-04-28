---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-scalarcast
title: ScalarCast
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 标量计算 > ScalarCast
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:39+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6289f635afba640a0de40c5916c5f468f45403f76567101231045e4958d5e6f9
---

## 功能说明

将一个scalar的类型转换为指定的类型。

## 函数原型

```
1. template <typename srcT, typename dstT, RoundMode roundMode>
2. __aicore__ inline dstT ScalarCast(srcT valueIn)
```

## 参数说明

**表1** 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| valueIn | 输入 | 被转换数据类型的scalar。 |
| srcT | 输入 | valueIn的数据类型，支持float。 |
| dstT | 输入 | 转换后的数据类型，支持half、int32\_t。 |
| roundMode | 输入 | 精度转换处理模式，类型是RoundMode。  RoundMode为枚举类型，用以控制精度转换处理模式，具体取值为：CAST\_NONE、CAST\_RINT、CAST\_FLOOR、CAST\_FLOOR、CAST\_ROUND、CAST\_TRUNC、CAST\_ODD。  对于ScalarCast，转换类型仅支持float转half(f32tof16)与float转int32\_t(f32tos32)，相应支持的RoundMode如下。  - f32tof16：CAST\_ODD  - f32tos32：CAST\_ROUND、CAST\_CEIL、CAST\_FLOOR、CAST\_RINT  ScalarCast的精度转换规则与Cast保持一致，具体可参考[Cast函数功能](cannkit-precision-conversion-instruction.md#函数功能)下的表1。 |

## 返回值

dstT类型的valueIn。

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 约束说明

无。

## 调用示例

```
1. float valueIn = 2.5;
2. // 输出数据(valueOut): 3
3. int32_t valueOut = AscendC::ScalarCast<float, int32_t, AscendC::RoundMode::CAST_ROUND>(valueIn);
```
