---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/appgallery-kit-faq-0009
title: 应用上架审核稳定性驳回日志获取问题排查
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 常见问题 > 应用上架审核稳定性驳回日志获取问题排查
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:44+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:20526e22b594fa0389044b15d4a43e5ecf0ab2b0b7d37f3083ee8ed90666e564
---

**Q：应用上架因为稳定性等原因审核被驳回，应用如何获取到被驳回原因的日志来定位问题，HarmonyOS是否提供用来检测应用稳定性的工具？**

**A**：处理方式如下：

* 在[互动中心](../app/agc-help-interaction-center-0000002276985946.md)查看是否有日志附件，若没有找到相关日志，可在互动中心召唤人工咨询[处理应用审核问题](../app/agc-help-interaction-center-0000002276985946.md#section345518126011)。
* [使用Deveco Testing进行稳定性测试](../best-practices/bpta-stability-deveco-testing.md)，根据稳定性测试日志定位问题。
* 使用云测试进行[稳定性测试](../app/agc-help-cloudtest-stabilitytest-0000002254933876.md)，提供长时间遍历测试及随机测试，以检测应用在华为手机上的崩溃、冻屏、内存泄漏、进程（线程）限制、文件资源限制等稳定性问题。
