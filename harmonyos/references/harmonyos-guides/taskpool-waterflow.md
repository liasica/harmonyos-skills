---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/taskpool-waterflow
title: ArkUI瀑布流渲染场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > ArkUI瀑布流渲染场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:41+08:00
doc_updated_at: 2026-04-24
content_hash: sha256:7a1f814feaab36633ef8fac19c28ff68a4e767f6b79056dee506c65678534e38
---

此处提供使用任务池[TaskPool](../harmonyos-references/js-apis-taskpool.md)提升[WaterFlow瀑布流](../harmonyos-references/ts-container-waterflow.md)渲染性能的开发指导。UI线程查询数据库数据，并将数据渲染到瀑布流组件，数据过大时会导致UI线程长时间等待，影响用户体验。因此，我们可以将数据查询操作放到子线程中，并通过TaskPool的接口返回数据给UI线程。

本示例说明以下场景：

* 模拟子线程[读取数据库数据](batch-database-operations-guide.md)并返回给UI线程。
* UI线程感知到数据更新，将子线程返回的数据渲染到瀑布流组件。

1. 定义一个接口，用于子线程查询数据库并将数据返回给UI线程。

   ```
   1. import { taskpool } from '@kit.ArkTS';
   2. import { fillImg } from './WaterfallRendering';

   4. @Concurrent
   5. function query() {
   6. console.info('TaskPoolTest-this is query');
   7. let result = new Array<string>(33);
   8. for (let i = 0; i < 33; i++) {
   9. result[i] = 'Image' + i;
   10. }
   11. taskpool.Task.sendData(result);
   12. }

   14. export function getImgFromDB() {
   15. // 此处模拟查询数据库，并返回数据
   16. let task = new taskpool.Task(query);
   17. task.onReceiveData(fillImg);
   18. taskpool.execute(task);
   19. }
   ```
2. 封装一个瀑布流组件数据源，用于瀑布流组件加载数据。

   ```
   1. // 实现IDataSource接口的对象，用于瀑布流组件加载数据
   2. export class WaterFlowDataSource implements IDataSource {
   3. private dataArray: number[] = [];
   4. private listeners: DataChangeListener[] = [];

   6. constructor() {
   7. for (let i = 0; i < 100; i++) {
   8. this.dataArray.push(i);
   9. }
   10. }

   12. // 获取索引对应的数据
   13. public getData(index: number): number {
   14. return this.dataArray[index];
   15. }

   17. // 通知控制器数据重新加载
   18. notifyDataReload(): void {
   19. this.listeners.forEach(listener => {
   20. listener.onDataReloaded();
   21. })
   22. }

   24. // 通知控制器数据增加
   25. notifyDataAdd(index: number): void {
   26. this.listeners.forEach(listener => {
   27. listener.onDataAdd(index);
   28. })
   29. }

   31. // 通知控制器数据变化
   32. notifyDataChange(index: number): void {
   33. this.listeners.forEach(listener => {
   34. listener.onDataChange(index);
   35. })
   36. }

   38. // 通知控制器数据删除
   39. notifyDataDelete(index: number): void {
   40. this.listeners.forEach(listener => {
   41. listener.onDataDelete(index);
   42. })
   43. }

   45. // 通知控制器数据位置变化
   46. notifyDataMove(from: number, to: number): void {
   47. this.listeners.forEach(listener => {
   48. listener.onDataMove(from, to);
   49. })
   50. }

   52. // 通知控制器数据批量修改
   53. notifyDatasetChange(operations: DataOperation[]): void {
   54. this.listeners.forEach(listener => {
   55. listener.onDatasetChange(operations);
   56. })
   57. }

   59. // 获取数据总数
   60. public totalCount(): number {
   61. return this.dataArray.length;
   62. }

   64. // 注册改变数据的控制器
   65. registerDataChangeListener(listener: DataChangeListener): void {
   66. if (this.listeners.indexOf(listener) < 0) {
   67. this.listeners.push(listener);
   68. }
   69. }

   71. // 注销改变数据的控制器
   72. unregisterDataChangeListener(listener: DataChangeListener): void {
   73. const pos = this.listeners.indexOf(listener);
   74. if (pos >= 0) {
   75. this.listeners.splice(pos, 1);
   76. }
   77. }

   79. // 增加数据
   80. public add1stItem(): void {
   81. this.dataArray.splice(0, 0, this.dataArray.length);
   82. this.notifyDataAdd(0);
   83. }

   85. // 在数据尾部增加一个元素
   86. public addLastItem(): void {
   87. this.dataArray.splice(this.dataArray.length, 0, this.dataArray.length);
   88. this.notifyDataAdd(this.dataArray.length - 1);
   89. }

   91. // 在指定索引位置增加一个元素
   92. public addItem(index: number): void {
   93. this.dataArray.splice(index, 0, this.dataArray.length);
   94. this.notifyDataAdd(index);
   95. }

   97. // 删除第一个元素
   98. public delete1stItem(): void {
   99. this.dataArray.splice(0, 1);
   100. this.notifyDataDelete(0);
   101. }

   103. // 删除第二个元素
   104. public delete2ndItem(): void {
   105. this.dataArray.splice(1, 1);
   106. this.notifyDataDelete(1);
   107. }

   109. // 删除最后一个元素
   110. public deleteLastItem(): void {
   111. this.dataArray.splice(-1, 1);
   112. this.notifyDataDelete(this.dataArray.length);
   113. }

   115. // 在指定索引位置删除一个元素
   116. public deleteItem(index: number): void {
   117. this.dataArray.splice(index, 1);
   118. this.notifyDataDelete(index);
   119. }

   121. // 重新加载数据
   122. public reload(): void {
   123. this.dataArray.splice(3, 2);
   124. this.dataArray.splice(1, 1);
   125. this.notifyDataReload();
   126. }
   127. }
   ```
3. 在应用冷启动阶段，调用getImgFromDB()接口，将数据查询操作放到子线程中。在img接收到子线程返回的数据后，将数据渲染到瀑布流组件。

   ```
   1. import { WaterFlowDataSource } from './WaterFlowDataSource';
   2. import { getImgFromDB } from './Mock';

   4. // 模拟图片数组
   5. let img = new Array<string>(33);

   7. export function fillImg(imgArr: Array<string>) {
   8. img = imgArr;
   9. }

   11. @Entry
   12. @Component
   13. struct WaterFlowDemo {
   14. @State minSize: number = 80;
   15. @State maxSize: number = 180;
   16. @State fontSize: number = 24;
   17. @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F];
   18. scroller: Scroller = new Scroller();
   19. dataSource: WaterFlowDataSource = new WaterFlowDataSource();
   20. private itemWidthArray: number[] = [];
   21. private itemHeightArray: number[] = [];

   23. // 计算FlowItem宽/高
   24. getSize() {
   25. let ret = Math.floor(Math.random() * this.maxSize);
   26. return (ret > this.minSize ? ret : this.minSize);
   27. }

   29. // 设置FlowItem的宽/高数组
   30. setItemSizeArray() {
   31. for (let i = 0; i < 100; i++) {
   32. this.itemWidthArray.push(this.getSize());
   33. this.itemHeightArray.push(this.getSize());
   34. }
   35. }

   37. aboutToAppear() {
   38. this.setItemSizeArray();
   39. }

   41. @Builder
   42. itemFoot() {
   43. Column() {
   44. Text(`Footer`)
   45. .fontSize(10)
   46. .backgroundColor(Color.Red)
   47. .width(50)
   48. .height(50)
   49. .align(Alignment.Center)
   50. .margin({ top: 2 });
   51. }
   52. }

   54. build() {
   55. Column({ space: 2 }) {
   56. Text('ArkUI WaterFlow Demo')
   57. .onAppear(() => {
   58. getImgFromDB();
   59. })
   60. WaterFlow() {
   61. LazyForEach(this.dataSource, (item: number) => {
   62. FlowItem() {
   63. Column() {
   64. Text('N' + item)
   65. .fontSize(12)
   66. .height('16')
   67. .onClick(() => {
   68. });
   69. // 为了模拟图片加载，使用Text组件显示，正常加载jpg文件时，可以直接使用Image组件
   70. // 参考 Image(this.img[item % 33]).objectFit(ImageFit.Contain).width('100%').layoutWeight(1)
   71. if (img[item % 33] == null) {
   72. Text($r('app.string.Image_loading')) // 加载资源，可根据项目实际资源自定义
   73. .width('100%')
   74. .layoutWeight(1);
   75. }
   76. Text(img[item % 33])
   77. .width('100%')
   78. .layoutWeight(1);
   79. }
   80. }
   81. .onAppear(() => {
   82. // 即将触底时提前增加数据
   83. if (item + 20 == this.dataSource.totalCount()) {
   84. for (let i = 0; i < 100; i++) {
   85. this.dataSource.addLastItem();
   86. }
   87. }
   88. })
   89. .width('100%')
   90. .height(this.itemHeightArray[item % 100])
   91. .backgroundColor(this.colors[item % 5])
   92. }, (item: string) => item)
   93. }
   94. .columnsTemplate('1fr 1fr')
   95. .columnsGap(10)
   96. .rowsGap(5)
   97. .backgroundColor(0xFAEEE0)
   98. .width('100%')
   99. .height('100%')
   100. .onReachStart(() => {
   101. console.info('TaskPoolTest-waterFlow reach start');
   102. })
   103. .onScrollStart(() => {
   104. console.info('TaskPoolTest-waterFlow scroll start');
   105. })
   106. .onScrollStop(() => {
   107. console.info('TaskPoolTest-waterFlow scroll stop');
   108. })
   109. .onScrollFrameBegin((offset: number, state: ScrollState) => {
   110. console.info('TaskPoolTest-waterFlow scrollFrameBegin offset: ' + offset + ' state: ' + state.toString());
   111. return { offsetRemain: offset };
   112. })
   113. }
   114. }
   115. }
   ```
