---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-container-hyperlink
title: Hyperlink
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 文本与输入 > Hyperlink
category: harmonyos-references
scraped_at: 2026-09-05T06:17:15+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:2e1016a16ada640ccfd3c1f1f786ae8c4efaf09005d563213ff33cf99234030d
---

超链接组件，支持文本和图片两种展示形式，在组件宽高范围内点击可实现跳转到指定网页。适用于应用内打开外部网页链接的场景，该组件仅支持与系统浏览器配合使用。

**说明** 

* 该组件从API version 7开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 该组件仅支持与系统浏览器配合使用。

## 需要权限

跳转到目标网页需要使用网络时，需要申请权限ohos.permission.INTERNET。具体申请方式请参考[声明权限](../harmonyos-guides/declare-permissions.md)。

## 子组件

可以包含[Image](ts-basic-components-image.md)子组件。

## 接口

Hyperlink(address: string | Resource, content?: string | Resource)

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| address | string | [Resource](ts-types.md#resource) | 是 | Hyperlink组件跳转的网页地址。 |
| content | string | [Resource](ts-types.md#resource) | 否 | Hyperlink组件显示的文本。  默认值：''。若不传该参数且组件内无子组件时，默认显示address参数值。  **说明：**  组件内有子组件时，不显示超链接文本。 |

## 属性

除支持[通用属性](ts-component-general-attributes.md)外，还支持以下属性：

### color

color(value: Color | number | string | Resource)

设置超链接文本的颜色。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | [Color](ts-appendix-enums.md#color) | number | string | [Resource](ts-types.md#resource) | 是 | 超链接文本的颜色。  phone默认值为'#ff007dff'，wearable设备默认值'#1F71FF'，tv设备默认值为'#266EFB'，均显示为蓝色。 |

## 示例

该示例展示了超链接图片和文本跳转的效果。

```ts
@Entry
@Component
struct HyperlinkExample {
  build() {
    Column() {
      Column() {
        Hyperlink('https://example.com/') {
          // $r('app.media.bg')需要替换为开发者所需的图像资源文件。
          Image($r('app.media.bg'))
            .width(200)
            .height(100)
        }
      }

      Column() {
        Hyperlink('https://example.com/', 'Go to the developer website')
        .color(Color.Blue)
      }
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/6j58ofnXTIWFnBdozpWX7A/zh-cn_image_0000002742125151.png)
