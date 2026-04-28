---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendablecolorspacemanager
title: @ohos.graphics.sendableColorSpaceManager (可共享的色彩管理)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.sendableColorSpaceManager (可共享的色彩管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:36+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:edcd5960f9dd86ceac1e409c8fb7090e08ced8167e56a3d6bb5c6e5e3b097252
---

本模块提供管理抽象化色域对象的一些基础能力，包括可共享的色彩管理的创建与可共享的色域基础属性的获取等。

说明

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { sendableColorSpaceManager } from '@kit.ArkGraphics2D';
```

## ISendable

PhonePC/2in1TabletTVWearable

type ISendable = lang.ISendable

ISendable是所有Sendable类型（除null和undefined）的父类型。自身没有任何必须的方法和属性。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

| 类型 | 说明 |
| --- | --- |
| [lang.ISendable](js-apis-arkts-lang.md#langisendable) | 所有Sendable类型的父类型。 |

## sendableColorSpaceManager.create

PhonePC/2in1TabletTVWearable

create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager

创建标准可共享的色彩管理。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorSpaceName | [colorSpaceManager.ColorSpace](js-apis-colorspacemanager.md#colorspace) | 是 | 标准色域类型枚举值。  UNKNOWN与CUSTOM不可用于直接创建色域对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorSpaceManager](js-apis-sendablecolorspacemanager.md#colorspacemanager) | 返回当前创建的可共享的色彩管理实例。  该实例继承ISendable，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](../harmonyos-guides/sendable-guide.md)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[色彩管理错误码](errorcode-colorspace-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| 18600001 | The parameter value is abnormal. |

**示例：**

```
1. import { colorSpaceManager, sendableColorSpaceManager } from '@kit.ArkGraphics2D';
2. let colorSpace: sendableColorSpaceManager.ColorSpaceManager;
3. colorSpace = sendableColorSpaceManager.create(colorSpaceManager.ColorSpace.SRGB);
```

## sendableColorSpaceManager.create

PhonePC/2in1TabletTVWearable

create(primaries: colorSpaceManager.ColorSpacePrimaries, gamma: number): ColorSpaceManager

创建用户自定义可共享的色彩管理实例。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| primaries | [colorSpaceManager.ColorSpacePrimaries](js-apis-colorspacemanager.md#colorspaceprimaries) | 是 | 色域标准三原色。 |
| gamma | number | 是 | 色域gamma值，取值为大于0的浮点数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorSpaceManager](js-apis-sendablecolorspacemanager.md#colorspacemanager) | 返回当前创建的可共享的色彩管理实例。  色域类型定义为[colorSpaceManager.ColorSpace](js-apis-colorspacemanager.md#colorspace)枚举值CUSTOM。  该实例继承ISendable，可以在ArkTS并发实例间（包括主线程、TaskPool&Worker工作线程）传递，传递的行为是引用传递，参考[Sendable使用场景](../harmonyos-guides/sendable-guide.md)。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[色彩管理错误码](errorcode-colorspace-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| 18600001 | The parameter value is abnormal. |

**示例：**

```
1. import { colorSpaceManager, sendableColorSpaceManager } from '@kit.ArkGraphics2D';
2. let colorSpace: sendableColorSpaceManager.ColorSpaceManager;
3. let primaries: colorSpaceManager.ColorSpacePrimaries = {
4. redX: 0.1,
5. redY: 0.1,
6. greenX: 0.2,
7. greenY: 0.2,
8. blueX: 0.3,
9. blueY: 0.3,
10. whitePointX: 0.4,
11. whitePointY: 0.4
12. };
13. let gamma: number = 2.2;
14. colorSpace = sendableColorSpaceManager.create(primaries, gamma);
```

## ColorSpaceManager

PhonePC/2in1TabletTVWearable

当前可共享的色彩管理实例。

下列API示例中都需先使用[create()](js-apis-sendablecolorspacemanager.md#sendablecolorspacemanagercreate)获取到ColorSpaceManager实例，再通过此实例调用对应方法。

### getColorSpaceName

PhonePC/2in1TabletTVWearable

getColorSpaceName(): colorSpaceManager.ColorSpace

获取色域类型。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [colorSpaceManager.ColorSpace](js-apis-colorspacemanager.md#colorspace) | 返回色域类型枚举值。 |

**示例：**

```
1. let spaceName: colorSpaceManager.ColorSpace = colorSpace.getColorSpaceName();
```

### getWhitePoint

PhonePC/2in1TabletTVWearable

getWhitePoint(): collections.Array<number>

获取色域白点值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [collections.Array<number>](arkts-apis-arkts-collections-array.md) | 返回色域白点值[x, y]。 |

**示例：**

```
1. import { collections } from '@kit.ArkTS';
2. let point: collections.Array<number> = colorSpace.getWhitePoint();
```

### getGamma

PhonePC/2in1TabletTVWearable

getGamma(): number

获取色域gamma值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回色域gamma值。 |

**示例：**

```
1. let gamma: number = colorSpace.getGamma();
```
