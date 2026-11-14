---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-get-build-profile-para-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 定制构建 > 获取自定义编译参数 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:18+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:2435685b50ba8b9e129713633a7fd6b8fc402619b7713f7a1fdad5d2c0e086e6
---

示例：配置工程级和模块级的自定义参数并通过切换product来展示不同的message。

## 新建工程并创建一个har模块

在工程级build-profile.json5使用以下配置，是为了实现在所有模块中都可以使用到productMessage自定义参数。

通过切换不同的product从而使用到对应的productMessage值。

```json5
{
  "app": {
    "products": [
      {
        "name": "default",
        "signingConfig": "default",
        "compatibleSdkVersion": "26.0.0",
        "runtimeOS": "HarmonyOS",
        "buildOption": {
          "arkOptions": {
            // 工程级自定义参数
            "buildProfileFields": {
              "productMessage": 'defaultMessage'
            }
          }
        }
      },
      {
        "name": "mirror",
        "signingConfig": "default",
        "compatibleSdkVersion": "26.0.0",
        "runtimeOS": "HarmonyOS",
        "buildOption": {
          "arkOptions": {
            // 工程级自定义参数
            "buildProfileFields": {
              "productMessage": 'mirrorMessage'
            }
          }
        }
      },
      {
        "name": "product",
        "signingConfig": "default",
        "compatibleSdkVersion": "26.0.0",
        "runtimeOS": "HarmonyOS",
        "buildOption": {
          "arkOptions": {
            // 工程级自定义参数
            "buildProfileFields": {
              "productMessage": 'productMessage'
            }
          }
        }
      }
    ],
    "buildModeSet": [
      {
        "name": "debug",
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
            // 关联到多个product
            "default",
            "product",
            "mirror"
          ]
        }
      ]
    },
    {
      "name": "har",
      "srcPath": "./har"
    }
  ]
}
```

在har模块的build-profile.json5使用以下配置。

```json5
{
  "apiType": "stageMode",
  "buildOption": {
    "arkOptions": {
      // har模块的自定义参数
      "buildProfileFields": {
        "targetMessage1": 'this is target buildProfileValue1',
        "targetMessage2": 'this is target buildProfileValue2'
      }
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
          },
          "consumerFiles": [
            "./consumer-rules.txt"
          ]
        }
      },
    },
  ],
  "targets": [
    {
      "name": "default"
    }
  ]
}
```

在har模块的MainPage.ets中添加以下代码。

```ts
import BuildProfile from "../../../../BuildProfile"

@Component
export struct MainPage {
  // 默认赋值为工程级别BuildProfile自定义参数配置的productMessage
  @State message: string = BuildProfile.productMessage
  build() {
    Row() {
      Column() {
        Flex({ direction: FlexDirection.Row, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceAround }) {
          Button("Button 1").width("40%")
            .onClick(() => {
              // 点击展示自定义字段targetMessage1
              this.message = BuildProfile.targetMessage1;
            })
          Button("Button 2").width("40%")
            .onClick(() => {
              // 点击展示自定义字段targetMessage2
              this.message = BuildProfile.targetMessage2;
            })
        }.margin(20)
        .width(315)
        Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start, justifyContent: FlexAlign.SpaceBetween }) {
          Text(this.message)
            .textAlign(TextAlign.Start)
            .fontSize(12)
            .border({ width: 1 })
            .padding(10)
            .width('100%')
        }.height(600).width(350).padding({ left: 35, right: 35})
      }
    }
  }
}
```

在hap的oh-package.json5中引用本地的har模块。

```json5
{
  "name": "entry",
  "version": "1.0.0",
  "description": "Please describe the basic information.",
  "main": "",
  "author": "",
  "license": "",
  "dependencies": {
    "har": "file:../har"
  }
}
```

在hap的Index.ets文件中引用该har包并且使用MainPage方法。

```ts
import { MainPage } from "har"

@Entry
@Component
struct Index {
  build() {
    Row() {
      MainPage()
    }
  }
}
```

## 执行预览或签名后推包到设备调试

右键点击har模块，在菜单中点击**生成BuildProfile文件**。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/xeqOcTpDTo64yg1RG7ahJA/zh-cn_image_0000002810750633.png?HW-CC-KV=V1&HW-CC-Date=20261114T004918Z&HW-CC-Expire=31536000000&HW-CC-Sign=3936DE36E0C57DBA55F5278E01D098BC45DFBA83FFD7EF5449B0248163DF2806)

default模式下初始化的message为defaultMessage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/6L2LqSFqR-iLddBZoc9nJQ/zh-cn_image_0000002810630525.png?HW-CC-KV=V1&HW-CC-Date=20261114T004918Z&HW-CC-Expire=31536000000&HW-CC-Sign=A093D909F945FD1B1F256C5DE6CF9CDF587DAA44833BDE62E79086548F630BCA)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/aobBBxKSSE2725o98vGd2A/zh-cn_image_0000002810750635.png?HW-CC-KV=V1&HW-CC-Date=20261114T004918Z&HW-CC-Expire=31536000000&HW-CC-Sign=521B12BF8B6C15E13D7598538C9423EAF079AC1C215FC459BEF472029D3E3346)

通过切换不同的product，可以使用不同的自定义参数来初始化message。

切换product为mirror，可以观察到初始化参数为mirrorMessage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/jCddgOy1TaCJEIPm2jpy-A/zh-cn_image_0000002781470972.png?HW-CC-KV=V1&HW-CC-Date=20261114T004918Z&HW-CC-Expire=31536000000&HW-CC-Sign=5668D12ADE17709BFAC4ADDDB922D3BE8F2BC51B708B3061F91E859628419F8B)

点击不同的Button，message会变为对应的自定义参数：

**图1** 点击Button1  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/Hu6RBfc8SR-6BiQiC2QEFw/zh-cn_image_0000002781470970.png?HW-CC-KV=V1&HW-CC-Date=20261114T004918Z&HW-CC-Expire=31536000000&HW-CC-Sign=9814F4C61654506B3548C2C7A98C034D4196B2C5042EB494FBB306F01B9B4927)

**图2** 点击Button2  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/p4tPRhexQSSaVEDbBATNRg/zh-cn_image_0000002781311036.png?HW-CC-KV=V1&HW-CC-Date=20261114T004918Z&HW-CC-Expire=31536000000&HW-CC-Sign=F20DA393FFE07BCC0549ABF4F393468B15FC284C7C3E113E46834AF3D828549F)
