---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-router-to-navigation
title: Router切换Navigation
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 设置组件导航和页面路由 > Router切换Navigation
category: harmonyos-guides
scraped_at: 2026-04-29T13:27:38+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:da65fde33049796bba74657ad0bf9b042c0fcfbbb6c2b7c33c4a14ea950a3a12
---

鉴于组件导航（[Navigation](../harmonyos-references/ts-basic-components-navigation.md)）支持更丰富的动效、一次开发多端部署能力和更灵活的栈操作。本文主要从页面跳转、动效和生命周期等方面介绍如何从Router切换到Navigation。

## 页面结构

Router路由的页面是一个@Entry修饰的Component，每一个页面都需要在main\_page.json中声明。

```
1. // main_page.json
2. {
3. "src": [
4. "pages/Index",
5. "pages/pageOne",
6. "pages/pageTwo"
7. ]
8. }
```

以下为Router页面的示例。

```
1. // Index.ets
2. import { router } from '@kit.ArkUI';
3. import { hilog } from '@kit.PerformanceAnalysisKit';
4. const DOMAIN = 0xF811;
5. const TAG = '[Sample_ArkTSRouter]';

7. @Entry
8. @Component
9. struct Index {
10. @State message: string = 'Hello World';
11. @State router: string = 'Examples of Router, Navigation, and NavPathStack';

13. build() {
14. Row() {
15. Column() {
16. Text(this.message)
17. .fontSize(50)
18. .fontWeight(FontWeight.Bold)
19. Button('router to pageOne', { stateEffect: true, type: ButtonType.Capsule })
20. .width('80%')
21. .height(40)
22. .margin(20)
23. .onClick(() => {
24. this.getUIContext().getRouter().pushUrl({
25. url: 'pages/routerToNavigation/router/PageOne' // 目标url
26. }, router.RouterMode.Standard, (err) => {
27. if (err) {
28. hilog.error(DOMAIN, TAG, 'page ON_SHOWN:' + `Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
29. return;
30. }
31. hilog.info( DOMAIN, TAG, 'Invoke pushUrl succeeded.');
32. })
33. })
34. // ···
35. }
36. .width('100%')
37. }
38. .height('100%')
39. }
40. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/router/Index.ets#L16-L128)

```
1. @Entry
2. @Component
3. struct pageOne {
4. @State message: string = 'This is pageOne';

6. build() {
7. Row() {
8. Column() {
9. Text(this.message)
10. .fontSize(50)
11. .fontWeight(FontWeight.Bold)
12. Button('router back to Index', { stateEffect: true, type: ButtonType.Capsule })
13. .width('80%')
14. .height(40)
15. .margin(20)
16. .onClick(() => {
17. this.getUIContext().getRouter().back();
18. })
19. }
20. .width('100%')
21. }
22. .height('100%')
23. }
24. }
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/router/PageOne.ets#L16-L41)

而基于Navigation的路由页面分为导航页和子页，导航页又叫[Navbar](../harmonyos-references/ts-basic-components-navigation.md#navbar12)，是Navigation包含的子组件，子页是[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)包含的子组件。

以下为Navigation导航页的示例。

```
1. // Index.ets
2. @Entry
3. @Component
4. struct Index1 {
5. pathStack: NavPathStack = new NavPathStack();

7. build() {
8. Navigation(this.pathStack) {
9. Column() {
10. Button('Push PageOne', { stateEffect: true, type: ButtonType.Capsule })
11. .width('80%')
12. .height(40)
13. .margin(20)
14. .onClick(() => {
15. this.pathStack.pushPathByName('navigation_pageOne', null);
16. })
17. }.width('100%').height('100%')
18. }
19. .title('Navigation')
20. .mode(NavigationMode.Stack)
21. }
22. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/navigation/Index.ets#L16-L39)

以下为Navigation子页的示例。

```
1. @Builder
2. export function PageOneBuilder() {
3. PageOne();
4. }

6. @Entry
7. @Component
8. export struct PageOne {
9. pathStack: NavPathStack = new NavPathStack();

11. build() {
12. NavDestination() {
13. Column() {
14. // 请将$r('app.string.routerToNavigation_nav_text1_backHome')替换为实际资源文件，在本示例中该资源文件的value值为"回到首页"
15. Button($r('app.string.routerToNavigation_nav_text1_backHome'), { stateEffect: true, type: ButtonType.Capsule })
16. .width('80%')
17. .height(40)
18. .margin(20)
19. .onClick(() => {
20. this.pathStack.clear();
21. })
22. }.width('100%').height('100%')
23. }.title('PageOne')
24. .onReady((context: NavDestinationContext) => {
25. this.pathStack = context.pathStack;
26. })
27. }
28. }
```

[PageOne.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/navigation/PageOne.ets#L16-L45)

每个子页面也需要配置到系统配置文件router\_map.json中（参考[系统路由表](arkts-navigation-cross-package.md#系统路由表)）。

```
1. // 工程配置文件module.json5中配置 {"routerMap": "$profile:router_map"}
2. // router_map.json
3. {
4. "routerMap": [
5. {
6. "name": "pageOne",
7. "pageSourceFile": "src/main/ets/pages/PageOne.ets",
8. "buildFunction": "PageOneBuilder",
9. "data": {
10. "description": "this is pageOne"
11. }
12. }
13. ]
14. }
```

## 路由操作

Router通过@ohos.router模块提供的方法来操作页面，建议使用[UIContext](../harmonyos-references/arkts-apis-uicontext-uicontext.md)中的[getRouter](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getrouter)获取[Router](../harmonyos-references/arkts-apis-uicontext-router.md)对象。

```
1. // push page
2. this.getUIContext().getRouter().pushUrl({ url:'pages/pageOne', params: null });

4. // pop page
5. this.getUIContext().getRouter().back({ url: 'pages/pageOne' });

7. // replace page
8. this.getUIContext().getRouter().replaceUrl({ url: 'pages/pageOne' });

10. // clear all page
11. this.getUIContext().getRouter().clear();

13. // 获取页面栈大小
14. let size = this.getUIContext().getRouter().getLength();

16. // 获取页面状态
17. let pageState = this.getUIContext().getRouter().getState();
```

[GetRouter.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/navPathStack/GetRouter.ets#L34-L52)

Navigation通过导航控制器对象[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)提供的方法来操作页面，需要创建一个栈对象并传入Navigation中。

```
1. @Entry
2. @Component
3. struct Index {
4. pathStack: NavPathStack = new NavPathStack();

6. build() {
7. // 设置NavPathStack并传入Navigation
8. Navigation(this.pathStack) {
9. // ...
10. }.width('100%').height('100%')
11. .title('Navigation, Navigation')
12. .mode(NavigationMode.Stack)
13. }
14. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/navPathStack/Index.ets#L16-L31)

```
1. this.pathStack.pop();
2. // push page
3. this.pathStack.pushPath({ name: 'pageOne' });

5. // pop page
6. this.pathStack.pop();
7. this.pathStack.popToIndex(1);
8. this.pathStack.popToName('pageOne');

10. // replace page
11. this.pathStack.replacePath({ name: 'pageOne' });

13. // clear all page
14. this.pathStack.clear();

16. // 获取路由栈大小
17. let size: number = this.pathStack.size();

19. // 删除栈中name为PageOne的所有页面
20. this.pathStack.removeByName('pageOne');

22. // 删除指定索引的页面
23. this.pathStack.removeByIndexes([1, 3, 5]);

25. // 获取栈中所有页面name集合
26. this.pathStack.getAllPathName();

28. // 获取索引为1的页面参数
29. this.pathStack.getParamByIndex(1);

31. // 获取PageOne页面的参数
32. this.pathStack.getParamByName('pageOne');

34. // 获取PageOne页面的索引集合
35. this.pathStack.getIndexByName('pageOne');
36. // ...
```

[PathStack.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/navPathStack/PathStack.ets#L35-L72)

Router作为全局通用模块，可以在任意页面中调用，Navigation作为组件，子页面想要做路由需要拿到Navigation持有的导航控制器对象NavPathStack，可以通过如下几种方式获取：

**方式一**：通过@Provide和@Consume传递给子页面（有耦合，不推荐）。

```
1. // Navigation根容器
2. @Entry
3. @Component
4. struct Index {
5. // Navigation创建一个Provide修饰的NavPathStack
6. @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

8. build() {
9. Navigation(this.pathStack) {
10. // ...
11. }
12. .title('Method 1: Navigation')
13. .mode(NavigationMode.Stack)
14. }
15. }

17. // Navigation子页面
18. @Component
19. export struct PageOne {
20. // NavDestination通过Consume获取到
21. @Consume('pathStack') pathStack: NavPathStack;

23. build() {
24. NavDestination() {
25. // ...
26. }
27. .title('PageOne')
28. }
29. }
```

[Router1.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/router/Router1.ets#L16-L46)

**方式二**：子页面通过[OnReady](../harmonyos-references/ts-basic-components-navdestination.md#onready11)回调获取。

```
1. @Entry
2. @Component
3. export struct PageOne {
4. pathStack: NavPathStack = new NavPathStack();

6. build() {
7. NavDestination() {
8. // ...
9. }.title('Method 2: PageOne')
10. .onReady((context: NavDestinationContext) => {
11. this.pathStack = context.pathStack;
12. })
13. }
14. }
```

[Router2.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/router/Router2.ets#L16-L31)

**方式三**： 通过全局的AppStorage接口设置获取。

```
1. @Entry
2. @Component
3. struct Index {
4. pathStack: NavPathStack = new NavPathStack();

6. // 全局设置一个NavPathStack
7. aboutToAppear(): void {
8. AppStorage.setOrCreate('PathStack', this.pathStack);
9. }

11. build() {
12. Navigation(this.pathStack) {
13. // ...
14. }.title('Method 3: AppStorage')
15. .mode(NavigationMode.Stack)
16. }
17. }

19. // Navigation子页面
20. @Component
21. export struct PageOne {
22. // 子页面中获取全局的NavPathStack
23. pathStack: NavPathStack = AppStorage.get('PathStack') as NavPathStack;

25. build() {
26. NavDestination() {
27. // ...
28. }
29. .title('PageOne')
30. }
31. }
```

[Router3.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/router/Router3.ets#L16-L48)

**方式四**：通过自定义组件查询接口获取，参考[queryNavigationInfo](../harmonyos-references/ts-custom-component-api.md#querynavigationinfo12)。

```
1. // 子页面中的自定义组件
2. @Entry
3. @Component
4. struct CustomNode {
5. pathStack: NavPathStack = new NavPathStack();

7. aboutToAppear() {
8. // query navigation info
9. let navigationInfo: NavigationInfo = this.queryNavigationInfo() as NavigationInfo;
10. if (navigationInfo !=  undefined) {
11. this.pathStack = navigationInfo.pathStack ;
12. }
13. }

15. build() {
16. Row() {
17. Button('Method 4: queryNavigationInfo')
18. .onClick(() => {
19. this.pathStack.pushPath({ name: 'pageTwo' });
20. })
21. }
22. }
23. }
```

[Router4.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/router/Router4.ets#L16-L40)

## 生命周期

说明

router页面的生命周期和Navigation页面的生命周期关系如下：

1.router页面的跳转会影响其内部Navigation页面的生命周期。

2.Navigation页面的跳转不会影响其所在router页面的生命周期。

3.应用前后台切换会同时触发router页面和Navigation页面的生命周期。

Router页面[生命周期](arkts-routing.md#生命周期)为@Entry页面中的通用方法，主要有如下四个生命周期：

```
1. // 页面创建后挂树的回调
2. aboutToAppear(): void {
3. }

5. // 页面销毁前下树的回调
6. aboutToDisappear(): void {
7. }

9. // 页面显示时的回调
10. onPageShow(): void {
11. }

13. // 页面隐藏时的回调
14. onPageHide(): void {
15. }
```

[Comm.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/lifeCycle/Comm.ets#L20-L36)

其生命周期时序如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/0LjX2NH5RKe0Qmf6vqVl9A/zh-cn_image_0000002589324051.png?HW-CC-KV=V1&HW-CC-Date=20260429T052737Z&HW-CC-Expire=86400&HW-CC-Sign=DBB8BCC91C3930F68C53AA2AFBAAC27900C12A860FF286FB502FD950C99CE86B)

Navigation作为路由容器，其生命周期承载在NavDestination组件上，以组件事件的形式开放。

具体生命周期描述请参考Navigation[页面生命周期](arkts-navigation-navdestination.md#页面生命周期)。

```
1. @Entry
2. @Component
3. struct PageOne {
4. aboutToDisappear() {
5. }

7. aboutToAppear() {
8. }

10. build() {
11. NavDestination() {
12. // ...
13. }
14. .onWillAppear(() => {
15. })
16. .onAppear(() => {
17. })
18. .onWillShow(() => {
19. })
20. .onShown(() => {
21. })
22. .onWillHide(() => {
23. })
24. .onHidden(() => {
25. })
26. .onWillDisappear(() => {
27. })
28. .onDisAppear(() => {
29. })
30. }
31. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/lifeCycle/Index.ets#L16-L48)

## 转场动画

Router和Navigation都提供了系统的转场动画，也提供了自定义转场的能力。

其中Router自定义页面转场通过通用方法pageTransition()实现，具体可参考Router[页面转场动画](arkts-page-transition-animation.md)。

Navigation作为路由容器组件，其内部的页面切换动画本质上属于组件跟组件之间的属性动画，可以通过Navigation中的[customNavContentTransition](../harmonyos-references/ts-basic-components-navigation.md#customnavcontenttransition11)事件提供自定义转场动画的能力，具体实现可以参考Navigation[自定义转场](arkts-navigation-animation.md#自定义转场)。（注意：API version 13之前，Dialog类型的页面默认无转场动画。从API version13开始，Dialog类型的页面支持系统转场动画。）

## 共享元素转场

页面和页面之间跳转的时候需要进行共享元素过渡动画，Router可以通过通用属性sharedTransition来实现共享元素转场，具体可以参考如下链接：

[Router共享元素转场动画](../harmonyos-references/ts-transition-animation-shared-elements.md)。

Navigation也提供了共享元素一镜到底的转场能力，需要配合geometryTransition属性，在子页面（NavDestination）之间切换时，可以实现共享元素转场，具体可参考[Navigation共享元素转场动画](arkts-navigation-animation.md#共享元素转场)。

## 跨包路由

Router可以通过命名路由的方式实现跨包跳转。

1. 在想要跳转到的共享包[HAR](har-package.md)或者[HSP](in-app-hsp.md)页面里，给@Entry修饰的自定义组件[EntryOptions](arkts-create-custom-components.md#entry)命名。

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

   [Hsp11.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/router/Hsp11.ets#L16-L34)
2. 使用命名路由方式跳转时，需要在当前应用包的oh-package.json5文件中配置依赖。例如：

   ```
   1. "dependencies": {
   2. "library": "file:../library",
   3. // ...
   4. }
   ```
3. 配置成功后需要在跳转的页面中引入命名路由的页面并跳转。

   ```
   1. import { BusinessError } from '@kit.BasicServicesKit';
   2. import { hilog } from '@kit.PerformanceAnalysisKit';
   3. import('library/src/main/ets/pages/routerToNavigation/router/Index'); // 引入共享包中的命名路由页面
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
   18. this.getUIContext().getRouter().pushNamedRoute({
   19. name: 'myPage',
   20. params: {
   21. data1: 'message',
   22. data2: {
   23. data3: [123, 456, 789]
   24. }
   25. }
   26. })
   27. .then(() => {
   28. hilog.info(DOMAIN, TAG, 'pushNamedRoute succeeded.');
   29. })
   30. .catch((err: BusinessError) => {
   31. let code = err.code;
   32. let message = err.message;
   33. hilog.error(DOMAIN, TAG,`pushNamedRoute failed, code is ${code}, message is ${message}`);
   34. });
   35. })
   36. }
   37. .width('100%')
   38. .height('100%')
   39. }
   40. }
   ```

   [Hsp12.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/router/Hsp12.ets#L16-L57)

Navigation作为路由组件，默认支持跨包跳转。

1. 从HSP（HAR）中完成自定义组件（需要跳转的目标页面）开发，将自定义组件申明为export。

   ```
   1. @Component
   2. export struct PageInHSP {
   3. build() {
   4. NavDestination() {
   5. // ...
   6. }
   7. }
   8. }
   ```

   [Hsp21.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/router/Hsp21.ets#L16-L25)
2. 在HSP（HAR）的Index.ets中导出组件。

   ```
   1. export { PageInHSP } from './src/main/ets/pages/PageInHSP'
   ```

   [Hsp22.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/router/Hsp22.ets#L16-L18)
3. 使用跨包路由方式跳转时，需要在当前应用包的oh-package.json5文件中配置依赖。例如：

   ```
   1. "dependencies": {
   2. "library": "file:../library",
   3. // ...
   4. }
   ```
4. 配置好HSP（HAR）的项目依赖后，在mainPage中导入自定义组件，并添加到pageMap中，即可正常调用。

   ```
   1. // 1.导入跨包的路由页面
   2. import { PageInHSP } from 'library';

   4. @Entry
   5. @Component
   6. struct mainPage {
   7. pageStack: NavPathStack = new NavPathStack();

   9. @Builder pageMap(name: string) {
   10. if (name === 'PageInHSP') {
   11. // 2.定义路由映射表
   12. PageInHSP();
   13. }
   14. }

   16. build() {
   17. Navigation(this.pageStack) {
   18. Button('Push HSP Page')
   19. .onClick(() => {
   20. // 3.跳转到Hsp中的页面
   21. this.pageStack.pushPath({ name: 'PageInHSP' });
   22. })
   23. }
   24. .mode(NavigationMode.Stack)
   25. .navDestination(this.pageMap)
   26. }
   27. }
   ```

   [Hsp23.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/router/Hsp23.ets#L16-L44)

以上是通过**静态依赖**的形式完成了跨包的路由，在大型的项目中一般跨模块的开发需要解耦，那就需要依赖动态路由的能力。

## 动态路由

动态路由设计的目的是解决多个产品（Hap）之间可以复用相同的业务模块，各个业务模块之间解耦（模块之间跳转通过路由表跳转，不需要互相依赖）和路由功能扩展整合。

业务特性模块对外暴露的就是模块内支持完成具体业务场景的多个页面的集合；路由管理就是将每个模块支持的页面都用统一的路由表结构管理起来。 当产品需要某个业务模块时，就会注册对应的模块的路由表。

**动态路由的优势：**

1. 路由定义除了跳转的URL以外，可以丰富的配置任意扩展信息，如横竖屏默认模式，是否需要鉴权等等，做路由跳转时的统一处理。
2. 给每个路由设置一个名字，按照名称进行跳转而不是ets文件路径。
3. 页面的加载可以使用动态Import（按需加载），防止首个页面加载大量代码导致卡顿。

**Router实现动态路由主要有下面三个过程：**

1. 定义过程： 路由表定义新增路由 -> 页面文件绑定路由名称（装饰器） -> 加载函数和页面文件绑定（动态import函数）
2. 定义注册过程： 路由注册（可在入口ability中按需注入依赖模块的路由表）。
3. 跳转过程： 路由表检查(是否注册过对应路由名称) -> 路由前置钩子（路由页面加载-动态Import） -> 路由跳转 -> 路由后置钩子（公共处理，如打点）。

**Navigation实现动态路由有如下两种实现方案：**

**方案一：** 自定义路由表

基本实现跟上述Router动态路由类似。

1. 开发者自定义路由管理模块，各个提供路由页面的模块均依赖此模块；
2. 构建Navigation组件时，将NavPathStack注入路由管理模块，路由管理模块对NavPathStack进行封装，对外提供路由能力；
3. 各个路由页面不再提供组件，转为提供@build封装的构建函数，并再通过WrappedBuilder封装后，实现全局封装；
4. 各个路由页面将模块名称、路由名称、WrappedBuilder封装后构建函数注册如路由模块；
5. 当路由需要跳转到指定路由时，路由模块完成对指定路由模块的动态导入，并完成路由跳转。

具体的构建过程，可以参考Navigation[自动生成动态路由](https://gitcode.com/harmonyos-cases/cases/blob/master/CommonAppDevelopment/common/routermodule/README_AUTO_GENERATE.md)示例。

**方案二：** 系统路由表

从API version 12开始，Navigation支持系统跨模块的路由表方案，整体设计是将路由表方案下沉到系统中管理，即在需要路由的各个业务模块（HSP/HAR）中独立配置router\_map.json文件，在触发路由跳转时，应用只需要通过NavPathStack进行路由跳转，此时系统会自动完成路由模块的动态加载、组件构建，并完成路由跳转功能，从而实现了开发层面的模块解耦。

具体可参考Navigation[系统路由表](arkts-navigation-cross-package.md#系统路由表)。

## 生命周期监听

Router可以通过observer实现注册监听，接口定义请参考Router无感监听[uiObserver.on('routerPageUpdate')](../harmonyos-references/js-apis-arkui-observer.md#uiobserveronrouterpageupdate11)。

```
1. import { UIContext, uiObserver } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. const DOMAIN = 0xF811;
4. const TAG = '[Sample_ArkTSRouter]';

6. function callbackFunc(info: uiObserver.RouterPageInfo) {
7. hilog.info(DOMAIN, TAG,'RouterPageInfo is : ' + JSON.stringify(info));
8. }

10. // used in ability context.
11. uiObserver.on('routerPageUpdate', this.context, callbackFunc);

13. // used in UIContext.
14. uiObserver.on('routerPageUpdate', this.getUIContext(), callbackFunc);
```

[Comm.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/observer/Comm.ets#L16-L31)

在页面状态发生变化时，注册的回调将会触发，开发者可以通过回调中传入的入参拿到页面的相关信息，如：页面的名字，索引，路径，生命周期状态等。

Navigation同样可以通过在observer中实现注册监听。

```
1. // EntryAbility.ets
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { UIObserver, window } from '@kit.ArkUI';
4. import { UIAbility } from '@kit.AbilityKit';
5. import { hilog } from '@kit.PerformanceAnalysisKit';
6. const DOMAIN = 0xF811;
7. const TAG = '[Sample_ArkTSRouter]';

9. export default class EntryAbility extends UIAbility {
10. // ...
11. onWindowStageCreate(windowStage: window.WindowStage): void {
12. // ...
13. windowStage.getMainWindow((err: BusinessError, data) => {
14. // ...
15. let windowClass = data;
16. // 获取UIContext实例。
17. let uiContext: UIContext = windowClass.getUIContext();
18. // 获取UIObserver实例。
19. let uiObserver : UIObserver = uiContext.getUIObserver();
20. // 注册DevNavigation的状态监听.
21. uiObserver.on('navDestinationUpdate',(info) => {
22. // NavDestinationState.ON_SHOWN = 0, NavDestinationState.ON_HIDE = 1
23. if (info.state == 0) {
24. // NavDestination组件显示时操作
25. hilog.info(DOMAIN, TAG, 'page ON_SHOWN:' + info.name.toString())
26. }
27. })
28. })
29. }
30. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/observer/Index.ets#L16-L47)

## 页面信息查询

为了实现页面内自定义组件跟页面解耦，自定义组件中提供了全局查询页面信息的接口。

Router可以通过[queryRouterPageInfo](../harmonyos-references/ts-custom-component-api.md#queryrouterpageinfo12)接口查询当前自定义组件所在的Page页面的信息，其返回值包含如下几个属性，其中pageId是页面的唯一标识符：

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | UIAbilityContext/ UIContext | 是 | routerPage页面对应的上下文信息。 |
| index | number | 是 | routerPage在栈中的位置。 |
| name | string | 是 | routerPage页面的名称。 |
| path | string | 是 | routerPage页面的路径。 |
| state | RouterPageState | 是 | routerPage页面的状态。 |
| pageId12+ | string | 是 | routerPage页面的唯一标识。 |

```
1. import { uiObserver } from '@kit.ArkUI';

3. // 页面内的自定义组件
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

[PageInfo.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/observer/PageInfo.ets#L16-L30)

Navigation也可以通过[queryNavDestinationInfo](../harmonyos-references/ts-custom-component-api.md#querynavdestinationinfo)接口查询当前自定义组件所在的NavDestination的信息，其返回值包含如下几个属性，其中navDestinationId是页面的唯一标识符：

| 名称 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| navigationId | ResourceStr | 是 | 包含NavDestination组件的Navigation组件的id。 |
| name | ResourceStr | 是 | NavDestination组件的名称。 |
| state | NavDestinationState | 是 | NavDestination组件的状态。 |
| index12+ | number | 是 | NavDestination在路由栈中的索引。 |
| param12+ | Object | 否 | NavDestination组件的参数。 |
| navDestinationId12+ | string | 是 | NavDestination组件的唯一标识ID。 |

```
1. import { uiObserver } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. const DOMAIN = 0xF811;
4. const TAG = '[Sample_ArkTSRouter]';

6. @Component
7. export struct NavDestinationExample {
8. build() {
9. NavDestination() {
10. MyComponent();
11. }
12. }
13. }

15. @Component
16. struct MyComponent {
17. navDesInfo: uiObserver.NavDestinationInfo | undefined

19. aboutToAppear() {
20. this.navDesInfo = this.queryNavDestinationInfo();
21. hilog.info(DOMAIN, TAG, 'get navDestinationInfo: ' + JSON.stringify(this.navDesInfo))
22. }

24. build() {
25. // ...
26. }
27. }
```

[QueryNav.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/Navigation/entry/src/main/ets/pages/routerToNavigation/observer/QueryNav.ets#L16-L44)

## 路由拦截

Router没有提供路由拦截的能力，开发者需要自行封装路由跳转接口，并在自己封装的接口中做路由拦截的判断并重定向路由。

Navigation提供了[setInterception](../harmonyos-references/ts-basic-components-navigation.md#setinterception12)方法，用于设置Navigation页面跳转拦截回调。具体可以参考文档：Navigation[路由拦截](arkts-navigation-jump.md#路由拦截)
