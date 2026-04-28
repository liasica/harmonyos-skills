---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-multi-settings-application-page
title: 多设备设置界面
breadcrumb: 最佳实践 > 一次开发，多端部署 > 多设备界面开发 > 多设备界面开发案例 > 多设备设置界面
category: best-practices
scraped_at: 2026-04-28T08:21:33+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:eab4ecbd4cf7cd73d4af4352eb5bea6a1c492b6e68bff7570c591af4edb5b876
---

本小节以“设置”应用页面为例，介绍如何使用自适应布局能力和响应式布局能力适配不同尺寸窗口。

## 页面设计

为充分利用屏幕尺寸优势，应用常常有在小屏设备上单栏显示，大屏设备上左右分两栏显示的设计，设置应用页面设计如下。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fe/v3/vDa3-0nTTxy36tsvP4RzMw/zh-cn_image_0000002472234181.png?HW-CC-KV=V1&HW-CC-Date=20260428T002131Z&HW-CC-Expire=86400&HW-CC-Sign=9A81074378C36CDEBABDDB0316DD11B1065F91B6647473D64AF05C38D0A3A2EA "点击放大")

观察“设置”应用页面设计，不同断点下“设置主页”、“WLAN页面”和“更多WLAN设置页面”几乎完全一致，只是在sm断点下采用单栏显示，在md和lg断点下采用双栏显示。

在前面的典型页面场景中，已经介绍了如何分析及实现不同断点下设计相似的单个页面，本小节将展开介绍如何实现不同断点下存在单栏和双栏设计的场景。

为了方便读者理解，本小节将围绕以下三个问题进行介绍。

1. [如何实现单/双栏的显示效果](bpta-multi-settings-application-page.md#如何实现单双栏的显示效果)
2. [如何实现点击跳转或刷新](bpta-multi-settings-application-page.md#如何实现点击跳转或刷新)
3. [如何实现多级跳转](bpta-multi-settings-application-page.md#如何实现多级跳转)

## 如何实现单/双栏的显示效果

开发者可以使用Row、Column、[RowSplit](../harmonyos-references/ts-container-rowsplit.md)等基础的组件，实现分栏显示的效果，但是需要较多的开发工作量。方舟开发框架在API 9重构了[Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件，开发者可以通过配置Navigation组件的属性，控制其按照单栏或双栏的效果进行显示。

Navigation组件由NavBar和Content两部分区域组成，支持Stack、Split以及Auto三种模式。Stack及Split模式下Navigation组件的表现如下图所示。

* Stack模式

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/6qhZ-OHITNS7qDsA8T3ggQ/zh-cn_image_0000002321148442.png?HW-CC-KV=V1&HW-CC-Date=20260428T002131Z&HW-CC-Expire=86400&HW-CC-Sign=F389F0A89F80FD96706DF688DD3EF6000FDA38FF2F0AABFFBC49C85614678EF7 "点击放大")
* Split模式

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/xZEC9ocWTde8sSk2-UhfSg/zh-cn_image_0000002355266989.png?HW-CC-KV=V1&HW-CC-Date=20260428T002131Z&HW-CC-Expire=86400&HW-CC-Sign=FED1ADF6D9245BB9EC019967DAF37C84FD350D170EF2C599FFD94C3D7270CAF3 "点击放大")
* Auto模式

  Auto模式是指Navigation组件可以根据应用窗口尺寸，自动选择合适的模式：窗口宽度小于520vp时，采用Stack模式显示；窗口宽度大于等于520vp时，采用Split模式显示。当窗口尺寸发生改变时，Navigation组件也会自动在Stack模式和Split模式之间切换。

说明

* Navigation组件提供的title、navBarWidth、navBarPosition等属性来调整其显示效果。Navigation组件样式的配置与其它组件类似，这里不做赘述。

设置主页的核心代码如下所示。Navigation组件默认处于Auto模式，其样式会根据应用窗口尺寸在单栏和双栏之间自动切换。

```
1. import { SettingList } from 'settingItems';

3. const uiContext: UIContext | undefined = AppStorage.get('uiContext');
4. let storage: LocalStorage | undefined = uiContext!.getSharedLocalStorage();

6. @Entry(storage)
7. @Component
8. struct Index {
9. @LocalStorageProp('currentBreakpoint') curBp: string = 'sm';
10. @LocalStorageProp('windowWidth') windowWidth: number = 300;
11. @LocalStorageProp('isSplitMode') isSplitMode: boolean = false;
12. @Provide('pathInfos') pathStack: NavPathStack = new NavPathStack();

14. build() {
15. Navigation(this.pathStack) {
16. SettingList()
17. }
18. .title($r('app.string.settings'))
19. .mode(this.curBp !== 'sm' ? NavigationMode.Split : NavigationMode.Stack)
20. .navBarWidth(0.4 * this.windowWidth)
21. .hideToolBar(true)
22. .width('100%')
23. .height('100%')
24. .backgroundColor($r('sys.color.ohos_id_color_sub_background'))
25. }
26. }
```

[Index.ets](https://gitcode.com/harmonyos_samples/NavigationSettings/blob/master/products/default/src/main/ets/pages/Index.ets#L17-L42)

```
1. import { MainItem } from '../components/MainItem';
2. import { ItemGroup } from '../components/ItemGroup';
3. import { SearchBox } from '../components/SearchBox';
4. import { MoreConnectionsItem } from '../moreconnections/MoreConnectionsItem';
5. import { WlanSettingItem } from '../wlan/WlanSettingItem';

7. @Component
8. export struct SettingList {
9. @Builder CustomDivider() {
10. Divider()
11. .strokeWidth('1px')
12. .color($r('sys.color.ohos_id_color_list_separator'))
13. .margin({left: 48, right: 8})
14. }

16. build() {
17. List({space: 12}) {
18. ListItem() {
19. SearchBox()
20. }
21. .padding({top: 8, bottom: 8})
22. .width('100%')

24. ListItem() {
25. ItemGroup() {
26. WlanSettingItem()

28. this.CustomDivider()

30. MainItem({
31. title: $r('app.string.bluetoothTab'),
32. tag: $r('app.string.enabled'),
33. icon: $r('app.media.blueTooth'),
34. })

36. this.CustomDivider()

38. MainItem({
39. title: $r('app.string.mobileData'),
40. icon: $r('app.media.mobileData'),
41. })

43. this.CustomDivider()

45. MoreConnectionsItem()
46. }
47. }

49. ListItem() {
50. ItemGroup() {
51. MainItem({
52. title: $r('app.string.brightnessTab'),
53. icon: $r('app.media.displayAndBrightness'),
54. })
55. }
56. }

58. ListItem() {
59. ItemGroup() {
60. MainItem({
61. title: $r('app.string.volumeControlTab'),
62. icon: $r('app.media.volume'),
63. })
64. }
65. }

67. ListItem() {
68. ItemGroup() {
69. MainItem({
70. title: $r('app.string.biometricsAndPassword'),
71. icon: $r('app.media.biometricsAndPassword'),
72. })

74. this.CustomDivider()

76. MainItem({
77. title: $r('app.string.applyTab'),
78. icon: $r('app.media.application'),
79. })

81. this.CustomDivider()

83. MainItem({
84. title: $r('app.string.storageTab'),
85. icon: $r('app.media.storage'),
86. })

88. this.CustomDivider()

90. MainItem({
91. title: $r('app.string.security'),
92. icon: $r('app.media.security'),
93. })

95. this.CustomDivider()

97. MainItem({
98. title: $r('app.string.privacy'),
99. icon: $r('app.media.privacy'),
100. })
101. }
102. }

104. ListItem() {
105. ItemGroup() {
106. MainItem({
107. title: $r('app.string.usersAccountsTab'),
108. icon: $r('app.media.userAccounts'),
109. })

111. this.CustomDivider()

113. MainItem({
114. title: $r('app.string.systemTab'),
115. icon: $r('app.media.system'),
116. })

118. this.CustomDivider()

120. MainItem({
121. title: $r('app.string.aboutTab'),
122. icon: $r('app.media.aboutDevice'),
123. })
124. }
125. }

127. }
128. .padding({left: 12, right: 12})
129. .width('100%')
130. .height('100%')
131. .backgroundColor($r('sys.color.ohos_id_color_sub_background'))
132. }
133. }
```

[SettingList.ets](https://gitcode.com/harmonyos_samples/NavigationSettings/blob/master/features/settingitems/src/main/ets/settinglist/SettingList.ets#L17-L149)

## 如何实现点击跳转或刷新

Navigation组件通常搭配[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)对象以及[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)组件一起使用：

* NavPathStack对象，用于管理页面。主要涉及页面跳转、页面返回、页面替换、页面删除、参数获取、路由拦截等功能。
* NavDestination组件用于实际刷新Navigation组件Content区域的显示。

### 点击跳转

NavPathStack对象用于控制Navigation组件中页面的跳转，通过[Push相关的接口](../harmonyos-references/ts-basic-components-navigation.md#pushpath12)将指定的NavDestination页面信息入栈去实现页面跳转的功能。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/3g9kUow3R8WWxmvt3qMcKw/zh-cn_image_0000002321308278.png?HW-CC-KV=V1&HW-CC-Date=20260428T002131Z&HW-CC-Expire=86400&HW-CC-Sign=8A6FD414FCDB2AA441994A4F493870E8976DFCB7692BE701D3E53C92BF19FF5B)

结合设置应用的具体场景来看，点击上图1号小红框，跳转至2号红框WLAN页面，相应的核心代码实现如下。

```
1. import { MainItem } from '../components/MainItem';
2. import { WlanMoreSettingItem } from './WlanMoreSetting';
3. import { SubItemToggle } from '../components/SubItemToggle';
4. import { SubItemWifi } from '../components/SubItemWifi';
5. import { ItemGroup } from '../components/ItemGroup';
6. import { ItemDescription } from '../components/ItemDescription';
7. import { Logger } from '@ohos/common/Index';

9. const TAG = "WlanSettingItem"

11. @Component
12. export struct WlanSettingItem {
13. @LocalStorageLink('selectedLabel') selectedLabel: string = '';
14. @Consume('pathInfos') pathInfos: NavPathStack;

16. build() {
17. Column() {
18. MainItem({
19. title: $r('app.string.wifiTab'),
20. tag: 'UX',
21. icon: $r('app.media.wlan'),
22. label: 'WLAN'
23. })
24. .onClick(() => {
25. this.pathInfos.pushPath({ name: 'WlanSetting' });
26. this.selectedLabel = 'WLAN';
27. })
28. }
29. }
30. }

32. @Builder
33. export function WlanSettingBuilder() {
34. WlanSetting();
35. }

37. @Component
38. struct WlanSetting {
39. @State itemTitle: string = '';

41. aboutToAppear() {
42. try {
43. this.itemTitle = this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.wifiTab').id);
44. } catch (err) {
45. if (err.code) {
46. Logger.error(TAG, `Failed to get item title. Cause: ${JSON.stringify(err)}`);
47. }
48. }
49. }

51. @Builder
52. CustomDivider() {
53. Divider()
54. .strokeWidth('1px')
55. .color($r('sys.color.ohos_id_color_list_separator'))
56. .margin({ left: 12, right: 8 })
57. }

59. build() {
60. NavDestination() {
61. Column() {
62. Column() {
63. ItemGroup() {
64. SubItemToggle({ title: $r('app.string.wifiTab'), isOn: true })
65. }

67. Row().height(16)

69. ItemGroup() {
70. WlanMoreSettingItem()
71. }
72. }
73. .margin({ bottom: 19.5 })
74. .flexShrink(0)

76. Scroll() {
77. Column() {
78. ItemDescription({ description: $r('app.string.wifiTipConnectedWLAN') })
79. .padding({
80. left: 12,
81. right: 12,
82. bottom: 9.5
83. })

85. ItemGroup() {
86. SubItemWifi({
87. title: 'UX',
88. subTitle: $r('app.string.wifiSummaryConnected'),
89. isConnected: true,
90. icon: $r('app.media.ic_wifi_signal_4_dark')
91. })
92. }

94. Column() {
95. ItemDescription({ description: $r('app.string.wifiTipValidWLAN') })
96. .margin({
97. left: 12,
98. right: 12,
99. top: 19.5,
100. bottom: 9.5
101. })

103. ItemGroup() {
104. SubItemWifi({
105. title: 'Huwe-yee',
106. subTitle: $r('app.string.wifiSummaryEncrypted'),
107. isConnected: false,
108. icon: $r('app.media.ic_wifi_lock_signal_4_dark')
109. })

111. this.CustomDivider()

113. SubItemWifi({
114. title: 'UX-5G',
115. subTitle: $r('app.string.wifiSummaryOpen'),
116. isConnected: false,
117. icon: $r('app.media.ic_wifi_signal_4_dark')
118. })

120. this.CustomDivider()

122. SubItemWifi({
123. title: 'E1-AP',
124. subTitle: $r('app.string.wifiSummarySaveOpen'),
125. isConnected: false,
126. icon: $r('app.media.ic_wifi_signal_4_dark')
127. })
128. }
129. }
130. }
131. }
132. .scrollable(ScrollDirection.Vertical)
133. .scrollBar(BarState.Off)
134. .width('100%')
135. .flexShrink(1)
136. }
137. .width('100%')
138. .height('100%')
139. .padding({ left: 12, right: 12 })
140. }
141. .title(this.itemTitle)
142. .backgroundColor($r('sys.color.ohos_id_color_sub_background'))
143. }
144. }
```

[WlanSettingItem.ets](https://gitcode.com/harmonyos_samples/NavigationSettings/blob/master/features/settingitems/src/main/ets/wlan/WlanSettingItem.ets#L17-L160)

### 显示刷新

NavDestination组件用于实际刷新Navigation组件Content区域的显示。

开发者可以通过NavDestination组件提供的如下属性，调整其最终显示效果：

* backgroundColor：设置NavDestination组件的背景色。
* title：自定义NavDestination组件的标题。
* hideTitleBar：隐藏NavDestination组件的标题栏。

特别的，Navigation组件会根据当前的状态决定是否在NavDestination组件标题栏起始部分自动添加返回键图标。当Navigation组件添加了返回键图标时，还可以自动响应及处理系统三键导航中的返回键事件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/K0hliisOSEGhhLDrQaOFNA/zh-cn_image_0000002438914430.png?HW-CC-KV=V1&HW-CC-Date=20260428T002131Z&HW-CC-Expire=86400&HW-CC-Sign=BD9102353BCA03475E671E400CFFC206F45F04071D84405A8E2C47D4737757C3 "点击放大")

## 如何实现多级跳转

多级跳转场景下，Navigation组件同样会根据当前的状态决定是否自动添加返回键图标及响应系统三键导航中的返回键事件。

| 一级页面 | 二级页面 |
| --- | --- |
|  |  |

结合具体场景，点击上图3号小红框，跳转至4号红框更多WLAN设置页面，其核心代码实现如下所示。

```
1. import { SubItemArrow } from '../components/SubItemArrow'
2. import { SubItemToggle } from '../components/SubItemToggle'
3. import { ItemGroup } from '../components/ItemGroup'
4. import { ItemDescription } from '../components/ItemDescription'
5. import { Logger } from '@ohos/common/Index'

7. const TAG = "WlanMoreSetting"

9. @Component
10. export struct WlanMoreSettingItem {
11. @LocalStorageLink('selectedLabel') selectedLabel: string = '';
12. @Consume('pathInfos') pathInfos: NavPathStack;

14. build() {
15. SubItemArrow({ title: $r('app.string.moreWlanSettings') })
16. .onClick(() => {
17. this.pathInfos.pushPath({ name: 'WlanMoreSetting' });
18. this.selectedLabel = 'WLAN';
19. })
20. }
21. }

23. @Builder
24. export function WlanMoreSettingBuilder() {
25. WlanMoreSetting();
26. }

28. @Component
29. export struct WlanMoreSetting {

31. private getSettingTitle(): string {
32. let title = "";
33. try {
34. title = this.getUIContext().getHostContext()!.resourceManager.getStringSync($r('app.string.moreWlanSettings').id)
35. } catch(err) {
36. if (err.code) {
37. Logger.error(TAG, `Failed to get setting title. Cause: ${JSON.stringify(err)}`);
38. }
39. }
40. return title;
41. }

43. build() {
44. NavDestination() {
45. Scroll() {
46. Column() {
47. ItemGroup() {
48. SubItemArrow({
49. title: $r('app.string.wlanPlus'),
50. tag: $r('app.string.enabled')
51. })
52. }

54. ItemDescription({ description: $r('app.string.wlanPlusTip') })
55. .margin({
56. top: 8,
57. bottom: 24,
58. left: 12,
59. right: 12
60. })

62. ItemGroup() {
63. SubItemArrow({ title: $r('app.string.wlanDirect') })
64. }

66. Blank().height(12)

68. ItemGroup() {
69. SubItemToggle({ title: $r('app.string.wlanSecurityCheck') })
70. }

72. ItemDescription({ description: $r('app.string.wlanSecurityCheckTip') })
73. .margin({
74. top: 8,
75. bottom: 24,
76. left: 12,
77. right: 12
78. })

80. ItemGroup() {
81. SubItemArrow({ title: $r('app.string.savedWlan') })
82. Divider()
83. .strokeWidth('1px')
84. .color($r('sys.color.ohos_id_color_list_separator'))
85. .margin({ left: 12, right: 8 })
86. SubItemArrow({ title: $r('app.string.installCertificates') })
87. }
88. }
89. .backgroundColor($r('sys.color.ohos_id_color_sub_background'))
90. .padding({ left: 12, right: 12 })
91. }
92. .scrollBar(BarState.Off)
93. .width('100%')
94. }
95. .title(this.getSettingTitle())
96. .backgroundColor($r('sys.color.ohos_id_color_sub_background'))
97. }
98. }
```

[WlanMoreSetting.ets](https://gitcode.com/harmonyos_samples/NavigationSettings/blob/master/features/settingitems/src/main/ets/wlan/WlanMoreSetting.ets#L17-L114)

## 总结

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/ksUlnRXFREW_q5q8ZegpGg/zh-cn_image_0000002321308294.png?HW-CC-KV=V1&HW-CC-Date=20260428T002131Z&HW-CC-Expire=86400&HW-CC-Sign=D2603DF7E830F9D39431FBFA007F77AC228FE4CDBC265B614FDD3E75EC6A0B46 "点击放大")

本示例的基础导航结构上图所示：

* 激活SettingList中的WlanSettingItem，可以加载及显示WlanSetting。
* 激活WlanSetting中的WlanMoreSettingItem，可以加载及显示WlanMoreSetting。

Navigation组件支持自动切换单栏和双栏的显示效果，同时可以根据当前状态自动添加返回键及响应系统的返回键事件。借助Navigation组件，开发者不用关心单栏和双栏场景的差异而更关注于应用本身，极大的减少开发工作量及提高开发效率。

## 示例代码

* [开发设置应用页面功能](https://gitcode.com/HarmonyOS_Samples/NavigationSettings)
