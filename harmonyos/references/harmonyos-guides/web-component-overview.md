---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/web-component-overview
title: ArkWeb简介
breadcrumb: 指南 > 应用框架 > ArkWeb（方舟Web） > ArkWeb简介
category: harmonyos-guides
scraped_at: 2026-04-28T07:40:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:9cddd01db6e332f5fb6dea6f0066e7a4d2133d7e0a75629693e5cac00140af25
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

```
1. "requestPermissions":[
2. {
3. "name" : "ohos.permission.INTERNET"
4. }
5. ]
```

## 约束与限制

* 可依据ArkWeb内核版本在相关网站查询W3C标准的支持情况。例如：<https://developer.mozilla.org/en-US/> 和 <https://webassembly.org/features/> 。
* ArkWeb内核版本：ArkWeb基于谷歌Chromium内核开发，系统版本与Chromium版本的对应关系如表格所示。

  | 系统版本 | Chromium版本 |
  | --- | --- |
  | HarmonyOS 4.0及之前 | M99 |
  | HarmonyOS 4.1-5.1 | M114 |
  | HarmonyOS 6.0 | M132（默认，推荐使用）  M114（可选，若应用需切换为此内核，请参考[M114内核在HarmonyOS6.0系统上的适配指导](https://gitcode.com/openharmony-tpc/chromium_src/blob/132_trunk/web/ReleaseNote/CompatibleWithLegacyWebEngine.md)） |
  | HarmonyOS开发套件（基于API23） | M132 |
