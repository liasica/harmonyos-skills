---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-31
title: 构建多个不同的APP产物-icon和名称为何没有区别
breadcrumb: FAQ > DevEco Studio > 工程管理 > 构建多个不同的APP产物-icon和名称为何没有区别
category: harmonyos-faqs
scraped_at: 2026-11-13T07:34:14+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:02eade53e95f519912fa3dd5eea71bc582e6f0ac6deb0b1e8d95ece95538af98
---

## 问题现象

需要在一个工程项目中，构建多个不同的APP，不同product拥有不同的bundleName、应用名称、应用图标。但是构建完后，并不能根据当前的product配置的信息替换AppScope文件下的app.json5里面的默认内容。

## 背景知识

app.json5中的icon和label改变的是设置中显示的图标和名称。例如：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/2AXp4QN_RdGo19Wi8LBPZg/zh-cn_image_0000002658807325.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=80D77A5ACFC56B23733870584A734D3B6B61DE29EFB130580BE653EF1D8BFE07 "点击放大")

正常使用DevEco Studio推送安装到手机的是HAP包，而HAP包里的icon和label是由module.json5文件决定的。例如：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/Je2hgAnIRhC8hUWu43h7Gw/zh-cn_image_0000002628408064.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=FD4B1301A924252C16AC0BD2D6D3EFB04AF5AAD132389C3089AF772C9F325EF7 "点击放大")

要在工程级build-profile.json5文件products中配置不同的APP产物，并配置对应icon和label来覆盖app.json5里面的默认内容：

```json
{
  "app": {
    "signingConfigs": [],
    "products": [
      {
        "name": "default",
        "signingConfig": "default",
        "compatibleSdkVersion": "5.0.0(12)",
        "runtimeOS": "HarmonyOS",
        "icon":"$media:default_icon", // 定义default的icon
        "label":"$string:default_name", // 定义default的label
      },
      {
        "name": "productA",
        "signingConfig": "default",
        "compatibleSdkVersion": "5.0.0(12)",
        "runtimeOS": "HarmonyOS",
        "icon":"$media:productA_icon", // 定义productA的icon
        "label":"$string:productA_name", // 定义productA的label
      },
    ],
    "buildModeSet": [
      {
        "name": "debug",
      },
      {
        "name": "release"
      }
    ],
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
          },
          {
            "name": "productA",
            "applyToProducts": [
              "productA"
            ]
          }
        ]
      }
    ]
  }
}
```

HAP包中模块级的build-profile.json5定制对应的target产物，来覆盖module.json5中的配置：

```ts
{
  "apiType": 'stageMode',
  "buildOption": {
  },
  "targets": [
    {
      "name": "default",
      "source": {
        "abilities": [
          {
            "name": "EntryAbility",
            "icon":"$media:default_icon",
            "label":"$string:default_name"
          }
        ]
      }
    },
    {
      "name": "productA",
      "source": {
        "abilities": [
          {
            "name": "EntryAbility",
            "icon":"$media:productA_icon",
            "label":"$string:productA_name"
          }
        ]
      }
    }
  ]
}
```

## 问题定位

HAP包中build-profile.json5是否定制对应的target产物，来覆盖module.json5中的配置。

## 修改建议

针对HAP包也定制对应的target产物，并定制不同的icon、label。

## 分析结论

product中的icon和label改变设置中显示的图标和名称，应用桌面的图标和名称是由HAP包的icon和label决定的。

可通过打包后的产物来检查是否配置正确：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/fPP--174RiOqmbE15fezkw/zh-cn_image_0000002628567960.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=755E253BE26CFB881F2A447F88681805016BDB133A528942E7ADB820C83506B0 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/L3YdXJ-BRjGlaccI49h0UA/zh-cn_image_0000002658927283.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=01B54A5931380AAEA310B0625CC51191F35B5E9BE2D8C58F6C5C926A9CC60648 "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/03/v3/zGaK0HmDRYKyGJsW-ktoOw/zh-cn_image_0000002658807327.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=0A263CFBE324FBAA09FDDAF7BE43B2C5E7734BABE6B5A5DE6BBD81B114983D0D "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/MNHD09XQTRG9H_6PZGpeTA/zh-cn_image_0000002628408066.png?HW-CC-KV=V1&HW-CC-Date=20261112T233217Z&HW-CC-Expire=31536000000&HW-CC-Sign=DF8300EF29335110FC75A378DAC81E8325CA2723A7D6A2FD999731D3921F3496 "点击放大")

附：配置多目标产物-[定义产物的icon、label、launchType](../harmonyos-guides/ide-customized-multi-targets-and-products-guides.md#section82111917125413)。
