---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/map-faq-3
title: 手势卡顿或者不生效
breadcrumb: 指南 > 应用服务 > Map Kit（地图服务） > Map Kit常见问题 > 手势卡顿或者不生效
category: harmonyos-guides
scraped_at: 2026-04-28T07:49:56+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:176a17b8cca720e61cc11e717755a38f571f18da8064e97182eaea6161f88b87
---

**现象描述**

地图页面操作手势卡顿或者不生效。

**可能原因**

1. 手势遮盖或者手势冲突。

   * 手势遮盖：地图组件的上层存在没有做手势穿透的组件。
   * 手势冲突：以Swiper容器组件中使用地图组件为例，Swiper容器组件和地图组件手势会存在冲突。
2. 主线程阻塞。

   应用主线程处理大批量逻辑时，存在主线程阻塞，此时进行地图手势操作，手势应答会变慢甚至手势响应失败。

**处理步骤**

1. 手势遮盖或者手势冲突。

   * 手势遮盖：参考[触摸测试控制](../harmonyos-references/ts-universal-attributes-hit-test-behavior.md)做手势穿透。
   * 手势冲突：以Swiper容器组件和地图组件手势存在冲突为例，解决方案参考如下代码：

     ```
     1. import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
     2. import { map, mapCommon, MapComponent } from '@kit.MapKit';

     4. class MyDataSource implements IDataSource {
     5. private list: number[] = [];

     7. constructor(list: number[]) {
     8. this.list = list;
     9. }

     11. // 获取数组长度
     12. totalCount(): number {
     13. return this.list.length;
     14. }

     16. // 根据索引获取数据
     17. getData(index: number): number {
     18. return this.list[index];
     19. }

     21. // 注册数据变化监听器
     22. registerDataChangeListener(listener: DataChangeListener): void {
     23. }

     25. // 取消注册数据变化监听器
     26. unregisterDataChangeListener(listener: DataChangeListener): void {
     27. }
     28. }

     30. @Entry
     31. @Component
     32. struct SwiperExample {
     33. private swiperController: SwiperController = new SwiperController();
     34. private data: MyDataSource = new MyDataSource([]);
     35. private mapOptions?: mapCommon.MapOptions;
     36. private callback?: AsyncCallback<map.MapComponentController>;
     37. private mapController?: map.MapComponentController;
     38. private mapEventManager?: map.MapEventManager;
     39. @State mapPositionX: number = 0;
     40. @State mapPositionY: number = 0;
     41. @State mapHeight: number = 0;
     42. @State mapWidth: number = 0;
     43. @State index: number = 0;

     45. // 判断坐标是否在地图矩形内
     46. isMap(event: TouchEvent) {
     47. if (event.changedTouches[0].displayX > this.mapPositionX
     48. && event.changedTouches[0].displayX < this.mapPositionX + this.mapWidth
     49. && event.changedTouches[0].displayY > this.mapPositionY
     50. && event.changedTouches[0].displayY < this.mapPositionY + this.mapHeight) {
     51. return true;
     52. }
     53. return false;
     54. }

     56. aboutToAppear(): void {
     57. let list: number[] = [];
     58. for (let i = 1; i <= 10; i++) {
     59. list.push(i);
     60. }
     61. this.data = new MyDataSource(list);

     63. this.mapOptions = {
     64. position: {
     65. target: {
     66. latitude: 31.98441025,
     67. longitude: 118.766253
     68. },
     69. zoom: 10,
     70. tilt: 10,
     71. bearing: 90
     72. },
     73. scaleControlsEnabled: true
     74. }

     76. this.callback = async (err, mapController) => {
     77. if (!err) {
     78. this.mapController = mapController;
     79. this.mapEventManager = this.mapController.getEventManager();
     80. let callback = () => {
     81. console.info(`on-mapLoad`);
     82. };
     83. this.mapEventManager.on("mapLoad", callback);
     84. } else {
     85. console.error(`Failed to initialize the map, code is：${err.code}, message is ${err.message}`);
     86. }
     87. }
     88. }

     90. build() {
     91. Column({ space: 5 }) {
     92. Swiper(this.swiperController) {
     93. LazyForEach(this.data, (item: string) => {
     94. if (item == "3") {
     95. Column() {
     96. Text(item.toString())
     97. .width('90%')
     98. .height(160)
     99. .backgroundColor(0xAFEEEE)
     100. .textAlign(TextAlign.Center)
     101. .fontSize(30)
     102. MapComponent({ mapOptions: this.mapOptions, mapCallback: this.callback })
     103. // 获取MapComponent的位置和长宽
     104. .width('100%')
     105. .height('65%')
     106. .onAreaChange((_oldValue: Area, newValue: Area) => {
     107. try {
     108. if (newValue.globalPosition.x !== undefined && newValue.globalPosition.y !== undefined) {
     109. this.mapPositionX = Number(newValue.globalPosition.x);
     110. this.mapPositionY = Number(newValue.globalPosition.y);
     111. this.mapHeight = Number(newValue.height);
     112. this.mapWidth = Number(newValue.width);
     113. }
     114. } catch (error) {
     115. let e: BusinessError = error as BusinessError;
     116. console.error("onAreaChange error code:" + e.code + "message:" + e.message);
     117. }
     118. })
     119. }.height("100%")
     120. } else {
     121. Text(item.toString())
     122. .width('90%')
     123. .height(160)
     124. .backgroundColor(0xAFEEEE)
     125. .textAlign(TextAlign.Center)
     126. .fontSize(30)
     127. }
     128. }, (item: string) => item)
     129. }
     130. // 手势判断 当index为存在地图页面且点击在地图矩形内时为HitTestMode.None（不响应Swiper手势，响应子组件手势）
     131. .onTouchIntercept((event: TouchEvent) => {
     132. if (this.index === 2 && this.isMap(event)) {
     133. return HitTestMode.None;
     134. }
     135. return HitTestMode.Transparent;
     136. })
     137. .cachedCount(2)
     138. .index(1)
     139. .loop(true)
     140. .itemSpace(0)
     141. // 设置圆点导航点样式
     142. .indicator(
     143. new DotIndicator()
     144. .itemWidth(15)
     145. .itemHeight(15)
     146. .selectedItemWidth(15)
     147. .selectedItemHeight(15)
     148. .color(Color.Gray)
     149. .selectedColor(Color.Blue))
     150. .displayArrow({
     151. // 设置导航点箭头样式
     152. showBackground: true,
     153. isSidebarMiddle: true,
     154. backgroundSize: 24,
     155. backgroundColor: Color.White,
     156. arrowSize: 18,
     157. arrowColor: Color.Blue
     158. }, false)
     159. .curve(Curve.Linear)
     160. .onChange((index: number) => {
     161. this.index = index;
     162. })
     163. .onGestureSwipe((index: number, extraInfo: SwiperAnimationEvent) => {
     164. console.info("index: " + index);
     165. console.info("current offset: " + extraInfo.currentOffset);
     166. })

     168. Row({ space: 12 }) {
     169. Button('showNext')
     170. .onClick(() => {
     171. this.swiperController.showNext();
     172. })
     173. Button('showPrevious')
     174. .onClick(() => {
     175. this.swiperController.showPrevious();
     176. })
     177. }.margin(5)
     178. }.width('100%')
     179. .margin({ top: 5 })
     180. }
     181. }
     ```
2. 主线程阻塞。

   请分析应用的业务逻辑，将复杂逻辑放到子线程中处理。
