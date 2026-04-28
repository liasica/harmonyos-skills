---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-reloading-relational-operators
title: 关系符重载
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > AscendString > 关系符重载
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:d5c8c7a2187d72ee135cde6529060226d9ce4d287df668457b63b1d49f10d5bf
---

对于AscendString对象大小比较的使用场景（例如map数据结构的key进行排序），通过重载以下关系符实现。

```
1. bool operator<(const AscendString& d) const;
2. bool operator>(const AscendString& d) const;
3. bool operator<=(const AscendString& d) const;
4. bool operator>=(const AscendString& d) const;
5. bool operator==(const AscendString& d) const;
6. bool operator!=(const AscendString& d) const;
```
