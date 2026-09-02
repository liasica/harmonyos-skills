---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-62
title: 应用误删后的恢复与重新创建方式
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用误删后的恢复与重新创建方式
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:d4922a156af4bd8e0c5beae6b3315cdaf58c4601d8fc679a2b4c324331afae9e
---

## 问题现象

1. 误删应用后，有什么办法恢复吗？如果不能的话要怎么办？
2. 删除应用后包名是否立即释放，能否使用相同包名重新创建AppID？重新创建后现有发布证书和调试证书是否可以继续使用？

## 解决方案

问题一：删除操作不可逆，无法恢复。删除应用/元服务后，系统会彻底移除所有关联数据（包括AppID），不支持任何形式的恢复或撤销操作。点击删除确认后，系统将立即跳转至应用列表页，该应用不再展示。如已误删，必须在AppGallery Connect中重新创建应用。

问题二：删除应用后包名会立即释放，可以使用相同包名重新创建AppID。现有发布证书和调试证书可以继续使用，但Profile文件必须重新申请。重新创建后还需重新配置应用签名、服务开通等信息，完成开发后需再次走提审、测试、上架流程。
