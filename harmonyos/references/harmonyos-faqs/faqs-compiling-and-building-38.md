---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-38
title: 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:52+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:5598703773a709b7b3a3aef2dd574e7390cf3bf739cbe7dab42eb58c90fa5832
---

**问题现象**

DevEco Studio编译失败，提示“The reason and usedScene attributes are mandatory for user\_grant permissions”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/nafZzBx9TM-GYIZLAukLGg/zh-cn_image_0000002654797867.png "点击放大")

**问题原因**

从DevEco Studio NEXT Developer Preview 2版本开始，新增规则：APP包中，所有entry和feature hap的module下的requestPermissions权限清单必须指定（可以为空，若非空则name必填；user\_grant权限则必填reason和usedScene字段）。

**解决措施**

进入对应module.json5文件中，补齐requestPermissions字段下的reason和usedScene字段。如以下示例：

```json
"requestPermissions": [
  {
    "name": "ohos.permission.READ_IMAGEVIDEO",
    "reason": "$string:module_desc",
    "usedScene": {
      "abilities": [
        "EntryAbility"
      ],
      "when": "inuse"
    }
  }
],
```
