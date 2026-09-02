---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-8
title: 卡片数据同步异常
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 卡片数据同步异常
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:47cc3c8991d55de1fa80e364583b5ef54502f422d041593d4dbdc618f590b092
---

## 问题现象

服务卡片不会自动刷新或者加载失败。

## 背景知识

[卡片数据的交互](../harmonyos-guides/arkts-ui-widget-interaction-overview.md)分为定时刷新、定点刷新、下一次刷新、代理刷新四种：

* 定时刷新：表示在一定时间间隔内调用[onUpdateForm](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonupdateform)的生命周期回调函数自动刷新卡片内容。可以在form\_config.json配置文件的[updateDuration](../harmonyos-guides/arkts-ui-widget-configuration.md)字段中进行设置。例如，可以将刷新时间设置为每小时一次。

  ```json
  {
    "forms": [
      {
        "name": "widget",
        "description": "This is a service widget.",
        "src": "./ets/widget/pages/WidgetCard.ets",
        "uiSyntax": "arkts",
        "window": {
          "designWidth": 720,
          "autoDesignWidth": true
        },
        "colorMode": "auto",
        "isDefault": true,
        "updateEnabled": true,

        "scheduledUpdateTime": "10:30",
        "updateDuration": 2, // 设置卡片定时刷新的更新周期（单位为30分钟，取值为自然数）
        "defaultDimension": "2*2",
        "supportDimensions": ["2*2"]
      }
    ]
  }
  ```
* 定点刷新：表示在每天的某个特定时间点自动刷新卡片内容。可以在form\_config.json配置文件中的[scheduledUpdateTime](../harmonyos-guides/arkts-ui-widget-configuration.md)字段中进行设置。例如，可以将刷新时间设置为每天的上午10点30分。

  ```json
  {
    "forms": [
      {
        "name": "widget",
        "description": "This is a service widget.",
        "src": "./ets/widget/pages/WidgetCard.ets",
        "uiSyntax": "arkts",
        "window": {
          "designWidth": 720,
          "autoDesignWidth": true
        },
        "colorMode": "auto",
        "isDefault": true,
        "updateEnabled": true, // 使能刷新功能
        "scheduledUpdateTime": "10:30", // 设置卡片的定点刷新的时刻
        "updateDuration": 0,
        "defaultDimension": "2*2",
        "supportDimensions": ["2*2"]
      }
    ]
  }
  ```
* 下次刷新：表示指定卡片的下一次刷新时间。可以通过调用[setFormNextRefreshTime()](../harmonyos-references/js-apis-app-form-formprovider.md#formprovidersetformnextrefreshtime)接口来实现。最短刷新时间为5分钟。例如，可以在接口调用后的5分钟内刷新卡片内容。
* 代理刷新：通过[推送卡片刷新消息](../harmonyos-guides/push-form-update.md)实现作为代理模式刷新服务卡片内容。

## 问题定位

1. 查看form\_config.json配置文件上采用的是哪种刷新模式。
2. 根据日志查看报错信息，具体请看场景分析。

## 分析结论

* **场景一**：

  应用使用了错误的刷新模式，或者未开启卡片数据刷新功能，比如日期类应用应在每天24:00时刷新数据。
* **场景二**：

  卡片框架在重启时是使用onAddForm()回调方法的返回值，若应用重启前调用updateForm()更新的数据和onAddForm()方法返回的数据不一致，会导致设备重启前后卡片数据不一致的现象。
* **场景三**：

  日志中出现关键字：“Cannot get SourceMap info, dump raw stack”。此报错一般是开发者的API写法错误，或者引入了不支持卡片的模块，导致了相关模块的报错，从而导致卡片内容加载失败或出现白屏。
* **场景四**：

  当com.ohos.formrenderservice中出现关键日志can't find this page xxx.abc path。

  一般是.abc文件打包时出现了问题，需要应用确认hap包里xxx.abc是否存在，位置是否正确。

## 修改建议

* **场景一**：

  根据业务场景选择合适的刷新模式。
* **场景二**：

  需要对数据做持久化处理。例如使用关系型数据库存储卡片最新数据，在FormExtensionAbility的onAddForm()生命周期回调中，获取数据库中的最新数据后，使用updateForm()方法更新卡片。
* **场景三**：
  + “TypeError：Cannot read property xxx”、“xxx undefined”等的属性是业务自己的变量，业务方自己规避。
  + “TypeError：Cannot read property xxx”、“xxx undefined”等的属性是系统模块，需要明确当前模块是否支持服务卡片。
* **场景四**：

  在该路径下放入正确的abc文件，在DevEco Studio中通过Build->Clean Project清理后，重新编译运行。
