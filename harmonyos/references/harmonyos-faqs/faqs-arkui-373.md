---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-373
title: 窗口Orientation枚举值8~10或12和枚举值13~16的区别
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 窗口Orientation枚举值8~10或12和枚举值13~16的区别
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:249fb1a939ffa115976af73d93174ae24e65f17a6d64f59fab0c7cb9d4b05b8d
---

1. 窗口设置8~10或12，会跟随传感器自动旋转，且受控制中心的旋转开关控制。
2. 窗口设置13~16，会临时旋转到指定方向（如：13会临时旋转到竖屏），之后跟随传感器自动旋转，受控制中心的旋转开关控制，且可旋转方向受系统判定。

两者的区别是，当窗口方向设置为13~16时，会临时旋转到指定方向，且前后台切换时窗口方向保持；而设置为8~10或12时，前后台切换时窗口方向不会保持。

**场景举例：**

1. 竖持手机，关闭旋转锁定开关 -> 应用设置方向为AUTO\_ROTATION\_RESTRICTED -> 将手机旋转为横屏（应用方向为横屏） -> 应用退到后台进入桌面，竖持手机（方向为竖屏） -> 应用切换至前台（应用方向为竖屏）。
2. 竖持手机，关闭旋转锁定开关 -> 应用设置方向为USER\_ROTATION\_PORTRAIT（应用方向为竖屏） -> 将手机旋转为横屏（应用方向为横屏） -> 应用退到后台进入桌面，竖持手机（方向为竖屏） -> 应用切换至前台（应用方向为横屏）。

| 名称 | 值 | 可旋转方向 | 是否跟随传感器自动旋转 | 是否受旋转开关控制 |
| --- | --- | --- | --- | --- |
| AUTO\_ROTATION\_RESTRICTED | 8 | 横屏、竖屏、反向竖屏、反向横屏 | 是 | 是 |
| AUTO\_ROTATION\_PORTRAIT\_RESTRICTED | 9 | 竖屏、反向竖屏 | 是 | 是 |
| AUTO\_ROTATION\_LANDSCAPE\_RESTRICTED | 10 | 横屏、反向横屏 | 是 | 是 |
| AUTO\_ROTATION\_UNSPECIFIED | 12 | 受系统判定 | 是 | 是 |
| USER\_ROTATION\_PORTRAIT | 13 | 受系统判定 | 是 | 是 |
| USER\_ROTATION\_LANDSCAPE | 14 | 受系统判定 | 是 | 是 |
| USER\_ROTATION\_PORTRAIT\_INVERTED | 15 | 受系统判定 | 是 | 是 |
| USER\_ROTATION\_LANDSCAPE\_INVERTED | 16 | 受系统判定 | 是 | 是 |
