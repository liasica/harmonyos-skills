---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-basic-matrix-computation
title: 矩阵计算
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC昇腾到麒麟兼容性迁移指南 > Ascend910B/Ascend910C到KirinX90/Kirin9030迁移指导 > 基础API迁移指导 > 矩阵计算
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:00+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:13c6ca1bf18bd80465fc68c9bfa74271e6ba6845c1093312223fe4760da11e7e
---

KirinX90/Kirin9030处理器不支持结构化稀疏功能，并且Mmad左矩阵分形结构在Kirin9030有差异。

**表1** 矩阵计算兼容说明

| 基础API | 兼容说明 |
| --- | --- |
| MmadWithSparse | 不支持。不支持结构化稀疏功能，因此算子需要采用正常稠密的矩阵计算。 |
| Mmad | Kirin9030芯片平台，L0A Buffer分形改变，从ZZ(Ascend910B/Ascend910C/KirinX90)转换为ZN格式。算子做LoadData时，需要做LoadData参数修改适配，详见下图。 |

Mmad左矩阵分形格式变换修改适配方案：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/q-RV9QpDQVSRIJKh2IcSvA/zh-cn_image_0000002558765794.png?HW-CC-KV=V1&HW-CC-Date=20260429T054300Z&HW-CC-Expire=86400&HW-CC-Sign=4EE967ADC8556F6B17BF2E273679A5CA1DEDCCFAA6DDDC52C1E6408EEA37DE15)

```
1. // 示例代码
2. __aicore__ inline void SplitA()
3. {
4. int srcOffset = 0;
5. int dstOffset = 0;
6. AscendC::LocalTensor<half> a1Local = inQueueA1.DeQue<half>();
7. AscendC::LocalTensor<half> a2Local = inQueueA2.AllocTensor<half>();
8. #if defined(__NPU_ARCH__) && (__NPU_ARCH__ == 2201 || __NPU_ARCH__ == 3003)
9. // Ascend910B、Ascend910C和KirinX90，LoadData时做Nz2Zz的分形转换
10. for (int i = 0; i < mBlocks; ++i) {
11. AscendC::LoadData2DParams loadDataParams;
12. // kBlocks表示列方向上有几个宽为16的half类型矩阵
13. loadDataParams.repeatTimes = kBlocks;
14. // mBlocks表示行方向上有几个高为16的half类型矩阵
15. loadDataParams.srcStride = mBlocks;
16. loadDataParams.ifTranspose = false;
17. AscendC::LoadData(a2Local[dstOffset], a1Local[srcOffset], loadDataParams);
18. srcOffset += 16 * 16;
19. dstOffset += k * 16;
20. }
21. #endif
22. #if defined(__NPU_ARCH__) && (__NPU_ARCH__ == 3113)
23. // Kirin9030,LoadData时不需要做Nz2Zz的分形转换，对应搬运参数需要修改
24. AscendC::LoadData2DParams loadDataParams;
25. loadDataParams.repeatTimes = m * k / 512; // 小z矩阵的个数
26. loadDataParams.srcStride = 1; // 小z矩阵之间的间隔
27. loadDataParams.dstGap = 0;
28. loadDataParams.ifTranspose = false;
29. AscendC::LoadData(a2Local, a1Local, loadDataParams);

31. inQueueA2.EnQue<half>(a2Local);
32. inQueueA1.FreeTensor(a1Local);
33. #endif
34. }
```
