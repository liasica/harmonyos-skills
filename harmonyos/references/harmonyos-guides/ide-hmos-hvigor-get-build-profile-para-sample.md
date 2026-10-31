---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-get-build-profile-para-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 定制构建 > 获取自定义编译参数 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-01T07:13:11+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:5ad237a66b5d22d17187646cdc3e73473aaa2d7bb03ba7e8b2c94c6324fd1ae0
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/-eMYRhiOR2KFLb3tPnt9IQ/zh-cn_image_0000002750169524.png)

default模式下初始化的message为defaultMessage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/f7aoP_meQdi6x5jCw-Y4qQ/zh-cn_image_0000002750009640.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/WsQH3JmMSU-bDDUfbZdswA/zh-cn_image_0000002750009642.png)

通过切换不同的product，可以使用不同的自定义参数来初始化message。

切换product为mirror，可以观察到初始化参数为mirrorMessage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/CqO7p5DRTTGgS8rDkn0HSw/zh-cn_image_0000002779608553.png)

点击不同的Button，message会变为对应的自定义参数：

**图1** 点击Button1  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/w4zPlfr7SdaNyrh2WLovcQ/zh-cn_image_0000002779728701.png)

**图2** 点击Button2  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/CQbCBAIgSNyaVGlaQpEHWA/zh-cn_image_0000002779608551.png)
