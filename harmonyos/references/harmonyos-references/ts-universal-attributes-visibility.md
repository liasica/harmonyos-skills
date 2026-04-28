---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-visibility
title: 显隐控制
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 基础属性 > 显隐控制
category: harmonyos-references
scraped_at: 2026-04-28T08:01:00+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:937fbbb4016a2bc84fceed4045487d5c361b6713f970d06a06037316b2f198ac
---

控制组件是否可见。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## visibility

PhonePC/2in1TabletTVWearable

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
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例通过配置visibility的不同值，实现不同的显隐控制效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct VisibilityExample {
5. build() {
6. Column() {
7. Column() {
8. // 隐藏不参与占位
9. Text('None').fontSize(9).width('90%').fontColor(0xCCCCCC)
10. Row().visibility(Visibility.None).width('90%').height(80).backgroundColor(0xAFEEEE)

12. // 隐藏参与占位
13. Text('Hidden').fontSize(9).width('90%').fontColor(0xCCCCCC)
14. Row().visibility(Visibility.Hidden).width('90%').height(80).backgroundColor(0xAFEEEE)

16. // 正常显示，组件默认的显示模式
17. Text('Visible').fontSize(9).width('90%').fontColor(0xCCCCCC)
18. Row().visibility(Visibility.Visible).width('90%').height(80).backgroundColor(0xAFEEEE)
19. }.width('90%').border({ width: 1 })
20. }.width('100%').margin({ top: 5 })
21. }
22. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/ySn4IrvZSeuQz4tsIDjf5w/zh-cn_image_0000002552959476.png?HW-CC-KV=V1&HW-CC-Date=20260428T000059Z&HW-CC-Expire=86400&HW-CC-Sign=1EC7D2B35CFD6F416A6FB7CD4586FA92C0025165ED7BA41ACA04A427EE967059)
