---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-lazyforeach-args-check
title: @performance/lazyforeach-args-check（已下线）
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/lazyforeach-args-check（已下线）
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:16+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:ebbd88c8fef0c34e25800bcf8ebc42ac11e07fb83d0a9f52189084ea2227084f
---

建议在LazyForEach参数中设置keyGenerator。该规则已于5.0.3.500版本下线。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/lazyforeach-args-check": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. class BasicDataSource implements IDataSource {
2. private listeners: DataChangeListener[] = [];
3. private originDataArray: string[] = [];
4. public totalCount(): number {
5. return 0;
6. }
7. public getData(index: number): string {
8. return this.originDataArray[index];
9. }
10. registerDataChangeListener(listener: DataChangeListener): void {
11. if (this.listeners.indexOf(listener) < 0) {
12. console.info('add listener');
13. this.listeners.push(listener);
14. }
15. }
16. unregisterDataChangeListener(listener: DataChangeListener): void {
17. const pos = this.listeners.indexOf(listener);
18. if (pos >= 0) {
19. console.info('remove listener');
20. this.listeners.splice(pos, 1);
21. }
22. }
23. notifyDataReload(): void {
24. this.listeners.forEach(listener => {
25. listener.onDataReloaded();
26. })
27. }
28. notifyDataAdd(index: number): void {
29. this.listeners.forEach(listener => {
30. listener.onDataAdd(index);
31. })
32. }
33. notifyDataChange(index: number): void {
34. this.listeners.forEach(listener => {
35. listener.onDataChange(index);
36. })
37. }
38. notifyDataDelete(index: number): void {
39. this.listeners.forEach(listener => {
40. listener.onDataDelete(index);
41. })
42. }
43. }
44. class MyDataSource extends BasicDataSource {
45. private dataArray: string[] = [];
46. public totalCount(): number {
47. return this.dataArray.length;
48. }
49. public getData(index: number): string {
50. return this.dataArray[index];
51. }
52. public addData(index: number, data: string): void {
53. this.dataArray.splice(index, 0, data);
54. this.notifyDataAdd(index);
55. }
56. public pushData(data: string): void {
57. this.dataArray.push(data);
58. this.notifyDataAdd(this.dataArray.length - 1);
59. }
60. }
61. @Entry
62. @Component
63. struct MyComponent {
64. private data: MyDataSource = new MyDataSource();
65. aboutToAppear() {
66. for (let i = 0; i <= 20; i++) {
67. this.data.pushData(`Hello ${i}`)
68. }
69. }
70. build() {
71. Column({ space: 5 }) {
72. Grid() {
73. LazyForEach(this.data, (item: string) => {
74. GridItem() {
75. // 使用可复用自定义组件
76. // 业务逻辑
77. }
78. }, (item: string) => item)
79. }
80. .cachedCount(2) // 设置GridItem的缓存数量
81. .columnsTemplate('1fr 1fr 1fr')
82. .columnsGap(10)
83. .rowsGap(10)
84. .margin(10)
85. .height(500)
86. .backgroundColor(0xFAEEE0)
87. }
88. }
89. }
```

## 反例

```
1. class BasicDataSource implements IDataSource {
2. private listeners: DataChangeListener[] = [];
3. private originDataArray: string[] = [];
4. public totalCount(): number {
5. return 0;
6. }
7. public getData(index: number): string {
8. return this.originDataArray[index];
9. }
10. registerDataChangeListener(listener: DataChangeListener): void {
11. if (this.listeners.indexOf(listener) < 0) {
12. console.info('add listener');
13. this.listeners.push(listener);
14. }
15. }
16. unregisterDataChangeListener(listener: DataChangeListener): void {
17. const pos = this.listeners.indexOf(listener);
18. if (pos >= 0) {
19. console.info('remove listener');
20. this.listeners.splice(pos, 1);
21. }
22. }
23. notifyDataReload(): void {
24. this.listeners.forEach(listener => {
25. listener.onDataReloaded();
26. })
27. }
28. notifyDataAdd(index: number): void {
29. this.listeners.forEach(listener => {
30. listener.onDataAdd(index);
31. })
32. }
33. notifyDataChange(index: number): void {
34. this.listeners.forEach(listener => {
35. listener.onDataChange(index);
36. })
37. }
38. notifyDataDelete(index: number): void {
39. this.listeners.forEach(listener => {
40. listener.onDataDelete(index);
41. })
42. }
43. }
44. class MyDataSource extends BasicDataSource {
45. private dataArray: string[] = [];
46. public totalCount(): number {
47. return this.dataArray.length;
48. }
49. public getData(index: number): string {
50. return this.dataArray[index];
51. }
52. public addData(index: number, data: string): void {
53. this.dataArray.splice(index, 0, data);
54. this.notifyDataAdd(index);
55. }
56. public pushData(data: string): void {
57. this.dataArray.push(data);
58. this.notifyDataAdd(this.dataArray.length - 1);
59. }
60. }
61. @Entry
62. @Component
63. struct MyComponent {
64. private data: MyDataSource = new MyDataSource();
65. aboutToAppear() {
66. for (let i = 0; i <= 20; i++) {
67. this.data.pushData(`Hello ${i}`)
68. }
69. }
70. build() {
71. Column({ space: 5 }) {
72. Grid() {
73. LazyForEach(this.data, (item: string) => {
74. GridItem() {
75. // 使用可复用自定义组件
76. // 业务逻辑
77. }
78. })
79. }
80. .cachedCount(2) // 设置GridItem的缓存数量
81. .columnsTemplate('1fr 1fr 1fr')
82. .columnsGap(10)
83. .rowsGap(10)
84. .margin(10)
85. .height(500)
86. .backgroundColor(0xFAEEE0)
87. }
88. }
89. }
```

## 规则集

```
1. plugin:@performance/recommended
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
