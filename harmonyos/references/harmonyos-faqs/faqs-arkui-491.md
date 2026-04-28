---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-491
title: 如何实现三键导航的监听与避让
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现三键导航的监听与避让
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:10+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:95a02fb83e365543ba31a45993326f1034be4f305b3c4c46ed15d1df7086749e
---

**解决措施**

1、通过[settings.registerKeyObserver](../harmonyos-references/js-apis-settings.md#settingsregisterkeyobserver11)监听三键导航的开启。

```
1. settings.registerKeyObserver(this.getUIContext().getHostContext(), 'float_navigation_info',
2. settings.domainName.USER_PROPERTY, () => {
3. this.adaptLayout();
4. });
```

[MonitoringAvoidanceThreeKeyNavigation.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/MonitoringAvoidanceThreeKeyNavigation.ets#L43-L46)

2、通过[setting.getValue](../harmonyos-references/js-apis-settings.md#settingsgetvalue11)获取导航的信息。

```
1. settings.getValue(this.getUIContext().getHostContext(), 'float_navigation_info',
2. settings.domainName.USER_PROPERTY).then((data: string) => {
3. if (data) {
4. let navigationInfo = JSON.parse(data) as NavigationButtonInfo;
5. this.adaptValue = navigationInfo.getAdaptValue();
6. }
7. })
```

[MonitoringAvoidanceThreeKeyNavigation.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/MonitoringAvoidanceThreeKeyNavigation.ets#L54-L60)

3、定义三键导航信息。

```
1. class NavigationButtonInfo {
2. // Display Status: -1 Not displayed; 0 Appears in a three-key form; 1 Displayed as a floating ball
3. private showType: number = -1;
4. // Three-Key navigation location area: x coordinate; y coordinate; Width of the triple-key area; Triple key area height; unit: px
5. private region: number[] = [0, 0, 0, 0];

7. // Obtain the adaptation area and implement this function as required
8. public getAdaptValue(): number {
9. // If the three keys are displayed and an app is in full screen, the width of the three keys is used as the adaptation value
10. // this.region[2] < this.region[3] This indicates that the three buttons are displayed at the side of the screen when the screen is in landscape mode.
11. if (this.showType === 0 && this.region[2] < this.region[3]) {
12. return this.region[2];
13. } else {
14. return 0;
15. }
16. }
17. }
```

[MonitoringAvoidanceThreeKeyNavigation.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/MonitoringAvoidanceThreeKeyNavigation.ets#L99-L116)

4、根据region中的布局信息进行适配。

```
1. .padding({ right: this.getUIContext().px2vp(this.adaptValue) })
```

[MonitoringAvoidanceThreeKeyNavigation.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/MonitoringAvoidanceThreeKeyNavigation.ets#L90-L90)

示例代码参考如下：

```
1. import settings from '@ohos.settings';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import window from '@ohos.window';

6. @Entry
7. @Component
8. struct Index {
9. @State message: string = 'Hello World';
10. @State adaptValue: number = 0;

12. aboutToAppear(): void {
13. this.watchNavigationButtonChange();
14. window.getLastWindow(this.getUIContext().getHostContext(), ((err: BusinessError, data) => {
15. data.setWindowLayoutFullScreen(true);
16. }));
17. }

19. // Monitor the changes of three-key navigation information
20. private watchNavigationButtonChange(): void {
21. this.adaptLayout();

23. settings.registerKeyObserver(this.getUIContext().getHostContext(), 'float_navigation_info',
24. settings.domainName.USER_PROPERTY, () => {
25. this.adaptLayout();
26. });
27. }

29. // Adapt the app layout based on the Three Key Navigation information
30. private adaptLayout(): void {
31. try {
32. settings.getValue(this.getUIContext().getHostContext(), 'float_navigation_info',
33. settings.domainName.USER_PROPERTY).then((data: string) => {
34. if (data) {
35. let navigationInfo = JSON.parse(data) as NavigationButtonInfo;
36. this.adaptValue = navigationInfo.getAdaptValue();
37. }
38. })
39. } catch (e) {
40. this.adaptValue = 0;
41. hilog.warn(0, 'tag', 'adaptMargin err:' + e);
42. }
43. }

45. build() {
46. RelativeContainer() {
47. Column() {
48. Row() {
49. Text(this.message)
50. .id('HelloWorld')
51. .fontSize($r('app.float.page_text_font_size'))
52. .fontWeight(FontWeight.Bold)
53. .alignRules({
54. center: { anchor: '__container__', align: VerticalAlign.Center },
55. middle: { anchor: '__container__', align: HorizontalAlign.Center }
56. })
57. .onClick(() => {
58. this.message = 'Welcome';
59. })
60. }
61. .backgroundColor(Color.Red)
62. .height('100%')
63. .width('100%')
64. }
65. .backgroundColor(Color.Yellow)
66. .padding({ right: this.getUIContext().px2vp(this.adaptValue) })
67. }
68. .height('100%')
69. .width('100%')
70. }
71. }

73. class NavigationButtonInfo {
74. // Display Status: -1 Not displayed; 0 Appears in a three-key form; 1 Displayed as a floating ball
75. private showType: number = -1;
76. // Three-Key navigation location area: x coordinate; y coordinate; Width of the triple-key area; Triple key area height; unit: px
77. private region: number[] = [0, 0, 0, 0];

79. // Obtain the adaptation area and implement this function as required
80. public getAdaptValue(): number {
81. // If the three keys are displayed and an app is in full screen, the width of the three keys is used as the adaptation value
82. // this.region[2] < this.region[3] This indicates that the three buttons are displayed at the side of the screen when the screen is in landscape mode.
83. if (this.showType === 0 && this.region[2] < this.region[3]) {
84. return this.region[2];
85. } else {
86. return 0;
87. }
88. }
89. }
```

[MonitoringAvoidanceThreeKeyNavigation.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/MonitoringAvoidanceThreeKeyNavigation.ets#L20-L117)

导航条、状态栏、挖孔区沉浸式方案参考链接：[实现沉浸式效果](../best-practices/bpta-multi-device-window-immersive.md#section180431120426)。
