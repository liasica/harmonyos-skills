---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-promote
title: Promote
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > Promote
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:42+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ec0bec65e5272408d73e1a96a445d25577256ad9ad7aaa254421f30522a7ff04
---

## 函数功能

Promote类用于表示输出数据类型为输入或属性指定的数据类型间的提升类型。

## 函数原型

```cpp
class Promote {
 public:
  Promote(const std::initializer_list<const char *> &syms);
  std::vector<const char *> Syms() const; // 返回参与类型提升的符号名
  Promote(const Promote &other) = delete;
  Promote &operator=(const Promote &other) = delete;
  Promote(Promote &&other) noexcept;
  Promote &operator=(Promote &&other) noexcept;
 private:
  std::shared_ptr<void> data_;
};
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| syms | 参与提升的类型符号列表。 | 符号包括输入类型的符号或者属性指定的符号。 |

## 返回值

无

## 异常处理

无

## 约束说明

无
