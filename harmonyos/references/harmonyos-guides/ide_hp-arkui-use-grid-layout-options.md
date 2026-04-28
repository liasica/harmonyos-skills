---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-grid-layout-options
title: @performance/hp-arkui-use-grid-layout-options
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-grid-layout-options
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:09+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:758204513e961dd773ef0d7472fca3a56103a790edcec7b23299e81876ceef4c
---

建议在指定位置时使用GridLayoutOptions提升Grid性能。

通用丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-use-grid-layout-options": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';

4. @Reusable
5. @Component
6. struct TextItem {
7. @State item: string = "";

9. build() {
10. Text(this.item)
11. .fontSize(16)
12. .backgroundColor(0xF9CF93)
13. .width('100%')
14. .height(80)
15. .textAlign(TextAlign.Center)
16. .onClick(() => {
17. this.item = 'click';
18. })
19. }
20. }

22. @Entry
23. @Component
24. export struct MyComponent{
25. private datasource: MyDataSource = new MyDataSource();
26. scroller: Scroller = new Scroller();
27. private irregularData: number[] = [];
28. layoutOptions: GridLayoutOptions = {
29. regularSize: [1, 1],
30. irregularIndexes: this.irregularData,
31. };

33. aboutToAppear() {
34. for (let i = 1; i <= 2000; i++) {
35. this.datasource.pushData(i + '');
36. if ((i - 1) % 4 === 0) {
37. this.irregularData.push(i - 1);
38. }
39. }
40. }

42. build() {
43. Column({ space: 5 }) {
44. Text('Set GridItem size using GridLayoutOptions').fontColor(0xCCCCCC).fontSize(9).width('90%')
45. Grid(this.scroller, this.layoutOptions) {
46. LazyForEach(this.datasource, (item: string, index: number) => {
47. GridItem() {
48. TextItem({ item: item })
49. }
50. }, (item: string) => item)
51. }
52. .cachedCount(1)
53. .columnsTemplate('1fr 1fr 1fr')
54. .columnsGap(10)
55. .rowsGap(10)
56. .width('90%')
57. .height('40%')

59. Button("scrollToIndex:1900").onClick(() => {
60. this.scroller.scrollToIndex(1900);
61. })
62. }.width('100%')
63. .margin({ top: 5 })
64. }
65. }
```

## 反例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';

4. @Reusable
5. @Component
6. struct TextItem {
7. @State item: string = "";

9. build() {
10. Text(this.item)
11. .fontSize(16)
12. .backgroundColor(0xF9CF93)
13. .width('100%')
14. .height(80)
15. .textAlign(TextAlign.Center)
16. .onClick(() => {
17. this.item = 'click';
18. })
19. }
20. }

22. @Entry
23. @Component
24. struct MyComponent{
25. private datasource: MyDataSource = new MyDataSource();
26. scroller: Scroller = new Scroller();

28. aboutToAppear() {
29. for (let i = 1; i <= 2000; i++) {
30. this.datasource.pushData(i + '');
31. }
32. }

34. build() {
35. Column({ space: 5 }) {
36. Text('Use columnStart and columnEnd to set the GridItem size').fontColor(0xCCCCCC).fontSize(9).width('90%')
37. Grid(this.scroller) {
38. LazyForEach(this.datasource, (item: string, index: number) => {
39. if ((index % 4) === 0) {
40. GridItem() {
41. TextItem({ item: item })
42. }
43. .columnStart(0).columnEnd(2)
44. } else {
45. GridItem() {
46. TextItem({ item: item })
47. }
48. }
49. }, (item: string) => item)
50. }
51. .cachedCount(1)
52. .columnsTemplate('1fr 1fr 1fr')
53. .columnsGap(10)
54. .rowsGap(10)
55. .width('90%')
56. .height('40%')

58. Button("scrollToIndex:1900").onClick(() => {
59. this.scroller.scrollToIndex(1900);
60. })
61. }.width('100%')
62. .margin({ top: 5 })
63. }
64. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
