---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-gettensorcountinque
title: GetTensorCountInQue
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TQueBind > GetTensorCountInQue
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:dd9263b03884503ada846ae59f6130247e40f17ec1d9538465fd60e68cd4d005
---

## 功能说明

查询队列中已入队的Tensor数量。

## 函数原型

```cpp
__aicore__ inline int32_t GetTensorCountInQue()
```

## 参数说明

无

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

无

## 返回值

Que中已入队的Tensor数量。

## 调用示例

```cpp
// 通过GetTensorCountInQue查询Queue中已入队的Tensor数量，当前通过AllocTensor接口分配了内存，并加入Queue中，num为1。
AscendC::TPipe pipe;
AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 4> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();
que.EnQue(tensor1);// 将tensor加入VECOUT的Queue中
int32_t numb = que.GetTensorCountInQue();
```
