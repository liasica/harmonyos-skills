---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-compilation-options-customizing-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 定制构建 > 灵活定制编译选项 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:33+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:a55bdece2f62b0079b620cc52b478f8ef22eb2b28f16bc18713f6d2344e93c8c
---

应用正式对外发布版本前，需要对应用进行代码调试。调试和正式发布版本，两者编译行为可能不同。此时，可以利用buildMode能力，来定制两个版本的编译差异性。

假设其中构建产物均为default，但编译行为不同：release模式下使能混淆，debug模式下使能调试。

示例工程中包含一个模块entry，将entry模块交付到构建产物default中，模块定制两种不同的编译模式debug、release，将两种构建模式均绑定到构建产物default中。工程示例图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/MMnbygXmQxCbFdze15VaNA/zh-cn_image_0000002779566440.png?HW-CC-KV=V1&HW-CC-Date=20261124T044233Z&HW-CC-Expire=31536000000&HW-CC-Sign=527D95E07F3061DBF00A24F1640F3D74AC377C42B0F620D53FD40ADE40E23388)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/oYapm9nDTBGBkM0GYenwZA/zh-cn_image_0000002810973119.png?HW-CC-KV=V1&HW-CC-Date=20261124T044233Z&HW-CC-Expire=31536000000&HW-CC-Sign=E6D75705D201ABAEB1468FC44FE5CEA233BF0AE7553DE746DDB3233E2AFEEC88)

示例2：构建APP时，构建产物为default，指定构建模式为release，可执行如下命令：

```bash
hvigorw --mode project -p product=default -p buildMode=release assembleApp
```

编译产物示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/NX9cU2p7Q7O9koFMiUqO9g/zh-cn_image_0000002810973251.png?HW-CC-KV=V1&HW-CC-Date=20261124T044233Z&HW-CC-Expire=31536000000&HW-CC-Sign=7DAD491FAEAF14E0C9B0DEB0E0D4A1060E2F578285BEDAFBF96AA11956916733)

### DevEco Studio界面

在DevEco Studio界面进行可视化配置，Product选择default，Build Mode选择debug后，点击Build -> Build Hap(s)/APP(s) -> Build APP(s) ，打包出产物为default、构建模式为debug的APP包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/_40BLm5xTxaHRkoY1yv2nw/zh-cn_image_0000002811091183.png?HW-CC-KV=V1&HW-CC-Date=20261124T044233Z&HW-CC-Expire=31536000000&HW-CC-Sign=1A64B453C7699D50BBDF2FBAAF981ACBF4BB5C3063CCCF5802C5799FD8B45242)
