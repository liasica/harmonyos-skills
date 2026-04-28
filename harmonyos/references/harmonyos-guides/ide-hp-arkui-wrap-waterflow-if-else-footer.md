---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-wrap-waterflow-if-else-footer
title: @performance/hp-arkui-wrap-waterflow-if-else-footer（已下线）
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-wrap-waterflow-if-else-footer（已下线）
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:11+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:e6cd2ac999797579f52d796251651fb5f112a2c3dfe72564024b0320da6493cc
---

建议使用容器包裹waterflow中footer的if-else逻辑。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-wrap-waterflow-if-else-footer": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';

4. @Entry
5. @Component
6. struct MyComponent{
7. private datasource: MyDataSource = new MyDataSource();
8. private showFooterStatus = 2;

10. aboutToAppear() {
11. for (let i = 0; i <= 20; i++) {
12. this.datasource.pushData(i)
13. }
14. }

16. build() {
17. Column({ space: 2 }) {
18. WaterFlow({ footer: (): void => this.itemFoot() }) {
19. LazyForEach(this.datasource, (item: number) => {
20. FlowItem() {
21. ReusableFlowItem({ item: item })

23. }.onAppear(() => {
24. if (item + 20 == this.datasource.totalCount()) {
25. for (let i = 0; i < 100; i++) {
26. this.datasource.addLastItem()
27. }
28. }
29. })

31. .width('100%')
32. }, (item: string) => item)
33. }
34. .columnsTemplate('1fr 1fr 1fr 1fr')
35. .columnsGap(10)
36. .rowsGap(5)
37. .width('100%')
38. .height('50%')
39. }
40. }

42. @Builder
43. itemFoot() {
44. //  外层加了一个column容器控制
45. Column() {
46. if (this.showFooterStatus == 1) {
47. // Code to show try again
48. } else if (this.showFooterStatus == 2) {
49. // Code to show end
50. } else {
51. // Code to show footer loading
52. }
53. }
54. }
55. }

57. @Component
58. @Reusable
59. struct ReusableFlowItem {
60. @State item: number = 0

62. aboutToReuse(params: Record<string, ESObject>) {
63. this.item = params.item;
64. }

66. build() {
67. Column() {
68. Text('N' + this.item)
69. .fontSize(12)
70. .height('16')
71. Image('res/waterFlowTest (' + this.item % 5 + ').jpg')
72. .objectFit(ImageFit.Fill)
73. .width('100%')
74. .layoutWeight(1)
75. }
76. }
77. }
```

## 反例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';

4. @Entry
5. @Component
6. struct MyComponent{
7. private datasource: MyDataSource = new MyDataSource();
8. private showFooterStatus = 2;

10. aboutToAppear() {
11. for (let i = 0; i <= 20; i++) {
12. this.datasource.pushData(i)
13. }
14. }

16. build() {
17. Column({ space: 2 }) {
18. WaterFlow({ footer: (): void => this.itemFoot() }) {
19. LazyForEach(this.datasource, (item: number) => {
20. FlowItem() {
21. ReusableFlowItem({ item: item })

23. }.onAppear(() => {
24. if (item + 20 == this.datasource.totalCount()) {
25. for (let i = 0; i < 100; i++) {
26. this.datasource.addLastItem()
27. }
28. }
29. })

31. .width('100%')
32. }, (item: string) => item)
33. }
34. .columnsTemplate('1fr 1fr 1fr 1fr')
35. .columnsGap(10)
36. .rowsGap(5)
37. .width('100%')
38. .height('50%')
39. }
40. }

42. @Builder
43. itemFoot() {
44. //  这个作为footer的build的逻辑里有if逻辑，应该在外层加一个容器控制
45. if (this.showFooterStatus == 1) {
46. // Code to show try again
47. } else if (this.showFooterStatus == 2) {
48. // Code to show end
49. } else {
50. // Code to show footer loading
51. }
52. }
53. }

55. @Component
56. @Reusable
57. struct ReusableFlowItem {
58. @State item: number = 0

60. aboutToReuse(params: Record<string, ESObject>) {
61. this.item = params.item;
62. }

64. build() {
65. Column() {
66. Text('N' + this.item)
67. .fontSize(12)
68. .height('16')
69. Image('res/waterFlowTest (' + this.item % 5 + ').jpg')
70. .objectFit(ImageFit.Fill)
71. .width('100%')
72. .layoutWeight(1)
73. }
74. }
75. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
