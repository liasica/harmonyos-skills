---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-hastensorinque
title: HasTensorInQue
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TQueBind > HasTensorInQue
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:ec96533d0d825062990c74e81758f94476045061bc2a62fc0be8bd999cc9f68f
---

## 功能说明

查询队列中目前是否已有入队的Tensor。

## 函数原型

```cpp
__aicore__ inline bool HasTensorInQue()
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

* true：表示Queue中存在已入队的Tensor。
* false：表示Queue为完全空闲。

## 调用示例

```cpp
// 根据HasTensorInQue判断当前Queue中是否有已入队的Tensor，当前Queue的深度为4，无内存EnQue动作，返回为false
AscendC::TPipe pipe;
AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 4> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
bool ret = que.HasTensorInQue();
```
