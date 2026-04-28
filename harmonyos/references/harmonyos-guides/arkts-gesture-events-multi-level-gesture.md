---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-multi-level-gesture
title: 多层级手势事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 添加手势响应 > 多层级手势事件
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:54+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8be15410d63ae89dea9c729793a0292a1d4f6061b51eb0f93766d1dd77ce0fda
---

多层级手势事件指父子组件嵌套时，父子组件均绑定了手势或事件。在该场景下，手势或者事件的响应受到多个因素的影响，相互之间发生传递和竞争，容易出现预期外的响应。

本章主要介绍了多层级手势事件的默认响应顺序，以及如何通过设置相关属性影响多层级手势事件的响应顺序。

## 默认多层级手势事件

### 触摸事件

[触摸事件](../harmonyos-references/ts-universal-events-touch.md)（onTouch事件）是所有手势组成的基础，包括Down、Move、Up、Cancel四种类型。手势均由触摸事件组成，例如，点击为Down和Up，滑动为Down和一系列Move及Up。触摸事件具有以下特殊性：

1.监听了onTouch事件的组件，在手指落下被触摸时均会收到onTouch事件的回调，被触摸受到触摸热区和触摸控制影响。

2.onTouch事件的回调是闭环的。若一个组件收到了手指Id为0的Down事件，后续也会收到手指Id为0的Move事件和Up事件。

3.onTouch事件的回调是一致的。若一个组件收到了手指Id为0的Down事件，但未收到手指Id为1的Down事件，则后续只会收到手指Id为0的touch事件，不会收到手指Id为1的后续touch事件。

对于一般的容器组件（例如：Column），父子组件之间onTouch事件能够同时触发，兄弟组件之间onTouch事件根据布局进行触发。

```
1. Column() {
2. Column().id('ComponentB').onTouch(() => {})
3. Column().id('ComponentC').onTouch(() => {})
4. }.id('ComponentA').onTouch(() => {})
```

[TouchEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultilevelGestureEvents/entry/src/main/ets/pages/TouchEvent.ets#L20-L25)

组件B和组件C作为组件A的子组件，当触摸到组件B或者组件C时，组件A也会被触摸到。onTouch事件允许多个组件同时触发，因此，当触摸组件B时，会触发组件A和组件B的onTouch回调，不会触发组件C的onTouch回调。

当触摸组件C时，会触发组件A和组件C的onTouch回调，不触发组件B的回调。

特殊的容器组件，如Stack等组件，由于子组件之间存在着堆叠关系，子组件的布局也存在相互遮盖关系。

所以，父子组件之间onTouch事件能够同时触发，兄弟组件之间onTouch事件会存在遮盖关系。

```
1. Stack() {
2. Column().id('ComponentB').onTouch(() => {})
3. Column().id('ComponentC').onTouch(() => {})
4. }.id('Stack A').onTouch(() => {})
```

[TouchEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultilevelGestureEvents/entry/src/main/ets/pages/TouchEvent.ets#L27-L32)

组件B和组件C作为Stack A的子组件，组件C覆盖在组件B上。当触摸到组件B或者组件C时，Stack A也会被触摸到。onTouch事件允许多个组件同时触发，因此，当触摸组件B和组件C的重叠区域时，会触发Stack A和组件C的onTouch回调，不会触发组件B的onTouch回调（组件B被组件C遮盖）。

### 手势与事件

除了触摸事件（onTouch事件）外的所有手势与事件，均是通过基础手势或者组合手势实现的。例如，拖拽事件是由长按手势和滑动手势组成的一个顺序手势。

在未显式声明的情况下，同一时间，一根手指对应的手势组中只会有一个手势获得成功从而触发所设置的回调。

因此，除非显式声明允许多个手势同时成功，同一时间只会有一个手势响应。

响应优先级遵循以下条件：

1.当父子组件均绑定同一类手势时，子组件优先于父组件触发。

2.当一个组件绑定多个手势时，先达到手势触发条件的手势优先触发。

```
1. Column() {
2. Column().id('ComponentB').gesture(TapGesture({ count: 1 }))
3. }.id('ComponentA').gesture(TapGesture({ count: 1 }))
```

[GesturesEvents.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultilevelGestureEvents/entry/src/main/ets/pages/GesturesEvents.ets#L20-L24)

当父组件和子组件均绑定点击手势时，子组件的优先级高于父组件。

因此，当在B组件上进行点击时，组件B所绑定的TapGesture的回调会被触发，而组件A所绑定的TapGesture的回调不会被触发。

```
1. Column()
2. .id('ComponentA')
3. .gesture(
4. GestureGroup(
5. GestureMode.Exclusive,
6. TapGesture({count: 1}),
7. PanGesture({distance: 5})
8. )
9. )
```

[GesturesEvents.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultilevelGestureEvents/entry/src/main/ets/pages/GesturesEvents.ets#L26-L36)

当组件A上绑定了由点击和滑动手势组成的互斥手势组时，先达到触发条件的手势触发对应的回调。

若使用者做了一次点击操作，则响应点击对应的回调。若使用者进行了一次滑动操作并且滑动距离达到了阈值，则响应滑动对应的回调。

## 自定义控制的多层级手势事件

可以通过设置属性，控制默认的多层级手势事件竞争流程，更好地实现手势事件。

目前，通过设置[触摸热区](../harmonyos-references/ts-universal-attributes-touch-target.md)和[触摸测试](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)可以控制Touch事件的分发，从而可以影响到onTouch事件和手势的响应。而绑定手势方法属性可以控制手势的竞争从而影响手势的响应，但不能影响到onTouch事件。

### 触摸热区对手势和事件的控制

通过[responseRegion](../harmonyos-references/ts-universal-attributes-touch-target.md#responseregion)和[mouseResponseRegion](../harmonyos-references/ts-universal-attributes-touch-target.md#mouseresponseregion10)属性可以设置组件的触摸热区。从API version 22开始，支持通过[responseRegionList](../harmonyos-references/ts-universal-attributes-touch-target.md#responseregionlist22)设置组件的触摸热区。触摸热区范围可以超出或者小于组件的布局范围。

```
1. Column() {
2. Column()
3. .id('ComponentB')
4. .onTouch(() => {})
5. .gesture(TapGesture({count: 1}))
6. .responseRegion([rect1, rect2, rect3])
7. }
8. .id('ComponentA')
9. .onTouch(() => {})
10. .gesture(TapGesture({count: 1}))
11. .responseRegion([rect4])
```

[CustomEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultilevelGestureEvents/entry/src/main/ets/pages/CustomEvent.ets#L37-L49)

当组件A绑定了.responseRegion({Rect4})的属性后，所有落在Rect4区域范围的触摸事件和手势可被组件A对应的回调响应。

当组件B绑定了.responseRegion({Rect1, Rect2, Rect3})的属性后，所有落在Rect1,Rect2和Rect3区域范围的触摸事件和手势可被组件B对应的回调响应。

当绑定了responseRegion后，手势与事件的响应区域范围将以所绑定的区域范围为准，而不是以布局区域为准，可能出现布局相关区域不响应手势与事件的情况。

此外，responseRegion属性支持由多个Rect组成的数组作为入参，以支持更多开发需求。

### 触摸测试对手势和事件的控制

[hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)属性可以实现在复杂的多层级场景下，一些组件能够响应手势和事件，而一些组件不能响应手势和事件。

```
1. Column() {
2. Column()
3. .id('ComponentB')
4. .onTouch(() => {})
5. .gesture(TapGesture({count: 1}))

7. Column() {
8. Column()
9. .id('ComponentD')
10. .onTouch(() => {})
11. .gesture(TapGesture({count: 1}))
12. }
13. .id('ComponentC')
14. .onTouch(() => {})
15. .gesture(TapGesture({count: 1}))
16. .hitTestBehavior(HitTestMode.Block)
17. }
18. .id('ComponentA')
19. .onTouch(() => {})
20. .gesture(TapGesture({count: 1}))
```

[CustomEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultilevelGestureEvents/entry/src/main/ets/pages/CustomEvent.ets#L51-L72)

HitTestMode.Block自身会响应触摸测试，阻塞子节点和兄弟节点的触摸测试，从而导致子节点和兄弟节点的onTouch事件和手势均无法触发。

当组件C未设置hitTestBehavior时，点击组件D区域，组件A、组件C和组件D的onTouch事件会触发，组件D的点击手势会触发。

当组件C设置了hitTestBehavior为HitTestMode.Block时，点击组件D区域，组件A和组件C的onTouch事件会触发，组件D的onTouch事件未触发。同时，由于组件D的点击手势因为被阻塞而无法触发，组件C的点击手势会触发。

```
1. Stack() {
2. Column()
3. .id('ComponentB')
4. .onTouch(() => {})
5. .gesture(TapGesture({count: 1}))

7. Column()
8. .id('ComponentC')
9. .onTouch(() => {})
10. .gesture(TapGesture({count: 1}))
11. .hitTestBehavior(HitTestMode.Transparent)
12. }
13. .id('Stack A')
14. .onTouch(() => {})
15. .gesture(TapGesture({count: 1}))
```

[CustomEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultilevelGestureEvents/entry/src/main/ets/pages/CustomEvent.ets#L74-L90)

HitTestMode.Transparent自身响应触摸测试，不会阻塞兄弟节点的触摸测试。

当组件C未设置hitTestBehavior时，点击组件B和组件C的重叠区域时，Stack A和组件C的onTouch事件会触发，组件C的点击事件会触发，组件B的onTouch事件和点击手势均不触发。

而当组件C设置hitTestBehavior为HitTestMode.Transparent时，点击组件B和组件C的重叠区域，组件A和组件C不受到影响与之前一致，组件A和组件C的onTouch事件会触发，组件C的点击手势会触发。而组件B因为组件C设置了HitTestMode.Transparent，组件B也收到了Touch事件，从而组件B的onTouch事件触发。

```
1. Column() {
2. Column()
3. .id('ComponentB')
4. .onTouch(() => {})
5. .gesture(TapGesture({count: 1}))
6. }
7. .id('ComponentA')
8. .onTouch(() => {})
9. .gesture(TapGesture({count: 1}))
10. .hitTestBehavior(HitTestMode.None)
```

[CustomEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultilevelGestureEvents/entry/src/main/ets/pages/CustomEvent.ets#L92-L103)

HitTestMode.None自身不响应触摸测试，不会阻塞子节点和兄弟节点的触摸控制。

当组件A未设置hitTestBehavior时，点击组件B区域时，组件A和组件B的onTouch事件均会触发，组件B的点击手势会触发。

当组件A设置hitTestBehavior为HitTestMode.None时，点击组件B区域时，组件B的onTouch事件触发，而组件A的onTouch事件无法触发，组件B的点击手势触发。

```
1. Stack() {
2. Column()
3. .id('ComponentB')
4. .onTouch(() => {})
5. .gesture(TapGesture({count: 1}))
6. Column() {
7. Column()
8. .id('ComponentD')
9. .onTouch(() => {})
10. .gesture(TapGesture({count: 1}))
11. }
12. .id('ComponentC')
13. .onTouch(() => {})
14. .gesture(TapGesture({count: 1}))
15. .hitTestBehavior(HitTestMode.BLOCK_HIERARCHY)
16. }
17. .id('Stack A')
18. .onTouch(() => {})
19. .gesture(TapGesture({count: 1}))
```

[CustomEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultilevelGestureEvents/entry/src/main/ets/pages/CustomEvent.ets#L105-L125)

从API version 20开始，HitTestMode.BLOCK\_HIERARCHY自身和子节点响应触摸测试，阻止所有优先级较低的兄弟节点和父节点参与触摸测试。

当组件C未设置hitTestBehavior时，点击组件B和组件D的重叠区域时，组件A，组件C和组件D的onTouch事件均会触发，组件D的点击手势会触发。

当组件C设置hitTestBehavior为HitTestMode.BLOCK\_HIERARCHY时，点击组件B和组件D的重叠区域时，组件C和组件D的onTouch事件触发，组件A和组件B的onTouch事件无法触发，组件D的点击手势会触发。

```
1. Stack() {
2. Column()
3. .id('ComponentB')
4. .onTouch(() => {})
5. .gesture(TapGesture({count: 1}))
6. Column() {
7. Column()
8. .id('ComponentD')
9. .onTouch(() => {})
10. .gesture(TapGesture({count: 1}))
11. }
12. .id('ComponentC')
13. .onTouch(() => {})
14. .gesture(TapGesture({count: 1}))
15. .hitTestBehavior(HitTestMode.BLOCK_DESCENDANTS)
16. }
17. .id('Stack A')
18. .onTouch(() => {})
19. .gesture(TapGesture({count: 1}))
```

[CustomEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultilevelGestureEvents/entry/src/main/ets/pages/CustomEvent.ets#L127-L147)

从API version 20开始，[HitTestMode](../harmonyos-references/ts-appendix-enums.md#hittestmode9).BLOCK\_DESCENDANTS自身不响应触摸测试，并且所有的后代（孩子，孙子等）也不响应触摸测试，不会影响祖先节点的触摸测试。

若组件C未设置[hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)，点击组件B和组件D的重叠区域时，组件A、组件C和组件D都会触发[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)事件，同时组件D的点击手势也会被触发。

当组件C设置[hitTestBehavior](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md#hittestbehavior)为HitTestMode.BLOCK\_DESCENDANTS时，点击组件B和组件D的重叠区域时，组件A和组件B的[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)事件触发，组件C和组件D的[onTouch](../harmonyos-references/ts-universal-events-touch.md#ontouch)事件无法触发，组件B的点击手势会触发。

针对简单的场景，建议在单个组件上绑定hitTestBehavior。

针对复杂场景，建议在多个组件上绑定不同的hitTestBehavior来控制Touch事件的分发。

### 绑定手势方法对手势的控制

设置绑定手势的方法可以实现在多层级场景下，当父组件与子组件绑定了相同的手势时，设置不同的绑定手势方法有不同的响应优先级。

当父组件使用.[gesture](../harmonyos-references/ts-gesture-settings.md#gesture)绑定手势，父子组件所绑定手势类型相同时，子组件优先于父组件响应。

```
1. Column() {
2. Column()
3. .id('ComponentB')
4. .gesture(TapGesture({count: 1}))
5. }
6. .id('ComponentA')
7. .gesture(TapGesture({count: 1}))
```

[CustomEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultilevelGestureEvents/entry/src/main/ets/pages/CustomEvent.ets#L149-L157)

当父子组件均正常绑定点击手势时，子组件优先于父组件响应。

此时，单击组件B区域范围，组件B的点击手势会触发，组件A的点击手势不会触发。

如果以带优先级的方式绑定手势，则可使得父组件所绑定手势的响应优先级高于子组件。

```
1. Column() {
2. Column()
3. .id('ComponentB')
4. .gesture(TapGesture({count: 1}))
5. }
6. .id('ComponentA')
7. .priorityGesture(TapGesture({count: 1}))
```

[CustomEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultilevelGestureEvents/entry/src/main/ets/pages/CustomEvent.ets#L159-L167)

当父组件以.[priorityGesture](../harmonyos-references/ts-gesture-settings.md#prioritygesture)的形式绑定手势时，父组件所绑定的手势优先级高于子组件。

此时，单击组件B区域范围，组件A的点击手势会触发，组件B的点击手势不会触发。

如果需要父子组件所绑定的手势不发生冲突，均可响应，则可以使用并行的方式在父组件绑定手势。

```
1. Column() {
2. Column()
3. .id('ComponentB')
4. .gesture(TapGesture({count: 1}))
5. }
6. .id('ComponentA')
7. .parallelGesture(TapGesture({count: 1}))
```

[CustomEvent.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultilevelGestureEvents/entry/src/main/ets/pages/CustomEvent.ets#L169-L177)

当父组件以.[parallelGesture](../harmonyos-references/ts-gesture-settings.md#parallelgesture)的形式绑定手势时，父组件和子组件所绑定的手势均可触发。

此时，单击组件B区域范围，组件A和组件B的点击手势均会触发。

### OverlayManager的事件透传

[OverlayManager](../harmonyos-references/arkts-apis-uicontext-overlaymanager.md)事件机制，默认优先被[WrappedBuilder](../harmonyos-references/ts-universal-wrapbuilder.md#wrappedbuilder)内组件先接收，不会向下传递。

若希望OverlayManager下方的页面也能感应到事件，可采用hitTestBehavior(HitTestMode.Transparent)来传递事件，参考以下伪代码。

```
1. @Builder
2. function builderOverlay(params: Params) {
3. Component1().hitTestBehavior(HitTestMode.Transparent)
4. }

6. // ···

8. aboutToAppear(): void {
9. // ···
10. let componentContent = new ComponentContent(
11. this.context, wrapBuilder<[Params]>(builderOverlay),
12. new Params(uiContext, {x:0, y: 100})
13. );
14. this.overlayManager.addComponentContent(componentContent, 0);
15. }
```

[OverlayManager.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/MultilevelGestureEvents/entry/src/main/ets/pages/OverlayManager.ets#L30-L54)
