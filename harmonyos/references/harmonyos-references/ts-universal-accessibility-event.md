---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-accessibility-event
title: 无障碍控制操作
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 通用事件 > 无障碍相关 > 无障碍控制操作
category: harmonyos-references
scraped_at: 2026-04-28T08:00:57+08:00
doc_updated_at: 2026-04-17
content_hash: sha256:4413739e4bd7fca0c42f21fc0a659b32ace2e5c3a401554a5d822e1a3a85475c
---

在开启无障碍模式后，需要判断是否拦截无障碍控制操作。

说明

* 本模块首批接口从API version 18开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 目前仅支持通过开启无障碍模式触发。

## onAccessibilityFocus

PhonePC/2in1TabletTVWearable

onAccessibilityFocus(callback: AccessibilityFocusCallback): T

设置无障碍节点获焦、失焦状态的回调函数。当状态发生变化时，触发回调函数。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AccessibilityFocusCallback](ts-universal-accessibility-event.md#accessibilityfocuscallback) | 是 | 向注册回调函数方通知当前获焦、失焦状态。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## AccessibilityFocusCallback

PhonePC/2in1TabletTVWearable

type AccessibilityFocusCallback = (isFocus: boolean) => void

定义onAccessibilityFocus中使用的回调类型。

**卡片能力：** 从API version 18开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isFocus | boolean | 是 | 用于表示组件是否获焦。  true：当前组件获焦。  false：当前组件失焦。 |

## onAccessibilityActionIntercept20+

PhonePC/2in1TabletTVWearable

onAccessibilityActionIntercept(callback: AccessibilityActionInterceptCallback): T

该接口在无障碍模式下，可在无障碍控制操作触发前通知注册的回调函数，由注册方决定是否拦截该次无障碍动作，对不支持Click的组件注册也无法触发回调。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | [AccessibilityActionInterceptCallback](ts-universal-accessibility-event.md#accessibilityactioninterceptcallback20) | 是 | 在无障碍控制操作触发前，向注册回调函数方通知，由注册方决定是否拦截该次无障碍控制操作。  入参设置undefined时取消回调注册。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| T | 返回当前组件。 |

## AccessibilityActionInterceptCallback20+

PhonePC/2in1TabletTVWearable

type AccessibilityActionInterceptCallback = (action: AccessibilityAction) => AccessibilityActionInterceptResult

提供onAccessibilityActionIntercept中使用的回调函数参数类型。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| action | [AccessibilityAction](ts-universal-accessibility-event.md#accessibilityaction20枚举说明) | 是 | 当前触发的无障碍控制操作类型。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [AccessibilityActionInterceptResult](ts-universal-accessibility-event.md#accessibilityactioninterceptresult20枚举说明) | 无障碍控制操作拦截结果。 |

## AccessibilityAction20+枚举说明

PhonePC/2in1TabletTVWearable

定义组件当前触发的无障碍控制操作类型。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| UNDEFINED\_ACTION | 0 | 未定义的无障碍操作。 |
| ACCESSIBILITY\_CLICK | 1 | 无障碍点击操作。 |

## AccessibilityActionInterceptResult20+枚举说明

PhonePC/2in1TabletTVWearable

定义AccessibilityActionInterceptCallback的无障碍控制操作拦截结果。

**卡片能力：** 从API version 20开始，该接口支持在ArkTS卡片中使用。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ACTION\_INTERCEPT | 0 | 拦截当前组件接收的无障碍控制操作，回调处理结束后，不允许当前组件响应无障碍控制操作。 |
| ACTION\_CONTINUE | 1 | 拦截当前组件接收的无障碍控制操作, 回调处理结束后，仍然需要组件做出响应，执行当前组件的处理逻辑。 |
| ACTION\_RISE | 2 | 拦截执行当前组件接收的无障碍控制操作，回调处理结束后，仍然需要组件做出响应，执行当前组件的处理逻辑，并且将ACTION信息往父组件传递，传递到下一个使用了onAccessibilityActionIntercept的组件，触发当前组件中注册的回调，但不触发组件处理逻辑。处理完成后，可以继续使用RISE向父组件传递ACTION。 |

## 示例

PhonePC/2in1TabletTVWearable

### 示例1（设置onAccessibilityActionIntercept拦截点击事件）

该示例主要演示通过使用onAccessibilityActionIntercept事件实现Toggle组件在无障碍模式下于点击事件发生之前拦截点击事件并确认是否拦截该点击事件的操作。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct SwitchBootcamp {
5. @State private isOn: boolean = false;

7. build() {
8. NavDestination() {
9. Column() {
10. Text('onTouchIntercept')
11. Row() {
12. Text('Label message')
13. Blank()
14. Toggle({ type: ToggleType.Switch, isOn: $$this.isOn })
15. .onAccessibilityActionIntercept((action : AccessibilityAction) => {
16. if (action === AccessibilityAction.ACCESSIBILITY_CLICK) {
17. this.getUIContext().showAlertDialog({
18. title: '标题',
19. message: '内容信息',
20. primaryButton: {
21. value: '确认',
22. action: () => {
23. this.isOn = !this.isOn;
24. }
25. },
26. secondaryButton: {
27. value: '取消',
28. action: () => {
29. }
30. }
31. })
32. return AccessibilityActionInterceptResult.ACTION_INTERCEPT;
33. } else {
34. return AccessibilityActionInterceptResult.ACTION_CONTINUE;
35. }
36. })
37. }.width('100%')
38. }
39. .padding(24)
40. .width('100%')
41. }
42. }
43. }
```

### 示例2（设置onAccessibilityFocus回调函数）

从API version 18开始，当获焦、失焦状态发生变化时，触发该回调函数。本示例展示了[onAccessibilityFocus](ts-universal-accessibility-event.md#onaccessibilityfocus)的基本用法，聚焦到"onAccessibilityFocus takes effect"时，会打印"[testingTag] isFocus current is true"，聚焦到除了"onAccessibilityFocus takes effect"以外的地方都会打印"[testingTag] isFocus current is false"。

```
1. // xxx.ets
2. @Entry
3. @Component
4. struct OnAccessibilityFocusExample {

6. build() {
7. NavDestination() {
8. Column() {
9. Text("onAccessibilityFocus doesn't take effect")
10. Text("onAccessibilityFocus takes effect")
11. .onAccessibilityFocus((isFocus)=>{
12. console.info(`[testingTag] isFocus current is ${isFocus}`)
13. })
14. }
15. .padding(24)
16. .width('100%')
17. }
18. }
19. }
```
