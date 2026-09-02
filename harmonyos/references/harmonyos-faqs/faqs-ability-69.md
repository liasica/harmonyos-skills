---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ability-69
title: 如何禁用窗口的全屏显示功能
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 程序框架（Ability） > 如何禁用窗口的全屏显示功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:55+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:246e053fb74b35f5622fd6b6ff5b17a5adb1d99a4caebc5c66ae1d3f0bed6b4a
---

在module.json5文件中配置abilities的supportWindowMode字段，用于指定窗口显示模式。

fullscreen表示支持全屏显示，split表示支持分屏显示，floating表示支持窗口化显示。

参考代码如下：

```json
"abilities": [
  {
    "name": "EntryAbility",
    "srcEntry": "./ets/entryability/EntryAbility.ets",
    "description": "$string:EntryAbility_desc",
    "icon": "$media:icon",
    "label": "$string:EntryAbility_label",
    "startWindowIcon": "$media:icon",
    "startWindowBackground": "$color:start_window_background",
    "exported": true,
    "supportWindowMode": ["split", "floating"],
    "skills": [
      {
        "entities": [
          "entity.system.home"
        ],
        "actions": [
          "ohos.want.action.home"
        ]
      }
    ]
  }
],
```

**参考链接**

[abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)
