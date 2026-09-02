---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-69
title: request.uploadFile多文件上传的特点
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > request.uploadFile多文件上传的特点
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:04f178a5e9a1e6ca3db1f27bfca11233d266aebce8ed71efc2b34d3018b5a82e
---

## 问题现象

如何使用request.uploadFile接口上传多个文件以及注意事项有哪些？

## 背景知识

[request.uploadFile](../harmonyos-references/js-apis-request.md#requestuploadfile9-1)创建并启动一个上传任务，需要[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)权限。

## 解决方案

使用[request.uploadFile](../harmonyos-references/js-apis-request.md#requestuploadfile9-1)接口上传文件时，通过设置[UploadConfig](../harmonyos-references/js-apis-request.md#uploadconfig)中的files参数即可实现多文件上传。上传多个文件时会发起多次请求，每个文件上传完都会触发一次[on('headerReceive')](../harmonyos-references/js-apis-request.md#onheaderreceive7)响应事件。

常见注意事项如下：

* [UploadConfig](../harmonyos-references/js-apis-request.md#uploadconfig)中的files参数中的uri仅支持"internal://cache/"，即调用方（传入的context）对应的缓存路径。
* 若后台服务将接收文件参数设置为"MultipartFile"类型，可以使用[request.agent.create](../harmonyos-references/js-apis-request.md#requestagentcreate10)接口，将[request.agent.Config](../harmonyos-references/js-apis-request.md#requestagentconfig10)里的multipart参数设置为true进行多文件上传。

除上述方法外，常见其他多文件上传方法有：

* 使用ohos.net.http模块，通过设置multiFormDataList参数进行多个文件列表上传，参考示例：[完整示例](../harmonyos-references/js-apis-http.md#完整示例)。
