---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-converttolistascendstring
title: ConvertToListAscendString
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > ConvertToListAscendString
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:13+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:736606fe7c735443e9eab67e2049dd9d9118c02021d28116af15b31c19449496
---

## 函数功能

定义了一个模板函数ConvertToListAscendString，用于将不同类型的字符串列表转换为AscendString类型的列表。

## 函数原型

```
1. template<typename T> std::vector<ge::AscendString> ConvertToListAscendString(T strs)
```

支持以下两种拓展：

```
1. template<> inline std::vector<ge::AscendString> ConvertToListAscendString(std::vector<std::string> strs)
```

对于std::vector<std::string>类型的字符串列表，先将其转换为std::vector<const char \*>类型，然后再进行转换。

```
1. template<> inline std::vector<ge::AscendString> ConvertToListAscendString(std::vector<ge::AscendString> strs)
```

对于std::vector<ge::AscendString>类型的字符串列表，直接返回原列表。

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| strs | 输入 | 待转换的字符串列表。 |

## 返回值

转换后的AscendString类型字符串列表。

## 异常处理

无

## 约束说明

无
