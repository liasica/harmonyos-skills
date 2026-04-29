---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-long-snapshot-practice
title: 长截图
breadcrumb: 最佳实践 > 媒体 > 图片 > 长截图
category: best-practices
scraped_at: 2026-04-29T14:11:14+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:9f84e9b6892e323e44aa020ba06713c9ce4f7027d967c84ba6cdd9dcde8fb947
---

## 概述

在移动应用中，标准的截图方法仅能捕捉当前屏幕显示的内容，对于超出屏幕可视区域的长页面或文档而言，这种方式显得不够便捷。当用户截图分享和保存（如聊天记录、网页文章、活动海报等）的内容较长的时候，需要用户多次截图来保证内容完整性。为了解决这一问题，本文将介绍长截图功能，使用户能够一键截取整个页面的长图，更轻松地分享和保存信息。

长截图功能适用于支持滚动的UI组件，比如List组件、Scroll组件、Web组件等。本文将以List组件和Web组件为例来介绍长截图功能的开发，分别通过控制器[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)和[WebviewController](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)，结合UIContext的[getComponentSnapshot().get()](../harmonyos-references/arkts-apis-uicontext-componentsnapshot.md#get12-1)方法，实现长截图功能。

## 实现原理

List组件和Web组件实现长截图功能的原理相同，均可以通过模拟用户滚动行为，然后使用getComponentSnapshot().get()方法逐步截取不同位置的画面，将这些画面通过拼接得到长截图。Web组件通过[WebviewController](../harmonyos-references/arkts-apis-webview-webviewcontroller.md)的相关API控制组件滚动，List组件通过[Scroller](../harmonyos-references/ts-container-scroll.md#scroller)的相关API控制组件滚动。

长截图拼接原理如下，将每次滚动新进入屏幕的内容裁剪后，拼接到之前的屏幕截图，依次类推。

**图1** 长截图拼接原理图  
![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/F6a1FplgTlq2XFdAX-Jutg/zh-cn_image_0000002229449985.png?HW-CC-KV=V1&HW-CC-Date=20260429T061108Z&HW-CC-Expire=86400&HW-CC-Sign=2A056C724BF2B9BAAC89914D97E6F39CE9D3756EF075374F1B41FC45B4B3014B "点击放大")

长截图主要流程如下：

**图2** 滚动长截图流程

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/AijPXT5yRbWzO6CuNyxatQ/zh-cn_image_0000002407557206.png?HW-CC-KV=V1&HW-CC-Date=20260429T061108Z&HW-CC-Expire=86400&HW-CC-Sign=61FFAAA7C58AE350DC0D7A1147FC634FDD999A5DC4E8F4267FD90B293667D04F "点击放大")

说明

在长截图的拼接过程中，所有截图会被暂时缓存到内存中。对于无限滚动或数据量较大的场景，应当限制单张截图的高度，以防止过高的内存占用影响应用性能。

## 滚动组件长截图

List、Scroll、Grid、WaterFlow等滚动组件均是通过Scroller来控制组件滚动，本章将以List组件为例来介绍滚动组件长截图的实现。下面介绍了滚动组件两种常见的长截图场景，一键截图和滚动截图。

### 一键截图

**场景描述**

一键截图将组件数据从顶部截取到底部，在截图过程中用户看不到界面的滚动，实现无感知滚动截图。这种方案一般用于分享截图、保存数据量较少的场景。

**实现效果**

点击“一键截图”，会生成整个列表的长截图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/bf8YXChhRTmsfw2FiBPpCg/zh-cn_image_0000002193850120.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061108Z&HW-CC-Expire=86400&HW-CC-Sign=CC910501CEA27B579630A0D6AA3340EA8548DCCFE682B22F18E5878963B72AEF "点击放大")

**开发流程**

1. 给List绑定滚动控制器，添加监听事件。

   1.1 为List滚动组件绑定Scroller控制器，以控制其滚动行为，并给List组件绑定自定义的id。

   1.2 通过onDidScroll()方法实时监听并获取滚动偏移量，确保截图拼接位置的准确性。

   1.3 同时，利用onAreaChange()事件获取List组件的尺寸，以便精确计算截图区域的大小。

   ```
   1. // src/main/ets/view/ScrollSnapshot.ets
   2. @Component
   3. export struct ScrollSnapshot {
   4. // Scroll controller
   5. private scroller: Scroller = new Scroller();
   6. private listComponentWidth: number = 0;
   7. private listComponentHeight: number = 0;
   8. // The current offset of the List component
   9. private curYOffset: number = 0;
   10. private scrollHeight: number = 0;
   11. // ...
   12. build() {
   13. // ...
   14. Stack() {
   15. // ...
   16. List({
   17. space: 12,
   18. scroller: this.scroller
   19. })
   20. // ...
   21. .id(LIST_ID)
   22. .onDidScroll(() => {
   23. this.curYOffset = this.scroller.currentOffset().yOffset;
   24. })
   25. .onAreaChange((oldValue, newValue) => {
   26. this.listComponentWidth = newValue.width as number;
   27. this.listComponentHeight = newValue.height as number;
   28. this.scrollHeight = this.listComponentHeight;
   29. })
   30. .onClick(() => {
   31. // Click on the list to stop scrolling
   32. if (!this.isEnableScroll) {
   33. this.scroller.scrollBy(0, 0);
   34. this.isClickStop = true;
   35. }
   36. })
   37. }
   38. .width('100%')
   39. .layoutWeight(1)
   40. .padding({
   41. left: 16,
   42. right: 16,
   43. top: 16
   44. })
   45. .bindContentCover($$this.isShowPreview, this.previewWindowComponent(),
   46. {
   47. modalTransition: ModalTransition.NONE,
   48. onWillDismiss: (action: DismissContentCoverAction) => {
   49. if (action.reason === DismissReason.PRESS_BACK) {
   50. Logger.info('BindContentCover dismiss reason is back pressed');
   51. }
   52. }
   53. })

   55. Row({ space: 12 }) {
   56. Button($r('app.string.one_click_snapshot'))
   57. .layoutWeight(1)
   58. .onClick(() => {
   59. this.onceSnapshot();
   60. })
   61. Button($r('app.string.scroll_snapshot'))
   62. .layoutWeight(1)
   63. .onClick(() => {
   64. // Prevent users from clicking the button during the screenshot process,
   65. // and the method is repeatedly called, resulting in an exception
   66. if (this.scrollYOffsets.length === 0) {
   67. this.scrollSnapshot();
   68. }
   69. })
   70. }
   71. .width('100%')
   72. .padding({
   73. left: 16,
   74. right: 16,
   75. bottom: (AppStorage.get<number>('naviIndicatorHeight') ?? 0) + 16,
   76. top: 12
   77. })
   78. }
   79. }
   80. .title($r('app.string.title_scroll_snapshot'))
   81. .backgroundColor($r('sys.color.background_secondary'))
   82. }
   83. }
   ```

   [ScrollSnapshot.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/view/ScrollSnapshot.ets#L29-L339)
2. 给List添加遮罩图，初始化滚动位置。

   “一键截图”功能确保在滚动截图过程中用户不会察觉到页面的滚动。通过截取当前屏幕生成遮罩图覆盖列表，并记录此时的滚动偏移量（yOffsetBefore），便于后续完成滚动截图之后，恢复到之前记录的偏移量，使用户无感知页面变化。

   为保证截图的完整性，设置完遮罩图后，同样利用scrollTo()方法将列表暂时滚至顶部，确保截图从最顶端开始。

   ```
   1. // src/main/ets/view/ScrollSnapshot.ets
   2. @Component
   3. export struct ScrollSnapshot {
   4. // Scroll controller
   5. private scroller: Scroller = new Scroller();
   6. private listComponentWidth: number = 0;
   7. private listComponentHeight: number = 0;
   8. // The current offset of the List component
   9. private curYOffset: number = 0;
   10. private scrollHeight: number = 0;
   11. // The component is overwritten during the screenshot process
   12. @State componentMaskImage: PixelMap | undefined = undefined;
   13. // The location of the component before backing up the screenshot
   14. private yOffsetBefore: number = 0;
   15. // ...
   16. /**
   17. * One-click screenshot
   18. */
   19. async onceSnapshot() {
   20. await this.beforeSnapshot();
   21. await this.snapAndMerge();
   22. await this.afterSnapshot();
   23. // ...
   24. }

   26. /**
   27. * Scroll through the screenshots
   28. */
   29. async scrollSnapshot() {
   30. // The settings list cannot be manually scrolled during the screenshot process
   31. // to avoid interference with the screenshot
   32. this.isEnableScroll = false;
   33. // Saves the current location of the component for recovery
   34. this.yOffsetBefore = this.curYOffset;
   35. // Set the prompt pop-up to be centered
   36. await this.scrollSnapAndMerge();
   37. // Open the prompt pop-up window
   38. this.isShowPreview = true;
   39. // Initial variable after stitching
   40. await this.afterGeneratorImage();
   41. this.isEnableScroll = true;
   42. this.isClickStop = false;
   43. }

   45. /**
   46. * One click screenshot loop traversal screenshot and merge
   47. */
   48. async snapAndMerge() {
   49. try {
   50. this.scrollYOffsets.push(this.curYOffset);
   51. // Call the component screenshot interface to obtain the current screenshot
   52. const pixelMap = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
   53. // Gets the number of bytes per line of image pixels.
   54. let area: image.PositionArea =
   55. await ImageUtils.getSnapshotArea(this.getUIContext(), pixelMap, this.scrollYOffsets, this.listComponentWidth,
   56. this.listComponentHeight);
   57. this.areaArray.push(area);
   58. // Determine whether the bottom has been reached during the loop process
   59. if (!this.scroller.isAtEnd()) {
   60. CommonUtils.scrollAnimation(this.scroller, 200, this.scrollHeight);
   61. await CommonUtils.sleep(200)
   62. await this.snapAndMerge();
   63. } else {
   64. this.mergedImage =
   65. await ImageUtils.mergeImage(this.getUIContext(), this.areaArray,
   66. this.scrollYOffsets[this.scrollYOffsets.length - 1],this.listComponentHeight);
   67. }
   68. } catch (err) {
   69. let error = err as BusinessError;
   70. Logger.error(TAG, `snapAndMerge err, errCode: ${error.code}, error message: ${error.message}`);
   71. }
   72. }

   75. /**
   76. * Rolling screenshots, looping through screenshots, and merge them
   77. */
   78. async scrollSnapAndMerge() {
   79. try {
   80. // Record an array of scrolls
   81. this.scrollYOffsets.push(this.curYOffset - this.yOffsetBefore);
   82. // Call the API for taking screenshots to obtain the current screenshots
   83. const pixelMap = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
   84. // Gets the number of bytes per line of image pixels.
   85. let area: image.PositionArea =
   86. await ImageUtils.getSnapshotArea(this.getUIContext(), pixelMap, this.scrollYOffsets, this.listComponentWidth,
   87. this.listComponentHeight)
   88. this.areaArray.push(area);

   90. // During the loop, it is determined whether the bottom is reached, and the user does not stop taking screenshots
   91. if (!this.scroller.isAtEnd() && !this.isClickStop) {
   92. // Scroll to the next page without scrolling to the end
   93. CommonUtils.scrollAnimation(this.scroller, 1000, this.scrollHeight);
   94. await CommonUtils.sleep(1500);
   95. await this.scrollSnapAndMerge();
   96. } else {
   97. // After scrolling to the bottom, the buffer obtained by each round of scrolling is spliced
   98. // to generate a long screenshot
   99. this.mergedImage =
   100. await ImageUtils.mergeImage(this.getUIContext(), this.areaArray,
   101. this.scrollYOffsets[this.scrollYOffsets.length - 1], this.listComponentHeight);
   102. }
   103. } catch (err) {
   104. let error = err as BusinessError;
   105. Logger.error(TAG, `scrollSnapAndMerge err, errCode: ${error.code}, error message: ${error.message}`);
   106. }
   107. }

   110. async beforeSnapshot() {
   111. try {
   112. this.yOffsetBefore = this.curYOffset;
   113. // Take a screenshot of the loaded List component as a cover image for the List component
   114. this.componentMaskImage = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
   115. this.scroller.scrollTo({
   116. xOffset: 0,
   117. yOffset: 0,
   118. animation:
   119. {
   120. duration: 200
   121. }
   122. });
   123. // ...
   124. await CommonUtils.sleep(200);
   125. } catch (err) {
   126. let error = err as BusinessError;
   127. Logger.error(TAG, `beforeSnapshot err, errCode: ${error.code}, error message: ${error.message}`);
   128. }
   129. }

   131. async afterSnapshot() {
   132. this.scroller.scrollTo({
   133. xOffset: 0,
   134. yOffset: this.yOffsetBefore,
   135. animation: {
   136. duration: 200
   137. }
   138. });
   139. await CommonUtils.sleep(200);
   140. }

   143. async afterGeneratorImage() {
   144. // Delay for transition animation
   145. await CommonUtils.sleep(200);
   146. this.componentMaskImage = undefined;
   147. this.scrollYOffsets.length = 0;
   148. this.areaArray.length = 0;
   149. }

   151. @Builder
   152. previewWindowComponent() {
   153. Column() {
   154. SnapshotPreview({
   155. mergedImage: $mergedImage,
   156. isShowPreview: $isShowPreview
   157. })
   158. }
   159. }

   161. build() {
   162. // ...
   163. Stack() {
   164. //  The masking layer of the screenshot process prevents users from noticing the screen swiping quickly
   165. //  and improves the user experience
   166. if (this.componentMaskImage) {
   167. Image(this.componentMaskImage)
   168. // ...
   169. }
   170. List({
   171. space: 12,
   172. scroller: this.scroller
   173. })
   174. // ...
   175. .id(LIST_ID)
   176. .onDidScroll(() => {
   177. this.curYOffset = this.scroller.currentOffset().yOffset;
   178. })
   179. .onAreaChange((oldValue, newValue) => {
   180. this.listComponentWidth = newValue.width as number;
   181. this.listComponentHeight = newValue.height as number;
   182. this.scrollHeight = this.listComponentHeight;
   183. })
   184. .onClick(() => {
   185. // Click on the list to stop scrolling
   186. if (!this.isEnableScroll) {
   187. this.scroller.scrollBy(0, 0);
   188. this.isClickStop = true;
   189. }
   190. })
   191. }
   192. .width('100%')
   193. .layoutWeight(1)
   194. .padding({
   195. left: 16,
   196. right: 16,
   197. top: 16
   198. })
   199. .bindContentCover($$this.isShowPreview, this.previewWindowComponent(),
   200. {
   201. modalTransition: ModalTransition.NONE,
   202. onWillDismiss: (action: DismissContentCoverAction) => {
   203. if (action.reason === DismissReason.PRESS_BACK) {
   204. Logger.info('BindContentCover dismiss reason is back pressed');
   205. }
   206. }
   207. })

   209. Row({ space: 12 }) {
   210. Button($r('app.string.one_click_snapshot'))
   211. .layoutWeight(1)
   212. .onClick(() => {
   213. this.onceSnapshot();
   214. })
   215. Button($r('app.string.scroll_snapshot'))
   216. .layoutWeight(1)
   217. .onClick(() => {
   218. // Prevent users from clicking the button during the screenshot process,
   219. // and the method is repeatedly called, resulting in an exception
   220. if (this.scrollYOffsets.length === 0) {
   221. this.scrollSnapshot();
   222. }
   223. })
   224. }
   225. .width('100%')
   226. .padding({
   227. left: 16,
   228. right: 16,
   229. bottom: (AppStorage.get<number>('naviIndicatorHeight') ?? 0) + 16,
   230. top: 12
   231. })
   232. }
   233. }
   234. .title($r('app.string.title_scroll_snapshot'))
   235. .backgroundColor($r('sys.color.background_secondary'))
   236. }
   237. }
   ```

   [ScrollSnapshot.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/view/ScrollSnapshot.ets#L30-L340)
3. 循环滚动截图，裁剪和缓存截图数据。

   3.1 记录每次滚动的位置到数组scrollYOffsets中，并使用componentSnapshot.get(LIST\_ID) 方法获取当前画面的截图。

   3.2 如果非首次截图，则使用crop方法截取从底部滚动进来的区域，然后调用pixmap.readPixelsSync(area)方法将截图数据读取到缓冲区域area中，并将area通过集合进行保存，用于后续截图拼接。

   3.3 如果页面没有滚动到底部，继续滚动，继续递归调用snapAndMerge()方法进行截图；如果到达底部，则调用mergeImage()方法拼接所有收集到的图像片段，生成完整的长截图；同时还需限制截图的高度，以防过大的截图占用过多内存，影响应用性能，例如这里设置截长截图高度不超过5000。

   ```
   1. /**
   2. * One click screenshot loop traversal screenshot and merge
   3. */
   4. async snapAndMerge() {
   5. try {
   6. this.scrollYOffsets.push(this.curYOffset);
   7. // Call the component screenshot interface to obtain the current screenshot
   8. const pixelMap = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
   9. // Gets the number of bytes per line of image pixels.
   10. let area: image.PositionArea =
   11. await ImageUtils.getSnapshotArea(this.getUIContext(), pixelMap, this.scrollYOffsets, this.listComponentWidth,
   12. this.listComponentHeight);
   13. this.areaArray.push(area);
   14. // Determine whether the bottom has been reached during the loop process
   15. if (!this.scroller.isAtEnd()) {
   16. CommonUtils.scrollAnimation(this.scroller, 200, this.scrollHeight);
   17. await CommonUtils.sleep(200)
   18. await this.snapAndMerge();
   19. } else {
   20. this.mergedImage =
   21. await ImageUtils.mergeImage(this.getUIContext(), this.areaArray,
   22. this.scrollYOffsets[this.scrollYOffsets.length - 1],this.listComponentHeight);
   23. }
   24. } catch (err) {
   25. let error = err as BusinessError;
   26. Logger.error(TAG, `snapAndMerge err, errCode: ${error.code}, error message: ${error.message}`);
   27. }
   28. }
   ```

   [ScrollSnapshot.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/view/ScrollSnapshot.ets#L104-L132)

   ```
   1. /**
   2. * Read the screenshot PixelMap object into the buffer area
   3. * @param {PixelMap} pixelMap - Screenshot PixelMap
   4. * @param {number[]} scrollYOffsets - Component scrolls an array of y-axis offsets
   5. * @param {number} listWidth - List component width
   6. * @param {number} listHeight - List component height
   7. * @returns {image.PositionArea} Picture buffer area
   8. */
   9. static async getSnapshotArea(uiContext: UIContext, pixelMap: PixelMap, scrollYOffsets: number[], listWidth: number,
   10. listHeight: number): Promise<image.PositionArea> {
   11. // Gets the number of bytes per line of image pixels.
   12. let stride = pixelMap.getBytesNumberPerRow();
   13. // Get the total number of bytes of image pixels.
   14. let bytesNumber = pixelMap.getPixelBytesNumber();
   15. let buffer: ArrayBuffer = new ArrayBuffer(bytesNumber);
   16. //     Region size, read based on region.   PositionArea represents the data within the specified area of the image.
   17. let len = scrollYOffsets.length;

   19. // Except for the first screenshot, you don't need to crop it, and you need to crop the new parts
   20. if (scrollYOffsets.length >= 2) {
   21. // Realistic roll distance
   22. let realScrollHeight = scrollYOffsets[len-1] - scrollYOffsets[len-2];
   23. if (listHeight - realScrollHeight > 0) {
   24. let cropRegion: image.Region = {
   25. x: 0,
   26. y: uiContext.vp2px(listHeight - realScrollHeight),
   27. size: {
   28. height: uiContext.vp2px(realScrollHeight),
   29. width: uiContext.vp2px(listWidth)
   30. }
   31. };
   32. // Crop roll area
   33. await pixelMap.crop(cropRegion);
   34. }
   35. }

   37. let area: image.PositionArea = {
   38. pixels: buffer,
   39. offset: 0,
   40. stride: stride,
   41. region: {
   42. size: {
   43. width: 0,
   44. height: 0
   45. },
   46. x: 0,
   47. y: 0
   48. }
   49. }

   51. try {
   52. let imgInfo = pixelMap.getImageInfoSync();
   53. // Region size, read based on region. PositionArea represents the data within the specified area of the image.
   54. area = {
   55. pixels: buffer,
   56. offset: 0,
   57. stride: stride,
   58. region: {
   59. size: {
   60. width: imgInfo.size.width,
   61. height: imgInfo.size.height
   62. },
   63. x: 0,
   64. y: 0
   65. }
   66. }
   67. // Write data to a specified area
   68. pixelMap.readPixelsSync(area);
   69. } catch (err) {
   70. let error = err as BusinessError;
   71. Logger.error(TAG, `getSnapshotArea err, code: ${error.code}, message: ${error.message}`);
   72. }
   73. return area;
   74. }
   ```

   [ImageUtils.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/common/ImageUtils.ets#L23-L97)
4. 拼接截图片段。

   使用image.createPixelMapSync()方法创建长截图longPixelMap，并遍历之前保存的图像片段数据 (this.areaArray)，构建image.PositionArea对象area，然后调用longPixelMap.writePixelsSync(area) 方法将这些片段逐个写入到正确的位置，从而拼接成一个完整的长截图。

   ```
   1. /**
   2. * Merge image area array into long screenshots
   3. * @param {image.PositionArea[]} areaArray - screenshot area
   4. * @param {number} lastOffsetY - The offset Y of the last screenshot
   5. * @param {number} listWidth - List component width
   6. * @param {number} listHeight - List component height
   7. * @returns {PixelMap} Long image after merge
   8. */
   9. static async mergeImage(uiContext: UIContext, areaArray: image.PositionArea[], lastOffsetY: number,
   10. listHeight: number): Promise<PixelMap> {
   11. // Create a long screenshot PixelMap
   12. let opts: image.InitializationOptions = {
   13. editable: true,
   14. pixelFormat: 4,
   15. size: {
   16. // You need to ensure that the width of the PixelMap is greater than the width of the area
   17. width:  ImageUtils.getMaxAreaWidth(areaArray),
   18. height: uiContext.vp2px(lastOffsetY + listHeight)
   19. }
   20. };
   21. let longPixelMap = image.createPixelMapSync(opts);
   22. let imgPosition: number = 0;

   24. for (let i = 0; i < areaArray.length; i++) {
   25. let readArea = areaArray[i];
   26. let area: image.PositionArea = {
   27. pixels: readArea.pixels,
   28. offset: 0,
   29. stride: readArea.stride,
   30. region: {
   31. size: {
   32. width: readArea.region.size.width,
   33. height: readArea.region.size.height
   34. },
   35. x: 0,
   36. y: imgPosition
   37. }
   38. }
   39. imgPosition += readArea.region.size.height;
   40. try {
   41. longPixelMap.writePixelsSync(area);
   42. } catch (err) {
   43. let error = err as BusinessError;
   44. Logger.error(TAG, `writePixelsSync err, code: ${error.code}, message: ${error.message}`);
   45. }
   46. }
   47. return longPixelMap;
   48. }
   ```

   [ImageUtils.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/common/ImageUtils.ets#L117-L165)
5. 恢复到截图前的状态，滚动到截图前的位置。

   ```
   1. async afterSnapshot() {
   2. this.scroller.scrollTo({
   3. xOffset: 0,
   4. yOffset: this.yOffsetBefore,
   5. animation: {
   6. duration: 200
   7. }
   8. });
   9. await CommonUtils.sleep(200);
   10. }
   ```

   [ScrollSnapshot.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/view/ScrollSnapshot.ets#L197-L207)
6. 使用安全控件SaveButton保存截图相册。

   通过安全控件[SaveButton](../harmonyos-references/ts-security-components-savebutton.md)结合[photoAccessHelper](../harmonyos-references/js-apis-photoaccesshelper.md)模块保存截图到相册。

   ```
   1. SaveButton({
   2. icon: SaveIconStyle.FULL_FILLED,
   3. text: SaveDescription.SAVE_IMAGE,
   4. buttonType: ButtonType.Capsule
   5. })
   6. // ...
   7. .onClick((event, result) => {
   8. this.saveSnapshot(result);
   9. })
   ```

   [SnapshotPreview.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/view/SnapshotPreview.ets#L132-L147)

   ```
   1. /**
   2. * Save the picture to the album
   3. * @param {SaveButtonOnClickResult} result - The security control returns the result
   4. */
   5. async saveSnapshot(result: SaveButtonOnClickResult): Promise<void> {
   6. try {
   7. if (result === SaveButtonOnClickResult.SUCCESS) {
   8. const helper = photoAccessHelper.getPhotoAccessHelper(this.context);
   9. const uri = await helper.createAsset(photoAccessHelper.PhotoType.IMAGE, 'png');
   10. // Open the file with a URI to write content continuously
   11. const file = await fileIo.open(uri, fileIo.OpenMode.READ_WRITE | fileIo.OpenMode.CREATE);
   12. const imagePackerApi: image.ImagePacker = image.createImagePacker();
   13. const packOpts: image.PackingOption = {
   14. format: 'image/png',
   15. quality: 100,
   16. };
   17. imagePackerApi.packToData(this.mergedImage, packOpts).then((data) => {
   18. fileIo.writeSync(file.fd, data);
   19. fileIo.closeSync(file.fd);
   20. Logger.info(TAG, `Succeeded in packToFile`);
   21. this.getUIContext().getPromptAction().showToast({
   22. message: $r('app.string.save_album_success'),
   23. duration: 1800
   24. })
   25. }).catch((error: BusinessError) => {
   26. Logger.error(TAG, `Failed to packToFile. Error code is ${error.code}, message is ${error.message}`);
   27. });
   28. }
   29. // ...
   30. } catch (err) {
   31. let error = err as BusinessError;
   32. Logger.error(TAG, `saveSnapshot err, errCode: ${error.code}, error message: ${error.message}`);
   33. }
   34. }
   ```

   [SnapshotPreview.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/view/SnapshotPreview.ets#L46-L81)

### 滚动截图

**场景描述**

此方案允许用户控制长截图的起止位置，增加了使用的灵活性。它适用于大数据量场景，方便用户选择性保存滚动组件中的特定数据。

**实现效果**

点击“滚动截图”按钮后，列表将自动滚动。点击列表中的任意条目时，滚动会立即停止，并开始截取从滚动开始到停止这段时间内的数据截图。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/egZs3tB8TpSua6Kniy2eqw/zh-cn_image_0000002193850136.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061108Z&HW-CC-Expire=86400&HW-CC-Sign=42A36D98E04BE30D5D6B4DE78AF95CA902287F3C2EF60600DDFBE22C0CC8E0E5 "点击放大")

**功能实现**

“滚动截图”功能的实现流程与前述的“一键截图”一样，因此这里不再重复详述整个过程，而仅聚焦于其中的几个关键差异点，例如滚动的控制和偏移量的记录，分别如下面1和2所描述。

1. 在截图滚动的过程中，为了防止用户手动滚动对截图产生干扰，应禁用列表的手动滚动功能。可以通过设置List组件的enableScrollInteraction属性来控制是否允许手动滚动。

   当准备开始截图时，将isEnableScroll设置为false以禁用滚动交互。而当用户点击列表项以确定截图结束位置时，使用scroller.scrollBy(0, 0)方法确保列表立即停止滑动。

   ```
   1. // src/main/ets/view/ScrollSnapshot.ets
   2. @Component
   3. export struct ScrollSnapshot {
   4. // Scroll controller
   5. private scroller: Scroller = new Scroller();
   6. private listComponentWidth: number = 0;
   7. private listComponentHeight: number = 0;
   8. // The current offset of the List component
   9. private curYOffset: number = 0;
   10. private scrollHeight: number = 0;
   11. // The component is overwritten during the screenshot process
   12. @State componentMaskImage: PixelMap | undefined = undefined;
   13. // The location of the component before backing up the screenshot
   14. private yOffsetBefore: number = 0;
   15. // is click to stop scroll
   16. private isClickStop: boolean = false;
   17. @State isEnableScroll: boolean = true;
   18. // ...
   19. /**
   20. * Scroll through the screenshots
   21. */
   22. async scrollSnapshot() {
   23. // The settings list cannot be manually scrolled during the screenshot process
   24. // to avoid interference with the screenshot
   25. this.isEnableScroll = false;
   26. // Saves the current location of the component for recovery
   27. this.yOffsetBefore = this.curYOffset;
   28. // Set the prompt pop-up to be centered
   29. await this.scrollSnapAndMerge();
   30. // ...
   31. this.isEnableScroll = true;
   32. this.isClickStop = false;
   33. }

   35. /**
   36. * One click screenshot loop traversal screenshot and merge
   37. */
   38. async snapAndMerge() {
   39. try {
   40. this.scrollYOffsets.push(this.curYOffset);
   41. // Call the component screenshot interface to obtain the current screenshot
   42. const pixelMap = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
   43. // Gets the number of bytes per line of image pixels.
   44. let area: image.PositionArea =
   45. await ImageUtils.getSnapshotArea(this.getUIContext(), pixelMap, this.scrollYOffsets, this.listComponentWidth,
   46. this.listComponentHeight);
   47. this.areaArray.push(area);
   48. // Determine whether the bottom has been reached during the loop process
   49. if (!this.scroller.isAtEnd()) {
   50. CommonUtils.scrollAnimation(this.scroller, 200, this.scrollHeight);
   51. await CommonUtils.sleep(200)
   52. await this.snapAndMerge();
   53. } else {
   54. this.mergedImage =
   55. await ImageUtils.mergeImage(this.getUIContext(), this.areaArray,
   56. this.scrollYOffsets[this.scrollYOffsets.length - 1],this.listComponentHeight);
   57. }
   58. } catch (err) {
   59. let error = err as BusinessError;
   60. Logger.error(TAG, `snapAndMerge err, errCode: ${error.code}, error message: ${error.message}`);
   61. }
   62. }

   65. /**
   66. * Rolling screenshots, looping through screenshots, and merge them
   67. */
   68. async scrollSnapAndMerge() {
   69. try {
   70. // Record an array of scrolls
   71. this.scrollYOffsets.push(this.curYOffset - this.yOffsetBefore);
   72. // Call the API for taking screenshots to obtain the current screenshots
   73. const pixelMap = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
   74. // Gets the number of bytes per line of image pixels.
   75. let area: image.PositionArea =
   76. await ImageUtils.getSnapshotArea(this.getUIContext(), pixelMap, this.scrollYOffsets, this.listComponentWidth,
   77. this.listComponentHeight)
   78. this.areaArray.push(area);

   80. // During the loop, it is determined whether the bottom is reached, and the user does not stop taking screenshots
   81. if (!this.scroller.isAtEnd() && !this.isClickStop) {
   82. // Scroll to the next page without scrolling to the end
   83. CommonUtils.scrollAnimation(this.scroller, 1000, this.scrollHeight);
   84. await CommonUtils.sleep(1500);
   85. await this.scrollSnapAndMerge();
   86. } else {
   87. // After scrolling to the bottom, the buffer obtained by each round of scrolling is spliced
   88. // to generate a long screenshot
   89. this.mergedImage =
   90. await ImageUtils.mergeImage(this.getUIContext(), this.areaArray,
   91. this.scrollYOffsets[this.scrollYOffsets.length - 1], this.listComponentHeight);
   92. }
   93. } catch (err) {
   94. let error = err as BusinessError;
   95. Logger.error(TAG, `scrollSnapAndMerge err, errCode: ${error.code}, error message: ${error.message}`);
   96. }
   97. }

   100. async beforeSnapshot() {
   101. try {
   102. this.yOffsetBefore = this.curYOffset;
   103. // Take a screenshot of the loaded List component as a cover image for the List component
   104. this.componentMaskImage = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
   105. this.scroller.scrollTo({
   106. xOffset: 0,
   107. yOffset: 0,
   108. animation:
   109. {
   110. duration: 200
   111. }
   112. });
   113. this.isShowPreview = true;
   114. // Delay ensures that the scroll has reached the top
   115. await CommonUtils.sleep(200);
   116. } catch (err) {
   117. let error = err as BusinessError;
   118. Logger.error(TAG, `beforeSnapshot err, errCode: ${error.code}, error message: ${error.message}`);
   119. }
   120. }

   122. async afterSnapshot() {
   123. this.scroller.scrollTo({
   124. xOffset: 0,
   125. yOffset: this.yOffsetBefore,
   126. animation: {
   127. duration: 200
   128. }
   129. });
   130. await CommonUtils.sleep(200);
   131. }

   134. async afterGeneratorImage() {
   135. // Delay for transition animation
   136. await CommonUtils.sleep(200);
   137. this.componentMaskImage = undefined;
   138. this.scrollYOffsets.length = 0;
   139. this.areaArray.length = 0;
   140. }

   142. @Builder
   143. previewWindowComponent() {
   144. Column() {
   145. SnapshotPreview({
   146. mergedImage: $mergedImage,
   147. isShowPreview: $isShowPreview
   148. })
   149. }
   150. }

   152. build() {
   153. // ...
   154. List({
   155. space: 12,
   156. scroller: this.scroller
   157. })
   158. // ...
   159. .id(LIST_ID)
   160. .onDidScroll(() => {
   161. this.curYOffset = this.scroller.currentOffset().yOffset;
   162. })
   163. .onAreaChange((oldValue, newValue) => {
   164. this.listComponentWidth = newValue.width as number;
   165. this.listComponentHeight = newValue.height as number;
   166. this.scrollHeight = this.listComponentHeight;
   167. })
   168. .onClick(() => {
   169. // Click on the list to stop scrolling
   170. if (!this.isEnableScroll) {
   171. this.scroller.scrollBy(0, 0);
   172. this.isClickStop = true;
   173. }
   174. })
   175. }
   176. .width('100%')
   177. .layoutWeight(1)
   178. .padding({
   179. left: 16,
   180. right: 16,
   181. top: 16
   182. })
   183. .bindContentCover($$this.isShowPreview, this.previewWindowComponent(),
   184. {
   185. modalTransition: ModalTransition.NONE,
   186. onWillDismiss: (action: DismissContentCoverAction) => {
   187. if (action.reason === DismissReason.PRESS_BACK) {
   188. Logger.info('BindContentCover dismiss reason is back pressed');
   189. }
   190. }
   191. })

   193. Row({ space: 12 }) {
   194. Button($r('app.string.one_click_snapshot'))
   195. .layoutWeight(1)
   196. .onClick(() => {
   197. this.onceSnapshot();
   198. })
   199. Button($r('app.string.scroll_snapshot'))
   200. .layoutWeight(1)
   201. .onClick(() => {
   202. // Prevent users from clicking the button during the screenshot process,
   203. // and the method is repeatedly called, resulting in an exception
   204. if (this.scrollYOffsets.length === 0) {
   205. this.scrollSnapshot();
   206. }
   207. })
   208. }
   209. .width('100%')
   210. .padding({
   211. left: 16,
   212. right: 16,
   213. bottom: (AppStorage.get<number>('naviIndicatorHeight') ?? 0) + 16,
   214. top: 12
   215. })
   216. }
   217. }
   218. .title($r('app.string.title_scroll_snapshot'))
   219. .backgroundColor($r('sys.color.background_secondary'))
   220. }
   221. }
   ```

   [ScrollSnapshot.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/view/ScrollSnapshot.ets#L31-L338)
2. “滚动截图”功能依据当前坐标启动截图过程，因此在记录滚动偏移量时，通过 this.curYOffset - this.yOffsetBefore 来计算相对于初始位置的变化。

   ```
   1. /**
   2. * Rolling screenshots, looping through screenshots, and merge them
   3. */
   4. async scrollSnapAndMerge() {
   5. try {
   6. // Record an array of scrolls
   7. this.scrollYOffsets.push(this.curYOffset - this.yOffsetBefore);
   8. // Call the API for taking screenshots to obtain the current screenshots
   9. const pixelMap = await this.getUIContext().getComponentSnapshot().get(LIST_ID);
   10. // Gets the number of bytes per line of image pixels.
   11. let area: image.PositionArea =
   12. await ImageUtils.getSnapshotArea(this.getUIContext(), pixelMap, this.scrollYOffsets, this.listComponentWidth,
   13. this.listComponentHeight)
   14. this.areaArray.push(area);

   16. // During the loop, it is determined whether the bottom is reached, and the user does not stop taking screenshots
   17. if (!this.scroller.isAtEnd() && !this.isClickStop) {
   18. // Scroll to the next page without scrolling to the end
   19. CommonUtils.scrollAnimation(this.scroller, 1000, this.scrollHeight);
   20. await CommonUtils.sleep(1500);
   21. await this.scrollSnapAndMerge();
   22. } else {
   23. // After scrolling to the bottom, the buffer obtained by each round of scrolling is spliced
   24. // to generate a long screenshot
   25. this.mergedImage =
   26. await ImageUtils.mergeImage(this.getUIContext(), this.areaArray,
   27. this.scrollYOffsets[this.scrollYOffsets.length - 1], this.listComponentHeight);
   28. }
   29. } catch (err) {
   30. let error = err as BusinessError;
   31. Logger.error(TAG, `scrollSnapAndMerge err, errCode: ${error.code}, error message: ${error.message}`);
   32. }
   33. }
   ```

   [ScrollSnapshot.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/view/ScrollSnapshot.ets#L136-L169)
3. 与“一键截图”不同，“滚动截图”在执行过程中不使用遮罩层，用户能够直接看到列表的滚动效果。为了确保流畅的视觉体验，在调用 scroller.scrollTo 进行滚动时，添加了动画效果，使得滚动更加自然和顺滑。

   ```
   1. static scrollAnimation(scroller: Scroller, duration: number, scrollHeight: number): void {
   2. scroller.scrollTo({
   3. xOffset: 0,
   4. yOffset: (scroller.currentOffset().yOffset + scrollHeight),
   5. animation: {
   6. duration: duration,
   7. curve: Curve.Smooth,
   8. canOverScroll: false
   9. }
   10. });
   11. }
   ```

   [CommonUtils.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/common/CommonUtils.ets#L22-L32)

## Web组件长截图

### 场景描述

Web组件的长截图功能与之前介绍的滚动组件长截图在使用场景上相似，两者均旨在为用户提供快速便捷的数据信息分享和保存方式。主要区别在于，Web组件专门针对网页内容进行截图，确保用户能够完整地捕获和分享浏览的网页信息。

### 实现效果

点击“截图”按钮即可完成整个网页的长截图，并可将截图保存至相册。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/h3Z7dMCPQnKa_zrGtAEp5g/zh-cn_image_0000002522310291.gif?HW-CC-KV=V1&HW-CC-Date=20260429T061108Z&HW-CC-Expire=86400&HW-CC-Sign=8BEF4474674BA992FD8B0BE1F3989403403826657FB2DF696DC39B819C6AF381 "点击放大")

### 功能实现

Web组件的长截图可以通过前文介绍的滚动截图方案以及使用WebView提供的webPageSnapshot()方法进行全量截图。本章将重点介绍webPageSnapshot()方法的使用方法，而滚动截图的相关信息已在前文详述。

**使用滚动截图的方式进行长截图**

Web组件滚动长截图和滚动组件长截图开发流程大体一样，主要是控制组件的滚动的方法不同。List组件使用的是Scroller，而Web组件使用的是webViewController。

在滚动截图过程中，webViewController负责控制Web组件的滚动，通过调用webViewController.scrollBy()方法来实现。为了判断是否已滚动到底部，使用this.webViewController.getPageHeight() 方法获取网页内容的总高度，并将当前偏移量this.curYOffset加上组件自身的高度与网页总高度进行比较。如果两者的和小于网页总高度，则表示尚未触底。

```
1. /**
2. * One click screenshot loop traversal screenshot and merge
3. */
4. async snapAndMerge() {
5. try {
6. this.scrollYOffsets.push(this.curYOffset);
7. // Call the component screenshot interface to obtain the current screenshot
8. const pixelMap = await this.getUIContext().getComponentSnapshot().get(WEB_ID);
9. let area: image.PositionArea =
10. await ImageUtils.getSnapshotArea(this.getUIContext(), pixelMap, this.scrollYOffsets, this.webComponentWidth,
11. this.webComponentHeight);
12. this.areaArray.push(area);
13. // Determine whether the bottom has been reached during the loop process
14. if (Math.ceil(this.curYOffset + this.webComponentHeight) < this.webviewController.getPageHeight()) {
15. // Not scrolling to the bottom, scrolling to the next page
16. this.webviewController.scrollBy(0, this.scrollHeight, 500);
17. await CommonUtils.sleep(600)
18. await this.snapAndMerge();
19. } else {
20. this.mergedImage =
21. await ImageUtils.mergeImage(this.getUIContext(), this.areaArray,
22. this.scrollYOffsets[this.scrollYOffsets.length - 1], this.webComponentHeight);
23. }
24. } catch (err) {
25. let error = err as BusinessError;
26. Logger.error(TAG, `snapAndMerge err, errCode: ${error.code}, error message: ${error.message}`);
27. }
28. }
```

[WebSnapshot.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/view/WebSnapshot.ets#L79-L107)

**使用webPageSnapshot()方法进行网页全量截图**

此外，Web组件还可以使用[webPageSnapshot()](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#webpagesnapshot12)方法进行网页全量截图，比较适合结构简单、静态元素的页面长截图。如果网页中有动态资源，结构相对复杂，比如有固定的标题头等，推荐上面的滚动长截图方案。使用webPageSnapshot()方法实现长截图的步骤如下：

1. Web初始化，调用enableWholeWebPageDrawing()方法开启网页全量绘制能力。

   ```
   1. aboutToAppear(): void {
   2. try {
   3. webview.WebviewController.initializeWebEngine();
   4. webview.WebviewController.enableWholeWebPageDrawing();
   5. webview.WebviewController.prepareForPageLoad(EXAMPLE_URL, true, 2);
   6. } catch (err) {
   7. let error = err as BusinessError;
   8. Logger.error(TAG, `web snapshot init err, errCode: ${error.code}, error message: ${error.message}`);
   9. }
   10. }
   ```

   [WebSnapshotWebTag.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/view/WebSnapshotWebTag.ets#L33-L42)
2. 获取网页内容高度和宽度。

   ```
   1. async getWebSize() {
   2. const SCRIPT = '[document.documentElement.scrollWidth, document.documentElement.scrollHeight]';
   3. try {
   4. this.webviewController.runJavaScriptExt(SCRIPT).then((result) => {
   5. if (result.getType() === webview.JsMessageType.ARRAY) {
   6. this.h5Width = (result.getArray() as number[])[0];
   7. this.h5Height = (result.getArray() as number[])[1];
   8. Logger.info(TAG, `h5Width is ${this.h5Width}, h5Height is ${this.h5Height}`);
   9. }
   10. }).catch((error: BusinessError) => {
   11. Logger.error(TAG, `getWebSize exception, errCode: ${error.code}, error message: ${error.message}`);
   12. });
   13. } catch (error) {
   14. let err = error as BusinessError;
   15. Logger.error(TAG, `getWebSize failed, errCode: ${err.code}, error message: ${err.message}`);
   16. }
   17. }
   ```

   [WebSnapshotWebTag.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/view/WebSnapshotWebTag.ets#L107-L123)
3. 调用webPageSnapshot()方法，进行网页截图。

   ```
   1. async webSnapshot() {
   2. try {
   3. this.webviewController.webPageSnapshot({ id: WEB_ID, size: { width: this.h5Width, height: this.h5Height } },
   4. async (error, result) => {
   5. if (result) {
   6. this.longPixelMap = result.imagePixelMap;
   7. }
   8. });
   9. } catch (error) {
   10. let err = error as BusinessError;
   11. Logger.error(TAG, `webSnapshot err, errCode: ${err.code}, error message: ${err.message}`);
   12. }
   13. }
   ```

   [WebSnapshotWebTag.ets](https://gitcode.com/harmonyos_samples/LongSnapshotPractice/blob/master/entry/src/main/ets/view/WebSnapshotWebTag.ets#L91-L103)

说明

加载网络html文件时，需要在entry/src/main路径下的module.json5中配置网络权限。示例代码如下所示：

```
1. {
2. "module": {
3. "requestPermissions": [
4. {
5. "name": "ohos.permission.INTERNET"
6. }
7. ]
8. }
9. }
```

## 示例代码

* [实现长截图功能](https://gitcode.com/harmonyos_samples/LongSnapshotPractice)
