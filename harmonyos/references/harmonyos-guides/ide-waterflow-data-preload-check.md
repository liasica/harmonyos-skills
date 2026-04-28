---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-waterflow-data-preload-check
title: @performance/waterflow-data-preload-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/waterflow-data-preload-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:20+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:2d3160490eecd5b8cc86bcc67cb7e96389b2f2eb68f76a9e294edc5cdf7f095f
---

建议对waterflow子组件进行数据预加载。

滑动丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/waterflow-data-preload-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

下文中WaterFlowDataSource.ets为依赖代码：

```
1. // WaterFlowDataSource.ets

3. // 实现IDataSource接口的对象，用于瀑布流组件加载数据
4. export class WaterFlowDataSource implements IDataSource {
5. private dataArray: number[] = []
6. private listeners: DataChangeListener[] = []

8. constructor() {
9. for (let i = 0; i < 100; i++) {
10. this.dataArray.push(i)
11. }
12. }

14. // 获取索引对应的数据
15. public getData(index: number): number {
16. return this.dataArray[index]
17. }

19. // 通知控制器数据重新加载
20. notifyDataReload(): void {
21. this.listeners.forEach(listener => {
22. listener.onDataReloaded()
23. })
24. }

26. // 通知控制器数据增加
27. notifyDataAdd(index: number): void {
28. this.listeners.forEach(listener => {
29. listener.onDataAdd(index)
30. })
31. }

33. // 通知控制器数据变化
34. notifyDataChange(index: number): void {
35. this.listeners.forEach(listener => {
36. listener.onDataChange(index)
37. })
38. }

40. // 通知控制器数据删除
41. notifyDataDelete(index: number): void {
42. this.listeners.forEach(listener => {
43. listener.onDataDelete(index)
44. })
45. }

47. // 通知控制器数据位置变化
48. notifyDataMove(from: number, to: number): void {
49. this.listeners.forEach(listener => {
50. listener.onDataMove(from, to)
51. })
52. }

54. // 获取数据总数
55. public totalCount(): number {
56. return this.dataArray.length
57. }

59. // 注册改变数据的控制器
60. registerDataChangeListener(listener: DataChangeListener): void {
61. if (this.listeners.indexOf(listener) < 0) {
62. this.listeners.push(listener)
63. }
64. }

66. // 注销改变数据的控制器
67. unregisterDataChangeListener(listener: DataChangeListener): void {
68. const pos = this.listeners.indexOf(listener)
69. if (pos >= 0) {
70. this.listeners.splice(pos, 1)
71. }
72. }

74. // 增加数据
75. public add1stItem(): void {
76. this.dataArray.splice(0, 0, this.dataArray.length)
77. this.notifyDataAdd(0)
78. }

80. // 在数据尾部增加一个元素
81. public addLastItem(): void {
82. this.dataArray.splice(this.dataArray.length, 0, this.dataArray.length)
83. this.notifyDataAdd(this.dataArray.length - 1)
84. }

86. // 在指定索引位置增加一个元素
87. public addItem(index: number): void {
88. this.dataArray.splice(index, 0, this.dataArray.length)
89. this.notifyDataAdd(index)
90. }

92. // 删除第一个元素
93. public delete1stItem(): void {
94. this.dataArray.splice(0, 1)
95. this.notifyDataDelete(0)
96. }

98. // 删除第二个元素
99. public delete2ndItem(): void {
100. this.dataArray.splice(1, 1)
101. this.notifyDataDelete(1)
102. }

104. // 删除最后一个元素
105. public deleteLastItem(): void {
106. this.dataArray.splice(-1, 1)
107. this.notifyDataDelete(this.dataArray.length)
108. }

110. // 重新加载数据
111. public reload(): void {
112. this.dataArray.splice(1, 1)
113. this.dataArray.splice(3, 2)
114. this.notifyDataReload()
115. }
116. }
```

下文中Index.ets为正例测试代码，依赖上文中WaterFlowDataSource.ets：

```
1. // Index.ets
2. import { WaterFlowDataSource } from './WaterFlowDataSource'

4. @Entry
5. @Component
6. struct WaterFlowDemo {
7. @State minSize: number = 80
8. @State maxSize: number = 180
9. @State fontSize: number = 24
10. @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F]
11. scroller: Scroller = new Scroller()
12. dataSource: WaterFlowDataSource = new WaterFlowDataSource()
13. private itemWidthArray: number[] = []
14. private itemHeightArray: number[] = []

16. // 计算FlowItem宽/高
17. getSize() {
18. let ret = Math.floor(Math.random() * this.maxSize)
19. return (ret > this.minSize ? ret : this.minSize)
20. }

22. // 设置FlowItem的宽/高数组
23. setItemSizeArray() {
24. for (let i = 0; i < 100; i++) {
25. this.itemWidthArray.push(this.getSize())
26. this.itemHeightArray.push(this.getSize())
27. }
28. }

30. aboutToAppear() {
31. this.setItemSizeArray()
32. }

34. @Builder
35. itemFoot() {
36. Text(`Footer`)
37. .fontSize(10)

39. .width(50)
40. .height(50)
41. .align(Alignment.Center)
42. .margin({ top: 2 })
43. }

45. build() {
46. Column({ space: 2 }) {
47. WaterFlow() {
48. LazyForEach(this.dataSource, (item: number) => {
49. FlowItem() {
50. ReusableFlowItem({ item: item })
51. }
52. .onAppear(() => {
53. // 即将触底时提前增加数据，即执行数据预加载
54. if (item + 20 == this.dataSource.totalCount()) {
55. for (let i = 0; i < 100; i++) {
56. this.dataSource.addLastItem()
57. }
58. }
59. })
60. .width('100%')
61. .height(this.itemHeightArray[item % 100])
62. .backgroundColor(this.colors[item % 5])
63. }, (item: string) => item)
64. }
65. .columnsTemplate('1fr 1fr')
66. .columnsGap(10)
67. .rowsGap(5)
68. .width('100%')
69. .height('100%')
70. }
71. }
72. }

74. @Reusable
75. @Component
76. struct ReusableFlowItem {
77. @State item: number = 0

79. // 从复用缓存中加入到组件树之前调用，可在此处更新组件的状态变量以展示正确的内容
80. aboutToReuse(params: Record<string, ESObject>) {
81. this.item = params.item;
82. }

84. build() {
85. Column() {
86. Text('N' + this.item).fontSize(12).height('16')
87. Image('res/waterFlowTest (' + this.item % 5 + ').jpg')
88. .objectFit(ImageFit.Fill)
89. .width('100%')
90. .layoutWeight(1)
91. }
92. }
93. }
```

## 反例

下文中WaterFlowDataSource.ets为依赖代码：

```
1. // WaterFlowDataSource.ets

3. // 实现IDataSource接口的对象，用于瀑布流组件加载数据
4. export class WaterFlowDataSource implements IDataSource {
5. private dataArray: number[] = []
6. private listeners: DataChangeListener[] = []

8. constructor() {
9. for (let i = 0; i < 100; i++) {
10. this.dataArray.push(i)
11. }
12. }

14. // 获取索引对应的数据
15. public getData(index: number): number {
16. return this.dataArray[index]
17. }

19. // 通知控制器数据重新加载
20. notifyDataReload(): void {
21. this.listeners.forEach(listener => {
22. listener.onDataReloaded()
23. })
24. }

26. // 通知控制器数据增加
27. notifyDataAdd(index: number): void {
28. this.listeners.forEach(listener => {
29. listener.onDataAdd(index)
30. })
31. }

33. // 通知控制器数据变化
34. notifyDataChange(index: number): void {
35. this.listeners.forEach(listener => {
36. listener.onDataChange(index)
37. })
38. }

40. // 通知控制器数据删除
41. notifyDataDelete(index: number): void {
42. this.listeners.forEach(listener => {
43. listener.onDataDelete(index)
44. })
45. }

47. // 通知控制器数据位置变化
48. notifyDataMove(from: number, to: number): void {
49. this.listeners.forEach(listener => {
50. listener.onDataMove(from, to)
51. })
52. }

54. // 获取数据总数
55. public totalCount(): number {
56. return this.dataArray.length
57. }

59. // 注册改变数据的控制器
60. registerDataChangeListener(listener: DataChangeListener): void {
61. if (this.listeners.indexOf(listener) < 0) {
62. this.listeners.push(listener)
63. }
64. }

66. // 注销改变数据的控制器
67. unregisterDataChangeListener(listener: DataChangeListener): void {
68. const pos = this.listeners.indexOf(listener)
69. if (pos >= 0) {
70. this.listeners.splice(pos, 1)
71. }
72. }

74. // 增加数据
75. public add1stItem(): void {
76. this.dataArray.splice(0, 0, this.dataArray.length)
77. this.notifyDataAdd(0)
78. }

80. // 在数据尾部增加一个元素
81. public addLastItem(): void {
82. this.dataArray.splice(this.dataArray.length, 0, this.dataArray.length)
83. this.notifyDataAdd(this.dataArray.length - 1)
84. }

86. // 在指定索引位置增加一个元素
87. public addItem(index: number): void {
88. this.dataArray.splice(index, 0, this.dataArray.length)
89. this.notifyDataAdd(index)
90. }

92. // 删除第一个元素
93. public delete1stItem(): void {
94. this.dataArray.splice(0, 1)
95. this.notifyDataDelete(0)
96. }

98. // 删除第二个元素
99. public delete2ndItem(): void {
100. this.dataArray.splice(1, 1)
101. this.notifyDataDelete(1)
102. }

104. // 删除最后一个元素
105. public deleteLastItem(): void {
106. this.dataArray.splice(-1, 1)
107. this.notifyDataDelete(this.dataArray.length)
108. }

110. // 重新加载数据
111. public reload(): void {
112. this.dataArray.splice(1, 1)
113. this.dataArray.splice(3, 2)
114. this.notifyDataReload()
115. }
116. }
```

下文中Index.ets为反例测试代码，依赖上文中WaterFlowDataSource.ets：

```
1. // Index.ets
2. import { WaterFlowDataSource } from './WaterFlowDataSource'

4. @Entry
5. @Component
6. struct WaterFlowDemo {
7. @State minSize: number = 80
8. @State maxSize: number = 180
9. @State fontSize: number = 24
10. @State colors: number[] = [0xFFC0CB, 0xDA70D6, 0x6B8E23, 0x6A5ACD, 0x00FFFF, 0x00FF7F]
11. scroller: Scroller = new Scroller()
12. dataSource: WaterFlowDataSource = new WaterFlowDataSource()
13. private itemWidthArray: number[] = []
14. private itemHeightArray: number[] = []

16. // 计算FlowItem宽/高
17. getSize() {
18. let ret = Math.floor(Math.random() * this.maxSize)
19. return (ret > this.minSize ? ret : this.minSize)
20. }

22. // 设置FlowItem的宽/高数组
23. setItemSizeArray() {
24. for (let i = 0; i < 100; i++) {
25. this.itemWidthArray.push(this.getSize())
26. this.itemHeightArray.push(this.getSize())
27. }
28. }

30. aboutToAppear() {
31. this.setItemSizeArray()
32. }

34. @Builder
35. itemFoot() {
36. Text(`Footer`)
37. .fontSize(10)
38. .backgroundColor(Color.Red)
39. .width(50)
40. .height(50)
41. .align(Alignment.Center)
42. .margin({ top: 2 })
43. }

45. build() {
46. Column({ space: 2 }) {
47. WaterFlow() {
48. LazyForEach(this.dataSource, (item: number) => {
49. FlowItem() {
50. ReusableFlowItem({ item: item })
51. }
52. .width('100%')
53. .height(this.itemHeightArray[item % 100])
54. .backgroundColor(this.colors[item % 5])
55. }, (item: string) => item)
56. }
57. .onReachEnd(() => {
58. console.info("onReachEnd")
59. setTimeout(() => {
60. for (let i = 0; i < 100; i++) {
61. this.dataSource.addLastItem()
62. }
63. }, 1000)
64. })
65. .columnsTemplate("1fr 1fr")
66. .columnsGap(10)
67. .rowsGap(5)
68. .backgroundColor(0xFAEEE0)
69. .width('100%')
70. .height('100%')
71. }
72. }
73. }

75. @Reusable
76. @Component
77. struct ReusableFlowItem {
78. @State item: number = 0

80. // 从复用缓存中加入到组件树之前调用，可在此处更新组件的状态变量以展示正确的内容
81. aboutToReuse(params: Record<string, ESObject>) {
82. this.item = params.item;
83. }

85. build() {
86. Column() {
87. Text("N" + this.item).fontSize(12).height('16')
88. Image('res/waterFlowTest (' + this.item % 5 + ').jpg')
89. .objectFit(ImageFit.Fill)
90. .width('100%')
91. .layoutWeight(1)
92. }
93. }
94. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
