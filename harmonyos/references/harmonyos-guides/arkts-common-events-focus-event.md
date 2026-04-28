---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-common-events-focus-event
title: 支持焦点处理
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 支持焦点处理
category: harmonyos-guides
scraped_at: 2026-04-28T07:39:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:912ccb6bdacef39af9d6fa085e7823853ac7bb0d97b0b50fe9feb37f998c5316
---

## 基础概念与规范

### 基础概念

**焦点、焦点链和走焦**

* 焦点：指向当前应用界面上唯一的一个可交互元素，当用户使用键盘、电视遥控器、车机摇杆/旋钮等非指向性输入设备与应用程序进行间接交互时，基于焦点的导航和交互是重要的输入手段。
* 焦点链：在应用的组件树形结构中，当一个组件获得焦点时，从根节点到该组件节点的整条路径上的所有节点都会处于焦点状态，形成一条连续的焦点链。
* 走焦：指焦点在应用内的组件之间转移的行为。这一过程对用户是透明的，但开发者可以通过监听onFocus（焦点获取）和onBlur（焦点失去）事件来捕捉这些变化。关于走焦的具体方式和规则，详见[走焦规范](arkts-common-events-focus-event.md#走焦规范)。

**焦点激活态**

焦点激活态是用来显示当前获焦组件焦点框的视觉样式。

* 显示规则

  + 默认状态：焦点激活态默认是隐藏的。
  + 激活条件：只有当应用程序进入"激活态"时，焦点激活态才会显示。
  + 重要关系：
    - 获得焦点的组件不一定显示激活态（取决于应用是否处于激活态）。
    - 显示激活态的组件必定是当前获得焦点的组件。
  + 样式定制：组件通常有内置的激活态样式，开发者可以通过样式接口自定义，自定义后会覆盖默认样式。
  + 显示优先级：当多个组件同时拥有焦点时，系统优先显示子组件的激活态，且同一时间只显示一个激活态。
* 如何进入激活态

  + 按下外接键盘的Tab键（注意：首次激活时的Tab键仅用于激活，不会触发焦点移动）。
  + 调用[FocusController](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md)的activate(true)方法。
* 如何退出激活态

  + 调用FocusController的activate(false)方法。
  + 发生点击事件时（包括触屏点击或鼠标左键点击）。

```
1. @Entry
2. @Component
3. export struct FocusActiveExample {
4. build() {
5. NavDestination() {
6. Column() {
7. Button('Set Active').width(140).height(45).margin(5).onClick(() => {
8. this.getUIContext().getFocusController().activate(true, true);
9. })
10. Button('Set Not Active').width(140).height(45).margin(5).onClick(() => {
11. this.getUIContext().getFocusController().activate(false, true);
12. })
13. }.width('100%')
14. }
15. // ...
16. }
17. }
```

[FocusActive.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/FocusActive.ets#L16-L38)

按下Tab键，焦点激活态显示。点击鼠标退出焦点激活态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/bp-gn9cFRpW-u69x3oNwjg/zh-cn_image_0000002583477969.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=BA2896A615830771956F85704B88BAB213C07E7F1C08BDB5F344F0DAA1E8E5FD)

调用[activate](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#activate14)接口进入和退出焦点激活态。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/Z3Idv67ISomdxcyvQYQZfw/zh-cn_image_0000002552798320.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=A81ED08875BB3F91FA294DB112F41B4EBDC7E3D23D17B0867F9F8F998BB2A511)

示例操作步骤：

1. 点击Set Active按钮，调用[activate](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#activate14)接口进入焦点激活态。
2. Tab键走焦至Set Not Active按钮，Enter键触发按键事件，调用[activate](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#activate14)接口退出焦点激活态。

**层级页面**

层级页面是焦点框架中特定容器组件的统称，涵盖Page、Dialog、SheetPage、ModalPage、Menu、Popup、NavBar、NavDestination等。这些组件通常具有以下关键特性：

* 视觉层级独立性：从视觉呈现上看，这些组件独立于其他页面内容，并通常位于其上方，形成视觉上的层级差异。
* 焦点跟随：此类组件在首次创建并展示之后，会立即将应用内焦点抢占。
* 走焦范围限制：当焦点位于这些组件内部时，用户无法通过键盘按键将焦点转移到组件外部的其他元素上，焦点移动仅限于组件内部。

在一个应用程序中，任何时候都至少存在一个层级页面组件，并且该组件会持有当前焦点。当该层级页面关闭或不再可见时，焦点会自动转移到下一个可用的层级页面组件上，确保用户交互的连贯性和一致性。

说明

Popup组件在focusable属性（组件属性，非通用属性）为false的时候，不会有第2条特性。

NavBar、NavDestination没有第3条特性，对于它们的走焦范围，是与它们的首个父层级页面相同的。

**根容器**

根容器是[层级页面](arkts-common-events-focus-event.md#基础概念)内的概念，当某个[层级页面](arkts-common-events-focus-event.md#基础概念)首次创建并展示时，根据[层级页面](arkts-common-events-focus-event.md#基础概念)的特性，焦点会立即被该[层级页面](arkts-common-events-focus-event.md#基础概念)抢占。此时，该[层级页面](arkts-common-events-focus-event.md#基础概念)所在焦点链的末端节点将成为默认焦点，而这个默认焦点通常位于该[层级页面](arkts-common-events-focus-event.md#基础概念)的根容器上。

在缺省状态下，[层级页面](arkts-common-events-focus-event.md#基础概念)的默认焦点位于其根容器上，但开发者可以通过defaultFocus属性来自定义这一行为。

当焦点位于根容器时，首次按下Tab键不仅会使焦点进入激活状态，还会根据[焦点传递规则](arkts-common-events-focus-event.md#焦点传递规则)进行传递。

### 焦点传递规则

焦点传递是指当用户首次激活应用焦点系统时，焦点如何从根节点逐级向下传递到具体组件的过程。

在焦点链上的组件，都会处于获焦状态。同时组件在获焦时，会继续向下递归传递获焦状态，每次传递给第一个子组件，直到叶子节点。

```
1. @Entry
2. export struct FocusTransferExample {
3. @State logText: string = '\n';
4. context = this.getUIContext().getHostContext();

6. addText(message: string) {
7. this.logText += `${message}\n`;
8. };

10. build() {
11. NavDestination() {
12. Column() {
13. Row() {
14. Column() {
15. Button('Button 1')
16. .margin(20)
17. .onClick(() => {
18. // 请将$r('app.string.Focus_Event')替换为实际资源文件，在本示例中该资源文件的value值为"获焦信息"
19. this.logText = this.context!.resourceManager.getStringSync($r('app.string.Focus_Event').id) + '：\n';
20. this.getUIContext().getFocusController().requestFocus('Row 2');
21. })
22. }
23. }

25. Column() {
26. Row() {
27. Button('Button 2')
28. .margin(20)
29. .onFocus(() => {
30. // 请将$r('app.string.Get_Focus')替换为实际资源文件，在本示例中该资源文件的value值为"获得焦点"
31. this.addText('Button 2' + this.context!.resourceManager.getStringSync($r('app.string.Get_Focus').id));
32. })
33. Button('button 3')
34. .margin(20)
35. .onFocus(() => {
36. // 请将$r('app.string.Get_Focus')替换为实际资源文件，在本示例中该资源文件的value值为"获得焦点"
37. this.addText('Button 3' + this.context!.resourceManager.getStringSync($r('app.string.Get_Focus').id));
38. })
39. }
40. .id('Row 2')
41. .onFocus(() => {
42. // 请将$r('app.string.Get_Focus')替换为实际资源文件，在本示例中该资源文件的value值为"获得焦点"
43. this.addText('Row 2' + this.context!.resourceManager.getStringSync($r('app.string.Get_Focus').id));
44. })
45. }
46. .onFocus(() => {
47. // 请将$r('app.string.Get_Focus')替换为实际资源文件，在本示例中该资源文件的value值为"获得焦点"
48. this.addText('Column 2' + this.context!.resourceManager.getStringSync($r('app.string.Get_Focus').id));
49. })

51. Scroll() {
52. Text(this.logText)
53. .fontSize(14)
54. .textAlign(TextAlign.Start)
55. .padding(10)
56. }
57. .height('40%')
58. .width('100%')
59. .border({ width: 1, color: '#ccc' })
60. .margin(10)
61. }
62. .height('100%')
63. .padding(20)
64. }
65. // ...
66. }
67. }
```

[FocusTransfer.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/FocusTransfer.ets#L16-L88)

运行后点击Button1，请求焦点给Row组件，Row组件的第一个可获焦子节点Button2获焦。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/eHZ6mBwFRkC80UTyohHZxw/zh-cn_image_0000002583438015.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=06DADB353F229B2340615E1179B923A1E915FF71A11576BDBA2FDF1979AFA8DE)

### 走焦规范

根据走焦的触发方式，可以分为主动走焦和被动走焦。

**主动走焦**

指开发者/用户主观行为导致的焦点移动，包括：使用外接键盘的按键走焦（Tab键/Shift+Tab键/方向键）、使用requestFocus申请焦点、clearFocus清除焦点、focusOnTouch点击申请焦点等接口导致的焦点转移。

* 按键走焦

  1. 前提：当前应用需处于焦点激活态。
  2. 范围限制：按键走焦仅在当前获得焦点的层级页面内进行，具体参见“层级页面”中的“走焦范围限制”部分。
  3. 按键类型：

     Tab键：遵循Z字型遍历逻辑，完成当前范围内所有叶子节点的遍历，到达当前范围内的最后一个组件后，继续按下Tab键，焦点将循环至范围内的第一个可获焦组件，实现循环走焦。

     Shift+Tab键：与Tab键具有相反的焦点转移效果。

     方向键（上、下、左、右）：遵循十字型移动策略，在单层容器中，焦点的转移由该容器的特定走焦算法决定。若算法判定下一个焦点应落在某个容器组件上，系统将采用中心点距离优先的算法来进一步确定容器内的目标子节点。
  4. 走焦算法：每个可获焦的容器组件都有其特定的走焦算法，用于定义焦点转移的规则。
  5. 子组件优先：当子组件处理按键走焦事件，父组件将不再介入。
* requestFocus

  详见[主动获焦失焦](arkts-common-events-focus-event.md#主动获焦失焦)，可以主动将焦点转移到指定组件上。

  不可跨窗口或跨ArkUI实例申请焦点，但可以跨层级页面申请焦点。
* clearFocus

  详见[clearFocus](../harmonyos-references/arkts-apis-uicontext-focuscontroller.md#clearfocus12)，会清除当前层级页面中的焦点，最终焦点停留在根容器上。
* focusOnTouch

  详见[focusOnTouch](../harmonyos-references/ts-universal-attributes-focus.md#focusontouch9)，使绑定组件具备点击后获得焦点的能力。若组件本身不可获焦，则此功能无效。若绑定的是容器组件，点击后优先将焦点转移给上一次获焦的子组件，否则转移给第一个可获焦的子组件。

**被动走焦**

被动走焦是指组件焦点因系统或其他操作而自动转移，无需开发者直接干预，这是焦点系统的默认行为。

目前会被动走焦的机制有：

* 组件删除：当处于焦点状态的组件被删除时，焦点框架首先尝试将焦点转移到相邻的兄弟组件上，遵循先向后再向前的顺序。若所有兄弟组件均不可获焦，则焦点将释放，并通知其父组件进行焦点处理。
* 属性变更：若将处于焦点状态的组件的focusable或enabled属性设置为false，或者将visibility属性设置为不可见，系统将自动转移焦点至其他可获焦组件，转移方式与1中相同。
* [层级页面](arkts-common-events-focus-event.md#基础概念)切换：当发生[层级页面](arkts-common-events-focus-event.md#基础概念)切换时，如从一个[层级页面](arkts-common-events-focus-event.md#基础概念)跳转到另一个[层级页面](arkts-common-events-focus-event.md#基础概念)，当前[层级页面](arkts-common-events-focus-event.md#基础概念)的焦点将自动释放，新[层级页面](arkts-common-events-focus-event.md#基础概念)可能会根据预设逻辑自动获得焦点。
* Web组件初始化：对于Web组件，当其被创建时，若其设计需要立即获得焦点（如某些弹出框或输入框），则可能触发焦点转移至该Web组件，其行为属于组件自身的行为逻辑，不属于焦点框架的规格范围。

### 走焦算法

在焦点管理系统中，每个可获焦的容器都配备有特定的走焦算法，这些算法定义了当使用Tab键、Shift+Tab键或方向键时，焦点如何从当前获焦的子组件转移到下一个可获焦的子组件。

容器采用何种走焦算法取决于其UX（用户体验）规格，并由容器组件进行适配。目前，焦点框架支持三种走焦算法：线性走焦、投影走焦和自定义走焦。

**线性走焦算法**

线性走焦算法是默认的走焦策略，它基于容器中子节点在节点树中的挂载顺序进行走焦，常用于单方向布局的容器，如Row、Column和Flex容器。运行规则如下：

* 顺序依赖：走焦顺序完全基于子节点在节点树中的挂载顺序，与它们在界面上的实际布局位置无关。
* Tab键走焦：使用Tab键时，焦点将按照子节点的挂载顺序依次遍历。
* 方向键走焦：当使用与容器定义方向垂直的方向键时，容器不接受该方向的走焦请求。例如，在横向的Row容器中，无法使用方向键进行上下移动。
* 边界处理：当焦点位于容器的首尾子节点时，容器将拒绝与当前焦点方向相反的方向键走焦请求。例如，焦点在一个横向的Row容器的第一个子节点上时，该容器无法处理方向键左的走焦请求。

```
1. @Entry
2. @Component
3. export struct FocusLinerExample {
4. build() {
5. NavDestination() {
6. Column() {
7. Column() {
8. Button('Column Button1')
9. .width(150)
10. .height(45)
11. .fontColor(Color.White)
12. .margin(10)
13. Button('Column Button2')
14. .width(150)
15. .height(45)
16. .fontColor(Color.White)
17. .margin(10)
18. }
19. .margin(10)
20. Row() {
21. Button('Row Button1')
22. .width(150)
23. .height(45)
24. .fontColor(Color.White)
25. .margin(10)
26. Button('Row Button2')
27. .width(150)
28. .height(45)
29. .fontColor(Color.White)
30. .margin(10)
31. }
32. }
33. }
34. // ...
35. }
36. }
```

[FocusTraversalGuidelines.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/FocusTraversalGuidelines.ets#L16-L57)

Tab键走焦：按照子节点的挂载顺序循环走焦。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/F0V4R1bGS2imEj_VXfY99Q/zh-cn_image_0000002552957970.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=0992F658C22B7D18E310678BEF47BDDAA9A42EDB9963FA56A1938CE4DC8D91B4)

方向键上下走焦：纵向的Column容器中，可以使用上下键走焦，无法使用左右键走焦。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/kmFzi6B7QSq8yASvjRmxAA/zh-cn_image_0000002583477971.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=7EA2DDCDF3DE7A0069135BB277E149F1160ADC2D2AEB3BADBB52F7034FC2EDA7)

横向的Row容器中，可以使用左右键走焦，无法使用上下键走焦。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/14K8W3FrSzq1GNiXdOhgUQ/zh-cn_image_0000002552798322.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=417DD86A5F42330C4F915D8E783662DF48B549445D0DBBB9E48C7582046308F0)

**投影走焦算法**

投影走焦算法基于当前获焦组件在走焦方向上的投影，结合子组件与投影的重叠面积和中心点距离进行胜出判定。该算法适用于子组件大小不一的容器，目前仅支持配置了wrap属性的Flex组件。运行规则如下：

* 方向键走焦时，判断投影与子组件区域的重叠面积，在所有面积不为0的子组件中，计算它们与当前获焦组件的中心点直线距离，选择距离最短的子组件。若存在多个备选子组件，则选择节点树上更靠前的子组件。若无任何子组件与投影有重叠，说明该容器无法处理该方向键的走焦请求。
* Tab键走焦时，先使用规格1，按照方向键右进行判定，若找到则成功退出，若无法找到，则将当前获焦子组件的位置模拟往下移动该获焦子组件的高度，然后再按照方向键左进行投影判定，有投影重叠且中心点直线距离最近的子组件胜出，若无投影重叠的子组件，则表示该容器无法处理本次Tab键走焦请求。
* Shift+Tab键走焦时，先使用规格1，按照方向键左进行判定，找到则成功退出。若无法找到，则将当前获焦子组件的位置模拟向上移动该获焦子组件的高度，然后再按照方向键右进行投影判定，有投影重叠且中心点直线距离最近的子组件胜出，若无投影重叠的子组件，则表示该容器无法处理本次的Shift+Tab键走焦请求。

```
1. @Entry
2. @Component
3. export struct ProjectAreaFocusExample {
4. build() {
5. NavDestination() {
6. Column() {
7. Column({ space: 5 }) {
8. Text('Wrap').fontSize(12).width('90%')
9. // 子组件多行布局
10. Flex({ wrap: FlexWrap.Wrap }) {
11. Button('1').width(140).height(50).margin(5)
12. Button('2').width(140).height(50).margin(5)
13. Button('3').width(140).height(50).margin(5)
14. Button('4').width(140).height(50).margin(5)
15. Button('5').width(140).height(50).margin(5)
16. }
17. .width('90%')
18. .padding(10)
19. }.width('100%').margin({ top: 5 })
20. }.width('100%')
21. }
22. // ...
23. }
24. }
```

[ProjectionBasedFocus.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/ProjectionBasedFocus.ets#L16-L45)

说明

* 这种投影走焦算法计算的走焦顺序与组件布局和大小密切相关，建议在组件排列非常规整的场景下使用。如果组件大小不一且存在横向或纵向的交叠关系，则可能会导致走焦顺序与开发者预期不符。
* 如果开发者希望有明确的走焦顺序，建议使用Column/Row等顺序走焦的容器实现。

Flex多行组件布局，组件大小一致，走焦正常。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/qutuHPEYR3CAH8XuBwfr6g/zh-cn_image_0000002583438017.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=3D5D13E34A79B4A8E14803F5088CF8604BC575969EE37650B7DFE686309717AF)

```
1. @Entry
2. @Component
3. export struct ProjectAreaFocusFlexExample {
4. build() {
5. NavDestination() {
6. Column() {
7. Column({ space: 5 }) {
8. Text('Wrap').fontSize(12).width('90%')
9. // 子组件多行布局
10. Flex({ wrap: FlexWrap.Wrap }) {
11. Button('1').width(145).height(50).margin(5)
12. Button('2').width(145).height(50).margin(5)
13. Button('3').width(150).height(50).margin(5)
14. Button('4').width(160).height(50).margin(5)
15. Button('5').width(170).height(50).margin(5)
16. }
17. .width('90%')
18. .padding(10)
19. }.width('100%').margin({ top: 5 })
20. }.width('100%')
21. }
22. // ...
23. }
24. }
```

[FrojectAreaFocusFlex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/FrojectAreaFocusFlex.ets#L16-L45)

Flex多行组件布局，组件大小不一且有纵向的交叠关系，无法Tab键走焦至下方4、5按钮组件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/3XLFWWKjSNGwKEizHMoCag/zh-cn_image_0000002552957972.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=BF46DFC5F8F95D0D839AD9ED2C0C3707BF37C32A382875F61BBFA368E06B94EB)

**自定义走焦算法**

由组件自定义的走焦算法，规格由组件定义。

## 获焦/失焦事件

```
1. onFocus(event: () => void)
```

获焦事件回调，绑定该接口的组件获焦时，回调响应。

```
1. onBlur(event:() => void)
```

失焦事件回调，绑定该接口的组件失焦时，回调响应。

onFocus和onBlur两个接口通常成对使用，来监听组件的焦点变化。

```
1. @Entry
2. @Component
3. export struct OnFocusBlur {
4. @State oneButtonColor: Color = Color.Gray;
5. @State twoButtonColor: Color = Color.Gray;
6. @State threeButtonColor: Color = Color.Gray;

8. build() {
9. NavDestination() {
10. Column({ space: 20 }) {
11. // 通过外接键盘的上下键可以让焦点在三个按钮间移动，按钮获焦时颜色变化，失焦时变回原背景色
12. Button('First Button')
13. .width(260)
14. .height(70)
15. .backgroundColor(this.oneButtonColor)
16. .fontColor(Color.Black)
17. // 监听第一个组件的获焦事件，获焦后改变颜色
18. .onFocus(() => {
19. this.oneButtonColor = Color.Green;
20. })
21. // 监听第一个组件的失焦事件，失焦后改变颜色
22. .onBlur(() => {
23. this.oneButtonColor = Color.Gray;
24. })

26. Button('Second Button')
27. .width(260)
28. .height(70)
29. .backgroundColor(this.twoButtonColor)
30. .fontColor(Color.Black)
31. // 监听第二个组件的获焦事件，获焦后改变颜色
32. .onFocus(() => {
33. this.twoButtonColor = Color.Green;
34. })
35. // 监听第二个组件的失焦事件，失焦后改变颜色
36. .onBlur(() => {
37. this.twoButtonColor = Color.Gray;
38. })

40. Button('Third Button')
41. .width(260)
42. .height(70)
43. .backgroundColor(this.threeButtonColor)
44. .fontColor(Color.Black)
45. // 监听第三个组件的获焦事件，获焦后改变颜色
46. .onFocus(() => {
47. this.threeButtonColor = Color.Green;
48. })
49. // 监听第三个组件的失焦事件，失焦后改变颜色
50. .onBlur(() => {
51. this.threeButtonColor = Color.Gray;
52. })
53. }.width('100%').margin({ top: 20 })
54. }
55. // ...
56. }
57. }
```

[onFocusBlur.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/onFocusBlur.ets#L16-L78)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/uHYtXLLMRBOIIp0kGtgOfQ/zh-cn_image_0000002583477973.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=ABE15BEA2A83B1A70DB1D2CD35550FA3AF3F757F20EE2F323624236E0F4543E3)

上述示例包含以下3步：

* 应用打开，按下Tab键激活走焦，“First Button”显示焦点激活态样式：组件外围有一个蓝色的闭合框，onFocus回调响应，背景色变成绿色。
* 按下Tab键，触发走焦，“Second Button”获焦，onFocus回调响应，背景色变成绿色；“First Button”失焦，onBlur回调响应，背景色变回灰色。
* 按下Tab键，触发走焦，“Third Button”获焦，onFocus回调响应，背景色变成绿色；“Second Button”失焦，onBlur回调响应，背景色变回灰色。

父子节点同时存在获焦和失焦事件时，获焦/失焦事件响应顺序为：

父节点Row1失焦 —> 子节点Button1失焦 —> 子节点Button2获焦 —> 父节点Row2获焦。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_FocusAndBlurExample]';
4. const DOMAIN = 0xF811;
5. const BUNDLE = 'MyApp_FocusAndBlurExample';

7. @Entry
8. @Component
9. export struct FocusAndBlurExample {
10. build() {
11. NavDestination() {
12. Column() {
13. Column({ space: 5 }) {
14. Row() { // 父节点Row1
15. Button('Button1') // 子节点Button1
16. .width(140)
17. .height(45)
18. .margin(5)
19. .onFocus(() => {
20. hilog.info(DOMAIN, TAG, `${BUNDLE} Button1 onFocus`);
21. })
22. .onBlur(() => {
23. hilog.info(DOMAIN, TAG, `${BUNDLE} Button1 onBlur`);
24. })
25. }
26. .onFocus(() => {
27. hilog.info(DOMAIN, TAG, BUNDLE + 'Row1 onFocus');
28. })
29. .onBlur(() => {
30. hilog.info(DOMAIN, TAG, `${BUNDLE} Row1 onBlur`);
31. })

33. Row() { // 父节点Row2
34. Button('Button2') // 子节点Button2
35. .width(140)
36. .height(45)
37. .margin(5)
38. .onFocus(() => {
39. hilog.info(DOMAIN, TAG, `${BUNDLE} Button2 onFocus`);
40. })
41. .onBlur(() => {
42. hilog.info(DOMAIN, TAG, `${BUNDLE} Button2 onBlur`);
43. })
44. }
45. .onFocus(() => {
46. hilog.info(DOMAIN, TAG, BUNDLE + 'Row2 onFocus');
47. })
48. .onBlur(() => {
49. hilog.info(DOMAIN, TAG, `${BUNDLE} Row2 onBlur`);
50. })
51. }.width('100%').margin({ top: 5 })
52. }.width('100%')
53. }
54. // ...
55. }
56. }
```

[OnFocusOnBlurEvents.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/OnFocusOnBlurEvents.ets#L16-L77)

Button1走焦到Button2，日志打印顺序：

```
1. Row1 onBlur
2. Button1 onBlur
3. Button2 onFocus
4. Row2 onFocus
```

## 设置组件是否可获焦

```
1. focusable(value: boolean)
```

设置组件是否可获焦。

按照组件的获焦能力可大致分为三类：

* 默认可获焦的组件，通常是有交互行为的组件，例如Button、Checkbox、TextInput组件，此类组件无需设置任何属性，默认即可获焦。
* 有获焦能力，但默认不可获焦的组件，典型的是Text、Image组件，此类组件缺省情况下无法获焦，若需要使其获焦，可使用通用属性focusable(true)使能。对于没有配置focusable属性，有获焦能力但默认不可获焦的组件，例如没有可获焦子组件的容器组件，为其配置onClick或是单指单击的Tap手势，该组件会隐式地成为可获焦组件。如果其focusable属性被设置为false，即使配置了上述事件，该组件依然不可获焦。
* 无获焦能力的组件，通常是无任何交互行为的展示类组件，例如[Blank](../harmonyos-references/ts-basic-components-blank.md)、[Canvas](../harmonyos-references/ts-components-canvas-canvas.md)、[Circle](../harmonyos-references/ts-drawing-components-circle.md)组件，此类组件即使使用focusable属性也无法使其可获焦。

设置容器组件可获焦：

获焦的主要目的是为了响应用户交互，如果组件不具备交互能力，则其也不会具有可获焦能力。容器组件通常不具备交互能力，因此如果一个容器组件（如Stack、Column）作为叶子节点，即使通过.focusable(true)也无法使其具备可获焦能力。需要注意的是通过动态方式创建的[FrameNode](../harmonyos-references/js-apis-arkui-framenode.md)节点也受限于这个规则。

如果想让作为叶子节点的容器组件可获焦，可通过以下任一方式实现：

* 在其内添加一个具备获焦能力的叶子节点组件(如button)。
* 为其配置onClick、Tap手势等使其能响应点击交互。

```
1. enabled(value: boolean)
```

设置组件可交互性属性[enabled](../harmonyos-references/ts-universal-attributes-enable.md#enabled)为false，则组件不可交互，无法获焦。

```
1. visibility(value: Visibility)
```

设置组件可见性属性[visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)为Visibility.None或Visibility.Hidden，则组件不可见，无法获焦。

```
1. focusOnTouch(value: boolean)
```

设置当前组件是否支持点击获焦能力。

说明

当某组件处于获焦状态时，将其的focusable属性或enabled属性设置为false，会自动使该组件失焦，然后焦点按照[走焦规范](arkts-common-events-focus-event.md#走焦规范)将焦点转移给其他组件。

```
1. @Entry
2. @Component
3. export struct FocusableExample {
4. @State textFocusable: boolean = true;
5. @State textEnabled: boolean = true;
6. @State color1: Color = Color.Yellow;
7. @State color2: Color = Color.Yellow;
8. @State color3: Color = Color.Yellow;

10. build() {
11. NavDestination() {
12. Column({ space: 12 }) {
13. // 请将$r('app.string.Focus_Focusable_text')替换为实际资源文件，在本示例中该资源文件的value值为"当某组件处于获焦状态"
14. Text($r('app.string.Focus_Focusable_text'))
15. .fontSize(14)
16. .fontColor('#666')
17. Column({ space: 5 }) {
18. Text('Default Text')    // 第一个Text组件未设置focusable属性，默认不可获焦
19. .borderColor(this.color1)
20. .borderWidth(2)
21. .width(300)
22. .height(70)
23. .onFocus(() => {
24. this.color1 = Color.Blue;
25. })
26. .onBlur(() => {
27. this.color1 = Color.Yellow;
28. })
29. Divider()

31. Text('focusable: ' + this.textFocusable)    // 第二个Text设置了focusable初始为true，focusableOnTouch为true
32. .borderColor(this.color2)
33. .borderWidth(2)
34. .width(300)
35. .height(70)
36. .focusable(this.textFocusable)
37. .focusOnTouch(true)
38. .onFocus(() => {
39. this.color2 = Color.Blue;
40. })
41. .onBlur(() => {
42. this.color2 = Color.Yellow;
43. })

45. Text('enabled: ' + this.textEnabled)    // 第三个Text设置了focusable为true，enabled初始为true
46. .borderColor(this.color3)
47. .borderWidth(2)
48. .width(300)
49. .height(70)
50. .focusable(true)
51. .enabled(this.textEnabled)
52. .focusOnTouch(true)
53. .onFocus(() => {
54. this.color3 = Color.Blue;
55. })
56. .onBlur(() => {
57. this.color3 = Color.Yellow;
58. })

60. Divider()

62. Row() {
63. Button('Button1')
64. .width(140).height(70)
65. Button('Button2')
66. .width(160).height(70)
67. }

69. Divider()
70. Button('Button3')
71. .width(300).height(70)

73. Divider()
74. }.width('100%').justifyContent(FlexAlign.Center)
75. .onKeyEvent((e) => {
76. // 绑定onKeyEvent，在该Column组件获焦时，按下'F'键，可将第二个Text的focusable置反
77. if (e.keyCode === 2022 && e.type === KeyType.Down) {
78. this.textFocusable = !this.textFocusable;
79. }
80. // 绑定onKeyEvent，在该Column组件获焦时，按下'G'键，可将第三个Text的enabled置反
81. if (e.keyCode === 2023 && e.type === KeyType.Down) {
82. this.textEnabled = !this.textEnabled;
83. }
84. })
85. }
86. .width('100%')
87. .height('100%')
88. .padding({ left: 12, right: 12 })
89. }
90. // ...
91. }
92. }
```

[Focusable.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/Focusable.ets#L18-L115)

运行效果：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/4Gs4L1Y6QzedmJ_mwkwnag/zh-cn_image_0000002552798324.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=8231AA492D967948EA3B30D62D228BED48CAF8D07B7A7D1EE050A6CF8A84175E)

上述示例包含以下3步：

* 第一个Text组件没有设置focusable(true)属性，该Text组件无法获焦。
* 点击第二个Text组件，由于设置了focusOnTouch(true)，第二个组件获焦。按下Tab键，触发走焦，仍然是第二个Text组件获焦。按键盘F键，触发onKeyEvent，focusable置为false，第二个Text组件变成不可获焦，焦点自动转移，会自动从Text组件寻找下一个可获焦组件，焦点转移到第三个Text组件上。
* 按键盘G键，触发onKeyEvent，enabled置为false，第三个Text组件变成不可获焦，焦点自动转移，使焦点转移到Row容器上，容器中使用的是默认配置，会转移到Button1上。

## 设置容器绘制焦点框

虽然容器组件本身可以获焦，但是无法绘制焦点框。可以为其配置onClick或是单指单击的Tap手势，在容器上绘制焦点框。

说明

容器绘制焦点框前提：

* 容器内部没有可获焦子节点。
* 容器配置有onClick或是单指单击的Tap手势。
* 容器本身未设置focusable属性，或设置在onClick或是单指单击的Tap手势之后。

```
1. import { hilog } from '@kit.PerformanceAnalysisKit';

3. const TAG = '[Sample_FocusAndBlurExample]';
4. const DOMAIN = 0xF811;
5. const BUNDLE = 'MyApp_FocusAndBlurExample';

7. @Entry
8. @Component
9. export struct ScopeFocusExample {
10. @State scopeFocusState: boolean = true;

12. build() {
13. NavDestination() {
14. Column() {
15. Column({ space: 5 }) {
16. // 请将$r('app.string.Container_Coking')替换为实际资源文件，在本示例中该资源文件的value值为"容器获焦"
17. Text($r('app.string.Container_Coking')).textAlign(TextAlign.Center)
18. }
19. .justifyContent(FlexAlign.Center)
20. .width('80%')
21. .height(50)
22. .margin({ top: 5, bottom: 5 })
23. .onClick(() => {
24. })
25. .focusable(this.scopeFocusState)

27. Button('Button1')
28. .width(140)
29. .height(45)
30. .margin(5)
31. .onClick(() => {
32. this.scopeFocusState = !this.scopeFocusState;
33. hilog.info(DOMAIN, TAG, BUNDLE + 'Button1 onFocus');
34. })
35. Button('Button2')
36. .width(140)
37. .height(45)
38. .margin(5)
39. }.width('100%')
40. }
41. // ...
42. }
43. }
```

[ScopeFocus.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/ScopeFocus.ets#L16-L66)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/mqyRHf3bTeKXt0aJ9EH_ug/zh-cn_image_0000002583438019.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=5C0613D06A2A395CE60F933D9D3065BC9D2AF9C8676B536419EB7251442FB7E0)

上述示例包含以下2步：

* Column配置onClick事件并设置focusable为true后，Tab键走焦，Column容器可以绘制焦点框。
* 点击Button1，将Column的focusable属性设置为false，Column容器无法获焦和绘制焦点框。

## 设置焦点停留在容器上

```
1. tabStop(isTabStop: boolean)
```

设置当前容器组件的[tabStop](../harmonyos-references/ts-universal-attributes-focus.md#tabstop14)属性，可决定在走焦时焦点是否会停留在当前容器。

```
1. @Entry
2. @Component
3. export struct TabStopExample {
4. build() {
5. NavDestination() {
6. Column({ space: 20 }) {
7. Button('Button1')
8. .width(140)
9. .height(45)
10. .margin(5)
11. Column() {
12. Button('Button2')
13. .width(140)
14. .height(45)
15. .margin(5)
16. Button('Button3')
17. .width(140)
18. .height(45)
19. .margin(5)
20. }.tabStop(true)
21. }.width('100%')
22. }
23. // ...
24. }
25. }
```

[TabStop.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/TabStop.ets#L16-L46)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/xGerce5kS7uEC75fig-Yvw/zh-cn_image_0000002552957974.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=3FBEF0DEB5ABE57AA2381097EA3AC6B3503368F98C0A90E8F584FA4F944E3739)

上述示例包含以下2步：

* Column配置tabStop后，Tab键走焦，焦点在Button1和Column容器之间切换，Column容器可以绘制焦点框。
* 走焦至Column容器后，按Enter键，焦点转移到容器中的第一个可获焦节点上。Tab键走焦，走焦至容器中其他可获焦节点。

## 默认焦点

### 层级页面的默认焦点

```
1. defaultFocus(value: boolean)
```

设置当前组件是否为当前[层级页面](arkts-common-events-focus-event.md#基础概念)上的默认焦点。

```
1. @Entry
2. @Component
3. export struct DefaultFocus {
4. @State oneButtonColor: Color = Color.Gray;
5. @State twoButtonColor: Color = Color.Gray;
6. @State threeButtonColor: Color = Color.Gray;

8. build() {
9. NavDestination() {
10. Column({ space: 20 }) {
11. // 通过外接键盘的上下键可以让焦点在三个按钮间移动，按钮获焦时颜色变化，失焦时变回原背景色
12. Button('First Button')
13. .width(260)
14. .height(70)
15. .backgroundColor(this.oneButtonColor)
16. .fontColor(Color.Black)
17. // 监听第一个组件的获焦事件，获焦后改变颜色
18. .onFocus(() => {
19. this.oneButtonColor = Color.Green;
20. })
21. // 监听第一个组件的失焦事件，失焦后改变颜色
22. .onBlur(() => {
23. this.oneButtonColor = Color.Gray;
24. })

26. Button('Second Button')
27. .width(260)
28. .height(70)
29. .backgroundColor(this.twoButtonColor)
30. .fontColor(Color.Black)
31. // 监听第二个组件的获焦事件，获焦后改变颜色
32. .onFocus(() => {
33. this.twoButtonColor = Color.Green;
34. })
35. // 监听第二个组件的失焦事件，失焦后改变颜色
36. .onBlur(() => {
37. this.twoButtonColor = Color.Gray;
38. })

40. Button('Third Button')
41. .width(260)
42. .height(70)
43. .backgroundColor(this.threeButtonColor)
44. .fontColor(Color.Black)
45. // 设置默认焦点
46. .defaultFocus(true)
47. // 监听第三个组件的获焦事件，获焦后改变颜色
48. .onFocus(() => {
49. this.threeButtonColor = Color.Green;
50. })
51. // 监听第三个组件的失焦事件，失焦后改变颜色
52. .onBlur(() => {
53. this.threeButtonColor = Color.Gray;
54. })
55. }.width('100%').margin({ top: 20 })
56. }
57. // ...
58. }
59. }
```

[DefaultFocus.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/DefaultFocus.ets#L16-L80)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/UwhWzQJzSDyDHS5bqWTadA/zh-cn_image_0000002583477975.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=6BD99A8B413B57C0CE1CBA182F96A588076E40B88C1DE41820DC5A3BEC157F29)

上述示例包含以下2步：

* 在第三个Button组件上设置了defaultFocus(true)，进入[层级页面](arkts-common-events-focus-event.md#基础概念)后第三个Button默认获焦，显示为绿色。
* 按下Tab键，触发走焦，第三个Button正处于获焦状态，会出现焦点框。

### 容器的默认焦点

容器的默认焦点受到[获焦优先级](arkts-common-events-focus-event.md#焦点组与获焦优先级)的影响。

**defaultFocus与FocusPriority的区别**

[defaultFocus](../harmonyos-references/ts-universal-attributes-focus.md#defaultfocus9)是用于指定[层级页面](arkts-common-events-focus-event.md#基础概念)首次展示时的默认获焦节点，[FocusPriority](../harmonyos-references/ts-universal-attributes-focus.md#focuspriority12)是用于指定某个容器首次获焦时其子节点的获焦优先级。上述两个属性在某些场景同时配置时行为未定义，例如下面的场景，[层级页面](arkts-common-events-focus-event.md#基础概念)首次展示无法同时满足defaultFocus获焦和高优先级组件获焦。

示例

```
1. @Entry
2. @Component
3. export struct FocusScopePriorityPrevious {
4. build() {
5. NavDestination() {
6. Row() {
7. Button('Button1')
8. .defaultFocus(true)
9. Button('Button2')
10. .focusScopePriority('RowScope', FocusPriority.PREVIOUS)
11. }.focusScopeId('RowScope')
12. }
13. // ···
14. }
15. }
```

[FocusScopePriorityPrevious.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/FocusScopePriorityPrevious.ets#L16-L35)

### 层级页面/容器整体获焦时的焦点链

**整体获焦与非整体获焦**

* 整体获焦是[层级页面](arkts-common-events-focus-event.md#基础概念)/容器自身作为焦点链的叶节点获焦，获焦后再把焦点链叶节点转移到子孙组件。例如，[层级页面](arkts-common-events-focus-event.md#基础概念)切换、Navigation组件中的路由切换、焦点组走焦、容器组件主动调用requestFocusById等。
* 非整体获焦是某个组件作为焦点链叶节点获焦，导致其祖先节点跟着获焦。例如TextInput组件主动获取焦点、Tab键在非焦点组场景下走焦等。

**整体获焦的焦点链形成**

1.[层级页面](arkts-common-events-focus-event.md#基础概念)首次获焦：

* 焦点链叶节点为配置了defaultFocus的节点。
* 未配置defaultFocus时，焦点停留在[层级页面](arkts-common-events-focus-event.md#基础概念)的根容器上。

2.[层级页面](arkts-common-events-focus-event.md#基础概念)非首次获焦：由上次获焦的节点获焦。

3.获焦链上存在配置了获焦优先级的组件和容器：

* 容器内存在优先级大于PREVIOUS的组件，由优先级最高的组件获焦。
* 容器内不存在优先级大于PREVIOUS的组件，由上次获焦的节点获焦。例如，窗口失焦后重新获焦。

## 焦点样式

说明

最终绘制焦点激活态的组件的[zIndex](../harmonyos-references/ts-universal-attributes-z-order.md#zindex)默认会被抬升至INT\_MAX，如果该组件已经配置了zIndex，则不做zIndex调整。该组件不再绘制焦点激活态时，例如组件失焦或是退出走焦态，zIndex恢复为默认层级。

```
1. focusBox(style: FocusBoxStyle)
```

设置当前组件系统焦点框样式。

```
1. import { ColorMetrics, LengthMetrics } from '@kit.ArkUI';

3. @Entry
4. @Component
5. export struct RequestFocusExample {
6. build() {
7. NavDestination() {
8. Column({ space: 30 }) {
9. Button('small black focus box')
10. .focusBox({
11. margin: new LengthMetrics(0),
12. strokeColor: ColorMetrics.rgba(0, 0, 0),
13. })
14. Button('large red focus box')
15. .focusBox({
16. margin: LengthMetrics.px(20),
17. strokeColor: ColorMetrics.rgba(255, 0, 0),
18. strokeWidth: LengthMetrics.px(10)
19. })
20. }
21. .alignItems(HorizontalAlign.Center)
22. .width('100%')
23. }
24. // ...
25. }
26. }
```

[RequestFocus.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/RequestFocus.ets#L16-L47)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/_-RmSiyQRsGX2qX1bG4GqA/zh-cn_image_0000002552798326.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=4E5D5089EE9DAAF25EDC8E2F9A2FD7E9C69FEBE546CD19B44C19FC2C2189DB9C)

上述示例包含以下2步：

* 进入[层级页面](arkts-common-events-focus-event.md#基础概念)，按下Tab键触发走焦，第一个Button获焦，焦点框样式为紧贴边缘的黑色细框。
* 按下Tab键，走焦到第二个Button，焦点框样式为远离边缘的红色粗框。

## 主动获焦/失焦

* 使用FocusController中的方法

  更推荐使用FocusController中的requestFocus主动获取焦点。优势如下：

  + 当前帧生效，避免被下一帧组件树变化影响。
  + 有异常值返回，便于排查主动获取焦点失败的原因。
  + 避免多实例场景中取到错误实例。

  需先使用UIContext中的[getFocusController()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getfocuscontroller12)方法获取实例，再通过此实例调用对应方法。

  ```
  1. requestFocus(key: string): void
  ```

  通过组件的id将焦点转移到组件树对应的实体节点，生效时间为当帧生效。

  ```
  1. clearFocus(): void
  ```

  清除焦点，将焦点强制转移到层级页面根容器节点，焦点链路上其他节点失焦。
* 使用focusControl中的方法

  ```
  1. requestFocus(value: string): boolean
  ```

  调用此接口可以主动让焦点转移至参数指定的组件上，焦点转移生效时间为下一个帧信号。

  ```
  1. @Entry
  2. @Component
  3. export struct FocusControl {
  4. @State btColor: string = '#ff2787d9';
  5. @State btColor2: string = '#ff2787d9';

  7. build() {
  8. NavDestination() {
  9. Column({ space: 20 }) {
  10. Column({ space: 5 }) {
  11. Button('Button')
  12. .width(200)
  13. .height(70)
  14. .fontColor(Color.White)
  15. .focusOnTouch(true)
  16. .backgroundColor(this.btColor)
  17. .onFocus(() => {
  18. this.btColor = '#ffd5d5d5';
  19. })
  20. .onBlur(() => {
  21. this.btColor = '#ff2787d9';
  22. })
  23. .id('testButton')

  25. Button('Button')
  26. .width(200)
  27. .height(70)
  28. .fontColor(Color.White)
  29. .focusOnTouch(true)
  30. .backgroundColor(this.btColor2)
  31. .onFocus(() => {
  32. this.btColor2 = '#ffd5d5d5';
  33. })
  34. .onBlur(() => {
  35. this.btColor2 = '#ff2787d9';
  36. })
  37. .id('testButton2')

  39. Divider()
  40. .vertical(false)
  41. .width('80%')
  42. .backgroundColor('#ff707070')
  43. .height(10)

  45. Button('FocusController.requestFocus')
  46. .width(200).height(70).fontColor(Color.White)
  47. .onClick(() => {
  48. this.getUIContext().getFocusController().requestFocus('testButton');
  49. })
  50. .backgroundColor('#ff2787d9')

  52. Button('focusControl.requestFocus')
  53. .width(200).height(70).fontColor(Color.White)
  54. .onClick(() => {
  55. focusControl.requestFocus('testButton2');
  56. })
  57. .backgroundColor('#ff2787d9')

  59. Button('clearFocus')
  60. .width(200).height(70).fontColor(Color.White)
  61. .onClick(() => {
  62. this.getUIContext().getFocusController().clearFocus();
  63. })
  64. .backgroundColor('#ff2787d9')
  65. }
  66. }
  67. .width('100%')
  68. .height('100%')
  69. }
  70. // ...
  71. }
  72. }
  ```

  [FocusController.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/FocusController.ets#L16-L93)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/wbL4hcKMTIOauqPvvnoGOQ/zh-cn_image_0000002583438021.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=CD157B722EECF42A6067EF4321F75053B74C9B2808960ADF6E70F040FC4E1BFE)

上述示例包含以下3步：

* 点击FocusController.requestFocus按钮，第一个Button获焦。
* 点击focusControl.requestFocus按钮，第二个Button获焦。
* 点击clearFocus按钮，第二个Button失焦。

## 自定义组件走焦顺序

### nextFocus自定义走焦

```
1. nextFocus(nextStep: Optional<FocusMovement>): T
```

若存在配置了nextFocus的组件，则走焦只会按照设置的nextFocus走焦顺序走焦，没有设置自定义走焦或者设置自定义走焦的组件或容器不存在时，仍进行默认走焦规则。

说明

* 该能力从API version 18开始支持。

```
1. @Entry
2. @Component
3. export struct NextFocusExample {
4. build() {
5. NavDestination() {
6. Column({ space: 30 }) {
7. Row().height('30%')
8. Row({ space: 10 }) {
9. Button('A')
10. .id('A')
11. .nextFocus({ forward: 'F', backward: 'C', down: 'B' })
12. Button('B')
13. .id('B')
14. .nextFocus({ down: 'C' })
15. Button('C')
16. .id('C')
17. }

19. Column({ space: 10 }) {
20. Button('D')
21. .id('D')
22. Button('E')
23. .id('E')
24. .nextFocus({
25. forward: 'A',
26. backward: 'M',
27. up: 'E',
28. right: 'F'
29. })
30. }

32. Row({ space: 10 }) {
33. Button('F')
34. .id('F')
35. .nextFocus({ forward: 'B', down: 'A' })
36. }
37. }.width('100%')
38. }
39. // ...
40. }
41. }
```

[NextFocus.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/NextFocus.ets#L16-L62)

Tab键走焦：未配置nextFocus时，Tab键走焦顺序为A->B->C->D->E->F。配置nextFocus之后，Tab键走焦顺序为A->F->B->C->D->E->A。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/sEwSGOQARKOG0w9Df0R73w/zh-cn_image_0000002552957976.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=8286504212E3F1E333E76BD0BBDEFB4F80BD2034D893DA1CC119CCABEB8D72BA)

方向键走焦（以方向下键为例）：未配置nextFocus时，按下Tab键激活焦点态之后，按方向下键走焦顺序为A->D->E->F。配置nextFocus之后，按下Tab键激活焦点态之后，按方向下键走焦顺序为A->B->C->D->E->F->A。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/P3EJ2RAJSKadjNXqSg0Pwg/zh-cn_image_0000002583477977.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=46E2589B92465032DDABFF905CFC4BF7A92B3BC41B06B6CB8D7B78BA6DAF3C99)

### tabIndex自定义走焦

```
1. tabIndex(index: number)
```

tabIndex自定义组件Tab键走焦顺序。

若存在配置了tabIndex大于0的组件，则Tab键走焦只会在tabIndex大于0的组件内，按照tabIndex的值从小到大并循环依次走焦。若没有配置tabIndex大于0的组件，则tabIndex等于0的组件按照组件预设的走焦规则走焦。

说明

不能同时设置tabIndex与focusScopeId属性。

不建议在[层级页面](arkts-common-events-focus-event.md#基础概念)中通过单独设置组件的tabIndex属性为负数来控制获焦能力，可以使用focusable属性代替。

tabIndex只能够自定义Tab键走焦，若想同时自定义方向键等走焦能力，建议使用[nextfocus](arkts-common-events-focus-event.md#nextfocus自定义走焦)。

```
1. @Entry
2. @Component
3. export struct TabIndexExample {
4. build() {
5. NavDestination() {
6. Column() {
7. Button('Button1')
8. .width(140)
9. .height(45)
10. .margin(5)
11. Button('Focus Button1')
12. .width(140)
13. .height(45)
14. .margin(5).tabIndex(1)
15. Button('Button2')
16. .width(140)
17. .height(45)
18. .margin(5)
19. Button('Focus Button2')
20. .width(140)
21. .height(45)
22. .margin(5).tabIndex(2)
23. }.width('100%')
24. }
25. // ...
26. }
27. }
```

[TabIndex.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/TabIndex.ets#L16-L48)

Tab键走焦：只在配置TabIndex的节点间循环走焦。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/sx4bN4KrT56xcp2jqvNKgw/zh-cn_image_0000002552798328.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=1FD6174538F49E331DE44ECB0C8CD37C2A2E52A15835F6739B2FD0BFAEF0B0C1)

tabIndex配置在容器上时，如果容器中的所有组件都没有获焦过，则走到第一个可获焦组件上，否则会走到上次获焦的节点。

```
1. @Entry
2. @Component
3. export struct TabIndexFocusExample {
4. build() {
5. NavDestination() {
6. Column() {
7. Button('Button1')
8. .width(140)
9. .height(45)
10. .margin(5).tabIndex(1)
11. Column() {
12. Button('Button2')
13. .width(140)
14. .height(45)
15. .margin(5)
16. Button('Button3')
17. .width(140)
18. .height(45)
19. .margin(5)
20. }.tabIndex(2)
21. }.width('100%')
22. }
23. // ...
24. }
25. }
```

[TabIndexFocus.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/TabIndexFocus.ets#L16-L46)

Tab键走焦：tabIndex配置在容器上。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/aGlbw3PbSp-n4Shzel4x9g/zh-cn_image_0000002583438023.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=EFDEAA8E7D8F6B14252C93B1FEBF45835E5EC2226B54255025CBE627E91FF6B6)

上述示例包含以下3步：

* 使用Tab键走焦，焦点在Button1和Button2之间循环走焦（tabIndex配置在Button2和Button3的父组件上）。
* 在走焦至Button2时，使用方向下键，将焦点转移至Button3上。
* 使用Tab键走焦，焦点在Button1和Button3之间循环走焦。

## 焦点组与获焦优先级

```
1. focusScopePriority(scopeId: string, priority?: FocusPriority)
```

设置当前组件在指定容器内获焦的优先级。需要配合focusScopeId一起使用。

```
1. focusScopeId(id: string, isGroup?: boolean)
```

设置当前容器组件的id标识，设置当前容器组件是否为焦点组。焦点组与tabIndex不能混用。

```
1. @Entry
2. @Component
3. export struct FocusScopePriority {
4. @State inputValue: string = '';

6. build() {
7. NavDestination() {
8. Column({ space: 12 }) {

10. Scroll() {
11. Row({ space: 20 }) {
12. Column({ space: 20 }) {  // 标记为Column1
13. Column({ space: 5 }) {
14. Button('Group1')
15. .width(165)
16. .height(40)
17. .fontColor(Color.White)
18. Row({ space: 5 }) {
19. Button()
20. .width(80)
21. .height(40)
22. .fontColor(Color.White)
23. Button()
24. .width(80)
25. .height(40)
26. .fontColor(Color.White)
27. }
28. Row({ space: 5 }) {
29. Button()
30. .width(80)
31. .height(40)
32. .fontColor(Color.White)
33. Button()
34. .width(80)
35. .height(40)
36. .fontColor(Color.White)
37. }
38. }.borderWidth(2).borderColor(Color.Red).borderStyle(BorderStyle.Dashed)
39. Column({ space: 5 }) {
40. Button('Group2')
41. .width(165)
42. .height(40)
43. .fontColor(Color.White)
44. Row({ space: 5 }) {
45. Button()
46. .width(80)
47. .height(40)
48. .fontColor(Color.White)
49. Button()
50. .width(80)
51. .height(40)
52. .fontColor(Color.White)
53. .focusScopePriority('ColumnScope1', FocusPriority.PRIOR)  // Column1首次获焦时获焦
54. }
55. Row({ space: 5 }) {
56. Button()
57. .width(80)
58. .height(40)
59. .fontColor(Color.White)
60. Button()
61. .width(80)
62. .height(40)
63. .fontColor(Color.White)
64. }
65. }.borderWidth(2).borderColor(Color.Green).borderStyle(BorderStyle.Dashed)
66. }
67. .focusScopeId('ColumnScope1')
68. Column({ space: 5 }) {  // 标记为Column2
69. TextInput({placeholder: 'input', text: this.inputValue})
70. .onChange((value: string) => {
71. this.inputValue = value;
72. })
73. .width(156)
74. Button('Group3')
75. .width(165)
76. .height(40)
77. .fontColor(Color.White)
78. Row({ space: 5 }) {
79. Button()
80. .width(80)
81. .height(40)
82. .fontColor(Color.White)
83. Button()
84. .width(80)
85. .height(40)
86. .fontColor(Color.White)
87. }
88. Button()
89. .width(165)
90. .height(40)
91. .fontColor(Color.White)
92. .focusScopePriority('ColumnScope2', FocusPriority.PREVIOUS)  // Column2获焦时获焦
93. Row({ space: 5 }) {
94. Button()
95. .width(80)
96. .height(40)
97. .fontColor(Color.White)
98. Button()
99. .width(80)
100. .height(40)
101. .fontColor(Color.White)
102. }
103. Button()
104. .width(165)
105. .height(40)
106. .fontColor(Color.White)
107. Row({ space: 5 }) {
108. Button()
109. .width(80)
110. .height(40)
111. .fontColor(Color.White)
112. Button()
113. .width(80)
114. .height(40)
115. .fontColor(Color.White)
116. }
117. }.borderWidth(2).borderColor(Color.Orange).borderStyle(BorderStyle.Dashed)
118. .focusScopeId('ColumnScope2', true)  // Column2为焦点组
119. }.alignItems(VerticalAlign.Top)
120. }

122. }
123. .width('100%')
124. .height('100%')
125. .padding({ left: 12, right: 12 })
126. }
127. // ...
128. }
129. }
```

[FocusScopePriority.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/FocusScopePriority.ets#L16-L150)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/pJYjenSqRKmqqsYsgLGdyg/zh-cn_image_0000002552957978.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=05B52FB5887B805DFE6BB2033F83EC0EBEEF03D5734F4AC49A2AE27C60D73E15)

上述示例包含以下2步：

* input方框内设置了焦点组，因此按下Tab键后焦点会快速从input中走出去，而按下方向键后可以在input内走焦。
* 左侧的两个Column没有设置焦点组，因此只能通过Tab键一个一个地走焦。

在API version 14，焦点组新增参数arrowStepOut，用于设置能否使用方向键走焦出当前焦点组。

```
1. focusScopeId(id: string, isGroup?: boolean, arrowStepOut?: boolean)
```

```
1. @Entry
2. @Component
3. export struct FocusScopeIdExample {
4. build() {
5. NavDestination() {
6. Column({ space: 20 }) {
7. Column() {
8. Button('Group1')
9. .width(165)
10. .height(40)
11. .margin(5)
12. .fontColor(Color.White)
13. Row({ space: 5 }) {
14. Button('Button1')
15. .width(80)
16. .height(40)
17. .margin(5)
18. .fontColor(Color.White)
19. Button('Button2')
20. .width(80)
21. .height(40)
22. .margin(5)
23. .fontColor(Color.White)
24. }
25. }.focusScopeId('1', true, true)
26. .borderWidth(2).borderColor(Color.Red).borderStyle(BorderStyle.Dashed)

28. TextInput()
29. Column() {
30. Button('Group2')
31. .width(165)
32. .height(40)
33. .margin(5)
34. .fontColor(Color.White)
35. Row({ space: 5 }) {
36. Button('Button3')
37. .width(80)
38. .height(40)
39. .margin(5)
40. .fontColor(Color.White)
41. Button('Button4')
42. .width(80)
43. .height(40)
44. .margin(5)
45. .fontColor(Color.White)
46. }
47. }.focusScopeId('2', true, false)
48. .borderWidth(2).borderColor(Color.Green).borderStyle(BorderStyle.Dashed)

50. TextInput()
51. }.width('100%')
52. }
53. // ...
54. }
55. }
```

[FocusScopeId.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/FocusScopeId.ets#L16-L76)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/b_FkcSfXQRqtFEBhr1MsHw/zh-cn_image_0000002583477979.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=272995F92A674AB74001BD66C873B16575133C3E85894CEE3E06D8BC23127C43)

上述示例包含以下3步：

* Group1和Group2设置焦点组，因此按下Tab键后焦点会快速从Group1和Group2的方框内走出。
* Group1设置焦点组时，允许使用方向键走焦出当前焦点组。在Group1方框内走焦时，使用方向键可以走焦至input输入框。
* Group2设置焦点组时，不允许使用方向键走焦出当前焦点组。在Group2方框内走焦时，使用方向键无法走焦至input输入框。

说明

TextInput组件本身对方向键存在独有处理，因此无法使用方向键直接走出TextInput组件。

## 焦点与按键事件

当组件获焦且存在点击事件（onClick）或单指单击事件（TapGesture）时，回车和空格会触发对应的事件回调。

说明

* 点击事件（onClick）或单指单击事件（TapGesture）在回车、空格触发对应事件回调时，默认不冒泡传递，即父组件对应[按键事件](../harmonyos-references/ts-universal-events-key.md)不会被同步触发。
* 按键事件（onKeyEvent）默认冒泡传递，即同时会触发父组件的按键事件回调。
* 组件同时存在点击事件（onClick）和按键事件（onKeyEvent），在回车、空格触发时，两者都会响应。
* 从API version 18开始，获焦组件只有在焦点激活态时才会响应点击事件（onClick）。

```
1. @Entry
2. @Component
3. export struct FocusOnclickExample {
4. @State count: number = 0;
5. @State name: string = 'Button';

7. build() {
8. NavDestination() {
9. Column() {
10. Button(this.name)
11. .fontSize(30)
12. .onClick(() => {
13. this.count++;
14. if (this.count % 2 === 0) {
15. this.name = 'count is even number';
16. } else {
17. this.name = 'count is odd number';
18. }
19. }).height(60)
20. }.height('100%').width('100%').justifyContent(FlexAlign.Center)
21. }
22. // ...
23. }
24. }
```

[FocusOnClick.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/EventProject/entry/src/main/ets/pages/focus/FocusOnClick.ets#L16-L45)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/mVgE4TvFT9Wt-fjQuhWaag/zh-cn_image_0000002552798330.gif?HW-CC-KV=V1&HW-CC-Date=20260427T233953Z&HW-CC-Expire=86400&HW-CC-Sign=363ED00DEA0E7FA2532E3C0391A1F3EFB66AB87C350B80F62AE6531E1FAFE080)

## 组件获焦能力说明

**表1** 基础组件获焦能力

| 基础组件 | 是否有获焦能力 | focusable默认值 |
| --- | --- | --- |
| [AlphabetIndexer](../harmonyos-references/ts-container-alphabet-indexer.md) | 是 | true |
| [Blank](../harmonyos-references/ts-basic-components-blank.md) | 否 | false |
| [Button](../harmonyos-references/ts-basic-components-button.md) | 是 | true |
| [CalendarPicker](../harmonyos-references/ts-basic-components-calendarpicker.md) | 是 | true |
| [Canvas](../harmonyos-references/ts-components-canvas-canvas.md) | 否 | false |
| [Checkbox](../harmonyos-references/ts-basic-components-checkbox.md) | 是 | true |
| [CheckboxGroup](../harmonyos-references/ts-basic-components-checkboxgroup.md) | 是 | true |
| [Circle](../harmonyos-references/ts-drawing-components-circle.md) | 否 | false |
| [Component3D](../harmonyos-references/ts-basic-components-component3d.md) | 否 | false |
| [ContainerSpan](../harmonyos-references/ts-basic-components-containerspan.md) | 否 | false |
| [DataPanel](../harmonyos-references/ts-basic-components-datapanel.md) | 是 | false |
| [DatePicker](../harmonyos-references/ts-basic-components-datepicker.md) | 是 | true |
| [Divider](../harmonyos-references/ts-basic-components-divider.md) | 是 | false |
| [Ellipse](../harmonyos-references/ts-drawing-components-ellipse.md) | 否 | false |
| [Gauge](../harmonyos-references/ts-basic-components-gauge.md) | 是 | false |
| [Image](../harmonyos-references/ts-basic-components-image.md) | 是 | false |
| [ImageAnimator](../harmonyos-references/ts-basic-components-imageanimator.md) | 否 | false |
| [ImageSpan](../harmonyos-references/ts-basic-components-imagespan.md) | 否 | false |
| [Indicator](../harmonyos-references/ts-swiper-components-indicator.md) | 是 | true |
| [Line](../harmonyos-references/ts-drawing-components-line.md) | 否 | false |
| [LoadingProgress](../harmonyos-references/ts-basic-components-loadingprogress.md) | 是 | true |
| [Marquee](../harmonyos-references/ts-basic-components-marquee.md) | 否 | false |
| [Menu](../harmonyos-references/ts-basic-components-menu.md) | 是 | true |
| [MenuItem](../harmonyos-references/ts-basic-components-menuitem.md) | 是 | true |
| [MenuItemGroup](../harmonyos-references/ts-basic-components-menuitemgroup.md) | 否 | false |
| [MultiNavigation](../harmonyos-references/ohos-arkui-advanced-multinavigation.md) | 否 | false |
| [Navigation](../harmonyos-references/ts-basic-components-navigation.md) | 是 | true |
| [NavRouter](../harmonyos-references/ts-basic-components-navrouter.md) | 否 | false |
| [NavDestination](../harmonyos-references/ts-basic-components-navdestination.md) | 是 | true |
| [Path](../harmonyos-references/ts-drawing-components-path.md) | 否 | false |
| [PatternLock](../harmonyos-references/ts-basic-components-patternlock.md) | 是 | true |
| [Polygon](../harmonyos-references/ts-drawing-components-polygon.md) | 否 | false |
| [Polyline](../harmonyos-references/ts-drawing-components-polyline.md) | 否 | false |
| [Progress](../harmonyos-references/ts-basic-components-progress.md) | 是 | true |
| [QRCode](../harmonyos-references/ts-basic-components-qrcode.md) | 是 | true |
| [Radio](../harmonyos-references/ts-basic-components-radio.md) | 是 | true |
| [Rating](../harmonyos-references/ts-basic-components-rating.md) | 是 | true |
| [Rect](../harmonyos-references/ts-drawing-components-rect.md) | 否 | false |
| [RichEditor](../harmonyos-references/ts-basic-components-richeditor.md) | 是 | true |
| [RichText](../harmonyos-references/ts-basic-components-richtext.md) | 否 | false |
| [ScrollBar](../harmonyos-references/ts-basic-components-scrollbar.md) | 否 | false |
| [Search](../harmonyos-references/ts-basic-components-search.md) | 是 | true |
| [Select](../harmonyos-references/ts-basic-components-select.md) | 是 | true |
| [Shape](../harmonyos-references/ts-drawing-components-shape.md) | 否 | false |
| [Slider](../harmonyos-references/ts-basic-components-slider.md) | 是 | true |
| [Span](../harmonyos-references/ts-basic-components-span.md) | 否 | false |
| [Stepper](../harmonyos-references/ts-basic-components-stepper.md) | 是 | true |
| [StepperItem](../harmonyos-references/ts-basic-components-stepperitem.md) | 是 | true |
| [SymbolSpan](../harmonyos-references/ts-basic-components-symbolspan.md) | 否 | false |
| [SymbolGlyph](../harmonyos-references/ts-basic-components-symbolglyph.md) | 否 | false |
| [Text](../harmonyos-references/ts-basic-components-text.md) | 是 | false |
| [TextArea](../harmonyos-references/ts-basic-components-textarea.md) | 是 | true |
| [TextClock](../harmonyos-references/ts-basic-components-textclock.md) | 否 | false |
| [TextInput](../harmonyos-references/ts-basic-components-textinput.md) | 是 | true |
| [TextPicker](../harmonyos-references/ts-basic-components-textpicker.md) | 是 | true |
| [TextTimer](../harmonyos-references/ts-basic-components-texttimer.md) | 否 | false |
| [TimePicker](../harmonyos-references/ts-basic-components-timepicker.md) | 否 | false |
| [Toggle](../harmonyos-references/ts-basic-components-toggle.md) | 是 | true |
| [XComponent](../harmonyos-references/ts-basic-components-xcomponent.md) | 是 | false |

**表2** 容器组件获焦能力

| 容器组件 | 是否可获焦 | focusable默认值 |
| --- | --- | --- |
| [Badge](../harmonyos-references/ts-container-badge.md) | 否 | false |
| [Column](../harmonyos-references/ts-container-column.md) | 是 | true |
| [ColumnSplit](../harmonyos-references/ts-container-columnsplit.md) | 是 | true |
| [Counter](../harmonyos-references/ts-container-counter.md) | 是 | false |
| [EmbeddedComponent](../harmonyos-references/ts-container-embedded-component.md) | 否 | false |
| [Flex](../harmonyos-references/ts-container-flex.md) | 是 | true |
| [FlowItem](../harmonyos-references/ts-container-flowitem.md) | 是 | true |
| [FolderStack](../harmonyos-references/ts-container-folderstack.md) | 是 | true |
| [FormLink](../harmonyos-references/ts-container-formlink.md) | 否 | false |
| [GridCol](../harmonyos-references/ts-container-gridcol.md) | 是 | true |
| [GridRow](../harmonyos-references/ts-container-gridrow.md) | 是 | true |
| [Grid](../harmonyos-references/ts-container-grid.md) | 是 | true |
| [GridItem](../harmonyos-references/ts-container-griditem.md) | 是 | true |
| [Hyperlink](../harmonyos-references/ts-container-hyperlink.md) | 是 | true |
| [LazyVGridLayout](../harmonyos-references/ts-container-lazyvgridlayout.md) | 否 | false |
| [List](../harmonyos-references/ts-container-list.md) | 是 | true |
| [ListItem](../harmonyos-references/ts-container-listitem.md) | 是 | true |
| [ListItemGroup](../harmonyos-references/ts-container-listitemgroup.md) | 是 | true |
| [Navigator](../harmonyos-references/ts-container-navigator.md) | 是 | true |
| [Refresh](../harmonyos-references/ts-container-refresh.md) | 是 | true |
| [RelativeContainer](../harmonyos-references/ts-container-relativecontainer.md) | 否 | false |
| [Row](../harmonyos-references/ts-container-row.md) | 是 | true |
| [RowSplit](../harmonyos-references/ts-container-rowsplit.md) | 是 | true |
| [Scroll](../harmonyos-references/ts-container-scroll.md) | 是 | true |
| [SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md) | 是 | true |
| [Stack](../harmonyos-references/ts-container-stack.md) | 是 | true |
| [Swiper](../harmonyos-references/ts-container-swiper.md) | 是 | true |
| [Tabs](../harmonyos-references/ts-container-tabs.md) | 是 | true |
| [TabContent](../harmonyos-references/ts-container-tabcontent.md) | 否 | false |
| [WaterFlow](../harmonyos-references/ts-container-waterflow.md) | 否 | false |
| [WithTheme](../harmonyos-references/ts-container-with-theme.md) | 是 | true |

**表3** 媒体组件获焦能力

| 媒体组件 | 是否可获焦 | focusable默认值 |
| --- | --- | --- |
| [Video](../harmonyos-references/ts-media-components-video.md) | 是 | true |
