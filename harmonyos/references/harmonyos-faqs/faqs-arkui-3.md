---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-3
title: 如何实现防截屏功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现防截屏功能
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:00+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:d2fbd873a9015f93a8c4bee13071b5a699b9d3d4a263bf61e7fef5c15f1a7c89
---

设置窗口隐私模式，禁止截屏或录屏。此接口适用于禁止截屏/录屏的场景。

方式一：进入页面开启隐私模式，离开页面取消，具体可参考以下步骤：

首先，在 module.json5 文件中声明需要使用 ohos.permission.PRIVACY\_WINDOW 权限。

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.PRIVACY_WINDOW"
4. }
5. ],
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/module.json5#L74-L78)

通过导航栏显示状态切换触发 onNavBarStateChange回调。进入页面时，isVisible 为 true，调用setWindowPrivacyMode 设置窗口为隐私模式。离开页面时，isVisible 为 false，设置窗口为非隐私模式。参考示例代码如下：

```
1. import { BusinessError } from '@kit.BasicServicesKit';
2. import { common } from '@kit.AbilityKit';
3. import { window } from '@kit.ArkUI';

5. class WindowUtils {
6. static setWindowPrivacyModeInPage(context: common.UIAbilityContext, isFlag: boolean) {
7. window.getLastWindow(context).then((lastWindow) => {
8. lastWindow.setWindowPrivacyMode(isFlag, (err: BusinessError) => {
9. const errCode: number = err.code;
10. if (errCode) {
11. console.error('Failed to set the window to privacy mode. Cause:' + JSON.stringify(err));
12. return;
13. }
14. console.info('Succeeded in setting the window to privacy mode.');
15. });
16. })
17. }
18. }

20. @Entry
21. @Component
22. struct Index {
23. @State message: string = 'hello world';
24. @Provide('NavPathStack') pageStack: NavPathStack = new NavPathStack();
25. context = this.getUIContext();

27. @Builder
28. PagesMap(name: string) {
29. if (name === 'Index') {
30. Index();
31. } else if (name === 'PageOne') {
32. PageOne();
33. }
34. }

36. build() {
37. Navigation(this.pageStack) {
38. Column() {
39. Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
40. .width('80%')
41. .height(40)
42. .margin(20)
43. .onClick(() => {
44. this.pageStack.pushPath({ name: 'PageOne' }) // Push the page info of specified NavDestination into the stack
45. })
46. }
47. }
48. .navDestination(this.PagesMap)
49. .onNavBarStateChange((isVisible: boolean) => {
50. // Callback triggered when navigation bar display state changes
51. console.info('------>isVisible：' + isVisible)
52. WindowUtils.setWindowPrivacyModeInPage(this.context.getHostContext() as common.UIAbilityContext, isVisible);
53. })
54. }
55. }

57. @Component
58. struct PageOne {
59. @Consume('NavPathStack') pageStack: NavPathStack;

61. build() {
62. NavDestination() {
63. Column() {
64. Text('PageOne')
65. }
66. }
67. .title('pageOne')
68. .onBackPressed(() => {
69. const popDestinationInfo = this.pageStack.pop(); // Pop the top element from the navigation stack
70. return true;
71. })
72. }
73. }
```

[SetWindowPrivacyModeInPage.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/SetWindowPrivacyModeInPage.ets#L21-L93)

方式二：设置主窗口为隐私模式，参考以下步骤：

在module.json5文件中声明需要使用的ohos.permission.PRIVACY\_WINDOW权限。

```
1. "requestPermissions": [
2. {
3. "name": "ohos.permission.PRIVACY_WINDOW"
4. }
5. ],
```

[module.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/module.json5#L74-L78)

在EntryAbility.ets文件的onWindowStageCreate回调中设置主窗口为隐私模式，具体可参考示例代码：

```
1. import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';
4. import { BusinessError } from '@kit.BasicServicesKit';

6. export default class EntryAbility extends UIAbility {
7. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
8. this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
9. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
10. }

12. onDestroy(): void {
13. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
14. }

16. onWindowStageCreate(windowStage: window.WindowStage): void {
17. // Main window is created, set main page for this ability
18. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
19. // Get the main window
20. windowStage.getMainWindow((err: BusinessError, data) => {
21. let errCode: number = err.code;
22. if (errCode) {
23. console.error('Failed to obtain the main window. Cause: ' + JSON.stringify(err));
24. return;
25. }
26. let windowClass: window.Window = data;
27. console.info('Succeeded in obtaining the main window. Data: ' + JSON.stringify(data));
28. // Set the window privacy mode
29. let isPrivacyMode: boolean = true;
30. try {
31. windowClass.setWindowPrivacyMode(isPrivacyMode, (err: BusinessError) => {
32. const errCode: number = err.code;
33. if (errCode) {
34. console.error('Failed to set the window to privacy mode. Cause:' + JSON.stringify(err));
35. return;
36. }
37. console.info('Succeeded in setting the window to privacy mode.');
38. });
39. } catch (exception) {
40. console.error('Failed to set the window to privacy mode. Cause:' + JSON.stringify(exception));
41. }
42. })
43. windowStage.loadContent('pages/Index', (err, data) => {
44. if (err.code) {
45. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
46. return;
47. }
48. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
49. });
50. }

52. onWindowStageDestroy(): void {
53. // Main window is destroyed, release UI related resources
54. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
55. }

57. onForeground(): void {
58. // Ability has brought to foreground
59. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
60. }

62. onBackground(): void {
63. // Ability has back to background
64. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
65. }
66. }
```

[EntryAbilitySetWindowPrivacy.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilitySetWindowPrivacy.ets#L21-L86)

**参考链接**

[setWindowPrivacyMode](../harmonyos-references/arkts-apis-window-window.md#setwindowprivacymode9)、[onNavBarStateChange](../harmonyos-references/ts-basic-components-navigation.md#onnavbarstatechange9)
