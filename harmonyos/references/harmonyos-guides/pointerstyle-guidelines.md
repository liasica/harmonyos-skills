---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/pointerstyle-guidelines
title: 鼠标光标开发指导
breadcrumb: 指南 > 系统 > 基础功能 > Input Kit（多模输入服务） > 鼠标光标开发指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:44:31+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:abdf56d0b436d52cb678fbee9c79e6af1e2d1a3d69a46855bcb156f667ab1266
---

## 场景介绍

鼠标光标控制提供鼠标光标显示和隐藏、光标样式查询和设置的能力。使用场景例如：用户在全屏观看视频时，开发者可以控制鼠标光标的显示隐藏；当用户执行取色时，开发者可以将鼠标光标样式切换为取色器样式。

## 导入模块

```
1. import { pointer } from '@kit.InputKit';
```

## 接口说明

鼠标光标控制常用接口如下表所示，接口详细介绍请参见[@ohos.multimodalInput.pointer](../harmonyos-references/js-apis-pointer.md)。

| 接口名称 | 描述 |
| --- | --- |
| isPointerVisible(callback: AsyncCallback<boolean>): void | 获取鼠标光标显示或隐藏状态。 |
| setPointerVisible(visible: boolean, callback: AsyncCallback<void>): void | 设置鼠标光标显示或隐藏状态，该接口会影响全局鼠标光标的显示状态。 |
| setPointerStyle(windowId: number, pointerStyle: PointerStyle, callback: AsyncCallback<void>): void | 设置鼠标光标样式，该接口会影响指定窗口鼠标光标样式。 |
| getPointerStyle(windowId: number, callback: AsyncCallback<PointerStyle>): void | 查询鼠标光标样式。 |

## 设置鼠标光标隐藏

用户在全屏观看视频时，可以调用鼠标光标的隐藏接口设置鼠标光标不可见，提升用户体验。

### 开发步骤

1. 应用切换到全屏播放。
2. 在应用中调用鼠标光标隐藏接口隐藏光标。
3. 应用退出全屏播放。
4. 在应用中调用鼠标光标显示接口显示光标。

```
1. Text("Click to hide pointer")
2. .onClick(() => {
3. // 1.应用切换到全屏播放
4. // 2.调用鼠标光标隐藏接口隐藏光标
5. try {
6. pointer.setPointerVisible(false, (error: Error) => {
7. if (error) {
8. hilog.error(DOMAIN, 'Pointer', `Set pointer visible failed, error: %{public}s`,
9. JSON.stringify(error, ["code", "message"]));
10. return;
11. }
12. hilog.info(DOMAIN, 'Pointer', 'Set pointer visible success.');
13. });
14. } catch (error) {
15. hilog.error(DOMAIN, 'Pointer', `The mouse pointer hide attributes is failed. %{public}s`,
16. JSON.stringify(error, ["code", "message"]));
17. }
18. })
19. // ...

21. // 3.应用退出全屏播放
22. // 4.调用鼠标光标显示接口显示光标
23. Text("Click to display pointer")
24. .onClick(() => {
25. try {
26. pointer.setPointerVisible(true, (error: Error) => {
27. if (error) {
28. hilog.error(DOMAIN, 'Pointer', `Set pointer visible failed, error: %{public}s`,
29. JSON.stringify(error, ["code", "message"]));
30. return;
31. }
32. hilog.info(DOMAIN, 'Pointer', 'Set pointer visible success.');
33. });
34. } catch (error) {
35. hilog.error(DOMAIN, 'Pointer', `Set pointer visible failed, error: %{public}s`,
36. JSON.stringify(error, ["code", "message"]));
37. }
38. })
39. // ...
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputKit/ArkTsPointer/entry/src/main/ets/pages/Index.ets#L29-L97)

## 设置鼠标光标样式

当开发者设计取色器特性时，可以将鼠标光标样式切换为取色器样式，完成取色后，设置鼠标光标样式为默认样式，该接口设置和查询当前应用内指定窗口的光标样式，总共可设置49种光标样式，具体参考[光标样式](../harmonyos-references/js-apis-pointer.md#pointerstyle)。

### 开发步骤

1. 开发者使能取色功能。
2. 调用窗口实例获取对应的窗口ID。
3. 设置鼠标光标样式为取色器样式。
4. 取色结束。
5. 设置鼠标光标样式为默认样式。

```
1. Text(`Click to set the mouse pointer style to the color picker style`)
2. .onClick(() => {
3. // 1.开发者使能取色功能
4. // 2.调用窗口实例获取对应的窗口id
5. window.getLastWindow(this.getUIContext().getHostContext(),
6. (error: BusinessError, windowClass: window.Window) => {
7. if (error.code) {
8. hilog.error(DOMAIN, 'Pointer', 'Failed to obtain the top window. Cause: %{public}s',
9. JSON.stringify(error));
10. return;
11. }
12. let windowId = windowClass.getWindowProperties().id;
13. if (windowId < 0) {
14. hilog.info(DOMAIN, 'Pointer', 'Invalid windowId');
15. return;
16. }
17. try {
18. // 3.设置鼠标光标样式为取色器样式
19. pointer.setPointerStyle(windowId, pointer.PointerStyle.COLOR_SUCKER).then(() => {
20. hilog.info(DOMAIN, 'Pointer', 'Successfully set mouse pointer style');
21. });
22. } catch (error) {
23. hilog.error(DOMAIN, 'Pointer', `Failed to set the pointer style, error=%{public}s, msg=%{public}s`,
24. JSON.stringify(error), error.message);
25. }
26. });
27. })
28. // ...

31. Text(`Click to set the mouse pointer style to default style`)
32. .onClick(() => {
33. // 4.取色结束
34. window.getLastWindow(this.getUIContext().getHostContext(),
35. (error: BusinessError, windowClass: window.Window) => {
36. if (error.code) {
37. hilog.error(DOMAIN, 'Pointer', 'Failed to obtain the top window. Cause: %{public}s',
38. JSON.stringify(error));
39. return;
40. }
41. let windowId = windowClass.getWindowProperties().id;
42. if (windowId < 0) {
43. hilog.info(DOMAIN, 'Pointer', 'Invalid windowId');
44. return;
45. }
46. try {
47. // 5.设置鼠标光标样式为默认样式
48. pointer.setPointerStyle(windowId, pointer.PointerStyle.DEFAULT).then(() => {
49. hilog.info(DOMAIN, 'Pointer', 'Successfully set mouse pointer style');
50. });
51. } catch (error) {
52. hilog.error(DOMAIN, 'Pointer', `Failed to set the pointer style, error=%{public}s, msg=%{public}s`,
53. JSON.stringify(error), error.message);
54. }
55. });
56. })
```

[Index.ets](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/InputKit/ArkTsPointer/entry/src/main/ets/pages/Index.ets#L99-L171)
