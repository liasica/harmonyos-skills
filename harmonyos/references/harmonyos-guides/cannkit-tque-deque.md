---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tque-deque
title: DeQue
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TQue > DeQue
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:28+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:c64e1749d4ee5264bb3a0d05252742432ec9f6ed3c3c9d75ce5f3326df001c53
---

## 功能说明

将Tensor从队列中取出，用于后续处理。

## 函数原型

* 无需指定源和目的位置

  ```cpp
  template <typename T> 
  __aicore__ inline LocalTensor<T> DeQue()
  ```
* 需要指定源和目的位置

  通过[TQueBind](cannkit-overview.md)绑定VECIN和VECOUT可实现VECIN和VECOUT内存复用，如下接口用于存在Vector计算的场景下实现复用，在出队时需要指定源和目的位置，不存在Vector计算的场景下可直接调用LocalTensor<T> DeQue()出队接口。

  ```cpp
  template <TPosition srcUserPos, TPosition dstUserPos, typename T> 
  __aicore__ inline LocalTensor<T> DeQue()
  ```

**图1** 将LocalTensor通过EnQue放入A1/B1的Queue中后再通过DeQue搬出

![](https://media:401788444118906976)

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
AscendC::TQue<AscendC::TPosition::VECOUT, 4> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();
que.EnQue(tensor1);
AscendC::LocalTensor<half> tensor2 = que.DeQue<half>(); // 将tensor从VECOUT的Queue中搬出
```

```cpp
// 接口：DeQue Tensor，指定特定的Src/Dst position
AscendC::TPipe pipe;
AscendC::TQueBind<AscendC::QuePosition::VECIN, AscendC::QuePosition::VECOUT, 1> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();
que.EnQue<AscendC::QuePosition::GM, AscendC::QuePosition::VECIN, half>(tensor1);
// 将tensor从VECIN的Queue中搬出
AscendC::LocalTensor<half> tensor2 = que.DeQue<AscendC::QuePosition::GM, AscendC::QuePosition::VECIN, half>();
```
