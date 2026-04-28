---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setscalar
title: SetScalar
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > SetScalar
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:80b9c4b55ccacdfe48bffcf6c2879c7eda13896657cd0f580da655c8040f58e7
---

## 函数功能

设置shape为标量。

## 函数原型

```
1. void SetScalar()
```

## 参数说明

无

## 返回值

无

## 约束说明

无

## 调用示例

```
1. Shape shape0({3, 256, 256});
2. shape0.IsScalar(); // false
3. shape0.SetScalar();
4. shape0.IsScalar(); // true
```
