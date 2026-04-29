---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/bytecode-obfuscation-questions
title: ArkGuard字节码混淆常见问题
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS编译工具链 > ArkGuard字节码混淆工具 > ArkGuard字节码混淆常见问题
category: harmonyos-guides
scraped_at: 2026-04-29T13:26:58+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:caaf7623180bdae9a57505c0bf202c7c3861142609dae5e71f0c9cde357095dc
---

## 字节码混淆与源码混淆差异

### 混淆范围差异

**json文件**

字节码混淆在开启-enable-filename-obfuscation混淆项后，json文件名会参与混淆。

### 混淆选项差异

1. 字节码混淆开关，默认关闭，在[开启混淆功能](bytecode-obfuscation-guide.md#开启混淆步骤)后，需要额外在模块目录下obfuscation-rules.txt文件中配置-enable-bytecode-obfuscation 、-enable-bytecode-obfuscation-debugging。
2. 字节码混淆，不支持以下混淆项-remove-comments。

### 混淆后文件结构差异

**目录差异**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/4_YfvMHdQ1-rlJCjVl9fsw/zh-cn_image_0000002589243847.png?HW-CC-KV=V1&HW-CC-Date=20260429T052657Z&HW-CC-Expire=86400&HW-CC-Sign=A939743E9E6507D9C517F33798CB17CCA0064B2E510E58221C967F97DBF4D950) ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/IhRZJsOfQfy9nms6Zody8Q/zh-cn_image_0000002558764040.png?HW-CC-KV=V1&HW-CC-Date=20260429T052657Z&HW-CC-Expire=86400&HW-CC-Sign=7D4A61A072937481EF5EE1F863F3BB3392A2571F4D27D5B4F111167E1DBF085B)

字节码混淆后，obfuscation目录中多了obf、origin文件夹和config.json文件，具体详见[混淆效果](bytecode-obfuscation-guide.md#查看混淆效果)。

**文件内容差异**

nameCache.json文件：

源码混淆后：

```
1. {
2. "entry/src/main/ets/entryability/EntryAbility.ets": {
3. "IdentifierCache": {
4. "#UIAbility": "UIAbility",
5. "#testObject": "i",
6. "#EntryAbility": "j"
7. },
8. "MemberMethodCache": {
9. "onCreate:6:8": "onCreate",
10. "onDestroy:10:12": "onDestroy",
11. "onWindowStageCreate:14:25": "onWindowStageCreate",
12. "onWindowStageDestroy:27:30": "onWindowStageDestroy",
13. "onForeground:32:35": "onForeground",
14. "onBackground:37:40": "onBackground"
15. },
16. "obfName": "entry/src/main/ets/entryability/EntryAbility.ets"
17. },
18. "compileSdkVersion": "5.0.0.70",
19. "entryPackageInfo": "entry|1.0.0",
20. "PropertyCache": {},
21. "FileNameCache": {
22. "Hide": "b"
23. }
24. }
```

字节码混淆后：

```
1. {
2. "entry/src/main/ets/entryability/EntryAbility.ets": {
3. "IdentifierCache": {
4. "#EntryAbility": "a",
5. "#testObject": "c"
6. },
7. "MemberMethodCache": {
8. "EntryAbility:0:0": "a",
9. "onBackground:33:35": "onBackground",
10. "onCreate:7:9": "onCreate",
11. "onDestroy:10:12": "onDestroy",
12. "onForeground:29:31": "onForeground",
13. "onWindowStageCreate:14:23": "onWindowStageCreate",
14. "onWindowStageDestroy:25:27": "onWindowStageDestroy"
15. },
16. "obfName": "entry/src/main/ets/entryability/EntryAbility.ets",
17. "OriSourceFile": "entry|entry|1.0.0|src/main/ets/entryability/EntryAbility.ts",
18. "ObfSourceFile": "entry|entry|1.0.0|src/main/ets/entryability/EntryAbility.ts"
19. },
20. "entryPackageInfo": "entry|1.0.0",
21. "compileSdkVersion": "5.0.0.70",
22. "PropertyCache": {},
23. "FileNameCache": {
24. "Hide": "b"
25. }
26. }
```

1. IdentifierCache中，字节码混淆时差异：
   1. 不涉及函数参数名混淆。
   2. 无匿名函数混淆名称映射。
2. 在开启-enable-filename-obfuscation混淆项时，字节码混淆比源码混淆，多了OriSourceFile（混淆前源文件路径）和ObfSourceFile（混淆后源文件路径）字段。

### 切换注意点

**UI组件混淆差异**

字节码混淆不提供UI组件混淆能力。

由于字节码中UI组件存在大量字符串的形式绑定属性、方法、类、变量等，字节码混淆已通过系统白名单扫描的机制，保证功能正常。

**以字符串的形式作为函数参数绑定属性**

源码：

```
1. @Component
2. export struct MainPage {
3. @State messageStr: string = 'Hello World';

5. build() {
6. }
7. }
```

中间文件：

```
1. this.__messageStr = new ObservedPropertySimplePU('Hello World', this, "messageStr");
```

在中间文件转换过程中，message以字面量形式进行了绑定；此时，存在messageStr这个属性被混淆了，但是这个方法的字符串参数没有混淆，导致UI失效。

**解决办法**：收集struct里所有成员，加入白名单，不参与混淆。目前由于字节码混淆不提供UI组件混淆能力，系统会自动识别添加到白名单，不需要开发者配置。

**字节码中通过字符串绑定属性**

源码：

```
1. // Sample.ets
2. import { Type } from '@kit.ArkUI';

4. // 数据中心
5. @ObservedV2
6. class SampleChild {
7. @Trace public p123: number = 0;
8. public p2: number = 10;
9. }

11. @ObservedV2
12. export class Sample {
13. // 对于复杂对象需要@Type修饰，确保序列化成功
14. @Type(SampleChild)
15. @Trace public f123: SampleChild = new SampleChild();
16. }

18. @ObservedV2
19. class Info {
20. @Trace public sample: Sample = new Sample();
21. }
```

字节码文件：

```
1. tryldglobalbyname 0x136, Trace
2. sta v2
3. lda v0
4. ldobjbyname 0x137, prototype
5. sta v3
6. lda.str sample
7. sta v4
8. lda v2
9. callargs2 0x2c, v3, v4
10. lda v0
11. ldobjbyname 0x139, prototype
12. sta v2
13. lda.str sample
14. sta v3
15. lda v1
16. callargs2 0x2e, v2, v3
```

字节码层面存在一个global对象Trace，再通过字符串sample绑定属性。

**解决办法**：字节码混淆需要收集扫描到的所有decorator节点，并且识别到Trace修饰的参数就自动加入白名单，不需要开发者配置。

## 如何排查功能异常

**排查功能异常步骤**

1. 先在obfuscation-rules.txt配置-disable-obfuscation选项用于关闭混淆，确认问题是否由混淆引起。
2. 若确认是开启混淆后功能出现的异常，请先阅读文档了解[混淆规则](bytecode-obfuscation.md#混淆选项)的能力以及哪些语法场景需要[配置白名单](bytecode-obfuscation.md#已有保留选项汇总)来保证应用功能正常。
3. 参考本文已有的问题，若是相似场景可参考对应的解决方法快速解决。
4. 若常见案例中未找到相似案例，建议依据各项配置功能正向定位（若不需要相应功能，可删除对应配置项）。
5. 应用运行时崩溃分析方法：

   a.打开应用运行日志或者点击DevEco Studio中出现的Crash弹窗，找到运行时崩溃栈。

   b.应用运行时崩溃栈中的行号为编译产物的行号，方法名也可能为混淆后名称；因此排查时建议直接根据崩溃栈查看编译产物，进而分析哪些名称不能被混淆，然后将其配置进白名单中。
6. 应用在运行时未崩溃但出现功能异常的分析方法（比如白屏）：

   a.打开应用运行日志：选择HiLog，检索与功能异常直接相关的日志，定位问题发生的上下文。

   b.定位异常代码段：通过分析日志，找到导致功能异常的具体代码块。

   c.增强日志输出：在疑似异常的功能代码中，对处理的数据字段增加日志记录。

   d.分析并确定关键字段：通过对新增日志输出的分析，识别是否由于混淆导致该字段的数据异常。

   e.配置白名单保护关键字段：将确认在混淆后对应用功能产生直接影响的关键字段添加到白名单中。

## 常规配置问题处理

### 开启enable-bytecode-obfuscation-debugging，没有生成pa文件如何处理

首先确保Build Mode设置为release，查看根目录下的build-profile.json5中，设置 "compatibleSdkVersionStage": "beta3"，再检查每个module中obfuscation-rules.txt文件里，开启字节码。

### 混淆如何查看混淆效果

在混淆结束后会将中间产物落盘，因此可以在编译产物build目录中找到混淆后的中间产物以查看混淆效果，同时可以找到混淆生成的名称映射表及系统API白名单文件。

* 混淆后的文件目录：build/default/[...]/release/obfuscation/obf。
* 混淆名称映射表及系统API白名单目录：build/default/[...]/release/obfuscation。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/Uj1-ZKu8SBG28dCs_MBM6w/zh-cn_image_0000002558604382.png?HW-CC-KV=V1&HW-CC-Date=20260429T052657Z&HW-CC-Expire=86400&HW-CC-Sign=0AC109DF50A60051157D36B62678540CF3A1BF53AD5C77C960272898BBF31151)

* 名称映射表文件：nameCache.json，该文件记录了源码名称混淆的映射关系。
* 系统API白名单文件：systemApiCache.json，该文件记录了SDK中的接口与属性名称，与其重名的源码不会被混淆。

## 编译报错处理

**案例一：报错内容为 ERROR: [Class]get different name for method.**

**问题现象**：使用@CustomDialog，自定义对话框，内部再弹出另一个对话框，开启字节码混淆后，执行build失败，报错信息为：

Error message: ArkTSCompilerError: ArkTS:ERROR Failed to execute ByteCode Obfuscate.

Error message: [Class]get different name for method:&entry/src/main/ets/pages/XXXX&.#~@0>#setController^1.

```
1. // 代码1
2. @CustomDialog
3. export default struct TmsDialog {
4. controller?: CustomDialogController
5. dialogController:CustomDialogController

7. build() {
8. }
9. }

11. // 代码2
12. @CustomDialog
13. struct Index{
14. controller?: CustomDialogController
15. dialogController?:CustomDialogController

17. build() {
18. }
19. }
```

**问题原因**：

在这个示例中，在自定义的对话框中，再弹一个对话框；如上示例中代码1，或在一个UI中定义两个CustomDialogController对象，执行时，ets代码转ts后，会生成两个相同的setController函数，从而导致字节码混淆时报错。

**解决方案**：

```
1. @CustomDialog
2. export default struct TmsDialog {
3. controller?: CustomDialogController
4. dialogController:CustomDialogController|null = null;  // 修改此处的定义声明方式

6. build() {
7. }
8. }
```

示例代码1中，在运行时，是无法正常弹出dialogController的，只需要在定义时改为解决方案中的代码，就可以正常弹出dialogController，同时字节码混淆功能正常；

示例代码2中，由于我们只是使用CustomDialogController，因此不需要@CustomDialog，直接删除@CustomDialog即可，删除后功能正常，字节码混淆功能正常。

从API version 18开始，上述示例代码将不能正常编译。新的版本中，一个@CustomDialog组件只能有一个未初始化的CustomDialogController。

## 运行异常处理

### 开启-enable-property-obfuscation选项可能出现的问题

**案例一：报错内容为 Cannot read property 'xxx' of undefined**

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

13. let jsonProp = jsonData.jsonObj.jsonProperty;
```

```
1. // 混淆后
2. import jsonData from "./test.json";

4. let jsonProp = jsonData.i.j;
```

开启属性混淆后，"jsonProperty"被混淆成随机字符"j"，但json文件中为原始名称，从而导致值为undefined。

**解决方案**：使用-keep-property-name选项将json文件里的字段配置到白名单。

**案例二：使用了数据库相关的字段，开启属性混淆后，出现报错**

报错内容为table Account has no column named a23 in 'INSERT INTO Account(a23)'。

代码里使用了数据库字段，混淆时该SQL语句中字段名称被混淆，但数据库中字段为原始名称，从而导致报错。

**解决方案**：使用-keep-property-name选项将使用到的数据库字段配置到白名单。

**案例三：使用Record<string, Object>作为对象的类型时，该对象里的属性被混淆，导致功能异常**

**问题现象**：

parameters的类型为Record<string, Object>，在开启属性混淆后，parameters对象中的属性linkSource被混淆，进而导致功能异常。示例如下：

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

**问题原因**：

在这个示例中，所创建的对象的内容需要传递给系统来加载某个页面，因此对象中的属性名称不能被混淆，否则会造成功能异常。示例中parameters的类型为Record<string, Object>，这只是一个表示以字符串为键的对象的泛型定义，并没有详细描述其内部结构和属性类型。因此，混淆工具无法识别该对象内部哪些属性不应被混淆，从而可能导致内部属性名linkSource被混淆。

**解决方案**：

将混淆后会出现问题的属性名配置到属性白名单中，示例如下：

```
1. -keep-property-name
2. linkSource
```

**案例四：使用@Type和@Trace组合修饰的装饰器属性，混淆后，功能不正常**

**问题现象**：

使用@Type和@Trace组合修饰的装饰器属性，可以正常混淆，但混淆后，功能异常。

```
1. // Sample.ets
2. import { Type } from '@kit.ArkUI';

4. @ObservedV2
5. class SampleChild {
6. @Trace public p123: number = 0;
7. public p2: number = 10;
8. }

10. @ObservedV2
11. export class Sample {
12. // 对于复杂对象需要@Type修饰，确保序列化成功
13. @Type(SampleChild)
14. @Trace public f123: SampleChild = new SampleChild();
15. }
```

```
1. // Call the API
2. // CallDecorator.ets
3. import { PersistenceV2 } from '@kit.ArkUI';
4. import { Sample } from './SampleChild';

6. @Entry
7. @ComponentV2
8. export struct Page {
9. prop: Sample = PersistenceV2.connect(Sample, () => new Sample())!;

11. build() {
12. Column() {
13. Text(`Page1 add 1 to prop.p1: ${this.prop.f123.p123}`)
14. }
15. }
16. }
```

混淆后，p123，f123都被正常替换了，但处理Trace，Type装饰器属性时，p123，f123都被识别为字符串，不参与混淆，导致调用失败。

**问题原因**：

装饰器修饰的属性名需要保留，使用@Type和@Trace组合修饰的装饰器属性同样需要被保留。

**解决方案**：

使用-keep-property-name选项，将未直接导出的类型内的属性配置到属性白名单中。示例如下：

```
1. -keep-property-name
2. f123
3. p123
```

**案例五：同时开启-enable-property-obfuscation和-keep选项可能会出现的问题**

**问题现象**：

使用如下混淆配置：

```
1. -enable-property-obfuscation
2. -keep
3. ./file1.ts
```

并且在file2.ts中导入file1.ts的接口。此时，接口中有属性的类型为对象类型，该对象类型的属性在file1.ts中被保留，在file2.ts中被混淆，从而导致调用时引发功能异常。示例如下：

```
1. // 混淆前
2. // ExportInterface.ts
3. export interface MyInfo {
4. age: number;
5. address: {
6. city1: string;
7. }
8. }
```

```
1. // ExportCompositeInterface.ts
2. import { MyInfo } from './ExportCompositeInterface';
3. // ...
4. const person: MyInfo = {
5. age: 20,
6. address: {
7. city1: 'shanghai'
8. }
9. }
```

```
1. // 混淆后，file1.ts的代码被保留
2. // file2.ts
3. import { MyInfo } from './file1';

5. const person: MyInfo = {
6. age: 20,
7. address: {
8. i: "shanghai"
9. }
10. }
```

**问题原因**:

-keep选项保留file1.ts文件时，file1.ts中代码不会被混淆。对于导出属性（如address）所属类型内的属性，不会被自动收集在属性白名单中。因此，该类型内的属性在其他文件中被使用时，会被混淆。

**解决方案**:

**方案一**：使用interface定义该属性的类型，并使用export进行导出，这样该属性会自动被收集到属性白名单中。示例如下：

```
1. // ExportCompositeInterface.ts
2. export interface AddressType {
3. city1: string
4. }
5. export interface MyInfo {
6. age: number;
7. address: AddressType;
8. }
```

**方案二**：使用-keep-property-name选项，将未直接导出的类型内的属性配置到属性白名单中。示例如下：

```
1. -keep-property-name
2. city1
```

### 同时开启-enable-export-obfuscation和-enable-toplevel-obfuscation选项可能出现的问题

**当开启这两个选项时，主模块调用其他模块方法时涉及的方法名称混淆情况如下**：

| 主模块 | 依赖模块 | 导入与导出的名称混淆情况 |
| --- | --- | --- |
| HAP/HSP | HSP | HSP和主模块是独立编译的，混淆后名称会不一致，因此都需要配置白名单 |
| HAP/HSP | 本地HAR | 本地HAR与主模块一起编译，混淆后名称一致 |
| HAP/HSP | 三方库 | 三方库中导出的名称及其属性会被收集到白名单，因此导入和导出时都不会被混淆 |

HSP需要将给其他模块用的方法配置到白名单中。因为主模块里也需要配置相同的白名单，所以推荐将HSP配置了白名单的混淆文件（假设名称为hsp-white-list.txt）添加到依赖它的模块的混淆配置项里，即下图files字段里。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/meCEJzB_SpSV1pl0W2Dlkg/zh-cn_image_0000002558604384.png?HW-CC-KV=V1&HW-CC-Date=20260429T052657Z&HW-CC-Expire=86400&HW-CC-Sign=DBA1F567BDCED8BA71939D4EF98452EE2A35E3505461E05D27B09A9B2048551A)

**案例一：动态导入某个类，类定义的地方被混淆，导入类名时却没有混淆，导致报错**

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
3. try {
4. const mathUtils = await import('./ExportUtils');
5. const result = mathUtils.add(2, 3);
6. } catch (error) {
7. console.error('Failure reason:', error);
8. }
9. }

11. loadAndUseAdd();
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
11. const b1 = a1.add(2, 3);
12. }
13. catch (z) {
14. console.error('Failure reason:', z);
15. }
16. }
17. i();
```

函数add在定义时位于顶层作用域，但通过.add访问时被视为属性。由于未开启-enable-property-obfuscation选项，导致add被使用时未进行混淆。

**解决方案**：

方案一：开启-enable-property-obfuscation选项。

方案二：使用-keep-global-name选项将"add"配置到白名单。

**案例二：在使用namespace中的方法时，该方法定义的地方被混淆了，但使用的地方却没有被混淆，导致报错**

```
1. // 混淆前
2. // ExportNs.ts
3. export namespace NS {
4. export function foo() {
5. console.info(`export NS function foo is called`);
6. }
7. }
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

namespace中的foo属于export元素，当通过NS.foo调用时被视为属性。由于未开启-enable-property-obfuscation选项，导致foo在使用时未被混淆。

**解决方案**：

1. 开启-enable-property-obfuscation选项。
2. 将namespace里导出的方法使用-keep-global-name选项添加到白名单。

**案例三：使用了declare global，混淆后报语法错误**

```
1. // ExportInterface.ts
2. // 混淆前
3. declare global {
4. var myAge : string
5. }
```

```
1. // 混淆后
2. declare a2 {
3. var b2 : string
4. }
```

报错内容为SyntaxError: Unexpected token。

**解决方案**：

使用-keep-global-name选项将global配置到白名单中。

从API version 18 开始，global 已加入系统的白名单，不需要开发者再使用 -keep-global-name 配置

**案例四：使用Reflect.defineMetadata()，混淆后，提示找不到函数，导致程序异常**

**问题现象**：

在开启-enable-toplevel-obfuscation属性混淆后，字节码混淆时，混淆正常，运行时报错，错误日志：

```
1. Error message: is not callable
2. Stacktrace: Cannot get SourceMap info, dump raw stack: at anonymous (ads_service|@hw-ads/ohos-ads-model|1.0.1|src/main/ets/annotations/FieldType.ts:6:1。
```

```
1. // oh-package.json5
2. "dependencies": {
3. "reflect-metadata": "0.2.1"
4. }

6. // test.ts
7. import 'reflect-metadata';

9. // 调用代码
10. export const FIELD_TYPE_KEY = Symbol('fieldType');
11. export function FieldType(...types: Function[]): PropertyDecorator {
12. return (target, key) => {
13. Reflect.defineMetadata(FIELD_TYPE_KEY, types, target, key);
14. };
15. }
```

**问题分析**：

在开启-enable-toplevel-obfuscation属性混淆后，Reflect文件中，函数名参与混淆，exporter函数中的字符串"defineMetadata"不参与混淆，导致外部使用Reflect.defineMetadata时，找不到对应函数。

**解决方案**：

使用-keep-global-name选项将defineMetadata配置到白名单中。由于Reflect文件中多次使用exporter，建议直接使用-keep选项。

```
1. -keep
2. ../xxx/xxx/xxx/Reflect.ts  // 使用文件的相对路径
```

### 未开启-enable-string-property-obfuscation混淆选项，字符串字面量属性名却被混淆，导致字符串字面量属性名的值为undefined

```
1. // ExportInterface.ts
2. // 混淆前
3. const person = {
4. myAge: 18
5. }
6. person["myAge"] = 20;
```

```
1. // file.ts
2. // 混淆后
3. const person = {
4. myAge: 18
5. }
6. person["m"] = 20;
```

**解决方案**：

1. 确认是否有依赖的HAR包开启了字符串属性名混淆，若开启了，则会影响主工程，需将其关闭。
2. 若不能关闭-enable-string-property-obfuscation选项，将属性名配置到白名单中。
3. 若依赖HAR包未开启字符串属性名混淆，同时SDK版本小于4.1.5.3，请更新SDK。

### 开启-enable-filename-obfuscation选项后，可能会出现的问题

**案例一：报错为Error Failed to get a resolved OhmUrl for 'D:code/MyApplication/f12/library1/pages/d.ets' imported by 'undefined'**

工程的目录结构如下图所示，模块library1的外层还有目录"directory"，开启文件名混淆后，"directory" 被混淆为f12，导致路径找不到。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/i6jqIoMdTrS_H-c_rx_KRQ/zh-cn_image_0000002589323909.png?HW-CC-KV=V1&HW-CC-Date=20260429T052657Z&HW-CC-Expire=86400&HW-CC-Sign=063CE4EB14379EC4283C6F3E665B142E87B4234CB869E59991A9447E396507D3)

**解决方案**：

1. 如果工程的目录结构和报错内容都相似，请将SDK更新至最低5.0.0.26版本。
2. 使用-keep-file-name将模块外层的目录名"directory"配置到白名单中。

**案例二：报错为Cannot find module 'ets/appability/AppAbility' which is application Entry Point**

由于系统会在应用运行时加载ability文件，用户需要手动配置相应的白名单，防止指定文件被混淆，导致运行失败。

**解决方案**：使用-keep-file-name选项，将src/main/module.json5文件中，'srcEntry'字段所对应的路径配置到白名单中。

```
1. -keep-file-name
2. appability
3. AppAbility
```

**HAP与HSP依赖相同的本地源码HAR模块，可能会出现的问题。**

* 若开启文件名混淆，会出现以下问题：

  **问题一**：单例功能异常问题。原因是HAP与HSP独立执行构建与混淆流程，本地源码HAR模块在HAP与HSP的包中可能会出现相同的文件名被混淆成不同文件名的情况。

  **问题二**：接口调用失败问题。原因是HAP与HSP独立执行构建与混淆流程，本地源码HAR模块在HAP与HSP的包中可能会出现不同的文件名被混淆成相同的文件名的情况。
* 若开启-enable-export-obfuscation和-enable-toplevel-obfuscation选项，在应用运行时会出现加载接口失败的问题。

  原因是HAP与HSP独立执行构建与混淆流程，本地源码HAR模块中暴露的接口在HAP与HSP中被混淆成不同的名称。

**解决方案**：

1. 将HAP与HSP共同依赖的本地源码HAR改造为字节码HAR，这样此HAR在被依赖时不会被二次混淆。
2. 将HAP与HSP共同依赖的本地源码HAR以release模式构建打包，这样此HAR在被依赖时，其文件名与对外接口不会被混淆。
