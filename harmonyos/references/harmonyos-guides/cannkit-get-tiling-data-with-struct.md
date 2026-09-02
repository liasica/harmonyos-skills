---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-get-tiling-data-with-struct
title: GET_TILING_DATA_WITH_STRUCT
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > Kernel Tiling > GET_TILING_DATA_WITH_STRUCT
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:355142ba01ebe69e5824d8b37b9f80fb740649c75b7cea372e8b0fc8ffdbe46b
---

## 函数功能

使用该接口指定结构体名称，可获取指定的tiling信息，并填入对应的Tiling结构体中，此函数会以宏展开的方式进行编译。与[GET\_TILING\_DATA](cannkit-get-tiling-data.md)的区别是：只能获取默认注册的结构体，该接口可以根据指定的结构体名称获取对应的结构体，常用于针对不同的TilingKey注册了不同结构体的情况下。

## 函数原型

```cpp
GET_TILING_DATA_WITH_STRUCT(struct_name, tiling_data, tiling_arg)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| struct\_name | 输入 | 指定的结构体名称。 |
| tiling\_data | 输出 | 返回指定Tiling结构体变量。 |
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
    KernelAdd op;
    if (TILING_KEY_IS(1)) {
        GET_TILING_DATA_WITH_STRUCT(Add_Struct_Special, tilingData, tiling); // 使用算子指定注册的结构体
    op.Init(x, y, z, tilingData.totalLengthSpecial, tilingData.tileNumSpecial);
    } else {
        GET_TILING_DATA(tilingData, tiling); // 使用算子默认注册的结构体
    op.Init(x, y, z, tilingData.totalLength, tilingData.tileNum);
    }
    if (TILING_KEY_IS(1)) {
        op.Process();
    }  else  if (TILING_KEY_IS(2)) {
        op.Process();
    } else  if (TILING_KEY_IS(3)) {
        op.Process();
    }
}
```
