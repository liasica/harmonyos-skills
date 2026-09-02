---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-debugging-79
title: 云调试应用期间出现黑屏如何处理
breadcrumb: FAQ > DevEco Studio > 应用调试 > 云调试应用期间出现黑屏如何处理
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3cc0c9204b39150c1b4ba59ba047f14e10658927d2f6226d9be4030fda678c57
---

## 问题现象

* **问题一：**

  云真机设备勾选隐私政策后，进入登录页面时，云真机一直黑屏是什么原因？
* **问题二：**

  为什么调试期间调试设备出现了黑屏？

## 解决方案

* **问题一解决方案**：

  由于应用自身登录页设置了防截屏，此时云真机会显示黑屏，有两种方案可选：

  1. 可以重新打包将防截屏开关关闭，参考文档[如何实现防截屏功能](faqs-arkui-3.md)。
  2. 通过点击“获取控件树”按钮启动辅助控件绘制功能来完成账号登录。详情请参见[使用获取控件树按钮完成登录](../app/agc-help-clouddebug-debugapp-0000002289629821.md#section1851413117162)。
* **问题二解决方案：**

  详情请参见[为什么调试期间调试设备出现了黑屏](../app/agc-help-clouddebug-faq-0000002254916526.md#section104351522193512)。
