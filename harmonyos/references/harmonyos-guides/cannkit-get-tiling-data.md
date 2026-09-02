---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-get-tiling-data
title: GET_TILING_DATA
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > Kernel Tiling > GET_TILING_DATA
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:17e3e7e34f817882848117254ba9be52e34a2aec18b91436acdc571b9df431cc
---

## 函数功能

用于获取算子kernel入口函数传入的tiling信息，并填入注册的Tiling结构体中，此函数会以宏展开的方式进行编译。对应的算子host实现中需要定义TilingData结构体，实现并注册计算TilingData的Tiling函数，具体请参考[Host侧tiling实现](cannkit-tiling-implementation-on-the-host.md)。如果开发者通过[TilingData结构注册](cannkit-tilingdata-structure-registration.md)注册了多个TilingData结构体，使用该接口返回默认注册的结构体。

## 函数原型

```cpp
GET_TILING_DATA(tiling_data, tiling_arg)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| tiling\_data | 输出 | 返回默认Tiling结构体变量。 |
| tiling\_arg | 输入 | 此参数为算子入口函数处传入的tiling参数。 |

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 约束说明

* 本函数需在算子kernel代码处使用，并且传入的tiling\_data参数不需要声明类型。
* 暂不支持kernel直调工程。

## 调用示例

```cpp
extern "C" __global__ __aicore__ void add_custom(__gm__ uint8_t *x, __gm__ uint8_t *y, __gm__ uint8_t *z, __gm__ uint8_t *tiling)
{
    GET_TILING_DATA(tilingData, tiling);
    KernelAdd op;
    op.Init(x, y, z, tilingData.blkDim, tilingData.totalSize, tilingData.splitTile);
    op.Process();
}
```
