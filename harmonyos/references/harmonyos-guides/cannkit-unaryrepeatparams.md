---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-unaryrepeatparams
title: UnaryRepeatParams
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 数据类型定义 > UnaryRepeatParams
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7d8c6aeaa9b398e4e429fccd8945157fb17be8a969b0032a0281843f6196f9e1
---

UnaryRepeatParams为用于控制操作数地址步长的数据结构。结构体内包含操作数相邻迭代间相同datablock的地址步长，操作数同一迭代内不同datablock的地址步长等参数。

结构体具体定义为：

```cpp
const int32_t DEFAULT_BLK_NUM = 8;
const int32_t DEFAULT_BLK_STRIDE = 1;
const uint8_t DEFAULT_REPEAT_STRIDE = 8;
 
struct UnaryRepeatParams {
    __aicore__ UnaryRepeatParams()
    {
        blockNumber = DEFAULT_BLK_NUM;
        dstBlkStride = DEFAULT_BLK_STRIDE;
        srcBlkStride = DEFAULT_BLK_STRIDE;
        dstRepStride = DEFAULT_REPEAT_STRIDE;
        srcRepStride = DEFAULT_REPEAT_STRIDE;
        halfBlock = false;
    }
    __aicore__ UnaryRepeatParams(const uint16_t dstBlkStrideIn, const uint16_t srcBlkStrideIn,
        const uint8_t dstRepStrideIn, const uint8_t srcRepStrideIn)
    {
        dstBlkStride = dstBlkStrideIn;
        srcBlkStride = srcBlkStrideIn;
        dstRepStride = dstRepStrideIn;
        srcRepStride = srcRepStrideIn;
    }
    __aicore__ UnaryRepeatParams(const uint16_t dstBlkStrideIn, const uint16_t srcBlkStrideIn,
        const uint8_t dstRepStrideIn, const uint8_t srcRepStrideIn, const bool halfBlockIn)
    {
        dstBlkStride = dstBlkStrideIn;
        srcBlkStride = srcBlkStrideIn;
        dstRepStride = dstRepStrideIn;
        srcRepStride = srcRepStrideIn;
        halfBlock = halfBlockIn;
    }
    uint32_t blockNumber = 0;
    uint16_t dstBlkStride = 0;
    uint16_t srcBlkStride = 0;
    uint8_t dstRepStride = 0;
    uint8_t srcRepStride = 0;
    bool repeatStrideMode = false;
    bool strideSizeMode = false;
    bool halfBlock = false;
};
```

其中，blockNumber，repeatStrideMode，strideSizeMode为保留参数，开发者无需关心，使用默认值即可。halfBlock表示CastDeq指令的结果写入对应UB的上半（halfBlock = true）还是下半（halfBlock = false）部分。开发者需要自行定义dataBlockStride参数，包含dstBlkStride，srcBlkStride，以及repeatStride参数，包含dstRepStride，srcRepStride。
