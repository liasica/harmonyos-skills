---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-unaryrepeatparams
title: UnaryRepeatParams
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 数据类型定义 > UnaryRepeatParams
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:21+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6d09c0308dae3edd2e1ae766cebe3f34c14b65059e5eda09df64a15b54dbdf49
---

UnaryRepeatParams为用于控制操作数地址步长的数据结构。结构体内包含操作数相邻迭代间相同datablock的地址步长，操作数同一迭代内不同datablock的地址步长等参数。

结构体具体定义为：

```
1. const int32_t DEFAULT_BLK_NUM = 8;
2. const int32_t DEFAULT_BLK_STRIDE = 1;
3. const uint8_t DEFAULT_REPEAT_STRIDE = 8;

5. struct UnaryRepeatParams {
6. __aicore__ UnaryRepeatParams()
7. {
8. blockNumber = DEFAULT_BLK_NUM;
9. dstBlkStride = DEFAULT_BLK_STRIDE;
10. srcBlkStride = DEFAULT_BLK_STRIDE;
11. dstRepStride = DEFAULT_REPEAT_STRIDE;
12. srcRepStride = DEFAULT_REPEAT_STRIDE;
13. halfBlock = false;
14. }
15. __aicore__ UnaryRepeatParams(const uint16_t dstBlkStrideIn, const uint16_t srcBlkStrideIn,
16. const uint8_t dstRepStrideIn, const uint8_t srcRepStrideIn)
17. {
18. dstBlkStride = dstBlkStrideIn;
19. srcBlkStride = srcBlkStrideIn;
20. dstRepStride = dstRepStrideIn;
21. srcRepStride = srcRepStrideIn;
22. }
23. __aicore__ UnaryRepeatParams(const uint16_t dstBlkStrideIn, const uint16_t srcBlkStrideIn,
24. const uint8_t dstRepStrideIn, const uint8_t srcRepStrideIn, const bool halfBlockIn)
25. {
26. dstBlkStride = dstBlkStrideIn;
27. srcBlkStride = srcBlkStrideIn;
28. dstRepStride = dstRepStrideIn;
29. srcRepStride = srcRepStrideIn;
30. halfBlock = halfBlockIn;
31. }
32. uint32_t blockNumber = 0;
33. uint16_t dstBlkStride = 0;
34. uint16_t srcBlkStride = 0;
35. uint8_t dstRepStride = 0;
36. uint8_t srcRepStride = 0;
37. bool repeatStrideMode = false;
38. bool strideSizeMode = false;
39. bool halfBlock = false;
40. };
```

其中，blockNumber，repeatStrideMode，strideSizeMode为保留参数，开发者无需关心，使用默认值即可。halfBlock表示CastDeq指令的结果写入对应UB的上半（halfBlock = true）还是下半（halfBlock = false）部分。开发者需要自行定义dataBlockStride参数，包含dstBlkStride，srcBlkStride，以及repeatStride参数，包含dstRepStride，srcRepStride。
