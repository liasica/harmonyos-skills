---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettpipeptr
title: GetTPipePtr
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > GetTPipePtr
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e6493b0d7b37a23d1503b3ef269c717e9100892c407b3eead5660ade51f37156
---

## 功能说明

创建[TPipe](cannkit-tpipe-constructor.md)对象时，对象初始化会设置全局唯一的TPipe指针。本接口用于获取该指针，获取该指针后，可进行TPipe相关的操作。

## 函数原型

```
1. __aicore__ inline AscendC::TPipe* GetTPipePtr()
```

## 支持的型号

Kirin9020系列处理器

KirinX90系列处理器

## 注意事项

无

## 调用示例

如下样例中，在核函数入口处创建TPipe对象，对象初始化会设置全局唯一的TPipe指针。在调用KernelAdd类Init函数时，无需显式传入TPipe指针，而是在函数内直接使用GetTPipePtr获取全局TPipe指针，用来做InitBuffer等操作。

```
1. class KernelAdd {
2. public:
3. __aicore__ inline KernelAdd() {}
4. __aicore__ inline void Init(GM_ADDR x, GM_ADDR y, GM_ADDR z)
5. {
6. xGm.SetGlobalBuffer((__gm__ half *)x + 2048 * AscendC::GetBlockIdx(), 2048);
7. yGm.SetGlobalBuffer((__gm__ half *)y + 2048 * AscendC::GetBlockIdx(), 2048);
8. zGm.SetGlobalBuffer((__gm__ half *)z + 2048 * AscendC::GetBlockIdx(), 2048);
9. GetTPipePtr()->InitBuffer(inQueueX, 2, 128 * sizeof(half));
10. GetTPipePtr()->InitBuffer(inQueueY, 2, 128 * sizeof(half));
11. GetTPipePtr()->InitBuffer(outQueueZ, 2, 128 * sizeof(half));
12. }
13. __aicore__ inline void Process()
14. {
15. // 算子kernel逻辑
16. // ...
17. }
18. private:
19. AscendC::TQue<AscendC::QuePosition::VECIN, 2> inQueueX, inQueueY;
20. AscendC::TQue<AscendC::QuePosition::VECOUT, 2> outQueueZ;
21. AscendC::GlobalTensor<half> xGm, yGm, zGm;
22. };
23. extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z)
24. {
25. AscendC::TPipe pipe;
26. KernelAdd op;
27. op.Init(x, y, z);
28. op.Process();
29. }
```
