---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-358
title: 如何实现状态栏背景颜色沉浸
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现状态栏背景颜色沉浸
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:31+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:3757decf328f55f0c02cc6d91c9c15988a817bf4b3c1fca3eee5380e6868dc9a
---

**问题描述**

为了避免状态栏颜色与背景重合，需根据状态栏和内容区域的颜色进行沉浸式效果适配，具体方式如下：

**解决措施**

方式一：设置窗口的背景色来实现沉浸式效果，参考代码如下：

```
1. // EntryAbility.ets

4. onWindowStageCreate(windowStage: window.WindowStage): void {
5. windowStage.loadContent('pages/Example', (err, data) => {
6. if (err?.code) {
7. return;
8. }
9. // Set the full window color to match the color of the application elements
10. windowStage.getMainWindowSync().setWindowBackgroundColor('#008000');
11. });
12. }
```

[EntryAbilityImmersingBackgroundColor\_One.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityImmersingBackgroundColor_One.ets#L28-L39)

方式二：对顶部组件使用[expandSafeArea](../harmonyos-references/ts-universal-attributes-expand-safe-area.md#expandsafearea)属性扩展安全区域属性，实现状态栏沉浸

```
1. @Entry
2. @Component
3. struct Example {
4. build() {
5. Column() {
6. Row() {
7. Text('Top Row')
8. .fontSize(40)
9. .textAlign(TextAlign.Center)
10. .width('100%')
11. }
12. .backgroundColor('#F08080')
13. // Set the top drawing to extend to the status bar
14. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP])

17. Row() {
18. Text('ROW2')
19. .fontSize(40)
20. }
21. .backgroundColor(Color.Orange)
22. .padding(20)

25. Row() {
26. Text('ROW3')
27. .fontSize(40)
28. }
29. .backgroundColor(Color.Orange)
30. .padding(20)

33. Row() {
34. Text('ROW4')
35. .fontSize(40)
36. }
37. .backgroundColor(Color.Orange)
38. .padding(20)

41. Row() {
42. Text('ROW5')
43. .fontSize(40)
44. }
45. .backgroundColor(Color.Orange)
46. .padding(20)

49. Row() {
50. Text('Bottom Row')
51. .fontSize(40)
52. .textAlign(TextAlign.Center)
53. .width('100%')
54. }
55. .backgroundColor(Color.Orange)
56. // Set the bottom drawing to extend to the navigation bar
57. .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM])
58. }
59. .width('100%')
60. .height('100%')
61. .alignItems(HorizontalAlign.Center)
62. .backgroundColor('#008000')
63. .justifyContent(FlexAlign.SpaceBetween)
64. }
65. }
```

[ImmersingBackgroundColorOfStatusBar\_One.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImmersingBackgroundColorOfStatusBar_One.ets#L21-L85)

方式三：手动设置状态栏的颜色：

实现步骤：

1. 获取并缓存窗口对象，可参考：[Interface (Window)](../harmonyos-references/arkts-apis-window-window.md)。
2. 在打开目标页面时，使用[setWindowSystemBarProperties](../harmonyos-references/arkts-apis-window-window.md#setwindowsystembarproperties9)接口设置状态栏属性。

获取窗口对象并缓存。

```
1. // EntryAbility.ets

4. onWindowStageCreate(windowStage: window.WindowStage): void {
5. // Main window is created, set main page for this ability
6. hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

9. windowStage.loadContent('pages/Index', (err) => {
10. if (err.code) {
11. hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
12. return;
13. }
14. hilog.info(0x0000, 'testTag', 'Succeeded in loading the content.');
15. let windowClass: window.Window = windowStage.getMainWindowSync(); // Get the main window of the application
16. // 1. Set the window to full screen
17. let isLayoutFullScreen = true;
18. windowClass.setWindowLayoutFullScreen(isLayoutFullScreen);
19. // 2. Cache window object
20. AppStorage.setOrCreate('windowClass', windowClass);
21. });
22. }
```

[EntryAbilityImmersingBackgroundColor\_Two.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/entryability/EntryAbilityImmersingBackgroundColor_Two.ets#L28-L49)

打开页面时，设置状态栏属性，选择所需的沉浸式颜色。

```
1. import { window } from '@kit.ArkUI';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. @Entry
6. @Component
7. struct CommonTopBar {
8. @State message: string = 'Hello World';

10. aboutToAppear() {
11. // Get the current application window
12. let windowClass = AppStorage.get<window.Window>('windowClass') as window.Window;
13. try {
14. // Set the background color of the status bar and navigation bar to the same color as the application window
15. windowClass.setWindowSystemBarProperties({
16. // The color attribute is ARGB, set the dust cover to 0% to make it transparent
17. // Navigation bar color
18. navigationBarColor: '#fd121de5',
19. // Status bar color
20. statusBarColor: '#ff0ad9c2',
21. // Status bar text color
22. statusBarContentColor: '#fff1e50a'
23. })
24. } catch (error) {
25. let err = error as BusinessError;
26. hilog.error(0x0000, 'CommonTopBar', `error code:${err.code},message:${err.message}`);
27. }
28. }

30. build() {
31. RelativeContainer() {
32. Text(this.message)
33. .id('PageHelloWorld')
34. .fontSize(50)
35. .fontWeight(FontWeight.Bold)
36. .alignRules({
37. center: {
38. anchor: '__container__',
39. align: VerticalAlign.Center
40. },
41. middle: {
42. anchor: '__container__',
43. align: HorizontalAlign.Center
44. }
45. })
46. }
47. .height('100%')
48. .width('100%')
49. }
50. }
```

[ImmersingBackgroundColorOfStatusBar\_Two.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImmersingBackgroundColorOfStatusBar_Two.ets#L21-L71)
