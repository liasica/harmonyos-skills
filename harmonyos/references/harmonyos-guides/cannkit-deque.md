---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-deque
title: DeQue
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TQueBind > DeQue
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:bbee15a4193d3ef2330926f4da644227026fba968da11470a77d58c3534319ad
---

## 功能说明

将Tensor从队列中取出，用于后续处理。

## 函数原型

```cpp
template <typename T> 
__aicore__ inline LocalTensor<T> DeQue()
```

**图1** 将LocalTensor通过EnQue放入A1/B1的Queue中后再通过DeQue搬出

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/byblt50bT_au9Mo8T7beOA/zh-cn_image_0000002706835350.png)

## 参数说明

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

无

## 返回值

从队列中取出的[LocalTensor](cannkit-localtensor.md)。

## 调用示例

```cpp
// 接口：DeQue Tensor
AscendC::TPipe pipe;
AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 4> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();
que.EnQue(tensor1);
AscendC::LocalTensor<half> tensor2 = que.DeQue<half>(); // 将tensor从VECOUT的Queue中搬出
```
