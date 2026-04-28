---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-stepperitem
title: StepperItem
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 已停止维护的组件与接口 > StepperItem
category: harmonyos-references
scraped_at: 2026-04-28T08:02:51+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:4e8753e680aca817867fa73eb6fe6e2c18d3c2d27baeb5dbec549284ddc504ff
---

用作[Stepper](ts-basic-components-stepper.md)组件的页面子组件。

说明

* 从API version 8开始支持，从API version 22开始废弃，建议使用[Swiper](ts-container-swiper.md)替代。
* 该组件从API version 8开始支持。后续版本如有新增内容，则采用上角标单独标记该内容的起始版本。

## 子组件

PhonePC/2in1TabletTVWearable

支持单个子组件。

## 接口

PhonePC/2in1TabletTVWearable

StepperItem()

创建[Stepper](ts-basic-components-stepper.md)组件的页面子组件。

说明

从API version 8开始支持，从API version 22开始废弃，建议使用[Swiper](ts-container-swiper.md#属性)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## 属性

PhonePC/2in1TabletTVWearable

### prevLabel(deprecated)

PhonePC/2in1TabletTVWearable

prevLabel(value: string)

设置左侧文本按钮内容，第一页没有左侧文本按钮，当步骤导航器大于一页时，除第一页外默认值都为“返回”。

说明

从API version 8开始支持，从API version 22开始废弃，建议使用[showPrevious](ts-container-swiper.md#showprevious)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 左侧文本按钮内容。字符串超长时，先缩小再换行（2行）最后截断。 |

### nextLabel(deprecated)

PhonePC/2in1TabletTVWearable

nextLabel(value: string)

设置右侧文本按钮内容，最后一页默认值为“开始”，其余页默认值为“下一步”。

说明

从API version 8开始支持，从API version 22开始废弃，建议使用[showNext](ts-container-swiper.md#shownext)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | string | 是 | 右侧文本按钮内容。字符串超长时，先缩小再换行（2行）最后截断。 |

### status(deprecated)

PhonePC/2in1TabletTVWearable

status(value?: ItemState)

设置步骤导航器nextLabel的显示状态。

说明

从API version 8开始支持，从API version 22开始废弃，建议使用[indicatorInteractive](ts-container-swiper.md#indicatorinteractive12)替代。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [ItemState](ts-basic-components-stepperitem.md#itemstate枚举说明) | 否 | 步骤导航器nextLabel的显示状态。  默认值：ItemState.Normal |

说明

* StepperItem组件不支持设置通用宽度属性，其宽度默认撑满Stepper父组件。
* StepperItem组件不支持设置通用高度属性，其高度由Stepper父组件高度减去label按钮组件高度。
* StepperItem组件不支持设置[aspectRatio](ts-universal-attributes-layout-constraints.md#aspectratio)/[constraintSize](ts-universal-attributes-size.md#constraintsize)影响长宽的属性。

## ItemState枚举说明

PhonePC/2in1TabletTVWearable

步骤导航器nextLabel的显示状态。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| Normal | 0 | 正常状态，右侧文本按钮正常显示，可点击进入下一个StepperItem。  **说明：**  从API version 8开始支持，从API version 22开始废弃，建议使用[index](ts-container-swiper.md#index)替代。 |
| Disabled | 1 | 不可用状态，右侧文本按钮灰度显示，不可点击进入下一个StepperItem。  **说明：**  从API version 8开始支持，从API version 22开始废弃，建议使用[indicatorInteractive](ts-container-swiper.md#indicatorinteractive12)替代。 |
| Waiting | 2 | 等待状态，右侧文本按钮不显示，显示等待进度条，不可点击进入下一个StepperItem。  **说明：**  从API version 8开始支持，从API version 22开始废弃，建议使用[Swiper](ts-container-swiper.md)替代。 |
| Skip | 3 | 跳过状态，右侧文本按钮默认显示“跳过”，此时可在Stepper的onSkip回调中自定义相关逻辑。  **说明：**  从API version 8开始支持，从API version 22开始废弃，建议使用[index](ts-container-swiper.md#index)替代。 |

## 示例

PhonePC/2in1TabletTVWearable

见[Stepper](ts-basic-components-stepper.md)。
