---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-use-reusable-component
title: @performance/hp-arkui-use-reusable-component
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-use-reusable-component
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:10+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:30f5afadb4a69b4a7010a11ebe849c6bb1d3e882bbfbd9cc75f744177fa0429e
---

建议复杂组件的定义，尽量使用组件复用。

滑动丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-use-reusable-component": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';
3. import { GoodItems } from './data/DataEntry';

5. @Reusable
6. @Component
7. struct GoodItemComponent {
8. @State introduce: string = ''
9. @State price: string = ''
10. @State numb: string = ''

12. aboutToReuse(params: Record<string, ESObject>) {
13. this.introduce = params.introduce
14. this.price = params.price
15. this.numb = params.numb
16. }

18. build() {
19. Column() {
20. Text(this.introduce)
21. .fontSize(14)
22. .padding({ left: 5, right: 5 })
23. .margin({ top: 5 })
24. Row() {
25. Text('￥')
26. .fontSize(10)
27. .fontColor(Color.Red)
28. .baselineOffset(-4)
29. Text(this.price)
30. .fontSize(16)
31. .fontColor(Color.Red)
32. Text(this.numb)
33. .fontSize(10)
34. .fontColor(Color.Gray)
35. .baselineOffset(-4)
36. .margin({ left: 5 })

38. }
39. .width('100%')
40. .justifyContent(FlexAlign.SpaceBetween)
41. .padding({ left: 5, right: 5 })
42. .margin({ top: 15 })
43. }
44. }
45. }

47. @Entry
48. @Component
49. struct MyComponent{
50. private data: MyDataSource = new MyDataSource([]);

52. build() {
53. Column() {
54. LazyForEach(this.data, (item: GoodItems, index) => {
55. GridItem() {
56. GoodItemComponent({
57. introduce: item.data.introduce,
58. price: item.data.price,
59. numb: item.data.numb,
60. }).reuseId(item.numb)
61. }
62. }, (item: GoodItems) => item.index)
63. }
64. }
65. }
```

## 反例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';
3. import { GoodItems } from './data/DataEntry';

5. @Entry
6. @Component
7. struct MyComponent{
8. private data: MyDataSource = new MyDataSource([]);

10. build() {
11. Column() {
12. LazyForEach(this.data, (item: GoodItems) => {
13. GridItem() {
14. Column() {
15. Text(item.introduce)
16. .fontSize(14)
17. .padding({ left: 5, right: 5 })
18. .margin({ top: 5 })
19. Row() {
20. Text('￥')
21. .fontSize(10)
22. .fontColor(Color.Red)
23. .baselineOffset(-4)
24. Text(item.price)
25. .fontSize(16)
26. .fontColor(Color.Red)
27. Text(item.numb)
28. .fontSize(10)
29. .fontColor(Color.Gray)
30. .baselineOffset(-4)
31. .margin({ left: 5 })

33. }
34. .width('100%')
35. .justifyContent(FlexAlign.SpaceBetween)
36. .padding({ left: 5, right: 5 })
37. .margin({ top: 15 })
38. }
39. .borderRadius(10)
40. .backgroundColor(Color.White)
41. .clip(true)
42. .width('100%')
43. .height(290)
44. }
45. }, (item: GoodItems) => item.index)
46. }
47. }
48. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
