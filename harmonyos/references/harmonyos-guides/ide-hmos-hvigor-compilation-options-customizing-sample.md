---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-compilation-options-customizing-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 定制构建 > 灵活定制编译选项 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-01T07:13:11+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:cea5d9c0a3fcc44097c4bde0cb3d76793a69c2110fff483d49f024dc8271d714
---

应用正式对外发布版本前，需要对应用进行代码调试。调试和正式发布版本，两者编译行为可能不同。此时，可以利用buildMode能力，来定制两个版本的编译差异性。

假设其中构建产物均为default，但编译行为不同：release模式下使能混淆，debug模式下使能调试。

示例工程中包含一个模块entry，将entry模块交付到构建产物default中，模块定制两种不同的编译模式debug、release，将两种构建模式均绑定到构建产物default中。工程示例图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/T68FvCphRNmB5yEDD4M1oQ/zh-cn_image_0000002750169776.png)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/brmiYvEDQCSgNeCr6vFY6g/zh-cn_image_0000002779608801.png)

示例2：构建APP时，构建产物为default，指定构建模式为release，可执行如下命令：

```bash
hvigorw --mode project -p product=default -p buildMode=release assembleApp
```

编译产物示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/VLdXSOpLSTa8Fx-TM7wcjw/zh-cn_image_0000002779728945.png)

### DevEco Studio界面

在鸿蒙电脑DevEco Studio界面进行可视化配置，Product选择default，构建模式选择debug后，点击**构建** **>** **编译App(s)** ，打包出产物为default、构建模式为debug的APP包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/PLPLgMTDSe2W5oZuhaWXaQ/zh-cn_image_0000002750009884.png)
