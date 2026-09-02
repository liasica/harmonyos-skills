---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tque-freetensor
title: FreeTensor
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TQue > FreeTensor
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:9782937f70afc7617e556559b65cfd1b0d14d36ec43693e33872ac0c6361e6da
---

## 功能说明

释放队列中的指定Tensor，供Que后续使用。

## 函数原型

```cpp
template <typename T> 
__aicore__ inline void FreeTensor(LocalTensor<T>& tensor)
```

## 参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| tensor | 输入 | 待释放的Tensor。 |

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
// 使用FreeTensor释放通过AllocTensor分配的Tensor，注意配对使用
AscendC::TPipe pipe;
AscendC::TQue<AscendC::TPosition::VECOUT, 2> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();
que.FreeTensor<half>(tensor1);
```
