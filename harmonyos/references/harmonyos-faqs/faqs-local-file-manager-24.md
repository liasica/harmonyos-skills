---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-file-manager-24
title: 使用request.uploadFile上传文件后，没有回调可以获取到服务器返回的message信息，不能明确知道文件是否上传成功
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地文件管理 > 使用request.uploadFile上传文件后，没有回调可以获取到服务器返回的message信息，不能明确知道文件是否上传成功
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:27+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:150f46cbdce9582fea3a61ecf42e000530e56c62c7e3e78aad359548d523d1c3
---

使用request.uploadFile上传文件时，on('complete')回调在成功后触发。如果需要获取服务端的响应信息并处理判断逻辑，还可以使用on('headerReceive')回调。

**参考链接**

[on('complete' | 'fail')](../harmonyos-references/js-apis-request.md#oncomplete--fail9)

[on('headerReceive')](../harmonyos-references/js-apis-request.md#onheaderreceive7)
