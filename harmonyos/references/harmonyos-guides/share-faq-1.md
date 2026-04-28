---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-faq-1
title: 拉起系统分享框失败
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > Share Kit常见问题 > 拉起系统分享框失败
category: harmonyos-guides
scraped_at: 2026-04-28T07:51:05+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:efb510aa5cdf87207ccb2afd68df5ee0fc07555c27d4295d125794b0bb9f8c61
---

**现象描述：**

无法拉起系统分享框

**可能原因：**

1. 使用API不当，API抛出了异常，导致无法拉起。
2. 其他模块出现异常，导致无法拉起，需要具体问题具体分析。

**处理步骤：**

1. 首先排查是否是分享API使用不当导致抛出异常，具体参考[分享服务API](../harmonyos-references/share-system-share.md)和[错误码](../harmonyos-references/share-error-code.md)，找到问题后修改代码。
2. 如果是其他模块出现异常，查看是否有faultlog，有的话可以根据faultlog中的模块排查问题。如果没有，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
3. 如果难以定位，也请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。
