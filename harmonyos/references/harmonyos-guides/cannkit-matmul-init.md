---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-matmul-init
title: Init
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 高阶API > 矩阵相乘 > Matmul > Init
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:8734c27ff022ca7666faeec99423ee9f0fefc2cae0f77cc219032014554c2bb2
---

## 功能说明

Init主要用于对Matmul对象中的Tiling数据进行初始化，根据Tiling参数进行资源划分，tiling参数的具体介绍请参考[Matmul Tiling](cannkit-matmul-tiling-usage-description.md)。

开发者可以先通过REGIST\_MATMUL\_OBJ初始化单个Matmul对象，不传入tiling参数，后续通过Init接口单独传入Tiling参数，对Tiling数据进行调整。比如，Tiling参数可变的场景下，可以通过多次调用Init来重新设置Tiling参数。

不需要Tiling变更的场景下，推荐使用REGIST\_MATMUL\_OBJ传入tiling参数进行初始化。

## 函数原型

```cpp
__aicore__ inline void Init(const TCubeTiling* __restrict cubeTiling, TPipe* tpipe = nullptr)
```

## 参数说明

**表1** 接口参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| cubeTiling | 输入 | Matmul tiling参数，TCubeTiling结构体定义请参见[TCubeTiling结构体](cannkit-tcubetiling-structure.md)表1。  Tiling参数可以通过host侧GetTiling接口获取，并传递到kernel侧使用。 |
| tpipe | 输入 | Tpipe对象。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

## 注意事项

无

## 调用示例

```cpp
// 开发者可以先通过REGIST_MATMUL_OBJ初始化单个matmul对象，不传入tiling参数，后续通过Init接口单独传入Tiling参数，对Tiling数据进行调整。
REGIST_MATMUL_OBJ(&pipe, GetSysWorkSpacePtr(), mm);
mm.Init(&tiling);
```
