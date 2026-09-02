---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-64
title: request上传文件后headerReceive内容无法解析
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > request上传文件后headerReceive内容无法解析
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5487238fd9c4c24009ff1c115f2b90004d2aa6d17aaff3f1aa9be53161d210ed
---

## 问题现象

[request](../harmonyos-references/js-apis-request.md)上传文件后通过[on('headerReceive')](../harmonyos-references/js-apis-request.md#onheaderreceive7)获取headerReceive内容：

```json
{ "headers": {},"body": "{"code ":0,"msg ":"操作成功","data ":{"name ":"file.png ","url ":"","path ":""}}"}
```

使用JSON序列化解析，报错Error message:Unexpected Object in JSON：

```ts
let headerObject: RequestUploadHeaderInterface = JSON.parse(headersStr)
```

## 解决方案

通过JSON校验工具可以看出，需要序列化的内容不是正规的JSON字符串，若在已知响应内容的情况下，通过属性名的字符串形式获取body对象的属性，再用JSON序列化，如：JSON.parse(headersStr["body"])。
