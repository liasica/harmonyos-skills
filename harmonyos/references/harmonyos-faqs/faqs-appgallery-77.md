---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-77
title: Publishing API提交应用返回204144660的几种场景和解决方法
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > Publishing API提交应用返回204144660的几种场景和解决方法
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:794dd15a07837cd2390b1406f9c4deafbaea5b4ce97dd64c295ab16a96e16a04
---

## 问题现象

调用Publishing API的提交应用接口，返回同一个错误码“204144660”，但是错误信息不同，分别对应哪些场景，如何解决？

问题1.调用[Publishing API](../app/agc-help-publish-api-guide-0000002271134665.md)的[提交发布](../app/agc-help-publish-api-app-submit-0000002271160585.md)接口时，返回报错：

```screen
[204144660]: [cds]submit failed, additional msg is [registeredEntity and registeredEntityName can not be empty.]
```

问题2.调用[Publishing API](../app/agc-help-publish-api-guide-0000002271134665.md)的[提交发布](../app/agc-help-publish-api-app-submit-0000002271160585.md)接口时，返回报错：

```screen
[204144660]: [cds]submit failed, additional msg is [The history of questionnaire feedback content ratings is empty .]
```

问题3.调用[Publishing API](../app/agc-help-publish-api-guide-0000002271134665.md)的[提交发布](../app/agc-help-publish-api-app-submit-0000002271160585.md)接口时，返回报错：

```screen
[204144660]:[cds]submit failed, additional msg is []
```

## 解决方案

问题1.需要在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)保存过“registeredDclType”、“registeredEntity”、“registeredEntityName”即“APP类型信息”、“主办单位”、“主办单位名称”三个字段后再进行操作。

问题2.在软件上架前需要完成年龄分级的问卷，该问卷无法通过API完成，需要登录[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)完成。此问卷仅需要完成一次，完成问卷后重试。

问题3.调用该接口前，确保应用信息完整，且已上传应用软件包。应用软件包的解析是异步的，上传完成后，建议在上传软件包后轮询[查询软件包编译状态](../app/agc-help-publish-api-query-compile-status-0000002236041434.md)，确认包解析完成后，再调用发布接口。
