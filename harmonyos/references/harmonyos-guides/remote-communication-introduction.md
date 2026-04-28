---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/remote-communication-introduction
title: Remote Communication Kit简介
breadcrumb: 指南 > 系统 > 网络 > Remote Communication Kit（远场通信服务） > Remote Communication Kit简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:01+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fe7988139fb02b1d06c033c88b0c950075a43de1282c9cf388584ad7db3f4317
---

## 概述

Remote Communication Kit提供请求网络数据的功能，当前包含以下能力：

* HTTP请求能力。Remote Communication Kit构建了一种场景化HTTP通信能力。和Network Kit提供的标准HTTP能力不同的是，Remote Communication Kit构建了场景化API，强调易用性，详见[支持的HTTP网络请求场景](remote-communication-introduction.md#支持的http网络请求场景)。开发者可根据需要选择合适的Kit。
* URPC（Unified Remote Procedure Call）高性能rpc通信库。可实现远程函数调用能力，且具有抗弱网传输、多径传输（蜂窝网络和Wi-Fi）等特性。开发者可通过URPC完成简单方便的远程过程调用。

## 基本概念

HTTP（Hypertext Transfer Protocol）是一种基于客户端-服务器模型的数据传输协议。客户端向服务器发出请求，服务器返回响应。

HTTP请求是客户端向服务器发送请求的过程，包括以下基本概念：

* 请求方法（Request Method）：客户端向服务器发送请求的方式，如GET、POST、PUT、DELETE、OPTIONS、HEAD、PATCH等。
* URL（Uniform Resource Locator）：统一资源定位符，用于指定要访问的资源的地址。
* 请求头（Request Header）：包含一些附加的信息，如请求的来源、客户端的浏览器类型、语言、字符集等。
* 请求体（Request Body）：包含客户端向服务器发送的数据，如表单数据等。
* HTTP版本（HTTP Version）：HTTP协议的版本号，如HTTP/1.1、HTTP/2等。
* 状态码（Status Code）：服务器响应请求后返回的状态码，如200表示请求成功、404表示请求的资源不存在等。
* 响应头（Response Header）：包含一些附加的信息，如服务器的类型、响应的日期、内容类型等。
* 响应体（Response Body）：包含服务器返回给客户端的数据，如HTML、JSON等格式的数据。

| 请求类型 | 说明 |
| --- | --- |
| GET | 获取资源，用于请求特定资源的表示形式。常用场景：获取网页、图片、视频等资源。 |
| POST | 提交资源，用于提交实体，通常用于提交表单数据。常用场景：提交数据，如表单数据、上传文件等。 |
| OPTIONS | 获取资源支持的HTTP方法。常用场景：查询有关目标资源所支持的HTTP方法，如获取某个API支持的请求方式。 |
| HEAD | 获取资源的元数据，与GET方法类似，但不返回资源的主体部分，只返回资源的元数据，如响应头。常用场景：获取资源的头部信息，如文件大小、修改时间等。 |
| PUT | 更新资源，用于修改已经存在服务器上的资源，对指定URL路径上的资源进行完全替换。常用场景：更新资源，如更新文件、修改数据库记录等。 |
| DELETE | 删除资源，用于删除目标资源。常用场景：删除如用户、文章等资源。 |
| PATCH | 更新资源的一部分，用于对资源进行局部修改。常用场景：更新服务器局部资源，如资源的某些属性和字段，而不需要替换整个资源。 |

## 支持的HTTP网络请求场景

| 场景名称 | 场景描述 | 备注 |
| --- | --- | --- |
| 发送PATCH类型请求 | 以PATCH的方式请求。 | - |
| 设置会话中URL的基地址 | 会话中URL的基地址将自动加在URL前面，除非URL是一个绝对URL。 | - |
| 取消自动重定向 | 用于取消HTTP请求的自动重定向。 | - |
| 拦截请求和响应 | 在请求后或响应前进行拦截。 | - |
| 取消请求 | 发送请求前取消、发送请求过程中取消、请求接收后取消。 | - |
| 响应缓存 | 可以使用缓存，并在请求时优先读取缓存。 | 缓存跟随当前进程生效，新缓存会替换旧缓存。 |
| 设置响应数据的类型 | 设置数据以何种方式返回。可将响应的数据类型设置为string、object、ArrayBuffer等类型。 | 响应体类型默认为ArrayBuffer，调用方可通过Response的toJSON或者toString方法得到object或者string类型的数据。 |
| 自定义证书校验 | 自定义校验客户端和服务端证书的逻辑，用于判断是否可以连接。 | - |
| 忽略SSL校验 | 在建立SSL连接时不验证服务器端的SSL证书。 | - |
| 自定义DNS解析 | 自定义DNS服务器或配置静态DNS规则。 | - |
| 捕获详细的跟踪信息 | 捕获HTTP请求中详细的跟踪信息。有助于调试、分析性能和深入了解通信过程中的数据流。 | - |
| 获取HTTP请求的时间数据 | 获取HTTP请求各阶段相关的时间信息。 | - |

## 约束与限制

支持Phone、2in1、Tablet、Wearable设备。并且从5.1.1(19)开始，新增支持TV设备；暂不支持Lite Wearable设备。

## 模拟器支持情况

本Kit支持模拟器开发，但与真机存在部分能力差异，具体差异如下：

* 通用差异：请参见“[模拟器与真机的差异](ide-emulator-specification.md#section1227613205203)”。
* 模拟器不支持使用URPC。
