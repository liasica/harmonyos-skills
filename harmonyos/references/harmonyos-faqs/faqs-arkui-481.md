---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-481
title: 组件截图（ComponentSnapshot）返回错误码100001，可能原因为截图尺寸过大，文档说明其与具体硬件限制有关，如何查看具体限制是多少
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 组件截图（ComponentSnapshot）返回错误码100001，可能原因为截图尺寸过大，文档说明其与具体硬件限制有关，如何查看具体限制是多少
category: harmonyos-faqs
scraped_at: 2026-04-28T08:27:07+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:7cd30f153e1d217467285bdc3b11cd1bccb7567c23cb9f772e5451accd3b63b1
---

硬件限制因平台而异，可以通过如下命令进行查看：

```
1. hdc shell hidumper -s 10 -a 'vktextureLimit'
```

常见值为“width: 8192 height: 8192”，表示最大绘制纹理尺寸的长宽都需要在8192像素以内。比较待截图组件的尺寸，以便确认截图失败是否为该原因导致，如果是，请调整所截图组件的大小，或实现为滚动截图后自行拼接。实现请参考[截取长内容（滚动截图）](../harmonyos-guides/arkts-uicontext-component-snapshot.md#截取长内容滚动截图)和[长截图](../best-practices/bpta-long-snapshot-practice.md)。

如需实现离屏组件的长截图，可参考以下实现：

```
1. // src/main/ets/utils/Utils.ets
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';

5. export class Utils {
6. static sleep(ms: number): Promise<void> {
7. return new Promise(resolve => setTimeout(resolve, ms));
8. }

10. // Calculate the valid screenshot area
11. static async getSnapshotArea(context: UIContext, pixelMap: PixelMap, scrollYOffsets: number[], listWidth: number,
12. listHeight: number): Promise<image.PositionArea> {
13. let stride = pixelMap.getBytesNumberPerRow();
14. let bytesNumber = pixelMap.getPixelBytesNumber();
15. let buffer: ArrayBuffer = new ArrayBuffer(bytesNumber);
16. let len = scrollYOffsets.length;

18. if (scrollYOffsets.length >= 2) {
19. let realScrollHeight = scrollYOffsets[len-1] - scrollYOffsets[len-2];
20. if (listHeight - realScrollHeight > 0) {
21. let cropRegion: image.Region = {
22. x: 0,
23. y: context.vp2px(listHeight - realScrollHeight) || 0,
24. size: {
25. height: context.vp2px(realScrollHeight) || 0,
26. width: context.vp2px(listWidth) || 0
27. }
28. };
29. await pixelMap.crop(cropRegion);
30. }
31. }

33. let area: image.PositionArea = {
34. pixels: buffer,
35. offset: 0,
36. stride: stride,
37. region: {
38. size: {
39. width: 0,
40. height: 0
41. },
42. x: 0,
43. y: 0
44. }
45. }

47. try {
48. let imgInfo = pixelMap.getImageInfoSync();
49. area.region.size.width = imgInfo.size.width;
50. area.region.size.height = imgInfo.size.height;
51. pixelMap.readPixelsSync(area);
52. } catch (err) {
53. let error = err as BusinessError;
54. console.error(`getSnapshotArea err, code:${error.code}, message: ${error.message}`);
55. }
56. return area;
57. }

59. // Graphic splicing
60. static async mergeImage(context: UIContext, areaArray: image.PositionArea[], lastOffsetY: number, listWidth: number,
61. listHeight: number): Promise<PixelMap> {
62. let opts: image.InitializationOptions = {
63. editable: true,
64. pixelFormat: 4,
65. size: {
66. width: context.vp2px(listWidth) || 0,
67. height: context.vp2px(lastOffsetY + listHeight) || 0
68. }
69. };
70. let longPixelMap = image.createPixelMapSync(opts);
71. let imgPosition: number = 0;

73. for (let i = 0; i < areaArray.length; i++) {
74. let readArea = areaArray[i];
75. let area: image.PositionArea = {
76. pixels: readArea.pixels,
77. offset: 0,
78. stride: readArea.stride,
79. region: {
80. size: {
81. width: readArea.region.size.width,
82. height: readArea.region.size.height
83. },
84. x: 0,
85. y: imgPosition
86. }
87. }
88. imgPosition += readArea.region.size.height;
89. try {
90. longPixelMap.writePixelsSync(area);
91. } catch (err) {
92. let error = err as BusinessError;
93. console.error(`writePixelsSync err, code:${error.code}, message: ${error.message}`);
94. }
95. }
96. return longPixelMap;
97. }
98. }
```

[Utils.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/utils/Utils.ets#L21-L119)

```
1. // src/main/ets/pages/Index.ets
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { Utils } from '../utils/Utils';

6. export class MyDataSource {
7. private _data: string[] = [];
8. private _listeners: DataChangeListener[] = [];

10. pushData(data: string): void {
11. this._data.push(data);
12. this._listeners.forEach(listener => {
13. listener.onDataAdd(this._data.length - 1);
14. })
15. }

17. getAllData(): string[] {
18. return this._data;
19. }

21. totalCount(): number {
22. return this._data.length;
23. }

25. getData(index: number): string {
26. return this._data[index];
27. }

29. registerDataChangeListener(listener: DataChangeListener): void {
30. this._listeners.push(listener);
31. }

33. unregisterDataChangeListener(listener: DataChangeListener): void {
34. const index = this._listeners.indexOf(listener);
35. if (index != -1) {
36. this._listeners.splice(index, 1);
37. }
38. }
39. }

41. @Entry
42. @Component
43. struct SnapshotExample {
44. private scroller: Scroller = new Scroller();
45. private listComponentWidth: number = 0;
46. private listComponentHeight: number = 0;
47. @State mergedImage: PixelMap | undefined = undefined;
48. private areaArray: image.PositionArea[] = [];
49. private scrollYOffsets: number[] = [];
50. private data: MyDataSource = new MyDataSource();
51. private listId: string = 'LIST_ID';

53. aboutToAppear(): void {
54. for (let i = 0; i < 50; i++) {
55. this.data.pushData(`Hello ${i}`);
56. }
57. }

59. async onceSnapshot() {
60. await this.beforeSnapshot();
61. await this.snapAndMerge();
62. this.afterGeneratorImage();
63. }

65. async snapAndMerge() {
66. try {
67. // Record the current scrolling position
68. this.scrollYOffsets.push(this.scroller.currentOffset().yOffset);
69. // Take a screenshot of the current display part of the component
70. const pixelMap = await this.getUIContext().getComponentSnapshot().get(this.listId);
71. // Calculate the valid screenshot area
72. let area: image.PositionArea =
73. await Utils.getSnapshotArea(this.getUIContext(), pixelMap, this.scrollYOffsets, this.listComponentWidth,
74. this.listComponentHeight);
75. this.areaArray.push(area);
76. // Determine whether to scroll to the bottom
77. if (!this.scroller.isAtEnd()) {
78. // Not to the bottom: Scroll down by one screen height
79. this.scroller.scrollTo({
80. xOffset: 0,
81. yOffset: (this.scroller.currentOffset().yOffset + this.listComponentHeight),
82. animation: {
83. duration: 200
84. }
85. });
86. await Utils.sleep(200);
87. await this.snapAndMerge();
88. } else {
89. this.mergedImage =
90. await Utils.mergeImage(this.getUIContext(), this.areaArray, this.scrollYOffsets[this.scrollYOffsets.length-1],
91. this.listComponentWidth, this.listComponentHeight);
92. }
93. } catch (err) {
94. let error = err as BusinessError;
95. console.error(`snapAndMerge err, code:${error.code}, message: ${error.message}`);
96. }
97. }

99. async beforeSnapshot() {
100. try {
101. this.scroller.scrollTo({
102. xOffset: 0,
103. yOffset: 0,
104. animation: {
105. duration: 200
106. }
107. });
108. await Utils.sleep(200);
109. } catch (err) {
110. let error = err as BusinessError;
111. console.error(`beforeSnapshot err, code:${error.code}, message: ${error.message}`);
112. }
113. }

115. afterGeneratorImage() {
116. this.scrollYOffsets.length = 0;
117. this.areaArray.length = 0;
118. }

120. build() {
121. Column({ space: 12 }) {
122. Button('Click to get the snapshot')
123. .onClick(() => {
124. this.onceSnapshot();
125. })
126. Stack() {
127. // Screenshot component
128. List({ space: 12, scroller: this.scroller }) {
129. LazyForEach(this.data, (item: string) => {
130. ListItem() {
131. Row() {
132. Text(item)
133. .fontSize(50)
134. .height(50)
135. }
136. }
137. }, (item: number) => item.toString())
138. }
139. .scrollBar(BarState.Off)
140. .cachedCount(3)
141. .width('100%')
142. .height('100%')
143. .backgroundColor($r('sys.color.background_secondary'))
144. .id(this.listId)
145. .onAreaChange((oldValue, newValue) => {
146. this.listComponentWidth = newValue.width as number;
147. this.listComponentHeight = newValue.height as number;
148. })
149. // Set the Z-sequence to -1 to ensure that this component is invisible
150. .zIndex(-1)

152. // Use a mask to cover the screenshot area
153. Column()
154. .width('100%').height('100%').backgroundColor(Color.White)
155. // Long screenshot
156. Scroll() {
157. Image(this.mergedImage)
158. }
159. }
160. .width('100%')
161. .layoutWeight(1)
162. }
163. }
164. }
```

[ComponentScreenshot.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ComponentScreenshot.ets#L21-L185)
