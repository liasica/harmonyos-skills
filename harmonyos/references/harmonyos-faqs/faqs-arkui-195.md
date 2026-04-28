---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-195
title: 调用window实例的setWindowSystemBarProperties接口设置窗口状态栏和导航栏的高亮属性时不生效
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 调用window实例的setWindowSystemBarProperties接口设置窗口状态栏和导航栏的高亮属性时不生效
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:52+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:61c41be9d924e2d45e5b5ffa5386737af4cc303cfab5a93745f2382b33a89760
---

**问题现象**

调用window实例的setWindowSystemBarProperties接口时，设置isStatusBarLightIcon和isNavigationBarLightIcon属性无效。

**解决措施**

状态栏字体高亮属性的作用是将字体变为白色。调用window实例的 setWindowSystemBarProperties接口时，如果设置了状态栏内容颜色statusBarContentColor，则以开发者设置的颜色为准，isStatusBarLightIcon属性将不生效。同理，如果设置了导航栏内容颜色 navigationBarContentColor，isNavigationBarLightIcon属性也将不生效。

**参考链接**

[window.setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)
