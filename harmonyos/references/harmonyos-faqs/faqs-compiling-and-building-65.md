---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-65
title: 如何定制构建多目标产物
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何定制构建多目标产物
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:833bb20183918c9d7c064727254f3007c59a46237ace219352f1612d2972030c
---

**问题场景：**

根据不同的部署环境、目标人群和运行环境，定制构建多目标产物，将同一应用定制为不同版本。

**参考代码：**

1、项目build-profile.json5配置示例如下：

```screen
{
  "app": {
    "products": [
      {
        "name": "default",
        "signingConfig": "default",
        "compileSdkVersion": "4.1.0(11)",
        "compatibleSdkVersion": "4.1.0(11)",
        "runtimeOS": "HarmonyOS",
      },
      {
        "name": "release",
        "signingConfig": "release",
        "compileSdkVersion": "4.1.0(11)",
        "compatibleSdkVersion": "4.1.0(11)",
        "runtimeOS": "HarmonyOS",
      },
      {
        "name": "beta1",
        "compileSdkVersion": "4.1.0(11)",
        "compatibleSdkVersion": "4.1.0(11)",
        "runtimeOS": "HarmonyOS",
      },
      {
        "name": "zhaohangzhuanyong",
        "compileSdkVersion": "4.1.0(11)",
        "compatibleSdkVersion": "4.1.0(11)",
        "runtimeOS": "HarmonyOS",
      }
    ],
    "buildModeSet": [
      {
        "name": "debug",
      },
      {
        "name": "beta1"
      }
    ],
    "signingConfigs": [
      {
        "name": "release",
        "material": {
          "storePassword": "",
          "certpath": "",
          "keyAlias": "",
          "keyPassword": "",
          "profile": "",
          "signAlg": "SHA256withECDSA",
          "storeFile": ""
        },
        "type": "HarmonyOS"
      },
      {
        "name": "default",
        "material": {
          "storePassword": "",
          "certpath": "",
          "keyAlias": "",
          "keyPassword": "",
          "profile": "",
          "signAlg": "SHA256withECDSA",
          "storeFile": ""
        },
        "type": "HarmonyOS"
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
            "release"
          ]
        }
      ]
    },
    {
      "name": "library1",
      "srcPath": "./library1"
    },
    {
      "name": "library2",
      "srcPath": "./library2"
    },
    {
      "name": "library",
      "srcPath": "./library",
      "targets": [
        {
          "name": "default",
          "applyToProducts": [
            "release"
          ]
        }
      ]
    },
  ]
}
```

2、target的配置在modules下的build-profile.json5中，配置示例如下：

```json
{
  "apiType": "stageMode",
  "buildOption": {
    "arkOptions": {
      // "apPath": "./modules.ap" /* Profile used for profile-guided optimization (PGO), a compiler optimization technique to improve app runtime performance. */
    }
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
  ],
  "targets": [
    {
      "name": "default",
      "runtimeOS": "HarmonyOS"
    },
    {
      "name": "ohosTest",
    }
  ]
}
```
