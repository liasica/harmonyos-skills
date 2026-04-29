---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-4
title: 设置地图Logo始终显示
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit常见问题 > 设置地图Logo始终显示
category: harmonyos-guides
scraped_at: 2026-04-29T13:39:21+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:ebd339d97c4247b59b9f127de3d70348c7de1afb972ca53c538270dde89e4954
---

**现象描述**

Map Kit地图Logo不可见。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/LCPL3o4KRUKO-OFQnQiRmA/zh-cn_image_0000002558765558.jpg?HW-CC-KV=V1&HW-CC-Date=20260429T053919Z&HW-CC-Expire=86400&HW-CC-Sign=2B11D117EFD10FD6FF473F7165406EDEE5C720DBB2E03BAAB25D392CAB19CDB8 "点击放大")

**可能原因**

用户在开发过程中，若地图Logo被其他UI控件或页面元素覆盖，则可能导致Logo不可见。

**处理步骤**

Map Kit无法隐藏地图Logo，用户可通过调整地图组件的边距或布局，确保地图Logo不被其他控件遮挡。解决方案参考如下代码：

```
1. import { MapComponent, mapCommon, map } from '@kit.MapKit';
2. import { AsyncCallback } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct MapKitAppDemo {
7. private mapOptions?: mapCommon.MapOptions;
8. private callback?: AsyncCallback<map.MapComponentController>;
9. private mapController?: map.MapComponentController;
10. private mapEventManager?: map.MapEventManager;
11. private TAG = 'MapKitAppDemo';
12. @State isShowSheet: boolean = true;

14. @Builder
15. Panel() {
16. Column() {
17. Row() {
18. Text() {
19. SymbolSpan($r('sys.symbol.magnifyingglass'))
20. .fontSize(24)
21. .fontColor([Color.Gray])
22. }

24. TextInput()
25. .layoutWeight(1)
26. .backgroundColor('#33b1afaf')
27. .borderRadius(24)
28. .margin({ left: 8, right: 8 })
29. }
30. .backgroundColor(Color.White)
31. .width('100%')
32. }
33. .borderRadius(10)
34. .padding({
35. top: 8,
36. left: 8,
37. right: 8,
38. bottom: 4
39. })
40. .width('100%')
41. }

43. aboutToAppear() {
44. // 地图初始化参数，设置地图中心点坐标及层级
45. this.mapOptions = {
46. position: {
47. target: {
48. latitude: 31.979227,
49. longitude: 118.762245
50. },
51. zoom: 17
52. }
53. };

55. // 地图初始化的回调
56. this.callback = async (err, mapController) => {
57. if (!err) {
58. // 获取地图的控制器类，用来操作地图
59. this.mapController = mapController;
60. // 返回地图组件的监听事件管理接口
61. this.mapEventManager = this.mapController.getEventManager();
62. let callback = () => {
63. console.info(this.TAG, `on-mapLoad`);
64. }
65. // 监听地图加载事件
66. this.mapEventManager?.on('mapLoad', callback);
67. } else {
68. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
69. }
70. }
71. }

73. aboutToDisappear(): void {
74. this.mapEventManager?.off('mapLoad');
75. this.mapController?.clear();
76. }

78. private bindSheetOptions() {
79. let bindSheetOptions = {
80. // 半模态框三个状态的高度
81. detents: [100, 300, 500],
82. // 半模态所在页面允许交互
83. enableOutsideInteractive: true,
84. maskColor: Color.Transparent,
85. backgroundColor: Color.White,
86. blurStyle: BlurStyle.Thick,
87. showClose: false,
88. preferType: SheetType.CENTER,
89. onAppear: () => {
90. this.mapController?.setPadding({
91. bottom: 358
92. })
93. },
94. onHeightDidChange: (height: number) => {
95. // 动态设置地图底部边距，避免遮挡logo
96. this.mapController?.setPadding({
97. bottom: height + 8
98. })
99. }
100. } as BindOptions
101. return bindSheetOptions;
102. }

104. build() {
105. Stack() {
106. Column() {
107. // 调用MapComponent组件初始化地图
108. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
109. .width('100%')
110. .height('100%')
111. Column()
112. .bindSheet(this.isShowSheet, this.Panel(), this.bindSheetOptions())
113. .visibility(this.isShowSheet ? Visibility.Visible : Visibility.None)
114. .justifyContent(FlexAlign.Start)
115. }
116. }
117. .height('100%')
118. .width('100%')
119. }
120. }
```

展示效果如图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/0LEwYHxiREqhf-6Jm-kFyw/zh-cn_image_0000002558605902.gif?HW-CC-KV=V1&HW-CC-Date=20260429T053919Z&HW-CC-Expire=86400&HW-CC-Sign=EE93101231F369E7C5A6C19E9D3AAAA4E88516C7BF487407EA73F0713DCA980C "点击放大")
