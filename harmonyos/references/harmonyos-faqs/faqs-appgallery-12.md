---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-12
title: 重新生成profile发布的应用，是否会影响安装之前发布的应用
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 重新生成profile发布的应用，是否会影响安装之前发布的应用
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:50+08:00
doc_updated_at: 2026-07-09
content_hash: sha256:1c0488c1d637e7e224d29f23ad2390ad3cd256298e15e208b579b04c55119ad2
---

## 问题现象

问题一：

重新生成发布profile（发布配置文件）的应用，是否可以覆盖安装之前发布的应用？

问题二：

发布profile重新添加ACL（访问控制列表）权限后是否需要更换数字证书（.cer）？

问题三：

AGC平台cer证书被删除，导致profile证书失效，本地csr（证书签名请求）文件也被删除，重新生成一套新的证书会影响已上架的版本吗？

问题四：

AGC平台重新生成profile成功后有下载按钮，为什么一段时间后刷新网页下载按钮消失？

## 解决方案

问题一：

重新生成profile发布的应用，安装不会受到影响，是可以覆盖安装之前发布的应用。

问题二：

发布profile重新添加ACL权限不会影响数字证书（.cer），所以不用更换数字证书，但是profile需要重新下载使用。

问题三：

APPID不变的情况下重新生成一套证书不会影响应用升级。如果APPID发生变化则需要确保密钥库文件（.p12）不变。

问题四：

出于对开发者信息安全的考虑，profile证书仅更新当天可下载。
