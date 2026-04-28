---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-392
title: 如何实现加载svga动画
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现加载svga动画
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:43+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:547daf859baba8cf3739d4da19abece4c7e587feee2c633cfec57da8a5fc5bfa
---

**问题描述**

在应用中存在多个页面会使用svga播放图片、动效、动画等。请问HarmonyOS怎么加载svga动画？

**解决措施**

当前HarmonyOS原生API尚未支持svga格式动画的解析，实现加载svga动画可以参考以下方案：

* 先将svga格式转换成[lottie](https://gitcode.com/openharmony-tpc/lottieArkTS)和[@tencent/libpag](https://ohpm.openharmony.cn/#/cn/detail/@tencent%2Flibpag)支持的格式，再通过对应库加载。
* 使用[web](../harmonyos-references/ts-basic-components-web.md)组件提供网页显示的方式来接入，在h5页面中使用相关播放器加载svga动画。

推荐使用svga2lottie等转换工具执行格式转换。
