---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-interaction-development-guide-gamepad
title: 支持游戏手柄输入事件
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 添加交互响应 > 输入设备与事件 > 支持游戏手柄输入事件
category: harmonyos-guides
scraped_at: 2026-04-29T13:28:06+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:285bba0b9d96fe538fa47c69f4d76b6d29e1feb1ec01faf541b37a2f51e1498e
---

从API version 15开始，支持使用游戏手柄作为输入设备。当用户使用手柄进行操作时，系统会识别其输入行为并上报为按键事件或焦点轴事件。开发者可以通过注册相应的回调函数，接收并处理这些事件，进而实现与游戏手柄的交互逻辑。

由于不同品牌和型号的手柄在硬件设计与信号输出上存在差异，其上报的键值和轴值可能并不统一，开发者在处理交互逻辑时应注意进行兼容性适配。

下面以常见的游戏手柄为例，说明其按键及操纵杆的常见映射关系：按键通常被映射为离散的键值（方向键有时也可映射为轴值），操纵杆则映射为连续的轴值。[KeyCode](../harmonyos-references/js-apis-keycode.md#keycode)针对游戏手柄提供了可支持的键值，[AxisModel](../harmonyos-references/ts-appendix-enums.md#axismodel15)则提供了可支持的轴值。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/gzSxZyLyRjqOKC-2jwdGRg/zh-cn_image_0000002558764444.png?HW-CC-KV=V1&HW-CC-Date=20260429T052804Z&HW-CC-Expire=86400&HW-CC-Sign=DEBF3ECBCC07F1F71A709C6C19C96B35E276E4E2FCBDC901DE4DA42DC2B0F487)

## 处理按键输入

游戏手柄的按键输入会被上报为按键事件，其具体处理机制可参考[按键事件数据流](arkts-interaction-development-guide-keyboard.md#按键事件数据流)。

为响应手柄的按键操作，开发者需要为组件绑定[onKeyEvent](../harmonyos-references/ts-universal-events-key.md#onkeyevent)接口回调。当组件处于获焦状态时，手柄的按键操作会触发此回调，进而处理按键输入的相应逻辑。相关示例如下：

```
1. import { KeyCode } from '@kit.InputKit';

3. @Entry
4. @Component
5. struct CommonKey {
6. build() {
7. Column() {
8. if (canIUse('SystemCapability.MultimodalInput.Input.Core')) {
9. Button('JoyStick')
10. .defaultFocus(true)
11. .onKeyEvent((event: KeyEvent) => {
12. if (event && event.type === KeyType.Down) {
13. switch (event.keyCode) {
14. case KeyCode.KEYCODE_BUTTON_SELECT:
15. console.info('trigger BUTTON_SELECT');
16. // 处理BUTTON_SELECT按键的输入逻辑
17. break;
18. case KeyCode.KEYCODE_BUTTON_START:
19. console.info('trigger BUTTON_START');
20. // 处理BUTTON_START按键的输入逻辑
21. break;
22. default:
23. console.info('trigger BUTTON_DEFAULT');
24. // 处理其他按键的输入逻辑
25. break;
26. }
27. }
28. })
29. }
30. }
31. .height('100%')
32. .width('100%')
33. .justifyContent(FlexAlign.Center)
34. }
35. }
```

[CommonKey.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InterAction/entry/src/main/ets/pages/gamepad/CommonKey.ets#L16-L52)

手柄的方向键输入在触发按键事件时也会带来默认的走焦效果。当开发者仅需利用方向键进行游戏内操作（如控制角色移动、旋转视角等）时，这种默认的走焦行为可能会干扰正常操作。使用焦点组可以解决这一问题。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/dNmm-3NgR5SmnYxk7gHQDA/zh-cn_image_0000002558604788.png?HW-CC-KV=V1&HW-CC-Date=20260429T052804Z&HW-CC-Expire=86400&HW-CC-Sign=D8DB534434D3433BEB3293DA55EF8D25035FF83418E0A560A5BBE2CA5864E883)

如图所示，在没有焦点组的情况下，方向键操作会使焦点在组件A、B、C之间自由移动。当使用焦点组容器将特定组件包裹起来时，就可以在该容器内部独立控制焦点行为。通过[focusScopeId](../harmonyos-references/ts-universal-attributes-focus.md#focusscopeid14)可以设置焦点组，并通过设置arrowStepOut参数为false来限制方向键走焦行为，以下示例展示了如何实现这一逻辑：

```
1. import { KeyCode } from '@kit.InputKit';

3. @Entry
4. @Component
5. struct DirectionKey {
6. build() {
7. Column({ space: 10 }) {
8. if (canIUse('SystemCapability.MultimodalInput.Input.Core')) {
9. Button('Button1')
10. Column() {
11. Button('JoyStick')
12. .defaultFocus(true)
13. .onKeyEvent((event: KeyEvent) => {
14. if (event && event.type === KeyType.Down) {
15. switch (event.keyCode) {
16. case KeyCode.KEYCODE_DPAD_UP:
17. case KeyCode.KEYCODE_DPAD_DOWN:
18. case KeyCode.KEYCODE_DPAD_LEFT:
19. case KeyCode.KEYCODE_DPAD_RIGHT:
20. console.info('trigger direction button');
21. break;
22. default:
23. console.info('trigger other button');
24. break;
25. }
26. }
27. })
28. }.focusScopeId('myGroup', true, false)

30. Button('Button2')
31. }
32. }
33. .height('100%')
34. .width('100%')
35. .justifyContent(FlexAlign.Center)
36. }
37. }
```

[DirectionKey.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InterAction/entry/src/main/ets/pages/gamepad/DirectionKey.ets#L16-L54)

此时使用方向键进行操作，焦点始终在JoyStick按钮处，方向键走焦行为被屏蔽。

## 处理操纵杆输入

游戏手柄的操纵杆输入会触发焦点轴事件，开发者可以为获焦的组件绑定[onFocusAxisEvent](../harmonyos-references/ts-universal-events-focus_axis.md#onfocusaxisevent)接口回调，处理相应的事件逻辑。示例如下：

```
1. @Entry
2. @Component
3. struct Joystick {
4. build() {
5. Column() {
6. Button('JoyStick')
7. .defaultFocus(true)
8. .onFocusAxisEvent((event: FocusAxisEvent) => {
9. let absX = event.axisMap.get(AxisModel.ABS_X);
10. let absY = event.axisMap.get(AxisModel.ABS_Y);
11. let absZ = event.axisMap.get(AxisModel.ABS_Z);
12. let absRZ = event.axisMap.get(AxisModel.ABS_RZ);
13. let absGas = event.axisMap.get(AxisModel.ABS_GAS);
14. let absBrake = event.axisMap.get(AxisModel.ABS_BRAKE);
15. // 处理操纵杆输入逻辑
16. console.info(`absX: ${absX}, absY: ${absY}, absZ: ${absZ}, absRZ: ${absRZ}, absGas: ${absGas}, absBrake: ${absBrake}`);
17. })
18. }
19. .height('100%')
20. .width('100%')
21. .justifyContent(FlexAlign.Center)
22. }
23. }
```

[Joystick.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InterAction/entry/src/main/ets/pages/gamepad/Joystick.ets#L16-L40)

## 示例

下面通过一个按键和操纵杆处理的综合示例来展示游戏手柄与应用的交互。

```
1. @Entry
2. @Component
3. struct GamepadSample {
4. @State keyValue: string = '';
5. @State keyEventType: string = '';
6. @State axisValue: string = '';

8. build() {
9. Column({ space: 10 }) {
10. Button('Button1')

12. Column() {
13. Button('JoyStick')
14. .defaultFocus(true)
15. .onFocusAxisEvent((event: FocusAxisEvent) => {
16. let absX = event.axisMap.get(AxisModel.ABS_X);
17. let absY = event.axisMap.get(AxisModel.ABS_Y);
18. let absZ = event.axisMap.get(AxisModel.ABS_Z);
19. let absRz = event.axisMap.get(AxisModel.ABS_RZ);
20. let absGas = event.axisMap.get(AxisModel.ABS_GAS);
21. let absBrake = event.axisMap.get(AxisModel.ABS_BRAKE);
22. let absHat0X = event.axisMap.get(AxisModel.ABS_HAT0X);
23. let absHat0Y = event.axisMap.get(AxisModel.ABS_HAT0Y);
24. this.axisValue =
25. 'absX: ' + absX + '\nabsY: ' + absY + '\nabsZ: ' + absZ + '\nabsRz: ' + absRz + '\nabsGas: ' + absGas +
26. '\nabsBrake: ' + absBrake + '\nabsHat0X: ' + absHat0X + '\nabsHat0Y: ' + absHat0Y;
27. })
28. .onKeyEvent((event: KeyEvent) => {
29. if (event && event.type === KeyType.Down) {
30. this.keyValue =
31. 'keyCode:' + event.keyCode + '\nkeyText:' + event.keyText + '\nintentionCode:' + event.intentionCode;
32. }
33. })
34. }.focusScopeId('myGroup', true, false)

36. Button('Button2')

38. Text('Axis value info: ').margin({ top: 10 })
39. Column() {
40. Text(this.axisValue).padding(15)
41. }.width('100%').alignItems(HorizontalAlign.Start).padding({ left: 40 })

43. Divider()

45. Text('Key value info: ').margin({ top: 10 })
46. Column() {
47. Text(this.keyValue).padding(15)
48. }.width('100%').alignItems(HorizontalAlign.Start).padding({ left: 40 })

50. }.height(300).width('100%').margin({ top: 30 })
51. }
52. }
```

[GamepadSample.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/ArkUISample/InterAction/entry/src/main/ets/pages/gamepad/GamepadSample.ets#L16-L69)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/ZpFBOOL1SrmCg7lx8iCexA/zh-cn_image_0000002589324313.gif?HW-CC-KV=V1&HW-CC-Date=20260429T052804Z&HW-CC-Expire=86400&HW-CC-Sign=3E2622484F93A287D6E4A132550A5BC58BDC9B7C562BD186D6330D371DB96F86)

运行示例，分别使用游戏手柄进行以下操作：

1. 按压手柄操纵杆，可以观察到焦点轴事件的轴值上报。
2. 按下手柄按键，可以观察到按键事件的键值上报。
3. 使用方向键进行走焦，可以观察到走焦行为被屏蔽。
