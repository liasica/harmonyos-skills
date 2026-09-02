---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getwithoffset
title: GetWithOffset
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TBuf > GetWithOffset
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:598f125477cb51b4d8ad463db38e26357bf8f4900f0e1a2a4601447b33a25130
---

## 功能说明

从TBuf上偏移指定长度且获取指定长度的Tensor。

## 函数原型

```cpp
LocalTensor<T> GetWithOffset<T>(uint32_t size, uint32_t bufOffset)
```

## 参数说明

**表1** 参数说明

| 参数名称 | 输入/输出 | 含义 |
| --- | --- | --- |
| size | 输入 | 需要获取的Tensor元素个数。 |
| bufOffset | 输入 | 从起始位置的偏移长度，单位为Byte，且需32B对齐。 |

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 注意事项

* size的数值是Tensor中元素的个数，size\*sizeof(T) + bufOffset不能超过TBuf初始化时的长度。
* bufOffset需满足32B对齐的要求。

## 返回值

返回从偏移位置截取的LocalTensor对象。

## 调用示例

```cpp
// 为TBuf初始化分配内存，分配内存长度为1024Bytes
AscendC::TPipe pipe;
AscendC::TBuf<AscendC::TPosition::VECCALC> calcBuf; // 模板参数为TPosition中的VECCALC类型
uint32_t byteLen = 1024;
pipe.InitBuffer(calcBuf, byteLen);
// 从calcBuf偏移64字节获取Tensor,Tensor为128个int32_t类型元素的内存大小，为512Bytes
AscendC::LocalTensor<int32_t> tempTensor1 = calcBuf.GetWithOffset<int32_t>(128, 64);
```
