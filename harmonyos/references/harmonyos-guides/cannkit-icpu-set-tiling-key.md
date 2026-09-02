---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-icpu-set-tiling-key
title: ICPU_SET_TILING_KEY
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 算子调测API > ICPU_SET_TILING_KEY
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:38+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:585d37a55434e7229bcc91ea3cd14b17040cc369c557ffedd24e7f5842a2dbe0
---

## 函数功能

用于指定本次CPU调测使用的tilingKey。调测执行时，将只执行算子核函数中该tilingKey对应的分支。

## 函数原型

```cpp
ICPU_SET_TILING_KEY(tilingKey)
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| tilingKey | 输入 | 指定本次CPU调测使用的tilingKey，参数类型为int32\_t。 |

## 返回值

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 约束说明

* 未使用该接口设置tilingKey的情况下，tilingKey将会为默认值0，在调测执行时，会有告警提示Tiling Key是0，并继续进行调测。如果核函数中有tilingKey分支，将会执行tilingKey为0的分支，其他tilingKey对应的分支不会执行。
* tilingKey建议传入正整数，如果设置为负数或者0，将会告警并继续调测。如果传入0，将会执行tilingKey为0的分支；tilingKey传入负数，将导致未定义的行为。
* 该接口需要在ICPU\_RUN\_KF前调用。

## 调用示例

```cpp
ICPU_SET_TILING_KEY(10086)
ICPU_RUN_KF(sort_kernel0, coreNum, (uint8_t*)x, (uint8_t*)y);
```
