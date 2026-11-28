---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-compilation-options-customizing-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 定制构建 > 灵活定制编译选项 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:56+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:b9dace2a72e333cfe8fbcfa793285a0e81c772e4108f672809bac6cde40c25a8
---

应用正式对外发布版本前，需要对应用进行代码调试。调试和正式发布版本，两者编译行为可能不同。此时，可以利用buildMode能力，来定制两个版本的编译差异性。

假设其中构建产物均为default，但编译行为不同：release模式下使能混淆，debug模式下使能调试。

示例工程中包含一个模块entry，将entry模块交付到构建产物default中，模块定制两种不同的编译模式debug、release，将两种构建模式均绑定到构建产物default中。工程示例图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/9gonYKY6RIWUP-tayTmCdA/zh-cn_image_0000002792001186.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=ED77A5068719ED8131A3DBF85957FC40E45AA3EFC0C21865B0A4A386B54A0866)

## 工程级build-profile.json5示例

```json5
{
  "app": {
    "signingConfigs": [],
    "products": [
      {
        "name": "default",
        "signingConfig": "default",
        "compatibleSdkVersion": "26.0.0",
        "runtimeOS": "HarmonyOS",
        "buildOption": {
          "strictMode": {
            "caseSensitiveCheck": true,
            "useNormalizedOHMUrl": true
          }
        }
      }
    ],
    "buildModeSet": [
      {
        "name": "debug"
      },
      {
        "name": "release"
      }
    ]
  },
  "modules": [
    {
      "name": "entry",
      "srcPath": "./entry",
      "targets": [
        {
          "name": "default",
          "applyToProducts": [
            "default"
          ]
        }
      ]
    }
  ]
}
```

## 模块级build-profile.json5示例

### entry模块

```json5
{
  "apiType": "stageMode",
  "buildOption": {
  },
  "buildOptionSet": [
    {
      "name": "release",
      "arkOptions": {
        "obfuscation": {
          "ruleOptions": {
            "enable": true,
            "files": [
              "./obfuscation-rules.txt"
            ]
          }
        }
      }
    },
    {
      "name": "debug",
      "debuggable": true,
      "arkOptions": {
        "obfuscation": {
          "ruleOptions": {
            "enable": false
          }
        }
      }
    }
  ],
  "buildModeBinder": [
    {
      "buildModeName": "release",
      "mappings": [
        {
          "buildOptionName": "release",
          "targetName": "default"
        }
      ]
    },
    {
      "buildModeName": "debug",
      "mappings": [
        {
          "buildOptionName": "debug",
          "targetName": "default"
        }
      ]
    }
  ],
  "targets": [
    {
      "name": "default",
    },
    {
      "name": "ohosTest",
    }
  ]
}
```

## 指定构建模式

### 命令行

示例1：构建APP时，构建产物为default，指定构建模式为debug，可执行如下命令：

```bash
hvigorw --mode project -p product=default -p buildMode=debug assembleApp
```

编译产物示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/Vz05nlRpQWmwijD7M_CjdA/zh-cn_image_0000002792001188.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F260803425AD1543B4A0F9DCB998692924C55DB49EF6843F4BF914E7B9E9150)

示例2：构建APP时，构建产物为default，指定构建模式为release，可执行如下命令：

```bash
hvigorw --mode project -p product=default -p buildMode=release assembleApp
```

编译产物示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/vNwBhN-PRH6xmR73WLj_vg/zh-cn_image_0000002820721151.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=B86ED7B84E6BB5F0478295DE9DC7721F0B0EC3FC2035AFE9195AD86DFDD1F429)

### DevEco Studio界面

在鸿蒙电脑DevEco Studio界面进行可视化配置，Product选择default，构建模式选择debug后，点击**构建** **>** **编译App(s)** ，打包出产物为default、构建模式为debug的APP包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/kqy375iATqSPOb6mhULvcw/zh-cn_image_0000002820721153.png?HW-CC-KV=V1&HW-CC-Date=20261128T023456Z&HW-CC-Expire=31536000000&HW-CC-Sign=841A9859A6BEBB6F54D981E3495185C48C1FD5915A47165AC331DE425CCE2C46)
