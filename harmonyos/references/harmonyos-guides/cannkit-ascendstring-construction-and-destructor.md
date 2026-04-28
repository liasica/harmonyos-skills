---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-ascendstring-construction-and-destructor
title: 构造函数和析构函数
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > AscendString > 构造函数和析构函数
category: harmonyos-guides
scraped_at: 2026-04-28T07:52:26+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:cf7406500db1bbea2696ae32dce3e3b572addb0ef9254071a8bf661d965520b2
---

## 函数功能

AscendString构造函数和析构函数。

## 函数原型

```
1. AscendString() = default;
2. ~AscendString() = default;
3. AscendString(const char_t *const name);
4. AscendString(const char_t *const name, size_t length);
```

## 参数说明

| 参数名 | 输入/输出 | 描述 |
| --- | --- | --- |
| name | 输入 | 字符串名称。 |
| length | 输入 | 字符串长度。 |

## 返回值

AscendString构造函数返回AscendString类型的对象。

## 异常处理

无

## 约束说明

无
