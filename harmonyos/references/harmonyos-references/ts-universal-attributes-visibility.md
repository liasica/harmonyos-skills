---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-visibility
title: 显隐控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 基础属性 > 显隐控制
category: harmonyos-references
scraped_at: 2026-09-05T06:17:03+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:ca5db0b1d7d7e03a827d7945167afd34b44773d05a89a584f08f8d7657f1b1d6
---

控制组件是否可见，适用于根据业务状态动态调整组件显示效果和页面布局的场景。

**说明** 

从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## visibility

visibility(value: Visibility): T

控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Visibility](ts-appendix-enums.md#visibility) | 是 | 控制当前组件显示或隐藏。根据具体场景需要可使用[条件渲染](../harmonyos-guides/arkts-rendering-control-ifelse.md)代替。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件，用于支持属性链式调用。 |

## 示例

该示例通过配置visibility的不同值，实现不同的显隐控制效果。

```ts
// xxx.ets
@Entry
@Component
struct VisibilityExample {
  build() {
    Column() {
      Column() {
        // 隐藏不参与占位
        Text('None').fontSize(9).width('90%').fontColor(0xCCCCCC);
        Row().visibility(Visibility.None).width('90%').height(80).backgroundColor(0xAFEEEE);

        // 隐藏参与占位
        Text('Hidden').fontSize(9).width('90%').fontColor(0xCCCCCC);
        Row().visibility(Visibility.Hidden).width('90%').height(80).backgroundColor(0xAFEEEE);

        // 正常显示，组件默认的显示模式
        Text('Visible').fontSize(9).width('90%').fontColor(0xCCCCCC);
        Row().visibility(Visibility.Visible).width('90%').height(80).backgroundColor(0xAFEEEE);
      }.width('90%').border({ width: 1 });
    }.width('100%').margin({ top: 5 });
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/6xFyuxUtRTiaSin8rF0zHw/zh-cn_image_0000002712405816.png)
