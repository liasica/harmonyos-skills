---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-69
title: 申请发布证书时提示上传的CSR文件无效怎么办
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 申请发布证书时提示上传的CSR文件无效怎么办
category: harmonyos-faqs
scraped_at: 2026-11-13T09:06:40+08:00
doc_updated_at: 2026-11-12
content_hash: sha256:7464f02026e31e381357bb5f5442d35138d3b3c6ca1cd34504cbe447eb2cb4d6
---

## 问题现象

[申请发布证书](../app/agc-help-release-cert-0000002283336729.md)时需要上传CSR文件，但是提示“上传的CSR文件无效，请重新上传”，请问如何解决？

## 解决方案

CSR文件无效，说明文件不完整，常见的原因是未使用正确的生成方式。比如在[准备申请签名所需文件](../harmonyos-guides/ide-command-line-building-app.md#section6103553181714)时，使用Keytool工具生成密钥和证书请求文件未将-keyalg参数设置为“EC”，导致生成的CSR文件使用了错误的密钥算法。

如果使用Keytool工具生成CSR文件建议检查各个参数项。或者使用开发工具按照[生成密钥和证书请求文件](../doccenter-deveco-studio/ide-signing-manual.md#section1245916381106)步骤重新生成CSR文件。
