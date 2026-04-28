---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-graphics-drawing-typefacearguments
title: Class (TypefaceArguments)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.drawing (绘制模块) > Class (TypefaceArguments)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:548a4a97d6bfd6d7895dd83d41b112560c4ccccb4ea79cc554d22e97acafd185
---

提供字体属性配置的结构体。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 20开始支持。
* 本模块使用屏幕物理像素单位px。
* 本模块为单线程模型策略，需要调用方自行管理线程安全和上下文状态的切换。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { drawing } from '@kit.ArkGraphics2D';
```

## constructor20+

PhonePC/2in1TabletTVWearable

constructor()

字体属性的构造函数。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';
2. let typeFaceArgument = new drawing.TypefaceArguments();
```

## addVariation20+

PhonePC/2in1TabletTVWearable

addVariation(axis: string, value: number)

给字体属性设置字重值。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Graphics.Drawing

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| axis | string | 是 | 字体属性对象可变维度字重的标签'wght'。具体是否支持的该标签取决于加载的字体文件。请打开对应的字体文件具体查看支持的属性。 |
| value | number | 是 | 字体属性对象可变维度字重的标签'wght'对应的属性值，需要在字体文件支持的范围内，否则不会生效。如果属性值小于支持的最小值，则默认和最小值一致。如果属性值大于支持的最大值，则默认和最大值效果一致。请打开对应的字体文件具体查看支持的属性值。 |

**错误码：**

以下错误码的详细介绍请参见[图形绘制与显示错误码](errorcode-drawing.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 25900001 | Parameter error.Possible causes: Incorrect parameter range. |

**示例：**

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. let typeFaceArgument = new drawing.TypefaceArguments();
4. typeFaceArgument.addVariation('wght', 10);
```
