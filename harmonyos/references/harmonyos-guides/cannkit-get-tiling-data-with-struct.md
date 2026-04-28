---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-get-tiling-data-with-struct
title: GET_TILING_DATA_WITH_STRUCT
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > Kernel Tiling > GET_TILING_DATA_WITH_STRUCT
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:46e69a7df61b0f7570203a51ec9cf49623a10e07d75adeab22c16474b7096d8a
---

## 函数功能

使用该接口指定结构体名称，可获取指定的tiling信息，并填入对应的Tiling结构体中，此函数会以宏展开的方式进行编译。与[GET\_TILING\_DATA](cannkit-get-tiling-data.md)的区别是：只能获取默认注册的结构体，该接口可以根据指定的结构体名称获取对应的结构体，常用于针对不同的TilingKey注册了不同结构体的情况下。

## 函数原型

```
1. GET_TILING_DATA_WITH_STRUCT(struct_name, tiling_data, tiling_arg)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| struct\_name | 输入 | 指定的结构体名称。 |
| tiling\_data | 输出 | 返回指定Tiling结构体变量。 |
| tiling\_arg | 输入 | 此参数为算子入口函数处传入的tiling参数。 |

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 约束说明

* 本函数需在算子kernel代码处使用，并且传入的tiling\_data参数不需要声明类型。
* 暂不支持kernel直调工程。

## 调用示例

```
1. extern "C" __global__ __aicore__ void add_custom(__gm__ uint8_t *x, __gm__ uint8_t *y, __gm__ uint8_t *z, __gm__ uint8_t *tiling)
2. {
3. KernelAdd op;
4. if (TILING_KEY_IS(1)) {
5. GET_TILING_DATA_WITH_STRUCT(Add_Struct_Special, tilingData, tiling); // 使用算子指定注册的结构体
6. op.Init(x, y, z, tilingData.totalLengthSpecial, tilingData.tileNumSpecial);
7. } else {
8. GET_TILING_DATA(tilingData, tiling);   // 使用算子默认注册的结构体
9. op.Init(x, y, z, tilingData.totalLength, tilingData.tileNum);
10. }
11. if (TILING_KEY_IS(1)) {
12. op.Process();
13. }  else  if (TILING_KEY_IS(2)) {
14. op.Process();
15. } else  if (TILING_KEY_IS(3)) {
16. op.Process();
17. }
18. }
```
