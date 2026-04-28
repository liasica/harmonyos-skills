---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/source-obfuscation-questions
title: ArkGuard混淆常见问题
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS编译工具链 > ArkGuard源码混淆工具 > ArkGuard混淆常见问题
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:834032a724f08f37f6c1250f83b81a0fa600b764c35b38f1237b254a4d23b370
---

## 如何排查功能异常

### 排查功能异常步骤

1. 在obfuscation-rules.txt中配置-disable-obfuscation选项关闭混淆，确认问题是否由混淆引起。
2. 若确认开启混淆后功能出现异常，请先阅读文档，了解模块已配置的混淆规则的能力和需要配置白名单的语法场景，以确保应用功能正常。下文简要介绍默认开启的四项选项功能，详情请参阅对应选项的完整描述。
   1. [-enable-toplevel-obfuscation](source-obfuscation.md#section-enable-toplevel-obfuscation)为顶层作用域名称混淆开关。
   2. [-enable-property-obfuscation](source-obfuscation.md#section-enable-property-obfuscation)为属性混淆开关。配置白名单的主要场景包括网络数据访问、json字段访问、动态属性访问、调用so库接口等。需要使用[-keep-property-name](source-obfuscation.md#section-keep-property-name)来保留指定的属性名称。
   3. [-enable-export-obfuscation](source-obfuscation.md#section-enable-export-obfuscation)为导入/导出名称混淆。一般与-enable-toplevel-obfuscation和-enable-property-obfuscation选项配合使用。配置白名单的主要场景为模块对外接口不能混淆。需要使用[-keep-global-name](source-obfuscation.md#section-keep-global-name)来保留指定的导出/导入名称。
   4. [-enable-filename-obfuscation](source-obfuscation.md#section-enable-filename-obfuscation)为文件名混淆。配置白名单的主要场景为动态import或运行时直接加载的文件路径。需要使用[-keep-file-name](source-obfuscation.md#section-keep-file-name)来保留这些文件路径及名称。
3. 排查需要配置的白名单场景时，推荐使用[混淆助手配置保留选项](ide-build-obfuscation.md#section19439175917123)，可以快速识别需要配置的保留选项和白名单字段。也可以参考以下典型报错案例，若遇到相似场景，可参照对应解决方法快速处理。
4. 若以下报错案例中未找到相似场景，建议依据各项配置功能正向定位（若不需要相应功能，可删除对应配置项）。
5. 应用运行时崩溃分析方法：
   1. 打开应用运行日志，或点击DevEco Studio中出现的Crash弹窗，找到运行时崩溃栈。
   2. 应用运行时异常栈中的行号为[编译产物](source-obfuscation-guide.md#查看混淆效果)的行号，方法名也可能为混淆后名称；因此排查时建议直接根据异常栈查看编译产物，进而分析哪些名称不能被混淆，然后将其配置到白名单中。
6. 应用在运行时未崩溃但出现功能异常（如白屏）的分析方法：
   1. 打开应用运行日志：选择HiLog，检索与功能异常直接相关的日志，定位问题发生的上下文。
   2. 定位异常代码段：分析日志，找到引发功能异常的代码块。
   3. 增强日志输出：在疑似异常的功能代码中，增加日志打印以检查数据是否正常。
   4. 分析并确定关键字段：通过分析新增的日志输出，判断数据异常是否由混淆导致。
   5. 配置白名单以保护关键字段：将混淆后对应用功能有直接影响的关键字段添加到白名单中。

### 排查非预期的混淆能力

若出现预期外的混淆效果，检查是否由于依赖的本地模块或三方库开启了某些混淆选项。

示例：

假设当前模块未配置-compact，但混淆的中间产物中代码都被压缩成一行，可按照以下步骤排查混淆选项：

1. 查看当前模块的oh-package.json5中的dependencies，此字段记录了当前模块的依赖信息。
2. 在依赖的模块/三方库中的混淆配置文件内检索"-compact"：
   * 在本地依赖的library中的consumer-rules.txt文件中检索"-compact"。
   * 在工程目录下的oh\_modules文件夹中，对全部的obfuscation.txt文件检索"-compact"。

从API version 18开始，主模块默认不合并三方库的obfuscation.txt文件中的混淆选项，保留选项仍然有效。

说明

三方库中的consumer-rules.txt不建议配置以下开关选项。这些选项在主模块开启混淆时会生效，可能导致意外的混淆效果，甚至应用运行时崩溃。如果发现三方库的obfuscation.txt文件中包含以下开关选项，建议联系发布该三方库的团队删除这些选项并重新打包发布。

-enable-property-obfuscation

-enable-string-property-obfuscation

-enable-toplevel-obfuscation

-remove-log

-compact

## 典型报错案例及解决方案

### 报错信息为：Error message: Cannot read property xxx of undefined

**问题现象**

混淆规则配置如下所示：

```
1. -enable-property-obfuscation
```

示例代码如下：

```
1. // 示例JSON文件结构（ImportJson.json）：
2. /*
3. {
4. "jsonObj": {
5. "jsonProperty": "value"
6. }
7. }
8. */

10. // 混淆前
11. import jsonData from './ImportJson.json';
12. // ...
13. let jsonProp = jsonData.jsonObj.jsonProperty;
```

```
1. // 混淆后
2. import jsonData from "./test.json";

4. let jsonProp = jsonData.i.j;
```

**问题原因**

开启属性混淆后，源码会被混淆，但JSON文件不会。源码中通过jsonData.i访问属性时，由于属性名称已经被混淆，JSON数据中并不存在对应的字段，导致获取的值为undefined。

**解决方案**

将JSON文件中的字段配置到属性白名单中。示例如下：

```
1. -keep-property-name
2. jsonObj
3. jsonProperty
```

### 报错信息为：Error message: is not callable

**场景一：导出namespace中的方法时，该方法定义处被混淆，调用时未被混淆**

**问题现象**

混淆规则配置如下所示：

```
1. -enable-toplevel-obfuscation
2. -enable-export-obfuscation
```

示例代码如下：

```
1. // 混淆前
2. // ExportNs.ts
3. export namespace NS {
4. export function foo() { }
5. }
```

```
1. // import.ts
2. import { NS } from './ExportNs';
3. // ...
4. NS.foo();
```

```
1. // 混淆后
2. // export.ts
3. export namespace i {
4. export function j() {}
5. }

7. // import.ts
8. import { i } from './export';

10. i.foo();
```

**问题原因**

namespace中的foo属于export元素，当通过NS.foo调用时被视为属性。由于未开启-enable-property-obfuscation选项，导致foo在使用时未被混淆。

**解决方案**

方案一：开启-enable-property-obfuscation选项。

方案二：使用-keep-global-name选项将namespace中导出的方法配置到白名单中。示例如下：

```
1. -keep-global-name
2. foo
```

**场景二：动态导入某个类，类定义处被混淆，调用时未被混淆**

**问题现象**

混淆规则配置如下所示：

```
1. -enable-toplevel-obfuscation
2. -enable-export-obfuscation
```

示例代码如下：

```
1. // 混淆前
2. // ExportUtils.ts
3. export function add(a: number, b: number): number {
4. return a + b;
5. }
```

```
1. // main.ts
2. async function loadAndUseAdd() {
3. let result: number = 0;
4. try {
5. const mathUtils = await import('./ExportUtils');
6. result = mathUtils.add(2, 3);
7. console.info(`result = ${result}`);
8. } catch (error) {
9. console.error('Failure reason:', error);
10. }
11. }

13. loadAndUseAdd();
```

```
1. // 混淆后
2. // utils.ts
3. export function c1(d1: number, e1: number): number {
4. return d1 + e1;
5. }

7. // main.ts
8. async function i() {
9. try {
10. const a1 = await import("@normalized:N&&&entry/src/main/ets/pages/utils&");
11. const b1 = a1.addNum(2, 3);
12. }
13. catch (z) {
14. console.error('Failure reason:', z);
15. }
16. }
17. i();
```

**问题原因**

函数addNum在定义时位于顶层作用域，但通过.addNum访问时被视为属性。由于未开启-enable-property-obfuscation选项，导致addNum被使用时未进行混淆。

**解决方案**

方案一：开启-enable-property-obfuscation选项。

方案二：使用-keep-global-name选项将add配置到白名单中。示例如下：

```
1. -keep-global-name
2. addNum
```

**场景三：调用so库的方法后导致crash**

**问题现象**

混淆规则配置如下所示：

```
1. -enable-property-obfuscation
2. -enable-export-obfuscation
```

示例代码如下：

```
1. // src/main/cpp/types/libentry/Index.d.ts
2. export const addNum: (a: number, b: number) => number;
```

```
1. // example.ets
2. // 混淆前
3. import testNapi from 'libentry.so';
4. // ...
5. let sun = testNapi.addNum(1, 2);
```

```
1. // example.ets
2. // 混淆后
3. import testNapi from "@normalized:Y&&&libentry.so&";

5. testNapi.m();
```

**问题原因**

混淆工具仅支持js/ts/ets代码的混淆。so库中的方法定义在C++侧，因此这些方法在定义处不会被混淆，但在调用处会被混淆。

**解决方案**

将so库导出的方法配置到属性白名单中。示例如下：

```
1. -keep-property-name
2. addNum
```

### 报错信息为：'module1/file1' does not provide an export name 'x', which is imported by 'module2/file2'

**问题现象**

主模块和HSP模块的混淆规则配置如下所示：

```
1. -enable-toplevel-obfuscation
2. -enable-export-obfuscation
```

示例代码如下：

```
1. export function addNum(a: number, b: number) {
2. return a + b;
3. }
```

```
1. // 混淆前。
2. // hsp模块。
3. export { addNum } from '../utils/Calc';
```

```
1. // entry模块
2. import { addNum } from 'sharedlibrary';

4. addNum(1, 2);
```

```
1. // 混淆后
2. // hsp模块
3. export function b() {}

5. // entry模块
6. import { n } from '@normalized:N&myhsp&&myhsp/Index&';

8. n();
```

**问题原因**

当同时开启-enable-toplevel-obfuscation和-enable-export-obfuscation选项时，主模块与被调用模块的混淆情况如下：

| 主模块 | 依赖模块 | 导入与导出的名称混淆情况 |
| --- | --- | --- |
| HAP/HSP | HSP | HSP和主模块是独立编译的，混淆后名称会不一致，因此都需要配置白名单。 |
| HAP/HSP | 本地HAR | 本地HAR与主模块一起编译，混淆后名称一致。 |
| HAP/HSP | 三方库 | 三方库中导出的名称及其属性会被收集到白名单，因此导入和导出时都不会被混淆。 |

由于HAP和HSP模块是独立编译，因此混淆后导入和导出名称不一致，从而导致HAP引用HSP的方法时报错。

**解决方案**

将HSP模块导出的方法配置到-keep-global-name下，并且需要在HSP的consumer-rules.txt和obfuscation-rules.txt文件中都进行对应配置。示例如下：

```
1. // consumer-rules.txt
2. -keep-global-name
3. addNum

5. // obfuscation-rules.txt
6. -keep-global-name
7. addNum
```

## 应用运行后无crash信息，但功能异常的情况

### 使用Record<string, Object>作为对象的类型定义时，属性被混淆

**问题现象**

parameters的类型为Record<string, Object>。开启属性混淆后，parameters对象中的linkSource属性被混淆，导致功能异常。

示例代码如下：

```
1. // 混淆前
2. import { Want } from '@kit.AbilityKit';
3. // ...
4. let petalMapWant: Want = {
5. bundleName: 'com.example.myapplication',
6. uri: 'maps://',
7. parameters: {
8. linkSource: 'com.other.app'
9. }
10. }
```

```
1. // 混淆后
2. import type Want from "@ohos:app.ability.Want";

4. let petalMapWant: Want = {
5. bundleName: 'com.example.myapplication',
6. uri: 'maps://',
7. parameters: {
8. i: 'com.other.app'
9. }
10. };
```

**问题原因**

示例中parameters的类型为Record<string, Object>，这仅表示以字符串为键的对象的泛型定义，未详细描述其内部属性。因此，混淆工具无法识别对象内部哪些属性不应被混淆，导致linkSource被混淆后，引发功能异常。

**解决方案**

将混淆后会出现问题的属性名配置到属性白名单中，示例如下：

```
1. -keep-property-name
2. linkSource
```

### 跨文件调用某属性，该属性在一个文件中保留，在另一个文件中被混淆

**问题现象**

混淆规则配置如下所示：

```
1. -enable-property-obfuscation
2. -keep
3. ./file1.ts
```

在file2.ts中导入file1.ts的接口。该接口包含一个对象类型的属性。此对象属性在file1.ts中被保留，但在file2.ts中被混淆，导致调用时出现功能异常。

示例代码如下：

```
1. // 混淆前
2. // FileInside.ts
3. export interface MyInfo {
4. age: number;
5. address: {
6. city1: string;
7. }
8. }
```

```
1. // FileOutside.ts
2. import { MyInfo } from './FileInside';
3. // ...
4. const person: MyInfo = {
5. age: 20,
6. address: {
7. city1: 'shanghai'
8. }
9. }
```

```
1. // 混淆后
2. // file1.ts
3. export interface MyInfo {
4. age: number;
5. address: {
6. city1: string;
7. }
8. }

10. // file2.ts
11. import { MyInfo } from './file1';

13. const person: MyInfo = {
14. age: 20,
15. address: {
16. i: "shanghai"
17. }
18. }
```

**问题原因**

使用-keep选项保留file1.ts文件时，该文件中的代码不会被混淆。导出属性（如address）所属类型内的属性不会自动加入白名单，因此在其他文件中使用时会被混淆。

**解决方案**

方案一：使用interface定义该属性的类型，并使用export进行导出，这样该属性将被自动加入到属性白名单中。示例如下：

```
1. // FileOutside.ts
2. export interface AddressType {
3. city1: string
4. }
5. export interface MyInfo2 {
6. age: number;
7. address: AddressType;
8. }
```

方案二：使用-keep-property-name选项，将未直接导出的类型内的属性配置到属性白名单中。示例如下：

```
1. -keep-property-name
2. city1
```

### 未开启-enable-string-property-obfuscation，字符串字面量属性名却被混淆

**问题现象**

```
1. // 混淆前
2. const person = {
3. myAge: 18
4. }
5. person["myAge"] = 20;
```

```
1. // 混淆后
2. const person = {
3. myAge: 18
4. }
5. person["m"] = 20;
```

**问题原因**

主模块所依赖的其他模块中的consumer-rules.txt文件配置了-enable-string-property-obfuscation选项，主模块会合并该选项，导致字符串字面量属性名被混淆。

**解决方案**

从API version 18开始，主模块默认不会被三方库的混淆规则所影响，因此不会有这种情况。但如果API version低于18，可参考以下两种解决方案。

方案一：确认依赖的远程HAR包的obfuscation.txt文件中是否配置了-enable-string-property-obfuscation选项。若配置了则会影响主模块，需将其关闭。参考[排查非预期的混淆能力](source-obfuscation-questions.md#排查非预期的混淆能力)。

方案二：若工程复杂无法找到配置了该混淆选项的远程HAR包，可以将属性名直接配置到白名单中。

### 数据库相关的字段被混淆后导致功能异常

**问题现象**

HiLog日志中报错信息为：table Account has no column named a23 in 'INSERT INTO Account(a23)'。

**问题原因**

混淆时代码中的SQL语句字段名称被混淆，但数据库中字段为原始名称，从而导致报错。

**解决方案**

使用-keep-property-name选项将使用到的数据库字段配置到白名单。
