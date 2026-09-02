---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tiling-key-is
title: TILING_KEY_IS
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > Kernel Tiling > TILING_KEY_IS
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:6c39260b86830efc35f51ffd6cbd380e8bc0eaf9ddf52fcc0a2c27f2babc7b79
---

## 函数功能

在核函数中判断本次执行时的tiling\_key是否等于某个key，从而标识tiling\_key==key的一条kernel分支。

## 函数原型

```cpp
TILING_KEY_IS(key)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| key | 输入 | 此参数是非负整数，表示某个核函数的分支。 |

## 约束说明

* key必须是非负整数。
* TILING\_KEY\_IS运用于if和else if分支，不支持else分支，即用TILING\_KEY\_IS函数来表征N个分支，必须用N个TILING\_KEY\_IS(key)来分别表示。
* 暂不支持kernel直调工程。

## 调用示例

```cpp
extern "C" __global__ __aicore__ void add_custom(__gm__ uint8_t *x, __gm__ uint8_t *y, __gm__ uint8_t *z, __gm__ uint8_t *workspace, __gm__ uint8_t *tiling)
{
    GET_TILING_DATA(tilingData, tiling);
    if (workspace == nullptr) {
        return;
    }
    KernelAdd op;
    op.Init(x, y, z, tilingData.blockDim, tilingData.totalLength, tilingData.tileNum);
    // 当TilingKey为1时，执行Process1；为2时，执行Process2；为3时，执行Process3
    if (TILING_KEY_IS(1)) {
        op.Process1();
    } else if (TILING_KEY_IS(2)) {
        op.Process2();
    } else if (TILING_KEY_IS(3)) {
        op.Process3();
    }
    // 其他代码逻辑
    // ...
    // 此处示例当TilingKey为3时，会执行ProcessOther
    if (TILING_KEY_IS(3)) {
        op.ProcessOther();
    }
}
// 配套的host侧tiling函数示例：
ge::graphStatus TilingFunc(gert::TilingContext* context)
{
    // 其他代码逻辑
    // ...
    if (context->GetInputShape(0) != nullptr && context->GetInputShape(0)->GetDims().size() > 10) {
        context->SetTilingKey(1);
    } else if (some condition) {
        context->SetTilingKey(2);
    } else if (some condition) {
        context->SetTilingKey(3);
    }
}
```
