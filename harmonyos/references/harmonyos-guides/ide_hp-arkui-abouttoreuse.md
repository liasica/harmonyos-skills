---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide_hp-arkui-abouttoreuse
title: @performance/hp-arkui-avoid-update-auto-state-var-in-aboutToReuse
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-avoid-update-auto-state-var-in-aboutToReuse
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:03+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:4b03d6cf8255085d750852a1f25f3cd3fdce0b6af7b825a9efd695e2fc5869d9
---

避免在aboutToReuse中对自动更新值的状态变量进行更新。

通用丢帧场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-avoid-update-auto-state-var-in-aboutToReuse": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';

4. // 此处为复用的自定义组件
5. @Reusable
6. @Component
7. struct ItemComponent {
8. @State desc: string = '';
9. @State sum: number = 0;
10. @State avg: number = 0;

12. aboutToReuse(params: Record<string, Object>): void {
13. this.desc = params.desc as string;
14. this.sum = params.sum as number;
15. this.avg = params.avg as number;
16. }

18. build() {
19. Column() {
20. Text('子组件' + this.desc)
21. .fontSize(30)
22. .fontWeight(30)
23. Text('结果' + this.sum)
24. .fontSize(30)
25. .fontWeight(30)
26. Text('平均值' + this.avg)
27. .fontSize(30)
28. .fontWeight(30)
29. }
30. }
31. }

33. @Entry
34. @Component
35. struct MyComponent {
36. private data: MyDataSource = new MyDataSource();

38. aboutToAppear(): void {
39. for (let index = 0; index < 20; index++) {
40. this.data.pushData(index.toString())
41. }
42. }

44. build() {
45. Column() {
46. List() {
47. LazyForEach(this.data, (item: string) => {
48. ListItem() {
49. ItemComponent({ desc: item, sum: 0, avg: 0 })
50. }
51. .width('100%')
52. .height(100)
53. }, (item: string) => item)
54. }
55. .width('100%')
56. .height('100%')
57. }
58. .width('100%')
59. .height('100%')
60. }
61. }
```

## 反例

```
1. // 源码文件，请以工程实际为准
2. import { MyDataSource } from './MyDataSource';

4. // 此处为复用的自定义组件
5. @Reusable
6. @Component
7. struct ItemComponent {
8. @State desc: string = '';
9. @State sum: number = 0;
10. @Link avg: number;

12. aboutToReuse(params: Record<string, Object>): void {
13. this.desc = params.desc as string;
14. this.sum = params.sum as number;
15. this.avg = params.avg as number;
16. }

18. build() {
19. Column() {
20. Text('子组件' + this.desc)
21. .fontSize(30)
22. .fontWeight(30)
23. Text('结果' + this.sum)
24. .fontSize(30)
25. .fontWeight(30)
26. Text('平均值' + this.avg)
27. .fontSize(30)
28. .fontWeight(30)
29. }
30. }
31. }

33. @Entry
34. @Component
35. struct MyComponent {
36. private data: MyDataSource = new MyDataSource();

38. aboutToAppear(): void {
39. for (let index = 0; index < 20; index++) {
40. this.data.pushData(index.toString())
41. }
42. }

44. build() {
45. Column() {
46. List() {
47. LazyForEach(this.data, (item: string) => {
48. ListItem() {
49. ItemComponent({ desc: item, sum: 0, avg: 0 })
50. }
51. .width('100%')
52. .height(100)
53. }, (item: string) => item)
54. }
55. .width('100%')
56. .height('100%')
57. }
58. .width('100%')
59. .height('100%')
60. }
61. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
