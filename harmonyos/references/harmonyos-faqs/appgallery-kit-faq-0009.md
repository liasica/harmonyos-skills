---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/appgallery-kit-faq-0009
title: 应用上架审核稳定性驳回日志获取问题排查
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 常见问题 > 应用上架审核稳定性驳回日志获取问题排查
category: harmonyos-faqs
scraped_at: 2026-11-13T09:06:38+08:00
doc_updated_at: 2026-11-12
content_hash: sha256:a7c2f85a8f0eaa4ca9b5c6708b7ca7c8a697233a51409ecad01deade978423c3
---

**Q：应用上架因为稳定性等原因审核被驳回，应用如何获取到被驳回原因的日志来定位问题，HarmonyOS是否提供用来检测应用稳定性的工具？**

**A**：处理方式如下：

* 在[互动中心](../doccenter-submission/50000-1.md#section7366111721215)查看是否有日志附件，若没有找到相关日志，可在互动中心召唤人工咨询[处理应用审核问题](../doccenter-submission/50000-1.md#section7366111721215)。
* [使用Deveco Testing进行稳定性测试](../best-practices/bpta-stability-deveco-testing.md)，根据稳定性测试日志定位问题。
* 使用云测试进行[稳定性测试](../app/agc-help-cloudtest-stabilitytest-0000002254933876.md)，提供长时间遍历测试及随机测试，以检测应用在华为手机上的崩溃、冻屏、内存泄漏、进程（线程）限制、文件资源限制等稳定性问题。
