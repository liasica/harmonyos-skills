---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-component-overview
title: ArkWeb简介
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > ArkWeb简介
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:54+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:d8d3565103534c2bbd83e3e9f8c3ee750bd3495e8d0ae8e5228a2bf0417ce058
---

## 使用场景

ArkWeb（方舟Web）提供了Web组件，用于在应用中显示Web页面内容。常见使用场景包括：

* 应用集成Web页面：应用可以在界面中使用Web组件，嵌入Web页面内容，以降低开发成本，提升开发、运维效率。
* 浏览器网页浏览场景：浏览器类应用可以使用Web组件，打开三方Web网页，使用无痕浏览模式浏览Web页面，设置广告拦截等。
* 小程序：小程序类宿主应用可以使用Web组件，渲染小程序的页面，实现同层渲染，视频托管等小程序的功能。

## 能力范围

Web组件为开发者提供了丰富的控制Web页面能力。包括：

* Web页面加载：声明式加载Web页面和离屏加载Web页面等。
* 生命周期管理：组件生命周期状态变化，通知Web页面的加载状态变化等。
* 常用属性与事件：[User-Agent开发指导](web-default-useragent.md)、[管理Cookie及数据存储](web-cookie-and-data-storage-mgmt.md)、字体与[Web深色模式适配](web-set-dark-mode.md)、权限管理等。
* 与应用界面交互：自定义文本选择菜单、上下文菜单、文件上传界面等与应用界面交互能力。
* 应用通过JavaScriptProxy，与Web页面进行JavaScript交互。
* 安全与隐私：无痕浏览模式、广告拦截、坚盾守护模式等。
* 维测能力：[DevTools工具](web-debugging-with-devtools.md)调试能力，使用crashpad收集Web组件崩溃信息、定位与解决Web白屏问题、使用Hypium实现ArkWeb自动化测试。
* 其他高阶能力：与系统组件同层渲染、Web组件的网络托管、Web组件的媒体播放托管、Web组件输入框拉起自定义输入法、[网页接入密码保险箱](arkweb-access-password-safe.md)等。

## 需要权限

使用Web组件访问在线Web网页时需添加网络权限：ohos.permission.INTERNET，具体申请方式请参考[声明权限](declare-permissions.md)。

```ts
"requestPermissions":[
    {
      "name" : "ohos.permission.INTERNET"
    }
  ]
```

## 约束与限制

* 可依据ArkWeb内核版本在相关网站查询W3C标准的支持情况。例如：<https://developer.mozilla.org/en-US/> 和 <https://webassembly.org/features/> 。
* ArkWeb内核版本：ArkWeb基于谷歌Chromium内核开发，系统版本与Chromium版本的对应关系如表格所示。

  | 系统版本 | Chromium版本 |
  | --- | --- |
  | HarmonyOS 4.0及之前 | M99 |
  | HarmonyOS 4.1-5.1 | M114 |
  | HarmonyOS 6.0 | M132（默认，推荐使用，请参考[M114->M132差异适配指南](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/web/ReleaseNote/ArkWeb_114_132.md)）  M114（可选，若应用需切换为此内核，请参考[M114内核在HarmonyOS 6.0系统上的适配指导](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/web/ReleaseNote/CompatibleWithLegacyWebEngine_6.0.md)） |
  | HarmonyOS 6.1 | M132 |
  | HarmonyOS 7.0 | M144（默认，推荐使用，请参考[M132->M144差异适配指南](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/web/ReleaseNote/ArkWeb_132_144.md)）  M132（可选，若应用需切换为此内核，请参考[M132内核在HarmonyOS 7.0系统上的适配指导](https://gitcode.com/openharmony-tpc/chromium_src/blob/master/web/ReleaseNote/CompatibleWithLegacyWebEngine_7.0.md)） |
* 为保障用户隐私安全，HarmonyOS内置了ArkWeb组件，旨在为全场景设备提供安全、可靠且一致的网页浏览体验。应用渲染网页需调用ArkWeb组件；元服务内嵌网页渲染则需使用官方提供的Webview组件。开发者可根据其元服务开发框架，选择使用[ASCF Webview](../atomic-ascf/develop-web-view.md)或[AtomicServiceEnhancedWeb](../atomic-guides/atomicserviceweb-guidelines.md#atomicserviceenhancedweb)组件。元服务内嵌页面内容需遵循元服务内嵌页面管理规范。

## 模拟器支持情况

* 本Kit支持模拟器。模拟器与真机存在通用差异，详情请参见“[模拟器与真机的差异](ide-emulator-specification.md)”。
