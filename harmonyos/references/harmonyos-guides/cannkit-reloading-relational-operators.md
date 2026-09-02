---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-reloading-relational-operators
title: 关系符重载
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > AscendString > 关系符重载
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a4e4aff4acaec9b2ea02e90c5860b030c431f6bcab004ef95ee09ccbcbe5138f
---

对于AscendString对象大小比较的使用场景（例如map数据结构的key进行排序），通过重载以下关系符实现。

```cpp
  bool operator<(const AscendString& d) const;
  bool operator>(const AscendString& d) const;
  bool operator<=(const AscendString& d) const;
  bool operator>=(const AscendString& d) const;
  bool operator==(const AscendString& d) const;
  bool operator!=(const AscendString& d) const;
```
