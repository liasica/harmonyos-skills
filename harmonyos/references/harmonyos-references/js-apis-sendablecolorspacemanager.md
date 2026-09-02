---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-sendablecolorspacemanager
title: "@ohos.graphics.sendableColorSpaceManager (可共享的色彩管理)"
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.sendableColorSpaceManager (可共享的色彩管理)
category: harmonyos-references
scraped_at: 2026-09-02T15:02:40+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:70441e6561b4cc5143b4b84a8f736c8185ac75f5457afe42594e9cc801330c35
---

本模块提供管理抽象化色域对象的基础能力，包括可共享的色彩管理的创建与可共享的色域基础属性的获取等。适用于需要在多线程间传递色域信息的场景，能够解决跨线程色彩管理对象无法共享的问题，提高色彩处理的效率和一致性。

**说明** 

本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

```ts
import { sendableColorSpaceManager } from '@kit.ArkGraphics2D';
```

## ISendable

type ISendable = lang.ISendable

为与当前模块的接口规范保持一致，定义了ISendable类型别名。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

| 类型 | 说明 |
| --- | --- |
| [lang.ISendable](js-apis-arkts-lang.md#langisendable) | 所有Sendable类型的父类型。 |

## sendableColorSpaceManager.create

create(colorSpaceName: colorSpaceManager.ColorSpace): ColorSpaceManager

创建标准可共享的色彩管理实例。

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
| 401 | Parameter error. Possible cause: 1. Incorrect parameter type. 2. Parameter verification failed. |
| 18600001 | The parameter value is abnormal. |

**示例：**

```ts
import { colorSpaceManager, sendableColorSpaceManager } from '@kit.ArkGraphics2D';
let colorSpace: sendableColorSpaceManager.ColorSpaceManager;
// 创建标准SRGB色域的色彩管理实例
colorSpace = sendableColorSpaceManager.create(colorSpaceManager.ColorSpace.SRGB);
```

## sendableColorSpaceManager.create

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
| 401 | Parameter error. Possible cause: 1. Incorrect parameter type. 2. Parameter verification failed. |
| 18600001 | The parameter value is abnormal. |

**示例：**

```ts
import { colorSpaceManager, sendableColorSpaceManager } from '@kit.ArkGraphics2D';
let colorSpace: sendableColorSpaceManager.ColorSpaceManager;
// 定义色域标准三原色参数
let primaries: colorSpaceManager.ColorSpacePrimaries = {
  redX: 0.1,
  redY: 0.1,
  greenX: 0.2,
  greenY: 0.2,
  blueX: 0.3,
  blueY: 0.3,
  whitePointX: 0.4,
  whitePointY: 0.4
};
// 定义色域gamma值
let gamma: number = 2.2;
// 创建自定义可共享的色彩管理实例
colorSpace = sendableColorSpaceManager.create(primaries, gamma);
```

## ColorSpaceManager

当前可共享的色彩管理实例。ColorSpaceManager是用于管理和操作色域对象的核心类，提供了获取色域类型、白点值、gamma值等功能，并支持在ArkTS并发实例间传递。

下列API示例中都需先使用[create()](js-apis-sendablecolorspacemanager.md#sendablecolorspacemanagercreate)获取到ColorSpaceManager实例，再通过此实例调用对应方法。

### getColorSpaceName

getColorSpaceName(): colorSpaceManager.ColorSpace

获取色域类型。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [colorSpaceManager.ColorSpace](js-apis-colorspacemanager.md#colorspace) | 返回色域类型枚举值。 |

**错误码：**

以下错误码的详细介绍请参见[色彩管理错误码](errorcode-colorspace-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 18600001 | The parameter value is abnormal.  适用版本：12-22 |

**示例：**

```ts
// 获取色域类型
let spaceName: colorSpaceManager.ColorSpace = colorSpace.getColorSpaceName();
```

### getWhitePoint

getWhitePoint(): collections.Array<number>

获取色域白点值，返回色度坐标[x, y]，表示色彩空间中白色点的坐标位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [collections.Array](arkts-apis-arkts-collections-array.md)<number> | 返回色域白点值[x, y]。 |

**错误码：**

以下错误码的详细介绍请参见[色彩管理错误码](errorcode-colorspace-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 18600001 | The parameter value is abnormal.  适用版本：12-22 |

**示例：**

```ts
import { collections } from '@kit.ArkTS';
// 获取色域白点值[x, y]
let point: collections.Array<number> = colorSpace.getWhitePoint();
```

### getGamma

getGamma(): number

获取色域gamma值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回色域gamma值。 |

**错误码：**

以下错误码的详细介绍请参见[色彩管理错误码](errorcode-colorspace-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 18600001 | The parameter value is abnormal.  适用版本：12-22 |

**示例：**

```ts
// 获取色域gamma值
let gamma: number = colorSpace.getGamma();
```
