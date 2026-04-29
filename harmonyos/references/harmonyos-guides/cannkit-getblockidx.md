---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getblockidx
title: GetBlockIdx
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 系统变量访问 > GetBlockIdx
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:25+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fedd6ab3bc35029faae03e5513b535304b8b8725a58865f66e90beddd87af8a2
---

## 功能说明

获取当前核的index，用于代码内部的多核逻辑控制及多核偏移量计算等。

## 函数原型

```
1. __aicore__ inline int64_t GetBlockIdx()
```

## 参数说明

无

## 返回值

当前核的index，index的范围为[0, 开发者配置的block\_dim数量 - 1]。

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 约束说明

GetBlockIdx为一个系统内置函数，返回当前核的index。

## 调用示例

```
1. #include "kernel_operator.h"
2. constexpr int32_t SINGLE_CORE_OFFSET = 256;
3. class KernelGetBlockIdx {
4. public:
5. __aicore__ inline KernelGetBlockIdx () {}
6. __aicore__ inline void Init(__gm__ uint8_t* src0Gm, __gm__ uint8_t* src1Gm, __gm__ uint8_t* dstGm)
7. {
8. // 根据index对每个核进行地址偏移
9. src0Global.SetGlobalBuffer((__gm__ float*)src0Gm + AscendC::GetBlockIdx() * SINGLE_CORE_OFFSET);
10. src1Global.SetGlobalBuffer((__gm__ float*)src1Gm + AscendC::GetBlockIdx() * SINGLE_CORE_OFFSET);
11. dstGlobal.SetGlobalBuffer((__gm__ float*)dstGm + AscendC::GetBlockIdx() * SINGLE_CORE_OFFSET);
12. pipe.InitBuffer(inQueueSrc0, 1, 256 * sizeof(float));
13. pipe.InitBuffer(inQueueSrc1, 1, 256 * sizeof(float));
14. pipe.InitBuffer(selMask, 1, 256);
15. pipe.InitBuffer(outQueueDst, 1, 256 * sizeof(float));
16. }
17. // ...
18. };
```
