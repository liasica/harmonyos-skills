---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-application-accessibilityextensionability
title: @ohos.application.AccessibilityExtensionAbility (辅助功能扩展能力)
breadcrumb: API参考 > 应用框架 > Accessibility Kit（无障碍服务） > ArkTS API > @ohos.application.AccessibilityExtensionAbility (辅助功能扩展能力)
category: harmonyos-references
scraped_at: 2026-04-28T07:59:06+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:cf41ef480ee562400674201cec1f48059e140154a99c6c8f8414070273a50989
---

AccessibilityExtensionAbility基于ExtensionAbility框架，提供辅助功能业务的能力。

说明

* 本模块首批接口从API version 9开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';
```

## AccessibilityExtensionAbility

PhonePC/2in1TabletWearable

AccessibilityExtensionAbility基于ExtensionAbility框架，提供辅助功能业务的能力。

### 属性

PhonePC/2in1TabletWearable

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [AccessibilityExtensionContext](is-inner-application-accessibilityextensioncontext.md) | 否 | 否 | 表示辅助扩展能力上下文。 |

## AccessibilityEvent

PhonePC/2in1TabletWearable

辅助事件信息。

### 属性

PhonePC/2in1TabletWearable

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| eventType | [accessibility.EventType](js-apis-accessibility.md#eventtype) | [accessibility.WindowUpdateType](js-apis-accessibility.md#windowupdatetype) | [TouchGuideType](js-apis-application-accessibilityextensionability.md#touchguidetype) | [GestureType](js-apis-application-accessibilityextensionability.md#gesturetype) | [PageUpdateType](js-apis-application-accessibilityextensionability.md#pageupdatetype) | 否 | 否 | 具体事件类型。  EventType：无障碍事件类型；  WindowUpdateType：窗口变化类型；  TouchGuideType：触摸浏览事件类型；  GestureType：手势事件类型；  PageUpdateType：页面刷新类型。 |
| target | [AccessibilityElement](is-inner-application-accessibilityextensioncontext.md#accessibilityelement) | 否 | 是 | 发生事件的目标组件。 |
| timeStamp | number | 否 | 是 | 事件时间戳，单位是毫秒。默认值为0。 |
| elementId12+ | number | 否 | 是 | 主动聚焦的组件ID。默认值为0。 |
| textAnnouncedForAccessibility12+ | string | 否 | 是 | 主动播报的内容。当应用需要主动播报时根据实际场景设置播报内容，无特殊限制。 |
| extraInfo20+ | string | 否 | 是 | 针对TextArea、TextInput、SearchField、RichEdit组件，当文本内容有新增或删除时，携带的文本内容。根据实际场景设置，无特殊限制。 |

## AccessibilityElement10+

PhonePC/2in1TabletWearable

type AccessibilityElement = \_AccessibilityElement

表示无障碍节点元素，请参考[AccessibilityElement](is-inner-application-accessibilityextensioncontext.md#accessibilityelement)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| \_AccessibilityElement | 表示无障碍节点元素，请参考[AccessibilityElement](is-inner-application-accessibilityextensioncontext.md#accessibilityelement)。 |

**示例：**

```
1. import { AccessibilityElement } from '@kit.AccessibilityKit';

3. let accessibilityElement: AccessibilityElement;
```

## ElementAttributeValues10+

PhonePC/2in1TabletWearable

type ElementAttributeValues = \_ElementAttributeValues

表示节点元素具备的属性名称及属性值类型信息，请参考[ElementAttributeValues](is-inner-application-accessibilityextensioncontext.md#elementattributevalues)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| \_ElementAttributeValues | 表示节点元素具备的属性名称及属性值类型信息，请参考[ElementAttributeValues](is-inner-application-accessibilityextensioncontext.md#elementattributevalues)。 |

**示例：**

```
1. import { ElementAttributeValues } from '@kit.AccessibilityKit';

3. let elementAttributeValues: ElementAttributeValues;
```

## FocusDirection10+

PhonePC/2in1TabletWearable

type FocusDirection = \_FocusDirection

表示查询下一焦点元素的方向，请参考[FocusDirection](is-inner-application-accessibilityextensioncontext.md#focusdirection)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| \_FocusDirection | 表示查询下一焦点元素的方向，请参考[FocusDirection](is-inner-application-accessibilityextensioncontext.md#focusdirection)。 |

**示例：**

```
1. import { FocusDirection } from '@kit.AccessibilityKit';

3. let focusDirection: FocusDirection;
```

## ElementAttributeKeys10+

PhonePC/2in1TabletWearable

type ElementAttributeKeys = keyof ElementAttributeValues

表示[ElementAttributeValues](is-inner-application-accessibilityextensioncontext.md#elementattributevalues)的属性名称。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| keyof [ElementAttributeValues](is-inner-application-accessibilityextensioncontext.md#elementattributevalues) | 表示[ElementAttributeValues](is-inner-application-accessibilityextensioncontext.md#elementattributevalues)中所有属性名组成的联合类型。 |

**示例：**

```
1. import { ElementAttributeKeys } from '@kit.AccessibilityKit';

3. let elementAttributeKeys: ElementAttributeKeys;
```

## FocusType10+

PhonePC/2in1TabletWearable

type FocusType = \_FocusType

表示查询焦点元素的类型，请参考[FocusType](is-inner-application-accessibilityextensioncontext.md#focustype)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| \_FocusType | 表示查询焦点元素的类型，请参考[FocusType](is-inner-application-accessibilityextensioncontext.md#focustype)。 |

**示例：**

```
1. import { FocusType } from '@kit.AccessibilityKit';

3. let focusType: FocusType;
```

## WindowType 10+

PhonePC/2in1TabletWearable

type WindowType = \_WindowType

表示窗口的类型，请参考[WindowType](is-inner-application-accessibilityextensioncontext.md#windowtype)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| \_WindowType | 表示窗口的类型，请参考[WindowType](is-inner-application-accessibilityextensioncontext.md#windowtype)。 |

**示例：**

```
1. import { WindowType } from '@kit.AccessibilityKit';

3. let windowType: WindowType;
```

## Rect10+

PhonePC/2in1TabletWearable

type Rect = \_Rect

表示矩形区域，请参考[Rect](is-inner-application-accessibilityextensioncontext.md#rect)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| \_Rect | 表示矩形区域，请参考[Rect](is-inner-application-accessibilityextensioncontext.md#rect)。 |

**示例：**

```
1. import { Rect } from '@kit.AccessibilityKit';

3. let rect: Rect;
```

## AccessibilityExtensionContext10+

PhonePC/2in1TabletWearable

type AccessibilityExtensionContext = \_AccessibilityExtensionContext.default

表示辅助功能扩展的上下文环境，请参考[AccessibilityExtensionContext](is-inner-application-accessibilityextensioncontext.md)。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| \_AccessibilityExtensionContext.default | 表示辅助功能扩展的上下文环境，请参考[AccessibilityExtensionContext](is-inner-application-accessibilityextensioncontext.md)。 |

**示例：**

```
1. import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';

3. class EntryAbility extends AccessibilityExtensionAbility {
4. onConnect(): void {
5. let axContext = this.context;
6. }
7. }
```

## GestureType

PhonePC/2in1TabletWearable

type GestureType = 'left' | 'leftThenRight' | 'leftThenUp' | 'leftThenDown' | 'right' | 'rightThenLeft' | 'rightThenUp' | 'rightThenDown' | 'up' | 'upThenLeft' | 'upThenRight' | 'upThenDown' | 'down' | 'downThenLeft' | 'downThenRight' | 'downThenUp' | 'twoFingerSingleTap' | 'twoFingerDoubleTap' | 'twoFingerDoubleTapAndHold' | 'twoFingerTripleTap' | 'twoFingerTripleTapAndHold' | 'threeFingerSingleTap' | 'threeFingerDoubleTap' | 'threeFingerDoubleTapAndHold' | 'threeFingerTripleTap' | 'threeFingerTripleTapAndHold' | 'fourFingerSingleTap' | 'fourFingerDoubleTap' | 'fourFingerDoubleTapAndHold' | 'fourFingerTripleTap' | 'fourFingerTripleTapAndHold' | 'threeFingerSwipeUp' | 'threeFingerSwipeDown' | 'threeFingerSwipeLeft' | 'threeFingerSwipeRight' | 'fourFingerSwipeUp' | 'fourFingerSwipeDown' | 'fourFingerSwipeLeft' | 'fourFingerSwipeRight'

手势事件类型。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'left' | 表示向左的手势。 |
| 'leftThenRight' | 表示先向左再向右的手势。 |
| 'leftThenUp' | 表示先向左再向上的手势。 |
| 'leftThenDown' | 表示先向左再向下的手势。 |
| 'right' | 表示向右的手势。 |
| 'rightThenLeft' | 表示先向右再向左的手势。 |
| 'rightThenUp' | 表示先向右再向上的手势。 |
| 'rightThenDown' | 表示先向右再向下的手势。 |
| 'up' | 表示向上的手势。 |
| 'upThenLeft' | 表示先向上再向左的手势。 |
| 'upThenRight' | 表示先向上再向右的手势。 |
| 'upThenDown' | 表示先向上再向下的手势。 |
| 'down' | 表示向下的手势。 |
| 'downThenLeft' | 表示先向下再向左的手势。 |
| 'downThenRight' | 表示先向下再向右的手势。 |
| 'downThenUp' | 表示先向下再向上的手势。 |
| 'twoFingerSingleTap'11+ | 表示双指单击的手势。 |
| 'twoFingerDoubleTap'11+ | 表示双指双击的手势。 |
| 'twoFingerDoubleTapAndHold'11+ | 表示双指双击长按的手势。 |
| 'twoFingerTripleTap'11+ | 表示双指三击的手势。 |
| 'twoFingerTripleTapAndHold'11+ | 表示双指三击长按的手势。 |
| 'threeFingerSingleTap'11+ | 表示三指单击的手势。 |
| 'threeFingerDoubleTap'11+ | 表示三指双击的手势。 |
| 'threeFingerDoubleTapAndHold'11+ | 表示三指双击长按的手势。 |
| 'threeFingerTripleTap'11+ | 表示三指三击的手势。 |
| 'threeFingerTripleTapAndHold'11+ | 表示三指三击长按的手势。 |
| 'fourFingerSingleTap'11+ | 表示四指单击的手势。 |
| 'fourFingerDoubleTap'11+ | 表示四指双击的手势。 |
| 'fourFingerDoubleTapAndHold'11+ | 表示四指双击长按的手势。 |
| 'fourFingerTripleTap'11+ | 表示四指三击的手势。 |
| 'fourFingerTripleTapAndHold'11+ | 表示四指三击长按的手势。 |
| 'threeFingerSwipeUp'11+ | 表示三指向上滑动的手势。 |
| 'threeFingerSwipeDown'11+ | 表示三指向下滑动的手势。 |
| 'threeFingerSwipeLeft'11+ | 表示三指向左滑动的手势。 |
| 'threeFingerSwipeRight'11+ | 表示三指向右滑动的手势。 |
| 'fourFingerSwipeUp'11+ | 表示四指向上滑动的手势。 |
| 'fourFingerSwipeDown'11+ | 表示四指向下滑动的手势。 |
| 'fourFingerSwipeLeft'11+ | 表示四指向左滑动的手势。 |
| 'fourFingerSwipeRight'11+ | 表示四指向右滑动的手势。 |

## PageUpdateType

PhonePC/2in1TabletWearable

type PageUpdateType = 'pageContentUpdate' | 'pageStateUpdate'

页面刷新类型。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'pageContentUpdate' | 表示页面内容刷新。 |
| 'pageStateUpdate' | 表示页面状态刷新。 |

## TouchGuideType

PhonePC/2in1TabletWearable

type TouchGuideType = 'touchBegin' | 'touchEnd'

触摸浏览事件类型。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

| 类型 | 说明 |
| --- | --- |
| 'touchBegin' | 表示触摸浏览时开始触摸。 |
| 'touchEnd' | 表示触摸浏览时结束触摸。 |

## AccessibilityExtensionAbility.onConnect(deprecated)

PhonePC/2in1TabletWearable

onConnect(): void;

用户启用AccessibilityExtensionAbility时，系统服务完成连接后，回调此接口，可以该方法中执行初始化业务逻辑操作。该方法可以选择性重写。

说明

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**示例：**

```
1. import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';

3. class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
4. onConnect(): void {
5. console.info('AxExtensionAbility onConnect');
6. }
7. }
```

## AccessibilityExtensionAbility.onDisconnect(deprecated)

PhonePC/2in1TabletWearable

onDisconnect(): void;

用户停用AccessibilityExtensionAbility时，系统服务完成断开连接后，回调此接口，可以该方法中执行资源回收退出业务逻辑操作。该方法可以选择性重写。

说明

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**示例：**

```
1. import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';

3. class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
4. onDisconnect(): void {
5. console.info('AxExtensionAbility onDisconnect');
6. }
7. }
```

## AccessibilityExtensionAbility.onAccessibilityEvent(deprecated)

PhonePC/2in1TabletWearable

onAccessibilityEvent(event: AccessibilityEvent): void;

在关注的应用及事件类型对应的事件发生时回调此接口，可以在该方法中根据事件信息进行业务逻辑处理。一般情况下需要重写该方法完成业务。

说明

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| event | [AccessibilityEvent](js-apis-application-accessibilityextensionability.md#accessibilityevent) | 是 | 无障碍事件。无返回值。 |

**示例：**

```
1. import { AccessibilityExtensionAbility, AccessibilityEvent } from '@kit.AccessibilityKit';

3. class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
4. onAccessibilityEvent(event: AccessibilityEvent): void {
5. console.info('AxExtensionAbility onAccessibilityEvent');
6. if (event.eventType === 'click') {
7. console.info('AxExtensionAbility onAccessibilityEvent: click');
8. }
9. }
10. }
```

## AccessibilityExtensionAbility.onKeyEvent(deprecated)

PhonePC/2in1TabletWearable

onKeyEvent(keyEvent: KeyEvent): boolean;

在物理按键按下时回调此方法，可以在该方法中根据业务判断是否对事件进行拦截。

说明

从API version 9开始支持，从API version 12开始废弃，系统不再开放相关能力。

**系统能力**：SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| keyEvent | [KeyEvent](js-apis-keyevent.md#keyevent) | 是 | 按键事件回调函数。返回true表示拦截此按键。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 返回true表示此事件被消费，不会继续传递。  返回false表示此事件未被消费，会继续传递。 |

**示例：**

```
1. import { AccessibilityExtensionAbility } from '@kit.AccessibilityKit';
2. import { KeyEvent } from '@kit.InputKit';

4. class MyAccessibilityExtensionAbility extends AccessibilityExtensionAbility {
5. onKeyEvent(keyEvent: KeyEvent): boolean {
6. console.info('AxExtensionAbility onKeyEvent');
7. if (keyEvent.key.code === 16) {
8. console.info('AxExtensionAbility onKeyEvent: intercept 16');
9. return true;
10. }
11. return false;
12. }
13. }
```
