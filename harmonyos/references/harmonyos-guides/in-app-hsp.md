---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/in-app-hsp
title: HSP
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 应用程序包基础知识 > 应用程序包开发与使用 > HSP
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:455b1d44db43f61796f53d8be63b80c81ab933d7aa571ad4f3fa943f2c48a1df
---

HSP（Harmony Shared Package）是动态共享包，包含代码、C++库、资源和配置文件，通过HSP可以实现代码和资源的共享。HSP不支持独立发布上架，而是跟随宿主应用的APP包一起发布，与宿主应用同进程，具有相同的包名和生命周期。

说明

* 应用内HSP：在编译过程中与应用包名（bundleName）强耦合，只能给某个特定的应用使用。
* [集成态HSP](integrated-hsp.md)：构建、发布过程中，不与特定的应用包名耦合；使用时，工具链支持自动将集成态HSP的包名替换成宿主应用包名，并且会重新签名生成一个新的HSP包，作为宿主应用的安装包，这个新的HSP也属于宿主应用HAP的应用内HSP。
* 指南和API参考文档中如无特殊说明，默认HSP都为应用内HSP。

## 使用场景

* 多个HAP/HSP共用的代码和资源放在同一个HSP中，可以提高代码、资源的可重用性和可维护性，同时编译打包时也只保留一份HSP代码和资源，能够控制应用包的大小。
* HSP在运行时[按需加载](../best-practices/bpta-modular-design.md#section28312051291)，有助于提升应用性能。
* 同一个组织内部的多个应用之间，可以使用集成态HSP实现代码和资源的共享。

## 约束限制

* 可以和依赖该HSP的HAP一起安装/运行。在安装或更新时，多模块之间存在校验，详情参考[一致性校验](install-and-update-consistency-verification.md)。使用打包工具进行打包时，会进行合法性校验，详情请参考[打包工具](packing-tool.md)。
* 从API version 14开始HSP支持在配置文件中[声明UIAbility](uiability-overview.md#声明配置)组件，但不支持具有入口能力的UIAbility（即skill标签配置了entity.system.home和ohos.want.action.home）。配置UIAbility的方法参考[模块中添加UIAbility](ide-add-new-ability.md#section18658758104318)，HSP中UIAbility的启动方式与[应用内启动UIAbility](uiability-intra-device-interaction.md)方法相同。API version 13及之前版本，不支持在配置文件中声明[UIAbility](uiability-overview.md#声明配置)组件。
* 从API version 18开始HSP支持在配置文件中声明[ExtensionAbility](extensionability-overview.md)组件，但不支持具有入口能力的ExtensionAbility（即skill标签配置了entity.system.home和ohos.want.action.home）。HSP中配置ExtensionAbility的方法参考[模块中添加ExtensionAbility](ide-add-new-ability.md#section18891639459)。 API version 17及之前版本，不支持在配置文件中声明[ExtensionAbility](extensionability-overview.md)组件。
* HSP可以依赖其他HAR或HSP，也可以被HAP或者HSP依赖集成，但不支持循环依赖，也不支持依赖传递。

说明

循环依赖：例如有三个HSP，HSP-A、HSP-B和HSP-C，循环依赖指HSP-A依赖HSP-B，HSP-B依赖HSP-C，HSP-C又依赖HSP-A。

依赖传递：例如有三个HSP，HSP-A、HSP-B和HSP-C，依赖关系是HSP-A依赖HSP-B，HSP-B依赖HSP-C。不支持传递依赖指HSP-A可以使用HSP-B的方法和组件，但是HSP-A不能直接使用HSP-C的方法和组件。

## 创建

使用DevEco Studio创建一个用于调用C++代码的HSP模块。并在“Configure New Module”页面中启用“Enable native”选项。详见[创建HSP模块](ide-hsp.md#section7717162312546)，以创建一个名为library的HSP模块为例。基本的工程目录结构如下：

```
1. MyApplication
2. ├── library
3. │   ├── src
4. │   │   └── main
5. |   |       ├── cpp
6. |   |       |   ├── CMakeLists.txt    //C++代码编译的配置文件
7. |   |       |   └── napi_init.cpp     //NAPI模块初始化的C++文件
8. │   │       ├── ets
9. │   │       │   └── pages
10. │   │       │       └── index.ets     //模块library的页面文件
11. │   │       ├── resources             //模块library的资源目录
12. │   │       └── module.json5          //模块library的配置文件
13. │   ├── oh-package.json5              //模块级
14. │   ├── index.ets                     //入口文件index.ets
15. │   └── build-profile.json5           //模块级
16. └── build-profile.json5               //工程级
```

## 开发

介绍如何导出HSP的ArkUI组件、接口、资源，供应用内的其他HAP/HSP引用。

### 导出ArkUI组件

ArkUI组件可以通过export导出，例如：

```
1. // library/src/main/ets/components/MyTitleBar.ets
2. @Component
3. export struct MyTitleBar {
4. build() {
5. Row() {
6. Text($r('app.string.library_title'))
7. .id('library')
8. .fontFamily('HarmonyHeiTi')
9. .fontWeight(FontWeight.Bold)
10. .fontSize(32)
11. .fontColor($r('app.color.text_color'))
12. }
13. .width('100%')
14. }
15. }
```

[MyTitleBar.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/InAppHsp1/library/src/main/ets/components/MyTitleBar.ets#L16-L32)

在入口文件 index.ets 中声明对外暴露的接口。

```
1. // library/index.ets
2. export { MyTitleBar } from './src/main/ets/components/MyTitleBar';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/InAppHsp1/library/Index.ets#L25-L30)

### 导出类和方法

通过export导出类和方法，例如：

```
1. // library/src/main/ets/utils/test.ets
2. export class Log {
3. static info(msg: string): void {
4. console.info(msg);
5. }
6. }

8. export function add(a: number, b: number): number {
9. return a + b;
10. }

12. export function minus(a: number, b: number): number {
13. return a - b;
14. }
```

[test.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/InAppHsp1/library/src/main/ets/utils/test.ets#L16-L31)

在入口文件 index.ets 中声明对外暴露的接口。

```
1. // library/index.ets
2. export { Log, add, minus } from './src/main/ets/utils/test';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/InAppHsp1/library/Index.ets#L19-L24)

### 导出native方法

在HSP中也可以包含C++编写的so。对于so中的native方法，HSP通过间接的方式导出，以导出liblibrary.so的乘法接口multi为例：

```
1. // library/src/main/ets/utils/nativeTest.ets
2. import native from 'liblibrary.so';

4. export function nativeMulti(a: number, b: number): number {
5. let result: number = native.multi(a, b);
6. return result;
7. }
```

[nativeTest.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/InAppHsp1/library/src/main/ets/utils/nativeTest.ets#L16-L24)

在入口文件 index.ets 中声明对外暴露的接口。

```
1. // library/index.ets
2. export { nativeMulti } from './src/main/ets/utils/nativeTest';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/InAppHsp1/library/Index.ets#L37-L41)

### 通过$r访问HSP中的资源

在组件中，经常需要使用字符串、图片等资源。HSP中的组件需要使用资源时，一般将其所用资源放在HSP包内，而非放在HSP的使用方处，以符合高内聚低耦合的原则。

在工程中，常通过$r/$rawfile的形式引用应用资源。可以用$r/$rawfile访问本模块resources目录下的资源，如访问resources目录下定义的图片src/main/resources/base/media/example.png时，可以用$r("app.media.example")。有关$r/$rawfile的使用方式，请参阅文档[资源分类与访问](resource-categories-and-access.md)中“资源访问-应用资源”小节。

不推荐使用相对路径的方式，容易引用错误路径。例如：

当要引用上述同一图片资源时，在HSP模块中使用Image("../../resources/base/media/example.png")，实际上该Image组件访问的是HSP调用方（如entry）下的资源entry/src/main/resources/base/media/example.png。

```
1. // library/src/main/ets/pages/Index.ets
2. // 正确用例
3. Image($r('app.media.example'))
4. .id('example')
5. .borderRadius('48px')
6. // // 错误用例
7. Image("../../resources/base/media/example.png")
8. .id('example1')
9. .borderRadius('48px')
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/InAppHsp1/library/src/main/ets/pages/Index.ets#L36-L46)

### 导出HSP中的资源

跨包访问HSP内资源时，推荐实现一个资源管理类，以封装对外导出的资源。采用这种方式，具有如下优点：

* HSP开发者可以控制自己需要导出的资源，不需要对外暴露的资源可以不用导出。
* 使用方无须感知HSP内部的资源名称。当HSP内部的资源名称发生变化时，也不需要使用方跟着修改。

其具体实现如下：

将需要对外提供的资源封装为一个资源管理类：

```
1. // library/src/main/ets/ResManager.ets
2. export class ResManager{
3. static getPic(): Resource{
4. return $r('app.media.pic');
5. }
6. static getDesc(): Resource{
7. return $r('app.string.shared_desc');
8. }
9. }
```

[ResManager.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/InAppHsp1/library/src/main/ets/ResManager.ets#L16-L26)

在入口文件 index.ets 中声明对外暴露的接口。

```
1. // library/index.ets
2. export { ResManager } from './src/main/ets/ResManager';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/InAppHsp1/library/Index.ets#L31-L36)

## 使用

介绍如何引用HSP中的接口，以及如何通过页面路由实现HSP的pages页面跳转与返回。

### 引用HSP中的接口

要使用HSP中的接口，首先需要在使用方的 oh-package.json5 文件中配置对它的依赖。具体配置方法请参考[引用动态共享包](ide-har-import.md)。

依赖配置成功后，就可以像使用HAR一样调用HSP的对外接口了。例如，上面的library已经导出了下面这些接口：

```
1. // library/index.ets
2. // ...
3. export { Log, add, minus } from './src/main/ets/utils/test';
4. // ...
5. export { MyTitleBar } from './src/main/ets/components/MyTitleBar';
6. // ...
7. export { ResManager } from './src/main/ets/ResManager';
8. // ...
9. export { nativeMulti } from './src/main/ets/utils/nativeTest';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/InAppHsp1/library/Index.ets#L16-L42)

在使用方的代码中，可以这样使用：

```
1. // entry/src/main/ets/pages/index.ets
2. import { Log, add, MyTitleBar, ResManager, nativeMulti } from 'library';
3. import { BusinessError } from "@kit.BasicServicesKit";
4. import { application} from '@kit.AbilityKit';

6. const TAG = 'Index';

8. @Entry
9. @Component
10. struct Index {
11. @State message: string = '';

13. build() {
14. Column() {
15. List() {
16. ListItem() {
17. MyTitleBar()
18. }
19. .margin({ left: '35px', top: '32px' })

21. ListItem() {
22. Text(this.message)
23. .fontFamily('HarmonyHeiTi')
24. .fontSize(18)
25. .textAlign(TextAlign.Start)
26. .width('100%')
27. .fontWeight(FontWeight.Bold)
28. }
29. .width('685px')
30. .margin({ top: 30, bottom: 10 })

32. ListItem() {
33. // ResManager返回的Resource对象，可以传给组件直接使用，也可以从中取出资源来使用
34. Image(ResManager.getPic())
35. .id('image')
36. .borderRadius('48px')
37. }
38. .width('685px')
39. .margin({ top: 10, bottom: 10 })
40. .padding({ left: 12, right: 12, top: 4, bottom: 4 })

42. ListItem() {
43. Text($r('app.string.add'))
44. .fontSize(18)
45. .textAlign(TextAlign.Start)
46. .width('100%')
47. .fontWeight(500)
48. .height('100%')
49. }
50. .id('add')
51. .borderRadius(24)
52. .width('685px')
53. .height('84px')
54. .backgroundColor($r('sys.color.ohos_id_color_foreground_contrary'))
55. .margin({ top: 10, bottom: 10 })
56. .padding({ left: 12, right: 12, top: 4, bottom: 4 })
57. .onClick(() => {
58. Log.info('add button click!');
59. this.message = 'result: ' + add(1, 2);
60. })

62. ListItem() {
63. Text(ResManager.getDesc())
64. .fontSize(18)
65. .textAlign(TextAlign.Start)
66. .width('100%')
67. .fontWeight(500)
68. .height('100%')
69. }
70. .id('getStringValue')
71. .borderRadius(24)
72. .width('685px')
73. .height('84px')
74. .backgroundColor($r('sys.color.ohos_id_color_foreground_contrary'))
75. .margin({ top: 10, bottom: 10 })
76. .padding({ left: 12, right: 12, top: 4, bottom: 4 })
77. .onClick(() => {
78. // 先通过当前application.createModuleContext获取hsp模块的上下文，再获取hsp模块的resourceManager，然后再调用resourceManager的接口获取资源
79. application.createModuleContext(this.getUIContext()?.getHostContext(), "library").then((context:Context)=>{
80. context.resourceManager.getStringValue(ResManager.getDesc().id)
81. .then(value => {
82. console.info('getStringValue is ' + value);
83. this.message = 'getStringValue is ' + value;
84. })
85. .catch((err: BusinessError) => {
86. console.error('getStringValue promise error is ' + err);
87. });
88. }).catch((err: BusinessError) => {
89. console.error('createModuleContext promise error is ' + err);
90. });
91. })

93. ListItem() {
94. Text($r('app.string.native_multi'))
95. .fontSize(18)
96. .textAlign(TextAlign.Start)
97. .width('100%')
98. .fontWeight(500)
99. .height('100%')
100. }
101. .id('nativeMulti')
102. .borderRadius(24)
103. .width('685px')
104. .height('84px')
105. .backgroundColor($r('sys.color.ohos_id_color_foreground_contrary'))
106. .margin({ top: 10, bottom: 10 })
107. .padding({ left: 12, right: 12, top: 4, bottom: 4 })
108. .onClick(() => {
109. Log.info('nativeMulti button click!');
110. this.message = 'result: ' + nativeMulti(3, 4);
111. })
112. }
113. .alignListItem(ListItemAlign.Center)
114. }
115. .width('100%')
116. .backgroundColor($r('app.color.page_background'))
117. .height('100%')
118. }
119. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/InAppHsp1/entry/src/main/ets/pages/Index.ets#L16-L136)

### 页面跳转和返回

开发者想在entry模块中，添加一个按钮跳转至library模块中的menu页面（路径为：library/src/main/ets/pages/library\_menu.ets），那么可以在使用方的代码（entry模块下的Index.ets，路径为：entry/src/main/ets/pages/Index.ets）里这样使用：

```
1. @Entry
2. @Component
3. struct Index {
4. @State message: string = '';
5. pathStack: NavPathStack = new NavPathStack();

7. build() {
8. Navigation(this.pathStack) {
9. Column() {
10. List() {
11. ListItem() {
12. Text($r('app.string.click_to_menu'))
13. .fontSize(18)
14. .textAlign(TextAlign.Start)
15. .width('100%')
16. .fontWeight(500)
17. .height('100%')
18. }
19. .id('clickToMenu')
20. .borderRadius(24)
21. .width('685px')
22. .height('84px')
23. .backgroundColor($r('sys.color.ohos_id_color_foreground_contrary'))
24. .margin({ top: 10, bottom: 10 })
25. .padding({
26. left: 12,
27. right: 12,
28. top: 4,
29. bottom: 4
30. })
31. .onClick(() => {
32. this.pathStack.pushPathByName('library_menu', null)
33. })
34. }
35. .alignListItem(ListItemAlign.Center)
36. }
37. .width('100%')
38. .backgroundColor($r('app.color.page_background'))
39. .height('100%')
40. }.title("Navigation_Index")
41. .mode(NavigationMode.Stack)
42. }
43. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/InAppHsp2/entry/src/main/ets/pages/Index.ets#L16-L60)

在library下新增page文件（library/src/main/ets/pages/library\_menu.ets），其中'back\_to\_index'的按钮返回上一页。

```
1. @Builder
2. export function PageOneBuilder() {
3. Library_Menu()
4. }

6. @Component
7. export struct Library_Menu {
8. @State message: string = 'Hello World';
9. pathStack: NavPathStack = new NavPathStack();

11. build() {
12. NavDestination() {
13. Row() {
14. Column() {
15. Text(this.message)
16. .fontSize($r('app.float.page_text_font_size'))
17. .fontWeight(FontWeight.Bold)
18. .onClick(() => {
19. this.message = 'Welcome';
20. })
21. Button('back_to_index').fontSize(50).onClick(() => {
22. this.pathStack.pop();
23. })
24. }
25. .width('100%')
26. }
27. .height('100%')
28. }.title('Library_Menu')
29. .onReady((context: NavDestinationContext) => {
30. this.pathStack = context.pathStack;
31. })
32. }
33. }
```

[library\_menu.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/InAppHsp2/library/src/main/ets/pages/library_menu.ets#L16-L51)

需要在library模块下新增route\_map.json文件（library/src/main/resources/base/profile/route\_map.json）。

```
1. {
2. "routerMap": [
3. {
4. "name": "library_menu",
5. "pageSourceFile": "src/main/ets/pages/library_menu.ets",
6. "buildFunction": "PageOneBuilder",
7. "data": {
8. "description": "this is library_menu"
9. }
10. }
11. ]
12. }
```

在library模块下的配置文件（library/src/main/module.json5）中配置json文件。

```
1. {
2. "module": {
3. "name": "library",
4. "type": "shared",
5. "description": "$string:shared_desc",
6. "deviceTypes": [
7. "tablet",
8. "2in1"
9. ],
10. "deliveryWithInstall": true,
11. "pages": "$profile:main_pages",
12. "routerMap": "$profile:route_map" // 新增配置，指向route_map.json文件
13. }
14. }
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/InAppHsp2/library/src/main/module.json5#L16-L31)

页面跳转和页面返回都使用了Navigation的特性，详情参考[Navigation跳转](arkts-navigation-jump.md#路由操作)。
