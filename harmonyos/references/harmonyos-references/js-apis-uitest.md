---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-uitest
title: @ohos.UiTest
breadcrumb: API参考 > 系统 > 调测调优 > Test Kit（应用测试服务） > ArkTS API > @ohos.UiTest
category: harmonyos-references
scraped_at: 2026-04-28T08:11:34+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:684b345fa6e775976e353c2d1420a3182ef28ee95750b83744811b11d7fbd757
---

UiTest提供模拟UI操作的能力，供开发者在测试场景使用，主要支持如点击、双击、长按、滑动等UI操作能力。

该模块提供以下功能：

* [On9+](js-apis-uitest.md#on9)：提供控件特征描述能力，用于控件筛选匹配查找。
* [Component9+](js-apis-uitest.md#component9)：代表UI界面上的指定控件，提供控件属性获取，控件点击，滑动查找，文本注入等能力。
* [Driver9+](js-apis-uitest.md#driver9)：入口类，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。
* [UiWindow9+](js-apis-uitest.md#uiwindow9)：入口类，提供窗口属性获取，窗口拖动、调整窗口大小等能力。
* [By(deprecated)](js-apis-uitest.md#bydeprecated)：提供控件特征描述能力，用于控件筛选匹配查找。从API version 8开始支持，从API version 9开始废弃，建议使用[On9+](js-apis-uitest.md#on9)替代。
* [UiComponent(deprecated)](js-apis-uitest.md#uicomponentdeprecated)：代表UI界面上的指定控件，提供控件属性获取，控件点击，滑动查找，文本注入等能力。从API version 8开始支持，从API version 9开始废弃，建议使用[Component9+](js-apis-uitest.md#component9)替代。
* [UiDriver(deprecated)](js-apis-uitest.md#uidriverdeprecated)：入口类，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。从API version 8开始支持，从API version 9开始废弃，建议使用[Driver9+](js-apis-uitest.md#driver9)替代。

说明

* 本模块首批接口从API version 8开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块接口在[自动化测试脚本](../harmonyos-guides/uitest-guidelines.md#使用arkts接口进行ui测试)中使用。
* 本模块接口不支持并发调用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { Component, Driver, UiWindow, ON, MatchPattern, DisplayRotation, ResizeDirection, WindowMode, PointerMatrix, UiDirection, MouseButton, UIElementInfo, UIEventObserver, UiComponent, UiDriver, BY } from '@kit.TestKit';
```

## MatchPattern

PhonePC/2in1TabletTVWearable

控件属性支持的匹配模式。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| --- | --- | --- |
| EQUALS | 0 | 等于给定值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| CONTAINS | 1 | 包含给定值。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| STARTS\_WITH | 2 | 以给定值开始。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| ENDS\_WITH | 3 | 以给定值结束。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| REG\_EXP18+ | 4 | 正则表达式匹配。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |
| REG\_EXP\_ICASE18+ | 5 | 正则表达式匹配，忽略大小写。  **元服务API：** 从API version 18开始，该接口支持在元服务中使用。 |

## ResizeDirection9+

PhonePC/2in1TabletTVWearable

窗口调整大小的方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 0 | 左方。 |
| RIGHT | 1 | 右方。 |
| UP | 2 | 上方。 |
| DOWN | 3 | 下方。 |
| LEFT\_UP | 4 | 左上方。 |
| LEFT\_DOWN | 5 | 左下方。 |
| RIGHT\_UP | 6 | 右上方。 |
| RIGHT\_DOWN | 7 | 右下方。 |

## Point9+

PhonePC/2in1TabletTVWearable

坐标点信息。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| x | number | 否 | 否 | 坐标点的横坐标，取值大于0的整数。  **说明：** 从API version 20开始，该属性不再为只读属性。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| y | number | 否 | 否 | 坐标点的纵坐标，取值大于0的整数。  **说明：** 从API version 20开始，该属性不再为只读属性。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| displayId20+ | number | 否 | 是 | 坐标点所属的屏幕ID，取值范围：大于等于0的整数。默认值为设备默认屏幕ID。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## Rect9+

PhonePC/2in1TabletTVWearable

控件的边框信息。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| left | number | 否 | 否 | 控件边框的左上角的X坐标，取值大于0的整数。  **说明：** 从API version 20开始，该属性不再为只读属性。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| top | number | 否 | 否 | 控件边框的左上角的Y坐标，取值大于0的整数。  **说明：** 从API version 20开始，该属性不再为只读属性。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| right | number | 否 | 否 | 控件边框的右下角的X坐标，取值大于0的整数。  **说明：** 从API version 20开始，该属性不再为只读属性。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| bottom | number | 否 | 否 | 控件边框的右下角的Y坐标，取值大于0的整数。  **说明：** 从API version 20开始，该属性不再为只读属性。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| displayId20+ | number | 否 | 是 | 控件边框所属的屏幕ID，取值大于或等于0的整数。默认值为设备默认屏幕ID。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## WindowMode9+

PhonePC/2in1TabletTVWearable

窗口的窗口模式。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| --- | --- | --- |
| FULLSCREEN | 0 | 全屏模式。 |
| PRIMARY | 1 | 主窗口。 |
| SECONDARY | 2 | 第二窗口。 |
| FLOATING | 3 | 浮动窗口。 |

## DisplayRotation9+

PhonePC/2in1TabletTVWearable

设备显示器的显示方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ROTATION\_0 | 0 | 设备显示器不旋转，初始形态垂直显示。 |
| ROTATION\_90 | 1 | 设备显示器顺时针旋转90°，水平显示。 |
| ROTATION\_180 | 2 | 设备显示器顺时针旋转180°，逆向垂直显示。 |
| ROTATION\_270 | 3 | 设备显示器顺时针旋转270°，逆向水平显示。 |

## WindowFilter9+

PhonePC/2in1TabletTVWearable

窗口的标志属性信息。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 否 | 是 | 窗口归属应用的包名，默认值为空。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| title | string | 否 | 是 | 窗口的标题信息，默认值为空。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| focused | boolean | 否 | 是 | 窗口是否处于获焦状态，true：获焦状态，false：未获焦状态，默认值为false。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| actived(deprecated) | boolean | 否 | 是 | 窗口是否正与用户进行交互，true：交互状态，false：未交互状态，默认值为false。  从API version 11开始废弃，建议使用active替代。 |
| active11+ | boolean | 否 | 是 | 窗口是否正与用户进行交互，true：交互状态，false：未交互状态，默认值为false。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| displayId20+ | number | 否 | 是 | 窗口所属的屏幕ID。取值大于或等于0的整数。默认值为设备默认屏ID。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## UiDirection10+

PhonePC/2in1TabletTVWearable

进行抛滑等UI操作时的方向。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 0 | 向左。 |
| RIGHT | 1 | 向右。 |
| UP | 2 | 向上。 |
| DOWN | 3 | 向下。 |

## MouseButton10+

PhonePC/2in1TabletTVWearable

模拟注入的鼠标按钮。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| --- | --- | --- |
| MOUSE\_BUTTON\_LEFT | 0 | 鼠标左键。 |
| MOUSE\_BUTTON\_RIGHT | 1 | 鼠标右键。 |
| MOUSE\_BUTTON\_MIDDLE | 2 | 鼠标中间键。 |

## WindowChangeType22+

PhonePC/2in1TabletTVWearable

支持监听的窗口变化事件类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| --- | --- | --- |
| WINDOW\_UNDEFINED | 0 | 非窗口变化事件。  **说明：** 该枚举值仅支持作为返回值，如果作为接口入参会抛出异常。 |
| WINDOW\_ADDED | 1 | 窗口出现事件。 |
| WINDOW\_REMOVED | 2 | 窗口消失事件。 |
| WINDOW\_BOUNDS\_CHANGED | 3 | 窗口边框变化事件。 |

## ComponentEventType22+

PhonePC/2in1TabletTVWearable

支持监听的控件操作事件类型。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 值 | 说明 |
| --- | --- | --- |
| COMPONENT\_UNDEFINED | 0 | 非控件操作事件。  **说明：** 该枚举值仅支持作为返回值，如果作为接口入参会抛出异常。 |
| COMPONENT\_CLICKED | 1 | 控件被点击事件。 |
| COMPONENT\_LONG\_CLICKED | 2 | 控件被长按事件。 |
| COMPONENT\_SCROLL\_START | 3 | 控件滚动开始事件。 |
| COMPONENT\_SCROLL\_END | 4 | 控件滚动结束事件。 |
| COMPONENT\_TEXT\_CHANGED | 5 | [输入框控件](../harmonyos-guides/arkts-common-components-text-input.md)文本变化事件。 |

## WindowChangeOptions22+

PhonePC/2in1TabletTVWearable

窗口变化事件监听的扩展配置，用于指定监听过程配置及事件筛选条件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number | 否 | 是 | 监听超时时间，默认值为10000，单位：ms。 |
| bundleName | string | 否 | 是 | 监听窗口对应包名，缺省时默认监听所有窗口。 |

## ComponentEventOptions22+

PhonePC/2in1TabletTVWearable

控件操作事件监听的扩展配置，用于指定监听过程配置及事件筛选条件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| timeout | number | 否 | 是 | 监听超时时间，默认值为10000，单位：ms。 |
| on | [On](js-apis-uitest.md#on9) | 否 | 是 | 监听目标控件的属性要求，默认监听所有控件。  **说明：** 仅支持监听指定属性要求的控件，不支持监听指定On.isBefore、On.isAfter、On.within等相对位置的控件。 |

## UIElementInfo10+

PhonePC/2in1TabletTVWearable

UI事件的相关信息。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| bundleName | string | 是 | 否 | 应用包名。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| type | string | 是 | 否 | 控件/窗口类型。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| text | string | 是 | 否 | 控件/窗口的文本信息。  **元服务API：** 从API version 11开始，该接口支持在元服务中使用。 |
| windowChangeType22+ | [WindowChangeType](js-apis-uitest.md#windowchangetype22) | 是 | 是 | 窗口变化事件类型，若非窗口变化事件返回WindowChangeType.WINDOW\_UNDEFINED。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| componentEventType22+ | [ComponentEventType](js-apis-uitest.md#componenteventtype22) | 是 | 是 | 控件操作事件类型，若非控件操作事件返回ComponentEventType.COMPONENT\_UNDEFINED。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| windowId22+ | number | 是 | 是 | 控件所属窗口id。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| componentId22+ | string | 是 | 是 | 控件id，若非控件操作事件返回空字符串。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |
| componentRect22+ | [Rect](js-apis-uitest.md#rect9) | 是 | 是 | 控件边框信息，若非控件操作事件则返回属性值均为0的Rect对象。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

## TouchPadSwipeOptions18+

PhonePC/2in1TabletTVWearable

触摸板多指滑动手势选项相关信息。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| stay | boolean | 否 | 是 | 触摸板多指滑动结束是否停留1s后再抬起，默认为false（不停留1s），true：停留，false：不停留。 |
| speed | number | 否 | 是 | 滑动速率，取值范围为200-40000的整数，默认值为2000，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值2000。为负数时抛出参数错误的错误码。 |

## InputTextMode20+

PhonePC/2in1TabletTVWearable

输入文本的方式。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| paste | boolean | 否 | 是 | 输入文本时是否指定以复制粘贴方式输入。true：指定以复制粘贴方式输入。false：指定以逐字键入方式输入。默认为false。  **说明：** 当输入文本中包含中文、特殊字符或文本长度超过200字符时，无论该参数取值为何，均以复制粘贴方式输入。 |
| addition | boolean | 否 | 是 | 输入文本时是否以追加的方式进行输入。true：以追加方式输入。false：不以追加方式输入。默认为false。 |

## On9+

PhonePC/2in1TabletTVWearable

UiTest框架从API version 9开始，通过On类提供了丰富的控件特征描述API，用于进行控件筛选来匹配/查找出目标控件。

On提供的API能力具有以下几个特点:

1、支持单属性匹配和多属性组合匹配，例如同时指定目标控件text和id。

2、控件属性支持多种匹配模式。

3、支持控件绝对定位，相对定位，可通过[ON.isBefore](js-apis-uitest.md#isbefore9)和[ON.isAfter](js-apis-uitest.md#isafter9)等API限定邻近控件特征进行辅助定位。

On类提供的所有API均为同步接口，建议使用者通过静态构造器ON来链式创建On对象。

```
1. // xxx.test.ets
2. import { ON } from '@kit.TestKit';

4. ON.text('123').type('Button');
```

### text9+

PhonePC/2in1TabletTVWearable

text(txt: string, pattern?: MatchPattern): On

指定目标控件文本属性，支持多种匹配模式，返回On对象自身。

说明

如果控件的无障碍属性[accessibilityLevel](ts-universal-attributes-accessibility.md#accessibilitylevel)设置为'no'或'no-hide-descendants'，无法使用本接口指定目标控件的文本属性用于查找控件，可以使用[On.originalText()](js-apis-uitest.md#originaltext20)接口实现。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| txt | string | 是 | 指定控件文本，用于匹配目标控件文本。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |
| pattern | [MatchPattern](js-apis-uitest.md#matchpattern) | 否 | 指定的文本匹配模式，默认为[EQUALS](js-apis-uitest.md#matchpattern)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件文本属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.text('123'); // 使用静态构造器ON创建On对象，指定目标控件的text属性。
```

### id9+

PhonePC/2in1TabletTVWearable

id(id: string): On

指定目标控件id属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 指定控件的id值。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件id属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.id('123'); // 使用静态构造器ON创建On对象，指定目标控件的id属性。
```

### id18+

PhonePC/2in1TabletTVWearable

id(id: string, pattern: MatchPattern): On

指定目标控件id属性和匹配模式，返回On对象自身。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | string | 是 | 指定控件的id值。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |
| pattern | [MatchPattern](js-apis-uitest.md#matchpattern) | 是 | 指定的文本匹配模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件id属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { MatchPattern, On, ON } from '@kit.TestKit';

4. let on: On = ON.id('id', MatchPattern.REG_EXP_ICASE); // 忽略大小写匹配控件的id属性值
```

### type9+

PhonePC/2in1TabletTVWearable

type(tp: string): On

指定目标控件的控件类型属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tp | string | 是 | 指定控件类型。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件的控件类型属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.type('Button'); // 使用静态构造器ON创建On对象，指定目标控件的控件类型属性。
```

### type18+

PhonePC/2in1TabletTVWearable

type(tp: string, pattern: MatchPattern): On

指定目标控件的控件类型属性和匹配模式，返回On对象自身。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tp | string | 是 | 指定控件类型。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |
| pattern | [MatchPattern](js-apis-uitest.md#matchpattern) | 是 | 指定的文本匹配模式。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件的控件类型属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON, MatchPattern } from '@kit.TestKit';

4. let on: On = ON.type('Button', MatchPattern.EQUALS); // 使用静态构造器ON创建On对象，指定目标控件的控件类型属性。
```

### clickable9+

PhonePC/2in1TabletTVWearable

clickable(b?: boolean): On

指定目标控件的可点击状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件可点击状态。true：可点击。false：不可点击。默认为true。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件的可点击状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.clickable(true); // 使用静态构造器ON创建On对象，指定目标控件的可点击状态属性。
```

### longClickable9+

PhonePC/2in1TabletTVWearable

longClickable(b?: boolean): On

指定目标控件的可长按点击状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件可长按点击状态。true：可长按点击。false：不可长按点击。默认为true。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件的可长按点击状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.longClickable(true); // 使用静态构造器ON创建On对象，指定目标控件的可长按点击状态属性。
```

### scrollable9+

PhonePC/2in1TabletTVWearable

scrollable(b?: boolean): On

指定目标控件的可滑动状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 控件可滑动状态。true：可滑动。false：不可滑动。默认为true。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件的可滑动状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.scrollable(true); // 使用静态构造器ON创建On对象，指定目标控件的可滑动状态属性。
```

### enabled9+

PhonePC/2in1TabletTVWearable

enabled(b?: boolean): On

指定目标控件的使能状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件使能状态。true：使能。false：未使能。默认为true。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件的使能状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.enabled(true); // 使用静态构造器ON创建On对象，指定目标控件的使能状态属性。
```

### focused9+

PhonePC/2in1TabletTVWearable

focused(b?: boolean): On

指定目标控件的获焦状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 控件获焦状态。true：获焦。false：未获焦。默认为true。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件的获焦状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.focused(true); // 使用静态构造器ON创建On对象，指定目标控件的获焦状态属性。
```

### selected9+

PhonePC/2in1TabletTVWearable

selected(b?: boolean): On

指定目标控件的被选中状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件被选中状态。true：被选中。false：未被选中。默认为true。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件的被选中状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.selected(true); // 使用静态构造器ON创建On对象，指定目标控件的被选中状态属性。
```

### checked9+

PhonePC/2in1TabletTVWearable

checked(b?: boolean): On

指定目标控件的被勾选状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件被勾选状态。true：被勾选。false：未被勾选。默认为true。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件的被勾选状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.checked(true); // 使用静态构造器ON创建On对象，指定目标控件的被勾选状态属性
```

### checkable9+

PhonePC/2in1TabletTVWearable

checkable(b?: boolean): On

指定目标控件能否被勾选状态属性，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件能否被勾选状态。true：能被勾选。false：不能被勾选。默认为true。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件能否被勾选状态属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.checkable(true); // 使用静态构造器ON创建On对象，指定目标控件的能否被勾选状态属性。
```

### isBefore9+

PhonePC/2in1TabletTVWearable

isBefore(on: On): On

指定目标控件位于给出的特征属性控件之前，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | [On](js-apis-uitest.md#on9) | 是 | 特征控件的属性要求。 可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件树，以判断控件间位置关系。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件位于给出的特征属性控件之前的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. // 使用静态构造器ON创建On对象，指定目标控件位于给出的特征属性控件之前。
5. let on: On = ON.type('Button').isBefore(ON.text('123')); // 查找text为123之前的第一个Button组件
```

### isAfter9+

PhonePC/2in1TabletTVWearable

isAfter(on: On): On

指定目标控件位于给出的特征属性控件之后，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | [On](js-apis-uitest.md#on9) | 是 | 特征控件的属性要求。 可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件树，以判断控件间位置关系。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件位于给出的特征属性控件之后的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. // 使用静态构造器ON创建On对象，指定目标控件位于给出的特征属性控件之后。
5. let on: On = ON.type('Text').isAfter(ON.text('123')); // 查找 text为123之后的第一个Text组件
```

### within10+

PhonePC/2in1TabletTVWearable

within(on: On): On

指定目标控件位于给出的特征属性控件之内，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | [On](js-apis-uitest.md#on9) | 是 | 特征控件的属性要求。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件树，以判断控件间位置关系。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件位于给出的特征属性控件内的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. // 使用静态构造器ON创建On对象，指定目标控件位于给出的特征属性控件之内。
5. let on: On = ON.text('java').within(ON.type('Scroll')); // 查找Scroller里面的text为java的子组件
```

### inWindow10+

PhonePC/2in1TabletTVWearable

inWindow(bundleName: string): On

指定目标控件位于给出的应用窗口内，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| bundleName | string | 是 | 应用窗口的包名。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件位于给出的应用窗口内的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.inWindow('com.uitestScene.acts'); // 使用静态构造器ON创建On对象，指定目标控件位于给出的应用窗口内。
```

### description11+

PhonePC/2in1TabletTVWearable

description(val: string, pattern?: MatchPattern): On

指定目标控件的描述属性，支持多种匹配模式，返回On对象自身。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | string | 是 | 控件的描述属性。 可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |
| pattern | [MatchPattern](js-apis-uitest.md#matchpattern) | 否 | 指定的文本匹配模式，默认为[EQUALS](js-apis-uitest.md#matchpattern)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件description属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.description('123'); // 使用静态构造器ON创建On对象，指定目标控件的description属性。
```

### hint18+

PhonePC/2in1TabletTVWearable

hint(val: string, pattern?: MatchPattern): On

获取指定提示文本的控件对象，返回On对象自身。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| val | string | 是 | 指定控件提示文本。 可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |
| pattern | [MatchPattern](js-apis-uitest.md#matchpattern) | 否 | 指定的文本匹配模式，默认为[EQUALS](js-apis-uitest.md#matchpattern)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定提示文本控件的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { MatchPattern, On, ON } from '@kit.TestKit';

4. let on: On = ON.hint('welcome', MatchPattern.EQUALS); // 使用静态构造器ON创建On对象，指定目标控件的提示文本属性。
```

### belongingDisplay20+

PhonePC/2in1TabletTVWearable

belongingDisplay(displayId: number): On

获取指定屏幕内的控件对象，返回On对象自身。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 指定控件所属屏幕ID，取值范围：大于等于0的整数。  **说明：** 传入displayId不存在时，将抛出17000007异常。可通过[getAllDisplays](js-apis-display.md#displaygetalldisplays9)获取当前所有的display对象，并由display对象获取对应的屏幕ID。可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定控件所属屏幕的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.belongingDisplay(0); // 使用静态构造器ON创建On对象，指定目标控件所属屏幕ID
```

### originalText20+

PhonePC/2in1TabletTVWearable

originalText(text: string, pattern?: MatchPattern): On

指定控件的文本内容和文本匹配模式，返回On对象自身。

说明

如果控件的无障碍属性[accessibilityLevel](ts-universal-attributes-accessibility.md#accessibilitylevel)设置为'no'或'no-hide-descendants'，可以使用本接口指定目标控件的文本属性用于查找控件，使用[On.text()](js-apis-uitest.md#text9)接口不生效。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 指定控件文本，用于匹配目标控件文本。 可以借助[DevEco Testing](../harmonyos-guides/deveco-testing.md)中UiViewer获取控件节点属性。 |
| pattern | [MatchPattern](js-apis-uitest.md#matchpattern) | 否 | 指定的文本匹配模式，默认为[EQUALS](js-apis-uitest.md#matchpattern)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [On](js-apis-uitest.md#on9) | 返回指定目标控件文本属性的On对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { On, ON } from '@kit.TestKit';

4. let on: On = ON.originalText('123'); // 使用静态构造器ON创建On对象，指定目标控件的originalText属性
```

## Component9+

PhonePC/2in1TabletTVWearable

UiTest框架在API9中，Component类代表了UI界面上的一个控件，提供控件属性获取，控件点击，滑动查找，文本注入等API。

该类提供的所有方法都使用Promise方式作为异步方法，需使用await调用。

### click9+

PhonePC/2in1TabletTVWearable

click(): Promise<void>

控件对象进行点击操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, ON, Component } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. await button.click();
8. }
```

### doubleClick9+

PhonePC/2in1TabletTVWearable

doubleClick(): Promise<void>

控件对象进行双击操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. await button.doubleClick();
8. }
```

### longClick9+

PhonePC/2in1TabletTVWearable

longClick(): Promise<void>

控件对象进行长按操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. await button.longClick();
8. }
```

### getId9+

PhonePC/2in1TabletTVWearable

getId(): Promise<string>

获取控件对象的id值。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的id值。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. let id = await button.getId();
8. }
```

### getText9+

PhonePC/2in1TabletTVWearable

getText(): Promise<string>

获取控件对象的文本信息。使用Promise异步回调。

说明

如果控件的无障碍属性[accessibilityLevel](ts-universal-attributes-accessibility.md#accessibilitylevel)设置为'no'或'no-hide-descendants'，无法使用本接口获取控件的文本信息，可以使用[Component.getOriginalText()](js-apis-uitest.md#getoriginaltext20)获取控件的文本信息。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的文本信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. let text = await button.getText();
8. }
```

### getType9+

PhonePC/2in1TabletTVWearable

getType(): Promise<string>

获取控件对象的控件类型。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的类型。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. let type = await button.getType();
8. }
```

### getBounds9+

PhonePC/2in1TabletTVWearable

getBounds(): Promise<Rect>

获取控件对象的边框信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Rect](js-apis-uitest.md#rect9)> | Promise对象，返回控件对象的边框信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. let rect = await button.getBounds();
8. }
```

### getBoundsCenter9+

PhonePC/2in1TabletTVWearable

getBoundsCenter(): Promise<Point>

获取控件对象所占区域的中心点信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Point](js-apis-uitest.md#point9)> | Promise对象，返回控件对象所占区域的中心点信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. let point = await button.getBoundsCenter();
8. }
```

### isClickable9+

PhonePC/2in1TabletTVWearable

isClickable(): Promise<boolean>

获取控件对象可点击属性。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象是否可点击。true：可点击。false：不可点击。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. if (await button.isClickable()) {
8. console.info('This button can be Clicked');
9. } else {
10. console.info('This button can not be Clicked');
11. }
12. }
```

### isLongClickable9+

PhonePC/2in1TabletTVWearable

isLongClickable(): Promise<boolean>

获取控件对象可长按点击属性。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象是否可长按点击。true：可长按点击。false：不可长按点击。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. if (await button.isLongClickable()) {
8. console.info('This button can longClick');
9. } else {
10. console.info('This button can not longClick');
11. }
12. }
```

### isChecked9+

PhonePC/2in1TabletTVWearable

isChecked(): Promise<boolean>

获取控件对象被勾选状态。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象被勾选状态。true：被勾选。false：未被勾选。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let checkBox: Component = await driver.findComponent(ON.type('Checkbox'));
7. if (await checkBox.isChecked()) {
8. console.info('This checkBox is checked');
9. } else {
10. console.info('This checkBox is not checked');
11. }
12. }
```

### isCheckable9+

PhonePC/2in1TabletTVWearable

isCheckable(): Promise<boolean>

获取控件对象能否被勾选属性。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象能否可被勾选属性。true：可被勾选。false：不可被勾选。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let checkBox: Component = await driver.findComponent(ON.type('Checkbox'));
7. if (await checkBox.isCheckable()) {
8. console.info('This checkBox is checkable');
9. } else {
10. console.info('This checkBox is not checkable');
11. }
12. }
```

### isScrollable9+

PhonePC/2in1TabletTVWearable

isScrollable(): Promise<boolean>

获取控件对象可滑动属性。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象是否可滑动。true：可滑动。false：不可滑动。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let scrollBar: Component = await driver.findComponent(ON.scrollable(true));
7. if (await scrollBar.isScrollable()) {
8. console.info('This scrollBar can be operated');
9. } else {
10. console.info('This scrollBar can not be operated');
11. }
12. }
```

### isEnabled9+

PhonePC/2in1TabletTVWearable

isEnabled(): Promise<boolean>

获取控件使能状态。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件使能状态。true：使能。false：未使能。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. if (await button.isEnabled()) {
8. console.info('This button can be operated');
9. } else {
10. console.info('This button can not be operated');
11. }
12. }
```

### isFocused9+

PhonePC/2in1TabletTVWearable

isFocused(): Promise<boolean>

判断控件对象获焦状态。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象获焦状态。true：获焦。false：未获焦。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. if (await button.isFocused()) {
8. console.info('This button is focused');
9. } else {
10. console.info('This button is not focused');
11. }
12. }
```

### isSelected9+

PhonePC/2in1TabletTVWearable

isSelected(): Promise<boolean>

获取控件对象被选中状态。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象被选中状态。true：被选中。false：未被选中。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. if (await button.isSelected()) {
8. console.info('This button is selected');
9. } else {
10. console.info('This button is not selected');
11. }
12. }
```

### inputText9+

PhonePC/2in1TabletTVWearable

inputText(text: string): Promise<void>

清空组件内原有文本并输入指定文本内容，仅针对可编辑的文本组件生效。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 输入的文本信息，当前支持英文、中文和特殊字符。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let text: Component = await driver.findComponent(ON.text('hello world'));
7. await text.inputText('123');
8. }
```

### inputText20+

PhonePC/2in1TabletTVWearable

inputText(text: string, mode: InputTextMode): Promise<void>

向控件中输入文本，并支持指定文本输入方式，仅针对可编辑的文本组件生效。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 输入的文本信息，当前支持英文、中文和特殊字符。 |
| mode | [InputTextMode](js-apis-uitest.md#inputtextmode20) | 是 | 输入文本的方式，取值请参考[InputTextMode](js-apis-uitest.md#inputtextmode20)。  **说明：** InputTextMode.addition取值为true时，在控件已有文本末尾后追加指定文本。取值为false时，指定文本将覆盖控件已有文本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported, function can not work correctly due to limited device capabilities. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function mode_demo() {
5. let driver: Driver = Driver.create();
6. let text: Component = await driver.findComponent(ON.text('hello world'));
7. await text.inputText('123', { paste: true, addition: false });
8. }
```

### clearText9+

PhonePC/2in1TabletTVWearable

clearText(): Promise<void>

清除控件的文本信息，仅针对可编辑的文本组件生效。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let text: Component = await driver.findComponent(ON.text('hello world'));
7. await text.clearText();
8. }
```

### scrollSearch9+

PhonePC/2in1TabletTVWearable

scrollSearch(on: On): Promise<Component>

在控件上滑动查找目标控件（适用支持滑动的控件）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | [On](js-apis-uitest.md#on9) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Component](js-apis-uitest.md#component9)> | Promise对象，返回目标控件对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
7. let button = await scrollBar.scrollSearch(ON.text('next page'));
8. }
```

### scrollSearch18+

PhonePC/2in1TabletTVWearable

scrollSearch(on: On, vertical?: boolean, offset?: number): Promise<Component>

在控件上滑动查找目标控件（适用支持滑动的控件），支持指定滑动方向和滑动起止点与组件边框的偏移量。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | [On](js-apis-uitest.md#on9) | 是 | 目标控件的属性要求。 |
| vertical | boolean | 否 | 默认为true，表示查找方向是纵向。false表示查找方向为横向。 |
| offset | number | 否 | 滑动起点/终点到组件边框的偏移，默认80，单位：px，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Component](js-apis-uitest.md#component9)> | Promise对象，返回目标控件对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
7. let button = await scrollBar.scrollSearch(ON.text('next page'));
8. }
```

### scrollToTop9+

PhonePC/2in1TabletTVWearable

scrollToTop(speed?: number): Promise<void>

在控件上滑动到顶部（适用支持滑动的控件）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
7. await scrollBar.scrollToTop();
8. }
```

### scrollToBottom9+

PhonePC/2in1TabletTVWearable

scrollToBottom(speed?: number): Promise<void>

在控件上滑动到底部（适用支持滑动的控件）。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let scrollBar: Component = await driver.findComponent(ON.type('Scroll'));
7. await scrollBar.scrollToBottom();
8. }
```

### dragTo9+

PhonePC/2in1TabletTVWearable

dragTo(target: Component): Promise<void>

将控件拖拽至目标控件处。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| target | [Component](js-apis-uitest.md#component9) | 是 | 目标控件。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. let text: Component = await driver.findComponent(ON.text('hello world'));
8. await button.dragTo(text);
9. }
```

### pinchOut9+

PhonePC/2in1TabletTVWearable

pinchOut(scale: number): Promise<void>

将控件按指定的比例进行捏合放大。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | 是 | 指定放大的比例。取值范围大于1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let image: Component = await driver.findComponent(ON.type('Image'));
7. await image.pinchOut(1.5);
8. }
```

### pinchIn9+

PhonePC/2in1TabletTVWearable

pinchIn(scale: number): Promise<void>

将控件按指定的比例进行捏合缩小。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | number | 是 | 指定缩小的比例。取值范围为0~1。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let image: Component = await driver.findComponent(ON.type('Image'));
7. await image.pinchIn(0.5);
8. }
```

### getDescription11+

PhonePC/2in1TabletTVWearable

getDescription(): Promise<string>

获取控件对象的描述信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的描述信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. let description = await button.getDescription();
8. }
```

### getHint18+

PhonePC/2in1TabletTVWearable

getHint(): Promise<string>

获取控件对象的提示文本。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的提示文本。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('TextInput'));
7. let hints = await button.getHint();
8. }
```

### getDisplayId20+

PhonePC/2in1TabletTVWearable

getDisplayId(): Promise<number>

获取控件对象所属的屏幕ID。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回控件所属的屏幕ID。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('TextInput'));
7. let displayId = await button.getDisplayId();
8. }
```

### getOriginalText20+

PhonePC/2in1TabletTVWearable

getOriginalText(): Promise<string>

获取控件对象的文本信息。使用Promise异步回调。如果控件的无障碍属性[accessibilityLevel](ts-universal-attributes-accessibility.md#accessibilitylevel)设置为'no'或'no-hide-descendants'，可以使用本接口获取控件的文本信息，无法使用[Component.getText()](js-apis-uitest.md#gettext9)获取控件的文本信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的文本信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.type('Button'));
7. let text = await button.getOriginalText();
8. }
```

## Driver9+

PhonePC/2in1TabletTVWearable

Driver类为uitest测试框架的总入口，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等能力。

该类提供的方法除Driver.create()以外的所有方法都使用Promise方式作为异步方法，需使用await方式调用。

### create9+

PhonePC/2in1TabletTVWearable

static create(): Driver

静态方法，构造一个Driver对象，并返回该对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Driver | 返回构造的Driver对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000001 | Initialization failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. }
```

### delayMs9+

PhonePC/2in1TabletTVWearable

delayMs(duration: number): Promise<void>

在给定的时间内延时。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| duration | number | 是 | 给定的时间，单位：ms，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.delayMs(1000);
7. }
```

### findComponent9+

PhonePC/2in1TabletTVWearable

findComponent(on: On): Promise<Component>

根据给出的目标控件属性要求查找目标控件。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | [On](js-apis-uitest.md#on9) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Component](js-apis-uitest.md#component9)> | Promise对象，返回控件对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.findComponent(ON.text('next page'));
7. }
```

### findComponents9+

PhonePC/2in1TabletTVWearable

findComponents(on: On): Promise<Array<Component>>

根据给出的目标控件属性要求查找出所有匹配控件，以列表保存。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | [On](js-apis-uitest.md#on9) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[Component](js-apis-uitest.md#component9)>> | Promise对象，返回控件对象的列表。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let buttonList: Array<Component> = await driver.findComponents(ON.text('next page'));
7. }
```

### findWindow9+

PhonePC/2in1TabletTVWearable

findWindow(filter: WindowFilter): Promise<UiWindow>

通过指定窗口的属性来查找目标窗口。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| filter | [WindowFilter](js-apis-uitest.md#windowfilter9) | 是 | 目标窗口的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[UiWindow](js-apis-uitest.md#uiwindow9)> | Promise对象，返回目标窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. }
```

### waitForComponent9+

PhonePC/2in1TabletTVWearable

waitForComponent(on: On, time: number): Promise<Component>

在用户给定的时间内，持续查找满足控件属性要求的目标控件。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | [On](js-apis-uitest.md#on9) | 是 | 目标控件的属性要求。 |
| time | number | 是 | 查找目标控件的持续时间。单位ms，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Component](js-apis-uitest.md#component9)> | Promise对象，返回控件对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let button: Component = await driver.waitForComponent(ON.text('next page'), 500);
7. }
```

### assertComponentExist9+

PhonePC/2in1TabletTVWearable

assertComponentExist(on: On): Promise<void>

断言API，用于断言当前界面是否存在满足给出的目标属性的控件。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | [On](js-apis-uitest.md#on9) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000003 | Assertion failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.assertComponentExist(ON.text('next page'));
7. }
```

### pressBack9+

PhonePC/2in1TabletTVWearable

pressBack(): Promise<void>

进行点击BACK键的操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.pressBack();
7. }
```

### pressBack20+

PhonePC/2in1TabletTVWearable

pressBack(displayId: number): Promise<void>

对指定屏幕进行点击BACK键的操作。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 指定的屏幕ID，取值范围：大于等于0的整数。  **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.pressBack(0);
7. }
```

### triggerKey9+

PhonePC/2in1TabletTVWearable

triggerKey(keyCode: number): Promise<void>

传入key值实现模拟点击对应按键的效果。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyCode | number | 是 | 指定的key值，取值范围：大于等于0的整数。取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';
3. import { KeyCode } from '@kit.InputKit';

5. async function demo() {
6. let driver: Driver = Driver.create();
7. await driver.triggerKey(KeyCode.KEYCODE_BACK); // 返回键
8. }
```

### triggerKey20+

PhonePC/2in1TabletTVWearable

triggerKey(keyCode: number, displayId: number): Promise<void>

在指定屏幕，传入key值实现模拟点击对应按键的效果。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyCode | number | 是 | 指定的key值，取值范围：大于等于0的整数。取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)。 |
| displayId | number | 是 | 指定的屏幕ID，取值范围：大于等于0的整数。  **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';
3. import { KeyCode } from '@kit.InputKit';

5. async function demo() {
6. let driver: Driver = Driver.create();
7. await driver.triggerKey(KeyCode.KEYCODE_BACK, 0); // 返回键
8. }
```

### triggerCombineKeys9+

PhonePC/2in1TabletTVWearable

triggerCombineKeys(key0: number, key1: number, key2?: number): Promise<void>

通过给定的key值，找到对应组合键并点击。使用Promise异步回调。例如，Key值为(2072, 2019)时，找到key值对应的组合键并点击，如Ctrl+c。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key0 | number | 是 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)。 |
| key1 | number | 是 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)。 |
| key2 | number | 否 | 指定的第三个key值，取值范围：大于等于0的整数。取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)，默认值为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.triggerCombineKeys(2072, 2047, 2035);
7. }
```

### triggerCombineKeys20+

PhonePC/2in1TabletTVWearable

triggerCombineKeys(key0: number, key1: number, key2?: number, displayId?: number): Promise<void>

通过给定的key值，找到对应组合键，并在指定屏幕下进行点击。使用Promise异步回调。例如，Key值为(2072, 2019)时，找到key值对应的组合键并点击，如Ctrl+c。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key0 | number | 是 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)。 |
| key1 | number | 是 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)。 |
| key2 | number | 否 | 指定的第三个key值，取值范围：大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)，默认值为0。 |
| displayId | number | 否 | 指定的屏幕ID，取值范围：大于等于0的整数，默认值为设备默认屏幕ID。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.triggerCombineKeys(2072, 2047, 2035, 0);
7. }
```

### click9+

PhonePC/2in1TabletTVWearable

click(x: number, y: number): Promise<void>

在目标坐标点单击。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.click(100, 100);
7. }
```

### clickAt20+

PhonePC/2in1TabletTVWearable

clickAt(point: Point): Promise<void>

在目标坐标点进行单击。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [Point](js-apis-uitest.md#point9) | 是 | 以Point对象的形式传入目标点信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.clickAt({ x: 100, y: 100, displayId: 0 });
7. }
```

### doubleClick9+

PhonePC/2in1TabletTVWearable

doubleClick(x: number, y: number): Promise<void>

在目标坐标点双击。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.doubleClick(100, 100);
7. }
```

### doubleClickAt20+

PhonePC/2in1TabletTVWearable

doubleClickAt(point: Point): Promise<void>

对目标坐标进行双击。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [Point](js-apis-uitest.md#point9) | 是 | 以Point对象的形式传入目标点信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.doubleClickAt({ x: 100, y: 100, displayId: 0 });
7. }
```

### longClick9+

PhonePC/2in1TabletTVWearable

longClick(x: number, y: number): Promise<void>

在目标坐标点长按。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.longClick(100, 100);
7. }
```

### longClickAt20+

PhonePC/2in1TabletTVWearable

longClickAt(point: Point, duration?: number): Promise<void>

长按目标坐标点，支持指定长按时长。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [Point](js-apis-uitest.md#point9) | 是 | 以Point对象的形式传入目标点信息。 |
| duration | number | 否 | 长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.longClickAt({ x: 100, y: 100, displayId: 0 }, 1500);
7. }
```

### swipe9+

PhonePC/2in1TabletTVWearable

swipe(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>

从起始坐标点滑向目的坐标点。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startx | number | 是 | 以number的形式传入起始点的横坐标信息，取值范围：大于等于0的整数。 |
| starty | number | 是 | 以number的形式传入起始点的纵坐标信息，取值范围：大于等于0的整数。 |
| endx | number | 是 | 以number的形式传入目的点的横坐标信息，取值范围：大于等于0的整数。 |
| endy | number | 是 | 以number的形式传入目的点的纵坐标信息，取值范围：大于等于0的整数。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.swipe(100, 100, 200, 200, 600);
7. }
```

### swipeBetween20+

PhonePC/2in1TabletTVWearable

swipeBetween(from: Point, to: Point, speed?: number): Promise<void>

从起始坐标点滑向目标坐标点。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | [Point](js-apis-uitest.md#point9) | 是 | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | [Point](js-apis-uitest.md#point9) | 是 | 以Point对象的形式传入终止点的坐标信息和所属屏幕ID。  **说明：** 应与起始点属于同一个屏幕，否则将抛出17000007异常。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.swipeBetween({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, 800);
7. }
```

### drag9+

PhonePC/2in1TabletTVWearable

drag(startx: number, starty: number, endx: number, endy: number, speed?: number): Promise<void>

从起始坐标点拖拽至目的坐标点。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startx | number | 是 | 以number的形式传入起始点的横坐标信息，取值范围：大于等于0的整数。 |
| starty | number | 是 | 以number的形式传入起始点的纵坐标信息，取值范围：大于等于0的整数。 |
| endx | number | 是 | 以number的形式传入目的点的横坐标信息，取值范围：大于等于0的整数。 |
| endy | number | 是 | 以number的形式传入目的点的纵坐标信息，取值范围：大于等于0的整数。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.drag(100, 100, 200, 200, 600);
7. }
```

### dragBetween20+

PhonePC/2in1TabletTVWearable

dragBetween(from: Point, to: Point, speed?: number, duration?: number): Promise<void>

从起始坐标点拖拽至目标坐标点，支持指定拖拽速度和拖拽前长按时间。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | [Point](js-apis-uitest.md#point9) | 是 | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | [Point](js-apis-uitest.md#point9) | 是 | 以Point对象的形式传入终止点的坐标信息和所属屏幕ID。  **说明：** 应与起始点属于同一个屏幕，否则将抛出17000007异常。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |
| duration | number | 否 | 拖拽前长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.dragBetween({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, 800, 1500);
7. }
```

### screenCap9+

PhonePC/2in1TabletTVWearable

screenCap(savePath: string): Promise<boolean>

捕获当前屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| savePath | string | 是 | 文件保存路径。路径需为当前应用的[沙箱路径](../harmonyos-guides/app-sandbox-directory.md)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回截图操作是否成功完成。true：完成，false：未完成。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.screenCap('/data/storage/el2/base/cache/1.png');
7. }
```

### screenCap20+

PhonePC/2in1TabletTVWearable

screenCap(savePath: string, displayId: number): Promise<boolean>

捕获指定屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| savePath | string | 是 | 文件保存路径。路径需为当前应用的[沙箱路径](../harmonyos-guides/app-sandbox-directory.md)。 |
| displayId | number | 是 | 指定设备屏幕ID。取值范围：大于等于0的整数。  **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回截图操作是否成功完成。true：完成。false：未完成。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.screenCap('/data/storage/el2/base/cache/1.png', 0);
7. }
```

### setDisplayRotation9+

PhonePC/2in1TabletTVWearable

setDisplayRotation(rotation: DisplayRotation): Promise<void>

将当前场景的显示方向设置为指定的显示方向。使用Promise异步回调。适用于可旋转的应用场景。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotation | [DisplayRotation](js-apis-uitest.md#displayrotation9) | 是 | 设备的显示方向。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, DisplayRotation } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.setDisplayRotation(DisplayRotation.ROTATION_180);
7. }
```

### getDisplayRotation9+

PhonePC/2in1TabletTVWearable

getDisplayRotation(): Promise<DisplayRotation>

获取当前设备的屏幕显示方向。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DisplayRotation](js-apis-uitest.md#displayrotation9)> | Promise对象，返回当前设备的显示方向。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |

**示例：**

```
1. // xxx.test.ets
2. import { DisplayRotation, Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let rotation: DisplayRotation = await driver.getDisplayRotation();
7. }
```

### getDisplayRotation20+

PhonePC/2in1TabletTVWearable

getDisplayRotation(displayId: number): Promise<DisplayRotation>

获取当前设备指定屏幕的显示方向。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 指定设备屏幕ID。取值范围：大于等于0的整数。  **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[DisplayRotation](js-apis-uitest.md#displayrotation9)> | Promise对象，返回指定屏幕的显示方向。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { DisplayRotation, Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let rotation: DisplayRotation = await driver.getDisplayRotation(0);
7. }
```

### setDisplayRotationEnabled9+

PhonePC/2in1TabletTVWearable

setDisplayRotationEnabled(enabled: boolean): Promise<void>

启用/禁用设备旋转屏幕的功能。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| enabled | boolean | 是 | 能否旋转屏幕的标识。true：可以旋转。false：不可以旋转。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.setDisplayRotationEnabled(false);
7. }
```

### getDisplaySize9+

PhonePC/2in1TabletTVWearable

getDisplaySize(): Promise<Point>

获取当前设备的屏幕大小。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Point](js-apis-uitest.md#point9)> | Promise对象，返回Point对象，当前设备屏幕的大小为Point.x \* Point.y。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let size = await driver.getDisplaySize();
7. }
```

### getDisplaySize20+

PhonePC/2in1TabletTVWearable

getDisplaySize(displayId: number): Promise<Point>

获取当前设备指定屏幕的大小。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 指定设备屏幕ID。取值范围：大于等于0的整数。  **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Point](js-apis-uitest.md#point9)> | Promise对象，返回Point对象，当前设备指定屏幕的大小为Point.x \* Point.y。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let size = await driver.getDisplaySize(0);
7. }
```

### getDisplayDensity9+

PhonePC/2in1TabletTVWearable

getDisplayDensity(): Promise<Point>

获取当前设备屏幕的分辨率。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Point](js-apis-uitest.md#point9)> | Promise对象，返回Point对象，当前设备屏幕的分辨率为Point.x\*Point.y。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let density = await driver.getDisplayDensity();
7. }
```

### getDisplayDensity20+

PhonePC/2in1TabletTVWearable

getDisplayDensity(displayId: number): Promise<Point>

获取当前设备指定屏幕的分辨率。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 指定设备屏幕ID。取值范围：大于等于0的整数。  **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Point](js-apis-uitest.md#point9)> | Promise对象，返回Point对象，当前设备指定屏幕的分辨率为Point.x\*Point.y。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let density = await driver.getDisplayDensity(0);
7. }
```

### wakeUpDisplay9+

PhonePC/2in1TabletTVWearable

wakeUpDisplay(): Promise<void>

唤醒当前设备即设备亮屏。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.wakeUpDisplay();
7. }
```

### pressHome9+

PhonePC/2in1TabletTVWearable

pressHome(): Promise<void>

设备注入返回桌面操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.pressHome();
7. }
```

### pressHome20+

PhonePC/2in1TabletTVWearable

pressHome(displayId: number): Promise<void>

设备指定屏幕上注入返回桌面操作。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| displayId | number | 是 | 指定设备屏幕ID。取值范围：大于等于0的整数。  **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.pressHome(0);
7. }
```

### waitForIdle9+

PhonePC/2in1TabletTVWearable

waitForIdle(idleTime: number, timeout: number): Promise<boolean>

判断当前界面的所有控件是否已经空闲。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| idleTime | number | 是 | 空闲时间的阈值。在这个时间段控件不发生变化，视为该控件空闲，单位：毫秒，取值范围：大于等于0的整数。 |
| timeout | number | 是 | 等待空闲的最大时间，单位：毫秒，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回当前界面的所有控件是否已经空闲。true：已经空闲，false：不空闲。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let idled: boolean = await driver.waitForIdle(4000, 5000);
7. }
```

### fling9+

PhonePC/2in1TabletTVWearable

fling(from: Point, to: Point, stepLen: number, speed: number): Promise<void>

模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | [Point](js-apis-uitest.md#point9) | 是 | 手指接触屏幕的起始点坐标。 |
| to | [Point](js-apis-uitest.md#point9) | 是 | 手指离开屏幕时的坐标点。 |
| stepLen | number | 是 | 间隔距离，取值大于等于0的整数，单位：px。 |
| speed | number | 是 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.fling({ x: 500, y: 480 }, { x: 450, y: 480 }, 5, 600);
7. }
```

### injectMultiPointerAction9+

PhonePC/2in1TabletTVWearable

injectMultiPointerAction(pointers: PointerMatrix, speed?: number): Promise<boolean>

向设备注入多指操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pointers | [PointerMatrix](js-apis-uitest.md#pointermatrix9) | 是 | 滑动轨迹，包括操作手指个数和滑动坐标序列。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回操作是否成功完成。true：完成，false：未完成。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, PointerMatrix } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let pointers: PointerMatrix = PointerMatrix.create(2, 5);
7. pointers.setPoint(0, 0, { x: 250, y: 480 });
8. pointers.setPoint(0, 1, { x: 250, y: 440 });
9. pointers.setPoint(0, 2, { x: 250, y: 400 });
10. pointers.setPoint(0, 3, { x: 250, y: 360 });
11. pointers.setPoint(0, 4, { x: 250, y: 320 });
12. pointers.setPoint(1, 0, { x: 250, y: 480 });
13. pointers.setPoint(1, 1, { x: 250, y: 440 });
14. pointers.setPoint(1, 2, { x: 250, y: 400 });
15. pointers.setPoint(1, 3, { x: 250, y: 360 });
16. pointers.setPoint(1, 4, { x: 250, y: 320 });
17. await driver.injectMultiPointerAction(pointers);
18. }
```

### fling10+

PhonePC/2in1TabletTVWearable

fling(direction: UiDirection, speed: number): Promise<void>

指定方向和滑动速率，模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | [UiDirection](js-apis-uitest.md#uidirection10) | 是 | 进行抛滑的方向。 |
| speed | number | 是 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiDirection } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.fling(UiDirection.DOWN, 10000);
7. }
```

### fling20+

PhonePC/2in1TabletTVWearable

fling(direction: UiDirection, speed: number, displayId: number): Promise<void>

指定方向、滑动速率和操作屏幕，模拟手指滑动后脱离屏幕的快速滑动操作。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| direction | [UiDirection](js-apis-uitest.md#uidirection10) | 是 | 进行抛滑的方向。 |
| speed | number | 是 | 滑动速率，取值范围为200-40000，默认值为600，单位：px/s。为不在范围内的非负数时设为默认值600。为负数时抛出401错误码。 |
| displayId | number | 是 | 指定设备屏幕ID。取值范围：大于等于0的整数。  **说明：** 传入displayId不存在时，将抛出17000007异常。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiDirection } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.fling(UiDirection.DOWN, 10000, 0);
7. }
```

### screenCapture10+

PhonePC/2in1TabletTVWearable

screenCapture(savePath: string, rect?: Rect): Promise<boolean>

捕获当前屏幕的指定区域，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。适用于支持截屏的场景。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| savePath | string | 是 | 文件保存路径。路径需为当前应用的[沙箱路径](../harmonyos-guides/app-sandbox-directory.md)。 |
| rect | [Rect](js-apis-uitest.md#rect9) | 否 | 截图区域，默认为全屏。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回截图操作是否成功完成。true：成功完成，false：未成功完成。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.screenCapture('/data/storage/el2/base/cache/1.png', {
7. left: 0,
8. top: 0,
9. right: 100,
10. bottom: 100
11. });
12. }
```

### mouseClick10+

PhonePC/2in1TabletTVWearable

mouseClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>

在指定坐标点注入鼠标点击动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标点击动作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | [Point](js-apis-uitest.md#point9) | 是 | 鼠标点击的坐标。 |
| btnId | [MouseButton](js-apis-uitest.md#mousebutton10) | 是 | 按下的鼠标按钮。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)，默认值为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, MouseButton } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.mouseClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
7. }
```

### mouseScroll10+

PhonePC/2in1TabletTVWearable

mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number): Promise<void>

在指定坐标点注入鼠标滚轮滑动动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标滚轮滑动动作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | [Point](js-apis-uitest.md#point9) | 是 | 鼠标点击的坐标。 |
| down | boolean | 是 | 滚轮滑动方向是否向下。true表示向下滑动。false表示向上滚动。 |
| d | number | 是 | 鼠标滚轮滚动的格数，取值大于等于0的整数，每格对应目标点位移120px。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)，默认值为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.mouseScroll({ x: 360, y: 640 }, true, 30, 2072);
7. }
```

### mouseMoveTo10+

PhonePC/2in1TabletTVWearable

mouseMoveTo(p: Point): Promise<void>

将鼠标光标移到目标点。使用Promise异步回调。

**系统能力**：SystemCapability.Test.UiTest

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | [Point](js-apis-uitest.md#point9) | 是 | 目标点的坐标。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.mouseMoveTo({ x: 100, y: 100 });
7. }
```

### createUIEventObserver10+

PhonePC/2in1TabletTVWearable

createUIEventObserver(): UIEventObserver;

创建一个UI事件监听器。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UIEventObserver](js-apis-uitest.md#uieventobserver10) | 返回找到的目标窗口对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UIEventObserver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let observer: UIEventObserver = driver.createUIEventObserver();
7. }
```

### mouseScroll11+

PhonePC/2in1TabletTVWearable

mouseScroll(p: Point, down: boolean, d: number, key1?: number, key2?: number, speed?: number): Promise<void>

在指定坐标点注入鼠标滚轮滑动动作，支持同时按下对应键盘组合键并且指定滑动速度。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | [Point](js-apis-uitest.md#point9) | 是 | 鼠标点击的坐标。 |
| down | boolean | 是 | 滚轮滑动方向是否向下。true表示向下滑动。false表示向上滚动。 |
| d | number | 是 | 鼠标滚轮滚动的格数，取值大于等于0的整数，每格对应目标点位移120px。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)，默认值为0。 |
| speed | number | 否 | 鼠标滚轮滚动的速度，范围：1-500的整数，单位：格/秒。为不在范围内的非负数或为null/undefined时设为默认值20。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.mouseScroll({ x: 360, y: 640 }, true, 30, 2072, 20);
7. }
```

### mouseDoubleClick11+

PhonePC/2in1TabletTVWearable

mouseDoubleClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>

在指定坐标点注入鼠标双击动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标双击动作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | [Point](js-apis-uitest.md#point9) | 是 | 鼠标双击的坐标。 |
| btnId | [MouseButton](js-apis-uitest.md#mousebutton10) | 是 | 按下的鼠标按钮。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)，默认值0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)，默认值0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, MouseButton } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.mouseDoubleClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
7. }
```

### mouseLongClick11+

PhonePC/2in1TabletTVWearable

mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number): Promise<void>

在指定坐标点注入鼠标长按动作，支持同时按下对应键盘组合键。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标长按动作。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | [Point](js-apis-uitest.md#point9) | 是 | 鼠标长按的坐标。 |
| btnId | [MouseButton](js-apis-uitest.md#mousebutton10) | 是 | 按下的鼠标按钮。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)，默认值为0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, MouseButton } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.mouseLongClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072);
7. }
```

### mouseLongClick20+

PhonePC/2in1TabletTVWearable

mouseLongClick(p: Point, btnId: MouseButton, key1?: number, key2?: number, duration?: number): Promise<void>

在指定坐标点注入鼠标长按动作，支持同时按下对应键盘组合键，支持指定长按时长。使用Promise异步回调。例如，Key值为2072时，按下Ctrl并进行鼠标长按动作。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | [Point](js-apis-uitest.md#point9) | 是 | 鼠标长按的坐标。 |
| btnId | [MouseButton](js-apis-uitest.md#mousebutton10) | 是 | 按下的鼠标按钮。 |
| key1 | number | 否 | 指定的第一个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)，默认值为0。 |
| key2 | number | 否 | 指定的第二个key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)，默认值为0。 |
| duration | number | 否 | 长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, MouseButton } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.mouseLongClick({ x: 248, y: 194 }, MouseButton.MOUSE_BUTTON_LEFT, 2072, 0, 2000);
7. }
```

### mouseMoveWithTrack11+

PhonePC/2in1TabletTVWearable

mouseMoveWithTrack(from: Point, to: Point, speed?: number): Promise<void>

鼠标从起始坐标点滑向终点坐标点。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | [Point](js-apis-uitest.md#point9) | 是 | 起始点坐标。 |
| to | [Point](js-apis-uitest.md#point9) | 是 | 终点坐标。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.mouseMoveWithTrack({ x: 100, y: 100 }, { x: 200, y: 200 }, 600);
7. }
```

### mouseDrag11+

PhonePC/2in1TabletTVWearable

mouseDrag(from: Point, to: Point, speed?: number): Promise<void>

鼠标按住鼠标左键从起始坐标点拖拽至终点坐标点。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | [Point](js-apis-uitest.md#point9) | 是 | 起始点坐标。 |
| to | [Point](js-apis-uitest.md#point9) | 是 | 终点坐标。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.mouseDrag({ x: 100, y: 100 }, { x: 200, y: 200 }, 600);
7. }
```

### mouseDrag20+

PhonePC/2in1TabletTVWearable

mouseDrag(from: Point, to: Point, speed?: number, duration?: number): Promise<void>

鼠标按住鼠标左键从起始坐标点拖拽至终点坐标点，支持指定拖拽速度和拖拽前长按时间。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Phone、Tablet、PC/2in1、TV设备上生效，在其他设备中调用无效果。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| from | [Point](js-apis-uitest.md#point9) | 是 | 起始点坐标。 |
| to | [Point](js-apis-uitest.md#point9) | 是 | 终点坐标。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |
| duration | number | 否 | 拖拽前长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.mouseDrag({ x: 100, y: 100 }, { x: 200, y: 200 }, 600, 2000);
7. }
```

### inputText11+

PhonePC/2in1TabletTVWearable

inputText(p: Point, text: string): Promise<void>

在指定坐标点输入文本，不清空组件内原有文本，直接在坐标处追加输入。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | [Point](js-apis-uitest.md#point9) | 是 | 输入文本的坐标点。 |
| text | string | 是 | 输入的文本信息，当前支持英文、中文和特殊字符。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let text: Component = await driver.findComponent(ON.type('TextInput'));
7. let point = await text.getBoundsCenter();
8. await driver.inputText(point, '123');
9. }
```

### inputText20+

PhonePC/2in1TabletTVWearable

inputText(p: Point, text: string, mode: InputTextMode): Promise<void>

在指定坐标点输入文本，支持指定文本输入方式。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| p | [Point](js-apis-uitest.md#point9) | 是 | 输入文本的坐标点。 |
| text | string | 是 | 输入的文本信息，当前支持英文、中文和特殊字符。 |
| mode | [InputTextMode](js-apis-uitest.md#inputtextmode20) | 是 | 输入文本的方式，取值请参考[InputTextMode](js-apis-uitest.md#inputtextmode20)。  **说明：**  InputTextMode.addition取值为true时，将光标移动至文本末尾后输入指定文本。取值为false时，将在坐标点位置输入指定文本。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not support, function can not work correctly due to limited device capabilities. |

**示例：**

```
1. // xxx.test.ets
2. import { Component, Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let text: Component = await driver.findComponent(ON.type('TextInput'));
7. let point = await text.getBoundsCenter();
8. await driver.inputText(point, '123', { paste: true, addition: false });
9. }

11. async function demo_Chinese() {
12. let driver: Driver = Driver.create();
13. let text: Component = await driver.findComponent(ON.type('TextInput'));
14. let point = await text.getBoundsCenter();
15. await driver.inputText(point, '中文&', { paste: false, addition: true });
16. // 以复制粘贴方式输入中文、特殊符号， 指定文本追加到指定坐标所在文本段的末尾。
17. }
```

### touchPadMultiFingerSwipe18+

PhonePC/2in1TabletTVWearable

touchPadMultiFingerSwipe(fingers: number, direction: UiDirection, options?: TouchPadSwipeOptions): Promise<void>

模拟触摸板多指滑动手势。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在PC/2in1设备中可正常调用，在其他设备中返回17000005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fingers | number | 是 | 触摸板多指滑动的手指数。取值为3或者4。 |
| direction | [UiDirection](js-apis-uitest.md#uidirection10) | 是 | 触摸板多指滑动的方向。 |
| options | [TouchPadSwipeOptions](js-apis-uitest.md#touchpadswipeoptions18) | 否 | 触摸板多指滑动手势附加选项，默认取TouchPadSwipeOptions中各属性的默认值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiDirection } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.touchPadMultiFingerSwipe(3, UiDirection.UP);
7. }
```

### touchPadTwoFingersScroll22+

PhonePC/2in1TabletTVWearable

touchPadTwoFingersScroll(point: Point, direction: UiDirection, d: number, speed?: number): Promise<void>

模拟触摸板双指滚动手势。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在PC/2in1设备中可正常调用，在其他设备中返回17000005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [Point](js-apis-uitest.md#point9) | 是 | 触摸板双指滚动时鼠标光标的位置。 |
| direction | [UiDirection](js-apis-uitest.md#uidirection10) | 是 | 触摸板双指滚动的方向。 |
| d | number | 是 | 触摸板双指滚动的格数，取值为大于等于0的整数，每格对应目标点位移120px。 |
| speed | number | 否 | 触摸板双指滚动的速度，范围：1-500的整数，单位：格/秒。为不在范围内的非负数或为null/undefined时设为默认值20。为负数时抛出17000007错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiDirection } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.touchPadTwoFingersScroll({ x: 100, y: 100 }, UiDirection.UP, 20, 10);
7. }
```

### penClick18+

PhonePC/2in1TabletTVWearable

penClick(point: Point): Promise<void>

模拟手写笔点击操作。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [Point](js-apis-uitest.md#point9) | 是 | 点击的坐标点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.penClick({ x: 100, y: 100 });
7. }
```

### penLongClick18+

PhonePC/2in1TabletTVWearable

penLongClick(point: Point, pressure?: number): Promise<void>

模拟手写笔长按操作。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [Point](js-apis-uitest.md#point9) | 是 | 长按的坐标点。 |
| pressure | number | 否 | 手写笔滑动操作的压力，默认为1.0，取值范围为0.0到1.0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.penLongClick({ x: 100, y: 100 }, 0.5);
7. }
```

### penDoubleClick18+

PhonePC/2in1TabletTVWearable

penDoubleClick(point: Point): Promise<void>

模拟手写笔双击操作。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| point | [Point](js-apis-uitest.md#point9) | 是 | 双击的坐标点。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.penDoubleClick({ x: 100, y: 100 });
7. }
```

### penSwipe18+

PhonePC/2in1TabletTVWearable

penSwipe(startPoint: Point, endPoint: Point, speed?: number, pressure?: number): Promise<void>

模拟手写笔的滑动操作。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startPoint | [Point](js-apis-uitest.md#point9) | 是 | 起始位置的坐标点。 |
| endPoint | [Point](js-apis-uitest.md#point9) | 是 | 结束位置的坐标点。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |
| pressure | number | 否 | 手写笔滑动操作的压力，默认为1.0，取值范围为0.0到1.0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. await driver.penSwipe({ x: 100, y: 100 }, { x: 100, y: 500 }, 600, 0.5);
7. }
```

### injectPenPointerAction18+

PhonePC/2in1TabletTVWearable

injectPenPointerAction(pointers: PointerMatrix, speed?: number, pressure?: number): Promise<void>

模拟手写笔多点连续注入操作。使用Promise异步回调。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pointers | [PointerMatrix](js-apis-uitest.md#pointermatrix9) | 是 | 滑动轨迹，包括操作手指个数和滑动坐标序列。  **说明**：当前仅支持单指操作，PointerMatrix中的操作手指个数fingers必须设置为1。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出401错误码。 |
| pressure | number | 否 | 手写笔多点连续注入的压力，默认为1.0，取值范围为0.0到1.0。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, PointerMatrix } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let pointer = PointerMatrix.create(1, 8);
7. for (let step = 0; step < 8; step++) {
8. pointer.setPoint(0, step, { x: 500, y: 1100 - 100 * step });
9. }
10. await driver.injectPenPointerAction(pointer, 600, 0.5);
11. }
```

### crownRotate20+

PhonePC/2in1TabletTVWearable

crownRotate(d: number, speed?: number): Promise<void>

注入手表表冠旋转事件，可指定旋转速度。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在Wearable设备中可正常调用，在其他设备中返回801错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| d | number | 是 | 手表表冠旋转的格数，正值表示顺时针旋转，负值表示逆时针旋转，取值需为整数。 |
| speed | number | 否 | 手表表冠旋转的速度，取值范围：1-500的整数，默认值为20，单位：格/秒。为不在范围内的非负数或为null/undefined时设为默认值20。为负数时抛出17000007错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |
| 801 | Capability not support, function can not work correctly due to limited device capabilities. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. // 顺时针旋转50格，旋转速度为30格/秒
7. await driver.crownRotate(50, 30);
8. // 逆时针旋转20格，旋转速度为30格/秒
9. await driver.crownRotate(-20, 30);
10. }
```

### knuckleKnock22+

PhonePC/2in1TabletTVWearable

knuckleKnock(pointers: Array<Point>, times: number): Promise<void>

模拟指关节敲击屏幕操作。使用Promise异步回调。

说明

若设备关闭了指关节手势，则调用本接口返回17000005错误码。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在支持指关节操作的Phone、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pointers | Array<[Point](js-apis-uitest.md#point9)> | 是 | 指关节敲击屏幕坐标点的数组，数组长度取值为1或2。 |
| times | number | 是 | 指关节连续敲击屏幕的次数，取值为1或2。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, Point } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. // 模拟指关节单指双击手势
7. let points: Array<Point> = [{ x: 100, y: 100 }];
8. await driver.knuckleKnock(points, 2);
9. }
```

### injectKnucklePointerAction22+

PhonePC/2in1TabletTVWearable

injectKnucklePointerAction(pointers: PointerMatrix, speed?: number): Promise<void>

模拟指关节多点注入滑动操作。使用Promise异步回调。

说明

若设备关闭了指关节手势，则调用本接口返回17000005错误码。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：该接口在支持指关节操作的Phone、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pointers | [PointerMatrix](js-apis-uitest.md#pointermatrix9) | 是 | 滑动轨迹，包括操作手指个数和滑动坐标序列。  **说明**：当前仅支持单指操作，PointerMatrix中的操作手指个数fingers必须设置为1。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, PointerMatrix } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. // 模拟指关节滑动在屏幕上画'S'
7. let pointers: PointerMatrix = PointerMatrix.create(1, 6);
8. pointers.setPoint(0, 0, { x: 750, y: 300 });
9. pointers.setPoint(0, 1, { x: 500, y: 100 });
10. pointers.setPoint(0, 2, { x: 250, y: 300 });
11. pointers.setPoint(0, 3, { x: 750, y: 800 });
12. pointers.setPoint(0, 4, { x: 500, y: 1000 });
13. pointers.setPoint(0, 5, { x: 250, y: 800 });
14. await driver.injectKnucklePointerAction(pointers);
15. }
```

### isComponentPresentWhenLongClick22+

PhonePC/2in1TabletTVWearable

isComponentPresentWhenLongClick(on: On, point: Point, duration?: number): Promise<boolean>

在坐标点长按，并查找目标控件是否存在。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | [On](js-apis-uitest.md#on9) | 是 | 目标控件的属性要求。 |
| point | [Point](js-apis-uitest.md#point9) | 是 | 长按的坐标点。 |
| duration | number | 否 | 长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回长按操作期间目标控件是否存在。true：存在。false：不存在。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let isExist = await driver.isComponentPresentWhenLongClick(ON.id('123'), { x: 100, y: 100 }, 2000);
7. }
```

### isComponentPresentWhenDrag22+

PhonePC/2in1TabletTVWearable

isComponentPresentWhenDrag(on: On, from: Point, to: Point, speed?: number, duration?: number): Promise<boolean>

从起始点拖拽至终止点，并查找目标控件是否存在。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | [On](js-apis-uitest.md#on9) | 是 | 目标控件的属性要求。 |
| from | [Point](js-apis-uitest.md#point9) | 是 | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | [Point](js-apis-uitest.md#point9) | 是 | 以Point对象的形式传入终止点的坐标信息和所属屏幕ID。  **说明：** 应与起始点属于同一个屏幕，否则将抛出17000007异常。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |
| duration | number | 否 | 拖拽前长按持续的时间，取值范围为大于等于1500的整数，默认值为1500，单位：ms。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回拖拽操作期间目标控件是否存在。true：存在。false：不存在。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let isExist = await driver.isComponentPresentWhenDrag(ON.id('123'), { x: 100, y: 100 }, { x: 200, y: 200 }, 1000, 2000);
7. }
```

### isComponentPresentWhenSwipe22+

PhonePC/2in1TabletTVWearable

isComponentPresentWhenSwipe(on: On, from: Point, to: Point, speed?: number): Promise<boolean>

从起始点滑向终止点，并查找目标控件是否存在。使用Promise异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| on | [On](js-apis-uitest.md#on9) | 是 | 目标控件的属性要求。 |
| from | [Point](js-apis-uitest.md#point9) | 是 | 以Point对象的形式传入起始点的坐标信息和所属屏幕ID。 |
| to | [Point](js-apis-uitest.md#point9) | 是 | 以Point对象的形式传入终止点的坐标信息和所属屏幕ID。  **说明：** 应与起始点属于同一个屏幕，否则将抛出17000007异常。 |
| speed | number | 否 | 滑动速率，取值范围为200-40000的整数，默认值为600，单位：px/s。为不在范围内的非负数或为null/undefined时设为默认值600。为负数时抛出17000007错误码。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象。返回滑动操作期间目标控件是否存在。true：存在。false：不存在。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let isExist = await driver.isComponentPresentWhenSwipe(ON.id('123'), { x: 100, y: 100 }, { x: 200, y: 200 }, 1000);
7. }
```

## PointerMatrix9+

PhonePC/2in1TabletTVWearable

存储多指操作中每根手指每一步动作的坐标点及其行为的二维数组。

### create9+

PhonePC/2in1TabletTVWearable

static create(fingers: number, steps: number): PointerMatrix

静态方法，构造一个PointerMatrix对象，并返回该对象。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| fingers | number | 是 | 多指操作中注入的手指数，取值范围：[1,10]的整数。 |
| steps | number | 是 | 每根手指操作的步骤数，取值范围：[1,1000]的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PointerMatrix](js-apis-uitest.md#pointermatrix9) | 返回构造的PointerMatrix对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { PointerMatrix } from '@kit.TestKit';

4. async function demo() {
5. let pointerMatrix: PointerMatrix = PointerMatrix.create(2, 3);
6. }
```

### setPoint9+

PhonePC/2in1TabletTVWearable

setPoint(finger: number, step: number, point: Point): void

设置PointerMatrix对象中指定手指和步骤对应动作的坐标点。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| finger | number | 是 | 手指的序号，取值大于等于0的整数，且不超过构造PointerMatrix对象时设置的手指数。 |
| step | number | 是 | 步骤的序号，取值大于等于0的整数，且不超过构造PointerMatrix对象时设置的操作的步骤数。 |
| point | [Point](js-apis-uitest.md#point9) | 是 | 该行为的坐标点。建议相邻的坐标点距离在10px至80px范围内。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { PointerMatrix } from '@kit.TestKit';

4. async function demo() {
5. let pointers: PointerMatrix = PointerMatrix.create(2, 5);
6. pointers.setPoint(0, 0, { x: 250, y: 480 });
7. pointers.setPoint(0, 1, { x: 250, y: 440 });
8. pointers.setPoint(0, 2, { x: 250, y: 400 });
9. pointers.setPoint(0, 3, { x: 250, y: 360 });
10. pointers.setPoint(0, 4, { x: 250, y: 320 });
11. pointers.setPoint(1, 0, { x: 250, y: 480 });
12. pointers.setPoint(1, 1, { x: 250, y: 440 });
13. pointers.setPoint(1, 2, { x: 250, y: 400 });
14. pointers.setPoint(1, 3, { x: 250, y: 360 });
15. pointers.setPoint(1, 4, { x: 250, y: 320 });
16. }
```

## UiWindow9+

PhonePC/2in1TabletTVWearable

UiWindow代表了UI界面上的一个窗口，提供窗口属性获取，窗口拖动、调整窗口大小等能力。

该类提供的所有方法都使用Promise方式作为异步方法，需使用await方式调用。

### getBundleName9+

PhonePC/2in1TabletTVWearable

getBundleName(): Promise<string>

获取窗口归属应用的包名信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回窗口归属应用的包名信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. let name: string = await window.getBundleName();
8. }
```

### getBounds9+

PhonePC/2in1TabletTVWearable

getBounds(): Promise<Rect>

获取窗口的边框信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[Rect](js-apis-uitest.md#rect9)> | Promise对象，返回窗口的边框信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. let rect = await window.getBounds();
8. }
```

### getTitle9+

PhonePC/2in1TabletTVWearable

getTitle(): Promise<string>

获取窗口的标题信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回窗口的标题信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. let title = await window.getTitle();
8. }
```

### getWindowMode9+

PhonePC/2in1TabletTVWearable

getWindowMode(): Promise<WindowMode>

获取窗口的窗口模式信息。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[WindowMode](js-apis-uitest.md#windowmode9)> | Promise对象，返回窗口的窗口模式信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. let mode = await window.getWindowMode();
8. }
```

### isFocused9+

PhonePC/2in1TabletTVWearable

isFocused(): Promise<boolean>

判断窗口是否处于获焦状态。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回窗口对象是否获取获焦状态。true：获焦。false：未获焦。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. let focused = await window.isFocused();
8. }
```

### isActived(deprecated)

PhonePC/2in1TabletTVWearable

isActived(): Promise<boolean>

判断窗口是否为用户正在交互窗口。使用Promise异步回调。

说明

从API version 9开始支持，从API version 11开始废弃，建议使用[isActive11+](js-apis-uitest.md#isactive11)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回窗口对象是否为用户正在交互窗口。true表示是交互窗口。false表示非交互窗口。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. let focused = await window.isActived();
8. }
```

### focus9+

PhonePC/2in1TabletTVWearable

focus(): Promise<void>

让窗口获焦。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. await window.focus();
8. }
```

### moveTo9+

PhonePC/2in1TabletTVWearable

moveTo(x: number, y: number): Promise<void>

将窗口移动到目标点。使用Promise异步回调。适用于支持移动的窗口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. await window.moveTo(100, 100);
8. }
```

### resize9+

PhonePC/2in1TabletTVWearable

resize(wide: number, height: number, direction: ResizeDirection): Promise<void>

根据传入的宽、高和调整方向来调整窗口的大小。使用Promise异步回调。适用于支持调整大小的窗口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| wide | number | 是 | 以number的形式传入调整后窗口的宽度，取值范围：大于等于0的整数。 |
| height | number | 是 | 以number的形式传入调整后窗口的高度，取值范围：大于等于0的整数。 |
| direction | [ResizeDirection](js-apis-uitest.md#resizedirection9) | 是 | 以[ResizeDirection](js-apis-uitest.md#resizedirection9)的形式传入窗口调整的方向。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, ResizeDirection, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. await window.resize(100, 100, ResizeDirection.LEFT);
8. }
```

### split9+

PhonePC/2in1TabletTVWearable

split(): Promise<void>

将窗口模式切换成分屏模式。使用Promise异步回调。适用于支持切换分屏模式的窗口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. await window.split();
8. }
```

### maximize9+

PhonePC/2in1TabletTVWearable

maximize(): Promise<void>

将窗口最大化。使用Promise异步回调。适用于支持窗口最大化操作的窗口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. await window.maximize();
8. }
```

### minimize9+

PhonePC/2in1TabletTVWearable

minimize(): Promise<void>

将窗口最小化。使用Promise异步回调。适用于支持窗口最小化操作的窗口。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，返回无结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. await window.minimize();
8. }
```

### resume9+

PhonePC/2in1TabletTVWearable

resume(): Promise<void>

将窗口恢复到之前的窗口模式。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. await window.resume();
8. }
```

### close9+

PhonePC/2in1TabletTVWearable

close(): Promise<void>

将窗口关闭。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**设备行为差异**：对于API version 22及之前的版本，该接口在PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。从API version 23开始，该接口在Phone、PC/2in1、Tablet设备中可正常调用，在其他设备中返回17000005错误码。

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |
| 17000005 | This operation is not supported. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ actived: true });
7. await window.close();
8. }
```

### isActive11+

PhonePC/2in1TabletTVWearable

isActive(): Promise<boolean>

判断窗口是否为用户正在交互窗口。使用Promise异步回调。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回窗口对象是否为用户正在交互窗口。true：交互窗口。false：非交互窗口。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiWindow } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ active: true });
7. let focused = await window.isActive();
8. }
```

### getDisplayId20+

PhonePC/2in1TabletTVWearable

getDisplayId(): Promise<number>

获取窗口所属的屏幕ID。使用Promise异步回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回窗口所属的屏幕ID。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000002 | The async function is not called with await. |
| 17000004 | The window or component is invisible or destroyed. |

**示例：**

```
1. // xxx.test.ets
2. import { UiWindow, Driver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let window: UiWindow = await driver.findWindow({ active: true });
7. let id = await window.getDisplayId();
8. }
```

## UIEventObserver10+

PhonePC/2in1TabletTVWearable

UI事件监听器。

### once('toastShow')10+

PhonePC/2in1TabletTVWearable

once(type: 'toastShow', callback: Callback<UIElementInfo>): void

开始监听toast控件出现的事件，使用callback的形式返回结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型，取值为'toastShow'。 |
| callback | Callback<[UIElementInfo](js-apis-uitest.md#uielementinfo10)> | 是 | 事件发生时执行的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UIElementInfo, UIEventObserver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let observer: UIEventObserver = driver.createUIEventObserver();
7. let callback = (UIElementInfo: UIElementInfo) => {
8. console.info(UIElementInfo.bundleName);
9. console.info(UIElementInfo.text);
10. console.info(UIElementInfo.type);
11. }
12. observer.once('toastShow', callback);
13. }
```

### once('dialogShow')10+

PhonePC/2in1TabletTVWearable

once(type: 'dialogShow', callback: Callback<UIElementInfo>): void

开始监听dialog控件出现的事件，使用callback的形式返回结果。

**元服务API：** 从API version 11开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型，取值为'dialogShow'。 |
| callback | Callback<[UIElementInfo](js-apis-uitest.md#uielementinfo10)> | 是 | 事件发生时执行的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UIElementInfo, UIEventObserver } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let observer: UIEventObserver = driver.createUIEventObserver();
7. let callback = (UIElementInfo: UIElementInfo) => {
8. console.info(UIElementInfo.bundleName);
9. console.info(UIElementInfo.text);
10. console.info(UIElementInfo.type);
11. }
12. observer.once('dialogShow', callback);
13. }
```

### once('windowChange')22+

PhonePC/2in1TabletTVWearable

once(type: 'windowChange', windowChangeType: WindowChangeType, options: WindowChangeOptions, callback: Callback<UIElementInfo>): void

开始监听指定类型的窗口变化事件，支持设置事件监听的扩展配置，监听到指定窗口变化事件时触发callback回调。仅支持[自由多窗模式](../harmonyos-guides/window-terminology.md#自由多窗模式)的窗口监听。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型，支持的事件为'windowChange'。当监听到窗口变化时，触发该事件。 |
| windowChangeType | [WindowChangeType](js-apis-uitest.md#windowchangetype22) | 是 | 窗口变化事件类型。 |
| options | [WindowChangeOptions](js-apis-uitest.md#windowchangeoptions22) | 是 | 窗口变化事件监听的扩展配置，包括监听超时时间和监听窗口对应包名。 |
| callback | Callback<[UIElementInfo](js-apis-uitest.md#uielementinfo10)> | 是 | 事件发生时执行的回调函数，返回事件的相关信息。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UIElementInfo, UIEventObserver, WindowChangeOptions, WindowChangeType } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let observer: UIEventObserver = driver.createUIEventObserver();
7. let options: WindowChangeOptions = {
8. timeout: 20000,
9. bundleName: 'com.example.myapplication'  // 请开发者替换为实际包名
10. }
11. let callback = (UIElementInfo: UIElementInfo) => {
12. console.info(UIElementInfo.bundleName);
13. console.info(UIElementInfo.text);
14. console.info(UIElementInfo.type);
15. console.info(UIElementInfo.windowChangeType?.toString());
16. console.info(UIElementInfo.windowId?.toString());
17. }
18. observer.once('windowChange', WindowChangeType.WINDOW_ADDED, options, callback);
19. }
```

### once('componentEventOccur')22+

PhonePC/2in1TabletTVWearable

once(type: 'componentEventOccur', componentEventType: ComponentEventType, options: ComponentEventOptions, callback: Callback<UIElementInfo>): void

开始监听指定类型的控件操作事件，支持设置事件监听的扩展配置，监听到指定控件操作事件时触发callback回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 订阅的事件类型，支持的事件为'componentEventOccur'。当监听到控件操作时，触发该事件。 |
| componentEventType | [ComponentEventType](js-apis-uitest.md#componenteventtype22) | 是 | 控件操作事件类型。 |
| options | [ComponentEventOptions](js-apis-uitest.md#componenteventoptions22) | 是 | 控件操作事件监听的扩展配置，包括监听超时时间和监听控件匹配条件。 |
| callback | Callback<[UIElementInfo](js-apis-uitest.md#uielementinfo10)> | 是 | 事件发生时执行的回调函数。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 17000005 | This operation is not supported. |
| 17000007 | Parameter verification failed. |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UIElementInfo, UIEventObserver, ComponentEventOptions, ComponentEventType, ON } from '@kit.TestKit';

4. async function demo() {
5. let driver: Driver = Driver.create();
6. let observer: UIEventObserver = driver.createUIEventObserver();
7. let option: ComponentEventOptions = {
8. timeout: 20000,
9. on: ON.id('123')  // 请开发者替换为实际存在的控件id值
10. };
11. let callback = (UIElementInfo: UIElementInfo) => {
12. console.info(UIElementInfo.bundleName);
13. console.info(UIElementInfo.text);
14. console.info(UIElementInfo.type);
15. console.info(UIElementInfo.componentEventType?.toString());
16. console.info(UIElementInfo.windowId?.toString());
17. console.info(UIElementInfo.componentId);
18. console.info(UIElementInfo.componentRect?.left.toString());
19. console.info(UIElementInfo.componentRect?.left.toString());
20. console.info(UIElementInfo.componentRect?.left.toString());
21. console.info(UIElementInfo.componentRect?.left.toString());
22. };
23. observer.once('componentEventOccur', ComponentEventType.COMPONENT_CLICKED, option, callback);
24. }
```

## By(deprecated)

PhonePC/2in1TabletTVWearable

UiTest框架通过By类提供了丰富的控件特征描述API，用于进行控件筛选来匹配/查找出目标控件。

By提供的API能力具有以下几个特点:

1、支持单属性匹配和多属性组合匹配，例如同时指定目标控件text和id。

2、控件属性支持多种匹配模式。

3、支持控件绝对定位，相对定位，可通过[By.isBefore(deprecated)](js-apis-uitest.md#isbeforedeprecated)和[By.isAfter(deprecated)](js-apis-uitest.md#isafterdeprecated)等API限定邻近控件特征进行辅助定位。

By类提供的所有API均为同步接口，建议使用者通过静态构造器BY来链式创建By对象。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[On9+](js-apis-uitest.md#on9)替代。

```
1. // xxx.test.ets
2. import { BY } from '@kit.TestKit';

4. BY.text('123').type('Button');
```

### text(deprecated)

PhonePC/2in1TabletTVWearable

text(txt: string, pattern?: MatchPattern): By

指定目标控件文本属性，支持多种匹配模式，返回By对象自身。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[text9+](js-apis-uitest.md#text9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| txt | string | 是 | 指定控件文本，用于匹配目标控件文本。 |
| pattern | [MatchPattern](js-apis-uitest.md#matchpattern) | 否 | 指定的文本匹配模式，默认为[EQUALS](js-apis-uitest.md#matchpattern)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [By](js-apis-uitest.md#bydeprecated) | 返回指定目标控件文本属性的By对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { BY, By } from '@kit.TestKit';

4. let by: By = BY.text('123'); // 使用静态构造器BY创建by对象，指定目标控件的text属性。
```

### key(deprecated)

PhonePC/2in1TabletTVWearable

key(key: string): By

指定目标控件key值属性，返回By对象自身。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[id9+](js-apis-uitest.md#id9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| key | string | 是 | 指定控件的Key值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [By](js-apis-uitest.md#bydeprecated) | 返回指定目标控件key值属性的By对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { By, BY } from '@kit.TestKit';

4. let by: By = BY.key('123'); // 使用静态构造器BY创建by对象，指定目标控件的key值属性。
```

### id(deprecated)

PhonePC/2in1TabletTVWearable

id(id: number): By

指定目标控件id属性，返回By对象自身。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[id9+](js-apis-uitest.md#id9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| id | number | 是 | 指定控件的id值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [By](js-apis-uitest.md#bydeprecated) | 返回指定目标控件id属性的By对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { By, BY } from '@kit.TestKit';

4. let by: By = BY.id(123); // 使用静态构造器BY创建by对象，指定目标控件的id属性。
```

### type(deprecated)

PhonePC/2in1TabletTVWearable

type(tp: string): By

指定目标控件的控件类型属性，返回By对象自身。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[type9+](js-apis-uitest.md#type9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| tp | string | 是 | 指定控件类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [By](js-apis-uitest.md#bydeprecated) | 返回指定目标控件的控件类型属性的By对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { By, BY } from '@kit.TestKit';

4. let by: By = BY.type('Button'); // 使用静态构造器BY创建by对象，指定目标控件的控件类型属性。
```

### clickable(deprecated)

PhonePC/2in1TabletTVWearable

clickable(b?: boolean): By

指定目标控件的可点击状态属性，返回By对象自身。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[clickable9+](js-apis-uitest.md#clickable9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件可点击状态。true：可点击。false：不可点击。默认为true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [By](js-apis-uitest.md#bydeprecated) | 返回指定目标控件的可点击状态属性的By对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { By, BY } from '@kit.TestKit';

4. let by: By = BY.clickable(true); // 使用静态构造器BY创建by对象，指定目标控件的可点击状态属性。
```

### scrollable(deprecated)

PhonePC/2in1TabletTVWearable

scrollable(b?: boolean): By

指定目标控件的可滑动状态属性，返回By对象自身。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[scrollable9+](js-apis-uitest.md#scrollable9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 控件可滑动状态。true：可滑动。false：不可滑动。默认为true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [By](js-apis-uitest.md#bydeprecated) | 返回指定目标控件的可滑动状态属性的By对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { By, BY } from '@kit.TestKit';

4. let by: By = BY.scrollable(true); // 使用静态构造器BY创建by对象，指定目标控件的可滑动状态属性。
```

### enabled(deprecated)

PhonePC/2in1TabletTVWearable

enabled(b?: boolean): By

指定目标控件的使能状态属性，返回By对象自身。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[enabled9+](js-apis-uitest.md#enabled9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件使能状态。true：使能。false：未使能。默认为true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [By](js-apis-uitest.md#bydeprecated) | 返回指定目标控件的使能状态属性的By对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { By, BY } from '@kit.TestKit';

4. let by: By = BY.enabled(true); // 使用静态构造器BY创建by对象，指定目标控件的使能状态属性。
```

### focused(deprecated)

PhonePC/2in1TabletTVWearable

focused(b?: boolean): By

指定目标控件的获焦状态属性，返回By对象自身。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[focused9+](js-apis-uitest.md#focused9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 控件获焦状态。true：获焦。false：未获焦。默认为true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [By](js-apis-uitest.md#bydeprecated) | 返回指定目标控件的获焦状态属性的By对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { By, BY } from '@kit.TestKit';

4. let by: By = BY.focused(true); // 使用静态构造器BY创建by对象，指定目标控件的获焦状态属性。
```

### selected(deprecated)

PhonePC/2in1TabletTVWearable

selected(b?: boolean): By

指定目标控件的被选中状态属性，返回By对象自身。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[selected9+](js-apis-uitest.md#selected9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| b | boolean | 否 | 指定控件被选中状态。true：被选中。false：未被选中。默认为true。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [By](js-apis-uitest.md#bydeprecated) | 返回指定目标控件的被选中状态属性的By对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { By, BY } from '@kit.TestKit';

4. let by: By = BY.selected(true); // 使用静态构造器BY创建by对象，指定目标控件的被选中状态属性。
```

### isBefore(deprecated)

PhonePC/2in1TabletTVWearable

isBefore(by: By): By

指定目标控件位于给出的特征属性控件之前，返回By对象自身。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[isBefore9+](js-apis-uitest.md#isbefore9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| by | [By](js-apis-uitest.md#bydeprecated) | 是 | 特征控件的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [By](js-apis-uitest.md#bydeprecated) | 返回指定目标控件位于给出的特征属性控件之前的By对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { By, BY } from '@kit.TestKit';

4. // 使用静态构造器BY创建by对象，指定目标控件位于给出的特征属性控件之前。
5. let by: By = BY.type('Button').isBefore(BY.text('123')); // 查找text为123之前的第一个Button组件
```

### isAfter(deprecated)

PhonePC/2in1TabletTVWearable

isAfter(by: By): By

指定目标控件位于给出的特征属性控件之后，返回By对象自身。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[isAfter9+](js-apis-uitest.md#isafter9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| by | [By](js-apis-uitest.md#bydeprecated) | 是 | 特征控件的属性。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [By](js-apis-uitest.md#bydeprecated) | 返回指定目标控件位于给出的特征属性控件之后的By对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { By, BY } from '@kit.TestKit';

4. // 使用静态构造器BY创建by对象，指定目标控件位于给出的特征属性控件之后。
5. let by: By = BY.type('Text').isAfter(BY.text('123')); // 查找 text为123之后的第一个Text组件
```

## UiComponent(deprecated)

PhonePC/2in1TabletTVWearable

UiTest中，UiComponent类代表了UI界面上的一个控件，提供控件属性获取，控件点击，滑动查找，文本注入等API。

该类提供的所有方法都使用Promise方式作为异步方法，需使用await调用。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[Component9+](js-apis-uitest.md#component9)替代。

### click(deprecated)

PhonePC/2in1TabletTVWearable

click(): Promise<void>

控件对象进行点击操作。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[click9+](js-apis-uitest.md#click9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, Driver, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let button: UiComponent = await driver.findComponent(BY.type('Button'));
7. await button.click();
8. }
```

### doubleClick(deprecated)

PhonePC/2in1TabletTVWearable

doubleClick(): Promise<void>

控件对象进行双击操作。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[doubleClick9+](js-apis-uitest.md#doubleclick9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let button: UiComponent = await driver.findComponent(BY.type('Button'));
7. await button.doubleClick();
8. }
```

### longClick(deprecated)

PhonePC/2in1TabletTVWearable

longClick(): Promise<void>

控件对象进行长按操作。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[longClick9+](js-apis-uitest.md#longclick9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let button: UiComponent = await driver.findComponent(BY.type('Button'));
7. await button.longClick();
8. }
```

### getId(deprecated)

PhonePC/2in1TabletTVWearable

getId(): Promise<number>

获取控件对象的id值。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getId9+](js-apis-uitest.md#getid9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<number> | Promise对象，返回控件的id值。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let button: UiComponent = await driver.findComponent(BY.type('Button'));
7. let id = await button.getId();
8. }
```

### getKey(deprecated)

PhonePC/2in1TabletTVWearable

getKey(): Promise<string>

获取控件对象的key值。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getId9+](js-apis-uitest.md#getid9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的key值。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let button: UiComponent = await driver.findComponent(BY.type('Button'));
7. let str_key = await button.getKey();
8. }
```

### getText(deprecated)

PhonePC/2in1TabletTVWearable

getText(): Promise<string>

获取控件对象的文本信息。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getText9+](js-apis-uitest.md#gettext9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的文本信息。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let button: UiComponent = await driver.findComponent(BY.type('Button'));
7. let text = await button.getText();
8. }
```

### getType(deprecated)

PhonePC/2in1TabletTVWearable

getType(): Promise<string>

获取控件对象的控件类型。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[getType9+](js-apis-uitest.md#gettype9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<string> | Promise对象，返回控件的类型。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let button: UiComponent = await driver.findComponent(BY.type('Button'));
7. let type = await button.getType();
8. }
```

### isClickable(deprecated)

PhonePC/2in1TabletTVWearable

isClickable(): Promise<boolean>

获取控件对象可点击状态。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[isClickable9+](js-apis-uitest.md#isclickable9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象可点击状态。true：可点击。false：不可点击。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let button: UiComponent = await driver.findComponent(BY.type('Button'));
7. if (await button.isClickable()) {
8. console.info('This button can be Clicked');
9. } else {
10. console.info('This button can not be Clicked');
11. }
12. }
```

### isScrollable(deprecated)

PhonePC/2in1TabletTVWearable

isScrollable(): Promise<boolean>

获取控件对象可滑动状态。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[isScrollable9+](js-apis-uitest.md#isscrollable9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象可滑动状态。true：可滑动。false：不可滑动。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let scrollBar: UiComponent = await driver.findComponent(BY.scrollable(true));
7. if (await scrollBar.isScrollable()) {
8. console.info('This scrollBar can be operated');
9. } else {
10. console.info('This scrollBar can not be operated');
11. }
12. }
```

### isEnabled(deprecated)

PhonePC/2in1TabletTVWearable

isEnabled(): Promise<boolean>

获取控件使能状态。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[isEnabled9+](js-apis-uitest.md#isenabled9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件使能状态。true：使能。false：未使能。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let button: UiComponent = await driver.findComponent(BY.type('Button'));
7. if (await button.isEnabled()) {
8. console.info('This button can be operated');
9. } else {
10. console.info('This button can not be operated');
11. }
12. }
```

### isFocused(deprecated)

PhonePC/2in1TabletTVWearable

isFocused(): Promise<boolean>

判断控件对象是否获焦。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[isFocused9+](js-apis-uitest.md#isfocused9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象是否获焦。true：获焦。false：未获焦。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let button: UiComponent = await driver.findComponent(BY.type('Button'));
7. if (await button.isFocused()) {
8. console.info('This button is focused');
9. } else {
10. console.info('This button is not focused');
11. }
12. }
```

### isSelected(deprecated)

PhonePC/2in1TabletTVWearable

isSelected(): Promise<boolean>

获取控件对象被选中状态。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[isSelected9+](js-apis-uitest.md#isselected9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回控件对象被选中的状态。true：被选中。false：未被选中。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let button: UiComponent = await driver.findComponent(BY.type('Button'));
7. if (await button.isSelected()) {
8. console.info('This button is selected');
9. } else {
10. console.info('This button is not selected');
11. }
12. }
```

### inputText(deprecated)

PhonePC/2in1TabletTVWearable

inputText(text: string): Promise<void>

向控件中输入文本，仅针对可编辑的文本组件生效。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[inputText9+](js-apis-uitest.md#inputtext9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| text | string | 是 | 输入的文本信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let text: UiComponent = await driver.findComponent(BY.text('hello world'));
7. await text.inputText('123');
8. }
```

### scrollSearch(deprecated)

PhonePC/2in1TabletTVWearable

scrollSearch(by: By): Promise<UiComponent>

在控件上滑动查找目标控件（适用于List等支持滑动的控件）。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[scrollSearch9+](js-apis-uitest.md#scrollsearch9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| by | [By](js-apis-uitest.md#bydeprecated) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[UiComponent](js-apis-uitest.md#uicomponentdeprecated)> | Promise对象，返回目标控件对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let scrollBar: UiComponent = await driver.findComponent(BY.type('Scroll'));
7. let button = await scrollBar.scrollSearch(BY.text('next page'));
8. }
```

## UiDriver(deprecated)

PhonePC/2in1TabletTVWearable

UiDriver类为uitest测试框架的总入口，提供控件匹配/查找，按键注入，坐标点击/滑动，截图等API。

该类提供的方法除UiDriver.create()以外的所有方法都使用Promise方式作为异步方法，需使用await调用。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[Driver9+](js-apis-uitest.md#driver9)替代。

### create(deprecated)

PhonePC/2in1TabletTVWearable

static create(): UiDriver

静态方法，构造一个UiDriver对象，并返回该对象。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[create9+](js-apis-uitest.md#create9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| UiDriver | 返回构造的UiDriver对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. }
```

### delayMs(deprecated)

PhonePC/2in1TabletTVWearable

delayMs(duration: number): Promise<void>

UiDriver对象在给定的时间内延时。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[delayMs9+](js-apis-uitest.md#delayms9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| duration | number | 是 | 给定的时间。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. await driver.delayMs(1000);
7. }
```

### findComponent(deprecated)

PhonePC/2in1TabletTVWearable

findComponent(by: By): Promise<UiComponent>

在UiDriver对象中，根据给出的目标控件属性要求查找目标控件。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[findComponent9+](js-apis-uitest.md#findcomponent9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| by | [By](js-apis-uitest.md#bydeprecated) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<[UiComponent](js-apis-uitest.md#uicomponentdeprecated)> | Promise对象，返回控件对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let button: UiComponent = await driver.findComponent(BY.text('next page'));
7. }
```

### findComponents(deprecated)

PhonePC/2in1TabletTVWearable

findComponents(by: By): Promise<Array<UiComponent>>

在UiDriver对象中，根据给出的目标控件属性要求查找出所有匹配控件，以列表保存。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[findComponents9+](js-apis-uitest.md#findcomponents9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| by | [By](js-apis-uitest.md#bydeprecated) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<Array<[UiComponent](js-apis-uitest.md#uicomponentdeprecated)>> | Promise对象，返回控件对象的列表。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY, UiComponent } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. let buttonList: Array<UiComponent> = await driver.findComponents(BY.text('next page'));
7. }
```

### assertComponentExist(deprecated)

PhonePC/2in1TabletTVWearable

assertComponentExist(by: By): Promise<void>

断言API，用于断言当前界面存在满足给出的目标控件属性的控件; 如果控件不存在，该API将抛出JS异常，使当前测试用例失败。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[assertComponentExist9+](js-apis-uitest.md#assertcomponentexist9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| by | [By](js-apis-uitest.md#bydeprecated) | 是 | 目标控件的属性要求。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**错误码：**

以下错误码的详细介绍请参见[uitest错误码](errorcode-uitest.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | if the input parameters are invalid. |
| 17000002 | if the async function was not called with await. |
| 17000003 | if the assertion failed. |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver, BY } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. await driver.assertComponentExist(BY.text('next page'));
7. }
```

### pressBack(deprecated)

PhonePC/2in1TabletTVWearable

pressBack(): Promise<void>

UiDriver对象进行点击BACK键的操作。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[pressBack9+](js-apis-uitest.md#pressback9)替代。

**系统能力**：SystemCapability.Test.UiTest

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. await driver.pressBack();
7. }
```

### triggerKey(deprecated)

PhonePC/2in1TabletTVWearable

triggerKey(keyCode: number): Promise<void>

UiDriver对象采取如下操作：通过key值找到对应键并点击。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[triggerKey9+](js-apis-uitest.md#triggerkey9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyCode | number | 是 | 指定的key值，取值大于等于0的整数，取值范围：[KeyCode键码值](js-apis-keycode.md#keycode)。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { Driver, UiDriver } from '@kit.TestKit';
3. import { KeyCode } from '@kit.InputKit';

5. async function demo() {
6. let driver: UiDriver = UiDriver.create();
7. await driver.triggerKey(KeyCode.KEYCODE_BACK); // 返回键
8. }
```

### click(deprecated)

PhonePC/2in1TabletTVWearable

click(x: number, y: number): Promise<void>

UiDriver对象采取如下操作：在目标坐标点单击。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[click9+](js-apis-uitest.md#click9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. await driver.click(100, 100);
7. }
```

### doubleClick(deprecated)

PhonePC/2in1TabletTVWearable

doubleClick(x: number, y: number): Promise<void>

UiDriver对象采取如下操作：在目标坐标点双击。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[doubleClick9+](js-apis-uitest.md#doubleclick9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. await driver.doubleClick(100, 100);
7. }
```

### longClick(deprecated)

PhonePC/2in1TabletTVWearable

longClick(x: number, y: number): Promise<void>

UiDriver对象采取如下操作：在目标坐标点长按下鼠标左键。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[longClick9+](js-apis-uitest.md#longclick9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| x | number | 是 | 以number的形式传入目标点的横坐标信息，取值范围：大于等于0的整数。 |
| y | number | 是 | 以number的形式传入目标点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. await driver.longClick(100, 100);
7. }
```

### swipe(deprecated)

PhonePC/2in1TabletTVWearable

swipe(startx: number, starty: number, endx: number, endy: number): Promise<void>

UiDriver对象采取如下操作：从给出的起始坐标点滑向给出的目的坐标点。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[swipe9+](js-apis-uitest.md#swipe9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| startx | number | 是 | 以number的形式传入起始点的横坐标信息，取值范围：大于等于0的整数。 |
| starty | number | 是 | 以number的形式传入起始点的纵坐标信息，取值范围：大于等于0的整数。 |
| endx | number | 是 | 以number的形式传入目的点的横坐标信息，取值范围：大于等于0的整数。 |
| endy | number | 是 | 以number的形式传入目的点的纵坐标信息，取值范围：大于等于0的整数。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象。无返回结果的Promise对象。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. await driver.swipe(100, 100, 200, 200);
7. }
```

### screenCap(deprecated)

PhonePC/2in1TabletTVWearable

screenCap(savePath: string): Promise<boolean>

UiDriver对象采取如下操作：捕获当前屏幕，并保存为PNG格式的图片至给出的保存路径中。使用Promise异步回调。

说明

从API version 8开始支持，从API version 9开始废弃，建议使用[screenCap9+](js-apis-uitest.md#screencap9)替代。

**系统能力**：SystemCapability.Test.UiTest

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| savePath | string | 是 | 文件保存路径。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回截图操作是否成功完成。true：成功完成，false：未成功完成。 |

**示例：**

```
1. // xxx.test.ets
2. import { UiDriver } from '@kit.TestKit';

4. async function demo() {
5. let driver: UiDriver = UiDriver.create();
6. await driver.screenCap('/data/storage/el2/base/cache/1.png');
7. }
```
