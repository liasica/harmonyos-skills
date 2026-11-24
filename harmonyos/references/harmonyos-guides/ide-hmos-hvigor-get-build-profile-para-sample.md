---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-get-build-profile-para-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 定制构建 > 获取自定义编译参数 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:48+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:306ece75ff95ab7ef5faeb539efe6577720d99d95fd6af241f8520110e8b7ccb
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/QLXonvZVSNSodWfbRT0WgQ/zh-cn_image_0000002820681047.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=44D7286BDC6E8BF4FB1B59C61B4C0B880907401E0FA5BEAEC7CAC184074B5281)

default模式下初始化的message为defaultMessage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/3mR25tq_Sva5iLRyL4BeSg/zh-cn_image_0000002792001092.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=B2B9D000CE19E2E6DC94EB6C4DB726DA683267E0AEE50E5910E473F999CE905A)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/ndQ71FqYS1KHa-7pOFBGNQ/zh-cn_image_0000002791841114.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=9CE517BD32C9389B0530DD9EF200D7B13D26E9547CBD0A13BB72E60FC86A8BC3)

通过切换不同的product，可以使用不同的自定义参数来初始化message。

切换product为mirror，可以观察到初始化参数为mirrorMessage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/-N60RufuQuih6hsOxzkKuQ/zh-cn_image_0000002820721055.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=5F6FE9DFCBDDAB1B141D8DAEB9DE658986E4F51BED0F6271BA74FC6E8E59EB2A)

点击不同的Button，message会变为对应的自定义参数：

**图1** 点击Button1  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/3VlMIUakTPOEEk1pMlBqSQ/zh-cn_image_0000002820681049.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=7EB9DAF9740A8C36CB74603CD511E7A708172CC19ADD114F3EBF286C0CB83674)

**图2** 点击Button2  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/RlQ_a5qySOu1s_IsO_1S0w/zh-cn_image_0000002791841116.png?HW-CC-KV=V1&HW-CC-Date=20261124T044247Z&HW-CC-Expire=31536000000&HW-CC-Sign=593C6156CF414968828828327E4173A599DC3FAF4DED58B1DC308A76E0DA25F9)
