---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-web
title: Web
breadcrumb: API参考 > 应用框架 > ArkWeb（方舟Web） > C API > 模块 > Web
category: harmonyos-references
scraped_at: 2026-04-28T08:05:25+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:6ab0a857fa3a6c000198c1579aedb2dcaad185dc4445ea880fa523260dcd582d
---

## 概述

PhonePC/2in1TabletTVWearable

为ArkWeb NDK接口发生异常提供错误码。

提供注入对象和执行JavaScript代码的API接口。

提供用于拦截ArkWeb请求的API。

为ArkWeb网络协议栈提供错误码。

提供ArkWeb在Native侧的能力，如网页刷新、执行JavaScript、注册回调等。

更多详细介绍请参考[应用侧与前端页面的相互调用(C/C++)](../harmonyos-guides/arkweb-ndk-jsbridge.md)、[建立应用侧与前端页面数据通道(C/C++)](../harmonyos-guides/arkweb-ndk-page-data-channel.md)和[拦截Web组件发起的网络请求](../harmonyos-guides/web-scheme-handler.md)。

**起始版本：** 12

## 文件汇总

PhonePC/2in1TabletTVWearable

| 名称 | 描述 |
| --- | --- |
| [arkweb\_error\_code.h](capi-arkweb-error-code-h.md) | 声明ArkWeb NDK接口异常错误码。 |
| [arkweb\_interface.h](capi-arkweb-interface-h.md) | 提供ArkWeb在Native侧获取API的接口，及基础Native API类型。 |
| [arkweb\_net\_error\_list.h](capi-arkweb-net-error-list-h.md) | 声明ArkWeb网络协议栈错误码。 |
| [arkweb\_scheme\_handler.h](capi-arkweb-scheme-handler-h.md) | 声明用于拦截来自ArkWeb的请求的API。 |
| [arkweb\_type.h](capi-arkweb-type-h.md) | 提供ArkWeb在Native侧的公共类型定义。 |
| [native\_interface\_arkweb.h](capi-native-interface-arkweb-h.md) | 声明API接口供开发者使用注入对象和执行JavaScript代码等功能。 |
