---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-16
title: 应用上架审核因稳定性被驳回如何获取相应的日志定位问题
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用上架审核因稳定性被驳回如何获取相应的日志定位问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f46546eaa4a825b8ddd59d362f9d7efa7184c594600e966be52837d1e36f6310
---

## 问题现象

应用上架因为稳定性等原因审核被驳回，应用如何获取到被驳回原因的日志来定位问题，HarmonyOS是否提供用来检测应用稳定性的工具？

## 解决方案

* 在[互动中心](../app/agc-help-interaction-center-0000002276985946.md)查看是否有日志附件，若没有找到相关日志，可在互动中心召唤人工咨询[处理应用审核问题](../app/agc-help-interaction-center-0000002276985946.md#section345518126011)。
* [使用Deveco Testing进行稳定性测试](../best-practices/bpta-stability-deveco-testing.md)，根据稳定性测试日志定位问题。
* 使用云测试进行[稳定性测试](../app/agc-help-cloudtest-stabilitytest-0000002254933876.md)，提供长时间遍历测试及随机测试，以检测应用在华为手机上的崩溃、冻屏、内存泄漏、进程（线程）限制、文件资源限制等稳定性问题。
