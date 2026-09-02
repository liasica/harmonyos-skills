---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-binaryrepeatparams
title: BinaryRepeatParams
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 数据类型定义 > BinaryRepeatParams
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6859baa6fbabd8ca49ce30a9a4029ca4f34cd3a2c8c19d02c659678dfbcb0744
---

BinaryRepeatParams为用于控制操作数地址步长的数据结构。结构体内包含操作数相邻迭代间相同datablock的地址步长，操作数同一迭代内不同datablock的地址步长等参数。

结构体具体定义为：

```cpp
const int32_t DEFAULT_BLK_NUM = 8;
const int32_t DEFAULT_BLK_STRIDE = 1;
const uint8_t DEFAULT_REPEAT_STRIDE = 8;
 
struct BinaryRepeatParams {
    __aicore__ BinaryRepeatParams()
    {
        blockNumber = DEFAULT_BLK_NUM;
        dstBlkStride = DEFAULT_BLK_STRIDE;
        src0BlkStride = DEFAULT_BLK_STRIDE;
        src1BlkStride = DEFAULT_BLK_STRIDE;
        dstRepStride = DEFAULT_REPEAT_STRIDE;
        src0RepStride = DEFAULT_REPEAT_STRIDE;
        src1RepStride = DEFAULT_REPEAT_STRIDE;
    }
    __aicore__ BinaryRepeatParams(const uint8_t dstBlkStrideIn, const uint8_t src0BlkStrideIn,
        const uint8_t src1BlkStrideIn, const uint8_t dstRepStrideIn, const uint8_t src0RepStrideIn,
        const uint8_t src1RepStrideIn)
    {
        dstBlkStride = dstBlkStrideIn;
        src0BlkStride = src0BlkStrideIn;
        src1BlkStride = src1BlkStrideIn;
        dstRepStride = dstRepStrideIn;
        src0RepStride = src0RepStrideIn;
        src1RepStride = src1RepStrideIn;
    }
    uint32_t blockNumber = 0;
    uint8_t dstBlkStride = 0;
    uint8_t src0BlkStride = 0;
    uint8_t src1BlkStride = 0;
    uint8_t dstRepStride = 0;
    uint8_t src0RepStride = 0;
    uint8_t src1RepStride = 0;
    bool repeatStrideMode = false;
    bool strideSizeMode = false;
};
```

其中，blockNumber，repeatStrideMode和strideSizeMode为保留参数，开发者无需关心，使用默认值即可。开发者需要自行定义dataBlockStride参数，包含dstBlkStride，src0BlkStride和src1BlkStride，以及repeatStride参数，包含dstRepStride，src0RepStride和src1RepStride。
