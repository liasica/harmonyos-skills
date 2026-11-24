---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-compilation-options-customizing-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 定制构建 > 灵活定制编译选项 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:47+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:bb7425f1a8bed0139426f847c16e8f8d2fdd13eb93e872945361453800b890e0
---

应用正式对外发布版本前，需要对应用进行代码调试。调试和正式发布版本，两者编译行为可能不同。此时，可以利用buildMode能力，来定制两个版本的编译差异性。

假设其中构建产物均为default，但编译行为不同：release模式下使能混淆，debug模式下使能调试。

示例工程中包含一个模块entry，将entry模块交付到构建产物default中，模块定制两种不同的编译模式debug、release，将两种构建模式均绑定到构建产物default中。工程示例图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/UWp7BT6tTmCvtAuT5Z_wZw/zh-cn_image_0000002792001186.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=24F7FA14FE23D9C85C90C06623E7D8B5F7DB0F7E5CEA457F2FDF893FC7DA44CC)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/Bmf_zbJeQIKKyhPQXkrwMg/zh-cn_image_0000002792001188.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=63C21F29339FD791FC91D2BA3732252CCC968332AAA103AB5C388050206EDEEB)

示例2：构建APP时，构建产物为default，指定构建模式为release，可执行如下命令：

```bash
hvigorw --mode project -p product=default -p buildMode=release assembleApp
```

编译产物示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/NyGtv5ILR3eitX6gGBVnVg/zh-cn_image_0000002820721151.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=8F59200054398D9EC7049C1B9E1718DF1AFD71939FC9808988582F0869B04135)

### DevEco Studio界面

在鸿蒙电脑DevEco Studio界面进行可视化配置，Product选择default，构建模式选择debug后，点击**构建** **>** **编译App(s)** ，打包出产物为default、构建模式为debug的APP包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/kHOy7MXZRQyrDPSQj4o-Pg/zh-cn_image_0000002820721153.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=BBE986FE625A6383B5260450276F85A4DE5D59812B99BF8F54684B3A20C487B3)
