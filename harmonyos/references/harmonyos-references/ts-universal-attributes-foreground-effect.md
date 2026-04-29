---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-foreground-effect
title: 前景属性设置
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用属性 > 视效与模糊 > 前景属性设置
category: harmonyos-references
scraped_at: 2026-04-29T13:51:20+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:5ee6ea047340cb806a120fea6586f1705fe4743a87059ccc04eafaef406fafb5
---

设置组件的前景属性。

说明

从API version 12开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## foregroundEffect

PhonePC/2in1TabletTVWearable

foregroundEffect(options: ForegroundEffectOptions): T

设置组件的前景属性。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [ForegroundEffectOptions](ts-universal-attributes-foreground-effect.md#foregroundeffectoptions12) | 是 | 设置组件前景属性包括：模糊半径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## ForegroundEffectOptions12+

PhonePC/2in1TabletTVWearable

前景效果参数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| radius | number | 否 | 否 | 模糊半径，取值范围：[0, +∞)。  仅在组件范围内生效，与其他接口连用时超出组件范围的效果无法生效。 |

## 示例

PhonePC/2in1TabletTVWearable

该示例主要演示通过foregroundEffect接口设置前景属性。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct Index {
5. build() {
6. Row() {
7. // $r("app.media.icon")需要替换为开发者所需的图像资源文件。
8. Image($r('app.media.icon'))
9. .width(100)
10. .height(100)
11. .foregroundEffect({ radius: 20 })
12. }
13. .width('100%')
14. .height('100%')
15. .justifyContent(FlexAlign.Center)
16. }
17. }
```

效果图如下：

radius表示模糊半径，数值越大，效果越模糊。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/CNTfN37rSZGwggphEgf9UA/zh-cn_image_0000002558606384.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T055118Z&HW-CC-Expire=86400&HW-CC-Sign=83870400D1B5B40722C133DAAE333E5BB76312DE1B75331266C1CE51ACCA30EF)
