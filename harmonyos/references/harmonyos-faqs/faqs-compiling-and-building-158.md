---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-158
title: 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“The reason and usedScene attributes are mandatory for user_grant permissions.”
category: harmonyos-faqs
scraped_at: 2026-10-28T07:48:55+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:c755a43d611637b8c3aa8548e228b375d2a011c1748c5fc8d893aa89b000aabf
---

**错误描述**

针对Hap模块，配置user\_grant权限时必须包含reason和usedScene属性。

**可能原因**

在module.json5文件中配置user\_grant类型的权限时，必须包含reason和usedScene属性。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/-CcC7vzZS3uL_N0tQWvG-g/zh-cn_image_0000002654797997.png)

**解决措施**

对于Hap模块，在module.json5文件的requestPermissions中添加reason和usedScene字段。

对于Har/Hsp模块，在module.json5文件的requestPermissions中添加reason字段。

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
