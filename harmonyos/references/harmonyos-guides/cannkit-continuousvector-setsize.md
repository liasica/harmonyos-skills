---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-continuousvector-setsize
title: SetSize
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > ContinuousVector > SetSize
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:53+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:aa57159152fc6abddab5922f257a864b8cd929133d673737afa4d082fea0af1b
---

## 函数功能

设置当前保存的元素个数。

## 函数原型

```
1. ge::graphStatus SetSize(const size_t size)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| size | 输入 | 当前保存的元素个数。 |

## 返回值

成功时返回ge::GRAPH\_SUCCESS。

设置的size>capacity时，返回失败ge::GRAPH\_FAILED。

## 约束说明

无

## 调用示例

```
1. size_t capacity = 100U;
2. auto cv_holder = ContinuousVector::Create<int64_t>(capacity);
3. auto cv = reinterpret_cast<ContinuousVector *>(cv_holder.get());
4. auto ret = cv->SetSize(10U); // ge::GRAPH_SUCCESS
5. ret = cv->GetSize(101U); // ge::GRAPH_FAILED
```
