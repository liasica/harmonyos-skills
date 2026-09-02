---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-cloudfoundation-5
title: 使用云存储进行身份验证如何获取用户ID
breadcrumb: FAQ > 应用服务开发 > 云开发服务（Cloud Foundation Kit） > 使用云存储进行身份验证如何获取用户ID
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:dcbc5a1f5a1d532ccadb5c25d4e51e133b970b56bcf47d46a58c4d49f8f826e3
---

## 问题现象

开发完应用后，进行私有化的存储文件访问控制，需要进行[用户身份认证](../AppGallery-connect-Guides/agc-cloudstorage-securityrules-userbasedsecurity-0000001055566792.md#section1117214372511)，校验通过后，使用用户的uid填充request.auth.uid变量，以此获得访问的权限。这个uid是怎么获取？是否是认证服务获取的[getCurrentUser](../app/agc-help-auth-api-auth-0000002273777093.md#section87068861218)信息呢？

## 解决方案

这个uid和认证服务的[getCurrentUser](../app/agc-help-auth-api-auth-0000002273777093.md#section87068861218)信息无关，可以使用华为账号用户的UnionID做认证，具体获取方式参考[华为账号登录（获取UnionID/OpenID）](../harmonyos-guides/account-unionid-login.md)。
