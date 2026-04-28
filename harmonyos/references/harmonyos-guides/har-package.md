---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/har-package
title: HAR
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 应用程序包基础知识 > 应用程序包开发与使用 > HAR
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:27+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:478ab8d4d06059426d1a011e2e94f977a6eecd8acf0ee3ddec4de2a923dba22d
---

HAR（Harmony Archive）是静态共享包，可以包含代码、C++库、资源和配置文件。通过HAR可以实现多个模块或多个工程共享ArkUI组件、资源等相关代码。

## 使用场景

* 支持应用内共享，也可以作为二方库（SDK）、三方库（SDK）发布后供其他应用使用。
* 作为二方库（SDK），发布到[OHPM私仓](ide-ohpm-repo.md)，供公司内部其他应用使用。
* 作为三方库（SDK），发布到[OHPM中心仓](https://ohpm.openharmony.cn/#/cn/home)，供其他应用使用。

## 约束限制

* HAR不支持在设备上单独安装或运行，只能作为应用模块的依赖项被引用。
* 从API version 14开始，HAR支持在配置文件中声明[UIAbility](uiability-overview.md)组件，配置UIAbility的方法参考[在模块中添加Ability](ide-add-new-ability.md#section18658758104318)，拉起HAR中UIAbility的方式与[启动应用内的UIAbility](uiability-intra-device-interaction.md)方法相同。

说明

如果使用[startAbility](../harmonyos-references/js-apis-inner-application-uiabilitycontext.md#startability)接口拉起HAR中的UIAbility，接口参数中的moduleName取值需要为依赖该HAR的[HAP](hap-package.md)/[HSP](in-app-hsp.md)的moduleName。

* 从API version 18开始，HAR支持在配置文件中声明[ExtensionAbility](extensionability-overview.md)组件，但不支持具有入口能力的ExtensionAbility（即skill标签配置了entity.system.home和ohos.want.action.home）。HAR中配置ExtensionAbility的方法和支持的类型请参考[模块中添加ExtensionAbility](ide-add-new-ability.md#section18891639459)。API version 17及之前版本，不支持在配置文件中声明[ExtensionAbility](extensionability-overview.md)组件。
* HAR不支持在配置文件中声明[pages](module-configuration-file.md#pages标签)页面，但是可以包含pages页面，并通过[Navigation跳转](arkts-navigation-jump.md#路由操作)的方式进行跳转。
* HAR不支持引用AppScope目录中的资源。在编译构建时，AppScope中的内容不会打包到HAR中，因此会导致HAR资源引用失败。
* 由于HSP仅支持应用内共享，如果HAR依赖了HSP，则该HAR文件仅支持应用内共享，不支持发布到二方仓或三方仓供其他应用使用，否则会导致编译失败。
* 多包（HAP/HSP）引用相同的HAR时，会造成多包间代码和资源的重复拷贝，从而导致应用包变大。
* HAR可以依赖其他HAR或者HSP，但不支持循环依赖，也不支持依赖传递。
* HAP引用HAR时，在编译构建过程中系统会自动合并两者的权限配置。因此开发者无需在HAP和HAR中重复申请相同权限。

说明

循环依赖：例如有三个HAR，HAR-A、HAR-B和HAR-C，循环依赖指HAR-A依赖HAR-B，HAR-B依赖HAR-C，HAR-C又依赖HAR-A。

依赖传递：例如有三个HAR，HAR-A、HAR-B和HAR-C，依赖关系是HAR-A依赖HAR-B，HAR-B依赖HAR-C。不支持传递依赖指HAR-A可以使用HAR-B的方法和组件，但是HAR-A不能直接使用HAR-C的方法和组件。

## 创建

开发者可以通过DevEco Studio创建一个用于调用C++代码的HAR模块，创建过程中需要在Configure New Module界面中开启Enable native。详见[创建库模块](ide-har.md#section643521083015)。

## 开发

介绍如何导出HAR的ArkUI组件、接口、资源，供其他应用或当前应用的其他模块引用。

Index.ets文件是HAR导出声明文件的入口，HAR需要导出的接口，统一在Index.ets文件中导出。Index.ets文件是DevEco Studio默认自动生成的，开发者也可以自定义，在模块的oh-package.json5文件中的main字段配置入口声明文件，配置如下所示：

```
1. {
2. // ...
3. "main": "Index.ets",
4. // ...
5. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarPackage/library/oh-package.json5#L16-L40)

说明

HAR在和宿主应用一起编译时，会把HAR的代码直接编译到宿主应用中，HAR包是一个编译中间态产物，不是最终的运行实体。运行时，HAR运行的身份信息是其宿主应用，系统会以宿主应用的版本做行为区分。如果需要在HAR中区分宿主应用的版本做不同的行为区分，可以调用[getBundleInfoForSelf](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagergetbundleinfoforself)接口，获取宿主应用的targetVersion，然后根据不同的targetVersion，做不同的逻辑处理。

### 导出ArkUI组件

通过export导出ArkUI组件，示例如下：

```
1. // library/src/main/ets/components/mainpage/MainPage.ets
2. @Component
3. export struct MainPage {
4. @State message: string = 'HAR MainPage';

6. build() {
7. Column() {
8. Row() {
9. Text(this.message)
10. .fontSize(32)
11. .fontWeight(FontWeight.Bold)
12. }
13. .margin({ top: '32px' })
14. .height(56)
15. .width('624px')

17. Flex({ justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center, alignContent: FlexAlign.Center }) {
18. Column() {
19. Image($r('app.media.pic_empty')).width('33%')
20. Text($r('app.string.empty'))
21. .fontSize(14)
22. .fontColor($r('app.color.text_color'))
23. }
24. }.width('100%')
25. .height('90%')
26. }
27. .width('100%')
28. .height('100%')
29. .backgroundColor($r('app.color.page_background'))
30. }
31. }
```

[MainPage.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarPackage/library/src/main/ets/components/mainpage/MainPage.ets#L16-L48)

HAR对外暴露的接口，在Index.ets导出文件中声明如下所示：

```
1. // library/Index.ets
2. export { MainPage } from './src/main/ets/components/mainpage/MainPage';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarPackage/library/Index.ets#L16-L19)

### 导出类和方法

通过export导出类和方法，支持导出多个类和方法，示例如下所示：

```
1. // library/src/main/ets/test.ets
2. export class Log {
3. static info(msg: string) {
4. console.info(msg);
5. }
6. }

8. export function func() {
9. return 'har func';
10. }

12. export function func2() {
13. return 'har func2';
14. }
```

[test.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarPackage/library/src/main/ets/test.ets#L16-L31)

HAR对外暴露的接口，在Index.ets导出文件中声明如下所示：

```
1. // library/Index.ets
2. export { Log, func, func2 } from './src/main/ets/test';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarPackage/library/Index.ets#L20-L23)

### 导出native方法

在HAR中也可以包含C++编写的so。对于so中的native方法，HAR通过以下方式导出，以导出liblibrary.so的加法接口add为例：

```
1. // library/src/main/ets/utils/nativeTest.ets
2. import native from 'liblibrary.so';

4. export function nativeAdd(a: number, b: number): number {
5. let result: number = native.add(a, b);
6. return result;
7. }
```

[nativeTest.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarPackage/library/src/main/ets/utils/nativeTest.ets#L16-L24)

HAR对外暴露的接口，在Index.ets导出文件中声明如下所示：

```
1. // library/Index.ets
2. export { nativeAdd } from './src/main/ets/utils/nativeTest';
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarPackage/library/Index.ets#L24-L27)

### 导出资源

在编译构建HAP时，DevEco Studio会从HAP模块及依赖的模块中收集资源文件，如果不同模块下的资源文件出现重名冲突时，DevEco Studio会按照以下优先级进行覆盖（优先级由高到低）：

* AppScope（仅Stage模型支持）。
* HAP包自身模块。
* 依赖的HAR模块，如果依赖的多个HAR之间有资源冲突，会按照工程oh-package.json5中dependencies下的依赖顺序进行覆盖，依赖顺序在前的优先级较高。例如下方示例中dayjs和lottie中包含同名文件时，会优先使用dayjs中的资源。

  说明

  如果在AppScope、HAP模块或HAR模块的国际化目录中配置了资源，在相同的国际化限定词下，合并的优先级也遵循上述规则。同时，国际化限定词中配置的优先级高于在base中的配置。例如，在AppScope的base中配置了资源字段，在HAR模块的en\_US中配置了同样的资源字段，则在en\_US的使用场景中，会更优先使用HAR模块中配置的资源字段。

```
1. {
2. // ...
3. "dependencies": {
4. // ...
5. "dayjs": "file:../dayjs",
6. "lottie": "file:../lottie",
7. },
8. }
```

[oh-package.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarPackage/library/oh-package.json5#L17-L39)

## 使用

介绍如何配置HAR依赖，并引用HAR的ArkUI组件、接口、资源。

引用HAR前，需要先配置对HAR的依赖，详见[引用HAR文件和资源](ide-har-import.md)。

### 引用HAR的ArkUI组件

HAR的依赖配置成功后，可以引用HAR的ArkUI组件。通过import引入HAR导出的ArkUI组件，示例如下所示：

```
1. // entry/src/main/ets/pages/IndexSec.ets
2. import { MainPage } from 'library';

4. @Entry
5. @Component
6. struct IndexSec {
7. build() {
8. Row() {
9. // 引用HAR的ArkUI组件
10. MainPage()
11. }
12. .height('100%')
13. }
14. }
```

[IndexSec.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarPackage/entry/src/main/ets/pages/IndexSec.ets#L16-L31)

### 引用HAR的类和方法

通过import引用HAR导出的类和方法，示例如下所示：

```
1. // entry/src/main/ets/pages/Index.ets
2. import { Log, func } from 'library';
3. // ...
4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. build() {
10. Column() {
11. Text(this.message)
12. .fontFamily('HarmonyHeiTi')
13. .fontWeight(FontWeight.Bold)
14. .fontSize(32)

16. // 引用HAR的ets类和方法
17. Button($r('app.string.button'))
18. .id('button')
19. .height(48)
20. .width('624px')
21. .margin({ top: '4%' })
22. .type(ButtonType.Capsule)
23. .onClick(() => {
24. // 引用HAR的类和方法
25. Log.info('har msg');
26. this.message = 'func return: ' + func();
27. })
28. // ...

30. // ...
31. }
32. .width('100%')
33. .backgroundColor($r('app.color.page_background'))
34. .height('100%')
35. }
36. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarPackage/entry/src/main/ets/pages/Index.ets#L16-L104)

### 引用HAR的native方法

通过import引用HAR导出的native方法，示例如下所示：

```
1. // entry/src/main/ets/pages/Index.ets
2. import { nativeAdd } from 'library';
3. // ...
4. @Entry
5. @Component
6. struct Index {
7. @State message: string = 'Hello World';

9. build() {
10. Column() {
11. Text(this.message)
12. .fontFamily('HarmonyHeiTi')
13. .fontWeight(FontWeight.Bold)
14. .fontSize(32)

16. // ...
17. // 引用HAR的native方法
18. Button($r('app.string.native_add'))
19. .id('nativeAdd')
20. .height(48)
21. .width('624px')
22. .margin({ top: '4%', bottom: '6%' })
23. .type(ButtonType.Capsule)
24. .onClick(() => {
25. this.message = 'result: ' + nativeAdd(1, 2);
26. })

28. // ...
29. }
30. .width('100%')
31. .backgroundColor($r('app.color.page_background'))
32. .height('100%')
33. }
34. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarPackage/entry/src/main/ets/pages/Index.ets#L20-L103)

### 引用HAR的资源

通过$r引用HAR中的资源，例如在HAR模块的src/main/resources里添加字符串资源（在string.json中定义，name：hello\_har）和图片资源（icon\_har.png），然后在Entry模块中引用该字符串和图片资源的示例如下所示：

```
1. // entry/src/main/ets/pages/Index.ets
2. @Entry
3. @Component
4. struct Index {
5. @State message: string = 'Hello World';

7. build() {
8. Column() {
9. Text(this.message)
10. .fontFamily('HarmonyHeiTi')
11. .fontWeight(FontWeight.Bold)
12. .fontSize(32)

14. // ...

16. // 引用HAR的字符串资源
17. Text($r('app.string.hello_har'))
18. .id('stringHar')
19. .fontFamily('HarmonyHeiTi')
20. .fontColor($r('app.color.text_color'))
21. .fontSize(24)
22. .fontWeight(500)
23. .margin({ top: '40%' })

25. List() {
26. ListItem() {
27. // 引用HAR的图片资源
28. Image($r('app.media.icon_har'))
29. .id('iconHar')
30. .borderRadius('48px')
31. }
32. .margin({ top: '5%' })
33. .width('312px')
34. }
35. .alignListItem(ListItemAlign.Center)
36. }
37. .width('100%')
38. .backgroundColor($r('app.color.page_background'))
39. .height('100%')
40. }
41. }
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarPackage/entry/src/main/ets/pages/Index.ets#L24-L102)

## 构建

详情请参见[构建HAR](ide-hvigor-build-har.md)。

### 混淆配置

HAR可以作为二方库和三方库提供给其他应用使用，如果需要对代码资产进行保护，建议[开启混淆](source-obfuscation-guide.md#开启源码混淆)。

[混淆能力](source-obfuscation.md)开启后，DevEco Studio在构建HAR时，会对代码进行编译、混淆及压缩处理，保护代码资产。

HAR模块原先默认开启混淆能力，会对API 10及以上的HAR模块，且编译模块为release时，自动进行简单的代码混淆；**从DevEco Studio 5.0.3.600开始，新建工程默认关闭代码混淆功能**，可以在HAR模块的build-profile.json5文件中的ruleOptions字段下的enable进行开启混淆，详情请见[代码混淆](ide-build-obfuscation.md)，配置如下所示：

```
1. {
2. "apiType": "stageMode",
3. "buildOption": {
4. // ...
5. },
6. "buildOptionSet": [
7. {
8. "name": "release",
9. "arkOptions": {
10. "obfuscation": {
11. "ruleOptions": {
12. "enable": true,
13. "files": [
14. "./obfuscation-rules.txt"
15. ]
16. },
17. "consumerFiles": [
18. "./consumer-rules.txt"
19. ]
20. }
21. },
22. // ...
23. },
24. ],
25. "targets": [
26. {
27. "name": "default"
28. },
29. // ...
30. ]
31. }
```

[build-profile.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HarPackage/library/build-profile.json5#L16-L65)

## 发布

详见[发布HAR](ide-har-publish.md)。
