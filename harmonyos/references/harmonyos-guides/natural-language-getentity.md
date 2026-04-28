---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/natural-language-getentity
title: 实体抽取
breadcrumb: 指南 > AI > Natural Language Kit（自然语言理解服务） > 实体抽取
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:50+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:97832d8d1bcbb5788b814028579fdf8cb97f83a4b6cbec99207bf2d7f5d7a0be
---

## 适用场景

实体抽取是自然语言处理服务的一项关键能力。通过综合分析上下文信息，从文本中准确识别出多种类型的实体：

1. 日期时间（DATETIME）：提取文本中的具体日期，如“2024年6月18日”等。
2. 电子邮件（EMAIL）：识别文本中的电子邮件地址，如“\*\*\*@example.com”。
3. 快递单号（EXPRESS\_NO）：抽取文本中的快递单号信息。
4. 航班号（FLIGHT\_NO）：定位文本中的航班号，如“CA1234”等。
5. 地址（LOCATION）：从文本中提取详细的地址描述。
6. 人名（NAME）：找出文本中出现的人名信息。
7. 手机号（PHONE\_NO）：识别文本中的手机号码。
8. 网址（URL）：抽取文本中的网址链接。
9. 验证码（VERIFICATION\_CODE）：定位文本中的验证码数字。
10. 身份证号（ID\_NO）：识别文本中的身份证号码信息。

通过准确抽取以上多种类型的实体信息，该项能力可以广泛应用于新闻阅读、信息检索、客户服务、社交聊天、金融运营等多种场景。例如，在新闻阅读场景中，可以对新闻正文进行实体抽取，并对人名、地名、时间、网址等关键实体信息进行高亮标识，帮助读者快速获取文章要点；在客服场景，通过抽取用户留言中的手机号、快递单号、验证码等信息，客服人员能够更高效地定位问题并给出解决方案。实体抽取为各行业的智能化应用提供了坚实的基础支持。

## 约束与限制

该能力当前不支持模拟器。

| AI能力 | 约束 |
| --- | --- |
| 实体抽取 | - 支持的语言：简体中文、英文、繁体中文。  - 支持的实体：时间、地点、邮箱、快递单号、航班号、人名、电话号码、网址链接、验证码、证件号。  - 文本长度：不超过1000字符。 |

## 开发步骤

1. 在使用实体抽取功能时，将实现实体抽取的类添加至工程。

   ```
   1. import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';
   ```
2. 配置输入文本框。

   ```
   1. private inputText: string = '张三的电话号码是12345';
   2. @State outputText: string = '';

   4. TextInput({ placeholder: '请输入文本', text: this.inputText })
   5. .height(40)
   6. .fontSize(16)
   7. .width('90%')
   8. .margin(10)
   9. .onChange((value: string) => {
   10. this.inputText = value;
   11. })
   ```
3. 配置按钮，调用实体抽取[textProcessing.getEntity](../harmonyos-references/natural-language-text-processing-api.md#textprocessinggetentity)接口。

   ```
   1. Button('获取实体结果')
   2. .type(ButtonType.Capsule)
   3. .fontColor(Color.White)
   4. .width('45%')
   5. .margin(10)
   6. .onClick(async () => {
   7. try {
   8. let result = await textProcessing.getEntity(this.inputText, {entityTypes: [EntityType.NAME, EntityType.PHONE_NO]});
   9. this.outputText = this.formatEntityResult(result);
   10. } catch (err) {
   11. console.error(`getEntity errorCode: ${err.code}, errorMessage: ${err.message}`);
   12. this.outputText = 'Error occurred while getting entities.';
   13. }
   14. })
   ```
4. 在界面上展示实体抽取结果。

   ```
   1. private formatEntityResult(entities: textProcessing.Entity[]): string {
   2. if (!entities || !entities.length) {
   3. return 'No entities found.';
   4. }

   6. let output = 'Entities:\n';
   7. for (let i = 0; i < entities.length; i++) {
   8. let entity = entities[i];
   9. output += `Entity[${i}]:\n`;
   10. output += `  oriText: ${entity.text}\n`;
   11. output += `  charOffset: ${entity.charOffset}\n`;
   12. output += `  entityType: ${entity.type}\n`;
   13. output += `  jsonObject: ${entity.jsonObject}\n\n`;
   14. }
   15. return output;
   16. }
   ```

## 开发实例

```
1. import { textProcessing, EntityType } from '@kit.NaturalLanguageKit';

3. @Entry
4. @Component
5. struct Index {
6. private inputText: string = '张三的电话号码是12345';
7. @State outputText: string = '';

9. build() {
10. Column() {
11. TextInput({ placeholder: '请输入文本', text: this.inputText })
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

28. // 调用实体抽取接口
29. Row() {
30. Button('获取实体结果')
31. .type(ButtonType.Capsule)
32. .fontColor(Color.White)
33. .width('45%')
34. .margin(10)
35. .onClick(async () => {
36. try {
37. let result = await textProcessing.getEntity(this.inputText, {entityTypes: [EntityType.NAME, EntityType.PHONE_NO]});
38. this.outputText = this.formatEntityResult(result);
39. } catch (err) {
40. console.error(`getEntity errorCode: ${err.code}, errorMessage: ${err.message}`);
41. this.outputText = 'Error occurred while getting entities.';
42. }
43. })
44. }
45. }
46. .width('100%')
47. .height('100%')
48. .justifyContent(FlexAlign.Center)
49. }

51. // 实体结果转义
52. private formatEntityResult(entities: textProcessing.Entity[]): string {
53. if (!entities || !entities.length) {
54. return 'No entities found.';
55. }

57. let output = 'Entities:\n';
58. for (let i = 0; i < entities.length; i++) {
59. let entity = entities[i];
60. output += `Entity[${i}]:\n`;
61. output += `  oriText: ${entity.text}\n`;
62. output += `  charOffset: ${entity.charOffset}\n`;
63. output += `  entityType: ${entity.type}\n`;
64. output += `  jsonObject: ${entity.jsonObject}\n\n`;
65. }
66. return output;
67. }
68. }
```
