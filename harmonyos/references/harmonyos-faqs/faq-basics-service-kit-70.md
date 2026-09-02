---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-70
title: 使用@ohos.request的request.agent上传文件，如何获得响应体
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 使用@ohos.request的request.agent上传文件，如何获得响应体
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a6f644ca237351b2acc732f5aeff7efc36e610a696ddf1c31f9528debf83eb0d
---

## 问题现象

使用@ohos.request上传文件，参考[文档中的方式2](../harmonyos-guides/app-file-upload-download.md)编码，无法拿到响应体。

当前把响应体放到响应头里，监听[on('response')](../harmonyos-references/js-apis-request.md#onresponse12)规避。

## 背景知识

上传下载是应用常见功能，常见的办法有几种。

1. 使用@ohos.request。

   链接：[@ohos.request (上传下载)-数据文件处理-ArkTS API-Basic Services Kit（基础服务）-基础功能-系统 - 华为HarmonyOS开发者](../harmonyos-references/js-apis-request.md)。
2. 使用network kit。

   链接：[@ohos.net.http (数据请求)-ArkTS API-Network Kit（网络服务）-网络-系统 - 华为HarmonyOS开发者](../harmonyos-references/js-apis-http.md)。
3. 使用RCP（推荐）

   链接：[上传下载文件-远场通信场景-Remote Communication Kit（远场通信服务）-网络-系统 - 华为HarmonyOS开发者](../harmonyos-guides/remote-communication-filetransferfast.md)。

当前，使用HTTP/HTTPS的端云通信的场景，推荐使用RCP。

## 问题定位

由于历史原因，@ohos.request的API设计容易让人困惑：

1. 从命名上看，[onResponse](../harmonyos-references/js-apis-request.md#onresponse12)的回调应该是在响应完全接受完毕后触发，实际上为接收完header后触发。
2. onResponse回调入参类型为HttpResponse，但是其中没有Body，仅有header。
3. 从命名上看，[onComplete](../harmonyos-references/js-apis-request.md#oncomplete--fail9)是在上传过程彻底完成后的回调，开发者在回调中应该重点关注完成的状态，以及执行必须在上传完毕后要执行的逻辑。

既然onResponse的入参[HttpResponse](../harmonyos-references/js-apis-request.md#requestagenthttpresponse12)不含Body，查找文档确认在[onComplete](../harmonyos-references/js-apis-request.md#oncompleted10)的回调入参[Progress](../harmonyos-references/js-apis-request.md#requestagentprogress10)中是否有响应体。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/jTT0K2ueSTuMuU9ARACMWw/zh-cn_image_0000002628774288.png "点击放大")

确认Progress中有响应体。

## 分析结论

在onComplete的Progress对象的extra属性中，可以拿到响应体。

## 修改建议

经过验证，在onComplete的Progress对象的extra属性中，可以拿到响应体。代码可以参考[on('completed')](../harmonyos-references/js-apis-request.md#oncompleted10)的示例，打印onComplete的Progress对象拿到extra属性。

## 总结

1. 使用@ohos.request的request.agent方式上传文件，在onResponse的回调的HttpResponse对象中拿响应头，在onComplete回调的Progress对象中拿响应体。
2. 建议使用RCP处理上传和下载：[上传下载文件-远场通信场景-Remote Communication Kit（远场通信服务）-网络-系统 - 华为HarmonyOS开发者](../harmonyos-guides/remote-communication-filetransferfast.md)。

## 常见FAQ

Q：目前axios三方库是否支持文件上传。

A：目前axios三方库支持文件上传，参考[@ohos/axios](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Faxios)。

Q：@ohos.request (下载)[Progress](../harmonyos-references/js-apis-request.md#onprogress-1)的sizes返回-1的问题。

A：在下载过程中，若服务器使用chunk方式传输导致无法从请求头中获取文件总大小时，sizes为-1。

总大小，是从服务器返回的响应头里面的Content-Length获取的，如果服务器的响应头里面没有Content-Length，那下载过程中不知道响应体的大小的，sizes为-1。

Q：request.agent相关接口底层是否会复用tcp链接。

A：是否复用连接取决于多个条件：不同请求是否连接到同一IP和端口、连接是否保持未中断，以及HTTP版本是否为HTTP/2。只有在请求绑定相同IP和端口、连接未断开且使用HTTP/2的情况下，才会进行连接复用。
