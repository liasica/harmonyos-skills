---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/share-faq-1
title: 拉起系统分享框失败
breadcrumb: 指南 > 应用服务 > Share Kit（分享服务） > Share Kit常见问题 > 拉起系统分享框失败
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:33+08:00
doc_updated_at: 2026-06-27
content_hash: sha256:6a883c73c9cb73701c8e23029c29967491bcfc9c1941ebe6fe9d3d7180dddb2f
---

**现象描述：**

无法拉起系统分享框

**可能原因：**

1. 使用API不当，API抛出了异常，导致无法拉起。
2. 其他模块出现异常，导致无法拉起，需要具体问题具体分析。

**处理步骤：**

1. 首先排查是否是分享服务API使用不当导致抛出异常，具体参考[分享服务API](../harmonyos-references/share-system-share.md)和[错误码](../harmonyos-references/share-error-code.md)，找到问题后修改代码。
2. 如果是其他模块出现异常，查看是否有faultlog，有的话可以根据faultlog中的模块排查问题。如果没有，请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题。
3. 如果难以定位，也请通过[在线提单](https://developer.huawei.com/consumer/cn/support/feedback/#/)提交问题，华为支持人员会及时处理。
