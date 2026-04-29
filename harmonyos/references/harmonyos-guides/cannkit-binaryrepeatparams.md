---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-binaryrepeatparams
title: BinaryRepeatParams
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 数据类型定义 > BinaryRepeatParams
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:22+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6936d5ef0fb20ce93b0d4400a26c6ee539382c81024c5074fc4bdf093ed641ab
---

BinaryRepeatParams为用于控制操作数地址步长的数据结构。结构体内包含操作数相邻迭代间相同datablock的地址步长，操作数同一迭代内不同datablock的地址步长等参数。

结构体具体定义为：

```
1. const int32_t DEFAULT_BLK_NUM = 8;
2. const int32_t DEFAULT_BLK_STRIDE = 1;
3. const uint8_t DEFAULT_REPEAT_STRIDE = 8;

5. struct BinaryRepeatParams {
6. __aicore__ BinaryRepeatParams()
7. {
8. blockNumber = DEFAULT_BLK_NUM;
9. dstBlkStride = DEFAULT_BLK_STRIDE;
10. src0BlkStride = DEFAULT_BLK_STRIDE;
11. src1BlkStride = DEFAULT_BLK_STRIDE;
12. dstRepStride = DEFAULT_REPEAT_STRIDE;
13. src0RepStride = DEFAULT_REPEAT_STRIDE;
14. src1RepStride = DEFAULT_REPEAT_STRIDE;
15. }
16. __aicore__ BinaryRepeatParams(const uint8_t dstBlkStrideIn, const uint8_t src0BlkStrideIn,
17. const uint8_t src1BlkStrideIn, const uint8_t dstRepStrideIn, const uint8_t src0RepStrideIn,
18. const uint8_t src1RepStrideIn)
19. {
20. dstBlkStride = dstBlkStrideIn;
21. src0BlkStride = src0BlkStrideIn;
22. src1BlkStride = src1BlkStrideIn;
23. dstRepStride = dstRepStrideIn;
24. src0RepStride = src0RepStrideIn;
25. src1RepStride = src1RepStrideIn;
26. }
27. uint32_t blockNumber = 0;
28. uint8_t dstBlkStride = 0;
29. uint8_t src0BlkStride = 0;
30. uint8_t src1BlkStride = 0;
31. uint8_t dstRepStride = 0;
32. uint8_t src0RepStride = 0;
33. uint8_t src1RepStride = 0;
34. bool repeatStrideMode = false;
35. bool strideSizeMode = false;
36. };
```

其中，blockNumber，repeatStrideMode和strideSizeMode为保留参数，开发者无需关心，使用默认值即可。开发者需要自行定义dataBlockStride参数，包含dstBlkStride，src0BlkStride和src1BlkStride，以及repeatStride参数，包含dstRepStride，src0RepStride和src1RepStride。
