---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1079
title: 禁用分屏功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 窗口管理 > 禁用分屏功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:14+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:3f7a2dd8206f7a7c756d406ee4517584480b40de6e26d7d8900ef84744f5a57c
---

## 问题现象

在手机或PAD非自由多窗模式下，长按窗口底部向上拖动可以设置窗口分屏或悬浮窗展示，在PC上，窗口拖动到屏幕边缘会自动最大化，如何禁用这些功能呢？

## 背景知识

* [module.json5配置文件](../harmonyos-guides/module-configuration-file.md)包含模块的基本配置信息、UIAbility组件和ExtensionAbility组件信息，以及应用运行过程中需要的权限信息，用于向编译工具、操作系统和应用市场提供应用的基本信息。文件所在目录为工程名称/模块名称（例如entry）/src/main/module.json5。
* [abilities标签](../harmonyos-guides/module-configuration-file.md#abilities标签)描述UIAbility组件的配置信息，标签值为数组类型，该标签下的配置只对当前UIAbility生效。
* abilities标签下的supportWindowMode属性标识当前UIAbility组件所支持的窗口模式。支持的取值如下：
  + fullscreen：全屏模式。
  + split：分屏模式。
  + floating：悬浮窗模式。

  在[自由窗口](../harmonyos-guides/window-terminology.md#freeform-window自由窗口)状态下同时配置fullscreen和split时，如果应用的targetAPIVersion小于15，窗口将以悬浮窗模式启动；如果应用的[targetAPIVersion](../harmonyos-guides/app-configuration-file.md#配置文件标签)大于等于15，窗口将以全屏模式启动。此外，还可以通过metadata配置窗口模式，具体的配置规则和优先级请参考[metadata](../harmonyos-guides/module-configuration-file.md#metadata标签)。

## 解决方案

* **禁用分屏模式**：将module.json5配置文件中的abilities标签下的supportWindowMode属性设置为["fullscreen", "floating"]，则只支持全屏及悬浮窗模式，不支持分屏模式。
* **禁用悬浮窗模式**：将module.json5配置文件中的abilities标签下的supportWindowMode属性设置为["fullscreen", "split"]，则只支持全屏及分屏模式，不支持悬浮窗模式。
* **禁用分屏及悬浮窗模式**：将module.json5配置文件中的abilities标签下的supportWindowMode属性设置为["fullscreen"]，则只支持全屏模式，不支持分屏及悬浮窗模式。
* **禁用全屏模式**：将module.json5配置文件中的abilities标签下的supportWindowMode属性设置为["floating","split"]，则只支持小窗（分屏或悬浮窗）模式，不支持全屏模式。

示例代码如下：

```json
"abilities": [
  {
    "name": "EntryAbility",
    "srcEntry": "./ets/entryability/EntryAbility.ets",
    "description": "$string:EntryAbility_desc",
    "icon": "$media:layered_image",
    "label": "$string:EntryAbility_label",
    "startWindowIcon": "$media:startIcon",
    "startWindowBackground": "$color:start_window_background",
    "exported": true,
    // 设置窗口模式:禁用分屏配置["fullscreen","floating"],禁用悬浮窗配置["fullscreen","split"],只全屏配置["fullscreen"]
    // 以下以禁用分屏为例,其他场景按上述配置
    "supportWindowMode": ["fullscreen","floating"],
    "skills": [
      {
        "entities": [
          "entity.system.home"
        ],
        "actions": [
          "ohos.want.action.home"
        ]
      }
    ]
  }
],
```

## 常见FAQ

Q：为何avoidAreaChange监听在悬浮窗时获取到的都是0？

A：需要排查监听避让区的方式是否正确，window.AvoidAreaType.TYPE\_CUTOUT表示挖孔区域，window.AvoidAreaType.TYPE\_SYSTEM表示悬浮窗下的三点控制栏区域，详情参考[AvoidAreaType](../harmonyos-references/arkts-apis-window-e.md#avoidareatype7)。
