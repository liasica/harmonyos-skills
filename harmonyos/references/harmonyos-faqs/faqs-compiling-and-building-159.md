---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-159
title: 编译报错“The reason attribute are mandatory for user_grant permissions.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The reason attribute are mandatory for user_grant permissions.”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:4d8b884324be8b5a78418013b97f312c3e895d39c06577a643725bc1bd5d095f
---

**错误描述**

针对Har和Hsp模块，配置user\_grant权限时必须包含reason属性。

**可能原因**

在module.json5文件中配置user\_grant类型的权限时，必须包含reason属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/VAbObV3qQIS8m3AjF_ZJhQ/zh-cn_image_0000002624638548.png)

**解决措施**

hap模块的module.json5文件中添加reason和usedScene字段。

在module.json5文件的requestPermissions中添加reason字段，用于har/hsp模块。

示例：

```json
"requestPermissions": [
      {
        "name": "ohos.permission.READ_IMAGEVIDEO",
        "usedScene": {
          "abilities": [
            "FormAbility"
          ]
        },
        "reason":"$string:location_permission_reason"
      }
    ]
```
