---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-spmd-model
title: SPMD模型
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > 自定义算子开发 > 基本概念 > 编程模型 > SPMD模型
category: harmonyos-guides
scraped_at: 2026-04-29T13:41:03+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:34cd6deeecbe312520c8a387256f1681da41089b5448e9522c97b5b3537accc5
---

AscendC算子编程是SPMD(Single-Program Multiple-Data)编程，SPMD是一种常用的并行计算的方法，是提高计算速度的有效手段。

假设，从输入数据到输出数据需要经过3个阶段任务的处理（T1、T2、T3）。如下图所示，SPMD模式下，系统会启动一组进程，并行处理待处理的数据：首先待处理数据会被切分成多个数据分片，切分后的数据分片随后被分发给不同进程处理，每个进程接收到一个或多个数据分片，并独立地对这些分片进行3个任务的处理。

**图1** SPMD数据并行示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/By2_AFV8TRSBPU_qtlcB2Q/zh-cn_image_0000002589245539.png?HW-CC-KV=V1&HW-CC-Date=20260429T054102Z&HW-CC-Expire=86400&HW-CC-Sign=41D43C6857137B8425C0D5267A8E10E4627064E7B84B6A4B4E9D55F9D1868086)

具体到AscendC编程模型中的应用，是将需要处理的数据拆分并同时在多个计算核心（类比于上文介绍中的多个进程）上运行，从而获取更高的性能。多个AI Core共享相同的指令代码，每个核上的运行实例唯一的区别是block\_idx不同，每个核通过不同的block\_idx来识别自己的身份。block的概念类似于上文中进程的概念，block\_idx就是标识进程唯一性的进程ID。并行计算过程如下图所示。

**图2** SPMD并行计算示意图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/cxprKw8eRtuTsdpx9d1F6A/zh-cn_image_0000002558765730.png?HW-CC-KV=V1&HW-CC-Date=20260429T054102Z&HW-CC-Expire=86400&HW-CC-Sign=17B4FE5797AC73F0279D31C474C106B583A6B2D37BA72CB770DF7E6D9BF80208)

下面的代码片段取自于AscendC Add算子的实现代码，算子被调用时，所有的计算核心都执行相同的实现代码，入口函数的入参也是相同的。每个核上处理的数据地址需要在起始地址上增加[GetBlockIdx](cannkit-getblockidx.md)\*BLOCK\_LENGTH（每个block处理的数据长度）的偏移来获取。这样也就实现了多核并行计算的数据切分。

```
1. class KernelAdd {
2. public:
3. __aicore__ inline KernelAdd() {}
4. __aicore__ inline void Init(GM_ADDR x, GM_ADDR y, GM_ADDR z)
5. {
6. // get start index for current core, core parallel
7. xGm.SetGlobalBuffer((__gm__ half*)x + BLOCK_LENGTH * GetBlockIdx(), BLOCK_LENGTH);
8. yGm.SetGlobalBuffer((__gm__ half*)y + BLOCK_LENGTH * GetBlockIdx(), BLOCK_LENGTH);
9. zGm.SetGlobalBuffer((__gm__ half*)z + BLOCK_LENGTH * GetBlockIdx(), BLOCK_LENGTH);
10. // pipe alloc memory to queue, the unit is Bytes
11. pipe.InitBuffer(inQueueX, BUFFER_NUM, TILE_LENGTH * sizeof(half));
12. pipe.InitBuffer(inQueueY, BUFFER_NUM, TILE_LENGTH * sizeof(half));
13. pipe.InitBuffer(outQueueZ, BUFFER_NUM, TILE_LENGTH * sizeof(half));
14. }
15. // ...
16. }

19. // 实现核函数
20. extern "C" __global__ __aicore__ void add_custom(GM_ADDR x, GM_ADDR y, GM_ADDR z)
21. {
22. // 初始化算子类，算子类提供算子初始化和核心处理等方法
23. KernelAdd op;
24. // 初始化函数，获取该核函数需要处理的输入输出地址，同时完成必要的内存初始化工作
25. op.Init(x, y, z);
26. // 核心处理函数，完成算子的数据搬运与计算等核心逻辑
27. op.Process();
28. }
```
