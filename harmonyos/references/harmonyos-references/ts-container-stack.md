---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-stack
title: Stack
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 行列与堆叠 > Stack
category: harmonyos-references
scraped_at: 2026-04-29T13:51:41+08:00
doc_updated_at: 2026-04-28
content_hash: sha256:799df296fa866c390be8eb3fc1def60103d6d7f73cb495e5932be61205364de2
---

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

说明

* 该组件从API version 7开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。
* 通用属性[align](ts-universal-attributes-location.md#align)在该组件上支持镜像能力。

## 子组件

PhonePC/2in1TabletTVWearable

可以包含子组件。

## 接口

PhonePC/2in1TabletTVWearable

Stack(options?: StackOptions)

堆叠容器，子组件按照顺序依次入栈，后一个子组件覆盖前一个子组件。

说明

过多的组件嵌套会导致性能劣化。在部分场景中，直接使用组件属性或借助系统API的能力可以替代层叠容器的效果，减少了嵌套组件数进而优化性能。最佳实践请参考[组件嵌套优化-优先使用组件属性代替嵌套组件](../best-practices/bpta-component-nesting-optimization.md#section78181114123811)。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [StackOptions](ts-container-stack.md#stackoptions18对象说明) | 否 | 设置子组件在容器内的对齐方式。 |

## StackOptions18+对象说明

PhonePC/2in1TabletTVWearable

设置堆叠容器的子组件对齐方式。

说明

为规范匿名对象的定义，API 18版本修改了此处的元素定义。其中，保留了历史匿名对象的起始版本信息，会出现外层元素@since版本号高于内层元素版本号的情况，但这不影响接口的使用。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| alignContent7+ | [Alignment](ts-appendix-enums.md#alignment) | 否 | 是 | 设置子组件在容器内的对齐方式。  默认值：Alignment.Center  非法值：按默认值处理。  **卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |

## 属性

PhonePC/2in1TabletTVWearable

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### alignContent

PhonePC/2in1TabletTVWearable

alignContent(value: Alignment)

设置子组件在容器内的对齐方式。该属性与[align](ts-universal-attributes-location.md#align)同时设置时，后设置的属性生效。该属性与接口的构造入参同时设置时，生效属性上的设置效果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**卡片能力：** 从API version 9开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Alignment](ts-appendix-enums.md#alignment) | 是 | 所有子组件在容器内的对齐方式。  默认值：Alignment.Center  非法值：按默认值处理。 |

## 事件

PhonePC/2in1TabletTVWearable

支持[通用事件](ts-component-general-events.md)。

## 示例

PhonePC/2in1TabletTVWearable

Stack的alignContent设置为Alignment.Bottom条件下子组件显示效果。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct StackExample {
5. build() {
6. Stack({ alignContent: Alignment.Bottom }) {
7. Text('First child, show in bottom').width('90%').height('100%').backgroundColor(0xd2cab3).align(Alignment.Top)
8. Text('Second child, show in top').width('70%').height('60%').backgroundColor(0xc1cbac).align(Alignment.Top)
9. }.width('100%').height(150).margin({ top: 5 })
10. }
11. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/v6kTTo7eR1WFix3LhWohNw/zh-cn_image_0000002589245927.png?HW-CC-KV=V1&HW-CC-Date=20260429T055139Z&HW-CC-Expire=86400&HW-CC-Sign=9A53DD2F7B2AACD3A6EE4CE3C06E4919650A444D5611748C9EBD99E71505A1F1)
