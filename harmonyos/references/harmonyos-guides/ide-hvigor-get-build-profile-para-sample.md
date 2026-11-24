---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-get-build-profile-para-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 定制构建 > 获取自定义编译参数 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-24T12:42:34+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:5d4fc2ff243e5964c0f67c11ff0144139c4a31f9f598845f48210e8142d317fb
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/EqssaQhDSKqIummbCBalSQ/zh-cn_image_0000002779567306.png?HW-CC-KV=V1&HW-CC-Date=20261124T044233Z&HW-CC-Expire=31536000000&HW-CC-Sign=56802D687A2C2680AE2926EAA0CE959A712DD2ECF513E38644BD986DC143672E)

default模式下初始化的message为defaultMessage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/CXQtu_aqTfuEs7ZLmTbecw/zh-cn_image_0000002779407330.png?HW-CC-KV=V1&HW-CC-Date=20261124T044233Z&HW-CC-Expire=31536000000&HW-CC-Sign=1C31C427DFD3FDDBFA8F3988E435F2DDD36D1581231FABF6F3809760582CF8D7)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/rCCubkt2RdOHqumP3hsjyQ/zh-cn_image_0000002808886973.png?HW-CC-KV=V1&HW-CC-Date=20261124T044233Z&HW-CC-Expire=31536000000&HW-CC-Sign=86F76544389FDA3E6CF945F64B717D895C2079ADF32920E2DEB7035325E276F5)

通过切换不同的product，可以使用不同的自定义参数来初始化message。

切换product为mirror。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/5yrePwtLRiiUcZReS9I2Kg/zh-cn_image_0000002808766887.png?HW-CC-KV=V1&HW-CC-Date=20261124T044233Z&HW-CC-Expire=31536000000&HW-CC-Sign=C4390541113827D37DD16153E3334A500FB25A11CA7ACF83483A72F172B5A25B)

可以观察到初始化参数为mirrorMessage：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/x5A9WoMASZKmGekaGGsbbA/zh-cn_image_0000002808766891.png?HW-CC-KV=V1&HW-CC-Date=20261124T044233Z&HW-CC-Expire=31536000000&HW-CC-Sign=1FD0132DB8411CF3093D89146403BFBFD859CE082F42CE73C171B02765845A1A)

点击不同的Button，message会变为对应的自定义参数：

**图1** 点击Button1  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/ZAZ3Zf87S2uxBvFT-MVbXw/zh-cn_image_0000002808886969.png?HW-CC-KV=V1&HW-CC-Date=20261124T044233Z&HW-CC-Expire=31536000000&HW-CC-Sign=65F17E5507D9949C57CFAEE01AEDBCB1EF24768E9887B70AB8363930C1C43703)

**图2** 点击Button2  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/oT5xdz9_TPSQ8Bf6kbr8Ew/zh-cn_image_0000002808766893.png?HW-CC-KV=V1&HW-CC-Date=20261124T044233Z&HW-CC-Expire=31536000000&HW-CC-Sign=D0B2A21D6933DCD03FDE36D025BB140EDEF6A1EC4980A45FCD0D7956D5F8BC5A)
