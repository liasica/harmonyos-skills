---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-observer
title: @ohos.arkui.observer (无感监听)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.observer (无感监听)
category: harmonyos-references
scraped_at: 2026-04-28T08:00:18+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:2cf1c46e2917fba93028849da2428bb769c82167f6f394c61534400105a65c71
---

提供UI组件行为变化的无感监听能力。推荐使用[UIObserver](arkts-apis-uicontext-uiobserver.md)进行组件监听。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* UIObserver仅能监听到本进程内的相关信息，不支持获取跨进程场景的信息。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { uiObserver } from '@kit.ArkUI';
```

## NavDestinationState

PhonePC/2in1TabletTVWearable

NavDestination组件状态。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ON\_SHOWN | 0 | NavDestination组件显示。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ON\_HIDDEN | 1 | NavDestination组件隐藏。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ON\_APPEAR12+ | 2 | NavDestination从组件树上挂载。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ON\_DISAPPEAR12+ | 3 | NavDestination从组件树上卸载。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ON\_WILL\_SHOW12+ | 4 | NavDestination组件显示之前。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ON\_WILL\_HIDE12+ | 5 | NavDestination组件隐藏之前。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ON\_WILL\_APPEAR12+ | 6 | NavDestination挂载到组件树之前。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ON\_WILL\_DISAPPEAR12+ | 7 | NavDestination从组件树上卸载之前。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| ON\_ACTIVE17+ | 8 | NavDestination组件处于激活态。  **元服务API：** 从API version 17开始，该接口支持在元服务中使用。 |
| ON\_INACTIVE17+ | 9 | NavDestination组件处于非激活态。  **元服务API：** 从API version 17开始，该接口支持在元服务中使用。 |
| ON\_BACKPRESS12+ | 100 | NavDestination组件返回。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |

## ScrollEventType12+

PhonePC/2in1TabletTVWearable

滚动事件的类型。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| SCROLL\_START | 0 | 滚动事件开始。 |
| SCROLL\_STOP | 1 | 滚动事件结束。 |

## RouterPageState

PhonePC/2in1TabletTVWearable

routerPage生命周期触发时对应的状态。RouterPageState用于[RouterPageInfo](js-apis-arkui-observer.md#routerpageinfo)中，作为[routerPageUpdate](js-apis-arkui-observer.md#uiobserveronrouterpageupdate11)无感监听的返回值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ABOUT\_TO\_APPEAR | 0 | page即将显示。 |
| ABOUT\_TO\_DISAPPEAR | 1 | page即将销毁。 |
| ON\_PAGE\_SHOW | 2 | page显示。 |
| ON\_PAGE\_HIDE | 3 | page隐藏。 |
| ON\_BACK\_PRESS | 4 | page返回时。 |

## TabContentState12+

PhonePC/2in1TabletTVWearable

TabContent组件的状态。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 值 | 说明 |
| --- | --- | --- |
| ON\_SHOW | 0 | TabContent组件显示。 |
| ON\_HIDE | 1 | TabContent组件隐藏。 |

## NavDestinationInfo

PhonePC/2in1TabletTVWearable

NavDestination组件信息，由系统返回给开发者。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| navigationId | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 包含NavDestination组件的Navigation组件的id。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| name | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | NavDestination组件的名称。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| state | [NavDestinationState](js-apis-arkui-observer.md#navdestinationstate) | 否 | 否 | NavDestination组件的状态。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| index12+ | number | 否 | 否 | NavDestination在页面栈中的索引。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。  取值范围：[0, +∞) |
| param12+ | Object | 否 | 是 | NavDestination组件的参数。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| navDestinationId12+ | string | 否 | 否 | NavDestination组件的唯一标识ID。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| mode15+ | [NavDestinationMode](ts-basic-components-navdestination.md#navdestinationmode枚举说明11) | 否 | 是 | NavDestination类型。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| uniqueId15+ | number | 否 | 是 | NavDestination组件的uniqueId。  **元服务API：** 从API version 15开始，该接口支持在元服务中使用。 |
| size23+ | [Size](js-apis-arkui-graphics.md#size) | 否 | 是 | NavDestination组件的大小，单位是vp。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## NavigationInfo12+

PhonePC/2in1TabletTVWearable

Navigation组件信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| navigationId | string | 否 | 否 | Navigation组件的id。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| pathStack | [NavPathStack](ts-basic-components-navigation.md#navpathstack10) | 否 | 否 | Navigation组件的导航控制器。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| uniqueId20+ | number | 否 | 是 | Navigation组件的uniqueId，可以通过[queryNavigationInfo](ts-custom-component-api.md#querynavigationinfo12)获取。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## ScrollEventInfo12+

PhonePC/2in1TabletTVWearable

ScrollEvent滚动信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 滚动组件的id。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| uniqueId | number | 否 | 否 | 滚动组件的uniqueId。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| scrollEvent | [ScrollEventType](js-apis-arkui-observer.md#scrolleventtype12) | 否 | 否 | 滚动事件的类型。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| offset | number | 否 | 否 | 滚动组件的当前偏移量。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| axis20+ | [Axis](ts-appendix-enums.md#axis) | 否 | 是 | 滚动组件的滚动方向。  **元服务API：** 从API version 20开始，该接口支持在元服务中使用。 |

## ObserverOptions12+

PhonePC/2in1TabletTVWearable

Observer选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 组件的id。 |

## RouterPageInfo

PhonePC/2in1TabletTVWearable

RouterPageInfo包含的信息，由系统返回给开发者。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | [UIContext](arkts-apis-uicontext-uicontext.md) | 否 | 否 | 触发生命周期的routerPage页面对应的上下文信息。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| index | number | 否 | 否 | 触发生命周期的routerPage在栈中的位置。  取值范围：[0, +∞)  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| name | string | 否 | 否 | 触发生命周期的routerPage页面的名称。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| path | string | 否 | 否 | 触发生命周期的routerPage页面的路径。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| state | [RouterPageState](js-apis-arkui-observer.md#routerpagestate) | 否 | 否 | 触发生命周期的routerPage页面的状态。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| pageId12+ | string | 否 | 否 | 触发生命周期的routerPage页面的唯一标识。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| size23+ | [Size](js-apis-arkui-graphics.md#size) | 否 | 是 | routerPage页面的大小，单位是vp。  **元服务API：** 从API version 23开始，该接口支持在元服务中使用。 |

## DensityInfo12+

PhonePC/2in1TabletTVWearable

屏幕像素密度变化回调包含的信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 否 | 否 | 屏幕像素密度变化时页面对应的上下文信息。 |
| density | number | 否 | 否 | 变化后的屏幕像素密度。  取值范围：[0, +∞) |

## NavDestinationSwitchInfo12+

PhonePC/2in1TabletTVWearable

Navigation组件页面切换的信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | [UIContext](arkts-apis-uicontext-uicontext.md) | 否 | 否 | 触发页面切换的Navigation对应的上下文信息。 |
| from | [NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo) | [NavBar](ts-basic-components-navigation.md#navbar12) | 否 | 否 | 页面切换的源页面。 |
| to | [NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo) | [NavBar](ts-basic-components-navigation.md#navbar12) | 否 | 否 | 页面切换的目的页面。 |
| operation | [NavigationOperation](ts-basic-components-navigation.md#navigationoperation11枚举说明) | 否 | 否 | 页面切换操作类型。 |

## NavDestinationSwitchObserverOptions12+

PhonePC/2in1TabletTVWearable

Navigation组件页面切换事件的监听选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| navigationId | [ResourceStr](ts-types.md#resourcestr) | 否 | 否 | 指定需要监听的Navigation的ID。 |

## TextChangeEventInfo22+

PhonePC/2in1TabletTVWearable

输入框文本变化的信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| id | string | 否 | 否 | 文本输入组件的ID。 |
| uniqueId | number | 否 | 否 | 文本输入组件的唯一标识符。 |
| content | string | 否 | 否 | 变化后的文本内容。 |

## TabContentInfo12+

PhonePC/2in1TabletTVWearable

TabContent页面的切换信息。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| tabContentId | string | 否 | 否 | TabContent组件的id。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| tabContentUniqueId | number | 否 | 否 | TabContent组件的uniqueId。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| state | [TabContentState](js-apis-arkui-observer.md#tabcontentstate12) | 否 | 否 | TabContent组件的状态。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| index | number | 否 | 否 | TabContent组件的下标索引。索引从0开始。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| id | string | 否 | 否 | Tabs组件的id。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| uniqueId | number | 否 | 否 | Tabs组件的uniqueId。  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |
| lastIndex22+ | number | 否 | 是 | 最近一次聚焦的TabsContent组件的下标索引。索引从0开始。仅在[on('tabChange')](arkts-apis-uicontext-uiobserver.md#ontabchange22)的回调函数中存在。  **元服务API：** 从API version 22开始，该接口支持在元服务中使用。 |

## WindowSizeLayoutBreakpointInfo22+

PhonePC/2in1TabletTVWearable

窗口尺寸布局断点变化回调的信息。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| widthBreakpoint | [WidthBreakpoint](ts-appendix-enums.md#widthbreakpoint13) | 是 | 否 | 窗口宽度所在的布局断点枚举。 |
| heightBreakpoint | [HeightBreakpoint](ts-appendix-enums.md#heightbreakpoint13) | 是 | 否 | 窗口高度所在的布局断点枚举。 |

## uiObserver.on('navDestinationUpdate')

PhonePC/2in1TabletTVWearable

on(type: 'navDestinationUpdate', callback: Callback<NavDestinationInfo>): void

监听NavDestination组件的状态变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationUpdate'，即NavDestination组件的状态变化。 |
| callback | Callback<[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)> | 是 | 回调函数。返回当前的NavDestination组件状态。 |

**示例：**

```
1. // Index.ets
2. // 演示 uiObserver.on('navDestinationUpdate', callback)
3. // uiObserver.off('navDestinationUpdate', callback)
4. import { uiObserver } from '@kit.ArkUI';

6. @Component
7. struct PageOne {
8. build() {
9. NavDestination() {
10. Text("pageOne")
11. }.title("pageOne")
12. }
13. }

15. @Entry
16. @Component
17. struct Index {
18. private stack: NavPathStack = new NavPathStack();

20. @Builder
21. PageBuilder(name: string) {
22. PageOne()
23. }

25. aboutToAppear() {
26. // 注册监听
27. uiObserver.on('navDestinationUpdate', (info) => {
28. console.info(`NavDestination state update ${JSON.stringify(info)}`);
29. });
30. }

32. aboutToDisappear() {
33. // 注销监听
34. uiObserver.off('navDestinationUpdate');
35. }

37. build() {
38. Column() {
39. Navigation(this.stack) {
40. Button("push").onClick(() => {
41. this.stack.pushPath({ name: "pageOne" });
42. })
43. }
44. .title("Navigation")
45. .navDestination(this.PageBuilder)
46. }
47. .width('100%')
48. .height('100%')
49. }
50. }
```

## uiObserver.off('navDestinationUpdate')

PhonePC/2in1TabletTVWearable

off(type: 'navDestinationUpdate', callback?: Callback<NavDestinationInfo>): void

取消监听NavDestination组件的状态变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationUpdate'，即NavDestination组件的状态变化。 |
| callback | Callback<[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)> | 否 | 回调函数。返回当前的NavDestination组件状态。 |

**示例：**

参考[uiObserver.on('navDestinationUpdate')](js-apis-arkui-observer.md#uiobserveronnavdestinationupdate)示例。

## uiObserver.on('navDestinationUpdate')

PhonePC/2in1TabletTVWearable

on(type: 'navDestinationUpdate', options: { navigationId: ResourceStr }, callback: Callback<NavDestinationInfo>): void

监听NavDestination组件的状态变化。与[uiObserver.on](js-apis-arkui-observer.md#uiobserveronnavdestinationupdate)相比，新增了options参数，即支持指定监听的Navigation的id。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationUpdate'，即NavDestination组件的状态变化。 |
| options | { navigationId: [ResourceStr](ts-types.md#resourcestr) } | 是 | 指定监听的Navigation的id。 |
| callback | Callback<[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)> | 是 | 回调函数。返回当前的NavDestination组件状态。 |

**示例：**

```
1. // Index.ets
2. // 演示 uiObserver.on('navDestinationUpdate', navigationId, callback)
3. // uiObserver.off('navDestinationUpdate', navigationId, callback)
4. import { uiObserver } from '@kit.ArkUI';

6. @Component
7. struct PageOne {
8. build() {
9. NavDestination() {
10. Text("pageOne")
11. }.title("pageOne")
12. }
13. }

15. @Entry
16. @Component
17. struct Index {
18. private stack: NavPathStack = new NavPathStack();

20. @Builder
21. PageBuilder(name: string) {
22. PageOne()
23. }

25. aboutToAppear() {
26. // 注册监听，指定Navigation的id
27. uiObserver.on('navDestinationUpdate', { navigationId: "testId" }, (info) => {
28. console.info(`NavDestination state update ${JSON.stringify(info)}`);
29. });
30. }

32. aboutToDisappear() {
33. // 注销监听
34. uiObserver.off('navDestinationUpdate', { navigationId: "testId" });
35. }

37. build() {
38. Column() {
39. Navigation(this.stack) {
40. Button("push").onClick(() => {
41. this.stack.pushPath({ name: "pageOne" });
42. })
43. }
44. .id("testId")
45. .title("Navigation")
46. .navDestination(this.PageBuilder)
47. }
48. .width('100%')
49. .height('100%')
50. }
51. }
```

## uiObserver.off('navDestinationUpdate')

PhonePC/2in1TabletTVWearable

off(type: 'navDestinationUpdate', options: { navigationId: ResourceStr }, callback?: Callback<NavDestinationInfo>): void

取消监听NavDestination组件的状态变化。与[uiObserver.off](js-apis-arkui-observer.md#uiobserveroffnavdestinationupdate)相比，新增了options参数，即支持指定监听的Navigation的id。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationUpdate'，即NavDestination组件的状态变化。 |
| options | { navigationId: [ResourceStr](ts-types.md#resourcestr) } | 是 | 指定监听的Navigation的id。 |
| callback | Callback<[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)> | 否 | 回调函数。返回当前的NavDestination组件状态。 |

**示例：**

参考[uiObserver.on('navDestinationUpdate')](js-apis-arkui-observer.md#uiobserveronnavdestinationupdate-1)示例。

## uiObserver.on('scrollEvent')12+

PhonePC/2in1TabletTVWearable

on(type: 'scrollEvent', callback: Callback<ScrollEventInfo>): void

监听所有滚动组件滚动事件的开始和结束。滚动组件包括[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)、[WaterFlow](ts-container-waterflow.md)、[ArcList](ts-container-arclist.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'scrollEvent'，即滚动事件的开始和结束。 |
| callback | Callback<[ScrollEventInfo](js-apis-arkui-observer.md#scrolleventinfo12)> | 是 | 回调函数。返回滚动事件的信息。 |

**示例：**

参考[uiObserver.off('scrollEvent')](js-apis-arkui-observer.md#uiobserveroffscrollevent12-1)示例。

## uiObserver.off('scrollEvent')12+

PhonePC/2in1TabletTVWearable

off(type: 'scrollEvent', callback?: Callback<ScrollEventInfo>): void

取消监听所有滚动组件滚动事件的开始和结束。滚动组件包括[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)、[WaterFlow](ts-container-waterflow.md)、[ArcList](ts-container-arclist.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'scrollEvent'，即滚动事件的开始和结束。 |
| callback | Callback<[ScrollEventInfo](js-apis-arkui-observer.md#scrolleventinfo12)> | 否 | 回调函数。返回滚动事件的信息。 |

**示例：**

参考[uiObserver.off('scrollEvent')](js-apis-arkui-observer.md#uiobserveroffscrollevent12-1)示例。

## uiObserver.on('scrollEvent')12+

PhonePC/2in1TabletTVWearable

on(type: 'scrollEvent', options: ObserverOptions, callback: Callback<ScrollEventInfo>): void

监听指定id的滚动组件滚动事件的开始和结束。滚动组件包括[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)、[WaterFlow](ts-container-waterflow.md)、[ArcList](ts-container-arclist.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'scrollEvent'，即滚动事件的开始和结束。 |
| options | [ObserverOptions](js-apis-arkui-observer.md#observeroptions12) | 是 | 指定监听的滚动组件的id。 |
| callback | Callback<[ScrollEventInfo](js-apis-arkui-observer.md#scrolleventinfo12)> | 是 | 回调函数。返回滚动事件的信息。 |

**示例：**

参考[uiObserver.off('scrollEvent')](js-apis-arkui-observer.md#uiobserveroffscrollevent12-1)示例。

## uiObserver.off('scrollEvent')12+

PhonePC/2in1TabletTVWearable

off(type: 'scrollEvent', options: ObserverOptions, callback?: Callback<ScrollEventInfo>): void

取消监听指定id的滚动组件滚动事件的开始和结束。滚动组件包括[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)、[WaterFlow](ts-container-waterflow.md)、[ArcList](ts-container-arclist.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'scrollEvent'，即滚动事件的开始和结束。 |
| options | [ObserverOptions](js-apis-arkui-observer.md#observeroptions12) | 是 | 指定监听的滚动组件的id。 |
| callback | Callback<[ScrollEventInfo](js-apis-arkui-observer.md#scrolleventinfo12)> | 否 | 回调函数。返回滚动事件的信息。 |

**示例：**

```
1. import { uiObserver } from '@kit.ArkUI'

3. @Entry
4. @Component
5. struct Index {
6. scroller: Scroller = new Scroller();
7. options: uiObserver.ObserverOptions = { id: 'testId' };
8. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7]

10. build() {
11. Column() {
12. Column() {
13. Scroll(this.scroller) {
14. Column() {
15. ForEach(this.arr, (item: number) => {
16. Text(item.toString())
17. .width('90%')
18. .height(150)
19. .backgroundColor(0xFFFFFF)
20. .borderRadius(15)
21. .fontSize(16)
22. .textAlign(TextAlign.Center)
23. .margin({ top: 10 })
24. }, (item: string) => item)
25. }.width('100%')
26. }
27. .id('testId')
28. .height('80%')
29. }
30. .width('100%')

32. Row() {
33. Button('UIObserver on')
34. .onClick(() => {
35. // 注册监听
36. uiObserver.on('scrollEvent', (info) => {
37. console.info(`scrollEventInfo ${JSON.stringify(info)}`);
38. });
39. })
40. Button('UIObserver off')
41. .onClick(() => {
42. // 注销监听
43. uiObserver.off('scrollEvent');
44. })
45. }

47. Row() {
48. Button('UIObserverWithId on')
49. .onClick(() => {
50. // 注册监听，指定组件的id
51. uiObserver.on('scrollEvent', this.options, (info) => {
52. console.info(`scrollEventInfo ${JSON.stringify(info)}`);
53. });
54. })
55. Button('UIObserverWithId off')
56. .onClick(() => {
57. // 注销监听
58. uiObserver.off('scrollEvent',this.options);
59. })
60. }
61. }
62. .height('100%')
63. }
64. }
```

## uiObserver.on('routerPageUpdate')11+

PhonePC/2in1TabletTVWearable

on(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback: Callback<RouterPageInfo>): void

监听router中page页面的状态变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'routerPageUpdate'，即router中page页面的状态变化。 |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 上下文信息，用以指定监听页面的范围。 |
| callback | Callback<[RouterPageInfo](js-apis-arkui-observer.md#routerpageinfo)> | 是 | 回调函数。携带pageInfo，返回当前的page页面状态。 |

**示例：**

```
1. // used in UIAbility
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { UIContext, window, uiObserver } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. private uiContext: UIContext | null = null;

9. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
10. // 注册监听，范围是abilityContext内的page
11. uiObserver.on('routerPageUpdate', this.context, (info: uiObserver.RouterPageInfo) => {
12. console.info(`[uiObserver][abilityContext] got info: ${JSON.stringify(info)}`)
13. })
14. }

16. onWindowStageCreate(windowStage: window.WindowStage): void {
17. windowStage.loadContent('pages/Index', (err) => {
18. windowStage.getMainWindow((err: BusinessError, data) => {
19. let windowInfo: window.Window = data;
20. // 获取UIContext实例
21. this.uiContext = windowInfo.getUIContext();
22. // 注册监听，范围是uiContext内的page
23. uiObserver.on('routerPageUpdate', this.uiContext, (info: uiObserver.RouterPageInfo)=>{
24. console.info(`[uiObserver][uiContext] got info: ${JSON.stringify(info)}`)
25. })
26. })
27. });
28. }

30. // ... other function in EntryAbility
31. }
```

## uiObserver.off('routerPageUpdate')11+

PhonePC/2in1TabletTVWearable

off(type: 'routerPageUpdate', context: UIAbilityContext | UIContext, callback?: Callback<RouterPageInfo>): void

取消监听router中page页面的状态变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'routerPageUpdate'，即router中page页面的状态变化。 |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 上下文信息，用以指定监听页面的范围。 |
| callback | Callback<[RouterPageInfo](js-apis-arkui-observer.md#routerpageinfo)> | 否 | 需要被注销的回调函数。 |

**示例：**

```
1. // used in UIAbility
2. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
3. import { uiObserver, UIContext } from '@kit.ArkUI';

5. export default class EntryAbility extends UIAbility {
6. // 实际使用前uiContext需要被赋值。参见示例uiObserver.on('routerPageUpdate')
7. private uiContext: UIContext | null = null;

9. onDestroy(): void {
10. // 注销当前abilityContext上的所有routerPageUpdate监听
11. uiObserver.off('routerPageUpdate', this.context)
12. }

14. onWindowStageDestroy(): void {
15. // 注销在uiContext上的所有routerPageUpdate监听
16. if (this.uiContext) {
17. uiObserver.off('routerPageUpdate', this.uiContext);
18. }
19. }

21. // ... other function in EntryAbility
22. }
```

## uiObserver.on('densityUpdate')12+

PhonePC/2in1TabletTVWearable

on(type: 'densityUpdate', context: UIContext, callback: Callback<DensityInfo>): void

监听屏幕像素密度变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'densityUpdate'，即屏幕像素密度变化。 |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 上下文信息，用以指定监听页面的范围。 |
| callback | Callback<[DensityInfo](js-apis-arkui-observer.md#densityinfo12)> | 是 | 回调函数。携带DensityInfo，返回变化后的屏幕像素密度。 |

**示例：**

```
1. import { uiObserver } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State density: number = 0;
7. @State message: string = '未注册监听';

9. densityUpdateCallback = (info: uiObserver.DensityInfo) => {
10. this.density = info.density;
11. this.message = '变化后的DPI：' + this.density.toString();
12. }

14. build() {
15. Column() {
16. Text(this.message)
17. .fontSize(24)
18. .fontWeight(FontWeight.Bold)
19. Button('注册屏幕像素密度变化监听')
20. .onClick(() => {
21. this.message = '已注册监听'
22. uiObserver.on('densityUpdate', this.getUIContext(), this.densityUpdateCallback);
23. })
24. }
25. }
26. }
```

## uiObserver.off('densityUpdate')12+

PhonePC/2in1TabletTVWearable

off(type: 'densityUpdate', context: UIContext, callback?: Callback<DensityInfo>): void

取消监听屏幕像素密度的变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'densityUpdate'，即屏幕像素密度变化。 |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 上下文信息，用以指定监听页面的范围。 |
| callback | Callback<[DensityInfo](js-apis-arkui-observer.md#densityinfo12)> | 否 | 需要被注销的回调函数。若不指定具体的回调函数，则注销指定UIContext下所有densityUpdate事件监听。 |

```
1. import { uiObserver, UIContext } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. @State density: number = 0;
7. @State message: string = '未注册监听'

9. densityUpdateCallback = (info: uiObserver.DensityInfo) => {
10. this.density = info.density;
11. this.message = '变化后的DPI：' + this.density.toString();
12. }

14. build() {
15. Column() {
16. Text(this.message)
17. .fontSize(24)
18. .fontWeight(FontWeight.Bold)
19. Button('注册屏幕像素密度变化监听')
20. .margin({ bottom: 10 })
21. .onClick(() => {
22. this.message = '已注册监听'
23. uiObserver.on('densityUpdate', this.getUIContext(), this.densityUpdateCallback);
24. })
25. Button('解除注册屏幕像素密度变化监听')
26. .onClick(() => {
27. this.message = '未注册监听'
28. uiObserver.off('densityUpdate', this.getUIContext(), this.densityUpdateCallback);
29. })
30. }
31. }
32. }
```

## uiObserver.on('willDraw')12+

PhonePC/2in1TabletTVWearable

on(type: 'willDraw', context: UIContext, callback: Callback<void>): void

监听每一帧绘制指令下发情况。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'willDraw'，即是否将要绘制。 |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 上下文信息，用以指定监听页面的范围。 |
| callback | Callback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { uiObserver } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. willDrawCallback = () => {
7. console.info("willDraw指令下发");
8. }
9. build() {
10. Column() {
11. Button('注册绘制指令下发监听')
12. .onClick(() => {
13. uiObserver.on('willDraw', this.getUIContext(), this.willDrawCallback);
14. })
15. }
16. }
17. }
```

## uiObserver.off('willDraw')12+

PhonePC/2in1TabletTVWearable

off(type: 'willDraw', context: UIContext, callback?: Callback<void>): void

取消监听每一帧绘制指令下发情况。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'willDraw'，即是否将要绘制。 |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 上下文信息，用以指定监听页面的范围。 |
| callback | Callback<void> | 否 | 需要被注销的回调函数。 |

```
1. import { uiObserver } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. willDrawCallback = () => {
7. console.info("willDraw指令下发")
8. }

10. build() {
11. Column() {
12. Button('注册绘制指令下发监听')
13. .margin({ bottom: 10 })
14. .onClick(() => {
15. uiObserver.on('willDraw', this.getUIContext(), this.willDrawCallback);
16. })
17. Button('解除注册绘制指令下发监听')
18. .onClick(() => {
19. uiObserver.off('willDraw', this.getUIContext(), this.willDrawCallback);
20. })
21. }
22. }
23. }
```

## uiObserver.on('didLayout')12+

PhonePC/2in1TabletTVWearable

on(type: 'didLayout', context: UIContext, callback: Callback<void>): void

监听每一帧布局完成情况。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'didLayout'，即是否布局完成。 |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 上下文信息，用以指定监听页面的范围。 |
| callback | Callback<void> | 是 | 回调函数。 |

**示例：**

```
1. import { uiObserver } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. didLayoutCallback = () => {
7. console.info("Layout布局完成");
8. }
9. build() {
10. Column() {
11. Button('注册布局完成监听')
12. .onClick(() => {
13. uiObserver.on('didLayout', this.getUIContext(), this.didLayoutCallback);
14. })
15. }
16. }
17. }
```

## uiObserver.off('didLayout')12+

PhonePC/2in1TabletTVWearable

off(type: 'didLayout', context: UIContext, callback?: Callback<void>): void

取消监听每一帧布局完成情况。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'didLayout'，即是否布局完成。 |
| context | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 上下文信息，用以指定监听页面的范围。 |
| callback | Callback<void> | 否 | 需要被注销的回调函数。 |

```
1. import { uiObserver } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct Index {
6. didLayoutCallback = () => {
7. console.info("Layout布局完成")
8. }

10. build() {
11. Column() {
12. Button('注册布局完成监听')
13. .margin({ bottom: 10 })
14. .onClick(() => {
15. uiObserver.on('didLayout', this.getUIContext(), this.didLayoutCallback);
16. })
17. Button('解除布局完成监听')
18. .onClick(() => {
19. uiObserver.off('didLayout', this.getUIContext(), this.didLayoutCallback);
20. })
21. }
22. }
23. }
```

## uiObserver.on('navDestinationSwitch')12+

PhonePC/2in1TabletTVWearable

on(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, callback: Callback<NavDestinationSwitchInfo>): void

监听Navigation的页面切换事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationSwitch'，即Navigation的页面切换事件。 |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 上下文信息，用以指定监听页面切换事件的范围。 |
| callback | Callback<[NavDestinationSwitchInfo](js-apis-arkui-observer.md#navdestinationswitchinfo12)> | 是 | 回调函数。携带NavDestinationSwitchInfo，返回页面切换事件的信息。 |

**示例：**

```
1. // EntryAbility.ets
2. // 演示 uiObserver.on('navDestinationSwitch', UIAbilityContext, callback)
3. // uiObserver.off('navDestinationSwitch', UIAbilityContext, callback)
4. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
5. import { uiObserver, window } from '@kit.ArkUI';
6. import { hilog } from "@kit.PerformanceAnalysisKit";

8. function callbackFunc(info: uiObserver.NavDestinationSwitchInfo) {
9. console.info(`testTag navDestinationSwitch from: ${JSON.stringify(info.from)} to: ${JSON.stringify(info.to)}`)
10. }

12. export default class EntryAbility extends UIAbility {
13. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
14. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
15. uiObserver.on('navDestinationSwitch', this.context, callbackFunc);
16. }

18. onDestroy(): void {
19. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
20. uiObserver.off('navDestinationSwitch', this.context, callbackFunc);
21. }

23. onWindowStageCreate(windowStage: window.WindowStage): void {
24. // Main window is created, set main page for this ability
25. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

27. windowStage.loadContent('pages/Index', (err, data) => {
28. if (err.code) {
29. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
30. return;
31. }
32. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
33. });
34. }

36. onWindowStageDestroy(): void {
37. // Main window is destroyed, release UI related resources
38. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
39. }

41. onForeground(): void {
42. // Ability has brought to foreground
43. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
44. }

46. onBackground(): void {
47. // Ability has back to background
48. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
49. }
50. }
```

```
1. // Index.ets
2. // 演示 uiObserver.on('navDestinationSwitch', UIContext, callback)
3. // uiObserver.off('navDestinationSwitch', UIContext, callback)
4. import { uiObserver } from '@kit.ArkUI';

6. @Component
7. struct PageOne {
8. build() {
9. NavDestination() {
10. Text("pageOne")
11. }.title("pageOne")
12. }
13. }

15. function callbackFunc(info: uiObserver.NavDestinationSwitchInfo) {
16. console.info(`testTag navDestinationSwitch from: ${JSON.stringify(info.from)} to: ${JSON.stringify(info.to)}`)
17. }

19. @Entry
20. @Component
21. struct Index {
22. private stack: NavPathStack = new NavPathStack();

24. @Builder
25. PageBuilder(name: string) {
26. PageOne()
27. }

29. aboutToAppear() {
30. uiObserver.on('navDestinationSwitch', this.getUIContext(), callbackFunc)
31. }

33. aboutToDisappear() {
34. uiObserver.off('navDestinationSwitch', this.getUIContext(), callbackFunc)
35. }

37. build() {
38. Column() {
39. Navigation(this.stack) {
40. Button("push").onClick(() => {
41. this.stack.pushPath({ name: "pageOne" });
42. })
43. }
44. .title("Navigation")
45. .navDestination(this.PageBuilder)
46. }
47. .width('100%')
48. .height('100%')
49. }
50. }
```

## uiObserver.off('navDestinationSwitch')12+

PhonePC/2in1TabletTVWearable

off(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, callback?: Callback<NavDestinationSwitchInfo>): void

取消监听Navigation的页面切换事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationSwitch'，即Navigation的页面切换事件。 |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 上下文信息，用以指定监听页面切换事件的范围。 |
| callback | Callback<[NavDestinationSwitchInfo](js-apis-arkui-observer.md#navdestinationswitchinfo12)> | 否 | 需要被注销的回调函数。 |

**示例：**

参考[uiObserver.on('navDestinationSwitch')](js-apis-arkui-observer.md#uiobserveronnavdestinationswitch12)示例。

## uiObserver.on('navDestinationSwitch')12+

PhonePC/2in1TabletTVWearable

on(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, observerOptions: NavDestinationSwitchObserverOptions, callback: Callback<NavDestinationSwitchInfo>): void

监听Navigation的页面切换事件。与[uiObserver.on](js-apis-arkui-observer.md#uiobserveronnavdestinationswitch12)相比，新增了observerOptions参数，即支持设置监听选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationSwitch'，即Navigation的页面切换事件。 |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 上下文信息，用以指定监听页面切换事件的范围。 |
| observerOptions | [NavDestinationSwitchObserverOptions](js-apis-arkui-observer.md#navdestinationswitchobserveroptions12) | 是 | 监听选项。 |
| callback | Callback<[NavDestinationSwitchInfo](js-apis-arkui-observer.md#navdestinationswitchinfo12)> | 是 | 回调函数。携带NavDestinationSwitchInfo，返回页面切换事件的信息。 |

**示例：**

```
1. // EntryAbility.ets
2. // 演示 uiObserver.on('navDestinationSwitch', UIAbilityContext, NavDestinationSwitchObserverOptions, callback)
3. // uiObserver.off('navDestinationSwitch', UIAbilityContext, NavDestinationSwitchObserverOptions, callback)
4. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
5. import { uiObserver, window } from '@kit.ArkUI';
6. import { hilog } from "@kit.PerformanceAnalysisKit"

8. function callbackFunc(info: uiObserver.NavDestinationSwitchInfo) {
9. console.info(`testTag navDestinationSwitch from: ${JSON.stringify(info.from)} to: ${JSON.stringify(info.to)}`)
10. }

12. export default class EntryAbility extends UIAbility {
13. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
14. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
15. uiObserver.on('navDestinationSwitch', this.context, {
16. navigationId: "myNavId"
17. }, callbackFunc);
18. }

20. onDestroy(): void {
21. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
22. uiObserver.off('navDestinationSwitch', this.context, {
23. navigationId: "myNavId"
24. }, callbackFunc);
25. }

27. onWindowStageCreate(windowStage: window.WindowStage): void {
28. // Main window is created, set main page for this ability
29. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

31. windowStage.loadContent('pages/Index', (err, data) => {
32. if (err.code) {
33. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
34. return;
35. }
36. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
37. });
38. }

40. onWindowStageDestroy(): void {
41. // Main window is destroyed, release UI related resources
42. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
43. }

45. onForeground(): void {
46. // Ability has brought to foreground
47. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
48. }

50. onBackground(): void {
51. // Ability has back to background
52. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
53. }
54. }
```

```
1. // Index.ets
2. // 演示 uiObserver.on('navDestinationSwitch', UIContext, NavDestinationSwitchObserverOptions, callback)
3. // uiObserver.off('navDestinationSwitch', UIContext, NavDestinationSwitchObserverOptions, callback)
4. import { uiObserver } from '@kit.ArkUI';

6. @Component
7. struct PageOne {
8. build() {
9. NavDestination() {
10. Text("pageOne")
11. }.title("pageOne")
12. }
13. }

15. function callbackFunc(info: uiObserver.NavDestinationSwitchInfo) {
16. console.info(`testTag navDestinationSwitch from: ${JSON.stringify(info.from)} to: ${JSON.stringify(info.to)}`)
17. }

19. @Entry
20. @Component
21. struct Index {
22. private stack: NavPathStack = new NavPathStack();

24. @Builder
25. PageBuilder(name: string) {
26. PageOne()
27. }

29. aboutToAppear() {
30. uiObserver.on('navDestinationSwitch', this.getUIContext(), { navigationId: "myNavId" }, callbackFunc)
31. }

33. aboutToDisappear() {
34. uiObserver.off('navDestinationSwitch', this.getUIContext(), { navigationId: "myNavId" }, callbackFunc)
35. }

37. build() {
38. Column() {
39. Navigation(this.stack) {
40. Button("push").onClick(() => {
41. this.stack.pushPath({ name: "pageOne" });
42. })
43. }
44. .id("myNavId")
45. .title("Navigation")
46. .navDestination(this.PageBuilder)
47. }
48. .width('100%')
49. .height('100%')
50. }
51. }
```

## uiObserver.off('navDestinationSwitch')12+

PhonePC/2in1TabletTVWearable

off(type: 'navDestinationSwitch', context: UIAbilityContext | UIContext, observerOptions: NavDestinationSwitchObserverOptions, callback?: Callback<NavDestinationSwitchInfo>): void

取消监听Navigation的页面切换事件。与[uiObserver.off](js-apis-arkui-observer.md#uiobserveroffnavdestinationswitch12)相比，新增了observerOptions参数，即支持设置监听选项。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationSwitch'，即Navigation的页面切换事件。 |
| context | [UIAbilityContext](js-apis-inner-application-uiabilitycontext.md) | [UIContext](arkts-apis-uicontext-uicontext.md) | 是 | 上下文信息，用以指定监听页面切换事件的范围。 |
| observerOptions | [NavDestinationSwitchObserverOptions](js-apis-arkui-observer.md#navdestinationswitchobserveroptions12) | 是 | 监听选项。 |
| callback | Callback<[NavDestinationSwitchInfo](js-apis-arkui-observer.md#navdestinationswitchinfo12)> | 否 | 需要被注销的回调函数。 |

**示例：**

参考[uiObserver.on('navDestinationSwitch')](js-apis-arkui-observer.md#uiobserveronnavdestinationswitch12-1)接口示例。

## uiObserver.on('tabContentUpdate')12+

PhonePC/2in1TabletTVWearable

on(type: 'tabContentUpdate', callback: Callback<TabContentInfo>): void

监听TabContent页面的切换事件。相比[on('tabChange')](arkts-apis-uicontext-uiobserver.md#ontabchange22)，本接口不支持监听Tabs组件初始化时，显示首个页签的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tabContentUpdate'，即TabContent页面的切换事件。 |
| callback | Callback<[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)> | 是 | 回调函数。携带TabContentInfo，返回TabContent页面切换事件的信息。 |

**示例：**

```
1. import { uiObserver } from '@kit.ArkUI';

3. function callbackFunc(info: uiObserver.TabContentInfo) {
4. console.info(`tabContentUpdate ${JSON.stringify(info)}`);
5. }

7. @Entry
8. @Component
9. struct TabsExample {

11. aboutToAppear(): void {
12. // 注册监听
13. uiObserver.on('tabContentUpdate', callbackFunc);
14. }

16. aboutToDisappear(): void {
17. // 注销监听
18. uiObserver.off('tabContentUpdate', callbackFunc);
19. }

21. build() {
22. Column() {
23. Tabs() {
24. TabContent() {
25. Column().width('100%').height('100%').backgroundColor('#00CB87')
26. }.tabBar('green').id('tabContentId0')

28. TabContent() {
29. Column().width('100%').height('100%').backgroundColor('#007DFF')
30. }.tabBar('blue').id('tabContentId1')

32. TabContent() {
33. Column().width('100%').height('100%').backgroundColor('#FFBF00')
34. }.tabBar('yellow').id('tabContentId2')

36. TabContent() {
37. Column().width('100%').height('100%').backgroundColor('#E67C92')
38. }.tabBar('pink').id('tabContentId3')
39. }
40. .width(360)
41. .height(296)
42. .backgroundColor('#F1F3F5')
43. .id('tabsId')
44. }.width('100%')
45. }
46. }
```

## uiObserver.off('tabContentUpdate')12+

PhonePC/2in1TabletTVWearable

off(type: 'tabContentUpdate', callback?: Callback<TabContentInfo>): void

取消监听TabContent页面的切换事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tabContentUpdate'，即TabContent页面的切换事件。 |
| callback | Callback<[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)> | 否 | 需要被注销的回调函数。 |

**示例：**

参考[uiObserver.on('tabContentUpdate')](js-apis-arkui-observer.md#uiobserverontabcontentupdate12)接口示例。

## uiObserver.on('tabContentUpdate')12+

PhonePC/2in1TabletTVWearable

on(type: 'tabContentUpdate', options: ObserverOptions, callback: Callback<TabContentInfo>): void

监听指定Tabs组件id的TabContent页面切换事件。相比[on('tabChange')](arkts-apis-uicontext-uiobserver.md#ontabchange22)，本接口不支持监听Tabs组件初始化时，显示首个页签的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tabContentUpdate'，即TabContent页面的切换事件。 |
| options | [ObserverOptions](js-apis-arkui-observer.md#observeroptions12) | 是 | 指定监听的Tabs组件的id。 |
| callback | Callback<[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)> | 是 | 回调函数。携带TabContentInfo，返回TabContent页面切换事件的信息。 |

**示例：**

```
1. import { uiObserver } from '@kit.ArkUI';

3. function callbackFunc(info: uiObserver.TabContentInfo) {
4. console.info(`tabContentUpdate ${JSON.stringify(info)}`);
5. }

7. @Entry
8. @Component
9. struct TabsExample {

11. aboutToAppear(): void {
12. // 注册监听，指定Tabs的id
13. uiObserver.on('tabContentUpdate', { id: 'tabsId' }, callbackFunc);
14. }

16. aboutToDisappear(): void {
17. // 注销监听
18. uiObserver.off('tabContentUpdate', { id: 'tabsId' }, callbackFunc);
19. }

21. build() {
22. Column() {
23. Tabs() {
24. TabContent() {
25. Column().width('100%').height('100%').backgroundColor('#00CB87')
26. }.tabBar('green').id('tabContentId0')

28. TabContent() {
29. Column().width('100%').height('100%').backgroundColor('#007DFF')
30. }.tabBar('blue').id('tabContentId1')

32. TabContent() {
33. Column().width('100%').height('100%').backgroundColor('#FFBF00')
34. }.tabBar('yellow').id('tabContentId2')

36. TabContent() {
37. Column().width('100%').height('100%').backgroundColor('#E67C92')
38. }.tabBar('pink').id('tabContentId3')
39. }
40. .width(360)
41. .height(296)
42. .backgroundColor('#F1F3F5')
43. .id('tabsId')
44. }.width('100%')
45. }
46. }
```

## uiObserver.off('tabContentUpdate')12+

PhonePC/2in1TabletTVWearable

off(type: 'tabContentUpdate', options: ObserverOptions, callback?: Callback<TabContentInfo>): void

取消监听指定Tabs组件id的TabContent页面切换事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tabContentUpdate'，即TabContent页面的切换事件。 |
| options | [ObserverOptions](js-apis-arkui-observer.md#observeroptions12) | 是 | 指定监听的Tabs组件的id。 |
| callback | Callback<[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)> | 否 | 需要被注销的回调函数。 |

**示例：**

参考[uiObserver.on('tabContentUpdate')](js-apis-arkui-observer.md#uiobserverontabcontentupdate12-1)接口示例。
