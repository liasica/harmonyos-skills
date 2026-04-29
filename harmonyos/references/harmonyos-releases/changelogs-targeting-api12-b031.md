---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-targeting-api12-b031
title: 针对API 12应用的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > 接口行为变更说明 > HarmonyOS NEXT Developer Beta2引入的接口行为变更 > 针对API 12应用的变更
category: harmonyos-releases
scraped_at: 2026-04-29T13:24:11+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:e32ea7cb42a7baa9a6f6e5fdaae02fdff42f50416ee2eb01b544d9c1d09aa1b2
---

## Ability Kit

### restartApp接口变更

**变更原因**

避免恶意应用在非获焦状态下重启自身，实现霸屏。

**变更影响**

此变更涉及应用适配。开发者需要在应用处于获焦状态时使用该接口，否则会影响功能。

**该能力起始支持的API Level**

12

**适配指导**

开发者需要在应用处于获焦状态时调用restartApp接口。

**示例：**

```
1. import { UIAbility, Want } from '@kit.AbilityKit';

3. export default class MyAbility extends UIAbility {
4. onForeground() {
5. let applicationContext = this.context.getApplicationContext();
6. let want: Want = {
7. bundleName: 'com.example.myapp',
8. abilityName: 'EntryAbility'
9. };
10. try {
11. applicationContext.restartApp(want);
12. } catch (error) {
13. console.error(`restartApp fail, error: ${JSON.stringify(error)}`);
14. }
15. }
16. }
```

## ArkData

### ValueType增加类型

**变更原因**

由于接口能力增强，ValueType需要增加类型。

**变更影响**

此变更涉及应用适配，ValueType增加类型，会导致getValue的返回值类型增加。当高低版本设备互通时，当高版本设备设置的数据类型为本次新增的类型时，由于低版本设备不支持新增的类型，会导致低版本设备上getValue失败。

**该能力起始支持的API Level**

12

**变更的接口/组件**

变更之前，ValueType类型如下：

```
1. type ValueType = number | string | image.PixelMap | Want | ArrayBuffer
```

变更之后，ValueType类型如下：

```
1. type ValueType = number | string  | boolean | image.PixelMap | Want | ArrayBuffer | object | null | undefined
```

**适配指导**

getValue接口的使用可参考[getValue示例代码](../harmonyos-references-V5/js-apis-data-unifieddatachannel-V5.md#getvalue12)。

## ArkTS

### Sendable容器TypedArray提供的map方法的回调函数声明变更

**变更原因**

Sendable容器TypedArray提供map方法。该方法对TypedArray中的每个元素进行某种操作或转换（通过callbackFn的返回值），并返回一个新的TypedArray，其中包含经过映射函数处理后的结果。

以Uint8Array为例，变更前，map函数的callbackFn声明无返回值，导致转换后的数据丢失，引起开发者使用上的困惑。

* map方法的回调函数声明为map(callbackFn: TypedArrayForEachCallback<number, Uint8Array>): Uint8Array;
* 而TypedArrayForEachCallback 的定义为无返回值的：type TypedArrayForEachCallback<ElementType, ArrayType> = (value: ElementType, index: number, array: ArrayType) => void;

**变更影响**

此变更涉及应用适配。

**变更前**

* 情况一： map函数中的callbackFn无返回值，能通过编译，但是无法实现map功能
* 情况二： map函数中的callbackFn有返回值，但是返回类型不是number，能通过编译，能实现map功能
* 情况三： map函数中的callbackFn有返回值，且返回类型是number，能通过编译，能实现map功能

```
1. let arr = [1, 2, 3, 4, 5];

3. // 创建一个Uint8Array
4. let uint8: collections.Uint8Array = new collections.Uint8Array(arr);

6. // 情况一：不能完成map功能：callbackFn无返回值，map函数返回新的collections.Uint8Array
7. let zeroMappedArray: collections.Uint8Array = uint8.map((value: number) => {}); // 能通过编译
8. console.info('' + zeroMappedArray); // 输出: collections.Uint8Array [0, 0, 0, 0, 0]

10. // 情况二：能完成map功能：callbackFn返回map后的元素值，但类型为string，map函数返回新的collections.Uint8Array
11. let wrongTypeMapped: collections.Uint8Array = uint8.map((value: number) => value + "1"); // 能通过编译
12. console.info('' + wrongTypeMapped); // 输出: collections.Uint8Array [11, 21, 31, 41, 51]

14. // 情况三：能完成map功能：callbackFn返回map后的元素值，map函数返回新的collections.Uint8Array
15. let normalMapped: collections.Uint8Array = uint8.map((value: number) => value * 2); // 能通过编译
16. console.info('' + normalMapped); // 输出: collections.Uint8Array [2, 4, 6, 8, 10]
```

**变更后**

* 情况一： map函数中的callbackFn无返回值，不能通过编译
* 情况二： map函数中的callbackFn有返回值，但是返回类型不是number，不能通过编译
* 情况三： map函数中的callbackFn有返回值，且返回类型是number，能通过编译，能实现map功能

```
1. let arr = [1, 2, 3, 4, 5];

3. // 创建一个Uint8Array
4. let uint8: collections.Uint8Array = new collections.Uint8Array(arr);

6. // 情况一：不能完成map功能：callbackFn无返回值，map函数返回新的collections.Uint8Array
7. let zeroMappedArray: collections.Uint8Array = uint8.map((value: number) => {}); // 不能通过编译

9. // 情况二：能完成map功能：callbackFn返回map后的元素值，但类型为string，map函数返回新的collections.Uint8Array
10. let wrongTypeMapped: collections.Uint8Array = uint8.map((value: number) => value + "1"); // 不能通过编译

12. // 情况三：能完成map功能：callbackFn返回map后的元素值，map函数返回新的collections.Uint8Array
13. let normalMapped: collections.Uint8Array = uint8.map((value: number) => value * 2); // 能通过编译
14. console.info('' + normalMapped); // 输出: collections.Uint8Array [2, 4, 6, 8, 10]
```

**该能力起始支持的API Level**

API12

**变更的接口/组件**

/interface/sdk-js/arkts/@arkts.collections.d.ets中TypedArray（包括Int8Array/Uint8Array/Int16Array/Uint16Array/Int32Array/Uint32Array）的map接口

**适配指导**

* 举例：上述场景二的例子，可以做如下修改：

  ```
  1. let wrongTypeMapped: collections.Uint8Array = uint8.map((value: number) => parseInt(value + "1")); // 通过parseInt进行字符串到number的转换
  ```
* 详细说明参见：接口使用的示例代码:

  [ArkTS容器集 - TypedArray](../harmonyos-references-V5/js-apis-arkts-collections-V5.md#collectionstypedarray)

### Sendable语法规则编译检查完善

**变更原因**

Sendable对象需要遵循一定[使用规则](../harmonyos-guides/sendable-constraints.md)，在Sendable泛型类的部分语法中，编译器没有对应的检查，导致这些语法下的Sendable对象用在并发场景中运行异常但是没有无编译时错误。在本次版本更新中，我们修复了这些场景下Sendable约束的编译时检查，将运行时异常提前到编译时。旨在通过编译时错误，帮助开发者更早发现Sendable使用约束，减少运行时定位成本。

**变更影响**

此变更涉及应用适配。

变更前：当Sendable泛型类用作类型标注时，类型形参可以使用Non-sendable类型，DevEco编辑界面没有错误提示，编译没有报错。

变更后：当Sendable泛型类用作类型标注时，类型形参不可以使用Non-sendable类型，DevEco编辑界面有错误提示，编译有报错。

对于使用Sendable泛型类进行声明，但是被赋值为Non-sendable对象的变量/参数/返回值，如果它们被用在并发实例共享的场景中，变更前会有运行时异常，变更后错误提前至编译期。如果它们被当作普通对象使用时，变更前运行时不报错，变更后编译器新增报错。

具体场景示例：

Sendable泛型类约束

场景一：当Sendable对象被用在多线程共享时，影响：运行时异常提前到编译时

变更前

```
1. // declaration.ets
2. export class NonSendableClass {};

4. // main.ets
5. import { NonSendableClass } from './declaration';
6. import collections from '@arkts.collections';

8. @Sendable
9. class SendableClass {
10. private arr: collections.Array<NonSendableClass> = new collections.Array();
11. constructor() {
12. this.arr.push(new NonSendableClass()); // Runtime ERROR
13. }
14. }
15. let sendableclassObject: SendableClass = new SendableClass();
```

变更后

```
1. // declaration.ets
2. export class NonSendableClass {};

4. // main.ets
5. import { NonSendableClass } from './declaration';
6. import collections from '@arkts.collections';

8. @Sendable
9. class SendableClass {
10. private arr: collections.Array<NonSendableClass> = new collections.Array(); // ArkTS compile-time error
11. constructor() {
12. this.arr.push(new NonSendableClass());
13. }
14. }
15. let sendableclassObject: SendableClass = new SendableClass();
```

场景二：Sendable对象被当作普通对象使用时，影响：产生新增编译报错

变更前

```
1. @Sendable
2. class SendableClassA<T> {
3. one: string = '1';
4. }
5. class NoneSendableClassA<T> {
6. one: string = '1';
7. }
8. let sendableObjectA: SendableClassA<NoneSendableClassA<number>> = new SendableClassA();
```

变更后

```
1. @Sendable
2. class SendableClassA<T> {
3. one: string = '1';
4. }
5. class NoneSendableClassA<T> {
6. one: string = '1';
7. }
8. let sendableObjectA: SendableClassA<NoneSendableClassA<number>> = new SendableClassA(); // ArkTS compile-time error
```

**该能力起始支持的API Level**

ArkTS Sendable语法检查从API 12起启用。

**变更的接口/组件**

不涉及。

**适配指导**

Sendable泛型类的类型必须使用Sendable类型。

### Sendable赋值语法规则编译检查完善

**访问级别**

其他

**变更原因**

Sendable赋值时需要遵循一定[使用规则](../harmonyos-guides/sendable-constraints.md)，但是在Non-sendable对象赋值给Sendable类型的部分场景中，编译没有对应的检查，导致这些场景下的Non-sendable对象被当成Sendable对象使用，运行异常但是没有编译时报错。在本次版本更新中，我们修复了这些场景下Sendable赋值约束的编译时检查，将运行时异常提前到编译时。旨在通过编译时错误，帮助开发者更早发现Sendable使用约束，减少运行时定位成本。

错误对象：使用Sendable类型/接口进行声明，但是被赋值为Non-sendable对象的变量/参数/返回值。

**变更影响**

此变更涉及应用适配。

变更前：Non-sendable对象赋值给Sendable类型的部分场景中，DevEco编辑界面没有错误提示，编译没有报错。

变更后：Non-sendable对象赋值给Sendable类型的部分场景中，DevEco编辑界面有错误提示，编译有报错。

当错误对象被当成Sendable对象使用时，将运行时报错提前到编译期。当错误对象被当做普通对象使用时，运行时不报错但编译期新增报错。变更前，在一些场景下Non-sendable对象可以被赋值给Sendable类型。变更后，Non-sendable对象不可以赋值给Sendable类型。

下面的场景将会报错：

Sendable赋值约束

场景一：当错误对象被当成Sendable对象使用时

变更前

```
1. // declaration.ets
2. export class NonSendableClass {};
3. @Sendable
4. export class SendableClass {};

6. export class NonSendableClassT<T> {};
7. @Sendable
8. export class SendableClassT<T> {};

10. // main.ets
11. import { NonSendableClass, SendableClass, NonSendableClassT, SendableClassT } from './declaration';
12. import collections from '@arkts.collections';

14. @Sendable
15. class SendableData {
16. propA: SendableClass = new NonSendableClass(); // Runtime ERROR
17. propB: SendableClassT<number>;
18. propC: SendableClass;
19. propD: SendableClass;
20. propE: SendableClass;

22. constructor(sendableT: SendableClassT<number>) {
23. const sendableList: SendableClass[] = [new NonSendableClass()];
24. this.propB = new NonSendableClassT<number>(); // Runtime ERROR
25. this.propC = this.getSendable(); // Runtime ERROR
26. this.propD = sendableList[0]; // Runtime ERROR
27. this.propE = sendableT; // Runtime ERROR
28. }

30. getSendable(): SendableClass {
31. return new NonSendableClass();
32. }
33. }

35. new SendableData(new NonSendableClassT<number>());

37. const sendable: SendableClassT<number> = new NonSendableClassT<number>();
38. const sendableArray: collections.Array<SendableClass> = new collections.Array<SendableClass>();
39. sendableArray.push(sendable); // Runtime ERROR
```

变更后

```
1. // declaration.ets
2. export class NonSendableClass {};
3. @Sendable
4. export class SendableClass {};

6. export class NonSendableClassT<T> {};
7. @Sendable
8. export class SendableClassT<T> {};

10. // main.ets
11. import { NonSendableClass, SendableClass, NonSendableClassT, SendableClassT } from './declaration';
12. import collections from '@arkts.collections';

14. @Sendable
15. class SendableData {
16. propA: SendableClass = new NonSendableClass(); // ArkTS compile-time error
17. propB: SendableClassT<number>;
18. propC: SendableClass;
19. propD: SendableClass;
20. propE: SendableClass;

22. constructor(sendableT: SendableClassT<number>) {
23. const sendableList: SendableClass[] = [new NonSendableClass()]; // ArkTS compile-time error
24. this.propB = new NonSendableClassT<number>(); // ArkTS compile-time error
25. this.propC = this.getSendable();
26. this.propD = sendableList[0];
27. this.propE = sendableT;
28. }

30. getSendable(): SendableClass {
31. return new NonSendableClass(); // ArkTS compile-time error
32. }
33. }

35. new SendableData(new NonSendableClassT<number>()); // ArkTS compile-time error

37. const sendable: SendableClassT<number> = new NonSendableClassT<number>(); // ArkTS compile-time error
38. const sendableArray: collections.Array<SendableClass> = new collections.Array<SendableClass>();
39. sendableArray.push(sendable);
```

场景二：错误对象被当作普通对象使用时，影响：新增报错

变更前

```
1. class NonSendableClass {};
2. @Sendable
3. class SendableClass {};

5. class NonSendableClassT<T> {};
6. @Sendable
7. class SendableClassT<T> {};

9. function getSendable(): SendableClass {
10. return new NonSendableClass();
11. }

13. const objectA: SendableClass = getSendable();
14. const objectB: SendableClassT<number> = new NonSendableClassT<number>();
```

变更后

```
1. class NonSendableClass {};
2. @Sendable
3. class SendableClass {};

5. class NonSendableClassT<T> {};
6. @Sendable
7. class SendableClassT<T> {};

9. function getSendable(): SendableClass {
10. return new NonSendableClass(); // ArkTS compile-time error
11. }

13. const objectA: SendableClass = getSendable();
14. const objectB: SendableClassT<number> = new NonSendableClassT<number>(); // ArkTS compile-time error
```

**该能力起始支持的API Level**

ArkTS Sendable语法检查从API 12起启用。

**变更的接口/组件**

不涉及。

**适配指导**

避免把Non-sendable对象赋值给Sendable变量/参数/返回值。

## ArkUI

### 按下鼠标任意按键移动鼠标情况下不再上报鼠标事件的行为变更

**变更原因**

优化鼠标按压态下拖移的执行效率。

**变更影响**

此变更涉及应用适配。

变更前：按压鼠标按键拖移过程中，中途经过的控件会收到鼠标事件。

变更后：按压鼠标按键拖移过程中，中途经过的控件不再会收到鼠标事件。

| 变更前(按住鼠标进行拖移) | 变更后(按住鼠标进行拖移) |
| --- | --- |
|  |  |

**该能力起始支持的API Level**

12

**变更的接口/组件**

[onHover](../harmonyos-references/ts-universal-events-hover.md#onhover)

[onMouse](../harmonyos-references-V5/ts-universal-mouse-key-V5.md#onmouse)

**适配指导**

如果开发者需要在按住鼠标按键移动情况下，中间经过的控件也要有hover效果，则需要整改为通过点击开始时命中的控件接收鼠标事件，自行处理。如果当前鼠标移动为拖拽场景，则不要使用[onHover](../harmonyos-references/ts-universal-events-hover.md#onhover)和[onMouse](../harmonyos-references-V5/ts-universal-mouse-key-V5.md#onmouse)而是通过[onDragMove](../harmonyos-references-V5/ts-universal-events-drag-drop-V5.md#ondragmove)去处理鼠标移动事件。

## 构造@ComponentV2修饰的自定义组件时，增加对常规变量的构造赋值校验

**变更原因**

在@ComponentV2修饰的自定义组件中使用@Local、@Provider()、@Consumer()、常规变量(没有任何装饰器修饰的，不涉及更新的普通变量)，在构造的时候传参赋值，进行校验并输出错误信息。

**变更影响**

此变更涉及应用适配。

执行下列用例：

```
1. @Entry
2. @ComponentV2
3. struct v2DecoratorInitFromParent {
4. build() {
5. Column() {
6. testChild({
7. regular_value: "hello",
8. local_value: "hello",
9. provider_value: "hello",
10. consumer_value: "hello"
11. })
12. }
13. }
14. }

16. @ComponentV2
17. struct testChild {
18. regular_value: string = "hello";
19. @Local local_value: string = "hello";
20. @Provider() provider_value: string = "hello";
21. @Consumer() consumer_value: string = "hello";
22. build() {}
23. }
```

变更前无报错

变更后报错信息为：

Property 'regular\_value' in the custom component 'testChild' cannot initialize here (forbidden to specify).

Property 'local\_value' in the custom component 'testChild' cannot initialize here (forbidden to specify).

Property 'provider\_value' in the custom component 'testChild' cannot initialize here (forbidden to specify).

Property 'consumer\_value' in the custom component 'testChild' cannot initialize here (forbidden to specify).

**该能力起始支持的API Level**

V2装饰器从API 12开始提供。

**适配指导**

如果开发者不按规范使用对应范式，则需按日志提示信息进行修改。

### @ohos.arkui.advanced.SubHeader删除SymbolRenderingStrategy和SymbolEffectStrategy

**变更原因**

SymbolGlyph中已定义SymbolRenderingStrategy和SymbolEffectStrategy，避免重复枚举定义。减少开发者引用工作量。

**变更影响**

此变更涉及应用适配。

变更前，引用@ohos.arkui.advanced.SubHeader中SymbolRenderingStrategy和SymbolEffectStrategy，运行时报错：

1.Error message:the requested module '@ohos.arkui.advanced.SubHeader' does not provide an export name 'SymbolRenderingStrategy' and 'SymbolEffectStrategy'.

变更后，引用@ohos.arkui.advanced.SubHeader中SymbolRenderingStrategy和SymbolEffectStrategy，编译期报错：

1.Module '@ohos.arkui.advanced.SubHeader' has no exported member 'SymbolRenderingStrategy' and 'SymbolEffectStrategy'.

**该能力起始支持的API Level**

12

**适配指导**

如果开发者不按规范使用对应范式，则需按编译提示信息进行修改。参考API文档，删除引用SubHeader中SymbolRenderingStrategy和SymbolEffectStrategy，自动引用SymbolGlyph中SymbolRenderingStrategy和SymbolEffectStrategy。

适配示例：

```
1. import { promptAction, OperationType, SubHeader } from '@kit.ArkUI'

3. @Entry
4. @Component
5. struct SubHeaderExample {
6. build() {
7. Column() {
8. SubHeader({
9. icon: $r('sys.symbol.ohos_wifi'),
10. iconSymbolOptions: {
11. effectStrategy: SymbolEffectStrategy.HIERARCHICAL,
12. renderingStrategy: SymbolRenderingStrategy.MULTIPLE_COLOR,
13. fontColor: [Color.Blue, Color.Grey, Color.Green],
14. },
15. secondaryTitle: '标题',
16. operationType: OperationType.BUTTON,
17. operationItem: [{ value: '操作',
18. action: () => {
19. promptAction.showToast({ message: 'demo' })
20. }
21. }]
22. })
23. }
24. }
25. }
```

### setWindowSystemBarEnable、setSystemBarEnable不在PC/2in1设备生效

**变更原因**

在PC/2in1设备下，全屏状态下的状态栏显示控制由系统布局约束，无需再调用接口去控制状态栏的显示和隐藏。即设置的setWindowSystemBarEnable、setSystemBarEnable在PC/2in1设备上不生效。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/LOqYv0vuSHifTY_ezpR3jQ/zh-cn_image_0000001993261849.png?HW-CC-KV=V1&HW-CC-Date=20260429T052410Z&HW-CC-Expire=86400&HW-CC-Sign=36B44CCFB5E9BFE4CB8CDD221602398FF7A9AC6C3EF819395DF11F3DDB23EAF7)

**变更影响**

此变更涉及应用适配。

此变更从API 12起生效，使用API 11及之前版本SDK进行编译的应用不受影响。

变更前PC/2in1设备上全屏调用此接口可以显示和隐藏状态栏。

变更后PC/2in1设备上窗口布局会自动适配避让逻辑，无需调用接口控制。

**该能力起始支持的API Level**

9

**变更的接口/组件**

@ohos.window.d.ts

setWindowSystemBarEnable

setSystemBarEnable

**适配指导**

默认效果变更，无需适配，但应注意变更后的默认效果是否影响应用显示效果。

## User Authentication Kit

### @ohos.useriam.userAuthIcon导出命名变更

**变更原因**

不符合命名规范，需将导出命名从小驼峰userAuthIcon改为大驼峰UserAuthIcon。

**变更影响**

此变更涉及应用适配。

变更前

```
1. import { userAuth, userAuthIcon } from '@kit.UserAuthenticationKit';
```

变更后

```
1. import { userAuth, UserAuthIcon } from '@kit.UserAuthenticationKit';
```

如不适配代码会导致编译报错，报错信息如下：

```
1. '"@kit.UserAuthenticationKit"' has no exported member named 'userAuthIcon'. Did you mean 'UserAuthIcon'? <ArkTSCheck>。
```

**该能力起始支持的API Level**

12

**变更的接口/组件**

@ohos.useriam.userAuthIcon

**适配指导**

```
1. import { userAuth, UserAuthIcon } from '@kit.UserAuthenticationKit';

3. @Entry
4. @Component
5. struct Index {
6. authParam: userAuth.AuthParam = {
7. challenge: new Uint8Array([49, 49, 49, 49, 49, 49]),
8. authType: [userAuth.UserAuthType.FACE, userAuth.UserAuthType.PIN],
9. authTrustLevel: userAuth.AuthTrustLevel.ATL3
10. };
11. widgetParam: userAuth.WidgetParam = {
12. title: '请进行身份认证'
13. };

15. build() {
16. Row() {
17. Column() {
18. UserAuthIcon({
19. authParam: this.authParam,
20. widgetParam: this.widgetParam,
21. iconHeight: 200,
22. iconColor: Color.Blue,
23. onIconClick: () => {
24. console.info('The user clicked the icon.');
25. },
26. onAuthResult: (result: userAuth.UserAuthResult) => {
27. console.info('Get user auth result, result = ' + JSON.stringify(result));
28. }
29. })
30. }
31. }
32. }
33. }
```
