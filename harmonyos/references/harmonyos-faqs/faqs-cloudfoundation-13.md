---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-cloudfoundation-13
title: 云托管创建站点域名中点（.）自动消失问题说明
breadcrumb: FAQ > 应用服务开发 > 云开发服务（Cloud Foundation Kit） > 云托管创建站点域名中点（.）自动消失问题说明
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:52+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c0fcd5db561fc957f287290a0f30fd57b6038133c9dfc35257746ce3fef74a14
---

## 问题现象

在云托管创建站点时，输入域名xxxxx.pay-xx-xx.xxx，创建后pay前的点（.）自动消失，显示为xxxxxpay-xx-xx.xxx。

## 解决方案

这是正常现象。云托管是一项提供内容托管的服务，包括网站托管和存储加速功能，为用户提供安全快速的内容访问能力，具体参考官网[业务介绍](../AppGallery-connect-Guides/agc-cloudhosting-introduction-0000001058210677.md)。控制台的站点名称是系统根据域名自动生成的，生成规则会自动去掉域名中的点（.）。该显示名称仅用于控制台标识，不会影响站点的实际访问、解析、配置及服务运行，可正常使用云托管服务。
