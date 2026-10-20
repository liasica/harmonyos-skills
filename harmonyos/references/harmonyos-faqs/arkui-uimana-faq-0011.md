---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0011
title: 如何判断当前设备是手机还是折叠屏手机
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > 如何判断当前设备是手机还是折叠屏手机
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:10+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:d8c5c62ef558b1481d07ec168fabb0cba2c96c6b37dbfe4d0aeec61520ed3f0d
---

**Q：如何判断当前设备是手机还是折叠屏手机？**

**A**：判断当前设备是手机还是折叠屏手机的方法如下：

* 页面布局类问题：页面布局应基于窗口形态（如折叠态/展开态）、宽度和高宽比等动态属性，而非静态设备类型。例如折叠屏设备的折叠态窗口应使用与普通手机相同的布局规则，Mate X5展开态单独设计一套布局。详情可参考[断点](../best-practices/bpta-multi-device-responsive-layout.md#section1532120147301)的使用。
* 非页面布局或功能类问题（例如折叠屏折叠状态切换时重新选择相机重置预览流）：手机设备（包括普通手机和折叠屏手机）的[DeviceTypes](../harmonyos-references/js-apis-device-info.md#devicetypes20)接口均返回phone，可以通过屏幕属性@ohos.display的[display.isFoldable](../harmonyos-references/js-apis-display.md#displayisfoldable10)返回是否可折叠。需要注意HUAWEI Pocket 2（纵向折叠屏手机）的isFoldable接口会返回false，需特殊处理。

折叠屏相关的具体开发案例可参考：[折叠屏应用开发](../best-practices/bpta-foldable-guide.md)。
