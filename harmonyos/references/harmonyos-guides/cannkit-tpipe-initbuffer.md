---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tpipe-initbuffer
title: InitBuffer
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TPipe > InitBuffer
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:9cdda5cd72112a33d494836fa134e8a884f9a68ee10c1eb8f8b48dd3c1c773db
---

## 功能说明

TPipe是用来管理全局内存的框架，开发者可以调用TPipe中的InitBuffer接口为TQue/TBuf进行内存分配。

## 函数原型

* 为TQue分配内存

  ```cpp
  template <class T>
  __aicore__ inline bool InitBuffer(T& que, uint8_t num, uint32_t len)
  ```
* 为TBuf分配内存

  ```cpp
  template <TPosition bufPos>
  __aicore__ inline bool InitBuffer(TBuf<bufPos>& buf, uint32_t len)
  ```

## 参数说明

**表1** bool InitBuffer(T& que, uint8\_t num, uint32\_t len) 原型定义参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| que | 输入 | 需要分配内存的TQue对象。 |
| num | 输入 | 分配内存块的个数。[double buffer](cannkit-double-buffer.md)功能通过该参数开启：num设置为1，表示不开启double buffer；num设置为2，表示开启double buffer。 |
| len | 输入 | 每个内存块的大小，单位为Bytes。当传入的len不满足32字节对齐时，API内部会自动向上补齐至32字节对齐。 |

**表2** InitBuffer(TBuf<bufPos>& buf, uint32\_t len)原型定义参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| buf | 输入 | 需要分配内存的TBuf对象。 |
| len | 输入 | 为TBuf分配的内存大小，单位为Bytes。当传入的len不满足32字节对齐时，API内部会自动向上补齐至32字节对齐。 |

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

同一个TPosition上QUE Buffer的数量根据AI处理器型号的不同，有数量约束。申请Buffer时，需要满足该约束。

Kirin9020/Kirin9030/KirinX90系列处理器不超过8块。

```cpp
AscendC::TQue<AscendC::TPosition::VECIN, 1> que0;
AscendC::TQue<AscendC::TPosition::VECIN, 1> que1;
// 不建议：
// 比如，算子有6个输入，需要申请6块buffer
// 通过2个队列为其申请内存，分别为que0、que1分配3块，申请VECIN position上的buffer总数为6
// 针对同一个TPosition上QUE Buffer的数量有限制，超出该限制，在后续使用AllocTensor/FreeTensor可能会出现分配资源失败。
pipe.InitBuffer(que0, 3, len);
pipe.InitBuffer(que1, 3, len);
// 此时建议通过以下方法解决：
// 如果确实有多块buffer使用，可以将多个buffer合并到一块buffer，通过偏移使用
pipe.InitBuffer(que0, 1, len * 3);
pipe.InitBuffer(que1, 1, len * 3);
/*
 * 分配出3块内存大小的LocalTensor，local1的地址为que0中buffer的起始地址，
 * local2的地址为local1的地址偏移len后的地址，local3的地址为local1的地址偏移
 * len * 2的地址
 */
int32_t offset1 = len;
int32_t offset2 = len * 2;
AscendC::LocalTensor<T> local1 = que0.AllocTensor<T>();
AscendC::LocalTensor<T> local2 = local1[offset1];
AscendC::LocalTensor<T> local3 = local1[offset2];
```

## 返回值

返回Buffer初始化的结果。

## 调用示例

```cpp
// 为TQue分配内存，分配内存块数为2，每块大小为128Bytes
AscendC::TPipe pipe; // Pipe内存管理对象
AscendC::TQue<AscendC::TPosition::VECOUT, 2> que; // 输出数据Queue队列管理对象，QuePosition为VECOUT
uint8_t num = 2;
uint32_t len = 128;
pipe.InitBuffer(que, num, len);
```

```cpp
// 为TBuf分配内存，分配长度为128Bytes
AscendC::TPipe pipe;
AscendC::TBuf<AscendC::TPosition::A1> buf; // 输出数据管理对象，QuePosition为A1
uint32_t len = 128;
pipe.InitBuffer(buf, len);
```
