---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-traceoverlay
title: TraceOverlay
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > TraceOverlay
category: harmonyos-references
scraped_at: 2026-04-28T08:17:17+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8c8c70961ced23c60f81b899e80755bdafefa6b2e65f4acc32e8982a9f043b4b
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## TraceOverlay

PhonePC/2in1TabletWearable

动态轨迹。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. // marker1的参数
2. let markerOptions1: mapCommon.MarkerOptions = {
3. position: {
4. latitude: 31.99227173519985,
5. longitude: 118.7622219990476
6. },
7. // 图标需存放在resources/base/media目录下
8. icon: $r("app.media.track_setting_sport_map_marker_22"),
9. anchorU: 0.5,
10. anchorV: 1,
11. visible: true
12. };
13. // 新增marker1
14. let markerBoy1 = await this.mapController.addMarker(markerOptions1);
15. let boyImages1: map.PlayImageAnimation = new map.PlayImageAnimation();
16. boyImages1.setDuration(1000);
17. let resourceArray: Array<Resource> = new Array();
18. resourceArray.push($r("app.media.side_0"));
19. resourceArray.push($r("app.media.side_1"));
20. resourceArray.push($r("app.media.side_2"));
21. resourceArray.push($r("app.media.side_3"));
22. resourceArray.push($r("app.media.side_4"));
23. resourceArray.push($r("app.media.side_5"));
24. resourceArray.push($r("app.media.side_6"));
25. resourceArray.push($r("app.media.side_7"));
26. resourceArray.push($r("app.media.side_8"));
27. resourceArray.push($r("app.media.side_9"));
28. resourceArray.push($r("app.media.side_10"));
29. resourceArray.push($r("app.media.side_11"));
30. resourceArray.push($r("app.media.side_12"));
31. resourceArray.push($r("app.media.side_13"));
32. resourceArray.push($r("app.media.side_14"));
33. resourceArray.push($r("app.media.side_15"));
34. resourceArray.push($r("app.media.side_16"));
35. resourceArray.push($r("app.media.side_17"));
36. resourceArray.push($r("app.media.side_18"));
37. resourceArray.push($r("app.media.side_19"));
38. resourceArray.push($r("app.media.side_20"));
39. await boyImages1.addImages(resourceArray);
40. boyImages1.setRepeatCount(-1);

42. // marker1添加动画
43. markerBoy1.setAnimation(boyImages1);
44. markerBoy1.startAnimation();

46. // marker2的参数
47. let markerOptions2: mapCommon.MarkerOptions = {
48. position: {
49. latitude: 31.99227173519985,
50. longitude: 118.7622219990476
51. },
52. // 图标需存放在resources/base/media目录下
53. icon: $r("app.media.track_setting_sport_map_marker_22"),
54. anchorU: 0.5,
55. anchorV: 1,
56. visible: false
57. };
58. // 新增marker2
59. let markerBoy2 = await this.mapController.addMarker(markerOptions2);
60. let boyImages2: map.PlayImageAnimation = new map.PlayImageAnimation();
61. boyImages2.setDuration(1000);
62. let resourceArray2: Array<Resource> = new Array();
63. resourceArray2.push($r("app.media.behavior_front_cycling_boy_000"));
64. resourceArray2.push($r("app.media.behavior_front_cycling_boy_001"));
65. resourceArray2.push($r("app.media.behavior_front_cycling_boy_002"));
66. resourceArray2.push($r("app.media.behavior_front_cycling_boy_003"));
67. resourceArray2.push($r("app.media.behavior_front_cycling_boy_004"));
68. resourceArray2.push($r("app.media.behavior_front_cycling_boy_005"));
69. resourceArray2.push($r("app.media.behavior_front_cycling_boy_006"));
70. resourceArray2.push($r("app.media.behavior_front_cycling_boy_007"));
71. resourceArray2.push($r("app.media.behavior_front_cycling_boy_008"));
72. resourceArray2.push($r("app.media.behavior_front_cycling_boy_009"));
73. resourceArray2.push($r("app.media.behavior_front_cycling_boy_010"));
74. resourceArray2.push($r("app.media.behavior_front_cycling_boy_011"));
75. resourceArray2.push($r("app.media.behavior_front_cycling_boy_012"));
76. resourceArray2.push($r("app.media.behavior_front_cycling_boy_013"));
77. resourceArray2.push($r("app.media.behavior_front_cycling_boy_014"));
78. resourceArray2.push($r("app.media.behavior_front_cycling_boy_015"));
79. resourceArray2.push($r("app.media.behavior_front_cycling_boy_016"));
80. resourceArray2.push($r("app.media.behavior_front_cycling_boy_017"));
81. resourceArray2.push($r("app.media.behavior_front_cycling_boy_018"));
82. await boyImages2.addImages(resourceArray2);
83. boyImages2.setRepeatCount(-1);
84. // marker2添加动画
85. markerBoy2.setAnimation(boyImages2);
86. markerBoy2.startAnimation();

88. let points: Array<mapCommon.LatLng> = new Array();
89. points.push({ latitude: 31.99685233070878, longitude: 118.75846023442728 });
90. points.push({ latitude: 31.99671325810786, longitude: 118.75846738985165 });
91. points.push({ latitude: 31.99659191076709, longitude: 118.7585347621686 });
92. points.push({ latitude: 31.99648202537233, longitude: 118.7586266510386 });
93. points.push({ latitude: 31.99637707201552, longitude: 118.75872004590596 });
94. points.push({ latitude: 31.996278207010903, longitude: 118.75880449946251 });
95. points.push({ latitude: 31.996187481969695, longitude: 118.7588781960278 });
96. points.push({ latitude: 31.996092248919354, longitude: 118.75895330554488 });
97. points.push({ latitude: 31.995962740450565, longitude: 118.75904721407304 });
98. points.push({ latitude: 31.995792921394, longitude: 118.75916904998051 });
99. points.push({ latitude: 31.995601885713416, longitude: 118.7593235241019 });
100. points.push({ latitude: 31.995398221178277, longitude: 118.75949998588176 });
101. points.push({ latitude: 31.995185902197715, longitude: 118.7596871082939 });
102. points.push({ latitude: 31.994983473052656, longitude: 118.75987334062296 });
103. points.push({ latitude: 31.99482433699269, longitude: 118.76002095184032 });
104. points.push({ latitude: 31.994709073721708, longitude: 118.76012902920532 });
105. points.push({ latitude: 31.99460732100702, longitude: 118.76023892576234 });
106. points.push({ latitude: 31.99449284962087, longitude: 118.7603694232856 });
107. points.push({ latitude: 31.99435358179254, longitude: 118.76053622438056 });
108. points.push({ latitude: 31.99420771148339, longitude: 118.76072790126692 });
109. points.push({ latitude: 31.994075194901523, longitude: 118.7609100960977 });
110. points.push({ latitude: 31.993952686158877, longitude: 118.7610741329013 });
111. points.push({ latitude: 31.993840180644217, longitude: 118.7612193418965 });
112. points.push({ latitude: 31.993733787150244, longitude: 118.76135383115654 });
113. points.push({ latitude: 31.993617206525155, longitude: 118.76150529647698 });

115. // 动态轨迹的入参
116. let traceOptions: mapCommon.TraceOverlayParams = {
117. // 轨迹点
118. points: points,
119. // 轨迹的动画时长
120. animationDuration: 5000,
121. // 相机是否跟随动画移动
122. isMapMoving: true,
123. // 轨迹的颜色
124. color: 0xAAFFAA00,
125. // 轨迹的宽度
126. width: 20,
127. // 轨迹的动画回调（回调轨迹点的index）
128. animationCallback: (pointIndex) => {
129. // 换成骑行
130. if (pointIndex === 10) {
131. markerBoy1.setVisible(false);
132. markerBoy2.setVisible(true);
133. }
134. }
135. };
136. let markers: Array<map.Marker> = new Array();
137. markers.push(markerBoy1, markerBoy2);
138. // 新增轨迹点动画
139. let traceOverlay: map.TraceOverlay = await this.mapController.addTraceOverlay(traceOptions, markers);
```

### getId

PhonePC/2in1TabletWearable

getId(): string

返回动态轨迹的ID。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回动态轨迹的ID。 |

**示例：**

```
1. let id: string = traceOverlay.getId();
```

### remove

PhonePC/2in1TabletWearable

remove(): void

删除动态轨迹。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. traceOverlay.remove();
```

### pause

PhonePC/2in1TabletWearable

pause(): void

暂停动态轨迹回放。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. traceOverlay.pause();
```

### resume

PhonePC/2in1TabletWearable

resume(): void

恢复动态轨迹回放。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. traceOverlay.resume();
```
