---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-compilation-options-customizing-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 定制构建 > 灵活定制编译选项 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:76b6512c6bd837ffb8fe9c34565b94912332a2d00ea09f00790c7abd3e9cc04e
---

应用正式对外发布版本前，需要对应用进行代码调试。调试和正式发布版本，两者编译行为可能不同。此时，可以利用buildMode能力，来定制两个版本的编译差异性。

假设其中构建产物均为default，但编译行为不同：release模式下使能混淆，debug模式下使能调试。

示例工程中包含一个模块entry，将entry模块交付到构建产物default中，模块定制两种不同的编译模式debug、release，将两种构建模式均绑定到构建产物default中。工程示例图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/1GRNhY2qQaqS9D780-5k4g/zh-cn_image_0000002779566440.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A6CCE74E45C72B598EBA4BC93473385A9F6DDE05E1D3F87A9AB8F276E23D4670)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/98ilP3eGRnmIeF8CFucKEA/zh-cn_image_0000002810973119.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=A49738F9D45071F6D9FB3E35B4BE5FD60DCC47E9D5BCC161243ABC8CCC945BAE)

示例2：构建APP时，构建产物为default，指定构建模式为release，可执行如下命令：

```bash
hvigorw --mode project -p product=default -p buildMode=release assembleApp
```

编译产物示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/HV0DF3oBTzGIJ_4eAWMNQA/zh-cn_image_0000002810973251.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=763A543360602BF6E492CEAAD9B02ED6AE15C7E58D45500E121B0F09692F7564)

### DevEco Studio界面

在DevEco Studio界面进行可视化配置，Product选择default，Build Mode选择debug后，点击Build -> Build Hap(s)/APP(s) -> Build APP(s) ，打包出产物为default、构建模式为debug的APP包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/U13SJqZUTtixJs694NxW8Q/zh-cn_image_0000002811091183.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=9A0DF7594C4E7EA6D23109BA77AD719EBA0F9FE5C5EF128E05B4CCB8C2D137D7)
