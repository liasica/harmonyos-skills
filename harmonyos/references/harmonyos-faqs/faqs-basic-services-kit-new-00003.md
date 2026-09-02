---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-basic-services-kit-new-00003
title: 打印场景如何通过软件设置自动选择打印机纸盒
breadcrumb: FAQ > 系统开发 > 基础功能 > 基础服务（Basics Service） > 打印场景如何通过软件设置自动选择打印机纸盒
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-07-22
content_hash: sha256:f328a434ed7216bf56f3c262cc25eba874eeda124192b01c82f8b3ef3a0d551d
---

## 问题现象

在打印场景中，需要打印不同尺寸、不同类型的纸张时，如何通过软件设置让打印机自动从正确的纸盒取纸，无需每次手动更换打印机物理纸盒里的纸张？

## 解决方案

该功能已在HarmonyOS 7.0 beta1版本交付，可通过[@ohos.print](../harmonyos-references/js-apis-print.md)模块中的 PrintAttributes 接口设置纸盒选择策略。在调用 print() 接口启动打印任务时，构建 PrintAttributes 对象并配置 mediaSize（纸张尺寸）和 inputTray（纸盒来源，设为自动匹配策略）属性，系统将根据这些配置自动从正确纸盒取纸。请申请对应版本进行验证。
