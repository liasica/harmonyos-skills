---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-354
title: 如何在系统深色模式下使用getColorSync(resource)返回深色颜色值
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何在系统深色模式下使用getColorSync(resource)返回深色颜色值
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:1e348ce9f778686f60baf782359ef37b793800d759cfc907ebf7601ab13c9c5a
---

目前有两种方案可供参考：

1. 传递资源ID。

   ```
   1. this.getUIContext().getHostContext()?.resourceManager.getColorSync($r('app.color.xxx').id);
   ```

   [GetDarkModeColorSync.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/GetDarkModeColorSync.ets#L21-L21)
2. 在配置了dark限定词目录的包的module.json5文件中添加配置。

   ```
   1. "metadata": [
   2. {
   3. "name": "ContextResourceConfigLoadFromParentTemp",
   4. "value": "true"
   5. }
   6. ],
   ```

   [module.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/module.json5#L81-L86)
