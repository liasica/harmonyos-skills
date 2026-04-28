---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-374
title: 如何实现应用的屏幕自动旋转
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现应用的屏幕自动旋转
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:a390852fd1b5f68dbf71ca42b81704b3facba4d1b66b5ac2bc4c196e1d5c34d6
---

1. 在module.json5添加属性"orientation": "auto\_rotation"。

   如下所示：

   ```
   1. "abilities": [
   2. {
   3. "name": "EntryAbility",
   4. "srcEntry": "./ets/entryability/EntryAbility.ets",
   5. "description": "$string:EntryAbility_desc",
   6. "icon": "$media:icon",
   7. "label": "$string:EntryAbility_label",
   8. "startWindowIcon": "$media:startIcon",
   9. "startWindowBackground": "$color:start_window_background",
   10. "exported": true,
   11. "skills": [
   12. // ...
   13. ],
   14. "orientation": "auto_rotation", // Rotate with the sensor
   15. }
   16. ],
   ```

   [auto\_rotation.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/auto_rotation.json5#L20-L44)
2. 打开手机自动旋转功能，操作步骤：进入手机控制中心 > 关闭旋转锁定。

**参考链接**

[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)
