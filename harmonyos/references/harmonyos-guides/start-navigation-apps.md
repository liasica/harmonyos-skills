---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/start-navigation-apps
title: 拉起导航类应用（startAbilityByType）
breadcrumb: 指南 > 应用框架 > Ability Kit（程序框架服务） > Stage模型开发指导 > 应用间跳转 > 拉起指定类型的应用 > 拉起导航类应用（startAbilityByType）
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:50+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:d566dda0d1a0c33ead210d204a6e57eeb6e1181d7d53cc1dbec4f63d7b5b446d
---

本章节介绍如何拉起导航类应用扩展面板。

## 导航类应用扩展面板参数说明

startAbilityByType接口中type字段为navigation，支持路线规划、导航、位置搜索三种意图场景，对应的wantParam参数如下：

说明

本文中的经纬度均采用GCJ-02坐标系统。

* 路线规划场景

  | 参数名 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | sceneType | number | 否 | 意图场景，表明本次请求对应的操作意图。默认为1，路线规划场景填1或不填。 |
  | originName | string | 否 | 起点名称。 |
  | originLatitude | number | 否 | 起点纬度。 |
  | originLongitude | number | 否 | 起点经度。 |
  | originPoiIds | Record<number, string> | 否 | 起点POI ID列表，当前仅支持传入花瓣地图、高德地图、百度地图的POI ID。 |
  | destinationName | string | 否 | 终点名称。 |
  | destinationLatitude | number | 是 | 终点纬度。 |
  | destinationLongitude | number | 是 | 终点经度。 |
  | destinationPoiIds | Record<number, string> | 否 | 终点POI ID列表，当前仅支持传入花瓣地图、高德地图、百度地图的POI ID。 |
  | vehicleType | number | 否 | 交通出行工具，取值：0-驾车，1-步行，2-骑行，3-公交。 |
* 导航场景

  | 参数名 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | sceneType | number | 是 | 意图场景，表明本次请求对应的操作意图。导航场景填2。 |
  | destinationName | string | 否 | 终点名称。 |
  | destinationLatitude | number | 是 | 终点纬度。 |
  | destinationLongitude | number | 是 | 终点经度。 |
  | destinationPoiIds | Record<number, string> | 否 | 终点POI ID列表，当前仅支持传入花瓣地图、高德地图、百度地图的POI ID。 |
* 位置搜索场景

  | 参数名 | 类型 | 必填 | 说明 |
  | --- | --- | --- | --- |
  | sceneType | number | 是 | 意图场景，表明本次请求对应的操作意图。位置搜索场景填3。 |
  | destinationName | string | 是 | 地点名称。 |

## 拉起方开发步骤

1. 导入相关模块。

   ```
   1. import { common } from '@kit.AbilityKit';
   ```
2. 构造接口参数并调用startAbilityByType接口。

   终点POI ID列表（destinationPoiIds）和起点POI ID列表（originPoiIds）需开发者自行从各地图系统中获取，并按照对应关系传参。

   ```
   1. @Entry
   2. @Component
   3. struct Index {
   4. @State hideAbility: string = 'hideAbility'

   6. build() {
   7. Row() {
   8. Column() {
   9. Text(this.hideAbility)
   10. .fontSize(30)
   11. .fontWeight(FontWeight.Bold)
   12. .onClick(() => {
   13. let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
   14. let wantParam: Record<string, Object> = {
   15. 'sceneType': 1,
   16. 'destinationLatitude': 32.060844,
   17. 'destinationLongitude': 118.78315,
   18. 'destinationName': 'xx市xx路xx号',
   19. 'destinationPoiIds': {
   20. 1: '1001', // key为1代表花瓣地图，value需为花瓣地图POI
   21. 2: '2002', // key为2代表高德地图，value需为高德地图POI
   22. 3: '3003'  // key为3代表百度地图，value需为百度地图POI
   23. } as Record<number, string>,
   24. 'originName': 'xx市xx公园',
   25. 'originLatitude': 31.060844,
   26. 'originLongitude': 120.78315,
   27. 'originPoiIds': {
   28. 1: '1101', // key为1代表花瓣地图，value需为花瓣地图POI
   29. 2: '2202', // key为2代表高德地图，value需为高德地图POI
   30. 3: '3303'  // key为3代表百度地图，value需为百度地图POI
   31. } as Record<number, string>,
   32. 'vehicleType': 0
   33. };
   34. let abilityStartCallback: common.AbilityStartCallback = {
   35. onError: (code: number, name: string, message: string) => {
   36. console.error(`onError code ${code} name: ${name} message: ${message}`);
   37. },
   38. onResult: (result) => {
   39. console.info(`onResult result: ${JSON.stringify(result)}`);
   40. }
   41. }

   43. context.startAbilityByType("navigation", wantParam, abilityStartCallback,
   44. (err) => {
   45. if (err) {
   46. console.error(`startAbilityByType fail, err: ${JSON.stringify(err)}`);
   47. } else {
   48. console.info(`success`);
   49. }
   50. });
   51. });
   52. }
   53. .width('100%')
   54. }
   55. .height('100%')
   56. }
   57. }
   ```

   效果示例图：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/F4hPi9BqQ7KzJMmettLutQ/zh-cn_image_0000002552797856.png?HW-CC-KV=V1&HW-CC-Date=20260427T233749Z&HW-CC-Expire=86400&HW-CC-Sign=3E6E200828953875C56CDFA8B8EA96CD131AFBA02615E5670217AFAE77A8893E)

## 目标方开发步骤

1. 在module.json5中配置[uris](module-configuration-file.md#skills标签)，步骤如下：

   1. 设置linkFeature属性以声明当前应用支持的特性功能，从而系统可以从设备已安装应用中找到当前支持该特性的应用，取值范围如下：

      | 取值 | 含义 |
      | --- | --- |
      | Navigation | 声明应用支持导航功能 |
      | RoutePlan | 声明应用支持路线规划功能 |
      | PlaceSearch | 声明应用支持位置搜索功能 |
   2. 设置scheme、host、port、path/pathStartWith属性，与Want中URI相匹配，以便区分不同功能。

   ```
   1. {
   2. "abilities": [
   3. {
   4. "skills": [
   5. {
   6. "uris": [
   7. {
   8. "scheme": "maps", // 这里仅示意，应用需确保这里声明的uri能被外部正常拉起
   9. "host": "navigation",
   10. "path": "",
   11. "linkFeature": "Navigation" // 声明应用支持导航功能
   12. },
   13. {
   14. "scheme": "maps", // 这里仅示意，应用需确保这里声明的uri能被外部正常拉起
   15. "host": "routePlan",
   16. "path": "",
   17. "linkFeature": "RoutePlan" // 声明应用支持路线规划功能
   18. },
   19. {
   20. "scheme": "maps", // 这里仅示意，应用需确保这里声明的uri能被外部正常拉起
   21. "host": "search",
   22. "path": "",
   23. "linkFeature": "PlaceSearch" // 声明应用支持位置搜索功能
   24. }
   25. ]
   26. }
   27. ]
   28. }
   29. ]
   30. }
   ```
2. 解析参数并做对应处理。

   ```
   1. UIAbility.onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void
   ```

   在参数**want.uri**中会携带目标方配置的linkFeature对应的uri。

   在参数**want.parameters**中会携带Caller方传入的参数，不同场景参数如下所示。

   * 路线规划场景

     | 参数名 | 类型 | 必填 | 说明 |
     | --- | --- | --- | --- |
     | originName | string | 否 | 起点名称。 |
     | originLatitude | number | 否 | 起点纬度。 |
     | originLongitude | number | 否 | 起点经度。 |
     | originPoiId | string | 否 | 起点POI ID，当前仅支持花瓣地图、高德地图、百度地图获取此参数。 |
     | destinationName | string | 否 | 终点名称。 |
     | destinationLatitude | number | 是 | 终点纬度。 |
     | destinationLongitude | number | 是 | 终点经度。 |
     | destinationPoiId | string | 否 | 终点POI ID，当前仅支持花瓣地图、高德地图、百度地图获取此参数。 |
     | vehicleType | number | 否 | 交通出行工具，取值：0-驾车，1-步行，2-骑行，3-公交。 |
   * 导航场景

     | 参数名 | 类型 | 必填 | 说明 |
     | --- | --- | --- | --- |
     | destinationName | string | 否 | 终点名称。 |
     | destinationLatitude | number | 是 | 终点纬度。 |
     | destinationLongitude | number | 是 | 终点经度。 |
     | destinationPoiId | string | 否 | 终点POI ID，当前仅支持花瓣地图、高德地图、百度地图获取此参数。 |
   * 位置搜索场景

     | 参数名 | 类型 | 必填 | 说明 |
     | --- | --- | --- | --- |
     | destinationName | string | 是 | 地点名称。 |

   应用可根据[linkFeature](module-configuration-file.md#skills标签)中定义的特性功能，比如路线规划、导航和位置搜索，结合接收到的uri和参数开发不同的样式页面。

**完整示例：**

```
1. import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
2. import { hilog } from '@kit.PerformanceAnalysisKit';
3. import { window } from '@kit.ArkUI';

5. const TAG = 'EntryAbility';

7. export default class EntryAbility extends UIAbility {
8. windowStage: window.WindowStage | null = null;

10. uri?: string;
11. destinationLatitude?: number;
12. destinationLongitude?: number;
13. destinationName?: string;
14. originName?: string;
15. originLatitude?: number;
16. originLongitude?: number;
17. vehicleType?: number;
18. destinationPoiId?: string;
19. originPoiId?: string;

21. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
22. hilog.info(0x0000, TAG, `onCreate, want=${JSON.stringify(want)}`);
23. super.onCreate(want, launchParam);
24. this.parseWant(want);
25. }

27. onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
28. hilog.info(0x0000, TAG, `onNewWant, want=${JSON.stringify(want)}`);
29. super.onNewWant(want, launchParam);
30. this.parseWant(want);
31. if (!this.windowStage) {
32. hilog.error(0x0000, TAG, 'windowStage is null');
33. this.context.terminateSelf();
34. return;
35. }
36. this.loadPage(this.windowStage);
37. }

39. private parseWant(want: Want): void {
40. this.uri = want.uri as string | undefined;
41. this.destinationLatitude = want.parameters?.destinationLatitude as number | undefined;
42. this.destinationLongitude = want.parameters?.destinationLongitude as number | undefined;
43. this.destinationName = want.parameters?.destinationName as string | undefined;
44. this.originName = want.parameters?.originName as string | undefined;
45. this.originLatitude = want.parameters?.originLatitude as number | undefined;
46. this.originLongitude = want.parameters?.originLongitude as number | undefined;
47. this.vehicleType = want.parameters?.vehicleType as number | undefined;
48. this.destinationPoiId = want.parameters?.destinationPoiId as string | undefined;
49. this.originPoiId = want.parameters?.originPoiId as string | undefined;
50. }

52. private loadPage(windowStage: window.WindowStage): void {
53. hilog.info(0x0000, TAG, `loadPage, uri=${this.uri}`);
54. if (this.uri === 'maps://navigation') {
55. // 构建导航场景参数
56. const storage: LocalStorage = new LocalStorage({
57. "destinationLatitude": this.destinationLatitude,
58. "destinationLongitude": this.destinationLongitude,
59. "destinationPoiId": this.destinationPoiId
60. } as Record<string, Object>);
61. // 拉起导航页面
62. windowStage.loadContent('pages/NavigationPage', storage)
63. } else if (this.uri === 'maps://routePlan') {
64. // 构建路径规划场景参数
65. const storage: LocalStorage = new LocalStorage({
66. "destinationLatitude": this.destinationLatitude,
67. "destinationLongitude": this.destinationLongitude,
68. "destinationName": this.destinationName,
69. "originName": this.originName,
70. "originLatitude": this.originLatitude,
71. "originLongitude": this.originLongitude,
72. "vehicleType": this.vehicleType,
73. "destinationPoiId": this.destinationPoiId,
74. "originPoiId": this.originPoiId
75. } as Record<string, Object>);
76. // 拉起路径规划页面
77. windowStage.loadContent('pages/RoutePlanPage', storage)
78. }  else if (this.uri === 'maps://search') {
79. // 构建位置搜索场景参数
80. const storage: LocalStorage = new LocalStorage({
81. "destinationName": this.destinationName
82. } as Record<string, Object>);
83. // 拉起位置搜索页面
84. windowStage.loadContent('pages/PlaceSearchPage', storage)
85. } else {
86. // 默认拉起首页
87. windowStage.loadContent('pages/Index', (err) => {
88. if (err.code) {
89. hilog.error(0x0000, TAG, 'Failed to load the content. Cause: %{public}s',
90. JSON.stringify(err) ?? '');
91. return;
92. }
93. hilog.info(0x0000, TAG, 'Succeeded in loading the content.');
94. });
95. }
96. }

98. onDestroy(): void {
99. hilog.info(0x0000, TAG, `onDestroy`);
100. }

102. onWindowStageCreate(windowStage: window.WindowStage): void {
103. hilog.info(0x0000, TAG, `onWindowStageCreate`);
104. this.windowStage = windowStage;
105. this.loadPage(this.windowStage);
106. }

108. onWindowStageDestroy(): void {
109. hilog.info(0x0000, TAG, '%{public}s', 'Ability onWindowStageDestroy');
110. }

112. onForeground(): void {
113. hilog.info(0x0000, TAG, '%{public}s', 'Ability onForeground');
114. }

116. onBackground(): void {
117. hilog.info(0x0000, TAG, '%{public}s', 'Ability onBackground');
118. }
119. }
```
