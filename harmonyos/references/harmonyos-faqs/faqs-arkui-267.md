---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-267
title: 如何实现文本展开收起功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > 如何实现文本展开收起功能
category: harmonyos-faqs
scraped_at: 2026-04-28T08:26:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:349b0b366c77dbcefd7b23b726a0354e368efbd955d7e3ad4d6d47865e59367d
---

使用[measureTextSize](../harmonyos-references/arkts-apis-uicontext-measureutils.md#measuretextsize12)接口实现文字段落展开收起的功能，具体实现如下所示：

```
1. // Text line width
2. const TEXT_WIDTH: number = 350;
3. // Number of lines to show when collapsed
4. const COLLAPSE_LINES: number = 2;
5. const ELLIPSIS: string = '...';
6. const EXPAND_STR: string = 'Expand';
7. const COLLAPSE_STR: string = 'Collapse';
8. const FULL_TEXT: string =
9. 'HarmonyOS provides a UI development framework called the ArkUI Framework. The ArkUI Framework provides developers with ' +
10. 'essential capabilities for application UI development, such as multiple components, layout calculations, animation capabilities, UI interaction, drawing, etc.\n' +
11. 'The ArkUI Framework offers two development paradigms for developers with different purposes and technical backgrounds: ' +
12. 'the Declarative Development Paradigm based on ArkTS (referred to as the "Declarative Development Paradigm") ' +
13. 'and the JS-compatible Web Development Paradigm (referred to as the "Web Development Paradigm"). Here is a simple comparison of these two development paradigms.'

15. @Entry
16. @Component
17. struct TextCollapseTest {
18. @State title: string = FULL_TEXT;
19. @State suffixStr: string = '';
20. private expanded: boolean = true;
21. private needProcess: boolean = true;

23. aboutToAppear(): void {
24. this.process();
25. }

27. process(): void {
28. if (this.expanded) {
29. this.collapseText();
30. } else {
31. this.expandText();
32. }
33. }

35. // Expand text
36. expandText(): void {
37. if (this.needProcess) {
38. this.suffixStr = COLLAPSE_STR;
39. this.expanded = true;
40. this.title = FULL_TEXT;
41. }
42. }

44. // Collapse text
45. collapseText(): void {
46. if (!this.needProcess) {
47. this.suffixStr = '';
48. return;
49. }
50. // Size of expanded text
51. let expandSize: SizeOptions = this.getUIContext().getMeasureUtils().measureTextSize({
52. textContent: FULL_TEXT,
53. constraintWidth: TEXT_WIDTH,
54. fontSize: 30
55. });

57. // Size of text to be collapsed
58. let collapseSize: SizeOptions = this.getUIContext().getMeasureUtils().measureTextSize({
59. textContent: FULL_TEXT,
60. constraintWidth: TEXT_WIDTH,
61. fontSize: 30,
62. maxLines: COLLAPSE_LINES
63. });

65. // No processing needed when collapsed and expanded text heights are equal
66. if (!expandSize || !collapseSize || (expandSize.height as number) == (collapseSize.height as number)) {
67. this.needProcess = false;
68. return;
69. }

71. let clipTitle: string = FULL_TEXT;
72. this.suffixStr = EXPAND_STR;
73. // Use binary search to find string length that fits exactly two lines
74. let leftCursor: number = 0;
75. let rightCursor: number = this.title.length;
76. let cursor: number = Math.floor(rightCursor / 2);
77. let tempTitle: string = '';
78. // Binary search to find the maximum text length fitting exactly two lines
79. while (true) {
80. tempTitle = this.title.substring(0, cursor) + ELLIPSIS + EXPAND_STR;
81. const currentLinesTextSize: SizeOptions = this.getUIContext().getMeasureUtils().measureTextSize({
82. textContent: tempTitle,
83. fontSize: 30,
84. wordBreak: WordBreak.BREAK_ALL,
85. constraintWidth: TEXT_WIDTH
86. });

88. if ((currentLinesTextSize.height as number) > (collapseSize.height as number)) {
89. // Current text exceeds two lines, continue searching left
90. rightCursor = cursor;
91. cursor = leftCursor + Math.floor((cursor - leftCursor) / 2);
92. } else {
93. // Current text less than two lines, might be ok but still need to search right
94. leftCursor = cursor;
95. cursor += Math.floor((rightCursor - cursor) / 2);
96. }
97. if (Math.abs(rightCursor - leftCursor) <= 1) {
98. // Pointers almost overlap, meaning we found the position
99. break;
100. }
101. }
102. clipTitle = this.title.substring(0, cursor - 1);
103. this.title = clipTitle + ELLIPSIS;
104. this.expanded = false;
105. }

107. build() {
108. Row() {
109. Column() {
110. Text() {
111. Span(this.title)
112. if (this.needProcess) {
113. Span(this.suffixStr)
114. .fontColor(Color.Orange)
115. .onClick(() => {
116. this.process();
117. })
118. }
119. }
120. .fontSize(30)
121. .fontWeight(FontWeight.Bold)
122. .width(TEXT_WIDTH)
123. }
124. .width('100%')
125. }
126. .height('100%')
127. }
128. }
```

[TextExpansionAndCollapseFunctions.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/TextExpansionAndCollapseFunctions.ets#L21-L149)
