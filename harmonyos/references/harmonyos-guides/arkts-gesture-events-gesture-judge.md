---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-gesture-events-gesture-judge
title: 手势冲突处理
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 添加手势响应 > 手势冲突处理
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:57+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:daeaba1ef199b5d49f11ee92aab22fcc6b85ed32fd39a774a590084b4bb0aa5d
---

手势冲突是指多个手势识别器在同一组件或重叠区域同时识别时产生竞争，导致识别结果不符合预期。常见冲突场景包括：

* 同一组件上的多手势（如按钮同时添加点击与长按手势）。
* 父子组件的同类型手势识别器。
* 系统默认手势与自定义手势（如[Scroll](../harmonyos-references/ts-container-scroll.md)滑动手势与子组件点击手势冲突）。

干预手势处理可有效解决冲突，除控制组件响应热区和命中测试模式外，主要通过以下三种方式：[自定义手势判定](arkts-gesture-events-gesture-judge.md#自定义手势判定)、[手势并行动态控制](arkts-gesture-events-gesture-judge.md#手势并行动态控制)、[阻止手势参与识别](arkts-gesture-events-gesture-judge.md#阻止手势参与识别)。

## 自定义手势判定

自定义手势判定是指在系统判定阈值已满足的条件下，应用可自行判断是否应拦截该手势，使该手势识别失败，从而将识别成功的机会留给其他手势。

**图1** 自定义手势判定流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/jza11yrIQz2H7khvqc1qpg/zh-cn_image_0000002583438007.png?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=ED23D5FBAA4384A5E68ECAD71E46A124CA810194987C34DC0CDFA974CCA291E3)

自定义手势判定涉及以下接口。

| **接口** | **说明** |
| --- | --- |
| [onGestureJudgeBegin](../harmonyos-references/ts-gesture-customize-judge.md#ongesturejudgebegin) | 用于手势拦截，是通用事件。在手势满足系统触发阈值场景下，回调给应用判断是否拦截手势。 |
| [onGestureRecognizerJudgeBegin](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin) | 用于手势拦截、获取手势识别器和设置手势识别器开闭状态。是onGestureJudgeBegin接口的能力扩展，可以代替onGestureJudgeBegin接口。  获取手势识别器时，会获取一次交互中手势响应链上的所有手势识别器，以及当前即将触发成功的手势识别器，此时可以设置手势的激活状态。 |

以下示例中，Image和Stack两个组件位于同一区域。长按Stack组件的上半部分可触发挂载在Stack组件上的长按手势，长按Stack组件的下半部分则会响应Image组件的拖拽操作。

**图2** 示例图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/BwNJ2M4sQBSd3qLLNxXxFg/zh-cn_image_0000002552957962.png?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=138EFAF8A61AAC4260500EDDD326F4312759F022559C6953D8EA52DD8296C28A)

1. Image组件设置拖拽。

   ```
   1. // $r('sys.media.ohos_app_icon') 需要替换为开发者所需的资源文件
   2. Image($r('sys.media.ohos_app_icon'))
   3. .draggable(true)
   4. .onDragStart(()=>{
   5. // ...
   6. // 请将$r('app.string.Allow_dragging_prompt')替换为实际资源文件，在本示例中该资源文件的value值为"Drag 下半区蓝色区域，Image响应"
   7. promptAction.showToast({ message: $r('app.string.Allow_dragging_prompt') });
   8. })
   9. .width('200vp').height('200vp')
   ```

   [CustomGestures.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureConflict/entry/src/main/ets/Component/CustomGestures/CustomGestures.ets#L34-L46)
2. Stack组件设置手势。

   ```
   1. Stack() {}
   2. .width('200vp')
   3. .height('200vp')
   4. .hitTestBehavior(HitTestMode.Transparent)
   5. .gesture(GestureGroup(GestureMode.Parallel,
   6. LongPressGesture()
   7. .onAction((event: GestureEvent) => {
   8. // ...
   9. /*
   10. 请将$r('app.string.Stop_dragging_prompt')替换为实际资源文件，在本示例中
   11. 该资源文件的value值为"LongPressGesture 长按上半区 红色区域，红色区域响应"
   12. */
   13. promptAction.showToast({ message: $r('app.string.Stop_dragging_prompt')  });
   14. })
   15. .tag('longpress')
   16. ))
   ```

   [CustomGestures.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureConflict/entry/src/main/ets/Component/CustomGestures/CustomGestures.ets#L50-L67)
3. Stack组件设置拦截。

   ```
   1. .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
   2. // 如果是长按类型手势，判断点击的位置是否在上半区
   3. if (gestureInfo.type == GestureControl.GestureType.LONG_PRESS_GESTURE) {
   4. if (event.fingerList.length > 0 && event.fingerList[0].localY < 100) {
   5. return GestureJudgeResult.CONTINUE;
   6. } else {
   7. return GestureJudgeResult.REJECT;
   8. }
   9. };
   10. return GestureJudgeResult.CONTINUE;
   11. })
   ```

   [CustomGestures.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureConflict/entry/src/main/ets/Component/CustomGestures/CustomGestures.ets#L69-L81)
4. 代码完整示例。

   ```
   1. import { PromptAction } from '@kit.ArkUI';

   3. @Entry
   4. @Component
   5. struct Index {
   6. scroller: Scroller = new Scroller();
   7. promptAction: PromptAction = this.getUIContext().getPromptAction();

   9. build() {
   10. Scroll(this.scroller) {
   11. Column({ space: 8 }) {
   12. /*
   13. 请将$r('app.string.Drag_instructions')替换为实际资源文件，在本示例中该资源文件的value值为"包括上下两层组件，上层组件绑定长按手势，
   14. 下层组件绑定拖拽。其中上层组件下半区域绑定手势拦截，使该区域响应下层拖拽手势。"
   15. */
   16. Text($r('app.string.Drag_instructions')).width('100%').fontSize(20).fontColor('0xffdd00')
   17. Stack({ alignContent: Alignment.Center }) {
   18. Column() {
   19. // 模拟上半区和下半区
   20. Stack().width('200vp').height('100vp').backgroundColor(Color.Gray)
   21. Stack().width('200vp').height('100vp').backgroundColor(Color.Blue)
   22. }.width('200vp').height('200vp')

   24. // Stack的下半区是绑定了滑动手势的图像区域。
   25. // $r('sys.media.ohos_app_icon') 需要替换为开发者所需的资源文件
   26. Image($r('sys.media.ohos_app_icon'))
   27. .draggable(true)
   28. .onDragStart(() => {
   29. // 请将$r('app.string.Allow_dragging_prompt')替换为实际资源文件，在本示例中该资源文件的value值为"Drag 下半区蓝色区域，Image响应"
   30. this.promptAction.showToast({ message: $r('app.string.Allow_dragging_prompt') });
   31. })
   32. .width('200vp').height('200vp')
   33. // Stack的上半区是绑定了长按手势的浮动区域。
   34. Stack() {
   35. }
   36. .width('200vp')
   37. .height('200vp')
   38. .hitTestBehavior(HitTestMode.Transparent)
   39. .gesture(GestureGroup(GestureMode.Parallel,
   40. LongPressGesture()
   41. .onAction((event: GestureEvent) => {
   42. /*
   43. 请将$r('app.string.Stop_dragging_prompt')替换为实际资源文件，在本示例中
   44. 该资源文件的value值为"LongPressGesture 长按上半区 红色区域，红色区域响应"
   45. */
   46. this.promptAction.showToast({ message: $r('app.string.Stop_dragging_prompt') });
   47. })
   48. .tag('longpress')
   49. ))
   50. .onGestureJudgeBegin((gestureInfo: GestureInfo, event: BaseGestureEvent) => {
   51. // 如果是长按类型手势，判断点击的位置是否在上半区
   52. if (gestureInfo.type == GestureControl.GestureType.LONG_PRESS_GESTURE) {
   53. if (event.fingerList.length > 0 && event.fingerList[0].localY < 100) {
   54. return GestureJudgeResult.CONTINUE;
   55. } else {
   56. return GestureJudgeResult.REJECT;
   57. }
   58. };
   59. return GestureJudgeResult.CONTINUE;
   60. })
   61. }.width('100%')
   62. }.width('100%')
   63. }
   64. }
   65. }
   ```

   [CustomGestureDetermination.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureConflict/entry/src/main/ets/Component/CustomGestures/CustomGestureDetermination.ets#L15-L78)

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/YUwXaNIqQOiHae2yEPhBTg/zh-cn_image_0000002583477963.png?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=35B208501737770529C90739AD49F2C8D9602F2ECD77C18059F4AA1B71CA2E52)

## 手势并行动态控制

手势并行动态控制指的是手势已经成功识别，但是开发者仍然可以通过调用API接口控制手势回调是否能够响应。

**图3** 手势并行动态控制流程图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/LCDSaKtKQduMG8_swNCLWA/zh-cn_image_0000002552798314.png?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=D6E908EBBD3CB19B804B2E0BF95F0652F72000B3C8729193620B0FDBAA42B523)

手势并行动态控制的前提是手势识别成功，如果手势不成功则不会产生手势回调响应。

1. 业务手势作业流：指真正触发UI变化的业务手势，比如使页面滚动的PanGesture，触发点击的TapGesture等。
2. 监听手势作业流：指在监听手势运行的过程中，应根据上下文的业务状态变化动态控制手势识别器的开闭，例如判断组件嵌套滚动过程中是否已滑至边缘。这一监听事件可借助一个使用[并行手势绑定方式](arkts-gesture-events-binding.md#parallelgesture并行手势绑定方法)的PanGesture实现，或者采用Touch事件来完成。
3. 设置手势并行：此步骤并非必需，典型场景是在嵌套滚动中，设置外部组件的滚动手势与内部的滚动手势并行。
4. 动态开闭手势：指通过手势识别器的setEnabled方法，控制手势是否响应用户回调。

手势并行动态控制涉及以下接口。

| **接口** | **说明** |
| --- | --- |
| [shouldBuiltInRecognizerParallelWith](../harmonyos-references/ts-gesture-blocking-enhancement.md#shouldbuiltinrecognizerparallelwith) | 用于设置系统组件内置手势与其他手势并行。 |
| [onGestureRecognizerJudgeBegin](../harmonyos-references/ts-gesture-blocking-enhancement.md#ongesturerecognizerjudgebegin) | 用于手势拦截，获取手势识别器，初始化手势识别器开闭状态。 |
| [parallelGesture](arkts-gesture-events-binding.md#parallelgesture并行手势绑定方法) | 可使开发者定义的手势，与比他优先级高的手势并行。 |

以下示例是两个Scroll组件的嵌套滚动场景，使用手势控制的api去控制外部组件和内部组件的嵌套滚动联动。

1. 使用shouldBuiltInRecognizerParallelWith接口设置外部Scroll组件的PanGesture手势与内部Scroll组件的PanGesture手势并行。

   ```
   1. .shouldBuiltInRecognizerParallelWith((current: GestureRecognizer, others: Array<GestureRecognizer>) => {
   2. for (let i = 0; i < others.length; i++) {
   3. let target = others[i].getEventTargetInfo();
   4. if (target.getId() == 'inner' && others[i].isBuiltIn() && others[i].getType() == GestureControl.GestureType.PAN_GESTURE) { // 找到将要组成并行手势的识别器
   5. this.currentRecognizer = current; // 保存当前组件的识别器
   6. this.childRecognizer = others[i]; // 保存将要组成并行手势的识别器
   7. return others[i]; // 返回和当前手势将要组成并行手势的识别器
   8. };
   9. };
   10. return undefined;
   11. })
   ```

   [GestureControl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureConflict/entry/src/main/ets/Component/GestureAndMotionControl/GestureControl.ets#L75-L87)
2. 使用onGestureRecognizerJudgeBegin接口获取到Scroll组件的PanGesture手势识别器，同时根据内外Scroll组件的边界条件，设置内外手势的开闭状态。

   ```
   1. .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
   2. others: Array<GestureRecognizer>) => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
   3. let target = current.getEventTargetInfo();
   4. if (target && target.getId() == 'outer' && current.isBuiltIn() && current.getType() == GestureControl.GestureType.PAN_GESTURE) {
   5. for (let i = 0; i < others.length; i++) {
   6. let target = others[i].getEventTargetInfo() as ScrollableTargetInfo;
   7. if (target instanceof ScrollableTargetInfo && target.getId() == 'inner') { // 找到响应链上对应并行的识别器
   8. let panEvent = event as PanGestureEvent;
   9. this.childRecognizer.setEnabled(true);
   10. this.currentRecognizer.setEnabled(false);
   11. if (target.isEnd()) { // 根据当前组件状态以及移动方向动态控制识别器使能状态
   12. if (panEvent && panEvent.offsetY < 0) {
   13. this.childRecognizer.setEnabled(false);
   14. this.currentRecognizer.setEnabled(true);
   15. };
   16. } else if (target.isBegin()) {
   17. if (panEvent.offsetY > 0) {
   18. this.childRecognizer.setEnabled(false);
   19. this.currentRecognizer.setEnabled(true);
   20. };
   21. };
   22. };
   23. };
   24. };
   25. return GestureJudgeResult.CONTINUE;
   26. })
   ```

   [GestureControl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureConflict/entry/src/main/ets/Component/GestureAndMotionControl/GestureControl.ets#L90-L117)
3. 设置监听手势，监听Scroll组件状态，动态调整手势开闭状态，控制手势回调是否触发，从而控制Scroll是否滚动。

   ```
   1. .parallelGesture( // 绑定一个Pan手势作为动态控制器
   2. PanGesture()
   3. .onActionUpdate((event: GestureEvent)=>{
   4. if (this.childRecognizer.getState() != GestureRecognizerState.SUCCESSFUL ||
   5. this.currentRecognizer.getState() != GestureRecognizerState.SUCCESSFUL) { // 如果识别器状态不是SUCCESSFUL，则不做控制
   6. return;
   7. };
   8. let target = this.childRecognizer.getEventTargetInfo() as ScrollableTargetInfo;
   9. let currentTarget = this.currentRecognizer.getEventTargetInfo() as ScrollableTargetInfo;
   10. if (target instanceof ScrollableTargetInfo && currentTarget instanceof ScrollableTargetInfo) {
   11. this.childRecognizer.setEnabled(true);
   12. this.currentRecognizer.setEnabled(false);
   13. if (target.isEnd()) { // 在移动过程中实时根据当前组件状态，控制识别器的开闭状态
   14. if ((event.offsetY - this.lastOffset) < 0) {
   15. this.childRecognizer.setEnabled(false);
   16. if (currentTarget.isEnd()) {
   17. this.currentRecognizer.setEnabled(false);
   18. } else {
   19. this.currentRecognizer.setEnabled(true);
   20. };
   21. };
   22. } else if (target.isBegin()) {
   23. if ((event.offsetY - this.lastOffset) > 0) {
   24. this.childRecognizer.setEnabled(false);
   25. if (currentTarget.isBegin()) {
   26. this.currentRecognizer.setEnabled(false);
   27. } else {
   28. this.currentRecognizer.setEnabled(true);
   29. };
   30. };
   31. };
   32. };
   33. this.lastOffset = event.offsetY;
   34. })
   35. )
   ```

   [GestureControl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureConflict/entry/src/main/ets/Component/GestureAndMotionControl/GestureControl.ets#L119-L155)
4. 代码完整示例。

   ```
   1. // xxx.ets
   2. @Entry
   3. @Component
   4. struct FatherControlChild {
   5. scroller: Scroller = new Scroller();
   6. scroller2: Scroller = new Scroller();
   7. private arr: number[] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
   8. private childRecognizer: GestureRecognizer = new GestureRecognizer();
   9. private currentRecognizer: GestureRecognizer = new GestureRecognizer();
   10. private lastOffset: number = 0;

   12. build() {
   13. Stack({ alignContent: Alignment.TopStart }) {
   14. Scroll(this.scroller) { // 外部滚动容器
   15. Column() {
   16. Text('Scroll Area')
   17. .width('90%')
   18. .height(150)
   19. .backgroundColor(0xFFFFFF)
   20. .borderRadius(15)
   21. .fontSize(16)
   22. .textAlign(TextAlign.Center)
   23. .margin({ top: 10 })
   24. Scroll(this.scroller2) { // 内部滚动容器
   25. Column() {
   26. Text('Scroll Area2')
   27. .width('90%')
   28. .height(150)
   29. .backgroundColor(0xFFFFFF)
   30. .borderRadius(15)
   31. .fontSize(16)
   32. .textAlign(TextAlign.Center)
   33. .margin({ top: 10 })
   34. Column() {
   35. ForEach(this.arr, (item: number) => {
   36. Text(item.toString())
   37. .width('90%')
   38. .height(150)
   39. .backgroundColor(0xFFFFFF)
   40. .borderRadius(15)
   41. .fontSize(16)
   42. .textAlign(TextAlign.Center)
   43. .margin({ top: 10 })
   44. }, (item: string) => item)
   45. }.width('100%')
   46. }
   47. }
   48. .id('inner')
   49. .width('100%')
   50. .height(800)
   51. }.width('100%')
   52. }
   53. .id('outer')
   54. .height(600)
   55. .scrollable(ScrollDirection.Vertical) // 滚动方向纵向
   56. .scrollBar(BarState.On) // 滚动条常驻显示
   57. .scrollBarColor(Color.Gray) // 滚动条颜色
   58. .scrollBarWidth(10) // 滚动条宽度
   59. .edgeEffect(EdgeEffect.None)
   60. .shouldBuiltInRecognizerParallelWith((current: GestureRecognizer, others: Array<GestureRecognizer>) => {
   61. for (let i = 0; i < others.length; i++) {
   62. let target = others[i].getEventTargetInfo();
   63. if (target.getId() == 'inner' && others[i].isBuiltIn() &&
   64. others[i].getType() == GestureControl.GestureType.PAN_GESTURE) { // 找到将要组成并行手势的识别器
   65. this.currentRecognizer = current; // 保存当前组件的识别器
   66. this.childRecognizer = others[i]; // 保存将要组成并行手势的识别器
   67. return others[i]; // 返回和当前手势将要组成并行手势的识别器
   68. }
   69. }
   70. return undefined;
   71. })
   72. .onGestureRecognizerJudgeBegin((event: BaseGestureEvent, current: GestureRecognizer,
   73. others: Array<GestureRecognizer>) => { // 在识别器即将要成功时，根据当前组件状态，设置识别器使能状态
   74. let target = current.getEventTargetInfo();
   75. if (target && target.getId() == 'outer' && current.isBuiltIn() &&
   76. current.getType() == GestureControl.GestureType.PAN_GESTURE) {
   77. for (let i = 0; i < others.length; i++) {
   78. let target = others[i].getEventTargetInfo() as ScrollableTargetInfo;
   79. if (target instanceof ScrollableTargetInfo && target.getId() == 'inner') { // 找到响应链上对应并行的识别器
   80. let panEvent = event as PanGestureEvent;
   81. this.childRecognizer.setEnabled(true);
   82. this.currentRecognizer.setEnabled(false);
   83. if (target.isEnd()) { // 根据当前组件状态以及移动方向动态控制识别器使能状态
   84. if (panEvent && panEvent.offsetY < 0) {
   85. this.childRecognizer.setEnabled(false);
   86. this.currentRecognizer.setEnabled(true);
   87. }
   88. } else if (target.isBegin()) {
   89. if (panEvent.offsetY > 0) {
   90. this.childRecognizer.setEnabled(false);
   91. this.currentRecognizer.setEnabled(true);
   92. }
   93. }
   94. }
   95. }
   96. }
   97. return GestureJudgeResult.CONTINUE;
   98. })
   99. .parallelGesture( // 绑定一个Pan手势作为动态控制器
   100. PanGesture()
   101. .onActionUpdate((event: GestureEvent) => {
   102. if (this.childRecognizer?.getState() != GestureRecognizerState.SUCCESSFUL ||
   103. this.currentRecognizer?.getState() != GestureRecognizerState.SUCCESSFUL) { // 如果识别器状态不是SUCCESSFUL，则不做控制
   104. return;
   105. }
   106. let target = this.childRecognizer.getEventTargetInfo() as ScrollableTargetInfo;
   107. let currentTarget = this.currentRecognizer.getEventTargetInfo() as ScrollableTargetInfo;
   108. if (target instanceof ScrollableTargetInfo && currentTarget instanceof ScrollableTargetInfo) {
   109. this.childRecognizer.setEnabled(true);
   110. this.currentRecognizer.setEnabled(false);
   111. if (target.isEnd()) { // 在移动过程中实时根据当前组件状态，控制识别器的开闭状态
   112. if ((event.offsetY - this.lastOffset) < 0) {
   113. this.childRecognizer.setEnabled(false);
   114. if (currentTarget.isEnd()) {
   115. this.currentRecognizer.setEnabled(false);
   116. } else {
   117. this.currentRecognizer.setEnabled(true);
   118. };
   119. };
   120. } else if (target.isBegin()) {
   121. if ((event.offsetY - this.lastOffset) > 0) {
   122. this.childRecognizer.setEnabled(false)
   123. if (currentTarget.isBegin()) {
   124. this.currentRecognizer.setEnabled(false);
   125. } else {
   126. this.currentRecognizer.setEnabled(true);
   127. };
   128. };
   129. };
   130. };
   131. this.lastOffset = event.offsetY;
   132. })
   133. )
   134. }.width('100%').height('100%').backgroundColor(0xDCDCDC)
   135. }
   136. }
   ```

   [GestureAndMotionControl.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureConflict/entry/src/main/ets/Component/GestureAndMotionControl/GestureAndMotionControl.ets#L16-L153)

## 阻止手势参与识别

手势识别基于[触摸测试](arkts-interaction-basic-principles.md#触摸测试)的响应链结果进行，因此在用户按下时，通过控制响应链中手势识别器的参与状态，实现高效的动态干预手势处理。

从API version 20开始，可以结合[onTouchTestDone](../harmonyos-references/ts-gesture-blocking-enhancement.md#ontouchtestdone20)接口来阻止手势参与识别。完成触摸测试后，系统通过该接口回调返回所有手势识别器对象。应用可根据类型、组件标识或关联组件信息筛选识别器，并通过调用[preventBegin](../harmonyos-references/ts-gesture-common.md#preventbegin20)接口主动禁用特定识别器。

根据手势类型进行禁用：

```
1. .onTouchTestDone((event, recognizers) => {
2. for (let i = 0; i < recognizers.length; i++) {
3. let recognizer = recognizers[i];
4. // 根据类型禁用所有滑动手势
5. if (recognizer.getType() == GestureControl.GestureType.PAN_GESTURE) {
6. recognizer.preventBegin();
7. };
8. };
9. })
```

[PreventIdentification.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureConflict/entry/src/main/ets/Component/PreventGestureRecognition/PreventIdentification.ets#L182-L192)

根据手势所归属的组件禁用：

组件需要提前通过通用属性[id](../harmonyos-references/ts-universal-attributes-component-id.md#id)配置组件标识。

```
1. .onTouchTestDone((event, recognizers) => {
2. for (let i = 0; i < recognizers.length; i++) {
3. let recognizer = recognizers[i];
4. // 禁用掉标识为myID的组件上的所有手势
5. if (recognizer.getEventTargetInfo().getId() == 'myID') {
6. recognizer.preventBegin();
7. };
8. };
9. })
```

[PreventIdentification.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureConflict/entry/src/main/ets/Component/PreventGestureRecognition/PreventIdentification.ets#L194-L204)

根据是否系统内置手势禁用：

```
1. .onTouchTestDone((event, recognizers) => {
2. for (let i = 0; i < recognizers.length; i++) {
3. let recognizer = recognizers[i];
4. // 禁用掉所有系统内置的手势
5. if (recognizer.isBuiltIn()) {
6. recognizer.preventBegin();
7. };
8. };
9. })
```

[PreventIdentification.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureConflict/entry/src/main/ets/Component/PreventGestureRecognition/PreventIdentification.ets#L206-L216)

根据具体情况组合使用这些条件。

说明

系统由内向外执行节点上的onTouchTestDone回调。

在NDK中onTouchTestDone与preventBegin对应的接口分别为[OH\_ArkUI\_SetTouchTestDoneCallback](../harmonyos-references/capi-native-gesture-h.md#oh_arkui_settouchtestdonecallback)和[OH\_ArkUI\_PreventGestureRecognizerBegin](../harmonyos-references/capi-native-gesture-h.md#oh_arkui_preventgesturerecognizerbegin)，它们的使用方式及功能与ArkTS接口一致。

以下通过一个简化的视频播放界面交互为例来说明具体的用法：

父容器（video\_layer）绑定了多种手势：

* 点击：控制暂停/播放。
* 双击：切换全屏。
* 长按：快进。
* 上下滑动：调节亮度。
* 左右滑动：调整进度。

其内部下方的Slider组件（progress\_layer）未绑定长按手势，导致用户长按Slider时会触发父容器的快进手势，不符合预期。

解决方案：在Slider上注册onTouchTestDone回调，通过该回调禁用非Slider组件的手势识别器，即可解决冲突。

以下为完整示例代码：

```
1. @Entry
2. @ComponentV2
3. struct Index {
4. @Local progress: number = 496000; // 初始进度，秒
5. @Local total: number = 27490000; // 总时长，秒
6. @Local currentWidth: string = '100%';
7. @Local currentHeight: string = '100%';
8. private currentPosX: number = 0;
9. private currentPosY: number = 0;
10. private currentFullScreenState: boolean = true;
11. private normalPlayTimer: number = -1;
12. private isPlaying: boolean = true;
13. private fastForwardTimer: number = -1;
14. private context = this.getUIContext().getHostContext()

16. aboutToAppear(): void {
17. // 启动一个周期性定时器每隔一秒刷新一次进度
18. this.startNormalPlayTimer();
19. };

21. startNormalPlayTimer(): void {
22. if (this.normalPlayTimer != -1) {
23. this.stopNormalPlayTimer()
24. };
25. this.normalPlayTimer = setInterval(() => {
26. this.progress = this.progress + 1000
27. }, 1000);
28. };

30. stopNormalPlayTimer(): void {
31. if (this.normalPlayTimer == -1) {
32. return;
33. };
34. clearInterval(this.normalPlayTimer);
35. this.normalPlayTimer = -1;
36. };

38. startFastForwardTimer(): void {
39. if (this.fastForwardTimer != -1) {
40. this.stopFastForwardTimer();
41. };
42. this.fastForwardTimer = setInterval(() => {
43. this.progress = this.progress + 100000;
44. }, 100);
45. };

47. stopFastForwardTimer(): void {
48. if (this.fastForwardTimer == -1) {
49. return;
50. };
51. clearInterval(this.fastForwardTimer);
52. this.fastForwardTimer = -1;
53. };

55. showMessage(message: string): void {
56. this.getUIContext().getPromptAction().showToast({ message: message, alignment: Alignment.Center });
57. };

59. resetPosInfo(): void {
60. this.currentPosX = 0;
61. this.currentPosY = 0;
62. };

64. toggleFullScreenState(): void {
65. this.currentFullScreenState = !this.currentFullScreenState;
66. if (this.currentFullScreenState) {
67. this.currentWidth = '100%';
68. this.currentHeight = '100%';
69. } else {
70. this.currentWidth = '100%';
71. this.currentHeight = '50%';
72. };
73. // 请将$r('app.string.Play_full_screen')替换为实际资源文件，在本示例中该资源文件的value值为"全屏播放"
74. // 请将$r('app.string.Exit_play_full_screen')替换为实际资源文件，在本示例中该资源文件的value值为"取消全屏播放"
75. this.showMessage(this.currentFullScreenState
76. ? this.context!.resourceManager.getStringSync($r('app.string.Play_full_screen').id)
77. : this.context!.resourceManager.getStringSync($r('app.string.Exit_play_full_screen').id));
78. };

80. togglePlayAndPause(): void {
81. this.isPlaying = !this.isPlaying;
82. if (!this.isPlaying) {
83. this.stopNormalPlayTimer();
84. } else {
85. // 重新启动
86. this.startNormalPlayTimer();
87. };
88. // 请将$r('app.string.stop_playing')替换为实际资源文件，在本示例中该资源文件的value值为"暂停播放"
89. // 请将$r('app.string.Continue_playing')替换为实际资源文件，在本示例中该资源文件的value值为"继续播放"
90. this.showMessage(this.isPlaying
91. ? this.context!.resourceManager.getStringSync($r('app.string.stop_playing').id)
92. : this.context!.resourceManager.getStringSync($r('app.string.Continue_playing').id));
93. };

95. doFastForward(start: boolean): void {
96. if (!start) { // 停止快进，恢复正常播放
97. this.stopFastForwardTimer();
98. this.startNormalPlayTimer();
99. // 请将$r('app.string.Cancel_FastForwarding')替换为实际资源文件，在本示例中该资源文件的value值为"取消快进"
100. this.showMessage(
101. this.context!.resourceManager.getStringSync($r('app.string.Cancel_FastForwarding').id));
102. return;
103. };

105. this.stopNormalPlayTimer();
106. this.startFastForwardTimer();
107. // 请将$r('app.string.Start_FastForwarding')替换为实际资源文件，在本示例中该资源文件的value值为"开始快进"
108. this.showMessage(
109. this.context!.resourceManager.getStringSync($r('app.string.Start_FastForwarding').id));
110. };

112. updateBrightness(start: boolean, event: BaseGestureEvent): void {
113. let newY = event.fingerList[0].localY;
114. if (start) {
115. this.currentPosY = newY;
116. // 请将$r('app.string.Start_adjusting_brightness')替换为实际资源文件，在本示例中该资源文件的value值为"开始调整 亮度"
117. this.showMessage(this.context!.resourceManager
118. .getStringSync($r('app.string.Start_adjusting_brightness').id));
119. return;
120. };
121. let offsetY = newY - this.currentPosY;
122. if (Math.abs(offsetY) > 10) {
123. // 请将$r('app.string.Reduce_brightness')替换为实际资源文件，在本示例中该资源文件的value值为"降低亮度"
124. // 请将$r('app.string.Increase_brightness')替换为实际资源文件，在本示例中该资源文件的value值为"提高亮度"
125. this.showMessage((offsetY > 0)
126. ? this.context!.resourceManager.getStringSync($r('app.string.Reduce_brightness').id)
127. : this.context!.resourceManager.getStringSync($r('app.string.Increase_brightness').id))
128. this.currentPosY = newY;
129. };
130. };

132. updateProgress(start: boolean, event: BaseGestureEvent): void {
133. let newX = event.fingerList[0].localX;
134. if (start) {
135. this.currentPosX = newX;
136. // 请将$r('app.string.Adjust_schedule')替换为实际资源文件，在本示例中该资源文件的value值为"开始调整 进度"
137. this.showMessage(this.context!.resourceManager
138. .getStringSync($r('app.string.Adjust_schedule').id));
139. return;
140. };
141. let offsetX = newX - this.currentPosX;
142. this.progress = Math.floor(this.progress + offsetX * 10000);
143. this.currentPosX = newX;
144. };

146. build() {
147. Stack({ alignContent: Alignment.Center }) {
148. Column() {
149. Column() {
150. // 请将$r('app.string.Playback_progress')替换为实际资源文件，在本示例中该资源文件的value值为"播放进度"
151. Text(this.context!.resourceManager.getStringSync($r('app.string.Playback_progress').id) + this.progress)
152. }
153. .width('100%').height('90%')

155. Flex({ alignItems: ItemAlign.Center, justifyContent: FlexAlign.SpaceBetween }) {
156. Slider({
157. value: this.progress,
158. min: 0,
159. max: this.total,
160. style: SliderStyle.OutSet
161. })
162. .onChange((value: number, mode: SliderChangeMode) => {
163. this.progress = value;
164. })
165. .id('progress_layer')
166. .onTouchTestDone((event, allRecognizers: Array<GestureRecognizer>) => {
167. for (let i = 0; i < allRecognizers.length; i++) {
168. let recognizer = allRecognizers[i];
169. let inspectorInfo = recognizer.getEventTargetInfo().getId();
170. if (inspectorInfo !== 'progress_layer') {
171. // 用户操作到进度条区域时，禁用掉所有非progress_layer上的手势
172. recognizer.preventBegin();
173. };
174. };
175. })
176. .margin({ left: 5 })
177. .trackColor(Color.Blue)
178. .blockColor(Color.Gray)
179. .selectedColor(Color.White)
180. .trackThickness(2)
181. .flexShrink(1)
182. .flexGrow(1)
183. }
184. .flexGrow(1)
185. .flexShrink(1)
186. .id('id_progress_view')
187. }
188. }
189. .id('video_layer')
190. .backgroundColor('#E0E0E0')
191. .gesture(
192. GestureGroup(GestureMode.Exclusive,
193. PanGesture({ direction: PanDirection.Vertical, distance: 10 })
194. .tag('pan_for_brightness_control')
195. .onActionStart((event) => {
196. this.updateBrightness(true, event);
197. })
198. .onActionUpdate((event) => {
199. this.updateBrightness(false, event);
200. }),
201. PanGesture({ direction: PanDirection.Horizontal, distance: 10 })
202. .tag('pan_for_play_progress_control')
203. .onActionStart((event) => {
204. this.updateProgress(true, event);
205. })
206. .onActionUpdate((event) => {
207. this.updateProgress(false, event);
208. }),

210. LongPressGesture()
211. .tag('long_press_for_fast_forward_control')
212. .onAction(() => {
213. this.doFastForward(true); // 开始快进
214. })
215. .onActionEnd(() => {
216. this.doFastForward(false); // 停止快进
217. })
218. .onActionCancel(() => {
219. this.doFastForward(false);
220. }),

222. TapGesture({ count: 2 })
223. .tag('double_tap_on_video')
224. .onAction(() => {
225. this.toggleFullScreenState();
226. }),

228. TapGesture()
229. .tag('single_tap_on_video')
230. .onAction(() => {
231. this.togglePlayAndPause();
232. })
233. )
234. )
235. .width(this.currentWidth)
236. .height(this.currentHeight)
237. }
238. }
```

[PreventGestureRecognition.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/GestureConflict/entry/src/main/ets/Component/PreventGestureRecognition/PreventGestureRecognition.ets#L16-L256)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/7Y2RgTVZT8yrVrtKCBWZWQ/zh-cn_image_0000002583438009.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=32C6D0C38DADB3A96F010353F8B97EA306561A8809B5D3F05ABF92D5EAD6C3E6)
