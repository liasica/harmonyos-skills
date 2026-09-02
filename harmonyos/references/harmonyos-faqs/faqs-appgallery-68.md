---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-68
title: 应用上架必须通过AppFreeze异常检测吗
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 应用上架必须通过AppFreeze异常检测吗
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7135c29d3beed0616161b3292b6b78e6605003ee63a51ff946f74299a1155c3c
---

## 问题现象

HarmonyOS应用上架必须通过AppFreeze异常检测吗，团结引擎开发的3D游戏也需要通过这个检测吗？

## 解决方案

HarmonyOS应用上架需要经过兼容性，稳定性等自动化检测，其中稳定性包含应用的Crash，AppFreeze等检测项。AppFreeze检测是应用上架审核的核心指标，该检测针对应用的主线程响应能力、用户输入反馈等核心性能指标进行验证。为了提高应用的质量，所有应用类型，包括开发框架是团结引擎的应用均要进行AppFreeze异常检测且需要满足审核标准。
