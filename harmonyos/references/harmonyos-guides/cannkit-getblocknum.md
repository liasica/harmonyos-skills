---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-getblocknum
title: GetBlockNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > AscendC API > 基础API > 系统变量访问 > GetBlockNum
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:37+08:00
doc_updated_at: 2026-08-18
content_hash: sha256:686410125d6a416c729d49185ee67a4867c8ee6a698fa8bc56fd321304674dfa
---

## 功能说明

获取当前任务配置的核数，用于代码内部的多核逻辑控制等。

## 函数原型

```cpp
__aicore__ inline int64_t GetBlockNum()
```

## 参数说明

无

## 返回值

当前任务配置的核数。

## 支持的型号

Kirin9020系列处理器

Kirin9030系列处理器

KirinX90系列处理器

## 约束说明

无

## 调用示例

```cpp
#include "kernel_operator.h"
// 在核内做简单的tiling计算时使用block_num，复杂tiling建议在host侧完成
__aicore__ inline void InitTilingParam(int32_t& totalSize, int32_t& loopSize)
{
    loopSize = totalSize / AscendC::GetBlockNum();
};
```
