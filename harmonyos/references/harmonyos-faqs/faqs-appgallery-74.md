---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-74
title: Publishing API更新应用软件包信息返回204144693如何解决
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > Publishing API更新应用软件包信息返回204144693如何解决
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2738e606c0adadcf0cd76beafcc1274bf7e4f269b0e85c86a8cb36c6239dc832
---

## 问题现象

* **问题1**：调用[Publishing API](../app/agc-help-publish-api-guide-0000002271134665.md)的[更新应用软件包信息](../app/agc-help-publish-api-app-package-info-update-0000002236201250.md)接口将上传的软件包绑定至应用时，返回报错：

  ```txt
  [204144693]:[AMIS] add app package failed, additional msg is [0x0c3c0063:pkg type not match with objectId suffix]
  ```
* **问题2**：调用[Publishing API](../app/agc-help-publish-api-guide-0000002271134665.md)的[提交发布](../app/agc-help-publish-api-app-submit-0000002271160585.md)接口将上传的软件包绑定至应用时，返回报错：

  ```txt
  [204144660]:[cds]submit failed, additional msg is [registeredIdType and registeredIdNumber can not be null.]"}]
  ```

## 解决方案

* **问题1**：该报错表示调用[更新应用软件包信息](../app/agc-help-publish-api-app-package-info-update-0000002236201250.md)接口时的请求参数[Body](../app/agc-help-publish-api-app-package-info-update-0000002236201250.md#section1131102811712)里面的fileName的文件后缀名填写有误，需要检查请求参数的fileName是否是以.app为后缀，如果不是需要修改为实际上传的.app为后缀的应用软件包名。
* **问题2**：该报错表示调用[更新应用基本信息](../app/agc-help-publish-api-appinfo-update-0000002236201246.md)时，请求参数[Body](../app/agc-help-publish-api-appinfo-update-0000002236201246.md#section17512144171520)中未上传“registeredIdType”和“registeredIdNumber”即备案的“主办单位类型”和“主办单位证件号”，需要在完成备案后提交这两个参数。
