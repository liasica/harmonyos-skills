---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-374
title: 如何实现应用的屏幕自动旋转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 屏幕管理 > 如何实现应用的屏幕自动旋转
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:13+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9bf05ae8d88206b3c518e26e2a766c2380e6df27dabc00f543f91e0d60675ad0
---

1. 在module.json5添加属性"orientation": "auto\_rotation"。

   如下所示：

   ```json
   "abilities": [
     {
       "name": "EntryAbility",
       "srcEntry": "./ets/entryability/EntryAbility.ets",
       "description": "$string:EntryAbility_desc",
       "icon": "$media:icon",
       "label": "$string:EntryAbility_label",
       "startWindowIcon": "$media:startIcon",
       "startWindowBackground": "$color:start_window_background",
       "exported": true,
       "skills": [
         // ...
       ],
       "orientation": "auto_rotation", // Rotate with the sensor
     }
   ],
   ```
2. 打开手机自动旋转功能，操作步骤：进入手机控制中心 > 关闭旋转锁定。

**参考链接**

[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)
