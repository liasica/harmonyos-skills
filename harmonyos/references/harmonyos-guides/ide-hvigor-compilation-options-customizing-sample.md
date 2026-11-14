---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-compilation-options-customizing-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 定制构建 > 灵活定制编译选项 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:03+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:b58a16e1d2e1bbe482a5e740fedf2e5b1a06e5e60cf813c4ac61c3f6f3ae1932
---

应用正式对外发布版本前，需要对应用进行代码调试。调试和正式发布版本，两者编译行为可能不同。此时，可以利用buildMode能力，来定制两个版本的编译差异性。

假设其中构建产物均为default，但编译行为不同：release模式下使能混淆，debug模式下使能调试。

示例工程中包含一个模块entry，将entry模块交付到构建产物default中，模块定制两种不同的编译模式debug、release，将两种构建模式均绑定到构建产物default中。工程示例图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/7gJRoJdiT2ChXAvEKTf3jw/zh-cn_image_0000002779566440.png?HW-CC-KV=V1&HW-CC-Date=20261114T004715Z&HW-CC-Expire=31536000000&HW-CC-Sign=511A7A20C1E10EF46312E7D24EACBE36E038E8467C3901A45AE623605C44D9BA)

## 工程级build-profile.json5示例

```json5
{
  "app": {
    "signingConfigs": [],
    "products": [
      {
        "name": "default",
        "signingConfig": "default",
        "compatibleSdkVersion": "26.0.1",
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/MoWYT-MmSv2OwmyCSkVFFw/zh-cn_image_0000002810973119.png?HW-CC-KV=V1&HW-CC-Date=20261114T004715Z&HW-CC-Expire=31536000000&HW-CC-Sign=2CA90B33279EA4FC8187C2D3DF021E9E45C4F0E8B1E949DC0C0DD1106D481434)

示例2：构建APP时，构建产物为default，指定构建模式为release，可执行如下命令：

```bash
hvigorw --mode project -p product=default -p buildMode=release assembleApp
```

编译产物示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/4aC0_KEjTtWN9EZ6Fa-4Pg/zh-cn_image_0000002810973251.png?HW-CC-KV=V1&HW-CC-Date=20261114T004715Z&HW-CC-Expire=31536000000&HW-CC-Sign=CCDF7B69B9405443A16CD3BB05CB38A288D8E52E51023B0BE72C8A19C37C740C)

### DevEco Studio界面

在DevEco Studio界面进行可视化配置，Product选择default，Build Mode选择debug后，点击Build -> Build Hap(s)/APP(s) -> Build APP(s) ，打包出产物为default、构建模式为debug的APP包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/ZglPa9T_QQqy4hANfMJjGw/zh-cn_image_0000002811091183.png?HW-CC-KV=V1&HW-CC-Date=20261114T004715Z&HW-CC-Expire=31536000000&HW-CC-Sign=F3E878E98C2C828F775BC1BB6B8C179C27967BB1F2E98C0F7D7DA77C0449B119)
