---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/load-module-base-nodeapi
title: 基于Node-API加载模块
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS运行时 > ArkTS模块化 > 基于Node-API加载模块
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:45+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:caa8c130fbb6cfc3767851633df254e63a76eff820b63e73e4250be9f290d607
---

Node-API中有多种方式支持开发者在C++侧加载工程内模块及文件。推荐使用napi\_load\_module\_with\_info接口。

## napi\_load\_module\_with\_info

在主线程或子线程内加载hap/hsp/har/native模块，使用时必须标记所加载的包的信息，支持多种场景。

具体参考：[napi\_load\_module\_with\_info](use-napi-load-module-with-info.md)。

## napi\_load\_module

在主线程内加载hap/hsp/har/native模块，参数传递简便。加载场景有限制，例如无法在子线程中使用该接口。

具体参考：[napi\_load\_module](use-napi-load-module.md)。
