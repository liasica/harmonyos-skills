---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-navigation-jump
title: Navigation页面路由
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 设置组件导航和页面路由 > 组件导航(Navigation) (推荐) > Navigation页面路由
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:37+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:a8d325fe7d42dcd3c6ce80ea8c52e916d64179fb22a65c7d38f9e9ba7777f441
---

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)路由相关操作均基于导航控制器[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)提供的方法实现，每个Navigation都需要创建并传入一个NavPathStack对象，用于管理页面。NavPathStack主要提供了页面跳转、页面返回、页面替换、页面删除、参数获取、路由拦截等功能。

在API version 9，Navigation需要配合[NavRouter](../harmonyos-references/ts-basic-components-navrouter.md)组件实现页面路由。从API version 10开始，更推荐使用NavPathStack实现页面路由。

路由相关的几个关键概念：

* 路由表：定义了页面名称和[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)页面的映射，若跳转时传入的页面名称未在路由表里注册，会跳转失败。系统提供了[系统路由表](arkts-navigation-cross-package.md#系统路由表)和[自定义路由表](arkts-navigation-cross-package.md#自定义路由表)两种实现方式。
* 路由栈：NavDestination页面以栈结构管理，每个Navigation都有自己的路由栈，不可共享。路由栈主要由NavPathStack控制，此外可通过[NavPathStack.getPathStack](../harmonyos-references/ts-basic-components-navigation.md#getpathstack19)获取完整路由栈信息。
* 页面转场：页面跳转动画，Navigation默认提供了页面切换的转场动画，也支持开发者自定义转场动画。

说明

* NavPathStack对象和Navigation需要一一对应，不可复用。
* NavPathStack主要控制的是[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)页面跳转、删除等，无法直接操作[NavBar导航栏](arkts-navigation-architecture.md#navbar导航栏)，若想跳转到NavBar页面只能通过[clear](../harmonyos-references/ts-basic-components-navigation.md#clear10)清空路由栈的方式。
* 不建议开发者通过监听生命周期的方式管理自己的路由栈，可通过[NavPathStack.getPathStack](../harmonyos-references/ts-basic-components-navigation.md#getpathstack19)查询路由栈。
* 在应用处于后台状态下，调用NavPathStack的栈操作方法，会在应用再次回到前台状态时触发刷新。

## 创建导航页面

### 构建导航根容器

首先，开发者需要创建一个[Navigation](../harmonyos-references/ts-basic-components-navigation.md)作为导航根容器，并创建一个[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)对象作为构造入参传给Navigation组件，以实现二者的绑定，后续的路由操作均基于该NavPathStack展开。

```
1. @Entry
2. @Component
3. struct Index {
4. // 创建一个导航控制器对象并传入Navigation
5. pageStack: NavPathStack = new NavPathStack();
6. // ...
7. build() {
8. Navigation(this.pageStack) {
9. // ...
10. }.title('Main')
11. }
12. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/Index.ets#L17-L77)

### 构建子页面

为每个[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)声明对外的实例化方法，如代码中的PageOneBuilder，执行该方法会创建一个PageOne的自定义组件，该组件就是一个Navigation的子页面。

```
1. @Builder
2. export function PageOneBuilder(name: string, param: string) {
3. PageOne({ name: name, value: param });
4. }

6. @Component
7. export struct PageOne {
8. navPathStack: NavPathStack = new NavPathStack();
9. name: string = '';
10. @State value: string = '';
11. context = this.getUIContext().getHostContext();

13. build() {
14. NavDestination() {
15. // ...
16. }.title(`${this.name}`)
17. // ...
18. }
19. }
```

[NavigationExampleOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/NavigationExampleOne.ets#L16-L77)

### 配置路由表

系统提供了系统路由表和自定义路由表两种实现方式，此处以系统路由表为例。将子页面中写好的实例化方法与它的name（开发者自定义）在路由表配置文件中注册，配置文件需要自行创建，路径：entry/src/main/resources/base/profile/router\_map.json。

```
1. {
2. "routerMap": [
3. {
4. "name": "basicPageOne", // 路由页面的唯一标识符
5. "pageSourceFile": "src/main/ets/pages/PageOne.ets", // 源码所在路径
6. "buildFunction": "PageOneBuilder" // 页面的实例化方法名称
7. }
8. ]
9. }
```

创建好路由表后，需要将其注册到工程中，在工程配置文件[module.json5](module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"。

## 路由操作

### 路由栈获取

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)根容器和子页面以及路由表配置完成后，即可通过调用[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)的API来实现页面之间的跳转。上文提到在一个Navigation容器中，只有一个NavPathStack对象，那么在子页面里执行路由操作就需要获取此NavPathStack对象，有两种方式：

* 方式一：使用[AppStorage](../harmonyos-references/ts-state-management.md#appstorage)存储与获取。

  ```
  1. @Entry
  2. @Component
  3. struct NavigationPage {
  4. navStack: NavPathStack = new NavPathStack();

  6. aboutToAppear(): void {
  7. AppStorage.setOrCreate<NavPathStack>('basicNavigationStack', this.navStack);
  8. // ...
  9. }

  11. build() {
  12. Navigation(this.navStack) {
  13. // ...
  14. }
  15. }
  16. }
  ```

  [NavigationPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/animation/NavigationPage.ets#L17-L47)

  ```
  1. @Builder
  2. export function BasicNavDestinationBuilder() {
  3. BasicNavDestination();
  4. }

  6. @Component
  7. struct BasicNavDestination {
  8. // 在NavDestination中获取导航控制器
  9. stack: NavPathStack = AppStorage.get<NavPathStack>('basicNavigationStack')!;

  11. build() {
  12. NavDestination() {
  13. // ...
  14. }
  15. .title('BasicNavDestination')
  16. }
  17. }
  ```

  [BasicNavDestination.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/animation/BasicNavDestination.ets#L16-L51)
* 方式二：[NavDestination.onReady](../harmonyos-references/ts-basic-components-navdestination.md#onready11)生命周期回调中获取。

  ```
  1. @Builder
  2. export function PageOneBuilder(name: string, param: string) {
  3. PageOne({ name: name, value: param });
  4. }

  6. @Component
  7. export struct PageOne {
  8. navPathStack: NavPathStack = new NavPathStack();
  9. name: string = '';
  10. @State value: string = '';
  11. context = this.getUIContext().getHostContext();

  13. build() {
  14. NavDestination() {
  15. // ...
  16. }.title(`${this.name}`)
  17. .onReady((ctx: NavDestinationContext) => {
  18. // 通过NavDestinationContext获取当前所在页面的导航控制器
  19. this.navPathStack = ctx.pathStack;
  20. })
  21. }
  22. }
  ```

  [NavigationExampleOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/NavigationExampleOne.ets#L17-L76)

### 基础操作

从API version 12开始，导航控制器允许被继承。开发者可以在派生类中自定义属性和方法，也可以重写父类的方法。派生类对象可以替代基类[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)对象使用。重写NavPathStack的示例代码请参考[定义导航控制器派生类](../harmonyos-references/ts-basic-components-navigation.md#示例10定义导航控制器派生类)。下文介绍了NavPathStack里提供的基础路由操作接口。

**页面跳转**

NavPathStack可以通过Push相关的接口（如[pushPath](../harmonyos-references/ts-basic-components-navigation.md#pushpath10)、[pushPathByName](../harmonyos-references/ts-basic-components-navigation.md#pushpathbyname10)、[pushDestination](../harmonyos-references/ts-basic-components-navigation.md#pushdestination11)、[pushDestinationByName](../harmonyos-references/ts-basic-components-navigation.md#pushdestinationbyname11)）实现页面跳转。跳转方式主要分为以下三种：

1. 普通跳转：通过页面名称跳转，并可以携带参数。

   ```
   1. this.pageStack.pushPath({ name: 'pageOne', param: 'PageOne Param' });
   ```

   [Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/Index.ets#L56-L58)

   ```
   1. this.pageStack.pushPathByName('pageTwo', 'PageTwo Param');
   ```

   [PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/PageOne.ets#L47-L49)
2. 带返回回调的跳转：跳转时添加onPop回调，能在页面出栈时获取返回信息，并进行处理。

   ```
   1. let DOMAIN = 0x0000;
   2. this.pageInfo.pushPathByName('temp4-pageTwo', 'temp4-pageTwo Param', (popInfo) => {
   3. hilog.info(DOMAIN, 'testTag', 'Pop page name is: ', popInfo.info.name, 'result: ',
   4. JSON.stringify(popInfo.result));
   5. // ...
   6. });
   ```

   [PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template4/PageOne.ets#L40-L50)
3. 带错误码的跳转：跳转结束会触发异步回调，返回错误码信息。

   ```
   1. const DOMAIN = 0x0000;
   2. this.pageStack.pushDestination({
   3. name: 'pageTwo', param: 'PageTwo Param'}).catch((error: BusinessError) => {
   4. hilog.info(DOMAIN, 'testTag', '[pushDestination]failed', 'error code = ', error.code,
   5. 'error.message = ', error.message);
   6. }).then(() => {
   7. hilog.info(DOMAIN, 'testTag', '[pushDestination]success.');
   8. });
   ```

   [PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/PageOne.ets#L56-L65)

   ```
   1. const DOMAIN = 0x0000;
   2. this.pageStack.pushDestinationByName('pageTwo', 'PageTwo Param').catch((error: BusinessError) => {
   3. hilog.info(DOMAIN, 'testTag', '[pushDestinationByName]failed', 'error code = ', error.code,
   4. 'error.message = ', error.message);
   5. }).then(() => {
   6. hilog.info(DOMAIN, 'testTag', '[pushDestinationByName]success.');
   7. });
   ```

   [PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/PageOne.ets#L71-L79)

**页面返回**

NavPathStack可以通过[pop](../harmonyos-references/ts-basic-components-navigation.md#pop11)相关接口实现页面返回，参考示例如下。

```
1. // 返回到上一页
2. this.pathStack.pop();
```

[PageTwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/PageTwo.ets#L54-L57)

```
1. // 返回到上一个pageOne页面
2. this.pathStack.popToName('temp4-pageOne');
```

[PageTwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template4/PageTwo.ets#L50-L53)

```
1. // 返回到索引为0的页面
2. this.pathStack.popToIndex(0);
```

[PageTwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template4/PageTwo.ets#L61-L64)

```
1. // 返回到根首页（清除栈中所有页面）
2. this.pageStack.clear();
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/PageOne.ets#L192-L195)

**页面替换**

NavPathStack可以通过Replace相关接口（如[replacePath](../harmonyos-references/ts-basic-components-navigation.md#replacepath11)、[replacePathByName](../harmonyos-references/ts-basic-components-navigation.md#replacepathbyname11)、[replaceDestination](../harmonyos-references/ts-basic-components-navigation.md#replacedestination18)）实现页面替换，参考示例如下。

```
1. // 将栈顶页面替换为pageTwo
2. this.pageStack.replacePath({ name: 'pageTwo', param: 'PageTwo Param' });
3. this.pageStack.replacePathByName('pageTwo', 'PageTwo Param');
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/PageOne.ets#L137-L141)

```
1. const DOMAIN = 0x0000;
2. // 带错误码的替换，跳转结束会触发异步回调，返回错误码信息
3. this.pageStack.replaceDestination({ name: 'pageTwo', param: 'PageTwo Param' })
4. .catch((error: BusinessError) => {
5. hilog.info(DOMAIN, 'testTag', '[replaceDestination]failed', 'error code = ', error.code,
6. 'error.message = ', error.message);
7. }).then(() => {
8. hilog.info(DOMAIN, 'testTag', '[replaceDestination]success.');
9. })
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/PageOne.ets#L150-L160)

**页面删除**

NavPathStack可以通过Remove相关接口（如[removeByName](../harmonyos-references/ts-basic-components-navigation.md#removebyname11)、[removeByIndexes](../harmonyos-references/ts-basic-components-navigation.md#removebyindexes11)、[removeByNavDestinationId](../harmonyos-references/ts-basic-components-navigation.md#removebynavdestinationid12)）实现删除路由栈中特定页面的功能，参考示例如下。

```
1. // 删除栈中name为pageTwo的所有页面
2. this.pageStack.removeByName('pageTwo');
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/PageOne.ets#L113-L116)

```
1. // 删除指定索引的页面
2. this.pageStack.removeByIndexes([1]);
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/PageOne.ets#L168-L171)

```
1. // 删除指定id的页面
2. this.pageStack.removeByNavDestinationId('1');
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/PageOne.ets#L180-L183)

**移动页面**

NavPathStack可以通过Move相关接口（如[moveToTop](../harmonyos-references/ts-basic-components-navigation.md#movetotop10)、[moveIndexToTop](../harmonyos-references/ts-basic-components-navigation.md#moveindextotop10)）实现移动路由栈中特定页面到栈顶的功能，参考示例如下。

```
1. // 移动栈中name为pageTwo的页面到栈顶
2. this.pageStack.moveToTop('pageTwo');
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/PageOne.ets#L87-L90)

```
1. // 移动栈中索引为1的页面到栈顶
2. this.pageStack.moveIndexToTop(1);
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/PageOne.ets#L100-L103)

### 单例跳转

通过设置[LaunchMode](../harmonyos-references/ts-basic-components-navigation.md#launchmode12枚举说明)为LaunchMode.MOVE\_TO\_TOP\_SINGLETON或LaunchMode.POP\_TO\_SINGLETON，可以实现Navigation路由栈的单实例跳转。单实例跳转的规则如下：

1. 如果指定为LaunchMode.MOVE\_TO\_TOP\_SINGLETON，系统会从栈底到栈顶查找具有指定名称的NavDestination。找到后，该页面将被移动到栈顶（replace操作会用指定的NavDestination替换当前栈顶）。
2. 如果指定为LaunchMode.POP\_TO\_SINGLETON，系统同样会从栈底到栈顶查找具有指定名称的NavDestination。找到后，会移除该NavDestination上方的所有页面（replace操作会用指定的NavDestination替换当前栈顶）。

当栈中存在的NavDestination页面通过单实例方式移动到栈顶时，将触发[onNewParam](../harmonyos-references/ts-basic-components-navdestination.md#onnewparam19)回调。

有关单实例跳转的示例代码，可以参考[使用导航控制器方法](../harmonyos-references/ts-basic-components-navigation.md#示例2使用导航控制器方法)。

### 参数获取

NavDestination子页第一次创建时会触发[onReady](../harmonyos-references/ts-basic-components-navdestination.md#onready11)回调，可以获取此页面对应的参数。

```
1. @Component
2. struct Page01 {
3. pathStack: NavPathStack | undefined = undefined;
4. // ...
5. pageParam: string = '';
6. build() {
7. NavDestination() {
8. // ...
9. .title('Page01')
10. .onReady((context: NavDestinationContext) => {
11. this.pathStack = context.pathStack;
12. this.pageParam = context.pathInfo.param as string;
13. })
14. }
15. }
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template7/PageOne.ets#L23-L48)

NavDestination组件中可以通过设置[onResult](../harmonyos-references/ts-basic-components-navdestination.md#onresult15)接口，接收返回时传递的路由参数。

```
1. class NavParam {
2. desc: string = 'navigation-param'
3. };
4. const DOMAIN = 0x0000;
5. // ...
6. @Component
7. export struct PageOne {
8. // ...
9. build() {
10. NavDestination() {
11. // ...
12. }
13. // ...
14. .onResult((param: Object) => {
15. if (param instanceof NavParam) {
16. console.info('TestTag', 'get NavParam, its desc: ' + (param as NavParam).desc);
17. return;
18. }
19. console.info('TestTag', 'param not instance of NavParam');
20. })
21. }
22. }
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/PageOne.ets#L17-L260)

其他业务场景，可以通过主动调用NavPathStack的获取接口（如[getAllPathName](../harmonyos-references/ts-basic-components-navigation.md#getallpathname10)、[getParamByIndex](../harmonyos-references/ts-basic-components-navigation.md#getparambyindex10)、[getParamByName](../harmonyos-references/ts-basic-components-navigation.md#getparambyname10)、[getIndexByName](../harmonyos-references/ts-basic-components-navigation.md#getindexbyname10)）获取指定页面的参数。

```
1. // 获取栈中所有页面name集合
2. this.pageStack.getAllPathName();
3. // 获取索引为1的页面参数
4. this.pageStack.getParamByIndex(1);
5. // 获取PageOne页面的参数
6. this.pageStack.getParamByName('PageOne');
7. // 获取PageOne页面的索引集合
8. this.pageStack.getIndexByName('pageOne');
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/PageOne.ets#L203-L212)

### 路由拦截

NavPathStack提供了[setInterception](../harmonyos-references/ts-basic-components-navigation.md#setinterception12)方法，用于设置Navigation页面跳转拦截回调。该方法需要传入一个[NavigationInterception](../harmonyos-references/ts-basic-components-navigation.md#navigationinterception12)对象，该对象包含多个回调函数，如willShow、didShow等，不同回调函数的调用时机不同，可根据业务需要选择拦截时机。

说明

* 无论是哪个回调，在进入回调时路由栈都已经发生了变化。
* interception回调时机比willShow更早，也可以做拦截重定向的能力，区别是，前者触发时不会创建被拦截的页面，willShow触发时会创建被拦截的页面然后销毁。

以willShow为例，在回调中通过修改路由栈实现路由拦截重定向。

```
1. const DOMAIN = 0x0000;
2. this.pageStack.setInterception({
3. willShow: (from: NavDestinationContext | 'navBar', to: NavDestinationContext | 'navBar',
4. operation: NavigationOperation, animated: boolean) => {
5. if (typeof to === 'string') {
6. hilog.info(DOMAIN, 'testTag', 'target page is navigation home');
7. return;
8. }
9. // 将跳转到PageTwo的路由重定向到PageOne
10. let target: NavDestinationContext = to as NavDestinationContext;
11. if (target.pathInfo.name === 'pageTwo') {
12. target.pathStack.pop();
13. target.pathStack.pushPathByName('pageOne', null);
14. }
15. }
16. })
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template2/Index.ets#L27-L44)

## 示例

### 创建导航首页

实现步骤为：

1. 使用Navigation创建导航主页，并创建导航控制器NavPathStack以此来实现不同页面之间的跳转。
2. 在Navigation中增加List组件，来定义导航主页中不同的一级界面。
3. 在List内的组件添加onClick方法，并在其中使用导航控制器NavPathStack的pushPathByName方法，使组件可以在点击之后从当前页面跳转到输入参数name在路由表内对应的页面。

```
1. @Entry
2. @Component
3. struct NavigationDemo {
4. @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();
5. private listArray: Array<string> = ['WLAN', 'Bluetooth', 'Personal Hotspot', 'Connect & Share'];
6. context = this.getUIContext().getHostContext();
7. build() {
8. Column() {
9. Navigation(this.navPathStack) {
10. // 请将$r('app.string.enterKeyWordsToSearch')替换为实际资源文件，在本示例中该资源文件的value值为"输入关键字搜索"
11. TextInput({ placeholder: $r('app.string.enterKeyWordsToSearch') })
12. .width('90%')
13. .height(40)
14. .margin({ bottom: 10 })

16. // 通过List定义导航的一级界面
17. List({ space: 12, initialIndex: 0 }) {
18. ForEach(this.listArray, (item: string) => {
19. ListItem() {
20. Row() {
21. Row() {
22. Text(`${item.slice(0, 1)}`)
23. .fontColor(Color.White)
24. .fontSize(14)
25. .fontWeight(FontWeight.Bold)
26. }
27. .width(30)
28. .height(30)
29. .backgroundColor('#a8a8a8')
30. .margin({ right: 20 })
31. .borderRadius(20)
32. .justifyContent(FlexAlign.Center)

34. Column() {
35. Text(item)
36. .fontSize(16)
37. .margin({ bottom: 5 })
38. }
39. .alignItems(HorizontalAlign.Start)

41. Blank()

43. Row()
44. .width(12)
45. .height(12)
46. .margin({ right: 15 })
47. .border({
48. width: { top: 2, right: 2 },
49. color: 0xcccccc
50. })
51. .rotate({ angle: 45 })
52. }
53. .borderRadius(15)
54. .shadow({ radius: 100, color: '#ededed' })
55. .width('90%')
56. .alignItems(VerticalAlign.Center)
57. .padding({ left: 15, top: 15, bottom: 15 })
58. .backgroundColor(Color.White)
59. }
60. .width('100%')
61. .onClick(() => {
62. // $r('app.string.detailsPageParameters')需要替换为开发者所需的字符串资源文件，资源文件中的value值为“详情页面参数”
63. this.navPathStack.pushPathByName(`${item}`,
64. // 将name指定的NavDestination页面信息入栈，传递的参数为param
65. this.context!.resourceManager.getStringSync($r('app.string.detailsPageParameters').id));
66. })
67. }, (item: string): string => item)
68. }
69. .listDirection(Axis.Vertical)
70. .edgeEffect(EdgeEffect.Spring)
71. .sticky(StickyStyle.Header)
72. .chainAnimation(false)
73. .width('100%')
74. }
75. .width('100%')
76. .mode(NavigationMode.Auto)
77. // $r('app.string.settings')需要替换为开发者所需的字符串资源文件,资源文件中的value值为“设置”
78. .title($r('app.string.settings')) // 设置标题文字
79. }
80. .size({ width: '100%', height: '100%' })
81. .backgroundColor(0xf4f4f5)
82. }
83. }
```

[NavigationExample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/NavigationExample.ets#L15-L99)

### 创建导航子页

导航子页1实现步骤为：

1. 使用NavDestination来创建导航子页PageOne。
2. 创建导航控制器NavPathStack并在onReady时进行初始化，获取当前所在的导航控制器，以此来实现不同页面之间的跳转。
3. 在子页面内的组件添加onClick，并在其中使用导航控制器NavPathStack的pop方法，使组件可以在点击之后弹出路由栈栈顶元素实现页面的返回。

```
1. @Builder
2. export function PageOneBuilder(name: string, param: string) {
3. PageOne({ name: name, value: param });
4. }

6. @Component
7. export struct PageOne {
8. navPathStack: NavPathStack = new NavPathStack();
9. name: string = '';
10. @State value: string = '';
11. context = this.getUIContext().getHostContext();

13. build() {
14. NavDestination() {
15. Column() {
16. // $r('app.string.settingPage')需要替换为开发者所需的字符串资源文件,资源文件中的value值为“设置页面”
17. Text(`${this.name}${this.context!.resourceManager.getStringSync($r('app.string.settingPage').id)}`)
18. .width('100%')
19. .fontSize(20)
20. .fontColor(0x333333)
21. .textAlign(TextAlign.Center)
22. .textShadow({
23. radius: 2,
24. offsetX: 4,
25. offsetY: 4,
26. color: 0x909399
27. })
28. .padding({ top: 30 })
29. Text(`${JSON.stringify(this.value)}`)
30. .width('100%')
31. .fontSize(18)
32. .fontColor(0x666666)
33. .textAlign(TextAlign.Center)
34. .padding({ top: 45 })
35. // $r('app.string.return')需要替换为开发者所需的字符串资源文件,资源文件中的value值为“返回”
36. Button($r('app.string.return'))
37. .width('50%')
38. .height(40)
39. .margin({ top: 50 })
40. .onClick(() => {
41. // 弹出路由栈栈顶元素，返回上个页面
42. this.navPathStack.pop();
43. })
44. }
45. .size({ width: '100%', height: '100%' })
46. }.title(`${this.name}`)
47. .onReady((ctx: NavDestinationContext) => {
48. // 通过NavDestinationContext获取当前所在页面的导航控制器
49. this.navPathStack = ctx.pathStack;
50. })
51. }
52. }
```

[NavigationExampleOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/NavigationExampleOne.ets#L15-L78)

导航子页2实现步骤为：

1. 使用NavDestination，来创建导航子页PageTwo。
2. 创建导航控制器NavPathStack并在onReady时进行初始化，获取当前所在的导航控制器，以此来实现不同页面之间的跳转。
3. 在子页面内的组件添加onClick，并在其中使用导航控制器NavPathStack的pushPathByName方法，使组件可以在点击之后从当前页面跳转到输入参数name在路由表内对应的页面。

```
1. @Builder
2. export function PageTwoBuilder(name: string) {
3. PageTwo({ name: name });
4. }

6. @Component
7. export struct PageTwo {
8. navPathStack: NavPathStack = new NavPathStack();
9. name: string = '';
10. private listArray: Array<string> = ['Projection', 'Print', 'VPN', 'Private DNS', 'NFC'];
11. context = this.getUIContext().getHostContext();
12. build() {
13. NavDestination() {
14. Column() {
15. List({ space: 12, initialIndex: 0 }) {
16. ForEach(this.listArray, (item: string) => {
17. ListItem() {
18. Row() {
19. Row() {
20. Text(`${item.slice(0, 1)}`)
21. .fontColor(Color.White)
22. .fontSize(14)
23. .fontWeight(FontWeight.Bold)
24. }
25. .width(30)
26. .height(30)
27. .backgroundColor('#a8a8a8')
28. .margin({ right: 20 })
29. .borderRadius(20)
30. .justifyContent(FlexAlign.Center)

32. Column() {
33. Text(item)
34. .fontSize(16)
35. .margin({ bottom: 5 })
36. }
37. .alignItems(HorizontalAlign.Start)

39. Blank()

41. Row()
42. .width(12)
43. .height(12)
44. .margin({ right: 15 })
45. .border({
46. width: { top: 2, right: 2 },
47. color: 0xcccccc
48. })
49. .rotate({ angle: 45 })
50. }
51. .borderRadius(15)
52. .shadow({ radius: 100, color: '#ededed' })
53. .width('90%')
54. .alignItems(VerticalAlign.Center)
55. .padding({ left: 15, top: 15, bottom: 15 })
56. .backgroundColor(Color.White)
57. }
58. .width('100%')
59. .onClick(() => {
60. // $r('app.string.pageSettingParam')需要替换为开发者所需的字符串资源文件,资源文件中的value值为“页面设置参数”
61. this.navPathStack.pushPathByName(`${item}`,
62. this.context!.resourceManager.getStringSync($r('app.string.pageSettingParam').id));
63. })
64. }, (item: string): string => item)
65. }
66. .listDirection(Axis.Vertical)
67. .edgeEffect(EdgeEffect.Spring)
68. .sticky(StickyStyle.Header)
69. .width('100%')
70. }
71. .size({ width: '100%', height: '100%' })
72. }.title(`${this.name}`)
73. .onReady((ctx: NavDestinationContext) => {
74. // NavDestinationContext获取当前所在的导航控制器
75. this.navPathStack = ctx.pathStack;
76. })
77. }
78. }
```

[NavigationExampleTwo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/NavigationSample/entry/src/main/ets/pages/navigation/template1/NavigationExampleTwo.ets#L15-L94)

### 创建路由表

实现步骤为：

1. router\_map.json中配置全局路由表，导航控制器NavPathStack可根据路由表中的name将对应页面信息入栈。

   ```
   1. {
   2. "routerMap" : [
   3. {
   4. "name" : "WLAN",
   5. "pageSourceFile"  : "src/main/ets/pages/PageOne.ets",
   6. "buildFunction" : "PageOneBuilder"
   7. },
   8. {
   9. "name" : "Bluetooth",
   10. "pageSourceFile"  : "src/main/ets/pages/PageOne.ets",
   11. "buildFunction" : "PageOneBuilder"
   12. },
   13. {
   14. "name" : "Personal Hotspot",
   15. "pageSourceFile"  : "src/main/ets/pages/PageOne.ets",
   16. "buildFunction" : "PageOneBuilder"
   17. },
   18. {
   19. "name" : "Connect & Share",
   20. "pageSourceFile"  : "src/main/ets/pages/PageTwo.ets",
   21. "buildFunction" : "PageTwoBuilder"
   22. },
   23. {
   24. "name" : "Projection",
   25. "pageSourceFile"  : "src/main/ets/pages/PageOne.ets",
   26. "buildFunction" : "PageOneBuilder"
   27. },
   28. {
   29. "name" : "Print",
   30. "pageSourceFile"  : "src/main/ets/pages/PageOne.ets",
   31. "buildFunction" : "PageOneBuilder"
   32. },
   33. {
   34. "name" : "VPN",
   35. "pageSourceFile"  : "src/main/ets/pages/PageOne.ets",
   36. "buildFunction" : "PageOneBuilder"
   37. },
   38. {
   39. "name" : "Private DNS",
   40. "pageSourceFile"  : "src/main/ets/pages/PageOne.ets",
   41. "buildFunction" : "PageOneBuilder"
   42. },
   43. {
   44. "name" : "NFC",
   45. "pageSourceFile"  : "src/main/ets/pages/PageOne.ets",
   46. "buildFunction" : "PageOneBuilder"
   47. }
   48. ]
   49. }
   ```
2. 工程配置文件[module.json5](module-configuration-file.md)中配置{"routerMap": "$profile:router\_map"}。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/RVmvKq0oSFekQMRFtL_HYw/zh-cn_image_0000002558764174.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052735Z&HW-CC-Expire=86400&HW-CC-Sign=6E8668041E30DDF19EF42BD372A5FC7DB477C4D6C96A696CBF6A9E735DD1ADDF)
