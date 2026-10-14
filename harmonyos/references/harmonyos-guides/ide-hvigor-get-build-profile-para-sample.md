---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-get-build-profile-para-sample
title: 实践说明
breadcrumb: 指南 > DevEco Studio（Windows/macOS版） > 构建应用 > 定制构建 > 获取自定义编译参数 > 实践说明
category: harmonyos-guides
scraped_at: 2026-10-15T07:06:32+08:00
doc_updated_at: 2026-10-10
content_hash: sha256:10d6f462ecdbfa948f76c00ac6e33cde9f2fa602473a7eeff0c390855b4f27b3
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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/O0xhAdPESb6IFByyi5Cm6w/zh-cn_image_0000002731542717.png)

default模式下初始化的message为defaultMessage。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/2COTaBuLSFmzyIDkKoFSxA/zh-cn_image_0000002701823444.png)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/BPWHg42ARoe22xainPtPcg/zh-cn_image_0000002731382749.png)

通过切换不同的product，可以使用不同的自定义参数来初始化message。

切换product为mirror。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/0W4zsIpuSH69dl2E_KVeSA/zh-cn_image_0000002731382745.png)

可以观察到初始化参数为mirrorMessage：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/L1LRL6gPQaizP22kzqNHMQ/zh-cn_image_0000002731382751.png)

点击不同的Button可以改变message为对应的自定义参数：

**图1** 点击Button1  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/J9x1IS23Ss6KUQ0D3L5uBQ/zh-cn_image_0000002731542721.png)

**图2** 点击Button2  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/w2yLN8qiRVG-gLXeKNwwgg/zh-cn_image_0000002731542715.png)
