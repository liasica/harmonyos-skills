---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-project-management-31
title: 构建多个不同的APP产物-icon和名称为何没有区别
breadcrumb: FAQ > DevEco Studio > 工程管理 > 构建多个不同的APP产物-icon和名称为何没有区别
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:ffea4560521702603213e3ee79914b54bced6d5020bbb00c49e991389e823c17
---

## 问题现象

需要在一个工程项目中，构建多个不同的APP，不同product拥有不同的bundleName、应用名称、应用图标。但是构建完后，并不能根据当前的product配置的信息替换AppScope文件下的app.json5里面的默认内容。

## 背景知识

app.json5中的icon和label改变的是设置中显示的图标和名称。例如：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/gAOo_avISAONBxi6pQc5iw/zh-cn_image_0000002658807325.png "点击放大")

正常使用DevEco Studio推送安装到手机的是HAP包，而HAP包里的icon和label是由module.json5文件决定的。例如：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/RzSwgEkSRuiwx4DCfJyryA/zh-cn_image_0000002628408064.png "点击放大")

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/7Uzub7JtQRu7uF72nYfanw/zh-cn_image_0000002628567960.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/wAf_cV1ySEGcbrviipokCw/zh-cn_image_0000002658927283.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/K_Kbh2KNRM6_l49yBvkzdA/zh-cn_image_0000002658807327.png "点击放大")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/AQF5q4xQRsmAO2jctZjuJg/zh-cn_image_0000002628408066.png "点击放大")

附：配置多目标产物-[定义产物的icon、label、launchType](../harmonyos-guides/ide-customized-multi-targets-and-products-guides.md#section82111917125413)。
