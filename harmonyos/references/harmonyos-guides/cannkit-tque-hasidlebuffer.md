---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-tque-hasidlebuffer
title: HasIdleBuffer
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 内存管理与同步控制 > TQue > HasIdleBuffer
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:77e5c2290b2944bf30358f850fd3cf09f76b35c65625b65f99e1dff56924f0dd
---

## 功能说明

查询队列中是否有空闲的内存块。

## 函数原型

```cpp
__aicore__ inline bool HasIdleBuffer()
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

* true：表示Queue中存在空闲内存。
* false：表示Queue中不存在空闲内存。

## 调用示例

```cpp
// 当前Que中已经分配了4块内存
AscendC::TPipe pipe;
AscendC::TQue<AscendC::TPosition::VECOUT, 1> que;
int num = 4;
int len = 1024;
pipe.InitBuffer(que, num, len);
bool ret = que.HasIdleBuffer(); // 没有AllocTensor的操作，返回值为true
AscendC::LocalTensor<half> tensor1 = que.AllocTensor<half>();
ret = que.HasIdleBuffer(); // AllocTensor了一块内存，返回值为true
AscendC::LocalTensor<half> tensor2 = que.AllocTensor<half>();
AscendC::LocalTensor<half> tensor3 = que.AllocTensor<half>();
AscendC::LocalTensor<half> tensor4 = que.AllocTensor<half>();
ret = que.HasIdleBuffer(); // AllocTensor了四块内存，当前无空闲内存，返回值为false，继续AllocTensor会报错
```
