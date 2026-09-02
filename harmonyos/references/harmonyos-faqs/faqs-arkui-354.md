---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-354
title: 如何在系统深色模式下使用getColorSync(resource)返回深色颜色值
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何在系统深色模式下使用getColorSync(resource)返回深色颜色值
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:28+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:477b4b910a8e6064b0552604add68fa28d49116f6fb21e6287c2aac067dd547b
---

目前有两种方案可供参考：

1. 传递资源ID。

   ```typescript
   this.getUIContext().getHostContext()?.resourceManager.getColorSync($r('app.color.xxx').id);
   ```
2. 在配置了dark限定词目录的包的module.json5文件中添加配置。

   ```json
   "metadata": [
     {
       "name": "ContextResourceConfigLoadFromParentTemp",
       "value": "true"
     }
   ],
   ```
