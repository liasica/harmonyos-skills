---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-prefetcher
title: @ohos.arkui.Prefetcher (Prefetching)
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > @ohos.arkui.Prefetcher (Prefetching)
category: harmonyos-references
scraped_at: 2026-04-29T13:50:32+08:00
doc_updated_at: 2026-03-09
content_hash: sha256:9f84d211673b6afc4e698eda8513731aee004e4009cf7304016141f1a4b64451
---

配合LazyForEach，为List、Grid、WaterFlow和Swiper等容器组件滑动浏览时提供内容预加载能力，提升用户浏览体验。

说明

* 本模块首批接口从API version 12开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 本模块内的接口不支持在预览器中使用。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { BasicPrefetcher, IDataSourcePrefetching, IPrefetcher } from '@kit.ArkUI';
```

## IPrefetcher

PhonePC/2in1TabletTVWearable

实现此接口以提供预取能力。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### setDataSource

PhonePC/2in1TabletTVWearable

setDataSource(dataSource: IDataSourcePrefetching): void;

设置支持预取的数据源以绑定到Prefetcher。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataSource | [IDataSourcePrefetching](js-apis-arkui-prefetcher.md#idatasourceprefetching) | 是 | 支持预取能力的数据源。 |

```
1. class MyPrefetcher implements IPrefetcher {
2. private dataSource?: IDataSourcePrefetching;

4. setDataSource(dataSource: IDataSourcePrefetching): void {
5. this.dataSource = dataSource;
6. }

8. visibleAreaChanged(minVisible: number, maxVisible: number): void {
9. this.dataSource?.prefetch(minVisible);
10. }
11. }
```

### visibleAreaChanged

PhonePC/2in1TabletTVWearable

visibleAreaChanged(minVisible: number, maxVisible: number): void;

当可见区域边界发生改变时调用此方法。支持与List、Grid、WaterFlow和Swiper组件配合使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| minVisible | number | 是 | 列表可见区域的上界。 |
| maxVisible | number | 是 | 列表可见区域的下界。 |

```
1. class MyPrefetcher implements IPrefetcher {
2. private dataSource?: IDataSourcePrefetching;

4. setDataSource(dataSource: IDataSourcePrefetching): void {
5. this.dataSource = dataSource;
6. }

8. visibleAreaChanged(minVisible: number, maxVisible: number): void {
9. this.dataSource?.prefetch(minVisible);
10. }
11. }
```

## BasicPrefetcher

PhonePC/2in1TabletTVWearable

BasicPrefetcher是IPrefetcher的基础实现。它提供了一种智能数据预取算法，以根据屏幕上可见区域的实时变化和预取持续时间的变化来决定应预取哪些数据项。它还可以根据用户的滚动操作来确定哪些预取请求应该被取消。

BasicPrefetcher对象不支持使用JSON序列化。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### constructor

PhonePC/2in1TabletTVWearable

constructor(dataSource?: IDataSourcePrefetching);

传入支持预取的DataSource以绑定到Prefetcher。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataSource | [IDataSourcePrefetching](js-apis-arkui-prefetcher.md#idatasourceprefetching) | 否 | 支持预取能力的数据源。 |

### setDataSource

PhonePC/2in1TabletTVWearable

setDataSource(dataSource: IDataSourcePrefetching): void;

设置支持预取的DataSource以绑定到Prefetcher。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| dataSource | [IDataSourcePrefetching](js-apis-arkui-prefetcher.md#idatasourceprefetching) | 是 | 支持预取能力的数据源。 |

### visibleAreaChanged

PhonePC/2in1TabletTVWearable

visibleAreaChanged(minVisible: number, maxVisible: number): void;

当可见区域边界发生改变时调用此方法。支持与List、Grid、WaterFlow和Swiper组件配合使用。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| minVisible | number | 是 | 列表可见区域的上界。 |
| maxVisible | number | 是 | 列表可见区域的下界。 |

## IDataSourcePrefetching

PhonePC/2in1TabletTVWearable

继承自[IDataSource](ts-rendering-control-lazyforeach.md#idatasource)。实现该接口，提供具备预取能力的DataSource。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

### prefetch

PhonePC/2in1TabletTVWearable

prefetch(index: number): Promise<void> | void;

从数据集中预取指定的元素。该方法可以为同步，也可为异步。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 预取数据项索引值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | void | 异步执行时返回Promise对象，同步执行时无返回值。Promise仅表示操作完成，无实际返回内容。 |

### cancel

PhonePC/2in1TabletTVWearable

cancel?(index: number): Promise<void> | void;

取消从数据集中预取指定的元素。该方法可以为同步，也可为异步。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 取消预取数据项索引值。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise<void> | void | 异步执行时返回Promise对象，同步执行时无返回值。Promise仅表示操作完成，无实际返回内容。 |

列表内容移出屏幕时（比如列表快速滑动场景下），预取算法判断屏幕以外的Item可以被取消预取时，该方法即会被调用。例如，如果HTTP框架支持请求取消，则可以在此处取消在prefetch中发起的网络请求。

## 示例

PhonePC/2in1TabletTVWearable

下面示例展示了Prefetcher的预加载能力。该示例采用分页的方式，配合LazyForEach实现懒加载效果，并通过添加延时来模拟加载过程。

```
1. import { BasicPrefetcher, IDataSourcePrefetching } from '@kit.ArkUI';
2. import { image } from '@kit.ImageKit';

4. const ITEMS_ON_SCREEN = 8;

6. @Entry
7. @Component
8. struct PrefetcherDemoComponent {
9. private page: number = 1;
10. private pageSize: number = 50;
11. private breakPoint: number = 25;
12. private readonly fetchDelayMs: number = 500;
13. private readonly dataSource = new MyDataSource(this.page, this.pageSize, this.fetchDelayMs);
14. private readonly prefetcher = new BasicPrefetcher(this.dataSource);

16. build() {
17. Column() {
18. List() {
19. LazyForEach(this.dataSource, (item: PictureItem, index: number) => {
20. ListItem() {
21. PictureItemComponent({ info: item })
22. .height(`${100 / ITEMS_ON_SCREEN}%`)
23. }
24. .onAppear(() => {
25. if (index >= this.breakPoint) {
26. this.dataSource.getHttpData(++this.page, this.pageSize);
27. this.breakPoint = this.dataSource.totalCount() - this.pageSize / 2;
28. }
29. })
30. }, (item: PictureItem) => item.title)
31. }
32. .onScrollIndex((start: number, end: number) => {
33. this.prefetcher.visibleAreaChanged(start, end);
34. })
35. }
36. }
37. }

39. @Component
40. struct PictureItemComponent {
41. @ObjectLink info: PictureItem;

43. build() {
44. Row() {
45. Image(this.info.imagePixelMap)
46. .objectFit(ImageFit.Contain)
47. .width('40%')
48. Text(this.info.title)
49. .width('60%')
50. }
51. }
52. }

54. @Observed
55. class PictureItem {
56. readonly color: number;
57. title: string;
58. imagePixelMap: image.PixelMap | undefined;
59. key: string;

61. constructor(color: number, title: string) {
62. this.color = color;
63. this.title = title;
64. this.key = title;
65. }
66. }

68. type ItemIndex = number;
69. type TimerId = number;

71. class MyDataSource implements IDataSourcePrefetching {
72. private readonly items: PictureItem[];
73. private readonly fetchDelayMs: number;
74. private readonly fetches: Map<ItemIndex, TimerId> = new Map();
75. private readonly listeners: DataChangeListener[] = [];

77. constructor(pageNum: number, pageSize: number, fetchDelayMs: number) {
78. this.items = [];
79. this.fetchDelayMs = fetchDelayMs;
80. this.getHttpData(pageNum, pageSize);
81. }

83. async prefetch(index: number): Promise<void> {
84. const item = this.items[index];
85. if (item.imagePixelMap) {
86. return;
87. }

89. // 模拟高耗时操作
90. return new Promise<void>(resolve => {
91. const timeoutId = setTimeout(async () => {
92. this.fetches.delete(index);
93. const bitmap = create10x10Bitmap(item.color);
94. const imageSource: image.ImageSource = image.createImageSource(bitmap);
95. item.imagePixelMap = await imageSource.createPixelMap();
96. resolve();
97. }, this.fetchDelayMs);

99. this.fetches.set(index, timeoutId)
100. });
101. }

103. cancel(index: number): void {
104. const timerId = this.fetches.get(index);
105. if (timerId) {
106. this.fetches.delete(index);
107. clearTimeout(timerId);
108. }
109. }

111. // 模拟分页方式加载数据
112. getHttpData(pageNum: number, pageSize:number): void {
113. const newItems: PictureItem[] = [];
114. for (let i = (pageNum - 1) * pageSize; i < pageNum * pageSize; i++) {
115. const item = new PictureItem(getRandomColor(), `Item ${i}`);
116. newItems.push(item);
117. }
118. const startIndex = this.items.length;
119. this.items.splice(startIndex, 0, ...newItems);
120. this.notifyBatchUpdate([
121. {
122. type: DataOperationType.ADD,
123. index: startIndex,
124. count: newItems.length,
125. key: newItems.map((item) => item.title)
126. }
127. ]);
128. }

130. private notifyBatchUpdate(operations: DataOperation[]) {
131. this.listeners.forEach((listener: DataChangeListener) => {
132. listener.onDatasetChange(operations);
133. });
134. }

136. totalCount(): number {
137. return this.items.length;
138. }

140. getData(index: number): PictureItem {
141. return this.items[index];
142. }

144. registerDataChangeListener(listener: DataChangeListener): void {
145. if (this.listeners.indexOf(listener) < 0) {
146. this.listeners.push(listener);
147. }
148. }

150. unregisterDataChangeListener(listener: DataChangeListener): void {
151. const pos = this.listeners.indexOf(listener);
152. if (pos >= 0) {
153. this.listeners.splice(pos, 1);
154. }
155. }
156. }

158. function getRandomColor(): number {
159. const maxColorCode = 256;
160. const r = Math.floor(Math.random() * maxColorCode);
161. const g = Math.floor(Math.random() * maxColorCode);
162. const b = Math.floor(Math.random() * maxColorCode);

164. return (r * 256 + g) * 256 + b;
165. }

167. function create10x10Bitmap(color: number): ArrayBuffer {
168. const height = 10;
169. const width = 10;

171. const fileHeaderLength = 14;
172. const bitmapInfoLength = 40;
173. const headerLength = fileHeaderLength + bitmapInfoLength;
174. const pixelSize = (width * 3 + 2) * height;

176. let length = pixelSize + headerLength;

178. const buffer = new ArrayBuffer(length);
179. const view16 = new Uint16Array(buffer);

181. view16[0] = 0x4D42;
182. view16[1] = length & 0xffff;
183. view16[2] = length >> 16;
184. view16[5] = headerLength;

186. let offset = 7;
187. view16[offset++] = bitmapInfoLength & 0xffff;
188. view16[offset++] = bitmapInfoLength >> 16;
189. view16[offset++] = width & 0xffff;
190. view16[offset++] = width >> 16;
191. view16[offset++] = height & 0xffff;
192. view16[offset++] = height >> 16;
193. view16[offset++] = 1;
194. view16[offset++] = 24;

196. const b = color & 0xff;
197. const g = (color >> 8) & 0xff;
198. const r = color >> 16;
199. offset = headerLength;
200. const view8 = new Uint8Array(buffer);
201. for (let y = 0; y < height; y++) {
202. for (let x = 0; x < width; x++) {
203. view8[offset++] = b;
204. view8[offset++] = g;
205. view8[offset++] = r;
206. }
207. offset += 2;
208. }

210. return buffer;
211. }
```

演示效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/MKLByu2gRD-u81IRXo_xLQ/zh-cn_image_0000002589245735.gif?HW-CC-KV=V1&HW-CC-Date=20260429T055030Z&HW-CC-Expire=86400&HW-CC-Sign=4ABD3F9CF392179DFB338964185F4CCD8201E38111674DEDF16F88E8F172D6CC)

## 补充说明

PhonePC/2in1TabletTVWearable

开发者也可使用HarmonyOS三方库[@netteam/prefetcher](https://ohpm.openharmony.cn/#/cn/detail/@netteam%2Fprefetcher)开发预加载功能。该三方库提供了更多的接口，可以更加便捷有效地实现数据预加载。
