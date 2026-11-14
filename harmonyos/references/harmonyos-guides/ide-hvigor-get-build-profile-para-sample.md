---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-get-build-profile-para-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 定制构建 > 获取自定义编译参数 > 实践说明
category: harmonyos-guides
scraped_at: 2026-11-14T08:49:03+08:00
doc_updated_at: 2026-11-11
content_hash: sha256:8d9425f6c6123e3f7a9b22feb84107f85d4f605db8ff4928cc76b5c7f2c6a567
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/XjlUUuRMTkS_CYu5q2mRdg/zh-cn_image_0000002779567306.png?HW-CC-KV=V1&HW-CC-Date=20261114T004903Z&HW-CC-Expire=31536000000&HW-CC-Sign=B47AD166C252EE5098B9048417F9F1D51BEB51B81CD327E362CD73B7BA1EF079)

default模式下初始化的message为defaultMessage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/yVGxhYoATRmnanc0pCj05g/zh-cn_image_0000002779407330.png?HW-CC-KV=V1&HW-CC-Date=20261114T004903Z&HW-CC-Expire=31536000000&HW-CC-Sign=A4A9F0143CBAC8422FC31D6320953445840DA8E72EC5C8E4ED624E0A0398C7F3)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/lZybycC7RfuLB_xeOlZV_A/zh-cn_image_0000002808886973.png?HW-CC-KV=V1&HW-CC-Date=20261114T004903Z&HW-CC-Expire=31536000000&HW-CC-Sign=FC89C9B7BCC36E0E3A6B5EA17FC2C427008774359D88653006EB3CDC809745AB)

通过切换不同的product，可以使用不同的自定义参数来初始化message。

切换product为mirror。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/rgphW0-3S3izZ4AkANKzlA/zh-cn_image_0000002808766887.png?HW-CC-KV=V1&HW-CC-Date=20261114T004903Z&HW-CC-Expire=31536000000&HW-CC-Sign=45059DCCBFB53A6CBF3212B2DAE2BFA350E3D64C10C205D0D1A5B793AAE1BEE3)

可以观察到初始化参数为mirrorMessage：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/PVga-mWhTSGssUfUfDKJxw/zh-cn_image_0000002808766891.png?HW-CC-KV=V1&HW-CC-Date=20261114T004903Z&HW-CC-Expire=31536000000&HW-CC-Sign=CDD91F0016361164C0EA648A48FB638A5F3131E2F1DD928DF6E589058C4704CC)

点击不同的Button，message会变为对应的自定义参数：

**图1** 点击Button1  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/btYVgcMVSl2otbL5niJVqg/zh-cn_image_0000002808886969.png?HW-CC-KV=V1&HW-CC-Date=20261114T004903Z&HW-CC-Expire=31536000000&HW-CC-Sign=5AE00CDCC3CE052E0D7F8DA69CA1155A4032DD4E8391B285E152D485488B1CDC)

**图2** 点击Button2  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/EqraKsF8QSCqPghmnSOEkA/zh-cn_image_0000002808766893.png?HW-CC-KV=V1&HW-CC-Date=20261114T004903Z&HW-CC-Expire=31536000000&HW-CC-Sign=4F476C90016541C838F188461EB679CF6D6B47CFAF43EE21C96481D015F38B10)
