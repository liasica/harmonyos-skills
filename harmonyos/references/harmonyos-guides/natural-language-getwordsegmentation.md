---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/natural-language-getwordsegmentation
title: 分词
breadcrumb: 指南 > AI > Natural Language Kit（自然语言理解服务） > 分词
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:49+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7bd784749bee87a86ab7d7d78e64bfa40b8eb307e58871224945a2dd467d6fbe
---

## 适用场景

分词的目的是让文本文件的中文、英文、数字内容变成一个一个的单词或者词组，从而为后续的转变为词向量提供基础。使用场景例如搜索引擎会将用户输入的文本分词处理后提取关键词送搜索。

## 约束与限制

该能力当前不支持模拟器。

| AI能力 | 约束 |
| --- | --- |
| 分词 | - 支持的语言：简体中文、英文、繁体中文。  - 文本长度：不超过1000字符。 |

## 开发步骤

1. 引用相关类添加至工程。

   ```
   1. import { textProcessing } from '@kit.NaturalLanguageKit';
   ```
2. 配置输入文本框和按钮，调用分词[textProcessing.getWordSegment](../harmonyos-references/natural-language-text-processing-api.md#textprocessinggetwordsegment)接口。

   ```
   1. private inputText: string = '';
   2. @State outputText: string = '';

   4. TextInput({ placeholder: '请输入文本' })
   5. .height(40)
   6. .fontSize(16)
   7. .width('90%')
   8. .margin(10)
   9. .onChange((value: string) => {
   10. this.inputText = value;
   11. })

   13. Button('获取分词结果')
   14. .type(ButtonType.Capsule)
   15. .fontColor(Color.White)
   16. .width('45%')
   17. .margin(10)
   18. .onClick(async () => {
   19. try {
   20. let result = await textProcessing.getWordSegment(this.inputText);
   21. this.outputText = this.formatWordSegmentResult(result);
   22. } catch (err) {
   23. console.error(`getWordSegment errorCode: ${err.code}, errorMessage: ${err.message}`);
   24. }
   25. })
   ```
3. 在界面上展示分词结果[WordSegment](../harmonyos-references/natural-language-text-processing-api.md#wordsegment)。

   ```
   1. private formatWordSegmentResult(segments: textProcessing.WordSegment[]): string {
   2. let output = 'Word Segments:\n';
   3. segments.forEach((segment, index) => {
   4. output += `Word[${index}]: ${segment.word}, Tag: ${segment.wordTag}\n`;
   5. });
   6. return output;
   7. }
   ```

## 开发实例

```
1. import { textProcessing } from '@kit.NaturalLanguageKit';

3. @Entry
4. @Component
5. struct Index {
6. private inputText: string = '';
7. @State outputText: string = '';

9. build() {
10. Column() {
11. TextInput({ placeholder: '请输入文本' })
12. .height(40)
13. .fontSize(16)
14. .width('90%')
15. .margin(10)
16. .onChange((value: string) => {
17. this.inputText = value;
18. })

20. Scroll() {
21. Text(this.outputText)
22. .fontSize(16)
23. .width('90%')
24. .margin(10)
25. }
26. .height('40%')

28. // 调用分词接口
29. Row() {
30. Button('获取分词结果')
31. .type(ButtonType.Capsule)
32. .fontColor(Color.White)
33. .width('45%')
34. .margin(10)
35. .onClick(async () => {
36. try {
37. let result = await textProcessing.getWordSegment(this.inputText);
38. this.outputText = this.formatWordSegmentResult(result);
39. } catch (err) {
40. console.error(`getWordSegment errorCode: ${err.code}, errorMessage: ${err.message}`);
41. }
42. })
43. }
44. }
45. .width('100%')
46. .height('100%')
47. .justifyContent(FlexAlign.Center)
48. }

50. // 分词结果转义
51. private formatWordSegmentResult(segments: textProcessing.WordSegment[]): string {
52. let output = 'Word Segments:\n';
53. segments.forEach((segment, index) => {
54. output += `Word[${index}]: ${segment.word}, Tag: ${segment.wordTag}\n`;
55. });
56. return output;
57. }
58. }
```
