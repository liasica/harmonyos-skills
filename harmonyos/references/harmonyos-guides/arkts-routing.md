---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-routing
title: 页面路由 (@ohos.router)(不推荐)
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 设置组件导航和页面路由 > 页面路由 (@ohos.router)(不推荐)
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:0722960a1912c8754b6a8ccf0f9f938c44746de94404dbd724bb5703038d6bfb
---

页面路由指在应用程序中实现不同页面之间的跳转和数据传递。Router模块通过不同的url地址，可以方便地进行页面路由，轻松地访问不同的页面。本文将从[页面跳转](arkts-routing.md#页面跳转)、[页面返回](arkts-routing.md#页面返回)、[页面返回前增加一个询问框](arkts-routing.md#页面返回前增加一个询问框)和[命名路由](arkts-routing.md#命名路由)这几个方面，介绍如何通过Router模块实现页面路由。

说明

[组件导航 (Navigation)](arkts-navigation-architecture.md)具有更强的功能和自定义能力，推荐使用该组件作为应用的路由框架。Navigation和Router的差异可参考[Router切换Navigation](arkts-router-to-navigation.md)指导。

## 页面跳转

页面跳转是开发过程中的一个重要组成部分。在使用应用程序时，通常需要在不同的页面之间跳转，有时还需要将数据从一个页面传递到另一个页面。

**图1** 页面跳转

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/xsYdg0crQHiV3aaK60Ga3Q/zh-cn_image_0000002558604524.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052736Z&HW-CC-Expire=86400&HW-CC-Sign=983088F2E10AB44FF43C4236FE822D0853DC86D750E593DA16B8530DF3B75476)

Router模块提供了两种跳转模式，分别是[pushUrl](../harmonyos-references/arkts-apis-uicontext-router.md#pushurl)和[replaceUrl](../harmonyos-references/arkts-apis-uicontext-router.md#replaceurl)。这两种模式决定了目标页面是否会替换当前页。

* pushUrl：目标页面不会替换当前页，而是压入页面栈。这样可以保留当前页的状态，并且可以通过返回键或者调用[back](../harmonyos-references/arkts-apis-uicontext-router.md#back)方法返回到当前页。
* replaceUrl：目标页面会替换当前页，并销毁当前页。这样可以释放当前页的资源，并且无法返回到当前页。

说明

* 创建新页面时，请参考[构建第二个页面](start-with-ets-stage.md#section47459107221)配置第二个页面的路由。
* 页面栈的最大容量为32个页面。如果超过这个限制，可以调用[clear](../harmonyos-references/arkts-apis-uicontext-router.md#clear)方法清空历史页面栈，释放内存空间。

同时，Router模块提供了两种实例模式，分别是Standard和Single。这两种模式决定了目标url是否会对应多个实例。

* Standard：多实例模式，也是默认情况下的跳转模式。目标页面会被添加到页面栈顶，无论栈中是否存在相同url的页面。
* Single：单实例模式。如果目标页面的url已经存在于页面栈中，则会将离栈顶最近的同url页面移动到栈顶，该页面成为新建页。如果目标页面的url在页面栈中不存在同url页面，则按照默认的多实例模式进行跳转。
* 场景一：有一个主页（Home）和一个详情页（Detail），希望从主页点击一个商品，跳转到详情页。同时，需要保留主页在页面栈中，以便返回时恢复状态。这种场景下，可以使用pushUrl方法，并且使用Standard实例模式（或者省略）。

  ```
  1. import { router } from '@kit.ArkUI';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. const DOMAIN = 0xF811;
  4. const TAG = '[Sample_ArkTSRouter]';

  6. @Entry
  7. @Component
  8. struct Index {
  9. // 在Home页面中
  10. onJumpClick(): void {
  11. this.getUIContext().getRouter().pushUrl({
  12. url: 'pages/pageRouter/jumpPage/Detail' // 目标url
  13. }, router.RouterMode.Standard, (err) => {
  14. if (err) {
  15. hilog.error(DOMAIN, TAG,`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
  16. return;
  17. }
  18. hilog.info(DOMAIN, TAG,'Invoke pushUrl succeeded.');
  19. });
  20. }

  22. build() {
  23. // ···
  24. }
  25. }
  ```

  [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/jumpPage/Index.ets#L16-L57)

  说明

  多实例模式下，router.RouterMode.Standard参数可以省略。
* 场景二：有一个登录页（Login）和一个个人中心页（Profile），希望从登录页成功登录后，跳转到个人中心页。同时，销毁登录页，在返回时直接退出应用。这种场景下，可以使用replaceUrl方法，并且使用Standard实例模式（或者省略）。

  ```
  1. import { router } from '@kit.ArkUI';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. const DOMAIN = 0xF811;
  4. const TAG = '[Sample_ArkTSRouter]';

  6. @Entry
  7. @Component
  8. struct Login {
  9. // 在Login页面中
  10. onJumpClick(): void {
  11. this.getUIContext().getRouter().replaceUrl({
  12. url: 'pages/pageRouter/jumpPage/Profile' // 目标url
  13. }, router.RouterMode.Standard, (err) => {
  14. if (err) {
  15. hilog.error(DOMAIN, TAG,`Invoke replaceUrl failed, code is ${err.code}, message is ${err.message}`);
  16. return;
  17. }
  18. hilog.info(DOMAIN, TAG,'Invoke replaceUrl succeeded.');
  19. });
  20. }

  22. build() {
  23. // ...
  24. }
  25. }
  ```

  [Login.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/jumpPage/Login.ets#L16-L57)

  说明

  多实例模式下，router.RouterMode.Standard参数可以省略。
* 场景三：有一个设置页（Setting）和一个主题切换页（Theme），希望从设置页点击主题选项，跳转到主题切换页。同时，需要保证每次只有一个主题切换页存在于页面栈中，在返回时直接回到设置页。这种场景下，可以使用pushUrl方法，并且使用Single实例模式。

  ```
  1. import { router } from '@kit.ArkUI';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. const DOMAIN = 0xF811;
  4. const TAG = '[Sample_ArkTSRouter]';

  6. @Entry
  7. @Component
  8. struct Login {
  9. // 在Setting页面中
  10. onJumpClick(): void {
  11. this.getUIContext().getRouter().pushUrl({
  12. url: 'pages/pageRouter/jumpPage/SetTheme' // 目标url
  13. }, router.RouterMode.Single, (err) => {
  14. if (err) {
  15. hilog.error(DOMAIN, TAG, `Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
  16. return;
  17. }
  18. hilog.info(DOMAIN, TAG, 'Invoke pushUrl succeeded.');
  19. });
  20. }

  22. build() {
  23. // ...
  24. }
  25. }
  ```

  [Setting.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/jumpPage/Setting.ets#L16-L57)
* 场景四：有一个搜索结果列表页（SearchResult）和一个搜索结果详情页（SearchDetail），希望从搜索结果列表页点击某一项结果，跳转到搜索结果详情页。同时，如果该结果已经被查看过，则不需要再新建一个详情页，而是直接跳转到已经存在的详情页。这种场景下，可以使用replaceUrl方法，并且使用Single实例模式。

  ```
  1. import { router } from '@kit.ArkUI';
  2. import { hilog } from '@kit.PerformanceAnalysisKit';
  3. const DOMAIN = 0xF811;
  4. const TAG = '[Sample_ArkTSRouter]';

  6. @Entry
  7. @Component
  8. struct SearchResult {
  9. // 在SearchResult页面中
  10. onJumpClick(): void {
  11. this.getUIContext().getRouter().replaceUrl({
  12. url: 'pages/pageRouter/jumpPage/SearchDetail' // 目标url
  13. }, router.RouterMode.Single, (err) => {
  14. if (err) {
  15. hilog.error(DOMAIN, TAG, `Invoke replaceUrl failed, code is ${err.code}, message is ${err.message}`);
  16. return;
  17. }
  18. hilog.error(DOMAIN, TAG, 'Invoke replaceUrl succeeded.');
  19. });
  20. }

  22. build() {
  23. // ...
  24. }

  26. }
  ```

  [SearchResult.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/jumpPage/SearchResult.ets#L15-L57)

以上是不带参数传递的场景。

如果需要在跳转时传递一些数据给目标页面，则可以在调用Router模块的方法时，添加一个params属性，并指定一个对象作为参数。例如：

```
1. class DataModelInfo {
2. public age: number = 0;
3. }

5. class DataModel {
6. public id: number = 0;
7. public info: DataModelInfo | null = null;
8. }
```

[IndexPara.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/jumpPage/IndexPara.ets#L19-L28)

```
1. onJumpClick(): void {
2. // 在Home页面中
3. let paramsInfo: DataModel = {
4. id: 123,
5. info: {
6. age: 20
7. }
8. };

10. this.getUIContext().getRouter().pushUrl({
11. url: 'pages/pageRouter/jumpPage/DetailPara', // 目标url
12. params: paramsInfo // 添加params属性，传递自定义参数
13. }, (err) => {
14. if (err) {
15. hilog.error(DOMAIN, TAG,`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
16. return;
17. }
18. hilog.info(DOMAIN, TAG,'Invoke pushUrl succeeded.');
19. });
20. }
```

[IndexPara.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/jumpPage/IndexPara.ets#L33-L54)

在目标页面中，可以通过调用Router模块的[getParams](../harmonyos-references/arkts-apis-uicontext-router.md#getparams)方法来获取传递过来的参数。例如：

```
1. class InfoTmp {
2. public age: number = 0;
3. }

5. class RouTmp {
6. // id: object = () => {
7. // };
8. public id: number = 0;
9. public info: InfoTmp = new InfoTmp();
10. }
```

[DetailPara.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/jumpPage/DetailPara.ets#L16-L27)

```
1. private params: RouTmp = (this.getUIContext().getRouter().getParams()) as RouTmp; // 获取传递过来的参数对象
2. // private id: number = this.params.id; // 获取id属性的值
3. private age: number = this.params.info.age; // 获取age属性的值
```

[DetailPara.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/jumpPage/DetailPara.ets#L32-L36)

## 页面返回

当用户在一个页面完成操作后，通常需要返回到上一个页面或者指定页面，这就需要用到页面返回功能。在返回的过程中，可能需要将数据传递给目标页面，这就需要用到数据传递功能。

**图2** 页面返回

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/S4DcJnFKQh-suf9_UyOF8w/zh-cn_image_0000002589324049.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052736Z&HW-CC-Expire=86400&HW-CC-Sign=4127D8F0C9FC96C720FDB1AC8A5F8DFFBF1A5E2F05CB74606B08465A282DC397)

直接使用router可能导致[UI上下文不明确](arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)实例，并使用[getRouter](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getrouter)获取绑定实例的router。

可以使用以下几种方式返回页面：

* 方式一：返回到上一个页面。

```
1. this.getUIContext().getRouter().back();
```

[BackDetail.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/jumpPage/BackDetail.ets#L33-L35)

这种方式会返回到上一个页面，即上一个页面在页面栈中的位置。但是，上一个页面必须存在于页面栈中才能够返回，否则该方法将无效。

* 方式二：返回到指定页面。

  返回普通页面。

  ```
  1. this.getUIContext().getRouter().back({
  2. url: 'pages/pageRouter/jumpPage/BackHome'
  3. });
  ```

  [BackDetail.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/jumpPage/BackDetail.ets#L43-L47)

  返回命名路由页面。

  ```
  1. this.getUIContext().getRouter().back({
  2. url: 'myPage' // myPage为返回的命名路由页面别名
  3. });
  ```

  [BackDetail.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/jumpPage/BackDetail.ets#L55-L59)

  这种方式可以返回到指定页面，需要指定目标页面的路径。目标页面必须存在于页面栈中才能够返回。
* 方式三：返回到指定页面，并传递自定义参数信息。

  返回到普通页面。

  ```
  1. this.getUIContext().getRouter().back({
  2. url: 'pages/pageRouter/jumpPage/BackHome',
  3. params: {
  4. // 请将$r('app.string.pageRouter_jump_text7_fromHome')替换为实际资源文件，在本示例中该资源文件的value值为"来自Home页"
  5. info: $r('app.string.pageRouter_jump_text7_fromHome')
  6. }
  7. });
  ```

  [BackDetail.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/jumpPage/BackDetail.ets#L67-L75)

  返回命名路由页面。

  ```
  1. this.getUIContext().getRouter().back({
  2. url: 'myPage', // myPage为返回的命名路由页面别名
  3. params: {
  4. // 请将$r('app.string.pageRouter_jump_text7_fromHome')替换为实际资源文件，在本示例中该资源文件的value值为"来自Home页"
  5. info: $r('app.string.pageRouter_jump_text7_fromHome')
  6. }
  7. });
  ```

  [BackDetail.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/jumpPage/BackDetail.ets#L83-L91)

  这种方式不仅可以返回到指定页面，还可以在返回的同时传递自定义参数信息。这些参数信息可以在目标页面中通过调用[getParams](../harmonyos-references/arkts-apis-uicontext-router.md#getparams)方法进行获取和解析。

在目标页面中，在需要获取参数的位置调用[getParams](../harmonyos-references/arkts-apis-uicontext-router.md#getparams)方法即可，例如在[onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)生命周期回调中：

说明

直接使用router可能导致[UI上下文不明确](arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)实例，并使用[getRouter](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getrouter)获取绑定实例的router。

```
1. @Entry
2. @Component
3. struct Home {
4. @State message: string = 'Hello World';

6. onPageShow() {
7. const params = this.getUIContext().getRouter().getParams() as Record<string, string>; // 获取传递过来的参数对象
8. if (params) {
9. const info: string = params.info as string; // 获取info属性的值
10. }
11. }

13. // ···
14. }
```

[Home.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/backPage/Home.ets#L15-L36)

说明

当使用back方法返回到指定页面时，原栈顶页面（包括）到指定页面（不包括）之间的所有页面栈都将从栈中弹出并销毁。

另外，如果使用back方法返回到原来的页面，原页面不会被重复创建，因此使用@State声明的变量不会重复声明，也不会触发页面的aboutToAppear生命周期回调。如果需要在原页面中使用返回页面传递的自定义参数，可以在需要的位置进行参数解析。例如，在onPageShow生命周期回调中进行参数解析。

## 生命周期

[router](../harmonyos-references/js-apis-router.md)页面生命周期，即被[@Entry](arkts-create-custom-components.md#entry)装饰的组件生命周期，提供以下生命周期接口，其中onPageShow和onPageHide的生命周期时序图可参考Router切换Navigation中的[生命周期](arkts-router-to-navigation.md#生命周期)：

* [onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)：页面每次显示时触发一次，包括路由过程、应用进入前台等场景。
* [onPageHide](../harmonyos-references/ts-custom-component-lifecycle.md#onpagehide)：页面每次隐藏时触发一次，包括路由过程、应用进入后台等场景。
* [onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)：当用户点击返回按钮时触发。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';
2. const DOMAIN = 0xF811;
3. const TAG = '[Sample_ArkTSRouter]';
4. // Index.ets
5. @Entry
6. @Component
7. struct MyComponent {
8. // 只有被@Entry装饰的组件才可以调用页面的生命周期
9. onPageShow() {
10. hilog.info(DOMAIN, TAG, 'Index onPageShow');
11. }

13. // 只有被@Entry装饰的组件才可以调用页面的生命周期
14. onPageHide() {
15. hilog.info(DOMAIN, TAG, 'Index onPageHide');
16. }

18. // 只有被@Entry装饰的组件才可以调用页面的生命周期
19. onBackPress() {
20. hilog.info(DOMAIN, TAG, 'Index onBackPress');
21. // 返回true表示页面自己处理返回逻辑，不进行页面路由；返回false表示使用默认的路由返回逻辑，不设置返回值按照false处理
22. return true;
23. }

25. build() {
26. Column() {
27. // push到Page页面，执行onPageHide
28. Button('push to next page')
29. .onClick(() => {
30. this.getUIContext().getRouter().pushUrl({ url: 'pages/pageRouter/lifeCycle/Page' });
31. })
32. }
33. }
34. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/lifeCycle/Index.ets#L16-L51)

```
1. // Page.ets
2. @Entry
3. @Component
4. struct Page {
5. @State textColor: Color = Color.Black;
6. @State num: number = 0;

8. // 只有被@Entry装饰的组件才可以调用页面的生命周期
9. onPageShow() {
10. console.info('Page onPageShow');
11. this.num = 5;
12. }

14. // 只有被@Entry装饰的组件才可以调用页面的生命周期
15. onPageHide() {
16. console.info('Page onPageHide');
17. }

19. // 只有被@Entry装饰的组件才可以调用页面的生命周期
20. onBackPress() { // 不设置返回值按照false处理
21. console.info('Page onBackPress');
22. this.textColor = Color.Grey;
23. this.num = 0;
24. }

26. build() {
27. Column() {
28. Text(`num is：${this.num}`)
29. .fontSize(30)
30. .fontWeight(FontWeight.Bold)
31. .fontColor(this.textColor)
32. .margin(20)
33. .onClick(() => {
34. this.num += 5;
35. })
36. Button('pop to previous page')
37. .onClick(() => {
38. this.getUIContext().getRouter().back();
39. })
40. }
41. .width('100%')
42. }
43. }
```

[Page.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/lifeCycle/Page.ets#L16-L63)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/XRIJVAqMQ4mumgW3IActkw/zh-cn_image_0000002589243989.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052736Z&HW-CC-Expire=86400&HW-CC-Sign=C81A583BEB92F22F386B8F0231EB0242871A9945F2B8E9541DE38C4B081C6F28)

## 自定义转场

router自定义转场可以通过[pageTransition](../harmonyos-references/ts-custom-component-lifecycle.md#pagetransition9)实现，具体参考[页面间转场 (pageTransition)](../harmonyos-references/ts-page-transition-animation.md)。

## 页面返回前增加一个询问框

在开发应用时，为了避免用户误操作或者丢失数据，有时候需要在用户从一个页面返回到另一个页面之前，弹出一个询问框，让用户确认是否要执行这个操作。

本文将从[系统默认询问框](arkts-routing.md#系统默认询问框)和[自定义询问框](arkts-routing.md#自定义询问框)两个方面来介绍如何实现页面返回前增加一个询问框的功能。

**图3** 页面返回前增加一个询问框

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/lOANEzfzQn-E0-QheY7wUw/zh-cn_image_0000002558764182.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052736Z&HW-CC-Expire=86400&HW-CC-Sign=2DAAA23BE1367A9228344544B3B683397D8F88154692EEEFE921CE782BCAB4D4)

### 系统默认询问框

为了实现这个功能，可以使用页面路由Router模块提供的两个方法：[showAlertBeforeBackPage](../harmonyos-references/arkts-apis-uicontext-router.md#showalertbeforebackpage)和[back](../harmonyos-references/arkts-apis-uicontext-router.md#back)来实现这个功能。

直接使用router可能导致[UI上下文不明确](arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)实例，并使用[getRouter](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getrouter)获取绑定实例的router。

如果想要在目标界面开启页面返回询问框，需要在调用[back](../harmonyos-references/arkts-apis-uicontext-router.md#back)方法之前，通过调用[showAlertBeforeBackPage](../harmonyos-references/arkts-apis-uicontext-router.md#showalertbeforebackpage)方法设置返回询问框的信息。例如，在支付页面中定义一个返回按钮的点击事件处理函数：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. const DOMAIN = 0xF811;
4. const TAG = '[Sample_ArkTSRouter]';
```

[ShowAlert.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/pageTransition/ShowAlert.ets#L16-L21)

```
1. // 定义一个返回按钮的点击事件处理函数
2. onBackClick(): void {
3. // 调用this.getUIContext().getRouter().showAlertBeforeBackPage方法，设置返回询问框的信息
4. try {
5. this.getUIContext().getRouter().showAlertBeforeBackPage({
6. // 请在resources\base\element\string.json文件中配置name为'pageRouter_dialog_context'，value为非空字符串的资源
7. message: this.getUIContext().getHostContext()?.resourceManager.getStringByNameSync('pageRouter_dialog_context') as string, // 设置询问框的内容
8. });
9. } catch (err) {
10. let message = (err as BusinessError).message;
11. let code = (err as BusinessError).code;
12. hilog.error(DOMAIN, TAG,`Invoke showAlertBeforeBackPage failed, code is ${code}, message is ${message}`);
13. }

15. // 调用this.getUIContext().getRouter().back()方法，返回上一个页面
16. this.getUIContext().getRouter().back();
17. }
```

[ShowAlert.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/pageTransition/ShowAlert.ets#L27-L45)

其中，this.getUIContext().getRouter().showAlertBeforeBackPage方法接收一个对象作为参数，该对象包含以下属性：

message：string类型，表示询问框的内容。

如果调用成功，则会在目标界面开启页面返回询问框；如果调用失败，则会抛出异常，并通过err.code和err.message获取错误码和错误信息。

当用户点击“返回”按钮时，会弹出确认对话框，询问用户是否确认返回。选择“取消”将停留在当前页目标页面；选择“确认”将触发[back](../harmonyos-references/arkts-apis-uicontext-router.md#back)方法，并根据参数决定如何执行跳转。

### 自定义询问框

自定义询问框的方式，可以使用弹窗[showDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showdialog-1)或者自定义弹窗实现。这样可以让应用界面与系统默认询问框有所区别，提高应用的用户体验度。本文以弹窗为例，介绍如何实现自定义询问框。

直接使用router可能导致[UI上下文不明确](arkts-global-interface.md#ui上下文不明确)的问题，建议使用getUIContext()获取[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)实例，并使用[getRouter](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getrouter)获取绑定实例的router。

在事件回调中，调用弹窗的[showDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#showdialog-1)方法：

```
1. import { promptAction} from '@kit.ArkUI';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. const DOMAIN = 0xF811;
5. const TAG = '[Sample_ArkTSRouter]';
```

[ShowDialog.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/pageTransition/ShowDialog.ets#L16-L22)

```
1. onBackClick() {
2. // 弹出自定义的询问框
3. this.getUIContext().getPromptAction().showDialog({
4. // 您还没有完成支付，确定要返回吗？
5. // 请将$r('app.string.pageRouter_dialog_context')替换为实际资源文件，在本示例中该资源文件的value值为"您还没有完成支付，确定要返回吗？"
6. message: $r('app.string.pageRouter_dialog_context'),
7. buttons: [
8. {
9. // 请将$r('app.string.pageRouter_dialog_canceled')替换为实际资源文件，在本示例中该资源文件的value值为"取消"
10. text: $r('app.string.pageRouter_dialog_canceled'),
11. color: '#FF0000'
12. },
13. {
14. // 请将$r('app.string.pageRouter_dialog_confirmed')替换为实际资源文件，在本示例中该资源文件的value值为"确认"
15. text: $r('app.string.pageRouter_dialog_confirmed'),
16. color: '#0099FF'
17. }
18. ]
19. }).then((result: promptAction.ShowDialogSuccessResponse) => {
20. if (result.index === 0) {
21. // 用户点击了“取消”按钮
22. hilog.info(DOMAIN, TAG, 'User canceled the operation.');
23. } else if (result.index === 1) {
24. // 用户点击了“确认”按钮
25. hilog.info(DOMAIN, TAG, 'User confirmed the operation.');
26. // 调用this.getUIContext().getRouter().back()方法，返回上一个页面
27. this.getUIContext().getRouter().back();
28. }
29. }).catch((err: Error) => {
30. let message = (err as BusinessError).message;
31. let code = (err as BusinessError).code;
32. hilog.error(DOMAIN, TAG, `Invoke showDialog failed, code is ${code}, message is ${message}`);
33. });
34. }
```

[ShowDialog.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/pageTransition/ShowDialog.ets#L28-L63)

当用户点击“返回”按钮时，会弹出自定义的询问框，询问用户是否确认返回。选择“取消”将停留在当前页目标页面；选择“确认”将触发[back](../harmonyos-references/arkts-apis-uicontext-router.md#back)方法，并根据参数决定如何执行跳转。

## 命名路由

在开发中为了跳转到共享包[HAR](har-package.md)或者[HSP](in-app-hsp.md)中的页面（即共享包中路由跳转），可以使用[pushNamedRoute](../harmonyos-references/arkts-apis-uicontext-router.md#pushnamedroute)来实现。

**图4** 命名路由跳转

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/WYyiM4vnTQGjEtDaw89YCQ/zh-cn_image_0000002558604526.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052736Z&HW-CC-Expire=86400&HW-CC-Sign=7C48DB756B0DBA60961341233F441206211E3F85215D97179C281E94E309344B)

在想要跳转到的共享包[HAR](har-package.md)或者[HSP](in-app-hsp.md)页面里，给[@Entry](arkts-create-custom-components.md#entry)修饰的自定义组件EntryOptions命名：

```
1. // library/src/main/ets/pages/Index.ets
2. // library为新建共享包自定义的名字
3. @Entry({ routeName: 'myPage' })
4. @Component
5. export struct MyComponent {
6. build() {
7. Row() {
8. Column() {
9. Text('Library Page')
10. .fontSize(50)
11. .fontWeight(FontWeight.Bold)
12. }
13. .width('100%')
14. }
15. .height('100%')
16. }
17. }
```

[Hsp12.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/hsp/Hsp12.ets#L16-L34)

配置成功后需要在跳转的页面中引入命名路由的页面：

说明

使用命名路由方式跳转时，需要在当前应用包的oh-package.json5文件中配置依赖。例如：

```
1. "dependencies": {
2. "library": "file:../library",
3. // ...
4. }
```

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import 'library/src/main/ets/pages/Index'; // 引入共享包中的命名路由页面
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. const DOMAIN = 0xF811;
5. const TAG = '[Sample_ArkTSRouter]';

7. @Entry
8. @Component
9. struct Index {
10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Text('Hello World')
13. .fontSize(50)
14. .fontWeight(FontWeight.Bold)
15. .margin({ top: 20 })
16. .backgroundColor('#ccc')
17. .onClick(() => { // 点击跳转到其他共享包中的页面
18. try {
19. this.getUIContext().getRouter().pushNamedRoute({
20. name: 'myPage',
21. params: {
22. data1: 'message',
23. data2: {
24. data3: [123, 456, 789]
25. }
26. }
27. });
28. } catch (err) {
29. let message = (err as BusinessError).message;
30. let code = (err as BusinessError).code;
31. hilog.error(DOMAIN, TAG,`pushNamedRoute failed, code is ${code}, message is ${message}`);
32. }
33. })
34. }
35. .width('100%')
36. .height('100%')
37. }
38. }
```

[Hsp3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/pageRouter/hsp/Hsp3.ets#L16-L55)
