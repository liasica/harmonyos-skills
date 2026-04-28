---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cannkit-dataformattoformat
title: DataFormatToFormat
breadcrumb: 指南 > AI > CANN Kit（CANN异构计算框架服务） > AscendC算子开发 > AscendC算子接口 > 基础数据结构和接口 > ge命名空间 > TypeUtils > DataFormatToFormat
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:11+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:6ed41be98beb921f8b0c914ee8b8256a2e67ca29ecd344659a9be3828f85cc83
---

## 函数功能

将数据格式字符串转化为Format类型值。

使用该接口需要包含type\_utils.h头文件。

```
1. #include "graph/utils/type_utils.h"
```

## 函数原型

```
1. static Format DataFormatToFormat(const AscendString &str);
2. Format DataFormatToFormat(const std::string &str);
```

## 参数说明

| 参数 | 输入/输出 | 说明 |
| --- | --- | --- |
| str | 输入 | 待转换的Format字符串形式。  从GCC 5.1版本开始，libstdc++为了更好的实现C++11规范，更改了std::string和std::list的一些接口，导致新老版本ABI不兼容。所以推荐使用入参为**AscendString**类型的接口。 |

## 返回值

输入合法时，返回转换后的Format enum值，枚举定义请参考[Format](cannkit-ge-format.md)，仅支持部分格式，详见[约束说明](cannkit-dataformattoformat.md#约束说明)；输入不合法时，返回FORMAT\_RESERVED，并打印报错信息。

## 约束说明

只支持以下几种格式：

* "NCHW"：FORMAT\_NCHW
* "NHWC"：FORMAT\_NHWC
* "NDHWC"：FORMAT\_NDHWC
* "NCDHW"：FORMAT\_NCDHW
* "ND"：FORMAT\_ND

## 调用示例

```
1. // 如果使用的是AscendString入参的接口(建议使用)
2. ge::AscendString format_str = "NHWC";
3. auto format = DataFormatToFormat(format_str); // 1

5. // 如果使用的是std::string入参的接口(不建议使用)
6. std::string format_str = "NHWC";
7. auto format = DataFormatToFormat(format_str); // 1
```
