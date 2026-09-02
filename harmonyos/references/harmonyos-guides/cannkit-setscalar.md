---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-setscalar
title: SetScalar
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > gert命名空间 > Shape > SetScalar
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6068368280fe03bcd89550ec585e10ad5ddc08808a6171299c1e28248632227b
---

## 函数功能

设置shape为标量。

## 函数原型

```cpp
void SetScalar()
```

## 参数说明

无

## 返回值

无

## 约束说明

无

## 调用示例

```cpp
Shape shape0({3, 256, 256});
shape0.IsScalar(); // false
shape0.SetScalar();
shape0.IsScalar(); // true
```
