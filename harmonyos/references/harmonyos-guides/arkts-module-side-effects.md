---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-module-side-effects
title: 模块加载副作用及优化
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS运行时 > ArkTS模块化 > 模块加载副作用及优化
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:45+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8dd7d83d93d136e5fbe62befeb249228c88a5ed16f59d2360738fd8b7bfa5bad
---

## 概述

当使用[ArkTS模块化](module-principle.md)时，模块的加载和执行可能会引发**副作用**。副作用是指在模块导入时除了导出功能或对象之外，额外的行为或状态变化，**这些行为可能影响程序的其他部分，并导致产生非预期的顶层代码执行、全局状态变化、原型链修改、导入内容未定义等问题**。

## ArkTS模块化导致副作用的场景及优化方式

### 模块执行顶层代码

**副作用产生场景**

模块在被导入时，整个模块文件中的顶层代码会立即执行，而不仅仅是导出的部分。这意味着，即使只想使用模块中的某些导出内容，任何在顶层作用域中执行的代码也会运行，从而产生副作用。

```
1. // ModulePartOne.ets
2. console.info('Module loaded!'); // 这段代码在导入时会立即执行，可能会导致副作用。
3. export const data = 1;
```

```
1. // PageOne.ets
2. import { data } from './ModulePartOne'; // 导入时，ModulePartOne.ets中的console.info会执行，产生输出。
3. console.info('data is ', data);
```

输出内容：

```
1. Module loaded!
2. data is  1
```

**产生的副作用**

即使只需要data，console.info("Module loaded!") 仍会运行，导致开发者可能预期只输出data的值，但却额外输出了“Module loaded!”，**影响输出内容**。

**优化方式**

优化方式1：去除顶层代码，只导出需要的内容，避免不必要的代码执行。

```
1. // ModulePartTwo.ets
2. export const data = 1;
```

```
1. // PageTwo.ets
2. import { data } from './ModulePartTwo';
3. console.info('data is ', data);
```

输出内容：

```
1. data is  1
```

优化方式2：将可能引发副作用的代码放在函数或方法内部，只有在需要时再执行，而不是在模块加载时立即执行。

```
1. // ModulePartThree.ets
2. export function initialize() {
3. console.info('Module loaded!');
4. }
5. export const data = 1;
```

```
1. // PageThree.ets
2. import { data } from './ModulePartThree';
3. console.info('data is ', data);
```

输出内容：

```
1. data is  1
```

### 修改全局对象

**副作用产生场景**

顶层代码或导入的模块可能会直接**操作全局变量**，改变全局状态，引发副作用。

```
1. // ModulePartFour.ets
2. export let data1 = 'data from module';
3. globalThis.someGlobalVar = 100; // 改变了全局状态
```

```
1. // SideEffectModuleFour.ets
2. export let data2 = 'data from side effect module';
3. globalThis.someGlobalVar = 200; // 也改变了全局状态
```

```
1. // ModuleUseGlobalVarFour.ets
2. import { data1 } from './ModulePartFour'; // 此时可能预期全局变量someGlobalVar的值为100
3. export function useGlobalVar() {
4. console.info('data1 is ', data1);
5. console.info('globalThis.someGlobalVar is ', globalThis.someGlobalVar); // 此时由于PageFour.ets中加载了SideEffectModuleFour模块，someGlobalVar的值已经被改为200
6. }
```

```
1. // PageFour.ets（执行入口）
2. import { data1 } from './ModulePartFour'; // 将全局变量someGlobalVar的值改为100
3. import { data2 } from './SideEffectModuleFour'; // 又将全局变量someGlobalVar的值改为200
4. import { useGlobalVar } from './ModuleUseGlobalVarFour';

6. useGlobalVar();
7. function maybeNotCalledAtAll() {
8. console.info('data1 is ', data1);
9. console.info('data2 is ', data2);
10. }
```

输出内容：

```
1. data1 is  data from module
2. globalThis.someGlobalVar is  200
```

**产生的副作用**

模块加载时直接修改全局变量 globalThis.someGlobalVar 的值，**会影响其他依赖该变量的模块或代码**。

**优化方式**

将可能引发副作用的代码放在函数或方法内部，只有在需要时再执行，而不是在模块加载时立即执行。

```
1. // ModulePartFive.ets
2. export let data1 = 'data from module';
3. export function changeGlobalVar() {
4. globalThis.someGlobalVar = 100;
5. }
```

```
1. // SideEffectModuleFive.ets
2. export let data2 = 'data from side effect module';
3. export function changeGlobalVar() {
4. globalThis.someGlobalVar = 200;
5. }
```

```
1. // ModuleUseGlobalVarFive.ets
2. import { data1, changeGlobalVar } from './ModulePartFive';
3. export function useGlobalVar() {
4. console.info('data1 is ', data1);
5. changeGlobalVar(); // 在需要的时候执行代码，而不是模块加载时执行。
6. console.info('globalThis.someGlobalVar is ', globalThis.someGlobalVar);
7. }
```

```
1. // PageFive.ets（执行入口）
2. import { data1 } from './ModulePartFive';
3. import { data2 } from './SideEffectModuleFive';
4. import { useGlobalVar } from './ModuleUseGlobalVarFive';

6. useGlobalVar();
7. function maybeNotCalledAtAll() {
8. console.info('data1 is ', data1);
9. console.info('data2 is ', data2);
10. }
```

输出内容：

```
1. data1 is  data from module
2. globalThis.someGlobalVar is  100
```

### 修改应用级ArkUI组件的状态变量信息

**副作用产生场景**

顶层代码或导入的模块可能会直接**修改应用级ArkUI组件的状态变量信息**，改变全局状态，引发副作用。

```
1. // ModulePartSix.ets
2. export let data = 'data from module';
3. AppStorage.setOrCreate('SomeAppStorageVar', 200); // 修改应用全局的UI状态
```

```
1. // PageSix.ets
2. import { data } from './ModulePartSix'; // 将AppStorage中的SomeAppStorageVar改为200

4. @Entry
5. @Component
6. struct Index {
7. // 开发者可能预期该值为100，但是由于ModulePartSix模块导入，该值已经被修改为200，但开发者可能并不知道值已经被修改
8. @StorageLink('SomeAppStorageVar') message: number = 100;
9. build() {
10. Row() {
11. Column() {
12. Text('test' + this.message)
13. .fontSize(50)
14. }
15. .width('100%')
16. }
17. .height('100%')
18. }
19. }
20. function maybeNotCalledAtAll() {
21. console.info('data is ', data);
22. }
```

显示内容：

```
1. test200
```

**产生的副作用**

模块加载时直接修改AppStorage中SomeAppStorageVar的值，**会影响其他依赖该变量的模块或代码**。

ArkUI组件的状态变量信息可以通过一些应用级接口修改，详见[ArkUI状态管理接口文档](arkts-state-management-overview.md)。

**优化方式**

将可能引发副作用的代码放在函数或方法内部，只有在需要时再执行，而不是在模块加载时立即执行。

```
1. // ModulePartSeven.ets
2. export let data = 'data from module';
3. export function initialize() {
4. AppStorage.setOrCreate('SomeAppStorageVar', 200);
5. }
```

```
1. // PageSeven.ets
2. import { data } from './ModulePartSeven';

4. @Entry
5. @Component
6. struct Index {
7. @StorageLink('SomeAppStorageVar') message: number = 100;
8. build() {
9. Row() {
10. Column() {
11. Text('test' + this.message)
12. .fontSize(50)
13. }
14. .width('100%')
15. }
16. .height('100%')
17. }
18. }
19. function maybeNotCalledAtAll() {
20. console.info('data is ', data);
21. }
```

显示内容：

```
1. test100
```

### 修改内置全局变量或原型链（ArkTS内禁止修改对象原型与内置方法）

**副作用产生场景**

为使现代JavaScript特性能够在旧版浏览器或运行环境中运行，第三方库或框架可能会修改内置的全局对象或原型链，从而影响其他代码的执行。

```
1. // ModifyPrototype.ts
2. export let data = 'data from modifyPrototype';
3. Array.prototype.includes = function (value) {
4. return this.indexOf(value) !== -1;
5. };
```

```
1. // PageEight.ets
2. import { data } from './ModifyPrototype'; // 此时修改了Array的原型链
3. let arr = [1, 2, 3, 4];
4. console.info('arr.includes(1) = ' + arr.includes(1)); // 此时调用的是ModifyPrototype.ts中的Array.prototype.includes方法
5. function maybeNotCalledAtAll() {
6. console.info('data is ', data);
7. }
```

**产生的副作用**

修改内置的全局对象或原型链，可能会影响其他代码运行。

**优化方式**

导入可能会修改内置的全局对象或原型链的第三方库时，确认该第三方库的行为是符合预期的。

### 循环依赖

**副作用产生场景**

ArkTS模块化支持循环依赖，即模块A依赖模块B，同时模块B又依赖模块A。在这种情况下，某些导入的模块可能尚未完全加载，从而导致部分代码在执行时行为异常，产生意外的副作用。

```
1. // ExportA.ets
2. import { b } from './ExportB';
3. console.info('Module A: ', b);
4. export const a = 'A';
```

```
1. // ExportB.ets
2. import { a } from './ExportA';
3. console.info('Module B: ', a);
4. export const b = 'B';
```

输出内容：

```
1. Error message: a is not initialized
2. Stacktrace:
3. at func_main_0 (b.ets:2:27)
```

**产生的副作用**

由于模块间相互依赖，模块的执行顺序可能导致导出的内容未定义，影响代码的逻辑流，具体报错信息为：“变量名 is not initialized”。

**优化方式**

尽量避免模块间的循环依赖，确保模块的加载顺序是明确和可控的，以避免产生意外的副作用。[@security/no-cycle循环依赖检查工具](ide_no-cycle.md) 可以辅助检查循环依赖。

### 延迟加载（lazy import）改变模块执行顺序，可能导致预期的全局变量未定义

**副作用产生场景**

[延迟加载](arkts-lazy-import.md)特性可使待加载模块在冷启动阶段不被加载，直至应用程序实际运行过程中需要用到这些模块时，才按需同步加载相关模块，从而缩短应用冷启动耗时。但这也同时会改变模块的执行顺序。

```
1. // ModulePartNine.ets
2. export let data = 'data from module';
3. globalThis.someGlobalVar = 100;
```

```
1. // ModuleUseGlobalVarNine.ets
2. import lazy { data } from './ModulePartNine';
3. console.info('globalThis.someGlobalVar', globalThis.someGlobalVar); // 此时由于lazy特性，ModulePartNine模块还未执行，someGlobalVar的值为undefined
4. console.info('data is ', data); // 使用到ModulePartNine模块的变量，此时ModulePartNine模块执行，someGlobalVar的值变为100
```

输出内容：

```
1. globalThis.someGlobalVar undefined
2. data is  data from module
```

**产生的副作用**

由于使用到延迟加载（lazy import）特性，会导致模块变量在使用到时再执行对应的模块，模块中的一些全局变量修改行为也会延迟，可能会导致运行结果不符合预期。

**优化方式**

将可能引发副作用的代码放在函数或方法内部，只有在需要时再执行，而不是在模块加载时立即执行。

```
1. // ModulePartTen.ets
2. export let data = 'data from module';
3. export function initialize() {
4. globalThis.someGlobalVar = 100; // 延迟到函数调用时执行
5. }
```

```
1. // ModuleUseGlobalVarTen.ets
2. import lazy { data, initialize } from './ModulePartTen';
3. initialize(); // 执行初始化函数，初始化someGlobalVar
4. console.info('globalThis.someGlobalVar is ', globalThis.someGlobalVar); // 此时someGlobalVar一定为预期的值
5. console.info('data is ', data);
```

输出内容：

```
1. globalThis.someGlobalVar is  100
2. data is  data from module
```

## 通过import路径展开优化性能

### 原理

在import语句中，跳过中间的依赖路径，直接依赖变量对应的模块，即为import路径展开。

下文将通过示例说明import路径展开优化性能的原理。

```
1. // main.ets
2. import * as har from "har"
3. console.info("har.One is ", har.One); // 这里的One变量是har/src/main/ets/NumberString.ets导出的

5. // har/Index.ets
6. export * from "./src/main/ets/OtherModule1"
7. export * from "./src/main/ets/OtherModule2"
8. export * from "./src/main/ets/Utils"
9. console.info("har Index.ets execute.");

11. // har/src/main/ets/Utils.ets
12. export * from "./OtherModule3"
13. export * from "./OtherModule4"
14. export * from "./NumberString"
15. console.info("har Utils.ets execute.");
```

```
1. // har/src/main/ets/NumberString.ets
2. export const One: string = '1';
3. console.info('har NumberString.ets execute.');
```

1. 如果main.ets只需要依赖har中的NumberString模块，import xxx from "har"的写法会导致har整条链路上的模块被解析、执行，**导致模块解析及执行耗时增加**。上述例子中的har/Index、OtherModule1、OtherModule2、Utils、OtherModule3、OtherModule4、NumberString模块均会被解析、执行。
2. 在模块解析阶段会通过深度优先遍历的方式建立变量的绑定关系，main.ets中使用的har.One变量是由har/src/main/ets/NumberString.ets导出的，由于使用了export 的写法，建立变量的绑定关系时需要递归去进行变量名的匹配，从而\*导致模块解析耗时增加。

在上述例子中，会先查找 har/Index.ets 文件。该文件中有多个 export \* 语句，因此会依次检查 OtherModule1 和 OtherModule2 是否导出 One 变量。接着，找到 Utils 模块，该模块也有 export \* 语句，因此会继续检查 OtherModule3 和 OtherModule4，最终确定 One 变量是从 NumberString 模块导出的。

优化方式：改为如下的代码写法，跳过中间的依赖路径，直接依赖变量对应的模块。

```
1. // PageEleven.ets
2. import { One } from 'staticlibrary/src/main/ets/components/NumberString';
3. console.info('One is ', One);
```

```
1. // har/src/main/ets/NumberString.ets
2. export const One: string = '1';
3. console.info('har NumberString.ets execute.');
```

### 副作用

**副作用产生场景**

由于import路径展开会跳过中间模块的执行，若业务依赖模块的执行顺序，修改后可能会导致业务异常。

```
1. // PageTwelve.ets
2. import { serviceManager } from 'staticlibrary';

4. serviceManager.print();
```

```
1. import { serviceManager } from './src/main/ets/ServiceManagerPartOne';

3. serviceManager.init();
4. export { serviceManager }
```

```
1. // har/src/main/ets/ServiceManagerPartOne.ets
2. class ServiceManager {
3. public inited: boolean = false;

5. public init() {
6. this.inited = true;
7. }
8. public print() {
9. if (this.inited) {
10. console.info('ServiceManager is inited.');
11. } else {
12. console.error('ServiceManager is not inited.');
13. }
14. }
15. }
16. export let serviceManager: ServiceManager = new ServiceManager();
```

运行的输出为：

```
1. ServiceManager is inited.
```

如果进行import路径展开，展开后的代码为：

```
1. // PageThirteen.ets
2. import { serviceManager } from 'staticlibrary/src/main/ets/ServiceManagerPartTwo';

4. serviceManager.print();
```

```
1. // har/src/main/ets/ServiceManagerPartTwo.ets
2. class ServiceManager {
3. public inited: boolean = false;

5. public init() {
6. this.inited = true;
7. }
8. public print() {
9. if (this.inited) {
10. console.info('ServiceManager is inited.');
11. } else {
12. console.error('ServiceManager is not inited.');
13. }
14. }
15. }
16. export let serviceManager: ServiceManager = new ServiceManager();
```

运行的输出为：

```
1. ServiceManager is not inited.
```

**产生的副作用**

由于har/Index模块中存在顶层代码进行ServiceManager的初始化，如果在main模块中进行import路径展开，将不会执行har/Index模块，从而导致ServiceManager未初始化，可能引起业务异常。

**优化方式**

开发者需根据业务需要排查跳过执行顶层代码的影响，并进行相应的修改。

对于上文的示例，可以进行如下修改：

```
1. // PageFourteen.ets
2. import { serviceManager } from 'staticlibrary/src/main/ets/ServiceManagerPartThree';

4. serviceManager.print();
```

```
1. // har/src/main/ets/ServiceManagerPartThree.ets
2. class ServiceManager {
3. public inited: boolean = false;

5. public init() {
6. this.inited = true;
7. }
8. public print() {
9. if (this.inited) {
10. console.info('ServiceManager is inited.');
11. } else {
12. console.error('ServiceManager is not inited.');
13. }
14. }
15. }
16. export let serviceManager: ServiceManager = new ServiceManager();
17. // 在导出的模块执行对应的逻辑。
18. serviceManager.init();
```
