---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-appgallery-50
title: 隐私声明和用户协议，若用户没同意该如何处理
breadcrumb: FAQ > 应用服务开发 > 应用市场服务（AppGallery Kit） > 隐私声明和用户协议，若用户没同意该如何处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7f05f732c1113624df81e0679498adeffd327300757d196a729c5310f5509746
---

## 问题现象

隐私声明和用户协议，如果用户没同意，是直接退出APP吗？可以弹出两次选择框吗？

## 解决方案

隐私声明和用户协议，若用户没同意，应用可做以下处理：

1. 方式一：用户选择不同意隐私政策，应用部分功能可以正常使用。
   * 应用部分功能不依赖用户信息和权限，可以在用户不同意隐私政策的情况下仅浏览使用；
   * 需要在隐私政策弹窗添加描述，告知用户不同意隐私政策，仅可通过游客方式浏览应用；
   * 同时添加限制策略，避免用户不同意隐私政策时应用依然能获取用户权限。
2. 方式二：用户选择不同意隐私政策，应用退出。
   * 用户拒绝隐私政策后强制终止应用实例并在任务列表中移除任务；
   * 通过[terminateSelf](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#terminateself)接口终止应用实例；
   * 同时在module.json5中设置[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)的removeMissionAfterTerminate属性清除任务快照。

若用户首次未同意隐私政策，不允许通过多次弹窗强制用户操作。
