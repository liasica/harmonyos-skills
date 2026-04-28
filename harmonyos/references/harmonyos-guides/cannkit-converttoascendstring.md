---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-converttoascendstring
title: ConvertToAscendString
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > ConvertToAscendString
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:12+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:abdae783810b3f795d7d97a22e2b380bb9e2c86fa50b1d20316f2b563117df33
---

## 函数功能

模板函数，接受一个模板参数T，并将其转换为AscendString类型。这个函数的主要功能是将不同类型的字符串转换为AscendString类型。

## 函数原型

```
1. template<typename T> ge::AscendString ConvertToAscendString(T str)
```

支持以下几种拓展：

```
1. template<> inline ge::AscendString ConvertToAscendString<const char *>(const char *str)
```

对于const char \*类型的字符串，直接使用AscendString的构造函数进行转换。

```
1. template<> inline ge::AscendString ConvertToAscendString<std::string>(std::string str)
```

对于std::string类型的字符串，先将其转换为const char \*类型，然后再进行转换。

```
1. template<> inline ge::AscendString ConvertToAscendString<ge::AscendString>(ge::AscendString str)
```

对于AscendString类型的字符串，直接返回AscendString类型字符串。

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| str | 输入 | 待转换的字符串。 |

## 返回值

转换后的AscendString类型字符串。

## 异常处理

无

## 约束说明

无
