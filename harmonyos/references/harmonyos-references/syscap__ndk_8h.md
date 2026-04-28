---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/syscap__ndk_8h
title: syscap_ndk.h
breadcrumb: API参考 > 公共基础能力 > C API > 头文件 > syscap_ndk.h
category: harmonyos-references
scraped_at: 2026-04-28T08:19:19+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9f06936aca12bf9c808ace888a155ea3227ec63a2b28a19478e474a70593ed9e
---

## 概述

PhonePC/2in1TabletTVWearable

查询单个系统能力是否被支持的API。

**起始版本：**

8

**相关模块：**

[Init](init.md)

## 汇总

PhonePC/2in1TabletTVWearable

### 函数

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [canIUse](init.md#caniuse) (const char \*cap) | 查询指定的系统能力是否被支持。  系统能力（SystemCapability，简称SysCap），指操作系统中每一个相对独立的特性。不同的设备对应不同的系统能力集，每个系统能力对应一个或多个API。开发者可根据系统能力来判断是否可以使用某接口。 |
