---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-no-stringify-lazyforeach-key
title: @performance/hp-arkui-no-stringify-in-lazyforeach-key-generator
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-no-stringify-in-lazyforeach-key-generator
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:05+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:34da12f64a94aa58208a29c13db70c0c3e69374b7305550dee887b082b848efd
---

在使用LazyForEach进行组件复用的key生成器函数里，不要使用stringify。

滑动丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-no-stringify-in-lazyforeach-key-generator": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. //源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';
3. // 此处为复用的自定义组件
4. @Reusable
5. @Component
6. struct ChildComponent {
7. @State desc: string = '';
8. @State sum: number = 0;
9. @State avg: number = 0;
10. aboutToReuse(params: Record<string, Object>): void {
11. this.desc = params.desc as string;
12. this.sum = params.sum as number;
13. this.avg = params.avg as number;
14. }
15. build() {
16. Column() {
17. Text('子组件' + this.desc)
18. .fontSize(30)
19. .fontWeight(30)
20. Text('结果' + this.sum)
21. .fontSize(30)
22. .fontWeight(30)
23. Text('平均值' + this.avg)
24. .fontSize(30)
25. .fontWeight(30)
26. }
27. }
28. }
29. class Item {
30. advertInfos: Model[] = []
31. productPrice: PriceInfo[] = []
32. addresses: string[] = []
33. id: string = ''
34. }
35. class Model {
36. pictureUrl: string = ""
37. name: string = ""
38. comments: string = ""
39. desc: string = ""
40. linkParam: string = ""
41. mcInfo: string = ""
42. label: string = ""
43. cgType: string = ""
44. constructor(pictureUrl: string, name: string, comments: string, desc: string, linkParam: string, mcInfo: string,
45. label: string, cgType: string) {
46. this.pictureUrl = pictureUrl;
47. this.name = name;
48. this.comments = comments;
49. this.desc = desc;
50. this.linkParam = linkParam;
51. this.mcInfo = mcInfo;
52. this.label = label;
53. this.cgType = cgType;
54. }
55. }
56. class PriceInfo {
57. price: number = 0;
58. level: number = 1;
59. constructor(price: number, level: number) {
60. this.price = price;
61. this.level = level;
62. }
63. }
64. @Entry
65. @Component
66. struct MyComponent {
67. private data: MyDataSource = new MyDataSource();
68. aboutToAppear(): void {
69. for (let index = 0; index < 20; index++) {
70. let item = new Item()
71. for (let i = 0; i < 1000; i++) {
72. item.advertInfos.push(new Model("Product A", "Product A", "Product A", "Product A", "Product A", "Product A", "Product A", "Product A"));
73. item.productPrice.push(new PriceInfo(1.99, 123456));
74. item.addresses.push("Beijing")
75. }
76. item.id = index.toString();
77. this.data.pushData(item)
78. }
79. }
80. build() {
81. Column() {
82. Text('Use the unique ID of an item as the key')
83. .fontSize(12)
84. .height('16')
85. .margin({
86. top: 5,
87. bottom: 10
88. })
89. List() {
90. LazyForEach(this.data, (item: Item) => {
91. ListItem() {
92. ChildComponent({ desc: item.id, sum: 0, avg: 0 })
93. }
94. .width('100%')
95. .height('10%')
96. .border({ width: 1 })
97. .borderStyle(BorderStyle.Dashed)
98. }, (item: Item) => item.id.toString())
99. }
100. .height('100%')
101. .width('100%')
102. }
103. }
104. }
```

## 反例

```
1. //源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';
3. // 此处为复用的自定义组件
4. @Reusable
5. @Component
6. struct ChildComponent {
7. @State desc: string = '';
8. @State sum: number = 0;
9. @State avg: number = 0;

11. aboutToReuse(params: Record<string, Object>): void {
12. this.desc = params.desc as string;
13. this.sum = params.sum as number;
14. this.avg = params.avg as number;
15. }

17. build() {
18. Column() {
19. Text('子组件' + this.desc)
20. .fontSize(30)
21. .fontWeight(30)
22. Text('结果' + this.sum)
23. .fontSize(30)
24. .fontWeight(30)
25. Text('平均值' + this.avg)
26. .fontSize(30)
27. .fontWeight(30)
28. }
29. }
30. }

32. class Item {
33. advertInfos: Model[] = []
34. productPrice: PriceInfo[] = []
35. addresses: string[] = []
36. id: string = ''
37. }

39. class Model {
40. pictureUrl: string = ""
41. name: string = ""
42. comments: string = ""
43. desc: string = ""
44. linkParam: string = ""
45. mcInfo: string = ""
46. label: string = ""
47. cgType: string = ""

49. constructor(pictureUrl: string, name: string, comments: string, desc: string, linkParam: string, mcInfo: string,
50. label: string, cgType: string) {
51. this.pictureUrl = pictureUrl;
52. this.name = name;
53. this.comments = comments;
54. this.desc = desc;
55. this.linkParam = linkParam;
56. this.mcInfo = mcInfo;
57. this.label = label;
58. this.cgType = cgType;
59. }
60. }

62. class PriceInfo {
63. price: number = 0;
64. level: number = 1;

66. constructor(price: number, level: number) {
67. this.price = price;
68. this.level = level;
69. }
70. }

72. @Entry
73. @Component
74. struct MyComponent {
75. private data: MyDataSource = new MyDataSource();

77. aboutToAppear(): void {
78. for (let index = 0; index < 20; index++) {
79. let item = new Item()
80. for (let i = 0; i < 1000; i++) {
81. item.advertInfos.push(new Model("Product A", "Product A", "Product A", "Product A", "Product A", "Product A", "Product A", "Product A"));
82. item.productPrice.push(new PriceInfo(1.99, 123456));
83. item.addresses.push("Beijing")
84. }
85. item.id = index.toString();
86. this.data.pushData(item)
87. }
88. }

90. build() {
91. Column() {
92. Text('Use the time-consuming function `JSON.stringify (item)` to generate a key')
93. .fontSize(12)
94. .height('16')
95. .margin({
96. top: 5,
97. bottom: 10
98. })
99. List() {
100. LazyForEach(this.data, (item: Item) => {
101. ListItem() {
102. ChildComponent({ desc: item.id, sum: 0, avg: 0 })
103. }
104. .width('100%')
105. .height('10%')
106. .border({ width: 1 })
107. .borderStyle(BorderStyle.Dashed)
108. }, (item: Item) => JSON.stringify(item))
109. }
110. .height('100%')
111. .width('100%')
112. }
113. }
114. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
