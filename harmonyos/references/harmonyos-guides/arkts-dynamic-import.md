---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-dynamic-import
title: 动态加载
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS运行时 > ArkTS模块化 > 动态加载
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:44+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:889cb6c0f6fa06901e64769058f1f7649bf081b957a6f1b6b2704c8700187311
---

动态import支持条件延迟加载，支持部分反射功能，可以提升页面的加载速度；动态import支持加载HSP模块/HAR模块/OHPM包/Native库等，并且HAR模块之间可通过变量动态import来访问彼此导出的内容，可避免编译期强依赖，实现模块解耦。

## 技术适用场景介绍

应用开发的有些场景中，如果希望根据条件导入模块或者按需导入模块，可以使用动态import代替[静态import](introduction-to-arkts.md#导入)。下面是可能会需要动态import的场景：

* 当静态import的模块明显降低了代码的加载速度且很少被使用，或者并不需要马上使用它。
* 当静态import的模块明显占用了大量的系统内存且很少被使用。
* 当被导入的模块，在加载时并不存在，需要异步获取。
* 当需要动态构建模块说明符时，应使用动态import。静态import仅支持静态说明符。
* 当导入的模块存在副作用（即模块中包含直接运行的代码），这些副作用仅在满足特定条件时才需要。

## 业务扩展场景介绍

动态import在业务上除了能实现条件延迟加载，还可以实现部分反射功能。实例如下，HAP动态import HAR包harlibrary，并调用类Calc的静态成员函数staticAdd()、成员函数instanceAdd()，以及全局方法addHarLibrary()。

```
1. // harlibrary's src/main/ets/utils/Calc.ets
2. export class Calc {
3. public static staticAdd(a: number, b: number): number {
4. let c = a + b;
5. console.info('DynamicImport I am harlibrary in staticAdd, %d + %d = %d', a, b, c);
6. return c;
7. }

9. public instanceAdd(a: number, b: number): number {
10. let c = a + b;
11. console.info('DynamicImport I am harlibrary in instanceAdd, %d + %d = %d', a, b, c);
12. return c;
13. }
14. }

16. export function addHarLibrary(a: number, b: number): number {
17. let c = a + b;
18. console.info('DynamicImport I am harlibrary in addHarLibrary, %d + %d = %d', a, b, c);
19. return c;
20. }
```

```
1. // harlibrary's Index.ets
2. export { Calc, addHarLibrary } from './src/main/ets/utils/Calc'
```

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "harlibrary": "file:../harlibrary"
4. }
```

```
1. // HAP's src/main/ets/pages/Index.ets
2. import('harlibrary').then((ns:ESObject) => {
3. ns.Calc.staticAdd(8, 9);  // 调用静态成员函数staticAdd()
4. let calc:ESObject = new ns.Calc();  // 实例化类Calc
5. calc.instanceAdd(10, 11);  // 调用成员函数instanceAdd()
6. ns.addHarLibrary(6, 7);  // 调用全局方法addHarLibrary()

8. // 使用类、成员函数和方法的字符串名字进行反射调用
9. let className = 'Calc';
10. let methodName = 'instanceAdd';
11. let staticMethod = 'staticAdd';
12. let functionName = 'addHarLibrary';
13. ns[className][staticMethod](12, 13);  // 调用静态成员函数staticAdd()
14. let calc1:ESObject = new ns[className]();  // 实例化类Calc
15. calc1[methodName](14, 15);  // 调用成员函数instanceAdd()
16. ns[functionName](16, 17);  // 调用全局方法addHarLibrary()
17. });
```

## 动态import实现方案介绍

动态import根据入参是常量或变量，分为动态import常量表达式和动态import变量表达式两大特性规格。

以下是动态import支持的规格列表：

| 动态import场景 | 动态import详细分类 | 说明 |
| --- | --- | --- |
| 本地工程模块 | 动态import模块内文件路径 | 要求路径以./或../开头。 |
| 本地工程模块 | 动态import HSP模块名 | - |
| 本地工程模块 | 动态import HSP模块文件路径 | - |
| 本地工程模块 | 动态import HAR模块名 | - |
| 本地工程模块 | 动态import HAR模块文件路径 | - |
| 远程包 | 动态import远程HAR模块名 | - |
| 远程包 | 动态import ohpm包名 | - |
| API | 动态import @system.\* | - |
| API | 动态import @ohos.\* | - |
| API | 动态import @arkui-x.\* | - |
| 模块Native库 | 动态import libNativeLibrary.so | - |

说明

1.当前所有import中使用的模块名都是依赖方oh-package.json5文件中dependencies项的别名。

2.本地模块在依赖方的dependencies中配置的别名建议与moduleName以及packageName三者一致。moduleName指的是被依赖的HSP/HAR的module.json5中配置的名字，packageName指的是被依赖的HSP/HAR的oh-package.json5中配置的名字。

3.import一个模块名，实际的行为是import该模块的入口文件，一般为Index.ets/ts。

## 动态import实现中的关键点

### 动态import常量表达式

动态import常量表达式是指动态import的入参为常量的场景。下面以HAP引用其他模块的API的示例来说明典型用法。

本文示例代码中的路径，如Index.ets，是根据当前DevEco Studio的模块配置设置的。如果后续有变化，请调整文件的位置和相对路径。

* **HAP常量动态import HAR模块名**

  ```
  1. // HAR's Index.ets
  2. export function add(a: number, b: number): number {
  3. let c = a + b;
  4. console.info('DynamicImport I am a HAR, %d + %d = %d', a, b, c);
  5. return c;
  6. }
  ```

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. import('myhar').then((ns:ESObject) => {
  3. console.info('DynamicImport ns.add(3, 5) = %d', ns.add(3, 5));
  4. });

  6. // 可使用 await 处理动态import (必须在 async 函数内使用)
  7. async function asyncDynamicImport() {
  8. let ns:ESObject = await import('myhar');
  9. console.info('DynamicImport ns.add(3, 5) = %d', ns.add(3, 5));
  10. }
  ```

  ```
  1. // HAP's oh-package.json5
  2. "dependencies": {
  3. "myhar": "file:../myhar"
  4. }
  ```
* **HAP常量动态import HAR模块文件路径**

  ```
  1. // HAR's Index.ets
  2. export function add(a: number, b: number): number {
  3. let c = a + b;
  4. console.info('DynamicImport I am a HAR, %d + %d = %d', a, b, c);
  5. return c;
  6. }
  ```

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. import('myhar/Index').then((ns:ESObject) => {
  3. console.info('DynamicImport ns.add(3, 5) = %d', ns.add(3, 5));
  4. });
  ```

  ```
  1. // HAP's oh-package.json5
  2. "dependencies": {
  3. "myhar": "file:../myhar"
  4. }
  ```
* **HAP常量动态import HSP模块名**

  ```
  1. // HSP's Index.ets
  2. export function add(a: number, b: number): number {
  3. let c = a + b;
  4. console.info('DynamicImport I am a HSP, %d + %d = %d', a, b, c);
  5. return c;
  6. }
  ```

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. import('myhsp').then((ns:ESObject) => {
  3. console.info('DynamicImport ns.add(3, 5) = %d', ns.add(3, 5));
  4. });
  ```

  ```
  1. // HAP's oh-package.json5
  2. "dependencies": {
  3. "myhsp": "file:../myhsp"
  4. }
  ```
* **HAP常量动态import HSP模块名文件路径**

  ```
  1. // HSP's Index.ets
  2. export function add(a: number, b: number): number {
  3. let c = a + b;
  4. console.info('DynamicImport I am a HSP, %d + %d = %d', a, b, c);
  5. return c;
  6. }
  ```

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. import('myhsp/Index').then((ns:ESObject) => {
  3. console.info('DynamicImport ns.add(3, 5) = %d', ns.add(3, 5));
  4. });
  ```

  ```
  1. // HAP's oh-package.json5
  2. "dependencies": {
  3. "myhsp": "file:../myhsp"
  4. }
  ```
* **HAP常量动态import远程HAR模块名**

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. import('@ohos/crypto-js').then((ns:ESObject) => {
  3. console.info('DynamicImport @ohos/crypto-js: ' + ns.CryptoJS.MD5(123456));
  4. });
  ```

  ```
  1. // HAP's oh-package.json5
  2. "dependencies": {
  3. "@ohos/crypto-js": "2.0.3-rc.0"
  4. }
  ```
* **HAP常量动态import ohpm包**

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. import('json5').then((ns:ESObject) => {
  3. console.info('DynamicImport json5');
  4. });
  ```

  ```
  1. // HAP's oh-package.json5
  2. "dependencies": {
  3. "json5": "1.0.2"
  4. }
  ```
* **HAP常量动态import自己的单文件**

  ```
  1. // HAP's src/main/ets/Calc.ets
  2. export function add(a: number, b: number): number {
  3. let c = a + b;
  4. console.info('DynamicImport I am a HAP, %d + %d = %d', a, b, c);
  5. return c;
  6. }
  ```

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. import('../Calc').then((ns:ESObject) => {
  3. console.info('DynamicImport ns.add(3, 5) = %d', ns.add(3, 5));
  4. });
  ```
* **HAP常量动态import自己的Native库**

  ```
  1. // libnativeapi.so's index.d.ts
  2. export const add: (a: number, b: number) => number;
  ```

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. import('libnativeapi.so').then((ns:ESObject) => {
  3. console.info('DynamicImport libnativeapi.so: ' + ns.default.add(2, 3));
  4. });
  ```

  ```
  1. // HAP's oh-package.json5
  2. "dependencies": {
  3. "libnativeapi.so": "file:./src/main/cpp/types/libnativeapi"
  4. }
  ```
* **HAP常量动态import加载API**

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. import('@system.app').then((ns:ESObject) => { ns.default.terminate(); });
  3. import('@system.router').then((ns:ESObject) => { ns.default.clear(); });
  4. import('@ohos.curves').then((ns:ESObject) => { ns.default.springMotion(0.555, 0.75, 0.001); });
  5. import('@ohos.matrix4').then((ns:ESObject) => { ns.default.identity(); });
  6. import('@ohos.hilog').then((ns:ESObject) => { ns.default.info(0x0000, 'testTag', '%{public}s', 'DynamicImport @ohos.hilog.'); });
  ```

### 动态import变量表达式

DevEco Studio中模块间的依赖关系通过oh-package.json5中的dependencies字段进行配置。dependencies列表中所有的模块默认都会进行安装（本地模块）或下载（远程模块），但是不会默认参与编译。HAP/HSP编译时会以入口文件（一般为Index.ets/Index.ts）开始搜索依赖关系，搜索到的模块或文件才会加入编译。

在编译期，静态import和常量动态import可以被打包工具rollup及其插件识别解析，加入依赖树中，参与编译流程，最终生成方舟字节码。但是，如果是变量动态import，该变量值可能需要进行运算或外部传入才能得到，在编译态无法解析其内容，也就无法加入编译。为了将这部分模块/文件加入编译，还需要额外增加一个runtimeOnly的buildOption配置，用于指定动态import的变量实际的模块名或文件路径。

**1. runtimeOnly字段schema配置格式**

在HAP/HSP/HAR的build-profile.json5中的buildOption中增加runtimeOnly配置项，仅在通过变量动态import时配置，静态import和常量动态import无需配置；并且，通过变量动态import加载API时也无需配置runtimeOnly。如下实例说明如何配置通过变量动态import其他模块，以及变量动态import本模块自己的单文件：

```
1. // 变量动态import其他模块myhar
2. let harName = 'myhar';
3. import(harName).then((obj: ESObject) => {
4. console.info('DynamicImport I am a har');
5. })

7. // 变量动态import本模块自己的单文件src/main/ets/index.ets
8. let filePath = './utils/Calc';
9. import(filePath).then((obj: ESObject) => {
10. console.info('DynamicImport I am a file');
11. })
```

对应的runtimeOnly配置：

```
1. "buildOption": {
2. "arkOptions": {
3. "runtimeOnly": {
4. "packages": [ "myhar" ],
5. "sources": [ "./src/main/ets/utils/Calc.ets" ]
6. }
7. }
8. }
```

"runtimeOnly"的"packages"：用于配置本模块变量动态import其他模块名，要求与dependencies中配置的名字一致。

"runtimeOnly"的"sources"：用于配置本模块变量动态import自己的文件路径，路径相对于当前build-profile.json5文件。

**2. 使用实例**

* **HAP变量动态import HAR模块名**

  ```
  1. // HAR's Index.ets
  2. export function add(a: number, b: number): number {
  3. let c = a + b;
  4. console.info('DynamicImport I am a HAR, %d + %d = %d', a, b, c);
  5. return c;
  6. }
  ```

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. let packageName = 'myhar';
  3. import(packageName).then((ns:ESObject) => {
  4. console.info('DynamicImport ns.add(3, 5) = %d', ns.add(3, 5));
  5. });
  ```

  ```
  1. // HAP's oh-package.json5
  2. "dependencies": {
  3. "myhar": "file:../myhar"
  4. }
  ```

  ```
  1. // HAP's build-profile.json5
  2. "buildOption": {
  3. "arkOptions": {
  4. "runtimeOnly": {
  5. "packages": [
  6. "myhar"  // 仅用于使用变量动态import其他模块名场景，静态import或常量动态import无需配置。
  7. ]
  8. }
  9. }
  10. }
  ```
* **HAP变量动态import HSP模块名**

  ```
  1. // HSP's Index.ets
  2. export function add(a: number, b: number): number {
  3. let c = a + b;
  4. console.info('DynamicImport I am a HSP, %d + %d = %d', a, b, c);
  5. return c;
  6. }
  ```

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. let packageName = 'myhsp';
  3. import(packageName).then((ns:ESObject) => {
  4. console.info('DynamicImport ns.add(3, 5) = %d', ns.add(3, 5));
  5. });
  ```

  ```
  1. // HAP's oh-package.json5
  2. "dependencies": {
  3. "myhsp": "file:../myhsp"
  4. }
  ```

  ```
  1. // HAP's build-profile.json5
  2. "buildOption": {
  3. "arkOptions": {
  4. "runtimeOnly": {
  5. "packages": [
  6. "myhsp"  // 仅用于使用变量动态import其他模块名场景，静态import或常量动态import无需配置。
  7. ]
  8. }
  9. }
  10. }
  ```
* **HAP变量动态import远程HAR模块名**

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. let packageName = '@ohos/crypto-js';
  3. import(packageName).then((ns:ESObject) => {
  4. console.info('DynamicImport @ohos/crypto-js: ' + ns.CryptoJS.MD5(123456));
  5. });
  ```

  ```
  1. // HAP's oh-package.json5
  2. "dependencies": {
  3. "@ohos/crypto-js": "2.0.3-rc.0"
  4. }
  ```

  ```
  1. // HAP's build-profile.json5
  2. "buildOption": {
  3. "arkOptions": {
  4. "runtimeOnly": {
  5. "packages": [
  6. "@ohos/crypto-js"  // 仅用于使用变量动态import其他模块名场景，静态import或常量动态import无需配置。
  7. ]
  8. }
  9. }
  10. }
  ```
* **HAP变量动态import ohpm包**

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. let packageName = 'json5';
  3. import(packageName).then((ns:ESObject) => {
  4. console.info('DynamicImport json5');
  5. });
  ```

  ```
  1. // HAP's oh-package.json5
  2. "dependencies": {
  3. "json5": "1.0.2"
  4. }
  ```

  ```
  1. // HAP's build-profile.json5
  2. "buildOption": {
  3. "arkOptions": {
  4. "runtimeOnly": {
  5. "packages": [
  6. "json5"  // 仅用于使用变量动态import其他模块名场景，静态import或常量动态import无需配置。
  7. ]
  8. }
  9. }
  10. }
  ```
* **HAP变量动态import自己的单文件**

  ```
  1. // HAP's src/main/ets/Calc.ets
  2. export function add(a: number, b: number): number {
  3. let c = a + b;
  4. console.info('DynamicImport I am a HAP, %d + %d = %d', a, b, c);
  5. return c;
  6. }
  ```

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. let filePath = '../Calc';
  3. import(filePath).then((ns:ESObject) => {
  4. console.info('DynamicImport ns.add(3, 5) = %d', ns.add(3, 5));
  5. });
  ```

  ```
  1. // HAP's build-profile.json5
  2. "buildOption": {
  3. "arkOptions": {
  4. "runtimeOnly": {
  5. "sources": [
  6. "./src/main/ets/Calc.ets"  // 仅用于使用变量动态import模块自己单文件场景，静态import或常量动态import无需配置。
  7. ]
  8. }
  9. }
  10. }
  ```
* **HAP变量动态import自己的Native库**

  ```
  1. // libnativeapi.so's index.d.ts
  2. export const add: (a: number, b: number) => number;
  ```

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. let soName = 'libnativeapi.so';
  3. import(soName).then((ns:ESObject) => {
  4. console.info('DynamicImport libnativeapi.so: ' + ns.default.add(2, 3));
  5. });
  ```

  ```
  1. // HAP's oh-package.json5
  2. "dependencies": {
  3. "libnativeapi.so": "file:./src/main/cpp/types/libnativeapi"
  4. }
  ```

  ```
  1. // HAP's build-profile.json5
  2. "buildOption": {
  3. "arkOptions": {
  4. "runtimeOnly": {
  5. "packages": [
  6. "libnativeapi.so"  // 仅用于使用变量动态import其他模块名场景，静态import或常量动态import无需配置。
  7. ]
  8. }
  9. }
  10. }
  ```
* **HAP变量动态import加载API**

  ```
  1. // HAP's src/main/ets/pages/Index.ets
  2. let packageName = '@system.app';
  3. import(packageName).then((ns:ESObject) => { ns.default.terminate(); });
  4. packageName = '@system.router';
  5. import(packageName).then((ns:ESObject) => { ns.default.clear(); });
  6. packageName = '@ohos.curves';
  7. import(packageName).then((ns:ESObject) => { ns.default.springMotion(0.555, 0.75, 0.001); });
  8. packageName = '@ohos.matrix4';
  9. import(packageName).then((ns:ESObject) => { ns.default.identity(); });
  10. packageName = '@ohos.hilog';
  11. import(packageName).then((ns:ESObject) => { ns.default.info(0x0000, 'testTag', '%{public}s', 'DynamicImport @ohos.hilog.'); });
  ```

通过变量动态import加载API时无需配置runtimeOnly。

### HAR模块间动态import依赖解耦

当应用包含多个HAR包，HAR包之间的依赖关系比较复杂。在DevEco Studio中配置依赖关系时，可能会形成循环依赖。这时，如果HAR之间的依赖关系中仅有变量动态import，可以将HAR包之间直接依赖关系转移到HAP/HSP中配置，HAR包之间无需配置依赖关系，从而达到HAR包间依赖解耦的目的。如下示意图：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/c3QI6t-iR4uX0YnNuTQR2A/zh-cn_image_0000002583477541.png?HW-CC-KV=V1&HW-CC-Date=20260427T233843Z&HW-CC-Expire=86400&HW-CC-Sign=34F860CC0FDA6F7E5CBF551BF60028A92D871B9260ABE1BCE1590CD67401CA48)

HAR之间的依赖关系转移至HAP/HSP后：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/a417rvIiTlS5_sCsAHWC0w/zh-cn_image_0000002552797892.png?HW-CC-KV=V1&HW-CC-Date=20260427T233843Z&HW-CC-Expire=86400&HW-CC-Sign=ADA7AE18537EC9BB79ED8D2E02FFBAA657E80EBE54A05A5F19E884668227021E)

**使用限制**

* 仅限在本地源码HAR包之间存在循环依赖时，使用该规避方案。
* 被转移依赖的HAR之间只能通过变量动态import，不能有静态import或常量动态import。
* 转移依赖时，需同时转移**dependencies**和**runtimeOnly**依赖配置。
* HSP不支持转移依赖。即：HAP->HSP1->HSP2->HSP3，这里的HSP2和HSP3不能转移到HAP上面。
* 转移依赖的整个链路上只能有HAR包，不能跨越HSP转移。即：HAP->HAR1->HAR2->HSP->HAR3->HAR4，HAR1对HAR2的依赖可以转移到HAP上，HAR3对HAR4的依赖可以转移到HSP上。但是，不能将HAR3或HAR4转移到HAP上。
* 如果引用了其他工程模块、远程包或集成HSP，需确保在[工程级build-profile.json5文件](ide-hvigor-build-profile-app.md)中的**useNormalizedOHMUrl**配置一致，同时设置为true或false，否则可能导致运行错误：**Cannot find dynamic-import module library**。

**使用实例**

下面的实例通过在单向依赖HAP->HAR1->HAR2->HAR3之上增加依赖HAR2->HAR1、HAR3->HAR1，形成了循环依赖。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/V2Fz5onET2GgOU-lPAhAog/zh-cn_image_0000002583477541.png?HW-CC-KV=V1&HW-CC-Date=20260427T233843Z&HW-CC-Expire=86400&HW-CC-Sign=209730394DF99546ED74B79B4376CA947EB30069A067ECDD210080F388438577)

```
1. // HAP's src/main/ets/pages/Index.ets
2. let harName = 'har1'
3. import(harName).then((ns: ESObject) => {
4. console.info('[DynamicImport] hap -> har1, 0 + 1 = ' + ns.classHar1.add(0, 1));
5. })

7. // HAR1's src/main/ets/utils/Calc.ets
8. export class classHar1 {
9. static isImportedHar2: boolean = false;

11. static add(a: number, b: number): number {
12. const c = a + b;
13. console.info('[DynamicImport] classHar1.add(), %d + %d = %d', a, b, c);

15. if (!classHar1.isImportedHar2) {
16. const harName = 'har2';
17. import(harName).then((ns: ESObject) => {
18. classHar1.isImportedHar2 = true;
19. console.info('[DynamicImport] har1 -> har2, 1 + 2 = ' + ns.classHar2.add(1, 2));
20. })
21. }

23. return c;
24. }
25. }
26. // HAR1's Index.ets
27. export { classHar1 } from './src/main/ets/utils/Calc';

29. // HAR2's src/main/ets/utils/Calc.ets
30. export class classHar2 {
31. static isImportedHar1: boolean = false;
32. static isImportedHar3: boolean = false;

34. static add(a: number, b: number): number {
35. const c = a + b;
36. console.info('[DynamicImport] classHar2.add(), %d + %d = %d', a, b, c);

38. if (!classHar2.isImportedHar1) {
39. const harName = 'har1';
40. import(harName).then((ns: ESObject) => {
41. classHar2.isImportedHar1 = true;
42. console.info('[DynamicImport] har2 -> har1, 2 + 1 = ' + ns.classHar1.add(2, 1));
43. })
44. }

46. if (!classHar2.isImportedHar3) {
47. const harName = 'har3';
48. import(harName).then((ns: ESObject) => {
49. classHar2.isImportedHar3 = true;
50. console.info('[DynamicImport] har2 -> har3, 2 + 3 = ' + ns.classHar3.add(2, 3));
51. })
52. }

54. return c;
55. }
56. }
57. // HAR2's Index.ets
58. export { classHar2 } from './src/main/ets/utils/Calc';

60. // HAR3's src/main/ets/utils/Calc.ets
61. export class classHar3 {
62. static isImportedHar1: boolean = false;

64. static add(a: number, b: number): number {
65. const c = a + b;
66. console.info('[DynamicImport] classHar3.add(), %d + %d = %d', a, b, c);

68. if (!classHar3.isImportedHar1) {
69. const harName = 'har1';
70. import(harName).then((ns: ESObject) => {
71. classHar3.isImportedHar1 = true;
72. console.info('[DynamicImport] har3 -> har1, 3 + 1 = ' + ns.classHar1.add(3, 1));
73. })
74. }

76. return c;
77. }
78. }
79. // HAR3's Index.ets
80. export { classHar3 } from './src/main/ets/utils/Calc';
```

若未对HAR之间的**dependencies**和**runtimeOnly**配置进行依赖解耦，ohpm无法解决循环依赖，依赖安装失败。

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "har1": "file:../har1"
4. }
5. // HAP's build-profile.json5
6. "buildOption": {
7. "arkOptions": {
8. "runtimeOnly": {
9. "packages": [ // 仅用于变量动态加载的场景，静态加载或常量动态加载无需配置。
10. "har1"
11. ]
12. }
13. }
14. }

16. // HAR1's oh-package.json5
17. "dependencies": {
18. "har2": "file:../har2"
19. }
20. // HAR1's build-profile.json5
21. "buildOption": {
22. "arkOptions": {
23. "runtimeOnly": {
24. "packages": [ // 仅用于变量动态加载的场景，静态加载或常量动态加载无需配置。
25. "har2"
26. ]
27. }
28. }
29. }

31. // HAR2's oh-package.json5
32. "dependencies": {
33. "har1": "file:../har1",
34. "har3": "file:../har3"
35. }
36. // HAR2's build-profile.json5
37. "buildOption": {
38. "arkOptions": {
39. "runtimeOnly": {
40. "packages": [ // 仅用于变量动态加载的场景，静态加载或常量动态加载无需配置。
41. "har1",
42. "har3"
43. ]
44. }
45. }
46. }

48. // HAR3's oh-package.json5
49. "dependencies": {
50. "har1": "file:../har1",
51. }
52. // HAR3's build-profile.json5
53. "buildOption": {
54. "arkOptions": {
55. "runtimeOnly": {
56. "packages": [ // 仅用于变量动态加载的场景，静态加载或常量动态加载无需配置。
57. "har1"
58. ]
59. }
60. }
61. }
```

**对应的报错信息如下：**

```
1. ohpm ERROR: Run install command failed
2. Error: 00618005 Invalid Dependency
3. Error Message: Invalid dependency har2@~\Coupled\har2 -> har2@1.0.0.

5. Try the following:
6. The name of an indirect dependency cannot be the same as the module name.
```

将HAR之间的**dependencies**和**runtimeOnly**配置转移到HAP中，解耦了包间循环依赖，程序能够正确运行。

```
1. // HAP's oh-package.json5
2. "dependencies": {
3. "har1": "file:../har1",
4. "har2": "file:../har2",
5. "har3": "file:../har3"
6. }
7. // HAP's build-profile.json5
8. "buildOption": {
9. "arkOptions": {
10. "runtimeOnly": {
11. "packages" : [ // 仅用于变量动态加载的场景，静态加载或常量动态加载无需配置。
12. "har1",
13. "har2",
14. "har3"
15. ]
16. }
17. }
18. }

20. // HAR1's oh-package.json5
21. "dependencies": {}
22. // HAR1's build-profile.json5
23. "buildOption": {}

25. // HAR2's oh-package.json5
26. "dependencies": {}
27. // HAR2's build-profile.json5
28. "buildOption": {}

30. // HAR3's oh-package.json5
31. "dependencies": {}
32. // HAR3's build-profile.json5
33. "buildOption": {}
```

**对应的运行日志如下：**

```
1. [DynamicImport] classHar1.add(), 0 + 1 = 1
2. [DynamicImport] hap -> har1, 0 + 1 = 1
3. [DynamicImport] classHar2.add(), 1 + 2 = 3
4. [DynamicImport] har1 -> har2, 1 + 2 = 3
5. [DynamicImport] classHar1.add(), 2 + 1 = 3
6. [DynamicImport] har2 -> har1, 2 + 1 = 3
7. [DynamicImport] classHar3.add(), 2 + 3 = 5
8. [DynamicImport] har2 -> har3, 2 + 3 = 5
9. [DynamicImport] classHar1.add(), 3 + 1 = 4
10. [DynamicImport] har3 -> har1, 3 + 1 = 4
```
