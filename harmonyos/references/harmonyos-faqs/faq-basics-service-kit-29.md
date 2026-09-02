---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-basics-service-kit-29
title: 使用request.uploadFile进行多文件上传，后台未收到文件
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 使用request.uploadFile进行多文件上传，后台未收到文件
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:39+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:5218f1f5a47437e196cb8e23c156a13dd1c0ddcd0e39aff8d0d06736572045b0
---

## 问题现象

多文件上传场景下使用[request.uploadFile](../harmonyos-references/js-apis-request.md#requestuploadfile9-1)，后台服务未收到文件，如何排查？

## 解决方案

* 检查是否调用request.uploadFile时，文件不存在于应用缓存文件路径下。
* 检查是否UploadConfig配置参数中文件的uri不是"internal://cache/"的形式。
* 检查是否后台服务将接收文件参数设置为"MultipartFile[] file"，如果后端服务接口定义接收文件参数设置为"MultipartFile[] file"，则不应使用request.uploadFile，可以使用[request.agent.create](../harmonyos-references/js-apis-request.md#requestagentcreate10)或者三方库[@ohos/axios](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Faxios)进行多文件上传。
