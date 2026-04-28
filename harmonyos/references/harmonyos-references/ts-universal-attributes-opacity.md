---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-opacity
title: 透明度设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 透明度设置
category: harmonyos-references
scraped_at: 2026-04-28T08:01:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:ad33847432b315a742c32563ff19a55438324218b17eacf0174a5c78825e651c
---

设置组件的透明度。

说明

从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## opacity

PhonePC/2in1TabletTVWearable

opacity(value: number | Resource): T

设置组件的不透明度。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | [Resource](ts-types.md#resource) | 是 | 元素的不透明度，取值范围为0到1，若设置的值小于0时，则取值为0，若设置的值大于1时，则取值为1，1表示不透明，0表示完全透明，达到隐藏组件效果，但是在布局中占位。  默认值：1  **说明：**  子组件会继承父组件的透明度，并与自身的透明度属性叠加。如：父组件透明度为0.1，子组件设置透明度为0.8，则子组件实际透明度为0.1\*0.8=0.08。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## opacity18+

PhonePC/2in1TabletTVWearable

opacity(opacity: Optional<number | Resource>): T

设置组件的不透明度。与[opacity](ts-universal-attributes-opacity.md#opacity)相比，opacity参数新增了对undefined类型的支持。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| opacity | [Optional](ts-universal-attributes-custom-property.md#optionalt)<number | [Resource](ts-types.md#resource)> | 是 | 元素的不透明度，取值范围为0到1，若设置的值小于0时，则取值为0，若设置的值大于1时，则取值为1，1表示不透明，0表示完全透明，达到隐藏组件效果，但是在布局中占位。  默认值：1  **说明：**  子组件会继承父组件的透明度，并与自身的透明度属性叠加。如：父组件透明度为0.1，子组件设置透明度为0.8，则子组件实际透明度为0.1\*0.8=0.08。  当opacity的值为undefined时，恢复为默认不透明度为1的状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例主要显示通过[opacity](ts-universal-attributes-opacity.md#opacity)设置组件的不透明度。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct OpacityExample {
5. build() {
6. Column({ space: 5 }) {
7. Text('opacity(1)').fontSize(9).width('90%').fontColor(0xCCCCCC)
8. Text().width('90%').height(50).opacity(1).backgroundColor(0xAFEEEE)
9. Text('opacity(0.7)').fontSize(9).width('90%').fontColor(0xCCCCCC)
10. Text().width('90%').height(50).opacity(0.7).backgroundColor(0xAFEEEE)
11. Text('opacity(0.4)').fontSize(9).width('90%').fontColor(0xCCCCCC)
12. Text().width('90%').height(50).opacity(0.4).backgroundColor(0xAFEEEE)
13. Text('opacity(0.1)').fontSize(9).width('90%').fontColor(0xCCCCCC)
14. Text().width('90%').height(50).opacity(0.1).backgroundColor(0xAFEEEE)
15. Text('opacity(0)').fontSize(9).width('90%').fontColor(0xCCCCCC)
16. Text().width('90%').height(50).opacity(0).backgroundColor(0xAFEEEE)
17. }
18. .width('100%')
19. .padding({ top: 5 })
20. }
21. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/HpBnuAq-SfS872hfobXXCg/zh-cn_image_0000002552959506.png?HW-CC-KV=V1&HW-CC-Date=20260428T000105Z&HW-CC-Expire=86400&HW-CC-Sign=862EC70F8D0AC148BDDE7861B356BD42E5CC09152CE61474D677EE5208191F10)
