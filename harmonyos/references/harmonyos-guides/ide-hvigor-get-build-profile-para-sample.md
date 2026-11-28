---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-get-build-profile-para-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 定制构建 > 获取自定义编译参数 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-28T10:34:42+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:721d5d87715d9d144d09e143c6a522f8e66d5c950adf197ec519f4ad1546235d
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
        "compatibleSdkVersion": "26.0.1",
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
        "compatibleSdkVersion": "26.0.1",
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
        "compatibleSdkVersion": "26.0.1",
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

@Preview
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

选中har模块后点击以下按钮。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/RtwNIeD6R_S4C5uY7hK9qg/zh-cn_image_0000002779567306.png?HW-CC-KV=V1&HW-CC-Date=20261128T023442Z&HW-CC-Expire=31536000000&HW-CC-Sign=5333C0D1BEBF405D7C450F8E8CDA0C266BF22A9FA5015015E26B4FA74EB582FC)

default模式下初始化的message为defaultMessage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/6wTe4QtwSW68NbXCsHZ5wg/zh-cn_image_0000002779407330.png?HW-CC-KV=V1&HW-CC-Date=20261128T023442Z&HW-CC-Expire=31536000000&HW-CC-Sign=1B2CD253262DA64E834E7A91CF9693C90C57F37F50498FFBE3EAF2D3A791D1BC)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/johZ6UddTWelZAOzxBRjyw/zh-cn_image_0000002808886973.png?HW-CC-KV=V1&HW-CC-Date=20261128T023442Z&HW-CC-Expire=31536000000&HW-CC-Sign=CAAD1D6723C16D2123CBD7E2F325B7E31A494F1F43E8825BD6D7391CBF9CD58D)

通过切换不同的product，可以使用不同的自定义参数来初始化message。

切换product为mirror。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/vH3uWZBoQL2AawJro4uAwA/zh-cn_image_0000002808766887.png?HW-CC-KV=V1&HW-CC-Date=20261128T023442Z&HW-CC-Expire=31536000000&HW-CC-Sign=C04A46C6578504847DC8824B141E8765A6595DAEC6254212D8158E4A0B9F1A6B)

可以观察到初始化参数为mirrorMessage：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Rs3M418gRpCQ7Jg6FL6NFA/zh-cn_image_0000002808766891.png?HW-CC-KV=V1&HW-CC-Date=20261128T023442Z&HW-CC-Expire=31536000000&HW-CC-Sign=4B546B3905F1C1C7E2645608A061E7495BAB52399C15E2CE37146CC5DE41D226)

点击不同的Button，message会变为对应的自定义参数：

**图1** 点击Button1  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/5x4kIk8FQg6xEvud_XN1hA/zh-cn_image_0000002808886969.png?HW-CC-KV=V1&HW-CC-Date=20261128T023442Z&HW-CC-Expire=31536000000&HW-CC-Sign=5EEBF3E6AE2303B0AFFFB7492138F0D420966B6BCB5C6D90F8D2E113FC9EF160)

**图2** 点击Button2  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/6CS9aDXlTLmvjoNiCpHZCQ/zh-cn_image_0000002808766893.png?HW-CC-KV=V1&HW-CC-Date=20261128T023442Z&HW-CC-Expire=31536000000&HW-CC-Sign=D75EDAB8EB8E643AB102558EB8C91B5A8C9748F79813DCB9F41CBBACD6150341)
