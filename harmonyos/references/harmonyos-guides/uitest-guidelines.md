---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/uitest-guidelines
title: UI测试框架使用指导
breadcrumb: 指南 > 应用测试 > 单元测试和UI测试 > 自动化测试框架使用指导 > UI测试框架使用指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:52+08:00
doc_updated_at: 2026-04-21
content_hash: sha256:7be4ce888fd7abb8da768da0143ea24441bb605a888b220a787b60aef7beebbd
---

## 概述

UI测试框架（UITest）为开发者提供UI界面查找和模拟操作能力，可覆盖UI自动化测试的关键场景，包括界面控件精准查找、UI交互操作（如点击、滑动、文本输入等）、外设行为模拟（如键盘输入、鼠标操作、触控板手势、手写笔动作等），助力开发者开发高效可靠的界面自动化测试用例。

## 功能全景

UITest支持采用ArkTS API与命令行两种方式，为界面自动化测试提供灵活高效的技术支撑，其中：

**ArkTS脚本开发能力：**

提供简洁易用的API接口，满足各类测试场景需求，支持点击、双击、长按、滑动等常用UI交互操作，助力开发者快速开发基于界面交互逻辑的自动化测试脚本。

**命令行测试能力：**

支持通过命令行直接实现多元化测试操作，包括获取当前界面截图、获取控件树、录制界面操作流程、便捷注入UI模拟事件等。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/b4jT_BDYRm2jYFQ0eMiKjg/zh-cn_image_0000002550617948.png?HW-CC-KV=V1&HW-CC-Date=20260427T235751Z&HW-CC-Expire=86400&HW-CC-Sign=30EBB245B32177776C1D69B6881C365B26F1A069A60A6662A6B15163E9B6799A)

UITest分为客户端和服务端。

**· 客户端：**

包含跨语言通信层、IPC模块等，主要功能为对外导出API，为UI测试框架启动提供入口。客户端由测试应用加载，运行在应用进程。其中，跨语言通信层主要进行接口导出、JSON序列化对象处理、上层ArkTS接口与底层C++接口的转换、参数解析和校验。此外，由于本模块涉及C++层对ArkTS层回调函数的调用，跨语言通信层同时负责ArkTS回调函数的管理和调用。

**· 服务端：**

以独立进程运行，通过IPC与客户端进行通信。服务端启动后，通过广播与客户端建立连接，通过IPC通信确保连接不断开。服务端监听客户端进程状态，实现按需启停。服务端负责UI测试框架核心逻辑的处理，主要分为以下两部分：

1. 框架运行通用能力：进行IPC消息处理、进程管理、C++接口和错误码的管理，包括接口调用监听等。
2. UI测试能力：解析无障碍节点构建页面控件树、控件匹配查找、操作事件构造、多模事件注入、UI事件监听、屏幕显示控制等。

## 使用ArkTS接口进行UI测试

本章节介绍UI测试框架ArkTS API的具体使用方法。

UI测试是在[单元测试](unittest-guidelines.md)基础上进行UITest接口调用，接口的详细定义与参数说明可参考[API文档](../harmonyos-references/js-apis-uitest.md)。

### UI测试示例

下面提供一个UI测试的简单示例，介绍如何在单元测试脚本基础上进行UI测试的增量开发，具体实现功能如下：

1. 调用[程序框架服务](../harmonyos-references/js-apis-inner-application-abilitydelegator.md)能力，启动目标被测应用，并确认应用运行状态。
2. 调用UI测试框架能力，页面中执行点击操作。
3. 通过[添加断言](unittest-guidelines.md#断言能力)，验证操作后当前页面的实际变化是否与预期结果一致。

开发步骤如下:

1. 在main > ets > pages文件夹下编写clickToAfter.ets页面代码，作为被测示例demo。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State message: string = 'Hello World';
   5. @State text: string = '';

   7. build() {
   8. Row() {
   9. Column() {
   10. Text(this.message)
   11. .fontSize(50)
   12. .fontWeight(FontWeight.Bold)
   13. Text('Next')
   14. .fontSize(50)
   15. .margin({ top: 20 })
   16. .fontWeight(FontWeight.Bold)
   17. .onClick((event?: ClickEvent) => {
   18. if (event) {
   19. this.text = 'after click';
   20. }
   21. })
   22. .width('100%')
   23. Text(this.text).margin(15)
   24. }
   25. }
   26. .height('100%')
   27. }
   28. }
   ```
2. 在ohosTest > ets > test文件夹下新建测试文件，并编写具体测试代码。

   ```
   1. import { describe, expect, it, Level } from '@ohos/hypium';
   2. // 导入测试依赖kit
   3. import { abilityDelegatorRegistry, Driver, ON } from '@kit.TestKit';
   4. import { UIAbility, Want } from '@kit.AbilityKit';

   6. const delegator: abilityDelegatorRegistry.AbilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();

   8. export default function abilityTest() {
   9. describe('ActsAbilityTest', () => {
   10. it('testUiExample', Level.LEVEL3, async (done: Function) => {
   11. // 初始化Driver对象
   12. const driver = Driver.create();
   13. const bundleName = abilityDelegatorRegistry.getArguments().bundleName;
   14. // 指定被测应用包名、ability名，请开发者替换为被测应用包名和ability名
   15. const want: Want = {
   16. bundleName: bundleName,
   17. abilityName: 'EntryAbility'
   18. }
   19. // 拉起被测应用
   20. await delegator.startAbility(want);
   21. // 等待应用拉起完成
   22. await driver.waitForIdle(4000, 5000);
   23. // 确认当前应用顶部Ability为指定的ability
   24. const ability: UIAbility = await delegator.getCurrentTopAbility();
   25. expect(ability.context.abilityInfo.name).assertEqual('EntryAbility');

   27. // 依据指定文本“Next”查找目标控件
   28. const next = await driver.findComponent(ON.text('Next'));
   29. // 点击目标控件
   30. await next.click();
   31. await driver.waitForIdle(4000, 5000);
   32. // 通过断言文本为“after click”的控件存在，确认操作后页面变化符合预期
   33. await driver.assertComponentExist(ON.text('after click'));
   34. await driver.pressBack();
   35. done();
   36. })
   37. })
   38. }
   ```

### 控件查找与操作

UITest支持[依据多种属性构造匹配器](../harmonyos-references/js-apis-uitest.md#on9)进行控件查找；支持查找当前页面符合匹配条件的单个或多个目标控件，并返回控件对象；支持在滚动组件内部进行滚动查找目标控件；支持[对控件对象进行操作或获取控件的属性信息](../harmonyos-references/js-apis-uitest.md#component9)。

如下给出控件查找与操作的示例，下面代码执行前请参考UI测试示例，实现对应的Index.ets页面代码。

```
1. import { describe, it, TestType } from '@ohos/hypium';
2. // 导入测试依赖kit
3. import { Component, Driver, ON, On } from '@kit.TestKit';

5. export default function abilityTest() {
6. describe('componentOperationTest', () => {
7. /**
8. * 查找类型为'Button'的控件，并进行控件点击操作
9. */
10. it('componentSearchAndOperation', TestType.FUNCTION, async () => {
11. let driver: Driver = Driver.create();
12. await driver.delayMs(1000);
13. let button: Component = await driver.findComponent(ON.type('Button'));
14. await button.click();
15. })

17. /**
18. * 利用相对位置查找控件，查找'Scroll'类型控件中文本内容为'123'的控件
19. */
20. it('relativePositioncomponentSearch', TestType.FUNCTION, async () => {
21. let driver: Driver = Driver.create();
22. let on: On = ON.text('123').within(ON.type('Scroll'));
23. let items: Array<Component> = await driver.findComponents(on);
24. })

26. /**
27. * 查找类型为'Image'的控件，并进行对其进行双指放大操作
28. */
29. it('componentPinch', TestType.FUNCTION, async () => {
30. let driver: Driver = Driver.create();
31. let image: Component = await driver.findComponent(ON.type('Image'));
32. await image.pinchOut(1.5);
33. })
34. })
35. }
```

### 模拟触摸屏手指操作

UITest支持模拟包括点击、双击、长按、滑动、拖拽、多指操作等事件。

如下给出触摸屏坐标级的手指操作模拟的示例，下面代码执行前请参考UI测试示例，实现对应的Index.ets页面代码。

```
1. import { describe, it, Level, Size, TestType } from '@ohos/hypium';
2. // 导入测试依赖kit
3. import { Driver, PointerMatrix, UiDirection } from '@kit.TestKit';

5. export default function abilityTest() {
6. describe('touchScreen_sample', () => {
7. /**
8. * 基于坐标的触摸屏手指操作
9. */
10. it('touchScreenOperation', TestType.FUNCTION, async () => {
11. let driver: Driver = Driver.create();
12. // 单击
13. await driver.click(100, 100);
14. // 指定屏幕id进行单击，从API version 20开始支持
15. await driver.clickAt({ x: 100, y: 100, displayId: 0 });
16. // 滑动
17. await driver.swipe(100, 100, 200, 200, 600);
18. // 指定屏幕id进行滑动，从API version 20开始支持
19. await driver.swipeBetween({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, 800);
20. // 抛滑
21. await driver.fling({ x: 100, y: 100 }, { x: 200, y: 200 }, 5, 600);
22. // 指定方向的抛滑
23. await driver.fling(UiDirection.DOWN, 10000);
24. // 拖拽
25. await driver.drag(100, 100, 200, 200, 600);
26. // 指定屏幕id和拖拽移动前的长按时间，从API version 20开始支持
27. await driver.dragBetween({ x: 100, y: 100, displayId: 0 }, { x: 1000, y: 1000, displayId: 0 }, 800, 1500);
28. // 多指操作，指定使用两根手指，每根手指基于两个坐标点滑动
29. let pointers: PointerMatrix = PointerMatrix.create(2, 2);
30. pointers.setPoint(0, 0, { x: 100, y: 100 });
31. pointers.setPoint(0, 1, { x: 200, y: 100 });
32. pointers.setPoint(1, 0, { x: 100, y: 200 });
33. pointers.setPoint(1, 1, { x: 200, y: 200 });
34. await driver.injectMultiPointerAction(pointers);
35. })
36. })
37. }
```

### 页面加载等待

在与页面进行交互后，可通过在指定时间内等待某控件的出现或等待页面空闲来判断页面跳转是否完成。

如下给出页面加载等待的示例，下面代码执行前请参考UI测试示例，实现对应的Index.ets页面代码。

```
1. import { describe, it, Level, Size, TestType } from '@ohos/hypium';
2. // 导入测试依赖kit
3. import { abilityDelegatorRegistry, Driver, ON } from '@kit.TestKit';

5. const delegator: abilityDelegatorRegistry.AbilityDelegator = abilityDelegatorRegistry.getAbilityDelegator();
6. // 指定被测应用包名、ability名，请开发者替换为被测应用包名和ability名
7. const bundleName: string = 'com.uitestScene.acts';
8. const abilityName: string = 'com.uitestScene.acts.MainAbility';

10. export default function abilityTest() {
11. describe('waitForComp_sample', () => {
12. it('testWaitForComponent_static', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3,
13. async (done: Function): Promise<void> => {
14. let driver = Driver.create();
15. // 拉起目标应用
16. await delegator.executeShellCommand(`aa start -b ${bundleName} -a ${abilityName}`).then(result => {
17. }).catch((err: Error) => {
18. done();
19. })
20. // 通过等待目标应用首页上的指定控件出现，判断应用拉起完成
21. let button = await driver.waitForComponent(ON.text('StartAbility Success!'), 1000);
22. })
23. })
24. }
```

### 模拟文本输入

UITest支持向指定坐标点或指定控件输入文本内容，同时支持[指定输入方式](../harmonyos-references/js-apis-uitest.md#inputtextmode20)：输入文本时是否以复制粘贴方式输入、是否以追加的方式进行输入。

如下给出文本输入的示例，包括基于控件的文本输入和基于坐标的文本输入两种方式。下面代码执行前请参考UI测试示例，实现对应的Index.ets页面代码。

```
1. import { describe, it, Level, Size, TestType } from '@ohos/hypium';
2. // 导入测试依赖kit
3. import { Driver, ON } from '@kit.TestKit';

5. export default function abilityTest() {
6. describe('inputTextTest', () => {
7. /**
8. * 基于控件的文本输入，调用接口会默认清空文本框中内容后输入指定文本
9. * 当输入文本中不包含中文、特殊字符，且文本长度不超过200字符时默认为逐字键入
10. */
11. it('componentInputText', TestType.FUNCTION, async () => {
12. let driver = Driver.create();
13. let input = await driver.findComponent(ON.type('TextInput'));
14. await input.inputText('abc');
15. })
16. /**
17. * 基于控件的文本输入，指定以复制粘贴方式注入输入指定文本
18. * 指定以追加方式输入，即在输入文本签不清空原有内容
19. */
20. it('componentInputTextAddition', TestType.FUNCTION, async () => {
21. let driver = Driver.create();
22. let input = await driver.findComponent(ON.type('TextInput'));
23. // 该接口从API version 20开始支持
24. await input.inputText('abc', { paste: true, addition: true });
25. })

27. /**
28. * 基于坐标的文本输入，点击指定位置使输入框获焦，并在光标处输入指定文本
29. * 当输入文本中不包含中文、特殊字符，且文本长度不超过200字符时默认为逐字键入
30. */
31. it('pointInputText', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
32. let driver = Driver.create();
33. let input = await driver.findComponent(ON.type('TextInput'));
34. let center = await input.getBoundsCenter();
35. await driver.inputText(center, 'abc');
36. })

38. /**
39. * 基于坐标的文本输入，指定以复制粘贴方式注入输入指定文本
40. * 指定以追加方式输入，即点击指定位置使输入框获焦后将光标移动至原有文本末尾后输入
41. */
42. it('pointInputTextAddition', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
43. let driver = Driver.create();
44. let input = await driver.findComponent(ON.type('TextInput'));
45. let center = await input.getBoundsCenter();
46. // 该接口从API version 20开始支持
47. await driver.inputText(center, '123', { paste: true, addition: true });
48. })

50. /**
51. * 基于坐标的文本输入，指定以复制粘贴方式注入输入指定文本
52. * 指定以追加方式输入，即点击指定位置使输入框获焦后将光标移动至原有文本末尾后输入
53. * 当输入内容包含中文或特殊字符时，仅支持以复制粘贴方式输入文本，'paste'字段不生效
54. */
55. it('pointInputTextChinese', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
56. let driver = Driver.create();
57. let input = await driver.findComponent(ON.type('TextInput'));
58. let center = await input.getBoundsCenter();
59. // 该接口从API version 20开始支持
60. await driver.inputText(center, '你好', { paste: false, addition: true });
61. })
62. })
63. }
```

### 截图

说明

1. 指定截图文件保存路径，路径需为当前应用的[沙箱路径](app-sandbox-directory.md)。
2. 测试HAP的[APL等级级别](app-permission-mgmt-overview.md#权限机制中的基本概念)为normal，对应要求使用用户级加密区的应用沙箱路径。且需指定将文件保存在应用在本设备上存放持久化数据的子目录。

如下给出屏幕截图的示例，指定屏幕id和截取屏幕区域，并将截图保存到指定路径下。下面代码执行前请参考UI测试示例，实现对应的Index.ets页面代码。多屏场景下，期望对指定屏幕做截图操作时，可以调用display模块的接口[获取Display对象](screenproperty-guideline.md#获取display对象)，实现[屏幕相关属性获取](screenproperty-guideline.md#获取屏幕相关属性)。

```
1. import { describe, it, Level, Size, TestType } from '@ohos/hypium';
2. // 导入测试依赖kit
3. import { Driver } from '@kit.TestKit';
4. import { display } from '@kit.ArkUI';

6. export default function abilityTest() {
7. describe('screenCap_sample', () => {
8. /**
9. * 截取指定区域的屏幕，并保存到指定路径
10. */
11. it('screenCapture', TestType.FUNCTION, async () => {
12. let driver = Driver.create();
13. // 应用沙箱路径，el2为用户级加密区，base为应用在本设备上存放持久化数据的子目录
14. // 请开发者使用时替换为实际的路径
15. let savePath = '/data/storage/el2/base/cache/1.png';
16. let res = await driver.screenCapture(savePath, {
17. left: 0,
18. top: 0,
19. right: 100,
20. bottom: 100
21. });
22. })

24. /**
25. * 截取指定屏幕id的屏幕全屏，并保存到指定路径
26. */
27. it('screenCapWithId', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
28. let driver = Driver.create();
29. // 获取默认屏幕对象
30. let disPlay = display.getDefaultDisplaySync();
31. let savePath = '/data/storage/el2/base/cache/1.png';
32. // 从API version 20开始支持
33. let res = await driver.screenCap(savePath, disPlay.id); // 获取默认屏幕ID属性
34. })
35. })
36. }
```

### UI事件监听

如下给出UI界面事件的监听的示例，设置监听回调函数，监听toast、dialog等控件的出现，等待事件发生后进行下一步操作。下面代码执行前请参考UI测试示例，实现对应的Index.ets页面代码。

```
1. import { describe, it, TestType } from '@ohos/hypium';
2. // 导入测试依赖kit
3. import { Driver, UIElementInfo } from '@kit.TestKit';

5. export default function abilityTest() {
6. describe('eventObserver_sample', () => {
7. // 监听Toast控件出现
8. it('toastObserver', TestType.FUNCTION, async () => {
9. let driver = Driver.create();
10. let observer = driver.createUIEventObserver();
11. let callback = (uiElementInfo: UIElementInfo) => {
12. let bundleName = uiElementInfo.bundleName;
13. let text = uiElementInfo.text;
14. let type = uiElementInfo.type;
15. }
16. observer.once('toastShow', callback);
17. })
18. })
19. }
```

### 模拟键鼠操作

如下给出键鼠模拟操作，包括键盘按键、组合键输入操作的示例，包括鼠标点击、移动、拖拽操作和键鼠组合操作等。下面代码执行前请参考UI测试示例，实现对应的Index.ets页面代码。

```
1. import { describe, it, Level, Size, TestType } from '@ohos/hypium';
2. // 导入测试依赖kit
3. import { Driver, MouseButton } from '@kit.TestKit';
4. import { KeyCode } from '@kit.InputKit';

6. export default function abilityTest() {
7. describe('mouseAndKey_sample', () => {
8. // 模拟键盘按键输入、组合键输入
9. it('keyBoardOperation', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
10. let driver = Driver.create();
11. // 键盘按键输入（注入返回键）
12. await driver.triggerKey(KeyCode.KEYCODE_BACK);
13. // 键盘组合键输入（注入保存组合键）
14. await driver.triggerCombineKeys(KeyCode.KEYCODE_CTRL_LEFT, KeyCode.KEYCODE_S);
15. })

17. // 模拟鼠标左键单击、鼠标移动、鼠标拖拽操作
18. it('mouseOperation', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
19. let driver = Driver.create();
20. // 鼠标左键单击
21. await driver.mouseClick({ x: 100, y: 100 }, MouseButton.MOUSE_BUTTON_LEFT);
22. // 鼠标移动
23. await driver.mouseMoveTo({ x: 100, y: 100 });
24. // 鼠标拖拽
25. await driver.mouseDrag({ x: 100, y: 100 }, { x: 200, y: 200 }, 600);
26. })

28. // 模拟键盘、鼠标组合操作
29. it('combinedOperation', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
30. let driver = Driver.create();
31. // 按下左CTRL键，同时鼠标滚轮滚动
32. await driver.mouseScroll({ x: 100, y: 100 }, true, 30, KeyCode.KEYCODE_CTRL_LEFT);
33. // 按下左CTRL键，同时鼠标左键长按
34. await driver.mouseLongClick({ x: 100, y: 100 }, MouseButton.MOUSE_BUTTON_LEFT, KeyCode.KEYCODE_CTRL_LEFT);
35. })
36. })
37. }
```

### 窗口查找与操作

如下给出窗口查找和操作的示例，根据窗口属性查找窗口，并进行窗口最小化等操作。下面代码执行前请参考UI测试示例，实现对应的Index.ets页面代码。

```
1. import { describe, expect, it, TestType } from '@ohos/hypium';
2. // 导入测试依赖kit
3. import { Driver } from '@kit.TestKit';

5. // 设备不支持时的错误代码
6. const DeviceErrorCode = 17000005;

8. export default function abilityTest() {
9. describe('findWindowAndOp_sample', () => {
10. // 根据指定条件查找活跃窗口，并对其进行窗口最小化操作
11. it('windowSearchAndOperation', TestType.FUNCTION, async () => {
12. let driver = Driver.create();
13. try {
14. let window = await driver.findWindow({ active: true });
15. await window.minimize();
16. } catch (error) {
17. // 在不支持窗口操作的设备上调用minimize接口操作窗口时，将抛出17000005错误码
18. expect(error.code).assertEqual(DeviceErrorCode);
19. }
20. })
21. })
22. }
```

### 模拟触摸板操作

如下给出触摸板模拟操作的示例，触摸板三指上滑返回桌面，三指下滑恢复应用窗口。下面代码执行前请参考UI测试示例，实现对应的Index.ets页面代码。

```
1. import { describe, expect, it, Level, Size, TestType } from '@ohos/hypium';
2. // 导入测试依赖kit
3. import { Driver, UiDirection } from '@kit.TestKit';

5. // 设备不支持时的错误代码
6. const DeviceErrorCode = 17000005;

8. export default function abilityTest() {
9. describe('touchPadOp_sample', () => {
10. // PC/2in1场景，模拟触摸板三指上滑（界面返回桌面），三指下滑（界面恢复窗口）操作
11. it('touchPadOperation', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
12. let driver = Driver.create();
13. try {
14. // 触摸板三指上滑返回桌面
15. await driver.touchPadMultiFingerSwipe(3, UiDirection.UP);
16. // 触摸板三指下滑恢复窗口
17. await driver.touchPadMultiFingerSwipe(3, UiDirection.DOWN);
18. } catch (error) {
19. // 在不支持触摸板操作的设备上调用时，将抛出17000005错误码
20. expect(error.code).assertEqual(DeviceErrorCode);
21. }
22. })
23. })
24. }
```

### 模拟手写笔操作

如下给出手写笔模拟操作，包括点击、滑动等操作的示例，支持设置操作时的压力值大小。下面代码执行前请参考UI测试示例，实现对应的Index.ets页面代码。

```
1. import { describe, it, Level, Size, TestType } from '@ohos/hypium';
2. // 导入测试依赖kit
3. import { Driver } from '@kit.TestKit';

5. export default function abilityTest() {
6. describe('penOp_sample', () => {
7. // 模拟手写笔单击、双击、长按、滑动操作
8. it('penOperation', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
9. let driver = Driver.create();
10. // 手写笔单击
11. await driver.penClick({ x: 100, y: 100 });
12. // 手写笔双击
13. await driver.penDoubleClick({ x: 100, y: 100 });
14. // 手写笔长按
15. await driver.penLongClick({ x: 100, y: 100 }, 0.5);
16. // 手写笔滑动
17. await driver.penSwipe({ x: 100, y: 100 }, { x: 100, y: 500 }, 600, 0.5);
18. })
19. })
20. }
```

### 模拟表冠操作

如下给出表冠模拟操作的示例，包括表冠的顺/逆时针旋转。下面代码执行前请参考UI测试示例，实现对应的Index.ets页面代码。

```
1. import { describe, expect, it, Level, Size, TestType } from '@ohos/hypium';
2. // 导入测试依赖kit
3. import { Driver } from '@kit.TestKit';

5. // 设备不支持时的错误代码
6. const CapabilityCode = 801;

8. export default function abilityTest() {
9. describe('watchOp_sample', () => {
10. // 手表场景，模拟表冠顺/逆时针旋转，从API version 20开始支持
11. it('crownRotate', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
12. let driver = Driver.create();
13. try {
14. // 顺时针旋转50格，旋转速度为30格/秒
15. await driver.crownRotate(50, 30);
16. // 逆时针旋转20格，旋转速度为30格/秒
17. await driver.crownRotate(-20, 30);
18. } catch (error) {
19. // driver.crownRotate接口仅在智能表设备上生效，其他设备调用时将抛出801错误码
20. expect(error.code).assertEqual(CapabilityCode);
21. }
22. })
23. })
24. }
```

### 屏幕显示操作

如下给出屏幕显示操作的示例，包括获取屏幕大小、分辨率等属性和屏幕唤醒、屏幕旋转等操作。下面代码执行前请参考UI测试示例，实现对应的Index.ets页面代码。

```
1. import { describe, it, Level, Size, TestType } from '@ohos/hypium';
2. // 导入测试依赖kit
3. import { DisplayRotation, Driver, Point } from '@kit.TestKit';

5. export default function abilityTest() {
6. describe('displayOp_sample', () => {
7. // 屏幕属性获取和屏幕操作
8. it('displayOperation', TestType.FUNCTION | Size.MEDIUMTEST | Level.LEVEL3, async () => {
9. let driver = Driver.create();
10. // 获取屏幕大小
11. let size: Point = await driver.getDisplaySize();
12. // 获取屏幕清晰度
13. let density: Point = await driver.getDisplayDensity();
14. // 唤醒屏幕
15. await driver.wakeUpDisplay();
16. // 屏幕顺时针旋转90度
17. await driver.setDisplayRotation(DisplayRotation.ROTATION_90);
18. })
19. })
20. }
```

## 基于命令行进行UI测试

在开发阶段，如果需要快速执行截图、界面操作录制、UI模拟操作注入、控件树获取等测试相关操作，可借助命令行实现，提升测试效率。

### 环境要求

根据hdc命令行工具指导，完成[环境准备](hdc.md#环境准备)。确保设备已成功连接，并执行hdc shell。

### 命令列表

| 命令 | 参数 | 说明 |
| --- | --- | --- |
| help | - | 显示UITest工具能够支持的命令信息。 |
| screenCap | [-p] [-d] | 截图。  各参数代表的含义请参考[获取截图](uitest-guidelines.md#获取截图)。 |
| dumpLayout | [-p] <-i | -a | -b | -w | -m | -d> | 获取控件树。  各参数代表的含义请参考[获取控件树](uitest-guidelines.md#获取控件树)。 |
| uiRecord | <record | read> | 录制界面操作。  **record** ：开始录制，将当前界面操作记录到'/data/local/tmp/record.csv'，结束录制操作使用Ctrl+C结束录制。  **read** ：读取并且打印录制数据。  各参数代表的含义请参考[录制界面操作](uitest-guidelines.md#录制界面操作)。 |
| uiInput | <help | click | doubleClick | longClick | fling | swipe | drag | dircFling | inputText | keyEvent | text> | 注入UI模拟操作。  各参数代表的含义请参考[注入UI模拟操作](uitest-guidelines.md#注入ui模拟操作)。 |
| --version | - | 获取当前UITest工具版本信息。 |
| start-daemon | - | 拉起UITest测试进程。 |

### 获取截图

| 参数 | 二级参数 | 说明 |
| --- | --- | --- |
| -p | <savePath> | 指定存储路径和文件名，只支持存放在'/data/local/tmp/'下。默认存储路径：'/data/local/tmp'，文件名：'时间戳 + .png'。 |
| -d | <displayId> | 多屏场景下，获取指定ID屏幕下的截图。  **说明：** 从API version 20开始支持该命令。 |

```
1. # 存储路径：/data/local/tmp，文件名：时间戳 + .png。
2. hdc shell uitest screenCap
3. # 指定存储路径和文件名，存放在/data/local/tmp/下。
4. hdc shell uitest screenCap -p /data/local/tmp/1.png
```

### 获取控件树

| 参数 | 二级参数 | 说明 |
| --- | --- | --- |
| -p | <savePath> | 指定存储路径和文件名，只支持存放在'/data/local/tmp/'下。默认存储路径：'/data/local/tmp'，文件名：'时间戳 + .json'。 |
| -i | - | 不过滤不可见控件，也不做窗口合并。 |
| -a | - | 保存控件的BackgroundColor、Content、FontColor、FontSize、extraAttrs属性数据。  **说明** ：默认不保存上述属性数据， **-a和-i不可同时使用。** |
| -b | <bundleName> | 获取指定包名对应目标窗口的控件树信息。 |
| -w | <windowId> | 获取指定ID目标窗口的控件树信息。  **说明:**  可通过hidumper工具[获取应用窗口信息](hidumper.md#获取应用窗口信息), 包含应用对应窗口的id。 |
| -m | <true|false> | 指定在获取控件树信息时是否合并窗口信息。true表示合并窗口信息，false表示不合并窗口信息，不设置时默认为true。 |
| -d | <displayId> | 多屏场景下，获取指定ID屏幕下的控件树。  **说明：**  1. 从API version 20开始支持该命令。  2. 可通过hidumper工具[获取应用窗口信息](hidumper.md#获取应用窗口信息)，包含应用对应窗口的DisplayId。 |

```
1. # 指定存储路径和文件名，存放在/data/local/tmp/下。
2. hdc shell uitest dumpLayout -p /data/local/tmp/1.json
```

### 录制界面操作

说明

录制过程中，需等待当前操作的识别结果在命令行输出后，再进行下一步操作。

**参数列表**

| 参数 | 二级参数 | 说明 |
| --- | --- | --- |
| -W | <true/false> | 录制过程中是否保存操作坐标对应的控件信息到/data/local/tmp/record.csv文件中。true表示保存控件信息，false表示仅记录坐标信息，不设置时默认为true。  **说明：** 从API version 20开始支持该命令。 |
| -l | - | 在每次操作后保存当前布局信息，文件保存路径：/data/local/tmp/layout\_录制启动时间戳\_操作序号.json。  **说明：** 从API version 20开始支持该命令。 |
| -c | <true/false> | 是否将录制到的操作事件信息打印到控制台，true表示打印，false表示打印，不设置时默认为true。  **说明：** 从API version 20开始支持该命令。 |

```
1. # 将当前界面操作记录到/data/local/tmp/record.csv，结束录制操作使用Ctrl+C结束录制。
2. hdc shell uitest uiRecord record
3. # 录制时仅记录操作的坐标，不匹配目标控件。
4. hdc shell uitest uiRecord record -W false
5. # 每次操作后，保存页面布局，文件保存路径：/data/local/tmp/layout_录制启动时间戳_操作序号.json。
6. hdc shell uitest uiRecord record -l
7. # 录制到的操作事件信息不打印到控制台。
8. hdc shell uitest uiRecord record -c false
9. # 读取并打印录制数据。
10. hdc shell uitest uiRecord read
```

录制数据中字段及含义如下。

```
1. {
2. "ABILITY": "com.ohos.launcher.MainAbility", // 被操作应用对应的Ability名称
3. "BUNDLE": "com.ohos.launcher", // 被操作应用对应的包名
4. "CENTER_X": "", // 预留字段，暂未使用
5. "CENTER_Y": "", // 预留字段，暂未使用
6. "EVENT_TYPE": "pointer", // 操作类型
7. "LENGTH": "0", // 总体步长
8. "OP_TYPE": "click", // 事件类型，当前支持点击、双击、长按、拖拽、滑动、抛滑动作录制
9. "VELO": "0.000000", // 离手速度
10. "direction.X": "0.000000",// 总体移动X方向
11. "direction.Y": "0.000000", // 总体移动Y方向
12. "duration": 33885000.0, // 手势操作持续时间
13. "fingerList": [{
14. "LENGTH": "0", // 总体步长
15. "MAX_VEL": "40000", // 最大速度
16. "VELO": "0.000000", // 离手速度
17. "W1_BOUNDS": "{"bottom":361,"left":37,"right":118,"top":280}", // 起点控件边界
18. "W1_HIER": "ROOT,3,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0", // 起点控件页面层级
19. "W1_ID": "", // 起点控件id
20. "W1_Text": "", // 起点控件text
21. "W1_Type": "Image", // 起点控件类型
22. "W2_BOUNDS": "{"bottom":361,"left":37,"right":118,"top":280}", // 终点控件边界
23. "W2_HIER": "ROOT,3,0,0,0,0,0,0,0,0,5,0,0,0,0,0,0,0", // 终点控件页面层级
24. "W2_ID": "", // 终点控件id
25. "W2_Text": "", // 终点控件text
26. "W2_Type": "Image", // 终点控件类型
27. "X2_POSI": "47", // 终点X
28. "X_POSI": "47", // 起点X
29. "Y2_POSI": "301", // 终点Y
30. "Y_POSI": "301", // 起点Y
31. "direction.X": "0.000000", // X方向移动量
32. "direction.Y": "0.000000" // Y方向移动量
33. }],
34. "fingerNumber": "1" // 手指数量
35. }
```

### 注入UI模拟操作

| 参数 | 说明 |
| --- | --- |
| help | uiInput命令相关帮助信息。 |
| click | 模拟单击操作。具体请参考下方**uiInput-click/doubleClick/longClick使用示例**。 |
| doubleClick | 模拟双击操作。具体请参考下方**uiInput click/doubleClick/longClick使用示例**。 |
| longClick | 模拟长按操作。具体请参考下方**uiInput click/doubleClick/longClick使用示例**。 |
| fling | 模拟快滑操作，即操作结束后页面存在惯性滚动。具体请参考下方**uiInput fling使用示例**。 |
| swipe | 模拟慢滑操作。具体请参考下方**uiInput swipe/drag使用示例**。 |
| drag | 模拟拖拽操作。具体请参考下方**uiInput swipe/drag使用示例**。 |
| dircFling | 模拟指定方向滑动操作。具体请参考下方**uiInput dircFling使用示例**。 |
| inputText | 指定坐标点，模拟输入框输入文本操作。具体请参考下方**uiInput inputText使用示例**。 |
| text | 无需指定坐标点，在当前获焦处，模拟输入框输入文本操作。具体请参考下方**uiInput text使用示例**。  **说明：** 从API version 18开始支持该命令。 |
| keyEvent | 模拟实体按键事件（如：键盘，电源键，返回上一级，返回桌面等），以及组合按键操作。具体请参考下方**uiInput keyEvent使用示例**。 |

* uiInput-click/doubleClick/longClick使用示例

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| point\_x | 是 | 点击x坐标点。 |
| point\_y | 是 | 点击y坐标点。 |

```
1. # 执行单击事件。
2. hdc shell uitest uiInput click 100 100

4. # 执行双击事件。
5. hdc shell uitest uiInput doubleClick 100 100

7. # 执行长按事件。
8. hdc shell uitest uiInput longClick 100 100
```

* uiInput fling使用示例

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| from\_x | 是 | 滑动起点x坐标。 |
| from\_y | 是 | 滑动起点y坐标。 |
| to\_x | 是 | 滑动终点x坐标。 |
| to\_y | 是 | 滑动终点y坐标。 |
| swipeVelocityPps\_ | 否 | 滑动速度，单位：px/s，取值范围：200-40000。  默认值：600。取值超出限定范围时，取默认值。 |
| stepLength\_ | 否 | 滑动步长，单位：px。默认值：滑动距离/50。  **说明：**  滑动距离根据入参给出的滑动起止坐标点计算得出。  **为实现更好的模拟效果，推荐参数缺省/使用默认值。** |

```
1. # 执行快滑操作，stepLength_缺省。
2. hdc shell uitest uiInput fling 10 10 200 200 500
```

* uiInput swipe/drag使用示例

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| from\_x | 是 | 滑动起点x坐标。 |
| from\_y | 是 | 滑动起点y坐标。 |
| to\_x | 是 | 滑动终点x坐标。 |
| to\_y | 是 | 滑动终点y坐标。 |
| swipeVelocityPps\_ | 否 | 滑动速度，单位：px/s，取值范围：200-40000。  默认值：600。取值超出限定范围时，取默认值。 |

```
1. # 执行慢滑操作。
2. hdc shell uitest uiInput swipe 10 10 200 200 500

4. # 执行拖拽操作。
5. hdc shell uitest uiInput drag 10 10 100 100 500
```

* uiInput dircFling使用示例

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| direction | 否 | 滑动方向，取值范围：[0,1,2,3]，默认值为0。  0代表向左滑动，1代表向右滑动，2代表向上滑动，3代表向下滑动。 |
| swipeVelocityPps\_ | 否 | 滑动速度，单位：px/s，取值范围：200-40000。  **默认值**: 600。取值超出限定范围时，取默认值。 |
| stepLength | 否 | 滑动步长，单位：px。  **默认值**： 如果滑动方向为0、1，默认值为屏幕宽度/200； 如果滑动方向为2、3，默认值为屏幕高度/200。为更好的模拟效果，推荐参数缺省/使用默认值。 |

```
1. # 执行左滑操作。
2. hdc shell uitest uiInput dircFling 0 500
3. # 执行向右滑动操作。
4. hdc shell uitest uiInput dircFling 1 600
5. # 执行向上滑动操作。
6. hdc shell uitest uiInput dircFling 2
7. # 执行向下滑动操作。
8. hdc shell uitest uiInput dircFling 3
```

* uiInput inputText使用示例

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| point\_x | 是 | 输入框x坐标点。 |
| point\_y | 是 | 输入框y坐标点。 |
| text | 是 | 输入文本内容。 |

```
1. # 执行输入框输入操作。
2. hdc shell uitest uiInput inputText 100 100 hello
```

* uiInput text使用示例

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| text | 是 | 输入文本内容。 |

```
1. # 无需输入坐标点，在当前获焦处，执行输入框输入操作。若当前获焦处不支持文本输入，则无实际效果。
2. hdc shell uitest uiInput text hello
```

* uiInput keyEvent使用示例

| 参数 | 必填 | 说明 |
| --- | --- | --- |
| keyID1 | 是 | 实体按键对应ID，取值范围：Back、Home、Power、或[KeyCode键码值](../harmonyos-references/js-apis-keycode.md#keycode)。  当取值为Back、Home或Power时，不支持输入组合键。  当前注入大写锁定键（KeyCode=2074）无效，请使用组合键实现大写字母输入。如“按键shift+按键V”输入大写字母V。 |
| keyID2 | 否 | 实体按键对应ID，取值范围：[KeyCode键码值](../harmonyos-references/js-apis-keycode.md#keycode)，默认值为空。 |
| keyID3 | 否 | 实体按键对应ID，取值范围：[KeyCode键码值](../harmonyos-references/js-apis-keycode.md#keycode)，默认值为空。 |

```
1. # 返回主页。
2. hdc shell uitest uiInput keyEvent Home
3. # 返回。
4. hdc shell uitest uiInput keyEvent Back
5. # 组合键粘贴。
6. hdc shell uitest uiInput keyEvent 2072 2038
7. # 输入小写字母v。
8. hdc shell uitest uiInput keyEvent 2038
9. # 输入大写字母V。
10. hdc shell uitest uiInput keyEvent 2047 2038
```

### 获取版本信息

```
1. hdc shell uitest --version
```

### 拉起UITest测试进程

说明

仅元能力aa test拉起的测试HAP才能调用Uitest的能力，且测试HAP的[APL等级级别](app-permission-mgmt-overview.md#权限机制中的基本概念)需为normal。

```
1. hdc shell uitest start-daemon
```

## 常见问题

### 失败日志有“uitest-api does not allow calling concurrently”错误信息

**问题描述**

UI测试用例执行失败，查看hilog日志发现日志中有“uitest-api does not allow calling concurrently”错误信息。

**可能原因**

1. 用例中UI测试框架提供异步接口没有增加await语法糖调用。
2. 多进程执行UI测试用例，导致拉起多个UITest进程，框架不支持多进程调用。

**解决方法**

1. 检查用例实现，异步接口增加await语法糖调用。
2. 避免多进程执行UI测试用例。

### 失败日志有“does not exist on current UI! Check if the UI has changed after you got the widget object”错误信息

**问题描述**

UI测试用例执行失败，查看hilog日志发现日志中有“does not exist on current UI! Check if the UI has changed after you got the widget object”错误信息。

**可能原因**

在用例中代码查找到目标控件后，设备界面发生了变化，导致查找到的控件丢失，无法进行下一步的模拟操作。

**解决方法**

重新执行UI测试用例，确保进行模拟操作时控件在界面中存在。

### 失败日志有“Cannot connect to AAMS, RET\_ERR\_CONNECTION\_EXIST”错误信息

**问题描述**

UI测试用例执行失败，查看hilog日志发现日志中有“Cannot connect to AAMS, RET\_ERR\_CONNECTION\_EXIST”错误信息。

**可能原因**

在用例执行的同时使用了其他依赖UI测试框架运行的测试工具。

**解决方法**

关闭依赖UI测试框架运行的测试工具或重启设备。
