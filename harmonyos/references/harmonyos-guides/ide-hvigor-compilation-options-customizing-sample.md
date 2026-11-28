---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-compilation-options-customizing-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 定制构建 > 灵活定制编译选项 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:42+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:20bc89f2a67ff67e07904b2774bf458b430eeae5fb5158f5150f67230bbdab15
---

应用正式对外发布版本前，需要对应用进行代码调试。调试和正式发布版本，两者编译行为可能不同。此时，可以利用buildMode能力，来定制两个版本的编译差异性。

假设其中构建产物均为default，但编译行为不同：release模式下使能混淆，debug模式下使能调试。

示例工程中包含一个模块entry，将entry模块交付到构建产物default中，模块定制两种不同的编译模式debug、release，将两种构建模式均绑定到构建产物default中。工程示例图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/9HYYT9CSRaGuZPLkcTCU1g/zh-cn_image_0000002779566440.png?HW-CC-KV=V1&HW-CC-Date=20261128T023442Z&HW-CC-Expire=31536000000&HW-CC-Sign=2DCD8561E868E48B5A04397BAF253D98A2FC7DEE3B16DAC215E1F61A73C1B0AE)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/ZLjlj3AXR-ajDRWq0kCOFg/zh-cn_image_0000002810973119.png?HW-CC-KV=V1&HW-CC-Date=20261128T023442Z&HW-CC-Expire=31536000000&HW-CC-Sign=CEFEDDB9C6FAD3AAEFA8394D2416528F132B9ACA18C50B17F9D90F23811BEC22)

示例2：构建APP时，构建产物为default，指定构建模式为release，可执行如下命令：

```bash
hvigorw --mode project -p product=default -p buildMode=release assembleApp
```

编译产物示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/XsAa9QU-RWSEe22U3C2ylQ/zh-cn_image_0000002810973251.png?HW-CC-KV=V1&HW-CC-Date=20261128T023442Z&HW-CC-Expire=31536000000&HW-CC-Sign=8830EE8A686B5891A5960F2973DB1E7D0925F7AB5D8578DE0D1E7E12074501CD)

### DevEco Studio界面

在DevEco Studio界面进行可视化配置，Product选择default，Build Mode选择debug后，点击Build -> Build Hap(s)/APP(s) -> Build APP(s) ，打包出产物为default、构建模式为debug的APP包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/hVa3obygQV2Oi0YxzVuAQQ/zh-cn_image_0000002811091183.png?HW-CC-KV=V1&HW-CC-Date=20261128T023442Z&HW-CC-Expire=31536000000&HW-CC-Sign=4741B494B5B97F92FA9138FA575DDE71439B35C369EFDEF25AA1A076DA0D98E9)
