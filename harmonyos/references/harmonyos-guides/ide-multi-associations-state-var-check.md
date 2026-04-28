---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-multi-associations-state-var-check
title: @performance/multiple-associations-state-var-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/multiple-associations-state-var-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:15+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:3f80f86019b62a9df4788318b0bc75ad29b9504d776fbdec6f1de187e809f9f2
---

多个组件关联同一数据时，建议在组件中使用@Watch装饰器添加更新条件，避免不必要的组件更新。

[通用丢帧场景](../best-practices/bpta-status-management.md#section117631443131915)下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/multiple-associations-state-var-check": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. @Observed
2. class UIStyle {
3. fontSize: number = 0;
4. fontColor: string = '';
5. isChecked: boolean = false;
6. }
7. @Entry
8. @Component
9. struct MultipleAssociationsStateVarNoReport0 {
10. @State uiStyle: UIStyle = new UIStyle();
11. private listData: string[] = [];
12. aboutToAppear(): void {
13. for (let i = 0; i < 10; i++) {
14. this.listData.push(`ListItemComponent ${i}`);
15. }
16. }
17. build() {
18. Row() {
19. Column() {
20. CompA({item: '1', index: 1, subStyle: this.uiStyle})
21. CompB({item: '2', index: 2, subStyle: this.uiStyle})
22. CompC({item: '3', index: 3, subStyle: this.uiStyle})
23. Text('change state var')
24. .onClick(()=>{
25. this.uiStyle.fontSize = 20;
26. })
27. }
28. .width('100%')
29. }
30. .height('100%')
31. }
32. }
33. @Component
34. struct CompA {
35. @Prop item: string;
36. @Prop index: number;
37. @Link @Watch('onStyleChange') subStyle: UIStyle;
38. @State fontSize: number = 0;
39. isRender(): number {
40. console.info(`CompA ${this.index} Text is rendered`);
41. return this.fontSize;
42. }
43. onStyleChange() {
44. this.fontSize = this.subStyle.fontSize;
45. }
46. build() {
47. Column() {
48. Text(this.item)
49. .fontSize(this.isRender())
50. Text('abc')
51. }
52. }
53. }
54. @Component
55. struct CompB {
56. @Prop item: string;
57. @Prop index: number;
58. @Link @Watch('onStyleChange') subStyle: UIStyle;
59. @State fontColor: string = '#00ffff';
60. isRender(): number {
61. console.info(`CompB ${this.index} Text is rendered`);
62. return 10;
63. }
64. onStyleChange() {
65. this.fontColor = this.subStyle.fontColor;
66. }
67. build() {
68. Column() {
69. Text(this.item)
70. .fontSize(this.isRender())
71. .fontColor(this.fontColor)
72. Text('abc')
73. }
74. }
75. }
76. @Component
77. struct CompC {
78. @Prop item: string;
79. @Prop index: number;
80. @Link @Watch('onStyleChange') subStyle: UIStyle;
81. @State isChecked: boolean = false;
82. isRender(): number {
83. console.info(`CompC ${this.index} Text is rendered`);
84. return 50;
85. }
86. onStyleChange() {
87. this.isChecked = this.subStyle.isChecked;
88. }
89. build() {
90. Column() {
91. if (this.isChecked) {
92. Text('checked')
93. } else {
94. Text('unchecked')
95. }
96. }
97. }
98. }
```

## 反例

```
1. @Observed
2. class UIStyle {
3. fontSize: number = 0;
4. fontColor: string = '';
5. isChecked: boolean = false;
6. }
7. @Entry
8. @Component
9. struct MultipleAssociationsStateVarReport0 {
10. @State uiStyle: UIStyle = new UIStyle();
11. private listData: string[] = [];
12. aboutToAppear(): void {
13. for (let i = 0; i < 10; i++) {
14. this.listData.push(`ListItemComponent ${i}`);
15. }
16. }
17. build() {
18. Row() {
19. Column() {
20. CompA({item: '1', index: 1, subStyle: this.uiStyle})
21. CompB({item: '2', index: 2, subStyle: this.uiStyle})
22. CompC({item: '3', index: 3, subStyle: this.uiStyle})
23. Text('change state var')
24. .onClick(()=>{
25. this.uiStyle.fontSize = 20;
26. })
27. }
28. .width('100%')
29. }
30. .height('100%')
31. }
32. }
33. @Component
34. struct CompA {
35. @Prop item: string;
36. @Prop index: number;
37. @Link subStyle: UIStyle;
38. private sizeFont: number = 50;
39. isRender(): number {
40. console.info(`CompA ${this.index} Text is rendered`);
41. return this.sizeFont;
42. }
43. build() {
44. Column() {
45. Text(this.item)
46. .fontSize(this.isRender())
47. Text('abc')
48. }
49. }
50. }
51. @Component
52. struct CompB {
53. @Prop item: string;
54. @Prop index: number;
55. @Link subStyle: UIStyle;
56. private sizeFont: number = 50;
57. isRender(): number {
58. console.info(`CompB ${this.index} Text is rendered`);
59. return this.sizeFont;
60. }
61. build() {
62. Column() {
63. Text(this.item)
64. .fontSize(this.isRender())
65. .fontColor(this.subStyle.fontColor)
66. Text('abc')
67. }
68. }
69. }
70. @Component
71. struct CompC {
72. @Prop item: string;
73. @Prop index: number;
74. @Link subStyle: UIStyle;
75. private sizeFont: number = 50;
76. isRender(): number {
77. console.info(`CompC ${this.index} Text is rendered`);
78. return this.sizeFont;
79. }
80. build() {
81. Column() {
82. if (this.subStyle.isChecked) {
83. Text('checked')
84. } else {
85. Text('unchecked')
86. }
87. }
88. }
89. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
