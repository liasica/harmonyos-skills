---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-for-all-apps-6002
title: OS平台API行为的变更
breadcrumb: 版本说明 > HarmonyOS 6.0.0(20) > OS平台能力 > OS平台行为变更说明 > 6.0.0(20) Beta2引入的行为变更 > OS平台API行为的变更
category: harmonyos-releases
scraped_at: 2026-04-29T13:21:48+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:dca2465750f25573547d69c2d7693c2d7bbb015878f5bdbe8171dd29a8dd6870
---

## Ability Kit

### Ability Kit相关公共事件行为变更，增加管控

**变更原因**

Ability Kit部分公共事件中包含应用信息，需要增加管控措施。

**变更影响**

此变更涉及应用适配。

对于公共事件[COMMON\_EVENT\_PACKAGE\_ADDED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_added)、[COMMON\_EVENT\_PACKAGE\_REMOVED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_removed)、[COMMON\_EVENT\_PACKAGE\_CHANGED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_changed)、[COMMON\_EVENT\_PACKAGE\_RESTARTED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_restarted)、[COMMON\_EVENT\_PACKAGE\_DATA\_CLEARED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_data_cleared)、[COMMON\_EVENT\_PACKAGE\_CACHE\_CLEARED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_cache_cleared)、[COMMON\_EVENT\_QUICK\_FIX\_APPLY\_RESULT](../harmonyos-references/commoneventmanager-definitions.md#common_event_quick_fix_apply_result)的订阅方增加了管控。

变更前，系统应用和三方应用都可以监听到相关事件。

变更后，系统应用可以监听自身应用和其他应用的相关事件，而三方应用只能监听到自身应用的相关事件。

**起始API Level**

9

**变更的接口/组件**

变更的公共事件列表：

| 事件名称 | 描述 |
| --- | --- |
| [COMMON\_EVENT\_PACKAGE\_ADDED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_added) | 应用安装完成的事件。 |
| [COMMON\_EVENT\_PACKAGE\_REMOVED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_removed) | 应用卸载完成的事件。 |
| [COMMON\_EVENT\_PACKAGE\_CHANGED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_changed) | 应用更新完成的事件。 |
| [COMMON\_EVENT\_PACKAGE\_RESTARTED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_restarted) | 应用重新启动的事件。 |
| [COMMON\_EVENT\_PACKAGE\_DATA\_CLEARED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_data_cleared) | 应用数据清理完成的事件。 |
| [COMMON\_EVENT\_PACKAGE\_CACHE\_CLEARED](../harmonyos-references/commoneventmanager-definitions.md#common_event_package_cache_cleared) | 应用缓存数据清理完成的事件。 |
| [COMMON\_EVENT\_QUICK\_FIX\_APPLY\_RESULT](../harmonyos-references/commoneventmanager-definitions.md#common_event_quick_fix_apply_result) | 应用使能快速修复包完成的事件。 |

**适配指导**

如果使用上述公共事件判断应用是否安装，请改用[canOpenLink](../harmonyos-references/js-apis-bundlemanager.md#bundlemanagercanopenlink12)接口来查询应用是否存在。

## ArkTS

### TreeSet/TreeMap扩容导致比较器丢失问题正向修复

**变更原因**

使用TreeSet/TreeMap模块的add接口触发扩容时，TreeSet/TreeMap自定义比较器会在扩容后丢失，导致扩容之后进行系统默认排序。

**变更影响**

此变更涉及应用适配。

说明

此变更已做版本隔离，变更仅在应用的targetSdkVersion设置为大于等于6.0.0(20)时生效。

变更前：

对于下述代码，预期结果与实际执行结果不一致，结果出现错误。

原因在于扩容后比较器丢失，remove(a1)失败，后续行为异常。

```
1. import { TreeSet } from '@kit.ArkTS';

3. class A {
4. time: number;
5. constructor(time: number) {
6. this.time = time;
7. }
8. static readonly compared = ((first: A, second: A): number => {
9. return second.time - first.time;
10. }) as Function as (first: A, second: A) => boolean;
11. }
12. const a1 = new A(1);
13. const a2 = new A(2);
14. const a3 = new A(3);
15. const a4 = new A(4);
16. const a5 = new A(5);
17. const a6 = new A(6);
18. const set = new TreeSet<A>(A.compared); // 在add扩容后A.compared丢失
19. set.add(a1);
20. set.add(a2);
21. set.add(a3); // 触发扩容，A.compared丢失
22. set.add(a4);
23. set.add(a5);
24. set.add(a6);
25. for (let i = 0; i < 5; ++i) {
26. set.remove(a1); // 同一个红黑树前后用了两种比较规则，数据结构的性质被破坏
27. console.info(set.has(a1).toString());
28. // 预期结果：false、false、false、false、false
29. // 实际结果：false、false、true、true、true
30. set.add(a1);
31. }
32. for (let item of set) {
33. console.info(item.time.toString());
34. // 预期结果：6、5、4、3、2、1
35. // 实际结果：6、1、1
36. }
```

变更后：

TaggedTree比较器扩容前后一致，TaggedTree的所有add、remove都用同一个比较规则，输出结果与预期一致。

**起始API Level**

8

**变更的接口/组件**

TreeSet、TreeMap

**适配指导**

行为变更，绝大多数情况不需要开发者进行适配。

只有当开发者用到自定义比较器，且将原本错误的结果当成正确的结果进行使用时，需注意TreeSet/TreeMap结果的变化，并按照修复后的结果进行代码适配。

## ArkUI

### 位置控件功能变更

**变更原因**

从最新的大数据分析，在需要获取位置信息时，大部分应用使用地图picker或者权限弹窗来申请位置权限，仅有极少数应用使用位置控件，该特性的价值有限，经谨慎评估将该特性下架。

位置控件已经在API 15版本开始废弃，此次需要将位置控件的接口删除。

**变更影响**

该变更涉及应用适配。

变更前：

应用界面上集成位置控件，用户点击位置控件后，应用可获取临时的位置权限。其中，用户首次在应用中使用位置控件时，会弹出确认弹窗请求用户允许或者拒绝。

变更后：

1. 位置控件相关的接口从SDK中删除。
2. 升级镜像后，存量的应用可以继续使用位置控件功能。位置控件每次被点击后，都会弹出确认弹窗请求用户允许或者拒绝。

**起始API Level**

10

**变更的接口/组件**

@internal/component/ets/location\_button.d.ts中所有接口。

**适配指导**

开发者通过权限弹窗申请用户授权，指导：[申请应用权限](../harmonyos-guides/request-user-authorization.md)。

### 通用属性drawModifier接口行为变更

**变更原因**

（1）当drawModifier接口参数从DrawModifier对象变为undefined时，实际生效的仍是原来的DrawModifier对象。开发者无法重置其值，这与通用属性接口的规范不符。

（2）当前实现中，若组件设置了drawModifier属性，则默认会在生命周期的布局阶段之后触发重绘。对于绘制内容和尺寸均未发生变化的场景，这将导致多余的重绘，造成性能损耗。因此，调整设置drawModifier的节点的重绘规则，默认仅执行过测量过程的节点才进行重绘。

**变更影响**

此变更涉及应用适配。

* 变更前：（1）drawModifier接口参数从DrawModifier对象变为undefined后，生效的仍旧是原来的DrawModifier对象。（2）任何组件，如果设置了drawModifier属性，无论是否跳过测量（尺寸是否发生变化），都会触发重绘。
* 变更后：（1）drawModifier接口参数从DrawModifier对象变为undefined后，会将原来设置的值重置为undefined。（2）任何组件，如果设置了drawModifier属性，当其未跳过测量（尺寸可能发生变化）时，就会触发重绘。

**起始API Level**

12

**变更的接口/组件**

drawModifier

**适配指导**

（1）变更前，this.modifier = undefined;不会清除组件上生效的DrawModifier对象，而变更后则会完成清除。因此，若想保持行为不变，需要注释或删除这一行代码。

（2）若开发者的自定义绘制内容变化逻辑受到本次变更影响，在受影响属性变化的代码后加入invalidate以主动触发重绘，即可完成适配。

具体适配方案可参考下文示例。

```
1. import { drawing } from '@kit.ArkGraphics2D';

3. class MyFrontDrawModifier extends DrawModifier {
4. public scaleX: number = 1;
5. public scaleY: number = 1;
6. public uiContext: UIContext;

8. constructor(uiContext: UIContext) {
9. super();
10. this.uiContext = uiContext;
11. }

13. drawFront(context: DrawContext): void {
14. const brush = new drawing.Brush();
15. brush.setColor({
16. alpha: 255,
17. red: 0,
18. green: 0,
19. blue: 255
20. });
21. context.canvas.attachBrush(brush);
22. const halfWidth = context.size.width / 2;
23. const halfHeight = context.size.width / 2;
24. const radiusScale = (this.scaleX + this.scaleY) / 2;
25. context.canvas.drawCircle(this.uiContext.vp2px(halfWidth), this.uiContext.vp2px(halfHeight), this.uiContext.vp2px(20 * radiusScale));
26. }
27. }

29. @Entry
30. @Component
31. struct DrawModifierExample {
32. @State public modifierToBeCleared: DrawModifier | undefined = new MyFrontDrawModifier(this.getUIContext());
33. public modifierToBeChanged: MyFrontDrawModifier = new MyFrontDrawModifier(this.getUIContext());
34. @State public testWidth: number = 100;

36. build() {
37. Column() {
38. Button("clearModifier").onClick(() => {
39. // 变更前：下面代码不生效，Row组件仍旧绑定原本的modifier
40. this.modifierToBeCleared = undefined;
41. // 规避方法：变更前若想清空Text组件的自定义绘制效果，可将其绑定的变量变为基类对象
42. this.modifierToBeCleared = new DrawModifier();
43. // 变更后：若开发者期望行为和变更前保持一致，即下面代码不生效的话，只需要注释掉这一行即可
44. // this.modifierToBeCleared = undefined;
45. })
46. Column() {
47. Row()
48. .width(100)
49. .height(100)
50. .margin(10)
51. .backgroundColor(Color.Gray)
52. .drawModifier(this.modifierToBeCleared)
53. }
54. .margin({ bottom: 50 })
55. Button('changeModifier')
56. .onClick(() => {
57. this.testWidth++;
58. this.modifierToBeChanged.scaleX += 0.1;
59. this.modifierToBeChanged.scaleY += 0.1;
60. // 变更前自动更新，变更后需要手动调用invalidate方法适配
61. this.modifierToBeChanged?.invalidate();
62. })
63. Column() {
64. Row()
65. .width(100)
66. .height(100)
67. .margin(10)
68. .backgroundColor(Color.Gray)
69. .drawModifier(this.modifierToBeChanged)
70. Row() {
71. Text("hello world")
72. .width(this.testWidth)
73. .height(100)
74. }
75. }
76. .width(300)
77. .height(300)
78. }
79. }
80. }
```

### 半模态SIDE侧边样式新增避让软键盘能力

**变更原因**

[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)半模态弹窗侧边样式默认支持避让软键盘，提升易用性。

**变更影响**

此变更涉及应用适配。

* 变更前：当半模态样式指定为[SheetType](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheettype11枚举说明)的SIDE侧边样式时，[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)的属性keyboardAvoidMode设置为[SheetKeyboardAvoidMode](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetkeyboardavoidmode13枚举说明)的避让软键盘方式无效，半模态默认不避让软键盘，需要开发者自定义避让软键盘。
* 变更后：当半模态样式指定为[SheetType](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheettype11枚举说明)的SIDE侧边样式时，[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)的属性keyboardAvoidMode设置为[SheetKeyboardAvoidMode](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetkeyboardavoidmode13枚举说明)的避让软键盘方式将生效，半模态支持避让软键盘，默认值为SheetKeyboardAvoidMode.TRANSLATE\_AND\_SCROLL。若开发者希望自定义避让软键盘，则需设置属性keyboardAvoidMode = SheetKeyboardAvoidMode.NONE。

**起始API Level**

* bindSheet：10
* SheetType：11

**变更的接口/组件**

* bindSheet的keyboardAvoidMode属性
* SheetType的SIDE半模态侧边样式

**适配指导**

默认行为变更，当半模态样式指定为[SheetType](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheettype11枚举说明)的SIDE侧边样式时，若开发者期望自定义避让软键盘，则需要设置[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)的属性keyboardAvoidMode = [SheetKeyboardAvoidMode](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetkeyboardavoidmode13枚举说明).NONE。

若开发者期望采用半模态控件自带的避让软键盘能力，则可以设置[bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet)的属性keyboardAvoidMode = [SheetKeyboardAvoidMode](../harmonyos-references/ts-universal-attributes-sheet-transition.md#sheetkeyboardavoidmode13枚举说明)的其他枚举值，或者不设置属性keyboardAvoidMode，采用默认值。

### CanvasRenderer的font接口支持自定义字体行为变更

**变更原因**

增强基础能力，CanvasRenderer的font接口支持设置自定义字体。

**变更影响**

此变更涉及应用适配。

变更前，CanvasRenderer的font接口设置自定义字体不生效，绘制字体显示为默认字体。

变更后，CanvasRenderer的font接口设置自定义字体生效，绘制字体显示为自定义字体。

```
1. import { text } from "@kit.ArkGraphics2D"

3. // xxx.ets
4. @Entry
5. @Component
6. struct FontDemo {
7. private settings: RenderingContextSettings = new RenderingContextSettings(true)
8. private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings)

10. build() {
11. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
12. Canvas(this.context)
13. .width('100%')
14. .height('100%')
15. .backgroundColor('rgb(213,213,213)')
16. .onReady(() => {
17. let fontCollection = text.FontCollection.getGlobalInstance();
18. fontCollection.loadFontSync('HarmonyOS_Sans_Thin_Italic', $rawfile("HarmonyOS_Sans_Thin_Italic.ttf"))
19. this.context.font = "50px HarmonyOS_Sans_Thin_Italic"
20. this.context.fillText("Hello World", 20, 60)
21. })
22. }
23. .width('100%')
24. .height('100%')
25. }
26. }
```

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

8

**变更的接口/组件**

CanvasRenderingContext2D和OffscreenCanvasRenderingContext2D的font接口。

**适配指导**

变更后，CanvasRenderer的font接口设置自定义字体生效。若需保持变更前的默认字体行为，可以不设置自定义字体。

### 去除保存控件系统提示弹框变更

**变更原因**

当前，保存控件支持自定义UI样式。应用选择使用自定义UI，当用户点击保存控件，成功保存媒体库文件时，系统将弹出系统弹框提示用户。在开发过程中，开发者可以调用指定API调整该系统弹框的位置。

保存控件系统提示弹框：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/6ubE1rI_TgqWMk6LAmdfsg/zh-cn_image_0000002394557509.png?HW-CC-KV=V1&HW-CC-Date=20260429T052147Z&HW-CC-Expire=86400&HW-CC-Sign=E946D5C0F0CDA4F64F3CB9E2D640515B646C5ED8118B84C3612C30AE76B3510F)

经评估，强制弹出系统弹框会与应用内已有弹框冲突，体验不够友好，系统将取消该系统强制弹框的行为。

**变更影响**

该变更涉及应用适配。

变更前：当开发者需要自定义保存控件的图标和文本时，或者保存控件不满足[约束与限制](../harmonyos-guides/security-component-overview.md#约束与限制)，点击保存控件时会弹出系统提示弹框。开发者可以使用tipPosition接口设置保存控件系统提示弹框展示在屏幕上的位置。

变更后：保存控件被点击后不会弹出系统提示弹框。开发者无法调用系统提示弹框的位置设置接口tipPosition。应用可根据自身UX设计，自行选择是否实现应用内保存提示。

**起始API Level**

20

**变更的接口/组件**

删除接口如下：

| 类名 | 删除接口声明 |
| --- | --- |
| SaveButtonAttribute | tipPosition(position: SaveButtonTipPosition) |

删除枚举如下：

| 枚举类型 | 删除的键值 |
| --- | --- |
| SaveButtonTipPosition | ABOVE\_BOTTOM |
| SaveButtonTipPosition | BELOW\_TOP |

**适配指导**

取消对设置系统提示位置接口tipPosition的调用，否则会导致编译和运行失败。

## Basic Services Kit

### zlib.unzipFile和zlib.decompressFile解压文件接口变更

**变更原因**

解压文件时，针对格式有误的压缩包进行拦截，避免解压之后的文件不符合预期。

**变更影响**

此变更涉及应用适配。

变更前，对于格式有误的压缩包能够正常解压成功，但解压出来的内容不符合预期。

变更后，对于格式有误的压缩包会解压失败，抛出文件格式有误的错误码。

**起始API Level**

9

**变更的接口/组件**

zlib.unzipFile

zlib.decompressFile

**适配指导**

调用zlib.unzipFile和zlib.decompressFile接口时，需要捕获接口异常，根据返回的错误码进行处理，检查传入的压缩包是否有误。

## Data Augmentation Kit

### retrieval.VectorQuery接口value字段变更为可选

**变更原因**

支持在检索接口中，自动将query生成向量。

**变更影响**

此变更涉及应用适配。

必选参数改为可选参数，未适配应用编译会报错。

**起始API Level**

6.0.0(20)

**变更的接口/组件**

retrieval.VectorQuery接口的value字段

**适配指导**

前提：该接口的上级节点为RecallCondition，如果传入了RecallCondition，则认为需要进行向量检索，此时就需要开发者在value接口传入query向量，或系统生成query向量，用于检索。

情况1：如果开发者正常填入value字段：则不需适配。

情况2：如果开发者未填入该字段：变更前，将该字段作为入参的方法会报错，完全无法正常使用；变更后，会自动生成向量并正常执行检索。

情况3：使用retrieval.VectorQuery接口的value属性，对新定义的变量赋值，需要做如下修改：

```
1. let floatArray = new Float32Array([0.1, 0.2]);
2. let vectorQuery:retrieval.VectorQuery = {
3. column:"keywords",
4. value:floatArray,
5. similarityThreshold:0.35
6. }

8. let value1:Float32Array = vectorQuery.value;               // 错误写法：value变更为可选字段后，编译报错
9. let value2:Float32Array | undefined = vectorQuery.value;   // 正确写法
```

## Localization Kit

### 泰国、沙特阿拉伯、阿富汗和伊朗的默认历法变更

**变更原因**

泰国、沙特阿拉伯、阿富汗和伊朗的默认历法配置错误。

**变更影响**

此变更不涉及应用适配。

变更前：泰国的默认历法为佛历，沙特阿拉伯的默认历法为伊斯兰历，阿富汗和伊朗的默认历法为波斯历。例如，创建[intl.DateTimeFormat](../harmonyos-references/js-apis-intl.md#datetimeformatdeprecated)时，传入地区为泰国，则调用[format](../harmonyos-references/js-apis-intl.md#formatdeprecated)接口时，会使用佛历显示日期。

变更后：泰国、沙特阿拉伯、阿富汗和伊朗的默认历法均为公历。例如，创建[intl.DateTimeFormat](../harmonyos-references/js-apis-intl.md#datetimeformatdeprecated)时，传入地区为泰国，则调用[format](../harmonyos-references/js-apis-intl.md#formatdeprecated)接口时，会使用公历显示日期。

**起始API Level**

8

**变更的接口/组件**

| 文件 | 接口 |
| --- | --- |
| @ohos.intl.d.ts | [intl.DateTimeFormat.prototype.format](../harmonyos-references/js-apis-intl.md#formatdeprecated) |
| @ohos.intl.d.ts | [intl.DateTimeFormat.prototype.formatRange](../harmonyos-references/js-apis-intl.md#formatrangedeprecated) |
| @ohos.i18n.d.ts | [i18n.Calendar.prototype.getDisplayName](../harmonyos-references/js-apis-i18n.md#getdisplayname8) |
| @ohos.i18n.d.ts | [i18n.Calendar.prototype.get](../harmonyos-references/js-apis-i18n.md#get8) |

**适配指导**

仅改变接口内部使用的历法，无需开发者进行适配。

## NDK开发

### libc++ condition\_variable::wait\_for接口变更

**变更原因**

变更前，libc++库condition\_variable::wait\_for接口使用系统墙上时间，受到修改系统时间的影响，和开发者预期不符合。

```
1. template <class _Rep, class _Period>
2. cv_status
3. condition_variable::wait_for(unique_lock<mutex>& __lk,
4. const chrono::duration<_Rep, _Period>& __d)
5. {
6. ...

8. #if defined(_LIBCPP_HAS_COND_CLOCKWAIT)
9. using __clock_tp_ns = time_point<steady_clock, nanoseconds>;
10. __ns_rep __now_count_ns = _VSTD::__safe_nanosecond_cast(__c_now.time_since_epoch()).count();
11. #else
12. using __clock_tp_ns = time_point<system_clock, nanoseconds>;
13. __ns_rep __now_count_ns = _VSTD::__safe_nanosecond_cast(system_clock::now().time_since_epoch()).count();
14. #endif

16. ...
17. __do_timed_wait(...);
18. ...
19. }
```

```
1. void
2. condition_variable::__do_timed_wait(unique_lock<mutex>& lk,
3. chrono::time_point<chrono::system_clock, chrono::nanoseconds> tp) noexcept
4. {
5. ...
6. nanoseconds d = tp.time_since_epoch();
7. if (d > nanoseconds(0x59682F000000E941))
8. d = nanoseconds(0x59682F000000E941);
9. ...
10. int ec = __libcpp_condvar_timedwait(&__cv_, lk.mutex()->native_handle(), &ts);
11. ...
12. }
```

其中0x59682F000000E941 ns = 6442450944s = 2174-02-25 17:42:24，当系统当前时间加上wait\_for接口入参需要等待的时间超过该值时被截断，\_\_libcpp\_condvar\_timedwait会立即返回。

**变更影响**

此变更涉及应用适配。

* 变更前：libc++库condition\_variable::wait\_for接口使用系统墙上时间，受修改系统时间影响；当系统当前时间加上接口入参需要等待的时间超过特定值（0x59682F000000E941），condition\_variable::wait\_for接口会立即返回。
* 变更后：libc++库condition\_variable::wait\_for接口使用单调递增时间，不受修改系统时间影响。

**起始API Level**

9

**适配指导**

libc++库以二进制的形式发布在NDK中（libc++\_shared.so）。condition\_variable::wait\_for接口原型未变，只是实现和C++标准、安卓、iOS、Windows等平台保持一致，开发者更新NDK后重新编译应用即可。

## Share Kit

### on('dataReceive')接口新增必填参数capabilities

**变更原因**

若应用在PC/2in1侧接入了沙箱接收，手机到PC/2in1碰一碰会将手机侧分享的所有数据都给到应用，考虑到不同应用能处理的数据类型存在差异。为防止手机侧分享的数据在PC/2in1侧应用无法处理带来的用户体验问题，针对PC/2in1侧沙箱接收的接口做出调整。RecvCapabilityRegistry新增必填参数capabilities，需应用配置支持的数据类型及最大数量。

**变更影响**

沙箱接收注册接口新增必填参数，此变更涉及应用适配，未适配应用编译会报错。

**起始API Level**

6.0.0(20)

**变更的接口/组件**

on('dataReceive')/off('dataReceive')接口第二个参数RecvCapabilityRegistry新增必填参数capabilities。

**适配指导**

新增必填参数capabilities，应用接入沙箱接收能力时，需配置支持接收的数据类型及最大数量。

```
1. import { uniformTypeDescriptor as utd } from '@kit.ArkData';
2. import { systemShare, harmonyShare } from '@kit.ShareKit';
3. import { common } from '@kit.AbilityKit';

5. @Component
6. export default struct Index {
7. aboutToAppear(): void {
8. let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
9. windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
10. capabilities: [{
11. utd: utd.UniformDataType.IMAGE, // 仅可接收图片类型文件
12. maxSupportedCount: 1, // 最大可接收1个文件
13. }]
14. }
15. // 注册沙箱接收'dataReceive'监听事件
16. harmonyShare.on('dataReceive', capabilityRegistry, (receivableTarget: harmonyShare.ReceivableTarget) => {
17. let uiContext: UIContext = this.getUIContext();
18. let context = uiContext.getHostContext() as common.UIAbilityContext;
19. receivableTarget.receive(context.filesDir, {
20. // 此路径仅为示例 使用时请替换实际路径
21. onDataReceived: (sharedData: systemShare.SharedData) => {
22. let sharedRecords = sharedData.getRecords();
23. sharedRecords.forEach((record: systemShare.SharedRecord) => {
24. // 处理分享数据
25. });
26. },
27. onResult(resultCode: harmonyShare.ShareResultCode) {
28. if (resultCode === harmonyShare.ShareResultCode.SHARE_SUCCESS) {
29. // To do things.
30. }
31. }
32. });
33. });
34. }

36. aboutToDisappear(): void {
37. let capabilityRegistry: harmonyShare.RecvCapabilityRegistry = {
38. windowId: 999, // 此值仅为示例 实际使用时请替换正确的windowId
39. capabilities: [{
40. utd: utd.UniformDataType.IMAGE,
41. maxSupportedCount: 1,
42. }]
43. }
44. // 解除沙箱接收'dataReceive'监听事件
45. harmonyShare.off('dataReceive', capabilityRegistry);
46. }

48. build() {
49. }
50. }
```
