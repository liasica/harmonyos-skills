---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/map-map-buildingoverlay
title: BuildingOverlay
breadcrumb: API参考 > 应用服务 > Map Kit（地图服务） > ArkTS API > map（地图显示功能） > BuildingOverlay
category: harmonyos-references
scraped_at: 2026-04-28T08:17:17+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:cd0fe6658597b100338029c4fd4e2221d0aaae27844bdf07b5f13a125274aa38
---

## 导入模块

PhonePC/2in1TabletWearable

```
1. import { map, mapCommon } from '@kit.MapKit';
```

## BuildingOverlay

PhonePC/2in1TabletWearable

3D建筑。缩放层级达到16级或以上，才可正常显示3D建筑效果。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. let points: Array<mapCommon.LatLng> = [
2. {
3. latitude: 31.984794,
4. longitude: 118.765865
5. },
6. {
7. latitude: 31.98468,
8. longitude: 118.766076
9. },
10. {
11. latitude: 31.98472,
12. longitude: 118.766116
13. },
14. {
15. latitude: 31.98463,
16. longitude: 118.766292
17. },
18. {
19. latitude: 31.984586,
20. longitude: 118.766251
21. },
22. {
23. latitude: 31.984536,
24. longitude: 118.766344
25. },
26. {
27. latitude: 31.984633,
28. longitude: 118.766446
29. },
30. {
31. latitude: 31.9848,
32. longitude: 118.766285
33. },
34. {
35. latitude: 31.984925,
36. longitude: 118.766312
37. },
38. {
39. latitude: 31.985282,
40. longitude: 118.766661
41. },
42. {
43. latitude: 31.985438,
44. longitude: 118.766419
45. },
46. {
47. latitude: 31.985801,
48. longitude: 118.766755
49. },
50. {
51. latitude: 31.985856,
52. longitude: 118.766504
53. },
54. {
55. latitude: 31.985785,
56. longitude: 118.766434
57. },
58. {
59. latitude: 31.985821,
60. longitude: 118.766278
61. },
62. {
63. latitude: 31.985897,
64. longitude: 118.766311
65. },
66. {
67. latitude: 31.985944,
68. longitude: 118.766095
69. },
70. {
71. latitude: 31.985909,
72. longitude: 118.766069
73. },
74. {
75. latitude: 31.985794,
76. longitude: 118.765989
77. },
78. {
79. latitude: 31.9857,
80. longitude: 118.766029
81. },
82. {
83. latitude: 31.985658,
84. longitude: 118.766164
85. },
86. {
87. latitude: 31.985647,
88. longitude: 118.766271
89. },
90. {
91. latitude: 31.985574,
92. longitude: 118.766297
93. },
94. {
95. latitude: 31.985458,
96. longitude: 118.766285
97. },
98. {
99. latitude: 31.985271,
100. longitude: 118.766002
101. },
102. {
103. latitude: 31.985219,
104. longitude: 118.766002
105. },
106. {
107. latitude: 31.985135,
108. longitude: 118.766029
109. },
110. {
111. latitude: 31.985093,
112. longitude: 118.766083
113. },
114. {
115. latitude: 31.985019,
116. longitude: 118.766109
117. },
118. {
119. latitude: 31.984978,
120. longitude: 118.766083
121. },
122. {
123. latitude: 31.984794,
124. longitude: 118.765865
125. }
126. ];
127. // 将点的顺序反转以符合地图绘制要求
128. points.reverse();
129. // 3D建筑参数
130. let buildingOverlayOptions: mapCommon.BuildingOverlayParams =
131. {
132. // 3D建筑的范围参数（点为顺时针绘制）
133. points: points,
134. // 3D建筑的高度
135. totalHeight: 51,
136. // 3D建筑的选中楼层高度
137. floorBottomHeight: 33,
138. // 3D建筑的顶部颜色
139. topFaceColor: 0xffa4b8f7,
140. // 3D建筑的侧面颜色
141. sideFaceColor: 0x44a4b8f7,
142. // 3D建筑的选中楼层颜色
143. floorColor: 0xff000000,
144. // 3D建筑的展示层级
145. showLevel: 14,
146. // 3D建筑选中楼层从底部升起的动画时长
147. animationDuration: 5000,
148. // 3D建筑侧面的纹理
149. sideTexture: {
150. image: $r("app.media.side_tex"),
151. height: 3,
152. width: 3
153. },
154. // 3D建筑选中楼层的纹理
155. floorTexture: {
156. image: $r("app.media.floor_tex"),
157. height: 3,
158. width: 3
159. }
160. }
161. let buildingOverlay: map.BuildingOverlay= await this.mapController.addBuildingOverlay(buildingOverlayOptions);
```

### getId

PhonePC/2in1TabletWearable

getId(): string

返回3D建筑的ID。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 返回3D建筑的ID。 |

**示例：**

```
1. let id: String = buildingOverlay.getId();
```

### remove

PhonePC/2in1TabletWearable

remove(): void

移除3D建筑。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**示例：**

```
1. buildingOverlay.remove();
```

### setSideVisible

PhonePC/2in1TabletWearable

setSideVisible(visible: boolean): void

设置是否显示3D建筑的侧面和顶部。如果不需要显示3D建筑请同时将[setSideVisible](map-map-buildingoverlay.md#setsidevisible)和[setFloorVisible](map-map-buildingoverlay.md#setfloorvisible)设置为false。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| visible | boolean | 是 | 是否显示3D建筑的侧面和顶部。  - true：显示  - false：不显示 |

**示例：**

```
1. buildingOverlay.setSideVisible(true);
```

### setFloorVisible

PhonePC/2in1TabletWearable

setFloorVisible(visible: boolean): void

设置是否显示选中的楼层。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| visible | boolean | 是 | 是否显示建筑的所选楼层。  - true：显示  - false：不显示 |

**示例：**

```
1. buildingOverlay.setFloorVisible(true);
```

### setFloorBottomHeight

PhonePC/2in1TabletWearable

setFloorBottomHeight(height: number): void

设置所选楼层底部到地面的高度。

**模型约束：** 此接口仅可在Stage模型下使用。

**元服务API：** 从版本5.0.0(12)开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.Map.Core

**起始版本：** 5.0.0(12)

**参数**：

| **参数名** | **类型** | 必填 | **说明** |
| --- | --- | --- | --- |
| height | number | 是 | 所选楼层底部到地面的高度，单位：米，取值范围：大于等于0，异常值不处理。 |

**示例：**

```
1. buildingOverlay.setFloorBottomHeight(80);
```
