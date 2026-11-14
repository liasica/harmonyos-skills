---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-compilation-options-customizing-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 定制构建 > 灵活定制编译选项 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:18+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:da445a1b3aaec64fd5c9277878bcb78a98595544668b1240f96d11a05f57aa8d
---

应用正式对外发布版本前，需要对应用进行代码调试。调试和正式发布版本，两者编译行为可能不同。此时，可以利用buildMode能力，来定制两个版本的编译差异性。

假设其中构建产物均为default，但编译行为不同：release模式下使能混淆，debug模式下使能调试。

示例工程中包含一个模块entry，将entry模块交付到构建产物default中，模块定制两种不同的编译模式debug、release，将两种构建模式均绑定到构建产物default中。工程示例图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/drf5DDV5RHqtQ0VVO5B6Hw/zh-cn_image_0000002810750913.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=96EB90123AEEB4F38C62CBFE7D6552CAC7517764AE2AC435CC11314755610C6E)

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/2LWN4B1gTBK-enq0Y2SFvQ/zh-cn_image_0000002781311320.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=F644AE1BCA714ABDFB061E4B5BD7F17457246EB4EEC692D913C154373D8AB7B7)

示例2：构建APP时，构建产物为default，指定构建模式为release，可执行如下命令：

```bash
hvigorw --mode project -p product=default -p buildMode=release assembleApp
```

编译产物示例如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/zPJAfcKkQb6jnoniRpnfEg/zh-cn_image_0000002781471254.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=B3EF5B9273FBCACBE4DC56BE1AA30C3798259B27A01FF7797423A303ED4B56D2)

### DevEco Studio界面

在鸿蒙电脑DevEco Studio界面进行可视化配置，Product选择default，构建模式选择debug后，点击**构建** **>** **编译App(s)** ，打包出产物为default、构建模式为debug的APP包。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/bmSoBZojT8KGv0h8K4t93g/zh-cn_image_0000002810630805.png?HW-CC-KV=V1&HW-CC-Date=20261114T004729Z&HW-CC-Expire=31536000000&HW-CC-Sign=98484D2D184A20FB376F030F8157FD12BED84E1E3DFDF7B588052FBA67703241)
