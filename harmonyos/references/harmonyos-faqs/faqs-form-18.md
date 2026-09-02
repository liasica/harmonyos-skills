---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-form-18
title: 如何实现拖拽卡片调整大小
breadcrumb: FAQ > 应用框架开发 > 程序框架 > 卡片开发（Form） > 如何实现拖拽卡片调整大小
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:56+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a4aa11d9f69b8d6061e99465876d63035124a0451b3e880045e0d8821159a54e
---

## 问题现象

应用内包含不同大小的卡片，卡片之间如何通过拖拽实现大小调整？

## 背景知识

* [Form Kit（卡片开发服务）](../harmonyos-guides/formkit-overview.md)提供了一种在桌面、锁屏等系统应用上嵌入显示应用信息的开发框架和API，可以将应用内用户关注的重要信息或常用操作抽取到服务卡片（简称“卡片”）上，通过将卡片添加到桌面、锁屏等系统应用上，以达到信息展示、服务直达的便捷体验效果。
* 在创建卡片时会自动生成[form\_config.json配置文件](../harmonyos-guides/arkts-ui-widget-configuration.md#配置文件字段说明)。其中，supportDimensions字段表示卡片支持的外观规格；resizable字段表示是否可以拖拽卡片调整大小；groupId字段表示一组卡片的共同id。

## 解决方案

场景一：单张卡片不同外观规格的调整。

1. 创建卡片。
2. 修改src/main/resources/base/profile/form\_config.json配置文件的supportDimensions字段。对于单张卡片的场景，需要声明该卡片支持多种外观规格。例如："supportDimensions": ["2\*4","4\*4"]。
3. 补充src/main/resources/base/profile/form\_config.json配置文件的resizable字段。该字段默认缺省，需配置"resizable": true。

完整配置文件为：

```json
{
  "forms": [
    {
      "name": "widget",
      "displayName": "$string:widget_display_name",
      "description": "$string:widget_desc",
      "src": "./ets/widget/pages/WidgetCard.ets",
      "uiSyntax": "arkts",
      "window": {
        "designWidth": 720,
        "autoDesignWidth": true
      },
      "colorMode": "auto",
      "isDynamic": true,
      "isDefault": true,
      "updateEnabled": false,
      "scheduledUpdateTime": "10:30",
      "updateDuration": 1,
      "defaultDimension": "2*4",
      "resizable": true,
      "supportDimensions": [
        "2*4",
        "4*4"
      ]
    }
  ]
}
```

场景二：多张卡片不同外观规格的调整。

1. 创建多张卡片。
2. 修改src/main/resources/base/profile/form\_config.json配置文件的supportDimensions字段。对于多张卡片的场景，需要分别声明卡片支持外观规格。例如：A卡片中声明"supportDimensions": ["2\*2"]，B卡片中声明"supportDimensions": ["2\*4"]。
3. 补充src/main/resources/base/profile/form\_config.json配置文件的resizable字段。该字段默认缺省，需配置"resizable": true。
4. 补充src/main/resources/base/profile/form\_config.json配置文件的groupId字段。该字段默认缺省，需要分别声明卡片共同id。例如：A卡片中声明"groupId": "0"，B卡片中也需要声明"groupId": "0"。

完整配置文件为：

```json
{
  "forms": [
    {
      "name": "widgetA",
      "displayName": "$string:widgetA_display_name",
      "description": "$string:widgetA_desc",
      "src": "./ets/widgeta/pages/WidgetACard.ets",
      "uiSyntax": "arkts",
      "window": {
        "designWidth": 720,
        "autoDesignWidth": true
      },
      "colorMode": "auto",
      "isDynamic": true,
      "isDefault": true,
      "updateEnabled": false,
      "scheduledUpdateTime": "10:30",
      "updateDuration": 1,
      "defaultDimension": "2*2",
      "resizable": true,
      "groupId": "0",
      "supportDimensions": [
        "2*2"
      ]
    },
    {
      "name": "widgetB",
      "displayName": "$string:widgetB_display_name",
      "description": "$string:widgetB_desc",
      "src": "./ets/widgetb/pages/WidgetBCard.ets",
      "uiSyntax": "arkts",
      "window": {
        "designWidth": 720,
        "autoDesignWidth": true
      },
      "colorMode": "auto",
      "isDynamic": true,
      "isDefault": false,
      "updateEnabled": false,
      "scheduledUpdateTime": "10:30",
      "updateDuration": 1,
      "defaultDimension": "2*4",
      "resizable": true,
      "groupId": "0",
      "supportDimensions": [
        "2*4"
      ]
    }
  ]
}
```

## 常见FAQ

Q：配置了单张卡片不同外观规格，拖拽卡片调整不生效的原因可能是什么？

A：对于需要拖拽调整大小的卡片，拖拽间两种外观规格需要保持连续。比如：2\*4与4\*4卡片之间实现拖拽调整，而2\*2与4\*4卡片之间则不能。

Q：配置多张卡片不同外观规格的调整，拖拽的优先级是什么？

A：

1. 如果当前卡片supportDimensions字段配置了多个规格，则在同一张卡片之间调整大小。卡片A的resizable配置为true，supportDimension为2\*2、2\*4，支持卡片A的两个尺寸之间调整大小。
2. 如果当前卡片supportDimensions字段配置了单个规格，则会将同一个应用中与当前卡片配置相同groupId卡片supportDimensions字段中第一个外观规格纳入到可调整范围中。例如：卡片A的groupId配置为'1'，resizable配置为true，supportDimension为1\*2。卡片B的groupId配置为'1'，resizable配置为true，supportDimension为2\*2、2\*4、4\*4。卡片A可以调整到卡片B的2\*2，卡片B只支持在B卡片支持的三个尺寸之间调整大小，无法调整为卡片A。
