---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-cloudfoundation-10
title: 使用云数据库查询数据的时候，报“401:205525007:verify signature failed”
breadcrumb: FAQ > 应用服务开发 > 云开发服务（Cloud Foundation Kit） > 使用云数据库查询数据的时候，报“401:205525007:verify signature failed”
category: harmonyos-faqs
scraped_at: 2026-11-13T09:06:41+08:00
doc_updated_at: 2026-11-12
content_hash: sha256:ba8b24f4255b1a3e93fdba98a4b2251813d7445664dc199f859cc08d1d1b4560
---

## 问题现象

在初始化云数据库完成后，调用[query()](../harmonyos-references/cloudfoundation-clouddatabase.md#query)方法查询数据报401。具体报错信息：401:205525007:verify signature failed，如何解决？

## 解决方案

“verify signature failed ”是[Cloud Foundation Kit（云开发服务）](../harmonyos-guides/cloud-foundation-kit-guide.md)身份认证失败的典型错误，本质是：客户端生成的请求签名与服务器验证的签名不匹配，导致服务器拒绝该请求（401未授权）。

请参考以下步骤进行排查：

1. 云数据库支持的签名方式为[关联注册应用进行签名](../doccenter-deveco-studio/ide-signing-auto.md)（DevEco Studio 6.0.0 Beta5及以上版本）和[手动签名](../doccenter-deveco-studio/ide-signing-manual.md)两种方式，请确保测试包是使用上述两种方式进行签名的。
2. 如果签名方式确认无误，可以[使用模拟器调试](../harmonyos-guides/cloudfoundation-emulator.md)（API 20及以上）或者真机调试。
