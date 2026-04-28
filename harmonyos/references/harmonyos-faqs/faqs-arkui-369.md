---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-369
title: 如何同时获取屏幕方向orientation和系统规避区avoidAreaChange信息
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何同时获取屏幕方向orientation和系统规避区avoidAreaChange信息
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:35+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:311dd9864e1033b647d49f5a71fffb9beaf942f94d38f047d415fcc048cb8815
---

以折叠屏形态变化时触发为示例，可以在EntryAbility.ets文件中通过[on('avoidAreaChange')](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9)接口监听窗口系统规避区的变化，在callback中获取avoidAreaChange信息，并通过Display实例获取屏幕方向orientation等信息。

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { display, window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
8. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
9. }

11. onDestroy(): void {
12. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
13. }

15. onWindowStageCreate(windowStage: window.WindowStage): void {
16. // Main window is created, set main page for this ability
17. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

19. windowStage.loadContent('pages/Index', (err) => {
20. if (err.code) {
21. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
22. return;
23. }
24. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
25. });

27. let windowClass: window.Window | undefined = undefined;
28. try {
29. window.getLastWindow(this.context, (err: BusinessError, data) => {
30. const errCode: number = err.code;
31. if (errCode) {
32. console.error(`Failed to obtain the top window. Cause code: ${err.code}, message: ${err.message}`);
33. return;
34. }
35. windowClass = data;
36. console.info('Succeeded in obtaining the top window. Data: ' + JSON.stringify(data));
37. if (windowClass) {
38. // Please ensure that the relevant Window instance, namely windowClass, has been obtained
39. windowClass.on('avoidAreaChange', async (data) => {
40. console.info('Succeeded in enabling the listener for avoid area changes. Type: ' +
41. JSON.stringify(data.type) + ', area ' + JSON.stringify(data.area));
42. try {
43. let defaultDisplay: display.Display = display.getDefaultDisplaySync();
44. console.info('---Orientation: ' + defaultDisplay.orientation);
45. } catch (error) {
46. let err = error as BusinessError;
47. hilog.error(0x0000, 'EntryAbility', `error code:${err.code},message:${err.message}`);
48. }
49. });
50. }
51. });
52. } catch (exception) {
53. console.error(`Failed to obtain the top window. Cause code: ${exception.code}, message: ${exception.message}`);
54. }
55. }

57. onWindowStageDestroy(): void {
58. // Main window is destroyed, release UI related resources
59. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
60. }

62. onForeground(): void {
63. // Ability has brought to foreground
64. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
65. }

67. onBackground(): void {
68. // Ability has back to background
69. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
70. }
71. }
```

[EntryAbilityOrientationAndAvoidAreaChange.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityOrientationAndAvoidAreaChange.ets#L21-L92)

**参考链接**

[开启当前窗口系统规避区变化的监听](../harmonyos-references/arkts-apis-window-window.md#onavoidareachange9) [显示设备当前显示的方向枚举](../harmonyos-references/js-apis-display.md#orientation10)
