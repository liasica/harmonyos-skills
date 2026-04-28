---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setdimnum
title: SetDimNum
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > SetDimNum
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:09+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:762f8ae24f65d578d20365c8e89485a406620adcf5e0a38a63559ef0ba82390e
---

## 函数功能

设置dim num。

## 函数原型

```
1. void SetDimNum(const size_t dim_num)
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| dim\_num | 输入 | 将Shape对象的dim\_num\_设置为dim\_num。 |

## 返回值

无

## 约束说明

无

## 调用示例

```
1. Shape shape0({3, 256, 256});
2. shape0.SetDimNum(1);
3. auto dim_num = shape0.GetDimNum(); // 1
```
