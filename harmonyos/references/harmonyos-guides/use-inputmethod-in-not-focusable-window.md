---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/use-inputmethod-in-not-focusable-window
title: 不可获焦窗口中输入框与输入法交互指南
breadcrumb: 指南 > 应用框架 > IME Kit（输入法开发服务） > 不可获焦窗口中输入框与输入法交互指南
category: harmonyos-guides
scraped_at: 2026-04-28T07:41:38+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:eb9576c10e14b00a35d008542eb4092f12218dca2f08c8103738d0914c11b6c7
---

## 场景介绍

应用获得焦点是使用输入法的必要条件，开发者需要正确处理焦点以确保输入法的正常工作。

例如，在应用开发中，开发者可以通过[setWindowFocusable](../harmonyos-references/arkts-apis-window-window.md#setwindowfocusable9)，将创建的窗口的可获焦属性设置为false（如悬浮窗、辅助交互窗口等），并希望在该窗口中绘制输入框（如[TextInput](../harmonyos-references/ts-basic-components-textinput.md)、[TextArea](../harmonyos-references/ts-basic-components-textarea.md)或[自绘输入框](use-inputmethod-in-custom-edit-box.md)）以支持用户输入，即拉起系统键盘进行输入操作。

## 系统限制

当通过[setWindowFocusable](../harmonyos-references/arkts-apis-window-window.md#setwindowfocusable9)将窗口设置为不可获焦时，系统侧会对该窗口施加限制。由于窗口无焦点，输入事件（如按键信息）无法被窗口正确接收和处理，输入内容无法同步到该窗口中的输入框，导致输入框与键盘交互异常。

## 推荐方案

若需要在不可获焦窗口中绘制输入框，并希望能够与键盘正常交互，建议按照以下方式开发（以[TextInput](../harmonyos-references/ts-basic-components-textinput.md)为例）：

1. 在主窗中创建一个子窗，设置其初始为不可获焦窗口。

   可达到效果：点击主窗输入组件，弹出子窗，焦点仍然在主窗的输入框上。

   ```
   1. // Index.ets实现主窗的布局内容
   2. import { window } from '@kit.ArkUI';

   4. @Entry
   5. @Component
   6. struct Index {
   7. async createSubWindow() {
   8. try {
   9. // 1.创建子窗并设置子窗id
   10. let windowStage: window.WindowStage | undefined = AppStorage.get('windowStage');
   11. if (windowStage == null) {
   12. console.error('Failed to get windowStage');
   13. return;
   14. }
   15. let options: window.SubWindowOptions = { title: 'title', decorEnabled: true };
   16. let subWindow = await windowStage?.createSubWindowWithOptions('mySubWindow', options);
   17. const subWindowId: number | undefined = subWindow?.getWindowProperties().id;
   18. AppStorage.setOrCreate('subWindowId', subWindowId);
   19. // 2.设置子窗为不可获焦
   20. subWindow?.resize(500, 500);
   21. subWindow?.setUIContent("pages/SubWindowIndex");
   22. subWindow?.setWindowFocusable(false);
   23. // 3.显示子窗
   24. subWindow?.showWindow();
   25. } catch (exception) {
   26. console.error(`Failed to create the subWindow. Cause code: ${exception.code}, message: ${exception.message}`);
   27. }
   28. }

   30. build() {
   31. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
   32. TextInput({ placeholder: '点击创建并显示子窗' })
   33. .onClick(() => {
   34. this.createSubWindow();
   35. })
   36. }
   37. }
   38. }
   ```
2. 当用户点击子窗中的输入框组件时，可以先通过[setWindowFocusable](../harmonyos-references/arkts-apis-window-window.md#setwindowfocusable9)将子窗设置为可获焦，然后通过[shiftAppWindowFocus](../harmonyos-references/arkts-apis-window-f.md#windowshiftappwindowfocus11)将焦点窗口从主窗切换为子窗，即可在子窗的输入框中正常使用输入法。

   ```
   1. // SubWindowIndex.ets实现子窗的布局内容
   2. import { window } from '@kit.ArkUI';

   4. @Entry
   5. @Component
   6. struct SubWindowIndex {
   7. async shiftFocusToSubWindow() {
   8. try {
   9. let windowStage: window.WindowStage | undefined = AppStorage.get('windowStage');
   10. if (windowStage == null) {
   11. console.error('Failed to get the subwindow. Cause: windowStage is undefined');
   12. return;
   13. }
   14. let subWindowList: window.Window[] = await windowStage?.getSubWindow();
   15. let subWindow: window.Window = subWindowList[0];
   16. // 1.将子窗口设置为可获焦
   17. subWindow?.setWindowFocusable(true);
   18. // 2.将焦点切换到子窗口
   19. const mainWindowId: number = AppStorage.get('mainWindowId') || 0;
   20. const subWindowId: number = AppStorage.get('subWindowId') || 0;
   21. await window.shiftAppWindowFocus(mainWindowId, subWindowId);
   22. } catch (exception) {
   23. console.error(`Failed to shift focus to subWindow. Cause code: ${exception.code}, message: ${exception.message}`);
   24. }
   25. }

   27. build() {
   28. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
   29. TextInput({ placeholder: '这是一个输入组件' })
   30. .onClick(() => {
   31. // 用户点击子窗的输入组件，切换焦点至子窗
   32. this.shiftFocusToSubWindow();
   33. })
   34. }
   35. }
   36. }
   ```
3. 当用户重新点击子窗中的非输入框组件时，可以通过[setWindowFocusable](../harmonyos-references/arkts-apis-window-window.md#setwindowfocusable9)将子窗重新设置为不可获焦，焦点窗口即可恢复至主窗。

   ```
   1. // SubWindowIndex.ets实现子窗的布局内容
   2. import { window } from '@kit.ArkUI';

   4. @Entry
   5. @Component
   6. struct SubWindowIndex {
   7. async shiftFocusToSubWindow() {
   8. try {
   9. let windowStage: window.WindowStage | undefined = AppStorage.get('windowStage');
   10. if (windowStage == null) {
   11. console.error('Failed to get the subwindow. Cause: windowStage is undefined');
   12. return;
   13. }
   14. let subWindowList: window.Window[] = await windowStage?.getSubWindow();
   15. let subWindow: window.Window = subWindowList[0];
   16. // 1.将子窗口设置为可获焦
   17. subWindow?.setWindowFocusable(true);
   18. // 2.将焦点切换到子窗口
   19. const mainWindowId: number = AppStorage.get('mainWindowId') || 0;
   20. const subWindowId: number = AppStorage.get('subWindowId') || 0;
   21. await window.shiftAppWindowFocus(mainWindowId, subWindowId);
   22. } catch (exception) {
   23. console.error(`Failed to shift focus to subWindow. Cause code: ${exception.code}, message: ${exception.message}`);
   24. }
   25. }

   27. async shiftFocusToMainWindow() {
   28. try {
   29. let windowStage: window.WindowStage | undefined = AppStorage.get('windowStage');
   30. if (windowStage == null) {
   31. console.error('Failed to get the subwindow. Cause: windowStage is undefined');
   32. return;
   33. }
   34. let subWindowList: window.Window[] = await windowStage?.getSubWindow();
   35. let subWindow: window.Window = subWindowList[0];
   36. // 将子窗口设置为不可获焦
   37. subWindow?.setWindowFocusable(false);
   38. } catch (exception) {
   39. console.error(`Failed to shift focus to main window. Cause code: ${exception.code}, message: ${exception.message}`);
   40. }
   41. }

   43. build() {
   44. Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
   45. TextInput({ placeholder: '这是一个输入组件' })
   46. .onClick(() => {
   47. // 点击子窗输入组件时，切换焦点至子窗口
   48. this.shiftFocusToSubWindow();
   49. })
   50. Button('这是一个普通组件')
   51. .onClick(() => {
   52. // 点击子窗非输入组件时，可切换焦点回主窗口
   53. this.shiftFocusToMainWindow();
   54. })
   55. }
   56. }
   57. }
   ```
