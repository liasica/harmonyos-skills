---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-colorspacemanager
title: @ohos.graphics.colorSpaceManager (色彩管理)
breadcrumb: API参考 > 图形 > ArkGraphics 2D（方舟2D图形服务） > ArkTS API > @ohos.graphics.colorSpaceManager (色彩管理)
category: harmonyos-references
scraped_at: 2026-04-28T08:14:35+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4fccabfcf0acd9832fc21a91cbe801d7d2d8a4aa19bf438ede9e98223670b1c5
---

本模块提供管理抽象化色域对象的一些基础能力，包括色域对象的创建与色域基础属性的获取等。

说明

本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { colorSpaceManager } from '@kit.ArkGraphics2D';
```

## ColorSpace

PhonePC/2in1TabletTVWearable

色域类型枚举。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNKNOWN | 0 | 未知的色域类型。 |
| ADOBE\_RGB\_1998 | 1 | RGB色域为Adobe RGB(1998)类型。  转换函数为Adobe RGB(1998)类型。  编码范围为Full类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DCI\_P3 | 2 | RGB色域为DCI-P3类型。  转换函数为Gamma 2.6类型。  编码范围为Full类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DISPLAY\_P3 | 3 | RGB色域为Display P3类型。  转换函数为SRGB类型。  编码范围为Full类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SRGB | 4 | RGB色域为SRGB类型。  转换函数为SRGB类型。  编码范围为Full类型。  系统默认色域类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| CUSTOM | 5 | 用户自定义色域类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BT70911+ | 6 | RGB色域为BT709类型。  转换函数为BT709类型。  编码范围为Full类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BT601\_EBU11+ | 7 | RGB色域为BT601\_P类型。  转换函数为BT709类型。  编码范围为Full类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BT601\_SMPTE\_C11+ | 8 | RGB色域为BT601\_N类型。  转换函数为BT709类型。  编码范围为Full类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BT2020\_HLG11+ | 9 | RGB色域为BT2020类型。  转换函数为HLG类型。  编码范围为Full类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BT2020\_PQ11+ | 10 | RGB色域为BT2020类型。  转换函数为PQ类型。  编码范围为Full类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| P3\_HLG11+ | 11 | RGB色域为Display P3类型。  转换函数为HLG类型。  编码范围为Full类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| P3\_PQ11+ | 12 | RGB色域为Display P3类型。  转换函数为PQ类型。  编码范围为Full类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ADOBE\_RGB\_1998\_LIMIT11+ | 13 | RGB色域为Adobe RGB(1998)类型。  转换函数为Adobe RGB(1998)类型。  编码范围为Limit类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DISPLAY\_P3\_LIMIT11+ | 14 | RGB色域为Display P3类型。  转换函数为SRGB类型。  编码范围为Limit类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| SRGB\_LIMIT11+ | 15 | RGB色域为SRGB类型。  转换函数为SRGB类型。  编码范围为Limit类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BT709\_LIMIT11+ | 16 | RGB色域为BT709类型。  转换函数为BT709类型。  编码范围为Limit类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BT601\_EBU\_LIMIT11+ | 17 | RGB色域为BT601\_P类型。  转换函数为BT709类型。  编码范围为Limit类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BT601\_SMPTE\_C\_LIMIT11+ | 18 | RGB色域为BT601\_N类型。  转换函数为BT709类型。  编码范围为Limit类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BT2020\_HLG\_LIMIT11+ | 19 | RGB色域为BT2020类型。  转换函数为HLG类型。  编码范围为Limit类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| BT2020\_PQ\_LIMIT11+ | 20 | RGB色域为BT2020类型。  转换函数为PQ类型。  编码范围为Limit类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| P3\_HLG\_LIMIT11+ | 21 | RGB色域为Display P3类型。  转换函数为HLG类型。  编码范围为Limit类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| P3\_PQ\_LIMIT11+ | 22 | RGB色域为Display P3类型。  转换函数为PQ类型。  编码范围为Limit类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| LINEAR\_P311+ | 23 | RGB色域为Display P3类型。  转换函数为Linear类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| LINEAR\_SRGB11+ | 24 | RGB色域为SRGB类型。  转换函数为Linear类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| LINEAR\_BT70911+ | 24 | 与LINEAR\_SRGB相同。  RGB色域为BT709类型。  转换函数为Linear类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| LINEAR\_BT202011+ | 25 | RGB色域为BT2020类型。  转换函数为Linear类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| H\_LOG18+ | 26 | RGB色域为BT2020类型。  转换函数为LOG类型。 |
| DISPLAY\_BT2020\_SRGB20+ | 27 | RGB色域为DISPLAY BT2020类型。  转换函数为SRGB类型。  编码范围为Full类型。 |
| DISPLAY\_SRGB11+ | 4 | 与SRGB相同。  RGB色域为SRGB类型。  转换函数为SRGB类型。  编码范围为Full类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DISPLAY\_P3\_SRGB11+ | 3 | 与DISPLAY\_P3相同。  RGB色域为Display P3类型。  转换函数为SRGB类型。  编码范围为Full类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DISPLAY\_P3\_HLG11+ | 11 | 与P3\_HLG相同。  RGB色域为Display P3类型。  转换函数为HLG类型。  编码范围为Full类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| DISPLAY\_P3\_PQ11+ | 12 | 与P3\_PQ相同。  RGB色域为Display P3类型。  转换函数为PQ类型。  编码范围为Full类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## ColorSpacePrimaries

PhonePC/2in1TabletTVWearable

色域标准三原色（红、绿、蓝）和白色，使用(x, y)表示其在色彩空间中的位置。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| redX | number | 否 | 否 | 标准红色在色彩空间的x坐标值。 |
| redY | number | 否 | 否 | 标准红色在色彩空间的y坐标值。 |
| greenX | number | 否 | 否 | 标准绿色在色彩空间的x坐标值。 |
| greenY | number | 否 | 否 | 标准绿色在色彩空间的y坐标值。 |
| blueX | number | 否 | 否 | 标准蓝色在色彩空间的x坐标值。 |
| blueY | number | 否 | 否 | 标准蓝色在色彩空间的y坐标值。 |
| whitePointX | number | 否 | 否 | 标准白色在色彩空间的x坐标值。 |
| whitePointY | number | 否 | 否 | 标准白色在色彩空间的y坐标值。 |

## colorSpaceManager.create

PhonePC/2in1TabletTVWearable

create(colorSpaceName: ColorSpace): ColorSpaceManager

创建标准色域对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| colorSpaceName | [ColorSpace](js-apis-colorspacemanager.md#colorspace) | 是 | 标准色域类型枚举值。  UNKNOWN与CUSTOM不可用于直接创建色域对象。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorSpaceManager](js-apis-colorspacemanager.md#colorspacemanager) | 返回当前创建的色域对象实例。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[色彩管理错误码](errorcode-colorspace-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| 18600001 | The parameter value is abnormal. |

**示例：**

```
1. let colorSpace: colorSpaceManager.ColorSpaceManager;
2. try {
3. colorSpace = colorSpaceManager.create(colorSpaceManager.ColorSpace.SRGB);
4. } catch (err) {
5. console.error(`Failed to create SRGB colorSpace. Cause: ` + JSON.stringify(err));
6. }
```

## colorSpaceManager.create

PhonePC/2in1TabletTVWearable

create(primaries: ColorSpacePrimaries, gamma: number): ColorSpaceManager

创建用户自定义色域对象。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| primaries | [ColorSpacePrimaries](js-apis-colorspacemanager.md#colorspaceprimaries) | 是 | 色域标准三原色。 |
| gamma | number | 是 | 色域gamma值，取值为大于0的浮点数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorSpaceManager](js-apis-colorspacemanager.md#colorspacemanager) | 返回当前创建的色域对象实例。  色域类型定义为[ColorSpace](js-apis-colorspacemanager.md#colorspace)枚举值CUSTOM。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[色彩管理错误码](errorcode-colorspace-manager.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible cause: 1.Incorrect parameter type. 2.Parameter verification failed. |
| 18600001 | Invalid parameter value. Possible cause: Used UNKNOWN or CUSTOM color space type enum values to directly create a colorSpaceManager object. |

**示例：**

```
1. let colorSpace: colorSpaceManager.ColorSpaceManager;
2. try {
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
13. let gamma = 2.2;
14. colorSpace = colorSpaceManager.create(primaries, gamma);
15. } catch (err) {
16. console.error(`Failed to create colorSpace with customized primaries and gamma. Cause: ` + JSON.stringify(err));
17. }
```

## ColorSpaceManager

PhonePC/2in1TabletTVWearable

当前色域对象实例。

下列API示例中都需先使用[create()](js-apis-colorspacemanager.md#colorspacemanagercreate)获取到ColorSpaceManager实例，再通过此实例调用对应方法。

### getColorSpaceName

PhonePC/2in1TabletTVWearable

getColorSpaceName(): ColorSpace

获取色域类型。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ColorSpace](js-apis-colorspacemanager.md#colorspace) | 返回色域类型枚举值。 |

**示例：**

```
1. try {
2. let spaceName = colorSpace.getColorSpaceName();
3. } catch (err) {
4. console.error(`Fail to get colorSpace's name. Cause: ` + JSON.stringify(err));
5. }
```

### getWhitePoint

PhonePC/2in1TabletTVWearable

getWhitePoint(): Array<number>

获取色域白点值。

**系统能力：** SystemCapability.Graphic.Graphic2D.ColorManager.Core

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Array<number> | 返回色域白点值[x, y]。 |

**示例：**

```
1. try {
2. let point = colorSpace.getWhitePoint();
3. } catch (err) {
4. console.error(`Failed to get white point. Cause: ` + JSON.stringify(err));
5. }
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
1. try {
2. let gamma = colorSpace.getGamma();
3. } catch (err) {
4. console.error(`Failed to get gamma. Cause: ` + JSON.stringify(err));
5. }
```
