---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-alloctensor
title: AllocTensor
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TQueBind > AllocTensor
category: harmonyos-guides
scraped_at: 2026-09-05T06:15:29+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:ffb44aaf28e22d1b503decfedcd0bffdca440e417a20797138869aee0a129187
---

## 功能说明

从队列中分配Tensor，Tensor所占大小为InitBuffer时设置的每块内存长度。

![](https://media:401788444117972969) 

分配的Tensor内容并非全0，可能会是随机值。

## 函数原型

```cpp
template <typename T> 
__aicore__ inline LocalTensor<T> AllocTensor()
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

LocalTensor对象。

## 调用示例

```cpp
// 使用AllocTensor分配Tensor
AscendC::TPipe pipe;
AscendC::TQueBind<AscendC::TPosition::VECOUT, AscendC::TPosition::GM, 2> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len); // InitBuffer分配内存块数为4，每块大小为1024Bytes
AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>(); // AllocTensor分配Tensor长度为1024Bytes
```
