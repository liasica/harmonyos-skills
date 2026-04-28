---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-custom-component-api
title: 自定义组件内置方法
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS组件 > 自定义组件 > 自定义组件内置方法
category: harmonyos-references
scraped_at: 2026-04-28T08:02:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:be0f3985041b734a16921f6e5ed6dea30eb0c53aaf5aa12a18bf010290f8bdc8
---

自定义组件内置方法是由ArkUI开发框架提供给应用开发者的，定义在自定义组件基类上的API。应用开发者可以在自定义组件的实例上调用对应的API以获取当前自定义组件实例相关的信息。例如，查询当前自定义组件上下文的UIContext信息。

说明

本模块首批接口从API version 11开始支持，后续版本的新增接口，采用上角标单独标记接口的起始版本。

## getUIContext

PhonePC/2in1TabletTVWearable

getUIContext(): UIContext

获取UIContext对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [UIContext](ts-custom-component-api.md#uicontext) | 返回UIContext实例对象。在异步调用的回调方法中使用该接口，或者该接口的起始调用不在当前页面时，可能导致接口调用发生在自定义组件销毁之后，返回 undefined。 |

## UIContext

PhonePC/2in1TabletTVWearable

type UIContext = UIContext

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [UIContext](arkts-apis-uicontext-uicontext.md) | 返回UIContext实例对象。 |

**示例：**

```
1. import { UIContext } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct MyComponent {
6. aboutToAppear() {
7. let uiContext: UIContext = this.getUIContext();
8. }

10. build() {
11. // ...
12. }
13. }
```

## getUniqueId12+

PhonePC/2in1TabletTVWearable

getUniqueId(): number

获取当前组件的UniqueId。UniqueId为系统为每个组件分配的Id，可保证当前应用中的唯一性。若在组件对应的节点未创建或已销毁时获取，返回无效UniqueId：-1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 返回当前Component的UniqueId。 |

**示例：**

```
1. @Entry
2. @Component
3. struct MyComponent {
4. aboutToAppear() {
5. let uniqueId: number = this.getUniqueId();
6. }

8. build() {
9. // ...
10. }
11. }
```

## queryNavDestinationInfo

PhonePC/2in1TabletTVWearable

queryNavDestinationInfo(): NavDestinationInfo | undefined;

查询自定义组件所属的NavDestination信息，仅当自定义组件在NavDestination的内部时才生效。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NavDestinationInfo](ts-custom-component-api.md#navdestinationinfo) | undefined | 返回NavDestinationInfo实例对象。 |

**示例：**

```
1. import { uiObserver } from '@kit.ArkUI';

3. @Component
4. export struct NavDestinationExample {
5. build() {
6. NavDestination() {
7. MyComponent()
8. }
9. }
10. }

12. @Component
13. struct MyComponent {
14. navDesInfo: uiObserver.NavDestinationInfo | undefined

16. aboutToAppear() {
17. // this指代MyComponent自定义节点，并从该节点向上查找其最近的一个类型为NavDestination的父亲节点
18. this.navDesInfo = this.queryNavDestinationInfo();
19. console.info('get navDestinationInfo: ' + JSON.stringify(this.navDesInfo));
20. }

22. build() {
23. // ...
24. }
25. }
```

## queryNavDestinationInfo18+

PhonePC/2in1TabletTVWearable

queryNavDestinationInfo(isInner: Optional<boolean>): NavDestinationInfo | undefined

查询当前自定义组件距离最近的NavDestination信息（要求该NavDestination是Navigation的导航页或子页），isInner为true表示向内查找，false表示向外查找。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isInner | [Optional](ts-universal-attributes-custom-property.md#optionalt)<boolean> | 是 | true：向内查询最近的，且在栈内的NavDestinationInfo的详细信息。  false：向外查询最近的，且在栈内的NavDestinationInfo的详细信息。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NavDestinationInfo](ts-custom-component-api.md#navdestinationinfo) | undefined | 返回NavDestinationInfo实例对象。 |

**示例：**

```
1. // Index.ets
2. @Entry
3. @Component
4. struct NavigationExample {
5. pageInfo: NavPathStack = new NavPathStack();

7. build() {
8. Navigation(this.pageInfo) {
9. Column() {
10. Button('pageOne', { stateEffect: true, type: ButtonType.Capsule })
11. .width('80%')
12. .height(40)
13. .margin(20)
14. .onClick(() => {
15. this.pageInfo.pushPath({ name: 'pageOne' }); // 将name指定的NavDestination页面信息入栈。
16. })
17. }
18. }.title('NavIndex')
19. }
20. }
```

```
1. // PageOne.ets
2. import { uiObserver } from '@kit.ArkUI';

4. @Builder
5. export function PageOneBuilder() {
6. PageOneComponent()
7. }

9. @Component
10. export struct PageOneComponent {
11. navDesInfo: uiObserver.NavDestinationInfo | undefined;
12. @State text: string = '';
13. build() {
14. NavDestination() {
15. Column() {
16. Button('点击向内查找')
17. .width('80%')
18. .height(40)
19. .margin(20)
20. .onClick(() => {
21. // 向内查询PageOne的NavDestination信息
22. this.navDesInfo = this.queryNavDestinationInfo(true);
23. this.text = JSON.stringify(this.navDesInfo?.name).toString();
24. })
25. Text('向内查找的NavDestination是:' + this.text)
26. .width('80%')
27. .height(50)
28. .margin(50)
29. .fontSize(20)
30. MyComponent()
31. }.width('100%').height('100%')
32. }
33. .title('pageOne')
34. }
35. }

37. @Component
38. struct MyComponent {
39. navDesInfo: uiObserver.NavDestinationInfo | undefined;
40. @State text: string = '';

42. build() {
43. Column() {
44. Button('点击向外查找')
45. .width('80%')
46. .height(40)
47. .margin(20)
48. .onClick(() => {
49. // 向外查询PageOne的NavDestination信息
50. this.navDesInfo = this.queryNavDestinationInfo(false);
51. this.text = JSON.stringify(this.navDesInfo?.name).toString();
52. })
53. Text('向外查找的NavDestination是:' + this.text)
54. .width('80%')
55. .height(50)
56. .margin(50)
57. .fontSize(20)
58. }
59. }
60. }
```

```
1. // route_map.json
2. {
3. "routerMap": [
4. {
5. "name": "pageOne",
6. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
7. "buildFunction": "PageOneBuilder",
8. "data": {
9. "description": "this is pageOne"
10. }
11. }
12. ]
13. }
```

## NavDestinationInfo

PhonePC/2in1TabletTVWearable

type NavDestinationInfo = NavDestinationInfo

NavDestinationInfo实例对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [NavDestinationInfo](js-apis-arkui-observer.md#navdestinationinfo) | 返回NavDestinationInfo实例对象。 |

## queryNavigationInfo12+

PhonePC/2in1TabletTVWearable

queryNavigationInfo(): NavigationInfo | undefined

查询自定义组件所属的Navigation信息。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [NavigationInfo](ts-custom-component-api.md#navigationinfo12) | undefined | 返回NavigationInfo实例对象。 |

**示例：**

```
1. // index.ets
2. import { uiObserver } from '@kit.ArkUI';

4. @Entry
5. @Component
6. struct MainPage {
7. pathStack: NavPathStack = new NavPathStack();

9. build() {
10. Navigation(this.pathStack) {
11. // ...
12. }.id("NavigationId")
13. }
14. }

17. @Component
18. export struct PageOne {
19. pathStack: NavPathStack = new NavPathStack();

21. aboutToAppear() {
22. // this指代PageOne自定义节点，并从该节点向上查找其最近的一个类型为Navigation的父亲节点
23. let navigationInfo: uiObserver.NavigationInfo | undefined = this.queryNavigationInfo();
24. console.info('get navigationInfo: ' + JSON.stringify(navigationInfo));
25. if (navigationInfo !== undefined) {
26. this.pathStack = navigationInfo.pathStack;
27. }
28. }

30. build() {
31. NavDestination() {
32. // ...
33. }.title('PageOne')
34. }
35. }
```

## NavigationInfo12+

PhonePC/2in1TabletTVWearable

type NavigationInfo = NavigationInfo

NavigationInfo实例对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [NavigationInfo](js-apis-arkui-observer.md#navigationinfo12) | 返回NavigationInfo实例对象。 |

## queryRouterPageInfo12+

PhonePC/2in1TabletTVWearable

queryRouterPageInfo(): RouterPageInfo | undefined;

获取RouterPageInfo实例对象。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RouterPageInfo](ts-custom-component-api.md#routerpageinfo12) | undefined | 返回RouterPageInfo实例对象。 |

**示例：**

```
1. import { uiObserver } from '@kit.ArkUI';

3. @Entry
4. @Component
5. struct MyComponent {
6. aboutToAppear() {
7. let info: uiObserver.RouterPageInfo | undefined = this.queryRouterPageInfo();
8. }

10. build() {
11. // ...
12. }
13. }
```

## RouterPageInfo12+

PhonePC/2in1TabletTVWearable

type RouterPageInfo = RouterPageInfo

RouterPageInfo实例对象。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

| 类型 | 说明 |
| --- | --- |
| [RouterPageInfo](js-apis-arkui-observer.md#routerpageinfo) | 返回RouterPageInfo实例对象。 |

## getDialogController18+

PhonePC/2in1TabletTVWearable

getDialogController(): PromptActionDialogController | undefined

获取PromptActionDialogController实例对象。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [PromptActionDialogController](ts-custom-component-api.md#promptactiondialogcontroller18) | undefined | 返回PromptActionDialogController实例对象。 |

**示例：**

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { ComponentContent } from '@kit.ArkUI';

4. class Params {
5. text: string = "";
6. constructor(text: string) {
7. this.text = text;
8. }
9. }

11. @ComponentV2
12. struct MyComponent {
13. build() {
14. Column() {
15. Button('Close Dialog')
16. .onClick(() => {
17. let ctrl: PromptActionDialogController = this.getDialogController();
18. if (ctrl != undefined) {
19. ctrl.close();
20. }
21. })
22. }
23. }
24. }

26. @Builder
27. function buildText(params: Params) {
28. Column() {
29. Text(params.text)
30. .fontSize(50)
31. .fontWeight(FontWeight.Bold)
32. .margin({ bottom: 36 })
33. MyComponent()
34. }.backgroundColor('#FFF0F0F0')
35. }

37. @Entry
38. @ComponentV2
39. struct Index {
40. @Local message: string = "hello";

42. build() {
43. Row() {
44. Column({ space: 10 }) {
45. Button('click me')
46. .fontSize(20)
47. .onClick(() => {
48. let ctx = this.getUIContext();
49. let promptAction = ctx.getPromptAction();
50. promptAction.openCustomDialog(new ComponentContent(ctx, wrapBuilder(buildText), new Params(this.message)))
51. .catch((err: BusinessError) => {
52. console.error("openCustomDialog error: " + err.code + " " + err.message);
53. })
54. })
55. }
56. .width('100%')
57. .height('100%')
58. }
59. .height('100%')
60. }
61. }
```

## PromptActionDialogController18+

PhonePC/2in1TabletTVWearable

type PromptActionDialogController = promptAction.DialogController

自定义弹窗控制器，可以控制当前自定义弹窗，具体控制能力包括关闭弹窗等，详见[promptAction.DialogController](js-apis-promptaction.md#dialogcontroller18)。

**元服务API：** 从API version 18开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

| 类型 | 说明 |
| --- | --- |
| [promptAction.DialogController](js-apis-promptaction.md#dialogcontroller18) | 表示对象类型为promptAction.DialogController实例对象。 |
