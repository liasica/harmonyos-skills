---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-remote-communication-3
title: "@ohos.request和rcp的上传下载功能有何区别"
breadcrumb: FAQ > 系统开发 > 网络 > 远场通信（Remote Communication） > @ohos.request和rcp的上传下载功能有何区别
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:37+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:b694521433f3aee87251774556fb41343943b189aa3a8b1a188670900e5d85d4
---

## 问题现象

@ohos.request和rcp都有上传下载功能，两者的上传下载功能有什么区别？当有上传下载需求时，如何选择？

## 背景知识

* [rcp](../harmonyos-references/remote-communication-rcp.md)模块提供HTTP数据请求功能。应用程序可通过HTTP发起数据请求。常见的HTTP方法包括GET、POST、HEAD、PUT、DELETE、PATCH、OPTIONS等。
* [request](../harmonyos-references/js-apis-request.md)模块给应用提供上传下载文件、后台代理传输的基础功能。

## 解决方案

rcp和request都有上传下载功能，但有以下区别：

| 特性 | @ohos.request | rcp |
| --- | --- | --- |
| 多文件支持 | 支持批量上传 | 仅单文件 |
| 后台传输 | 支持后台任务 | 仅前台运行 |
| 断点续传 | 自动处理 | 需手动实现 |
| 流式传输支持 | 不支持 | 支持 |
| 自定义协议 | 不支持 | 支持 |
| 自定义证书 | 不支持 | 支持 |
| 跨设备通信 | 不支持 | 支持 |
| 使用代理 | 不支持 | 支持 |

## 常见FAQ

Q：发起多个请求时，使用rcp.createSession与http.createhttp()的区别是什么？

A：

* 使用rcp.createSession与http.createhttp()的区别：
  1. rcp库请求发送能力与HTTP一致，两者使用底层库能力不同（HTTP底层使用为libcurl，rcp库底层由内部开发封装），两类型库相比较rcp上具备较好的演进性，可实现自定义证书校验，场景化传输API、服务器身份校验、NTLM校验、数字签名校验等场景能力。
  2. HTTP请求没有session，如果需要用到session，只能用rcp请求了，rcp请求的session是可以复用的session。

* rcp请求相关问题：
  1. [rcp.createSession](../harmonyos-references/remote-communication-rcp.md#createsession)创建的session可以用于发送多个网络请求，可以复用。
  2. 当用户的证书发生变化时，确实可能需要重新创建session。这是因为session可能会缓存一些认证信息，如果证书改变，这些缓存的信息可能变得无效。建议在检测到用户证书变化时，注销现有的session并重新创建一个新的session。
  3. 当网络请求出现异常时，是否需要重新创建session取决于异常的性质。如果异常是由网络问题或其他临时问题引起的，可以首先尝试重新发送请求。只有当session本身可能已损坏（例如，收到了无法恢复的错误响应）时，才需要考虑重新创建session。

## 总结

* @ohos.request（上传下载）适用场景：需后台下载、断点续传、多文件上传、大文件上传、快速实现HTTP上传下载可选@ohos.request实现。
* rcp适用场景：需快速实现单文件传输或流式处理、自定义协议、证书校验、跨设备通信或高性能传输可选rcp实现。
