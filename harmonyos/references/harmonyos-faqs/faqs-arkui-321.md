---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-321
title: 如何使用ListItemGroup和LazyForEach结合并实现组件复用
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何使用ListItemGroup和LazyForEach结合并实现组件复用
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:6a9f283f50b47e0e695c47563daa2e29b5ea97be2433219ae0268f878d13d67d
---

可参考如下代码：

```
1. @Entry
2. @Component
3. struct ListItemGroupAndReusable {
4. data: DataSrc2 = new DataSrc2();

6. @Builder
7. itemHead(text: string) {
8. Text(text)
9. .fontSize(20)
10. .backgroundColor(0xAABBCC)
11. .width('100%')
12. .padding(10)
13. }

15. aboutToAppear() {
16. for (let i = 0; i < 10000; i++) {
17. let currentData = new DataSrc1();
18. for (let j = 0; j < 12; j++) {
19. currentData.Data.push(`Test Data Test Data Test Data: ${i} - ${j}`);
20. }
21. this.data.Data.push(currentData);
22. }
23. }

25. build() {
26. Stack() {
27. List() {
28. LazyForEach(this.data, (item: DataSrc1, index: number) => {
29. ListItemGroup({ header: this.itemHead(index.toString()) }) {
30. LazyForEach(item, (ii: string, index: number) => {
31. ListItem() {
32. Inner({ str: ii })
33. }
34. })
35. }
36. .width('100%')
37. .height('60vp')
38. })
39. }
40. .cachedCount(10)
41. }
42. .width('100%')
43. .height('100%')
44. }
45. }

48. @Reusable
49. @Component
50. struct Inner {
51. @State str: string = '';

53. aboutToReuse(param: ESObject) {
54. this.str = param.str;
55. }

57. build() {
58. Text(this.str)
59. }
60. }

63. class DataSrc1 implements IDataSource {
64. listeners: DataChangeListener[] = [];
65. Data: string[] = [];

67. // data count
68. public totalCount(): number {
69. return this.Data.length;
70. }

72. // get data by index
73. public getData(index: number): string {
74. return this.Data[index];
75. }

77. // This method is called on the framework side to add listener listening to the LazyForEach component at its data source
78. registerDataChangeListener(listener: DataChangeListener): void {
79. if (this.listeners.indexOf(listener) < 0) {
80. this.listeners.push(listener);
81. }
82. }

84. // This method is called on the framework side to remove listener listening for the corresponding LazyForEach component at the data source
85. unregisterDataChangeListener(listener: DataChangeListener): void {
86. const pos = this.listeners.indexOf(listener);
87. if (pos >= 0) {
88. this.listeners.splice(pos, 1);
89. }
90. }
91. }

94. class DataSrc2 implements IDataSource {
95. listeners: DataChangeListener[] = [];
96. Data: DataSrc1[] = [];

98. // data count
99. public totalCount(): number {
100. return this.Data.length;
101. }

103. // get data by index
104. public getData(index: number): DataSrc1 {
105. return this.Data[index];
106. }

108. // This method is called on the framework side to add listener listening to the LazyForEach component at its data source
109. registerDataChangeListener(listener: DataChangeListener): void {
110. if (this.listeners.indexOf(listener) < 0) {
111. this.listeners.push(listener);
112. }
113. }

115. // This method is called on the framework side to remove listener listening for the corresponding LazyForEach component at the data source
116. unregisterDataChangeListener(listener: DataChangeListener): void {
117. const pos = this.listeners.indexOf(listener);
118. if (pos >= 0) {
119. this.listeners.splice(pos, 1);
120. }
121. }
122. }
```

[ReusingListItemGroupAndLazyForEachComponents.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ReusingListItemGroupAndLazyForEachComponents.ets#L21-L143)
