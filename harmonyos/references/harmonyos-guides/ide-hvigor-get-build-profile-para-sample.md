---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-get-build-profile-para-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 定制构建 > 获取自定义编译参数 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:10656b3ea75d9a55fa646be6cade62ff981428f5f3d50ee47bc81949b09b18f5
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/_2M-x6VvTEKnNnzmsL7RcA/zh-cn_image_0000002779567306.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FAB853B2DD4497FEF1DBA82C1E8071583601FE7B43AF8E9113C78287F5A8EB19)

default模式下初始化的message为defaultMessage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/ptoXsuaDQEOthN-ARIoNxw/zh-cn_image_0000002779407330.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=FF5C6E4CE1404C39B8499E398F58AB3E52A664F3C970F322CA7A69CCB2B47781)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/rLG6W0U6R0Ka2Cp5G8tfxA/zh-cn_image_0000002808886973.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=BA8B46D670D3E4C077BAA6EAE1AF0900B65A6A0B078CFD2878C2221FB016C4BA)

通过切换不同的product，可以使用不同的自定义参数来初始化message。

切换product为mirror。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/oeO_qtQTQvax5QANWPzqgw/zh-cn_image_0000002808766887.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=CBA77B0E00F75EC46E866BBD2DE072DC27AC49804AA67980B8E5EF0DD674DDB1)

可以观察到初始化参数为mirrorMessage：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/hLIc8jtxRZOOVQ3tVkzP8g/zh-cn_image_0000002808766891.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=03E6DBC9C9C9EE806CCD9AC0FFA0B2597DE7614148A81AEE535F1C28C51A00DC)

点击不同的Button，message会变为对应的自定义参数：

**图1** 点击Button1  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/UAvbMIuOQxiKWJNsMaH2eQ/zh-cn_image_0000002808886969.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=42527E4AC57629413D9B38710340234804B5BC2993BEBD054BB5D2C183E59EC9)

**图2** 点击Button2  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/hOmN-Eo3TrGpd5GEc8t5pg/zh-cn_image_0000002808766893.png?HW-CC-KV=V1&HW-CC-Date=20261112T233232Z&HW-CC-Expire=31536000000&HW-CC-Sign=61B1157D76B84ED4EA239B5DD12D7D0F334B92EE56D8EE8BCB285E8F4420CBF2)
