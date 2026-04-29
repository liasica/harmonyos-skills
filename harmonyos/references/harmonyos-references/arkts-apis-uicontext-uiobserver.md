---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-uicontext-uiobserver
title: Class (UIObserver)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.UIContext (UIContext) > Class (UIObserver)
category: harmonyos-references
scraped_at: 2026-04-29T13:50:39+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:bb714229e79322e0b7b7e097a06c6f8c962352822eed53d9c69306f162690b0a
---

提供UI组件行为变化的无感监听能力。

说明

* 本模块首批接口从API version 10开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本Class首批接口从API version 11开始支持。
* 以下API需先使用UIContext中的[getUIObserver()](arkts-apis-uicontext-uicontext.md#getuiobserver11)方法获取到UIObserver对象，再通过该对象调用对应方法。
* UIObserver仅能监听到本进程内的相关信息，不支持获取跨进程场景的信息。

## on('navDestinationUpdate')11+

PhonePC/2in1TabletTVWearable

on(type: 'navDestinationUpdate', callback: Callback<observer.NavDestinationInfo>): void

监听[NavDestination](ts-basic-components-navdestination.md)组件的状态变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationUpdate'，即[NavDestination](ts-basic-components-navdestination.md)组件的状态变化。 |
| callback | Callback<observer.[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)> | 是 | 回调函数。返回当前的[NavDestination](ts-basic-components-navdestination.md)组件状态。 |

**示例：**

```
1. // Index.ets
2. // 演示uiObserver.on('navDestinationUpdate', callback)
3. // uiObserver.off('navDestinationUpdate', callback)

5. @Component
6. struct PageOne {
7. build() {
8. NavDestination() {
9. Text("pageOne")
10. }.title("pageOne")
11. }
12. }

14. @Entry
15. @Component
16. struct Index {
17. private stack: NavPathStack = new NavPathStack();

19. @Builder
20. PageBuilder(name: string) {
21. PageOne()
22. }

24. aboutToAppear() {
25. // 添加监听
26. this.getUIContext().getUIObserver().on('navDestinationUpdate', (info) => {
27. console.info('NavDestination state update', JSON.stringify(info));
28. });
29. }

31. aboutToDisappear() {
32. // 取消监听，不选择回调时，取消所有监听的回调
33. this.getUIContext().getUIObserver().off('navDestinationUpdate');
34. }

36. build() {
37. Column() {
38. Navigation(this.stack) {
39. Button("push").onClick(() => {
40. // 将PageOne的NavDestination入栈
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

## off('navDestinationUpdate')11+

PhonePC/2in1TabletTVWearable

off(type: 'navDestinationUpdate', callback?: Callback<observer.NavDestinationInfo>): void

取消监听[NavDestination](ts-basic-components-navdestination.md)组件的状态变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationUpdate'，即[NavDestination](ts-basic-components-navdestination.md)组件的状态变化。 |
| callback | Callback<observer.[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)> | 否 | 需要取消的监听回调，不传参数时，取消所有的[Navigation](ts-basic-components-navigation.md)监听回调。 |

**示例：**

参考[on('navDestinationUpdate')](arkts-apis-uicontext-uiobserver.md#onnavdestinationupdate11)接口示例。

## on('navDestinationUpdate')11+

PhonePC/2in1TabletTVWearable

on(type: 'navDestinationUpdate', options: { navigationId: ResourceStr }, callback: Callback<observer.NavDestinationInfo>): void

通过[Navigation](ts-basic-components-navigation.md)的id监听[NavDestination](ts-basic-components-navdestination.md)组件的状态变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationUpdate'，即[NavDestination](ts-basic-components-navdestination.md)组件的状态变化。 |
| options | { navigationId: [ResourceStr](ts-types.md#resourcestr) } | 是 | 指定监听的[Navigation](ts-basic-components-navigation.md)的id。 |
| callback | Callback<observer.[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)> | 是 | 回调函数。返回当前的[NavDestination](ts-basic-components-navdestination.md)组件状态。 |

**示例：**

```
1. // Index.ets
2. // 演示uiObserver.on('navDestinationUpdate', options, callback)
3. // uiObserver.off('navDestinationUpdate', options, callback)

5. @Component
6. struct PageOne {
7. build() {
8. NavDestination() {
9. Text("pageOne")
10. }.title("pageOne")
11. }
12. }

14. @Entry
15. @Component
16. struct Index {
17. private stack: NavPathStack = new NavPathStack();

19. @Builder
20. PageBuilder(name: string) {
21. PageOne()
22. }

24. aboutToAppear() {
25. // 添加监听，指定Navigation的id
26. this.getUIContext().getUIObserver().on('navDestinationUpdate', { navigationId: "testId" }, (info) => {
27. console.info('NavDestination state update', JSON.stringify(info));
28. });
29. }

31. aboutToDisappear() {
32. // 取消监听，不选择回调时，取消所有监听的回调
33. this.getUIContext().getUIObserver().off('navDestinationUpdate', { navigationId: "testId" });
34. }

36. build() {
37. Column() {
38. Navigation(this.stack) {
39. Button("push").onClick(() => {
40. // 将PageOne的NavDestination入栈
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

## off('navDestinationUpdate')11+

PhonePC/2in1TabletTVWearable

off(type: 'navDestinationUpdate', options: { navigationId: ResourceStr }, callback?: Callback<observer.NavDestinationInfo>): void

取消通过[Navigation](ts-basic-components-navigation.md)的id监听[NavDestination](ts-basic-components-navdestination.md)组件的状态变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationUpdate'，即[NavDestination](ts-basic-components-navdestination.md)组件的状态变化。 |
| options | { navigationId: [ResourceStr](ts-types.md#resourcestr) } | 是 | 指定监听的[Navigation](ts-basic-components-navigation.md)的id。 |
| callback | Callback<observer.[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)> | 否 | 需要取消的监听回调，不传参数时，取消该[Navigation](ts-basic-components-navigation.md)上所有的监听回调。 |

**示例：**

参考[on('navDestinationUpdate')](arkts-apis-uicontext-uiobserver.md#onnavdestinationupdate11-1)接口示例。

## on('navDestinationUpdateByUniqueId')20+

PhonePC/2in1TabletTVWearable

on(type: 'navDestinationUpdateByUniqueId', navigationUniqueId: number, callback: Callback<observer.NavDestinationInfo>): void

通过[Navigation](ts-basic-components-navigation.md)的uniqueId监听[NavDestination](ts-basic-components-navdestination.md)组件的状态变化，uniqueId可通过[queryNavigationInfo](ts-custom-component-api.md#querynavigationinfo12)获取。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationUpdateByUniqueId'，即[NavDestination](ts-basic-components-navdestination.md)组件的状态变化。 |
| navigationUniqueId | number | 是 | 指定监听的[Navigation](ts-basic-components-navigation.md)的uniqueId，可以通过[queryNavigationInfo](ts-custom-component-api.md#querynavigationinfo12)获取。 |
| callback | Callback<observer.[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)> | 是 | 回调函数。返回当前的[NavDestination](ts-basic-components-navdestination.md)组件状态。 |

**示例：**

通过[Navigation](ts-basic-components-navigation.md)的uniqueId，可以触发[NavDestination](ts-basic-components-navdestination.md)组件的状态变化。

```
1. // Index.ets
2. // 演示on('navDestinationUpdateByUniqueId', navigationUniqueId, callback)
3. // off('navDestinationUpdateByUniqueId', navigationUniqueId, callback)

5. @Component
6. struct PageOne {
7. private text = '';
8. private uniqueid = -1;
9. aboutToAppear() {
10. // 获取Navigation的uniqueId
11. let navigationUniqueId = this.queryNavigationInfo()?.uniqueId;
12. if (navigationUniqueId) {
13. this.uniqueid = navigationUniqueId.valueOf();
14. }
15. this.text = JSON.stringify(this.uniqueid);
16. // 添加监听，指定Navigation的uniqueId
17. this.getUIContext().getUIObserver().on('navDestinationUpdateByUniqueId', this.uniqueid, (info) => {
18. console.info('NavDestination state update navigationId', JSON.stringify(info));
19. });
20. }
21. aboutToDisappear() {
22. // 取消监听，不选择回调时，取消所有监听的回调
23. this.getUIContext().getUIObserver().off('navDestinationUpdateByUniqueId', this.uniqueid);
24. }
25. build() {
26. NavDestination() {
27. Text("pageOne")
28. Text('navigationUniqueId是:' + this.text)
29. .width('80%')
30. .height(50)
31. .margin(50)
32. .fontSize(20)
33. }.title("pageOne")
34. }
35. }

37. @Entry
38. @Component
39. struct Index {
40. private stack: NavPathStack = new NavPathStack();

42. @Builder
43. PageBuilder(name: string) {
44. PageOne()
45. }

47. build() {
48. Column() {
49. Navigation(this.stack) {
50. Button("push").onClick(() => {
51. // 将PageOne的NavDestination入栈
52. this.stack.pushPath({ name: "pageOne" });
53. })
54. }
55. .id("testId")
56. .title("Navigation")
57. .navDestination(this.PageBuilder)
58. }
59. .width('100%')
60. .height('100%')
61. }
62. }
```

## off('navDestinationUpdateByUniqueId')20+

PhonePC/2in1TabletTVWearable

off(type: 'navDestinationUpdateByUniqueId', navigationUniqueId: number, callback?: Callback<observer.NavDestinationInfo>): void

取消通过[Navigation](ts-basic-components-navigation.md)的uniqueId监听[NavDestination](ts-basic-components-navdestination.md)组件的变化。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationUpdateByUniqueId'，即[NavDestination](ts-basic-components-navdestination.md)组件的状态变化。 |
| navigationUniqueId | number | 是 | 指定监听的[Navigation](ts-basic-components-navigation.md)的uniqueId，可以通过[queryNavigationInfo](ts-custom-component-api.md#querynavigationinfo12)获取。 |
| callback | Callback<observer.[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)> | 否 | 需要取消的监听回调，不传参数时，取消该[Navigation](ts-basic-components-navigation.md)上所有的监听回调。 |

**示例：**

参考[on('navDestinationUpdateByUniqueId')](arkts-apis-uicontext-uiobserver.md#onnavdestinationupdatebyuniqueid20)接口示例。

## on('scrollEvent')12+

PhonePC/2in1TabletTVWearable

on(type: 'scrollEvent', callback: Callback<observer.ScrollEventInfo>): void

监听所有滚动组件滚动事件的开始和结束。滚动组件包括[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)、[WaterFlow](ts-container-waterflow.md)、[ArcList](ts-container-arclist.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'scrollEvent'，即滚动事件的开始和结束。 |
| callback | Callback<observer.[ScrollEventInfo](js-apis-arkui-observer.md#scrolleventinfo12)> | 是 | 回调函数。返回滚动事件的信息。 |

**示例：**

```
1. // Index.ets
2. // 演示uiObserver.on('scrollEvent', callback)
3. // uiObserver.off('scrollEvent', callback)
4. // uiObserver.on('scrollEvent', options, callback)
5. // uiObserver.off('scrollEvent', options, callback)

7. import { UIObserver } from '@kit.ArkUI';

9. @Entry
10. @Component
11. struct Index {
12. scroller: Scroller = new Scroller();
13. observer: UIObserver = this.getUIContext().getUIObserver();
14. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7];

16. build() {
17. Column() {
18. Column() {
19. Scroll(this.scroller) {
20. Column() {
21. ForEach(this.arr, (item: number) => {
22. Text(item.toString())
23. .width('90%')
24. .height(150)
25. .backgroundColor(0xFFFFFF)
26. .borderRadius(15)
27. .fontSize(16)
28. .textAlign(TextAlign.Center)
29. .margin({ top: 10 })
30. }, (item: string) => item)
31. }.width('100%')
32. }
33. .id('testId')
34. .height('80%')
35. }
36. .width('100%')

38. Row() {
39. Button('UIObserver on')
40. .onClick(() => {
41. // 添加监听
42. this.observer.on('scrollEvent', (info) => {
43. console.info('scrollEventInfo', JSON.stringify(info));
44. });
45. })
46. Button('UIObserver off')
47. .onClick(() => {
48. // 取消监听，不选择回调时，取消所有监听的回调
49. this.observer.off('scrollEvent');
50. })
51. }

53. Row() {
54. Button('UIObserverWithId on')
55. .onClick(() => {
56. // 添加监听，指定滚动组件的id
57. this.observer.on('scrollEvent', { id: 'testId' }, (info) => {
58. console.info('scrollEventInfo', JSON.stringify(info));
59. });
60. })
61. Button('UIObserverWithId off')
62. .onClick(() => {
63. // 取消监听，不选择回调时，取消所有监听的回调
64. this.observer.off('scrollEvent', { id: 'testId' });
65. })
66. }
67. }
68. .height('100%')
69. }
70. }
```

## off('scrollEvent')12+

PhonePC/2in1TabletTVWearable

off(type: 'scrollEvent', callback?: Callback<observer.ScrollEventInfo>): void

取消监听所有滚动组件滚动事件的开始和结束。滚动组件包括[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)、[WaterFlow](ts-container-waterflow.md)、[ArcList](ts-container-arclist.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'scrollEvent'，即滚动事件的开始和结束。 |
| callback | Callback<observer.[ScrollEventInfo](js-apis-arkui-observer.md#scrolleventinfo12)> | 否 | 回调函数。返回滚动事件的信息。不传参数时，取消所有滚动事件的监听回调。 |

**示例：**

参考[on('scrollEvent')](arkts-apis-uicontext-uiobserver.md#onscrollevent12)接口示例。

## on('scrollEvent')12+

PhonePC/2in1TabletTVWearable

on(type: 'scrollEvent', options: observer.ObserverOptions, callback: Callback<observer.ScrollEventInfo>): void

监听指定id的滚动组件滚动事件的开始和结束。滚动组件包括[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)、[WaterFlow](ts-container-waterflow.md)、[ArcList](ts-container-arclist.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'scrollEvent'，即滚动事件的开始和结束。 |
| options | observer.[ObserverOptions](js-apis-arkui-observer.md#observeroptions12) | 是 | Observer选项，包含指定监听的滚动组件的id。 |
| callback | Callback<observer.[ScrollEventInfo](js-apis-arkui-observer.md#scrolleventinfo12)> | 是 | 回调函数。返回滚动事件的信息。 |

**示例：**

参考[on('scrollEvent')](arkts-apis-uicontext-uiobserver.md#onscrollevent12)接口示例。

## off('scrollEvent')12+

PhonePC/2in1TabletTVWearable

off(type: 'scrollEvent', options: observer.ObserverOptions, callback?: Callback<observer.ScrollEventInfo>): void

取消监听指定id的滚动组件滚动事件的开始和结束。滚动组件包括[List](ts-container-list.md)、[Grid](ts-container-grid.md)、[Scroll](ts-container-scroll.md)、[WaterFlow](ts-container-waterflow.md)、[ArcList](ts-container-arclist.md)。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'scrollEvent'，即滚动事件的开始和结束。 |
| options | observer.[ObserverOptions](js-apis-arkui-observer.md#observeroptions12) | 是 | Observer选项，包含指定监听的滚动组件的id。 |
| callback | Callback<observer.[ScrollEventInfo](js-apis-arkui-observer.md#scrolleventinfo12)> | 否 | 回调函数。返回滚动事件的信息。不传参数时，取消所有滚动事件的监听回调。 |

**示例：**

参考[on('scrollEvent')](arkts-apis-uicontext-uiobserver.md#onscrollevent12)接口示例。

## on('routerPageUpdate')11+

PhonePC/2in1TabletTVWearable

on(type: 'routerPageUpdate', callback: Callback<observer.RouterPageInfo>): void

监听[Router](arkts-apis-uicontext-router.md)中page页面的状态变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'routerPageUpdate'，即[Router](arkts-apis-uicontext-router.md)中page页面的状态变化。 |
| callback | Callback<observer.[RouterPageInfo](js-apis-arkui-observer.md#routerpageinfo)> | 是 | 回调函数。携带[RouterPageInfo](js-apis-arkui-observer.md#routerpageinfo)对象，返回当前的page页面状态。 |

**示例：**

```
1. // PageOne.ets

3. @Entry
4. @Component
5. struct PageOne {
6. build() {
7. Column() {
8. Text("pageOne")
9. }
10. }
11. }
```

```
1. // Index.ets
2. // 演示uiObserver.on('routerPageUpdate', callback)
3. // uiObserver.off('routerPageUpdate', callback)

5. @Entry
6. @Component
7. struct Index {
8. aboutToAppear() {
9. // 添加监听
10. this.getUIContext().getUIObserver().on('routerPageUpdate', (info) => {
11. console.info('router page update', JSON.stringify(info));
12. });
13. }

15. aboutToDisappear() {
16. // 取消监听，不选择回调时，取消所有监听的回调
17. this.getUIContext().getUIObserver().off('routerPageUpdate');
18. }

20. build() {
21. Column() {
22. Button("pushUrl").onClick(() => {
23. // router跳转到PageOne.ets页面
24. this.getUIContext().getRouter().pushUrl({ url: 'pages/PageOne' })
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

## off('routerPageUpdate')11+

PhonePC/2in1TabletTVWearable

off(type: 'routerPageUpdate', callback?: Callback<observer.RouterPageInfo>): void

取消监听[Router](arkts-apis-uicontext-router.md)中page页面的状态变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'routerPageUpdate'，即[Router](arkts-apis-uicontext-router.md)中page页面的状态变化。 |
| callback | Callback<observer.[RouterPageInfo](js-apis-arkui-observer.md#routerpageinfo)> | 否 | 需要被注销的回调函数。不传参数时，取消所有[Router](arkts-apis-uicontext-router.md)中page页面状态变化的监听回调。 |

**示例：**

参考[on('routerPageUpdate')](arkts-apis-uicontext-uiobserver.md#onrouterpageupdate11)接口示例。

## on('densityUpdate')12+

PhonePC/2in1TabletTVWearable

on(type: 'densityUpdate', callback: Callback<observer.DensityInfo>): void

监听屏幕像素密度变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'densityUpdate'，即屏幕像素密度变化。 |
| callback | Callback<observer.[DensityInfo](js-apis-arkui-observer.md#densityinfo12)> | 是 | 回调函数。携带[DensityInfo](js-apis-arkui-observer.md#densityinfo12)，返回变化后的屏幕像素密度。 |

**示例：**

```
1. // Index.ets
2. // 演示uiObserver.on('densityUpdate', callback)
3. // uiObserver.off('densityUpdate', callback)

5. import { uiObserver } from '@kit.ArkUI';

7. @Entry
8. @Component
9. struct Index {
10. @State density: number = 0;
11. @State message: string = '未注册监听';

13. // 定义监听回调函数
14. densityUpdateCallback = (info: uiObserver.DensityInfo) => {
15. this.density = info.density;
16. this.message = '变化后的DPI：' + this.density.toString();
17. }

19. build() {
20. Column() {
21. Text(this.message)
22. .fontSize(24)
23. .fontWeight(FontWeight.Bold)
24. Button('注册屏幕像素密度变化监听')
25. .margin({ bottom: 10 })
26. .onClick(() => {
27. this.message = '已注册监听';
28. // 添加监听
29. this.getUIContext().getUIObserver().on('densityUpdate', this.densityUpdateCallback);
30. })
31. Button('解除注册屏幕像素密度变化监听')
32. .onClick(() => {
33. this.message = '未注册监听';
34. // 取消监听
35. this.getUIContext().getUIObserver().off('densityUpdate', this.densityUpdateCallback);
36. })
37. }
38. }
39. }
```

## off('densityUpdate')12+

PhonePC/2in1TabletTVWearable

off(type: 'densityUpdate', callback?: Callback<observer.DensityInfo>): void

取消监听屏幕像素密度的变化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'densityUpdate'，即屏幕像素密度变化。 |
| callback | Callback<observer.[DensityInfo](js-apis-arkui-observer.md#densityinfo12)> | 否 | 需要被注销的回调函数。若不指定具体的回调函数，则注销该[UIContext](arkts-apis-uicontext-uicontext.md)下所有屏幕像素密度变化事件监听。 |

**示例：**

参考[on('densityUpdate')](arkts-apis-uicontext-uiobserver.md#ondensityupdate12)接口示例。

## on('willDraw')12+

PhonePC/2in1TabletTVWearable

on(type: 'willDraw', callback: Callback<void>): void

监听每一帧绘制指令下发情况。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'willDraw'，即是否将要绘制。 |
| callback | Callback<void> | 是 | 回调函数。 |

**示例：**

```
1. // Index.ets
2. // 演示uiObserver.on('willDraw', callback)
3. // uiObserver.off('willDraw', callback)

5. @Entry
6. @Component
7. struct Index {
8. // 定义监听回调函数
9. willDrawCallback = () => {
10. console.info("willDraw指令下发");
11. }

13. build() {
14. Column() {
15. Button('注册绘制指令下发监听')
16. .margin({ bottom: 10 })
17. .onClick(() => {
18. // 添加监听
19. this.getUIContext().getUIObserver().on('willDraw', this.willDrawCallback);
20. })
21. Button('解除注册绘制指令下发监听')
22. .onClick(() => {
23. // 取消监听
24. this.getUIContext().getUIObserver().off('willDraw', this.willDrawCallback);
25. })
26. }
27. }
28. }
```

## off('willDraw')12+

PhonePC/2in1TabletTVWearable

off(type: 'willDraw', callback?: Callback<void>): void

取消监听每一帧绘制指令下发情况。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'willDraw'，即是否将要绘制。 |
| callback | Callback<void> | 否 | 需要被注销的回调函数。不传参数时，取消所有绘制指令下发事件的监听回调。 |

**示例：**

参考[on('willDraw')](arkts-apis-uicontext-uiobserver.md#onwilldraw12)接口示例。

## on('didLayout')12+

PhonePC/2in1TabletTVWearable

on(type: 'didLayout', callback: Callback<void>): void

监听每一帧布局完成情况。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'didLayout'，即是否布局完成。 |
| callback | Callback<void> | 是 | 回调函数。 |

**示例：**

```
1. // Index.ets
2. // 演示uiObserver.on('didLayout', callback)
3. // uiObserver.off('didLayout', callback)

5. @Entry
6. @Component
7. struct Index {
8. // 定义监听回调函数
9. didLayoutCallback = () => {
10. console.info("layout布局完成");
11. }

13. build() {
14. Column() {
15. Button('注册布局完成监听')
16. .margin({ bottom: 10 })
17. .onClick(() => {
18. // 添加监听
19. this.getUIContext().getUIObserver().on('didLayout', this.didLayoutCallback);
20. })
21. Button('解除注册注册布局完成监听')
22. .onClick(() => {
23. // 取消监听
24. this.getUIContext().getUIObserver().off('didLayout', this.didLayoutCallback);
25. })
26. }
27. }
28. }
```

## off('didLayout')12+

PhonePC/2in1TabletTVWearable

off(type: 'didLayout', callback?: Callback<void>): void

取消监听每一帧布局完成情况。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'didLayout'，即是否布局完成。 |
| callback | Callback<void> | 否 | 需要被注销的回调函数。不传参数时，取消所有布局完成的监听回调。 |

**示例：**

参考[on('didLayout')](arkts-apis-uicontext-uiobserver.md#ondidlayout12)接口示例。

## on('navDestinationSwitch')12+

PhonePC/2in1TabletTVWearable

on(type: 'navDestinationSwitch', callback: Callback<observer.NavDestinationSwitchInfo>): void

监听[Navigation](ts-basic-components-navigation.md)的页面切换事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationSwitch'，即[Navigation](ts-basic-components-navigation.md)的页面切换事件。 |
| callback | Callback<observer.[NavDestinationSwitchInfo](js-apis-arkui-observer.md#navdestinationswitchinfo12)> | 是 | 回调函数。携带[NavDestinationSwitchInfo](js-apis-arkui-observer.md#navdestinationswitchinfo12)，返回页面切换事件的信息。 |

**示例：**

```
1. // Index.ets
2. // 演示UIObserver.on('navDestinationSwitch', callback)
3. // UIObserver.off('navDestinationSwitch', callback)

5. import { uiObserver } from '@kit.ArkUI';

7. @Component
8. struct PageOne {
9. build() {
10. NavDestination() {
11. Text("pageOne")
12. }.title("pageOne")
13. }
14. }

16. // 定义监听回调函数
17. function callbackFunc(info: uiObserver.NavDestinationSwitchInfo) {
18. console.info(`testTag navDestinationSwitch from: ${JSON.stringify(info.from)} to: ${JSON.stringify(info.to)}`);
19. }

21. @Entry
22. @Component
23. struct Index {
24. private stack: NavPathStack = new NavPathStack();

26. @Builder
27. PageBuilder(name: string) {
28. PageOne()
29. }

31. aboutToAppear() {
32. let obs = this.getUIContext().getUIObserver();
33. // 添加监听
34. obs.on('navDestinationSwitch', callbackFunc);
35. }

37. aboutToDisappear() {
38. let obs = this.getUIContext().getUIObserver();
39. // 取消监听
40. obs.off('navDestinationSwitch', callbackFunc);
41. }

43. build() {
44. Column() {
45. Navigation(this.stack) {
46. Button("push").onClick(() => {
47. // 将PageOne的NavDestination入栈
48. this.stack.pushPath({ name: "pageOne" });
49. })
50. }
51. .title("Navigation")
52. .navDestination(this.PageBuilder)
53. }
54. .width('100%')
55. .height('100%')
56. }
57. }
```

## off('navDestinationSwitch')12+

PhonePC/2in1TabletTVWearable

off(type: 'navDestinationSwitch', callback?: Callback<observer.NavDestinationSwitchInfo>): void

取消监听[Navigation](ts-basic-components-navigation.md)的页面切换事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationSwitch'，即[Navigation](ts-basic-components-navigation.md)的页面切换事件。 |
| callback | Callback<observer.[NavDestinationSwitchInfo](js-apis-arkui-observer.md#navdestinationswitchinfo12)> | 否 | 需要被注销的回调函数。不传参数时，取消该[Navigation](ts-basic-components-navigation.md)上所有的监听回调。 |

**示例：**

参考[on('navDestinationSwitch')](arkts-apis-uicontext-uiobserver.md#onnavdestinationswitch12)接口示例。

## on('navDestinationSwitch')12+

PhonePC/2in1TabletTVWearable

on(type: 'navDestinationSwitch', observerOptions: observer.NavDestinationSwitchObserverOptions, callback: Callback<observer.NavDestinationSwitchInfo>): void

通过监听选项监听[Navigation](ts-basic-components-navigation.md)的页面切换事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationSwitch'，即[Navigation](ts-basic-components-navigation.md)的页面切换事件。 |
| observerOptions | observer.[NavDestinationSwitchObserverOptions](js-apis-arkui-observer.md#navdestinationswitchobserveroptions12) | 是 | 监听选项。 |
| callback | Callback<observer.[NavDestinationSwitchInfo](js-apis-arkui-observer.md#navdestinationswitchinfo12)> | 是 | 回调函数。携带[NavDestinationSwitchInfo](js-apis-arkui-observer.md#navdestinationswitchinfo12)，返回页面切换事件的信息。 |

**示例：**

```
1. // Index.ets
2. // 演示UIObserver.on('navDestinationSwitch', observerOptions, callback)
3. // UIObserver.off('navDestinationSwitch', observerOptions, callback)

5. import { uiObserver } from '@kit.ArkUI';

7. @Component
8. struct PageOne {
9. build() {
10. NavDestination() {
11. Text("pageOne")
12. }.title("pageOne")
13. }
14. }

16. // 定义监听回调函数
17. function callbackFunc(info: uiObserver.NavDestinationSwitchInfo) {
18. console.info(`testTag navDestinationSwitch from: ${JSON.stringify(info.from)} to: ${JSON.stringify(info.to)}`);
19. }

21. @Entry
22. @Component
23. struct Index {
24. private stack: NavPathStack = new NavPathStack();

26. @Builder
27. PageBuilder(name: string) {
28. PageOne()
29. }

31. aboutToAppear() {
32. let obs = this.getUIContext().getUIObserver();
33. // 添加监听，指定Navigation的id
34. obs.on('navDestinationSwitch', { navigationId: "myNavId" }, callbackFunc);
35. }

37. aboutToDisappear() {
38. let obs = this.getUIContext().getUIObserver();
39. // 取消监听
40. obs.off('navDestinationSwitch', { navigationId: "myNavId" }, callbackFunc);
41. }

43. build() {
44. Column() {
45. Navigation(this.stack) {
46. Button("push").onClick(() => {
47. // 将PageOne的NavDestination入栈
48. this.stack.pushPath({ name: "pageOne" });
49. })
50. }
51. .id("myNavId")
52. .title("Navigation")
53. .navDestination(this.PageBuilder)
54. }
55. .width('100%')
56. .height('100%')
57. }
58. }
```

## off('navDestinationSwitch')12+

PhonePC/2in1TabletTVWearable

off(type: 'navDestinationSwitch', observerOptions: observer.NavDestinationSwitchObserverOptions, callback?: Callback<observer.NavDestinationSwitchInfo>): void

取消通过监听选项监听[Navigation](ts-basic-components-navigation.md)的页面切换事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'navDestinationSwitch'，即[Navigation](ts-basic-components-navigation.md)的页面切换事件。 |
| observerOptions | observer.[NavDestinationSwitchObserverOptions](js-apis-arkui-observer.md#navdestinationswitchobserveroptions12) | 是 | 监听选项。 |
| callback | Callback<observer.[NavDestinationSwitchInfo](js-apis-arkui-observer.md#navdestinationswitchinfo12)> | 否 | 需要被注销的回调函数。不传参数时，取消该[Navigation](ts-basic-components-navigation.md)上所有的监听回调。 |

**示例：**

参考[on('navDestinationSwitch')](arkts-apis-uicontext-uiobserver.md#onnavdestinationswitch12-1)接口示例。

## on('willClick')12+

PhonePC/2in1TabletTVWearable

on(type: 'willClick', callback: GestureEventListenerCallback): void

监听点击事件指令下发情况，所注册回调将于点击事件触发前触发。回调类型为[GestureEventListenerCallback](arkts-apis-uicontext-t.md#gestureeventlistenercallback12)。从API version 20开始支持屏幕朗读触控模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'willClick'，用于监听点击事件指令下发情况，所注册回调将于点击事件触发前触发。 |
| callback | [GestureEventListenerCallback](arkts-apis-uicontext-t.md#gestureeventlistenercallback12) | 是 | 回调函数。可以获得点击事件的[GestureEvent](ts-gesture-common.md#gestureevent对象说明)和组件的[FrameNode](js-apis-arkui-framenode.md)。 |

**示例：**

```
1. // Index.ets
2. // 演示uiObserver.on('willClick', callback)
3. // uiObserver.off('willClick', callback)
4. // uiObserver.off('didClick', callback)
5. // uiObserver.off('didClick', callback)

7. // 定义监听回调函数
8. function willClickGestureCallback(event: GestureEvent, node?: FrameNode) {
9. console.info('Example willClickCallback GestureEvent is called');
10. }

12. function willClickCallback(event: ClickEvent, node?: FrameNode) {
13. console.info('Example willClickCallback ClickEvent is called');
14. }

16. function didClickGestureCallback(event: GestureEvent, node?: FrameNode) {
17. console.info('Example didClickCallback GestureEvent is called');
18. }

20. function didClickCallback(event: ClickEvent, node?: FrameNode) {
21. console.info('Example didClickCallback ClickEvent is called');
22. }

24. @Entry
25. @Component
26. struct ClickExample {
27. @State clickCount: number = 0;
28. @State tapGestureCount: number = 0;

30. aboutToAppear(): void {
31. // 添加监听
32. let observer = this.getUIContext().getUIObserver();
33. observer.on('willClick', willClickGestureCallback);
34. observer.on('willClick', willClickCallback);
35. observer.on('didClick', didClickGestureCallback);
36. observer.on('didClick', didClickCallback);
37. }

39. aboutToDisappear(): void {
40. // 取消监听
41. let observer = this.getUIContext().getUIObserver();
42. observer.off('willClick', willClickGestureCallback);
43. observer.off('willClick', willClickCallback);
44. // 如果不选择回调，则会取消所有监听的回调
45. observer.off('didClick');
46. }

48. build() {
49. Column() {
50. /**
51. * onClick和TapGesture在后端的处理是一致的
52. * 所以无论是触发onClick还是触发TapGesture
53. * on('willClick')两种类型入参的回调（GestureEvent和ClickEvent）都会被触发
54. * 同理，on('didClick')的两种回调也会被触发
55. */
56. Column() {
57. Text('Click Count: ' + this.clickCount)
58. }
59. .height(200)
60. .width(300)
61. .padding(20)
62. .border({ width: 3 })
63. .margin(50)
64. .onClick((event: ClickEvent) => {
65. this.clickCount++;
66. console.info('Example Click event is called');
67. })

69. Column() {
70. Text('TapGesture Count: ' + this.tapGestureCount)
71. }
72. .height(200)
73. .width(300)
74. .padding(20)
75. .border({ width: 3 })
76. .margin(50)
77. .gesture(TapGesture({ count: 2 }).onAction((event: TapGestureEvent) => {
78. this.tapGestureCount++;
79. console.info('Example Click event is called');
80. }))
81. }
82. }
83. }
```

## off('willClick')12+

PhonePC/2in1TabletTVWearable

off(type: 'willClick', callback?: GestureEventListenerCallback): void

取消监听[on('willClick')](arkts-apis-uicontext-uiobserver.md#onwillclick12)中的点击事件指令下发情况。从API version 20开始，支持屏幕朗读触控模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'willClick'，即点击事件指令下发情况。 |
| callback | [GestureEventListenerCallback](arkts-apis-uicontext-t.md#gestureeventlistenercallback12) | 否 | 需要被注销的回调函数。不传参数时，取消所有的点击事件指令下发监听回调。 |

**示例：**

参考[on('willClick')](arkts-apis-uicontext-uiobserver.md#onwillclick12)接口示例。

## on('didClick')12+

PhonePC/2in1TabletTVWearable

on(type: 'didClick', callback: GestureEventListenerCallback): void

监听点击事件指令下发情况，所注册回调将于点击事件触发后触发。回调类型为[GestureEventListenerCallback](arkts-apis-uicontext-t.md#gestureeventlistenercallback12)。从API version 20开始支持屏幕朗读触控模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'didClick'，用于监听点击事件指令下发情况，所注册回调将于点击事件触发后触发。 |
| callback | [GestureEventListenerCallback](arkts-apis-uicontext-t.md#gestureeventlistenercallback12) | 是 | 回调函数。可以获得点击事件的[GestureEvent](ts-gesture-common.md#gestureevent对象说明)和组件的[FrameNode](js-apis-arkui-framenode.md)。 |

**示例：**

参考[on('willClick')](arkts-apis-uicontext-uiobserver.md#onwillclick12)接口示例。

## off('didClick')12+

PhonePC/2in1TabletTVWearable

off(type: 'didClick', callback?: GestureEventListenerCallback): void

取消监听[on('didClick')](arkts-apis-uicontext-uiobserver.md#ondidclick12)中的点击事件指令下发情况。从API version 20开始，支持屏幕朗读触控模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'didClick'，即点击事件指令下发情况。 |
| callback | [GestureEventListenerCallback](arkts-apis-uicontext-t.md#gestureeventlistenercallback12) | 否 | 需要被注销的回调函数。不传参数时，取消所有的点击事件指令下发监听回调。 |

**示例：**

参考[on('willClick')](arkts-apis-uicontext-uiobserver.md#onwillclick12)接口示例。

## on('willClick')12+

PhonePC/2in1TabletTVWearable

on(type: 'willClick', callback: ClickEventListenerCallback): void

监听点击事件指令下发情况，所注册回调将于点击事件触发前触发。回调类型为[ClickEventListenerCallback](arkts-apis-uicontext-t.md#clickeventlistenercallback12)。从API version 20开始支持屏幕朗读触控模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'willClick'，用于监听点击事件指令下发情况，所注册回调将于点击事件触发前触发。 |
| callback | [ClickEventListenerCallback](arkts-apis-uicontext-t.md#clickeventlistenercallback12) | 是 | 回调函数。可以获得点击事件的[ClickEvent](ts-universal-events-click.md#clickevent)和组件的[FrameNode](js-apis-arkui-framenode.md)。 |

**示例：**

参考[on('willClick')](arkts-apis-uicontext-uiobserver.md#onwillclick12)接口示例。

## off('willClick')12+

PhonePC/2in1TabletTVWearable

off(type: 'willClick', callback?: ClickEventListenerCallback): void

取消监听[on('willClick')](arkts-apis-uicontext-uiobserver.md#onwillclick12-1)中的点击事件指令下发情况。从API version 20开始，支持屏幕朗读触控模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'willClick'，即点击事件指令下发情况。 |
| callback | [ClickEventListenerCallback](arkts-apis-uicontext-t.md#clickeventlistenercallback12) | 否 | 需要被注销的回调函数。不传参数时，取消所有的点击事件指令下发监听回调。 |

**示例：**

参考[on('willClick')](arkts-apis-uicontext-uiobserver.md#onwillclick12)接口示例。

## on('didClick')12+

PhonePC/2in1TabletTVWearable

on(type: 'didClick', callback: ClickEventListenerCallback): void

监听点击事件指令下发情况，所注册回调将于点击事件触发后触发。回调类型为[ClickEventListenerCallback](arkts-apis-uicontext-t.md#clickeventlistenercallback12)。从API version 20开始支持屏幕朗读触控模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'didClick'，用于监听点击事件指令下发情况，所注册回调将于点击事件触发后触发。 |
| callback | [ClickEventListenerCallback](arkts-apis-uicontext-t.md#clickeventlistenercallback12) | 是 | 回调函数。可以获得点击事件的[ClickEvent](ts-universal-events-click.md#clickevent)和组件的[FrameNode](js-apis-arkui-framenode.md)。 |

**示例：**

参考[on('willClick')](arkts-apis-uicontext-uiobserver.md#onwillclick12)接口示例。

## off('didClick')12+

PhonePC/2in1TabletTVWearable

off(type: 'didClick', callback?: ClickEventListenerCallback): void

取消监听[on('didClick')](arkts-apis-uicontext-uiobserver.md#ondidclick12-1)中的点击事件指令下发情况。从API version 20开始，支持屏幕朗读触控模式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'didClick'，即点击事件指令下发情况。 |
| callback | [ClickEventListenerCallback](arkts-apis-uicontext-t.md#clickeventlistenercallback12) | 否 | 需要被注销的回调函数。不传参数时，取消所有的点击事件指令下发监听回调。 |

**示例：**

参考[on('willClick')](arkts-apis-uicontext-uiobserver.md#onwillclick12)接口示例。

## on('tabContentUpdate')12+

PhonePC/2in1TabletTVWearable

on(type: 'tabContentUpdate', callback: Callback<observer.TabContentInfo>): void

监听[TabContent](ts-container-tabcontent.md)页面的切换事件。相比[on('tabChange')](arkts-apis-uicontext-uiobserver.md#ontabchange22)，本接口不支持监听Tabs组件初始化时，显示首个页签的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tabContentUpdate'，即[TabContent](ts-container-tabcontent.md)页面的切换事件。 |
| callback | Callback<observer.[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)> | 是 | 回调函数。携带[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)，返回[TabContent](ts-container-tabcontent.md)页面切换事件的信息。 |

**示例：**

```
1. // Index.ets
2. // 演示uiObserver.on('tabContentUpdate', callback)
3. // uiObserver.off('tabContentUpdate', callback)

5. import { uiObserver } from '@kit.ArkUI';

7. // 定义监听回调函数
8. function callbackFunc(info: uiObserver.TabContentInfo) {
9. console.info('tabContentUpdate', JSON.stringify(info));
10. }

12. @Entry
13. @Component
14. struct TabsExample {

16. aboutToAppear(): void {
17. let observer = this.getUIContext().getUIObserver();
18. // 添加监听
19. observer.on('tabContentUpdate', callbackFunc);
20. }

22. aboutToDisappear(): void {
23. let observer = this.getUIContext().getUIObserver();
24. // 取消监听
25. observer.off('tabContentUpdate', callbackFunc);
26. }

28. build() {
29. Column() {
30. Tabs() {
31. TabContent() {
32. Column().width('100%').height('100%').backgroundColor('#00CB87')
33. }.tabBar('green').id('tabContentId0')

35. TabContent() {
36. Column().width('100%').height('100%').backgroundColor('#007DFF')
37. }.tabBar('blue').id('tabContentId1')

39. TabContent() {
40. Column().width('100%').height('100%').backgroundColor('#FFBF00')
41. }.tabBar('yellow').id('tabContentId2')

43. TabContent() {
44. Column().width('100%').height('100%').backgroundColor('#E67C92')
45. }.tabBar('pink').id('tabContentId3')
46. }
47. .width(360)
48. .height(296)
49. .backgroundColor('#F1F3F5')
50. .id('tabsId')
51. }.width('100%')
52. }
53. }
```

## off('tabContentUpdate')12+

PhonePC/2in1TabletTVWearable

off(type: 'tabContentUpdate', callback?: Callback<observer.TabContentInfo>): void

取消监听[TabContent](ts-container-tabcontent.md)页面的切换事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tabContentUpdate'，即[TabContent](ts-container-tabcontent.md)页面的切换事件。 |
| callback | Callback<observer.[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)> | 否 | 需要被注销的回调函数。不传参数时，取消该[Tabs](ts-container-tabs.md)上所有的监听回调。 |

**示例：**

参考[on('tabContentUpdate')](arkts-apis-uicontext-uiobserver.md#ontabcontentupdate12)接口示例。

## on('tabContentUpdate')12+

PhonePC/2in1TabletTVWearable

on(type: 'tabContentUpdate', options: observer.ObserverOptions, callback: Callback<observer.TabContentInfo>): void

通过[Tabs](ts-container-tabs.md)组件的id监听[TabContent](ts-container-tabcontent.md)页面的切换事件。相比[on('tabChange')](arkts-apis-uicontext-uiobserver.md#ontabchange22-1)，本接口不支持监听Tabs组件初始化时，显示首个页签的事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tabContentUpdate'，即[TabContent](ts-container-tabcontent.md)页面的切换事件。 |
| options | observer.[ObserverOptions](js-apis-arkui-observer.md#observeroptions12) | 是 | 指定监听的[Tabs](ts-container-tabs.md)组件的id。 |
| callback | Callback<observer.[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)> | 是 | 回调函数。携带TabContentInfo，返回[TabContent](ts-container-tabcontent.md)页面切换事件的信息。 |

**示例：**

```
1. // Index.ets
2. // 演示uiObserver.on('tabContentUpdate', options, callback)
3. // uiObserver.off('tabContentUpdate', options, callback)

5. import { uiObserver } from '@kit.ArkUI';

7. // 定义监听回调函数
8. function callbackFunc(info: uiObserver.TabContentInfo) {
9. console.info('tabContentUpdate', JSON.stringify(info));
10. }

12. @Entry
13. @Component
14. struct TabsExample {

16. aboutToAppear(): void {
17. let observer = this.getUIContext().getUIObserver();
18. // 添加监听，指定Tabs的id
19. observer.on('tabContentUpdate', { id: 'tabsId' }, callbackFunc);
20. }

22. aboutToDisappear(): void {
23. let observer = this.getUIContext().getUIObserver();
24. // 取消监听
25. observer.off('tabContentUpdate', { id: 'tabsId' }, callbackFunc);
26. }

28. build() {
29. Column() {
30. Tabs() {
31. TabContent() {
32. Column().width('100%').height('100%').backgroundColor('#00CB87')
33. }.tabBar('green').id('tabContentId0')

35. TabContent() {
36. Column().width('100%').height('100%').backgroundColor('#007DFF')
37. }.tabBar('blue').id('tabContentId1')

39. TabContent() {
40. Column().width('100%').height('100%').backgroundColor('#FFBF00')
41. }.tabBar('yellow').id('tabContentId2')

43. TabContent() {
44. Column().width('100%').height('100%').backgroundColor('#E67C92')
45. }.tabBar('pink').id('tabContentId3')
46. }
47. .width(360)
48. .height(296)
49. .backgroundColor('#F1F3F5')
50. .id('tabsId')
51. }.width('100%')
52. }
53. }
```

## off('tabContentUpdate')12+

PhonePC/2in1TabletTVWearable

off(type: 'tabContentUpdate', options: observer.ObserverOptions, callback?: Callback<observer.TabContentInfo>): void

取消通过[Tabs](ts-container-tabs.md)组件的id监听[TabContent](ts-container-tabcontent.md)页面的切换事件。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tabContentUpdate'，即[TabContent](ts-container-tabcontent.md)页面的切换事件。 |
| options | observer.[ObserverOptions](js-apis-arkui-observer.md#observeroptions12) | 是 | 指定监听的[Tabs](ts-container-tabs.md)组件的id。 |
| callback | Callback<observer.[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)> | 否 | 需要被注销的回调函数。不传参数时，取消该[Tabs](ts-container-tabs.md)上所有的监听回调。 |

**示例：**

参考[on('tabContentUpdate')](arkts-apis-uicontext-uiobserver.md#ontabcontentupdate12-1)接口示例。

## on('tabChange')22+

PhonePC/2in1TabletTVWearable

on(type: 'tabChange', callback: Callback<observer.TabContentInfo>): void

监听[Tabs](ts-container-tabs.md)组件页签的切换事件，支持多个[Tabs](ts-container-tabs.md)组件的监听。相比[on('tabContentUpdate')](arkts-apis-uicontext-uiobserver.md#ontabcontentupdate12)，本接口支持监听Tabs组件初始化时，显示首个页签的事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tabChange'，即[Tabs](ts-container-tabs.md)组件页签的切换事件。 |
| callback | Callback<observer.[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)> | 是 | 回调函数。携带[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)，返回[Tabs](ts-container-tabs.md)组件页签的切换事件的信息。 |

**示例：**

```
1. // Index.ets
2. // 演示监听Tabs组件页签的切换事件。
3. // 此用例同时监听id为'tabsId1'、'tabsId2'的两个Tabs组件。
4. // 两个Tabs组件初始化时，会监听到第0页页签的显示事件，页签对应id分别为'tabContentId0'、'tabContentId5'。
5. // 在id为'tabsId1'的Tabs组件上滑动一下，会监听到第0页的页签隐藏、id为'tabContentId1'的第1页页签显示事件。
6. import { uiObserver } from '@kit.ArkUI';

8. // 定义监听回调函数
9. function callbackFunc(info: uiObserver.TabContentInfo) {
10. console.info('tabChange', JSON.stringify(info));
11. }

13. @Entry
14. @Component
15. struct TabsExample {

17. aboutToAppear(): void {
18. let observer = this.getUIContext().getUIObserver();
19. // 添加监听
20. observer.on('tabChange', callbackFunc);
21. }

23. aboutToDisappear(): void {
24. let observer = this.getUIContext().getUIObserver();
25. // 取消监听
26. observer.off('tabChange', callbackFunc);
27. }

29. build() {
30. Column() {
31. Tabs() {
32. TabContent() {
33. Column().width('100%').height('100%').backgroundColor('#00CB87')
34. }.tabBar('green').id('tabContentId0')

36. TabContent() {
37. Column().width('100%').height('100%').backgroundColor('#007DFF')
38. }.tabBar('blue').id('tabContentId1')

40. TabContent() {
41. Column().width('100%').height('100%').backgroundColor('#FFBF00')
42. }.tabBar('yellow').id('tabContentId2')

44. TabContent() {
45. Column().width('100%').height('100%').backgroundColor('#E67C92')
46. }.tabBar('pink').id('tabContentId3')
47. }
48. .width(360)
49. .height(296)
50. .backgroundColor('#F1F3F5')
51. .id('tabsId1')

53. Tabs() {
54. TabContent() {
55. Column().width('100%').height('100%').backgroundColor('#00CB87')
56. }.tabBar('green').id('tabContentId5')

58. TabContent() {
59. Column().width('100%').height('100%').backgroundColor('#007DFF')
60. }.tabBar('blue').id('tabContentId6')

62. TabContent() {
63. Column().width('100%').height('100%').backgroundColor('#FFBF00')
64. }.tabBar('yellow').id('tabContentId7')

66. TabContent() {
67. Column().width('100%').height('100%').backgroundColor('#E67C92')
68. }.tabBar('pink').id('tabContentId8')
69. }
70. .width(360)
71. .height(296)
72. .backgroundColor('#F1F3F5')
73. .id('tabsId2')
74. }.width('100%')
75. }
76. }
```

## off('tabChange')22+

PhonePC/2in1TabletTVWearable

off(type: 'tabChange', callback?: Callback<observer.TabContentInfo>): void

取消监听所有的[Tabs](ts-container-tabs.md)组件页签的切换事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tabChange'，即[Tabs](ts-container-tabs.md)组件页签的切换事件。 |
| callback | Callback<observer.[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)> | 否 | 需要被注销的回调函数。若不指定具体的回调函数，则注销所有通过[on('tabChange')](arkts-apis-uicontext-uiobserver.md#ontabchange22)接口注册的回调函数。  默认值：undefined |

**示例：**

参考[on('tabChange')](arkts-apis-uicontext-uiobserver.md#ontabchange22)接口示例。

## on('tabChange')22+

PhonePC/2in1TabletTVWearable

on(type: 'tabChange', config: observer.ObserverOptions, callback: Callback<observer.TabContentInfo>): void

监听指定[Tabs](ts-container-tabs.md)组件的页签切换事件。相比[on('tabContentUpdate')](arkts-apis-uicontext-uiobserver.md#ontabcontentupdate12-1)，本接口支持监听Tabs组件初始化时，显示首个页签的事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tabChange'，即[Tabs](ts-container-tabs.md)组件页签的切换事件。 |
| config | observer.[ObserverOptions](js-apis-arkui-observer.md#observeroptions12) | 是 | 指定监听的[Tabs](ts-container-tabs.md)组件的id。 |
| callback | Callback<observer.[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)> | 是 | 回调函数。携带[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)，返回[Tabs](ts-container-tabs.md)组件页签的切换事件的信息。 |

**示例：**

```
1. // Index.ets
2. // 演示监听id为'tabsId'的Tabs组件页签的切换事件。
3. // Tabs组件页签初始化的时候，会监听到第0页页签的显示事件，页签对应id为'tabContentId0'；滑动一下，会监听到第0页的页签隐藏、id为'tabContentId1'的第1页页签显示事件。
4. import { uiObserver } from '@kit.ArkUI';

6. // 定义监听回调函数
7. function callbackFunc(info: uiObserver.TabContentInfo) {
8. console.info('tabChange', JSON.stringify(info));
9. }

11. @Entry
12. @Component
13. struct TabsExample {

15. aboutToAppear(): void {
16. let observer = this.getUIContext().getUIObserver();
17. // 添加监听，指定Tabs的id
18. observer.on('tabChange', { id: 'tabsId' }, callbackFunc);
19. }

21. aboutToDisappear(): void {
22. let observer = this.getUIContext().getUIObserver();
23. // 取消监听
24. observer.off('tabChange', { id: 'tabsId' }, callbackFunc);
25. }

27. build() {
28. Column() {
29. Tabs() {
30. TabContent() {
31. Column().width('100%').height('100%').backgroundColor('#00CB87')
32. }.tabBar('green').id('tabContentId0')

34. TabContent() {
35. Column().width('100%').height('100%').backgroundColor('#007DFF')
36. }.tabBar('blue').id('tabContentId1')

38. TabContent() {
39. Column().width('100%').height('100%').backgroundColor('#FFBF00')
40. }.tabBar('yellow').id('tabContentId2')

42. TabContent() {
43. Column().width('100%').height('100%').backgroundColor('#E67C92')
44. }.tabBar('pink').id('tabContentId3')
45. }
46. .width(360)
47. .height(296)
48. .backgroundColor('#F1F3F5')
49. .id('tabsId')

51. Tabs() {
52. TabContent() {
53. Column().width('100%').height('100%').backgroundColor('#00CB87')
54. }.tabBar('green').id('tabContentId5')

56. TabContent() {
57. Column().width('100%').height('100%').backgroundColor('#007DFF')
58. }.tabBar('blue').id('tabContentId6')

60. TabContent() {
61. Column().width('100%').height('100%').backgroundColor('#FFBF00')
62. }.tabBar('yellow').id('tabContentId7')

64. TabContent() {
65. Column().width('100%').height('100%').backgroundColor('#E67C92')
66. }.tabBar('pink').id('tabContentId8')
67. }
68. .width(360)
69. .height(296)
70. .backgroundColor('#F1F3F5')
71. }.width('100%')
72. }
73. }
```

## off('tabChange')22+

PhonePC/2in1TabletTVWearable

off(type: 'tabChange', config: observer.ObserverOptions, callback?: Callback<observer.TabContentInfo>): void

取消监听指定[Tabs](ts-container-tabs.md)组件页签的切换事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'tabChange'，即[Tabs](ts-container-tabs.md)组件页签的切换事件。 |
| config | observer.[ObserverOptions](js-apis-arkui-observer.md#observeroptions12) | 是 | 指定监听的[Tabs](ts-container-tabs.md)组件的id。 |
| callback | Callback<observer.[TabContentInfo](js-apis-arkui-observer.md#tabcontentinfo12)> | 否 | 需要被注销的回调函数。若不指定具体的回调函数，则注销config指定的[Tabs](ts-container-tabs.md)组件下注册的所有的回调函数。  默认值：undefined |

**示例：**

参考[on('tabChange')](arkts-apis-uicontext-uiobserver.md#ontabchange22-1)接口示例。

## on('textChange')22+

PhonePC/2in1TabletTVWearable

on(type: 'textChange', callback: Callback<observer.TextChangeEventInfo>): void

全局监听输入框文本变化。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'textChange'，表示文本输入的变化。 |
| callback | Callback<observer.[TextChangeEventInfo](js-apis-arkui-observer.md#textchangeeventinfo22)> | 是 | 回调函数，返回文本变化的信息。 |

**示例：**

```
1. import { UIObserver } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct TextUiObserver {
6. observer: UIObserver = this.getUIContext().getUIObserver();
7. build() {
8. Column() {
9. TextArea({ text: "Hello World TextArea" })
10. .width(336)
11. .height(56)
12. .margin({bottom:5})
13. .backgroundColor('#FFFFFF')
14. .id("TestId1")
15. TextInput({ text: "Hello World TextInput" })
16. .width(336)
17. .height(56)
18. .margin({bottom:5})
19. .backgroundColor('#FFFFFF')
20. .id("TestId2")
21. Search({ value: "Hello World Search" })
22. .width(336)
23. .height(56)
24. .margin({bottom:5})
25. .backgroundColor('#FFFFFF')
26. .id("TestId3")
27. Row() {
28. // 开启全局监听
29. Button('UIObserver on')
30. .onClick(() => {
31. this.observer.on('textChange', (info) => {
32. console.info('textChangeInfo', JSON.stringify(info));
33. });
34. })
35. // 关闭全局监听
36. Button('UIObserver off')
37. .onClick(() => {
38. this.observer.off('textChange');
39. })
40. }.margin({bottom:5})
41. // 开启和关闭指定ID的局部监听
42. Row() {
43. Button('UIObserver TestId1 on')
44. .onClick(() => {
45. this.observer.on('textChange', { id: "TestId1" }, (info) => {
46. console.info('textChangeInfo', JSON.stringify(info));
47. });
48. })

50. Button('UIObserver TestId1 off')
51. .onClick(() => {
52. this.observer.off('textChange', { id: "TestId1" });
53. })
54. }.margin({bottom:5})
55. Row() {
56. Button('UIObserver TestId2 on')
57. .onClick(() => {
58. this.observer.on('textChange', { id: "TestId2" }, (info) => {
59. console.info('textChangeInfo', JSON.stringify(info));
60. });
61. })

63. Button('UIObserver TestId2 off')
64. .onClick(() => {
65. this.observer.off('textChange', { id: "TestId2" });
66. })
67. }.margin({bottom:5})
68. Row() {
69. Button('UIObserver TestId3 on')
70. .onClick(() => {
71. this.observer.on('textChange', { id: "TestId3" }, (info) => {
72. console.info('textChangeInfo', JSON.stringify(info));
73. });
74. })

76. Button('UIObserver TestId3 off')
77. .onClick(() => {
78. this.observer.off('textChange', { id: "TestId3" });
79. })
80. }.margin({bottom:5})
81. }.width('100%').height('100%').backgroundColor('#F1F3F5')
82. }
83. }
```

## off('textChange')22+

PhonePC/2in1TabletTVWearable

off(type: 'textChange', callback?: Callback<observer.TextChangeEventInfo>): void

取消输入框文本变化的全局监听。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'textChange'，表示文本输入的变化。 |
| callback | Callback<observer.[TextChangeEventInfo](js-apis-arkui-observer.md#textchangeeventinfo22)> | 否 | 需要被注销的回调函数。不传参数时，取消输入框文本变化的所有全局监听。 |

**示例：**

参考[on('textChange')](arkts-apis-uicontext-uiobserver.md#ontextchange22)示例。

## on('textChange')22+

PhonePC/2in1TabletTVWearable

on(type: 'textChange', identity: observer.ObserverOptions, callback:Callback<observer.TextChangeEventInfo>): void

指定ID输入框文本变化的局部监听。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'textChange'，表示文本输入的变化。 |
| identity | observer.[ObserverOptions](js-apis-arkui-observer.md#observeroptions12) | 是 | 指定监听的文本输入组件的ID。 |
| callback | Callback<observer.[TextChangeEventInfo](js-apis-arkui-observer.md#textchangeeventinfo22)> | 是 | 回调函数。返回文本变化的信息。 |

**示例：**

参考[on('textChange')](arkts-apis-uicontext-uiobserver.md#ontextchange22)示例。

## off('textChange')22+

PhonePC/2in1TabletTVWearable

off(type: 'textChange', identity: observer.ObserverOptions, callback?: Callback<observer.TextChangeEventInfo>): void

取消指定ID输入框文本变化的局部监听。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'textChange'，表示文本输入的变化。 |
| identity | observer.[ObserverOptions](js-apis-arkui-observer.md#observeroptions12) | 是 | 指定监听的文本输入组件的ID。 |
| callback | Callback<observer.[TextChangeEventInfo](js-apis-arkui-observer.md#textchangeeventinfo22)> | 否 | 需要被注销的回调函数。不传参数时，取消指定ID输入框文本变化的所有局部监听。 |

**示例：**

参考[on('textChange')](arkts-apis-uicontext-uiobserver.md#ontextchange22)示例。

## on('beforePanStart')19+

PhonePC/2in1TabletTVWearable

on(type: 'beforePanStart', callback: PanListenerCallback): void

监听Pan手势[onActionStart](ts-basic-gestures-pangesture.md#onactionstart)事件，在[onActionStart](ts-basic-gestures-pangesture.md#onactionstart)事件执行之前执行callback回调。支持手指滑动、鼠标滑动、鼠标滚轮和触摸板拖动，暂不支持屏幕朗读触控模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'beforePanStart'，用于监听Pan手势[onActionStart](ts-basic-gestures-pangesture.md#onactionstart)事件执行前的指令下发情况，所注册回调将于Pan手势[onActionStart](ts-basic-gestures-pangesture.md#onactionstart)事件触发前触发。 |
| callback | [PanListenerCallback](arkts-apis-uicontext-t.md#panlistenercallback19) | 是 | 回调函数。可以获得Pan手势事件的[GestureEvent](ts-gesture-common.md#gestureevent对象说明)，[GestureRecognizer](ts-gesture-common.md#gesturerecognizer12)和组件的[FrameNode](js-apis-arkui-framenode.md)。 |

**示例：**

```
1. // Index.ets
2. // 演示uiObserver.on('beforePanStart', callback)
3. // uiObserver.off('beforePanStart', callback)
4. // uiObserver.on('afterPanStart', callback)
5. // uiObserver.off('afterPanStart', callback)
6. // uiObserver.on('beforePanEnd', callback)
7. // uiObserver.off('beforePanEnd', callback)
8. // uiObserver.on('afterPanEnd', callback)
9. // uiObserver.off('afterPanEnd', callback)

11. // 在页面Component中使用
12. let TEST_TAG: string = 'node';

14. // 定义监听回调函数
15. function callbackFunc() {
16. console.info('on == beforePanStart');
17. }

19. function afterPanCallBack() {
20. console.info('on == afterPanStart');
21. }

23. function beforeEndCallBack() {
24. console.info('on == beforeEnd');
25. }

27. function afterEndCallBack() {
28. console.info('on == afterEnd');
29. }

31. function beforeStartCallBack() {
32. console.info('on == beforeStartCallBack');
33. }

35. function panGestureCallBack(event: GestureEvent, current: GestureRecognizer, node?: FrameNode) {
36. TEST_TAG = 'panGestureEvent';
37. console.info('===' + TEST_TAG + '=== event.repeat is ' + event.repeat);
38. console.info('===' + TEST_TAG + '=== event target is ' + event.target.id);
39. TEST_TAG = 'panGestureCurrent';
40. console.info('===' + TEST_TAG + '=== current.getTag() is ' + current.getTag());
41. TEST_TAG = 'panGestureNode';
42. console.info('===' + TEST_TAG + '=== node?.getId() is ' + node?.getId());
43. }

46. @Entry
47. @Component
48. struct PanExample {
49. @State offsetX: number = 0;
50. @State offsetY: number = 0;
51. @State positionX: number = 0;
52. @State positionY: number = 0;
53. private panOption: PanGestureOptions = new PanGestureOptions({direction: PanDirection.All });

55. aboutToAppear(): void {
56. let observer = this.getUIContext().getUIObserver();
57. // 添加监听
58. observer.on('beforePanStart', callbackFunc);
59. observer.on('beforePanStart', panGestureCallBack);
60. observer.on('beforePanStart', beforeStartCallBack);
61. observer.on('afterPanStart', afterPanCallBack);
62. observer.on('beforePanEnd', beforeEndCallBack);
63. observer.on('afterPanEnd', afterEndCallBack);
64. }

66. aboutToDisappear(): void {
67. let observer = this.getUIContext().getUIObserver();
68. // 取消监听
69. observer.off('beforePanStart', callbackFunc);
70. observer.off('beforePanStart');
71. observer.off('afterPanStart', afterPanCallBack);
72. observer.off('beforePanEnd');
73. observer.off('afterPanEnd');
74. }

76. build() {
77. Column(){
78. Column(){
79. Text('PanGesture :\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
80. }
81. .height(200)
82. .width(300)
83. .padding(20)
84. .border({ width: 3 })
85. .margin(50)
86. .translate({ x: this.offsetX, y: this.offsetY, z: 0 })
87. .id('columnOuter')
88. .gesture(
89. PanGesture(this.panOption)
90. .onActionStart((event: GestureEvent) => {
91. console.info('Pan start');
92. })
93. .onActionUpdate((event: GestureEvent) => {
94. if (event) {
95. this.offsetX = this.positionX + event.offsetX;
96. this.offsetY = this.positionY + event.offsetY;
97. }
98. })
99. .onActionEnd((event: GestureEvent) => {
100. this.positionX = this.offsetX;
101. this.positionY = this.offsetY;
102. console.info('Pan end');
103. }))
104. }
105. }
106. }
```

## off('beforePanStart')19+

PhonePC/2in1TabletTVWearable

off(type: 'beforePanStart', callback?: PanListenerCallback): void

取消[on('beforePanStart')](arkts-apis-uicontext-uiobserver.md#onbeforepanstart19)监听Pan手势[onActionStart](ts-basic-gestures-pangesture.md#onactionstart)事件执行前的callback回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'beforePanStart'，即Pan手势[onActionStart](ts-basic-gestures-pangesture.md#onactionstart)事件执行前的指令下发情况。 |
| callback | [PanListenerCallback](arkts-apis-uicontext-t.md#panlistenercallback19) | 否 | 需要被注销的回调函数。不传参数时，取消所有的Pan手势[onActionStart](ts-basic-gestures-pangesture.md#onactionstart)事件执行前的指令下发监听回调。 |

**示例：**

参考[on('beforePanStart')](arkts-apis-uicontext-uiobserver.md#onbeforepanstart19)接口示例。

## on('afterPanStart')19+

PhonePC/2in1TabletTVWearable

on(type: 'afterPanStart', callback: PanListenerCallback): void

监听Pan手势[onActionStart](ts-basic-gestures-pangesture.md#onactionstart)事件执行后的指令下发情况，在[onActionStart](ts-basic-gestures-pangesture.md#onactionstart)事件执行之后执行callback回调。支持手指滑动、鼠标滑动、鼠标滚轮和触摸板拖动，暂不支持屏幕朗读触控模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'afterPanStart'，用于监听Pan手势[onActionStart](ts-basic-gestures-pangesture.md#onactionstart)事件执行后的指令下发情况，所注册回调将于Pan手势[onActionStart](ts-basic-gestures-pangesture.md#onactionstart)事件触发后触发。 |
| callback | [PanListenerCallback](arkts-apis-uicontext-t.md#panlistenercallback19) | 是 | 回调函数。可以获得Pan手势事件的[GestureEvent](ts-gesture-common.md#gestureevent对象说明)，[GestureRecognizer](ts-gesture-common.md#gesturerecognizer12)和组件的[FrameNode](js-apis-arkui-framenode.md)。 |

**示例：**

参考[on('beforePanStart')](arkts-apis-uicontext-uiobserver.md#onbeforepanstart19)接口示例。

## off('afterPanStart')19+

PhonePC/2in1TabletTVWearable

off(type: 'afterPanStart', callback?: PanListenerCallback): void

取消[on('afterPanStart')](arkts-apis-uicontext-uiobserver.md#onafterpanstart19)监听Pan手势[onActionStart](ts-basic-gestures-pangesture.md#onactionstart)事件执行后的callback回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'afterPanStart'，即Pan手势[onActionStart](ts-basic-gestures-pangesture.md#onactionstart)事件执行后的指令下发情况。 |
| callback | [PanListenerCallback](arkts-apis-uicontext-t.md#panlistenercallback19) | 否 | 需要被注销的回调函数。不传参数时，取消所有的Pan手势[onActionStart](ts-basic-gestures-pangesture.md#onactionstart)事件执行后的指令下发监听回调。 |

**示例：**

参考[on('beforePanStart')](arkts-apis-uicontext-uiobserver.md#onbeforepanstart19)接口示例。

## on('beforePanEnd')19+

PhonePC/2in1TabletTVWearable

on(type: 'beforePanEnd', callback: PanListenerCallback): void

监听Pan手势[onActionEnd](ts-basic-gestures-pangesture.md#onactionend)事件执行前的指令下发情况，在[onActionEnd](ts-basic-gestures-pangesture.md#onactionend)事件执行之前执行callback回调。支持手指滑动、鼠标滑动、鼠标滚轮和触摸板拖动，暂不支持屏幕朗读触控模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'beforePanEnd'，用于监听Pan手势[onActionEnd](ts-basic-gestures-pangesture.md#onactionend)事件执行前的指令下发情况，所注册回调将于Pan手势[onActionEnd](ts-basic-gestures-pangesture.md#onactionend)事件触发前触发。 |
| callback | [PanListenerCallback](arkts-apis-uicontext-t.md#panlistenercallback19) | 是 | 回调函数。可以获得Pan手势事件的[GestureEvent](ts-gesture-common.md#gestureevent对象说明)，[GestureRecognizer](ts-gesture-common.md#gesturerecognizer12)和组件的[FrameNode](js-apis-arkui-framenode.md)。 |

**示例：**

参考[on('beforePanStart')](arkts-apis-uicontext-uiobserver.md#onbeforepanstart19)接口示例。

## off('beforePanEnd')19+

PhonePC/2in1TabletTVWearable

off(type: 'beforePanEnd', callback?: PanListenerCallback): void

取消[on('beforePanEnd')](arkts-apis-uicontext-uiobserver.md#onbeforepanend19)监听Pan手势[onActionEnd](ts-basic-gestures-pangesture.md#onactionend)事件执行前的callback回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'beforePanEnd'，即Pan手势[onActionEnd](ts-basic-gestures-pangesture.md#onactionend)事件执行前的指令下发情况。 |
| callback | [PanListenerCallback](arkts-apis-uicontext-t.md#panlistenercallback19) | 否 | 需要被注销的回调函数。不传参数时，取消所有的Pan手势[onActionEnd](ts-basic-gestures-pangesture.md#onactionend)事件执行前的指令下发监听回调。 |

**示例：**

参考[on('beforePanStart')](arkts-apis-uicontext-uiobserver.md#onbeforepanstart19)接口示例。

## on('afterPanEnd')19+

PhonePC/2in1TabletTVWearable

on(type: 'afterPanEnd', callback: PanListenerCallback): void

监听Pan手势[onActionEnd](ts-basic-gestures-pangesture.md#onactionend)事件执行后的指令下发情况，在[onActionEnd](ts-basic-gestures-pangesture.md#onactionend)事件执行之后执行callback回调。支持手指滑动、鼠标滑动、鼠标滚轮和触摸板拖动，暂不支持屏幕朗读触控模式。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'beforePanEnd'，用于监听Pan手势[onActionEnd](ts-basic-gestures-pangesture.md#onactionend)事件执行后的指令下发情况，所注册回调将于Pan手势[onActionEnd](ts-basic-gestures-pangesture.md#onactionend)事件触发后触发。 |
| callback | [PanListenerCallback](arkts-apis-uicontext-t.md#panlistenercallback19) | 是 | 回调函数。可以获得Pan手势事件的[GestureEvent](ts-gesture-common.md#gestureevent对象说明)，[GestureRecognizer](ts-gesture-common.md#gesturerecognizer12)和组件的[FrameNode](js-apis-arkui-framenode.md)。 |

**示例：**

参考[on('beforePanStart')](arkts-apis-uicontext-uiobserver.md#onbeforepanstart19)接口示例。

## off('afterPanEnd')19+

PhonePC/2in1TabletTVWearable

off(type: 'afterPanEnd', callback?: PanListenerCallback): void

取消[on('afterPanEnd')](arkts-apis-uicontext-uiobserver.md#onafterpanend19)监听Pan手势[onActionEnd](ts-basic-gestures-pangesture.md#onactionend)事件执行后的callback回调。

**元服务API：** 从API version 19开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'afterPanEnd'，即Pan手势[onActionEnd](ts-basic-gestures-pangesture.md#onactionend)事件执行后的指令下发情况。 |
| callback | [PanListenerCallback](arkts-apis-uicontext-t.md#panlistenercallback19) | 否 | 需要被注销的回调函数。不传参数时，取消所有的Pan手势[onActionEnd](ts-basic-gestures-pangesture.md#onactionend)事件执行后的指令下发监听回调。 |

**示例：**

参考[on('beforePanStart')](arkts-apis-uicontext-uiobserver.md#onbeforepanstart19)接口示例。

## on('nodeRenderState')20+

PhonePC/2in1TabletTVWearable

on(type: 'nodeRenderState', nodeIdentity: NodeIdentity, callback: NodeRenderStateChangeCallback): void

注册一个回调函数，以便在特定节点的渲染状态发生变化时调用，当注册成功时，此回调将立即执行一次。

注意节点数量的限制。出于性能考虑，在单个UI实例中，注册节点太多，将会抛出异常。

通常，当组件被移动到屏幕外时，会收到RENDER\_OUT的通知。但在某些情况下，即使组件移动到屏幕外也不会触发RENDER\_OUT通知。例如，具有缓存功能的组件[Swiper](ts-container-swiper.md)，即使[cachedCount](ts-container-swiper.md#cachedcount15)属性中的参数isShown配置为true，也不会触发RENDER\_OUT通知。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'nodeRenderState'，用于监听节点渲染状态发生改变。 |
| nodeIdentity | [NodeIdentity](arkts-apis-uicontext-t.md#nodeidentity20) | 是 | 节点标识。 |
| callback | [NodeRenderStateChangeCallback](arkts-apis-uicontext-t.md#noderenderstatechangecallback20) | 是 | 回调函数。可以获得节点渲染状态改变事件的[NodeRenderState](arkts-apis-uicontext-e.md#noderenderstate20)和组件的[FrameNode](js-apis-arkui-framenode.md)。 |

**错误码：**

以下错误码的详细介绍请参见[注册节点渲染状态监听错误码](errorcode-node-render-monitor.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 161001 | The count of nodes monitoring render state is over the limitation. |

**示例：**

该示例展示了如何对目标组件添加监听和取消监听。当向左滑动，被监听组件从屏幕消失，会收到RENDER\_OUT的通知，然后向右滑动，被监听组件重新出现在屏幕上，会收到RENDER\_IN通知。

```
1. // Index.ets
2. // 演示uiObserver.on('nodeRenderState', nodeIdentity, callback)
3. // uiObserver.off('nodeRenderState', nodeIdentity, callback)

5. // 在页面Component中使用
6. import { NodeRenderState } from '@kit.ArkUI';

8. @Entry
9. @Component
10. struct Index {
11. @State fontColor: string = '#182431';
12. @State selectedFontColor: string = '#007DFF';
13. @State currentIndex: number = 0;
14. @State selectedIndex: number = 0;
15. @State notice: string = "";
16. private controller: TabsController = new TabsController();

18. @Builder
19. tabBuilder(index: number, name: string) {
20. Column() {
21. Text(name)
22. .fontColor(this.selectedIndex === index ? this.selectedFontColor : this.fontColor)
23. .fontSize(16)
24. .fontWeight(this.selectedIndex === index ? 500 : 400)
25. .lineHeight(22)
26. .margin({ top: 17, bottom: 7 })
27. Divider()
28. .strokeWidth(2)
29. .color('#007DFF')
30. .opacity(this.selectedIndex === index ? 1 : 0)
31. }.width('100%')
32. }

34. build() {
35. Column() {
36. Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
37. TabContent() {
38. Column() {
39. Column() {
40. Button("被监听节点").margin({ top: 5 }).id("button_1")
41. Button("添加监听").margin({ top: 5 }).onClick(() => {
42. let node: FrameNode | null = this.getUIContext().getFrameNodeById("button_1");
43. if (node) {
44. let observer = this.getUIContext().getUIObserver();
45. // 添加监听
46. observer.on("nodeRenderState", node?.getUniqueId(), (state: NodeRenderState, node?: FrameNode) => {
47. // 根据节点状态修改通知信息
48. if (state === 0) {
49. this.notice = "RENDER_IN";
50. } else {
51. this.notice = "RENDER_OUT";
52. }
53. console.info("节点状态发生改变，当前状态：", state);
54. })
55. }
56. })
57. Button("取消监听").margin({ top: 5 }).onClick(() => {
58. let node: FrameNode | null = this.getUIContext().getFrameNodeById("button_1");
59. if (node) {
60. let observer = this.getUIContext().getUIObserver();
61. // 取消监听，不选择回调时，取消所有监听的回调
62. observer.off("nodeRenderState", node?.getUniqueId());
63. }
64. this.notice = "";
65. })
66. }
67. }.width('100%').height('100%').backgroundColor('#00CB87')
68. }.tabBar(this.tabBuilder(0, 'green'))

70. TabContent() {
71. Column().width('100%').height('100%').backgroundColor('#007DFF')
72. }.tabBar(this.tabBuilder(1, 'blue'))

74. TabContent() {
75. Column().width('100%').height('100%').backgroundColor('#FFBF00')
76. }.tabBar(this.tabBuilder(2, 'yellow'))

78. TabContent() {
79. Column().width('100%').height('100%').backgroundColor('#E67C92')
80. }.tabBar(this.tabBuilder(3, 'pink'))
81. }
82. .vertical(false)
83. .barMode(BarMode.Fixed)
84. .barWidth(360)
85. .barHeight(56)
86. .animationDuration(400)
87. .onChange((index: number) => {
88. this.currentIndex = index;
89. this.selectedIndex = index;
90. })
91. .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
92. if (index === targetIndex) {
93. return;
94. }
95. this.selectedIndex = targetIndex;
96. })
97. .width(360)
98. .height(296)
99. .margin({ top: 52 })
100. .backgroundColor('#F1F3F5')

102. Text(`收到的通知: ${this.notice}`)
103. .fontSize(20)
104. .margin(10)
105. }.width('100%')
106. }
107. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/HSrQi_3URlaabTO6WeyqFQ/zh-cn_image_0000002558606280.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055037Z&HW-CC-Expire=86400&HW-CC-Sign=8AB40DDB9BC530B04D4D3D861B0715488F4E6C963785C6514C751B4026ECD5CC)

## off('nodeRenderState')20+

PhonePC/2in1TabletTVWearable

off(type: 'nodeRenderState', nodeIdentity: NodeIdentity, callback?: NodeRenderStateChangeCallback): void

取消监听节点渲染状态发生变化的callback回调。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'nodeRenderState'，即节点渲染状态变化指令下发情况。 |
| nodeIdentity | [NodeIdentity](arkts-apis-uicontext-t.md#nodeidentity20) | 是 | 节点标识。 |
| callback | [NodeRenderStateChangeCallback](arkts-apis-uicontext-t.md#noderenderstatechangecallback20) | 否 | 需要被注销的回调函数。不传参数时，取消该节点所有的渲染状态变化指令下发监听回调。 |

**示例：**

参考[on('nodeRenderState')](arkts-apis-uicontext-uiobserver.md#onnoderenderstate20)接口示例。

## addGlobalGestureListener20+

PhonePC/2in1TabletTVWearable

addGlobalGestureListener(type: GestureListenerType, option: GestureObserverConfigs, callback: GestureListenerCallback): void

注册回调函数以监听手势触发信息。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [GestureListenerType](arkts-apis-uicontext-e.md#gesturelistenertype20) | 是 | 要监听的手势类型。 |
| option | [GestureObserverConfigs](arkts-apis-uicontext-i.md#gestureobserverconfigs20) | 是 | 绑定全局监听器时的配置选项。 |
| callback | [GestureListenerCallback](arkts-apis-uicontext-t.md#gesturelistenercallback20) | 是 | 手势状态更新时的回调函数。 |

**示例：**

该示例使用全局手势监听器实时追踪Tap、Pan和LongPress三个独立区域的触发状态，记录各手势的触发次数和最后操作信息，并在组件生命周期内自动管理监听器的注册与注销。

```
1. // Index.ets
2. // 演示uiObserver.addGlobalGestureListener(type, option, callback)
3. // uiObserver.removeGlobalGestureListener(type, callback)

5. import { GestureListenerType, GestureActionPhase, GestureTriggerInfo, GestureListenerCallback } from '@kit.ArkUI';

7. @Entry
8. @Component
9. struct Index {
10. @State message: string = '全局手势监控';
11. @State tapCount: number = 0;
12. @State panCount: number = 0;
13. @State longPressCount: number = 0;
14. @State lastAction: string = '无';
15. @State lastArea: string = '无';

17. // 存储监听器回调引用
18. private tapCallback?: GestureListenerCallback;
19. private panCallback?: GestureListenerCallback;
20. private longPressCallback?: GestureListenerCallback;

22. // 启用全局监听
23. aboutToAppear() {
24. this.addGlobalListeners();
25. }
26. // 终止全局监听
27. aboutToDisappear() {
28. this.removeGlobalListeners();
29. }

31. private addGlobalListeners() {
32. const observer = this.getUIContext().getUIObserver();

34. // Tap监听任务
35. this.tapCallback = (info: GestureTriggerInfo) => {
36. if (info.event?.target?.id === 'tap-area') {
37. this.tapCount++;
38. this.lastAction = '点击';
39. this.lastArea = 'Tap区域';
40. }
41. };
42. observer.addGlobalGestureListener(
43. GestureListenerType.TAP,
44. { actionPhases: [GestureActionPhase.WILL_START, GestureActionPhase.WILL_END] },
45. this.tapCallback
46. );

48. // Pan监听任务
49. this.panCallback = (info: GestureTriggerInfo) => {
50. if (info.event?.target?.id === 'pan-area') {
51. this.panCount++;
52. this.lastAction = '平移';
53. this.lastArea = 'Pan区域';
54. }
55. };
56. observer.addGlobalGestureListener(
57. GestureListenerType.PAN,
58. {
59. actionPhases: [GestureActionPhase.WILL_START, GestureActionPhase.WILL_END]
60. },
61. this.panCallback
62. );

64. // LongPress监听任务
65. this.longPressCallback = (info: GestureTriggerInfo) => {
66. if (info.event?.target?.id === 'longpress-area') {
67. this.longPressCount++;
68. this.lastAction = '长按';
69. this.lastArea = 'LongPress区域';
70. }
71. };
72. observer.addGlobalGestureListener(
73. GestureListenerType.LONG_PRESS,
74. {
75. actionPhases: [GestureActionPhase.WILL_START, GestureActionPhase.WILL_END]
76. },
77. this.longPressCallback
78. );
79. }

81. private removeGlobalListeners() {
82. const observer = this.getUIContext().getUIObserver();
83. if (this.tapCallback) {
84. observer.removeGlobalGestureListener(0, this.tapCallback);
85. }
86. if (this.panCallback) {
87. observer.removeGlobalGestureListener(2, this.panCallback);
88. }
89. if (this.longPressCallback) {
90. observer.removeGlobalGestureListener(1, this.longPressCallback);
91. }
92. }

94. build() {
95. Column() {
96. // 手势数据统计面板
97. Row({ space: 30 }) {
98. Column() {
99. Text('点击次数:').fontSize(16)
100. Text(`${this.tapCount}`).fontSize(24).fontColor('#FF6B81')
101. }
102. Column() {
103. Text('平移次数:').fontSize(16)
104. Text(`${this.panCount}`).fontSize(24).fontColor('#7BED9F')
105. }
106. Column() {
107. Text('长按次数:').fontSize(16)
108. Text(`${this.longPressCount}`).fontSize(24).fontColor('#70A1FF')
109. }
110. }
111. .margin(10)

113. Text(`最后动作: ${this.lastAction} (${this.lastArea})`)
114. .fontSize(18)
115. .margin(10)

117. // 手势区域
118. Row() {
119. Text('Tap区域').fontSize(18)
120. }
121. .id('tap-area')
122. .width('90%')
123. .height(120)
124. .margin(10)
125. .border({ width: 2, color: '#FF6B81' })
126. .justifyContent(FlexAlign.Center)
127. .gesture(TapGesture().onAction((event: GestureEvent)=>{
128. // 具体实现内容
129. }))

131. Row() {
132. Text('Pan区域').fontSize(18)
133. }
134. .id('pan-area')
135. .width('90%')
136. .height(120)
137. .margin(10)
138. .border({ width: 2, color: '#7BED9F' })
139. .justifyContent(FlexAlign.Center)
140. .gesture(
141. PanGesture()
142. .onActionStart((event: GestureEvent) => {
143. // 具体实现内容
144. })
145. .onActionEnd((event: GestureEvent) => {
146. // 具体实现内容
147. })
148. )

150. Row() {
151. Text('LongPress区域').fontSize(18)
152. }
153. .id('longpress-area')
154. .width('90%')
155. .height(120)
156. .margin(10)
157. .border({ width: 2, color: '#70A1FF' })
158. .justifyContent(FlexAlign.Center)
159. .gesture(
160. LongPressGesture()
161. .onAction((event: GestureEvent)=>{
162. // 具体实现内容
163. })
164. .onActionEnd((event: GestureEvent) => {
165. // 具体实现内容
166. })
167. )
168. }
169. .width('100%')
170. .height('100%')
171. }
172. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/p9EmvYlXRXS_2MjgRSt1iw/zh-cn_image_0000002589325807.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055037Z&HW-CC-Expire=86400&HW-CC-Sign=78BC69C58A53D34010360BCFC832A25F927F4498D57F0558B41DA925619E24C7)

## removeGlobalGestureListener20+

PhonePC/2in1TabletTVWearable

removeGlobalGestureListener(type: GestureListenerType, callback?: GestureListenerCallback): void

移除某一手势监听器类型的回调函数。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | [GestureListenerType](arkts-apis-uicontext-e.md#gesturelistenertype20) | 是 | 要移除监听器的事件类型。 |
| callback | [GestureListenerCallback](arkts-apis-uicontext-t.md#gesturelistenercallback20) | 否 | 待移除的回调函数（未提供时将清除该手势类型的所有回调）。 |

**示例：**

参考[addGlobalGestureListener](arkts-apis-uicontext-uiobserver.md#addglobalgesturelistener20)接口示例。

## on('windowSizeLayoutBreakpointChange')22+

PhonePC/2in1TabletTVWearable

on(type: 'windowSizeLayoutBreakpointChange', callback: Callback<observer.WindowSizeLayoutBreakpointInfo>): void

注册窗口尺寸布局断点变化的回调函数。该方法用于监听窗口尺寸断点变化，可用于根据窗口尺寸自适应调整UI布局。使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowSizeLayoutBreakpointChange'，用于监听窗口尺寸布局断点发生改变。 |
| callback | Callback<observer.[WindowSizeLayoutBreakpointInfo](js-apis-arkui-observer.md#windowsizelayoutbreakpointinfo22)> | 是 | 回调函数。携带WindowSizeLayoutBreakpointinfo，包含窗口宽度和高度所在的布局断点枚举。 |

**示例：**

该示例展示添加和取消监听窗口尺寸布局断点变化的方法。

```
1. import { uiObserver, window } from '@kit.ArkUI';
2. import { common } from '@kit.AbilityKit';

4. @Entry
5. @Component
6. struct Index {
7. private changeOrientation(isLandscape: boolean) {
8. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
9. window.getLastWindow(context).then((lastWindow) => {
10. lastWindow.setPreferredOrientation(isLandscape ? window.Orientation.LANDSCAPE : window.Orientation.PORTRAIT)
11. });
12. }

14. @State message: string = '';
15. @State widthBreakpoint: WidthBreakpoint = WidthBreakpoint.WIDTH_SM;
16. @State heightBreakpoint: HeightBreakpoint = HeightBreakpoint.HEIGHT_SM;
17. winSizeLayoutBreakpointCallback = (info: uiObserver.WindowSizeLayoutBreakpointInfo) => {
18. this.widthBreakpoint = info.widthBreakpoint;
19. this.heightBreakpoint = info.heightBreakpoint;
20. this.message = 'widthBpt:' + this.widthBreakpoint.toString() + 'heightBpt:' + this.heightBreakpoint.toString();
21. }

23. build() {
24. Column() {
25. Text(this.message)
26. Button('注册窗口尺寸布局断点变化监听')
27. .onClick(() => {
28. this.getUIContext()
29. .getUIObserver()
30. .on('windowSizeLayoutBreakpointChange', this.winSizeLayoutBreakpointCallback);
31. })
32. Button('解除窗口尺寸布局断点变化监听')
33. .onClick(() => {
34. this.getUIContext()
35. .getUIObserver()
36. .off('windowSizeLayoutBreakpointChange', this.winSizeLayoutBreakpointCallback);
37. })
38. Button("竖屏").onClick(() => {
39. this.changeOrientation(false)
40. })
41. Button("横屏").onClick(() => {
42. this.changeOrientation(true)
43. })
44. }
45. }
46. }
```

## off('windowSizeLayoutBreakpointChange')22+

PhonePC/2in1TabletTVWearable

off(type: 'windowSizeLayoutBreakpointChange', callback?: Callback<observer.WindowSizeLayoutBreakpointInfo>): void

移除之前注册的窗口尺寸布局断点变化回调函数。如果未提供回调函数参数，将移除指定上下文的所有回调函数。使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| type | string | 是 | 监听事件，固定为'windowSizeLayoutBreakpointChange'，用于监听窗口尺寸布局断点发生改变。 |
| callback | Callback<observer.[WindowSizeLayoutBreakpointInfo](js-apis-arkui-observer.md#windowsizelayoutbreakpointinfo22)> | 否 | 需要被注销的回调函数。若不指定具体的回调函数，则注销该[UIContext](arkts-apis-uicontext-uicontext.md)下所有窗口尺寸布局断点变化事件监听。 |

**示例：**

参考[on('windowSizeLayoutBreakpointChange')](arkts-apis-uicontext-uiobserver.md#onwindowsizelayoutbreakpointchange22)接口示例。

## onSwiperContentUpdate22+

PhonePC/2in1TabletTVWearable

onSwiperContentUpdate(callback: Callback<SwiperContentInfo>): void

监听Swiper内容的切换事件。使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[SwiperContentInfo](arkts-apis-uicontext-i.md#swipercontentinfo22)> | 是 | 回调函数。携带SwiperContentInfo，返回Swiper内容切换的信息。 |

**示例：**

```
1. // Index.ets
2. import { SwiperContentInfo } from '@kit.ArkUI';

4. // 定义监听回调函数
5. function callbackFunc(info: SwiperContentInfo) {
6. console.info('swiperContentUpdate', JSON.stringify(info));
7. }

9. @Entry
10. @Component
11. struct SwiperExample {
12. private swiperController: SwiperController = new SwiperController();

14. aboutToAppear(): void {
15. // 注册swiperContentUpdate监听回调
16. this.getUIContext().getUIObserver().onSwiperContentUpdate(callbackFunc);
17. }

19. aboutToDisappear(): void {
20. // 取消swiperContentUpdate监听回调
21. this.getUIContext().getUIObserver().offSwiperContentUpdate(callbackFunc);
22. }

24. build() {
25. Column({ space: 5 }) {
26. Swiper(this.swiperController) {
27. Column() {
28. Text("SwiperItem1")
29. }.width('100%').height('100%').backgroundColor('#00CB87')

31. Column() {
32. Text("SwiperItem2")
33. }.width('100%').height('100%').backgroundColor('#007DFF')

35. Column() {
36. Text("SwiperItem3")
37. }.width('100%').height('100%').backgroundColor('#FFBF00')

39. Column() {
40. Text("SwiperItem4")
41. }.width('100%').height('100%').backgroundColor('#E67C92')
42. }
43. .width(360)
44. .height(300)
45. }.width('100%')
46. }
47. }
```

## offSwiperContentUpdate22+

PhonePC/2in1TabletTVWearable

offSwiperContentUpdate(callback?: Callback<SwiperContentInfo>): void

取消监听Swiper内容的切换事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<[SwiperContentInfo](arkts-apis-uicontext-i.md#swipercontentinfo22)> | 否 | 需要被注销的回调函数。不传参数时，取消该Swiper上所有的监听回调。 |

**示例：**

参考[onSwiperContentUpdate](arkts-apis-uicontext-uiobserver.md#onswipercontentupdate22)接口示例。

## onSwiperContentUpdate22+

PhonePC/2in1TabletTVWearable

onSwiperContentUpdate(config: observer.ObserverOptions, callback: Callback<SwiperContentInfo>): void

通过Swiper组件的id监听Swiper内容的切换事件。使用callback异步回调。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | observer.[ObserverOptions](js-apis-arkui-observer.md#observeroptions12) | 是 | 指定监听的Swiper组件信息。 |
| callback | Callback<[SwiperContentInfo](arkts-apis-uicontext-i.md#swipercontentinfo22)> | 是 | 回调函数。携带SwiperContentInfo，返回Swiper内容切换的信息。 |

**示例：**

```
1. // Index.ets
2. import { SwiperContentInfo } from '@kit.ArkUI';

4. // 定义监听回调函数
5. function callbackFunc(info: SwiperContentInfo) {
6. console.info('swiperContentUpdate', JSON.stringify(info));
7. }

9. @Entry
10. @Component
11. struct SwiperExample {
12. private swiperController: SwiperController = new SwiperController();

14. aboutToAppear(): void {
15. // 通过id注册swiperContentUpdate监听回调
16. this.getUIContext().getUIObserver().onSwiperContentUpdate({ id: 'swiperId' }, callbackFunc);
17. }

19. aboutToDisappear(): void {
20. // 通过id取消swiperContentUpdate监听回调
21. this.getUIContext().getUIObserver().offSwiperContentUpdate({ id: 'swiperId' }, callbackFunc);
22. }

24. build() {
25. Column({ space: 5 }) {
26. Swiper(this.swiperController) {
27. Column() {
28. Text("SwiperItem1")
29. }.width('100%').height('100%').backgroundColor('#00CB87')

31. Column() {
32. Text("SwiperItem2")
33. }.width('100%').height('100%').backgroundColor('#007DFF')

35. Column() {
36. Text("SwiperItem3")
37. }.width('100%').height('100%').backgroundColor('#FFBF00')

39. Column() {
40. Text("SwiperItem4")
41. }.width('100%').height('100%').backgroundColor('#E67C92')
42. }
43. .id("swiperId")
44. .width(360)
45. .height(300)
46. }.width('100%')
47. }
48. }
```

## offSwiperContentUpdate22+

PhonePC/2in1TabletTVWearable

offSwiperContentUpdate(config: observer.ObserverOptions, callback?: Callback<SwiperContentInfo>): void

取消通过Swiper组件id监听的Swiper内容切换事件。

**元服务API：** 从API version 22开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| config | observer.[ObserverOptions](js-apis-arkui-observer.md#observeroptions12) | 是 | 指定监听的Swiper组件信息。 |
| callback | Callback<[SwiperContentInfo](arkts-apis-uicontext-i.md#swipercontentinfo22)> | 否 | 需要被注销的回调函数。不传参数时，取消该Swiper上所有的监听回调。 |

**示例：**

参考[onSwiperContentUpdate](arkts-apis-uicontext-uiobserver.md#onswipercontentupdate22-1)接口示例。

## onRouterPageSizeChange23+

PhonePC/2in1TabletTVWearable

onRouterPageSizeChange(callback: Callback<observer.RouterPageInfo>): void

注册监听回调函数，当可见的Router页面大小发生变化时，会触发该回调函数。使用callback异步回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<observer.[RouterPageInfo](js-apis-arkui-observer.md#routerpageinfo)> | 是 | 回调函数。携带RouterPageInfo，返回Router页面的信息。 |

**示例：**

```
1. import { uiObserver } from '@kit.ArkUI';

3. function myPageRouterPageSizeCallback(info: uiObserver.RouterPageInfo): void {
4. console.info(`testTag pageSize changeTo ${(info && info.size) ? JSON.stringify(info.size) : 'NA'}`);
5. }

7. @Entry
8. @Component
9. struct QueryRouterPageSize {
10. aboutToAppear(): void {
11. // 可以通过注册监听的方式获取页面大小信息
12. this.getUIContext().getUIObserver().onRouterPageSizeChange(myPageRouterPageSizeCallback);
13. }

15. aboutToDisappear(): void {
16. this.getUIContext().getUIObserver().offRouterPageSizeChange(myPageRouterPageSizeCallback);
17. }

19. build() {
20. Column() {
21. Button('querySize').onClick(() => {
22. // 也可以主动获取页面大小信息
23. let info = this.queryRouterPageInfo();
24. console.info(`testTag pageSize: ${info && info.size ? JSON.stringify(info.size) : "NA"}`)
25. })
26. }
27. .width('100%')
28. .height('100%')
29. }
30. }
```

## offRouterPageSizeChange23+

PhonePC/2in1TabletTVWearable

offRouterPageSizeChange(callback?: Callback<observer.RouterPageInfo>): void

移除使用onRouterPageSizeChange接口注册的监听回调函数。使用callback异步回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<observer.[RouterPageInfo](js-apis-arkui-observer.md#routerpageinfo)> | 否 | 需要被移除的回调函数。不传参数时，移除所有回调函数。 |

**示例：**

参考[onRouterPageSizeChange](arkts-apis-uicontext-uiobserver.md#onrouterpagesizechange23)接口示例。

## onNavDestinationSizeChange23+

PhonePC/2in1TabletTVWearable

onNavDestinationSizeChange(callback: Callback<observer.NavDestinationInfo>): void

注册监听回调函数，当可见的NavDestination大小发生变化时，会触发该回调函数。使用callback异步回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<observer.[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)> | 是 | 回调函数。携带NavDestinationInfo，返回NavDestination的信息。 |

**示例：**

```
1. import { uiObserver } from '@kit.ArkUI';

3. @Component
4. struct PageOneContent {
5. destSizeCallback(info: uiObserver.NavDestinationInfo): void {
6. console.info(`testTag destSize changeTo ${(info && info.size) ? JSON.stringify(info.size) : "NA"}`)
7. }

9. aboutToAppear(): void {
10. // 可以通过注册监听的方式获取NavDestination页面大小信息
11. this.getUIContext().getUIObserver().onNavDestinationSizeChange(this.destSizeCallback);
12. }

14. aboutToDisappear(): void {
15. this.getUIContext().getUIObserver().offNavDestinationSizeChange(this.destSizeCallback);
16. }

18. build() {
19. Column() {
20. Button('queryDestSize').onClick(() => {
21. // 也可以主动获取NavDestination页面大小信息
22. let info = this.queryNavDestinationInfo();
23. console.info(`testTag destSize: ${(info && info.size) ? JSON.stringify(info.size) : "NA"}`)
24. })
25. }
26. .width('100%')
27. .height('100%')
28. }
29. }

31. @Component
32. struct PageOne {
33. build() {
34. NavDestination() {
35. PageOneContent()
36. }
37. .title('pageOne')
38. }
39. }

41. @Entry
42. @Component
43. struct QueryNavDestinationSize {
44. private stack: NavPathStack = new NavPathStack();

46. aboutToAppear(): void {
47. this.stack.pushPath({name: 'one'});
48. }

50. @Builder
51. MyPageMap(name: string) {
52. PageOne()
53. }

55. build() {
56. Navigation(this.stack) {
57. }
58. .width('100%')
59. .height('100%')
60. .navDestination(this.MyPageMap)
61. .hideNavBar(true)
62. }
63. }
```

## offNavDestinationSizeChange23+

PhonePC/2in1TabletTVWearable

offNavDestinationSizeChange(callback?: Callback<observer.NavDestinationInfo>): void

移除使用onNavDestinationSizeChange接口注册的监听回调函数。使用callback异步回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | Callback<observer.[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)> | 否 | 需要被移除的回调函数。不传参数时，移除所有回调函数。 |

**示例：**

参考[onNavDestinationSizeChange](arkts-apis-uicontext-uiobserver.md#onnavdestinationsizechange23)接口示例。

## onNavDestinationSizeChangeByUniqueId23+

PhonePC/2in1TabletTVWearable

onNavDestinationSizeChangeByUniqueId(navigationUniqueId: number, callback: Callback<observer.NavDestinationInfo>): void

注册监听回调函数，当属于指定Navigation的可见NavDestination的大小发生变化时，会触发该回调函数。使用callback异步回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| navigationUniqueId | number | 是 | 希望监听NavDestination所属的Navigation的唯一ID，可以通过[queryNavigationInfo](ts-custom-component-api.md#querynavigationinfo12)获取。 |
| callback | Callback<observer.[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)> | 是 | 回调函数。携带NavDestinationInfo，返回NavDestination的信息。 |

**示例：**

```
1. import { uiObserver } from '@kit.ArkUI';

3. @Component
4. struct PageOneContent {
5. private navUniqueId: number = 0;

7. destSizeCallback(info: uiObserver.NavDestinationInfo): void {
8. console.info(`testTag destSize changeTo ${(info && info.size) ? JSON.stringify(info.size) : "NA"}`)
9. }

11. aboutToAppear(): void {
12. let navInfo = this.queryNavigationInfo();
13. if (navInfo && navInfo.uniqueId) {
14. this.navUniqueId = navInfo.uniqueId;
15. // 可以通过注册监听的方式获取NavDestination页面大小信息
16. this.getUIContext().getUIObserver().onNavDestinationSizeChangeByUniqueId(this.navUniqueId, this.destSizeCallback);
17. }
18. }

20. aboutToDisappear(): void {
21. this.getUIContext().getUIObserver().offNavDestinationSizeChangeByUniqueId(this.navUniqueId, this.destSizeCallback);
22. }

24. build() {
25. Column() {
26. Button('queryDestSize').onClick(() => {
27. // 也可以主动获取NavDestination页面大小信息
28. let info = this.queryNavDestinationInfo();
29. console.info(`testTag destSize: ${(info && info.size) ? JSON.stringify(info.size) : "NA"}`)
30. })
31. }
32. .width('100%')
33. .height('100%')
34. }
35. }

37. @Component
38. struct PageOne {
39. build() {
40. NavDestination() {
41. PageOneContent()
42. }
43. .title('pageOne')
44. }
45. }

47. @Entry
48. @Component
49. struct QueryNavDestinationSize {
50. private stack: NavPathStack = new NavPathStack();

52. aboutToAppear(): void {
53. this.stack.pushPath({name: 'one'});
54. }

56. @Builder
57. MyPageMap(name: string) {
58. PageOne()
59. }

61. build() {
62. Navigation(this.stack) {
63. }
64. .width('100%')
65. .height('100%')
66. .navDestination(this.MyPageMap)
67. .hideNavBar(true)
68. }
69. }
```

## offNavDestinationSizeChangeByUniqueId23+

PhonePC/2in1TabletTVWearable

offNavDestinationSizeChangeByUniqueId(navigationUniqueId: number, callback?: Callback<observer.NavDestinationInfo>): void

移除使用onNavDestinationSizeChangeByUniqueId接口注册的监听回调函数。使用callback异步回调。

**元服务API：** 从API version 23开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| navigationUniqueId | number | 是 | 希望监听的NavDestination所属的Navigation的唯一ID，可以通过[queryNavigationInfo](ts-custom-component-api.md#querynavigationinfo12)获取。 |
| callback | Callback<observer.[NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo)> | 否 | 需要被移除的回调函数。不传参数时，移除所有指定了相同navigationUniqueId的回调函数。 |

**示例：**

参考[onNavDestinationSizeChangeByUniqueId](arkts-apis-uicontext-uiobserver.md#onnavdestinationsizechangebyuniqueid23)接口示例。
