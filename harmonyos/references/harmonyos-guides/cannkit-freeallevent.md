---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-freeallevent
title: FreeAllEvent
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TQueBind > FreeAllEvent
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:3a8036667bec256a551c13e617a283f46d84c377609af78265cec8abac915fe4
---

## 功能说明

释放对应队列中的所有事件，防止出现同步事件未匹配的情况，是一种额外的保护机制。建议优先保证AllocTensor/FreeTensor和EnQue/DeQue配对使用，配对使用情况下不需要调用该接口。

## 函数原型

```cpp
__aicore__ inline void FreeAllEvent()
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

无

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
tensor1 = que.DeQue<half>(); // 将tensor从VECOUT的Queue中搬出
que.FreeTensor<half>(tensor1);
que.FreeAllEvent();
```
