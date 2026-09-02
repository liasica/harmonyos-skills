---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-11
title: 编译报错“Property xxx does not exist on type 'typeof BuildProfile'.”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译报错“Property xxx does not exist on type 'typeof BuildProfile'.”
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:7cf2386531ebf800f096e418a555d9cca1bd12a3fde4cfbfc8a7cd9f02f8753f
---

**问题现象****1**

使用自定义参数BuildProfile时，编译过程中未出现异常，但编译构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/ZEzpw1koSu-OXvWQbYn1CA/zh-cn_image_0000002624638386.png)

**解决措施**

检查当前模块下build-profile.json5文件中targets>buildProfileFields配置的自定义参数的key值是否一致。如果不一致，请将targets内所有buildProfileFields的key值统一。

以下为导致编译报错的配置示例：

```json
"targets": [
  {
    "name": "default",
    "config": {
      "buildOption": {
        "arkOptions": {
          "buildProfileFields": {
            "targetName": "default"
          }
        }
      }
    }
  },
  {
    "name": "default1",
    "config": {
      "buildOption": {
        "arkOptions": {
          "buildProfileFields": {
            "targetName1": "default1"
          }
        }
      }
    }
  }
]
```

将targets内所有buildProfileFields的key值修改为一致，例如都修改为targetName。

**问题现象2**

使用了自定义参数BuildProfile并且编译器标红且构建失败，提示“Property xxx does not exist on type 'typeof BuildProfile'.”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/4ia2tvOkR9mESoGuFjUpJg/zh-cn_image_0000002654837791.png)

**解决措施**

检查当前模块下的 build-profile.json5文件，确保buildProfileFields中已添加所使用的自定义参数。
