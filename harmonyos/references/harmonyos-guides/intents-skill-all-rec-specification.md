---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-specification
title: 自定义意图相关信息定义规范
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 接入方案 > 任务执行类场景方案（装饰器接入方式） > 自定义意图相关信息定义规范
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:4d065fcdd32002690e6cc2917a167c02e1ef4653595d7c0c0517568795bafcf3
---

Intents Kit支持开发者自定义意图，开发者可通过在其代码上添加自然语言装饰器接入，装饰器中相关信息建议参考以下规范，以便于大模型更好的理解和分发调用。

1. **意图名称**

   意图名称应当遵循动词+名词的结构，命名风格通常使用大写字母开头的驼峰式命名法。命名应精准反映意图的核心功能，不宜过长（最大长度：64）或模糊。

   * 形式：动词+名词，采用驼峰命名，如CancelAlarm、CheckWeather、CreateReminder等。
   * 逻辑：意图名应直接描述该意图的操作行为，看到意图名称即可推测出意图功能，且避免使用模棱两可的词汇。例如，SwitchRoute本意是切换导航路线，但SwitchRoute也有切换路由的意思，可以改为SwitchNavigationRoute。
2. **意图描述**

   * 准确全面性：确保描述涵盖意图的全部功能，避免遗漏可能的功能点。例如，SendEmail意图的描述应明确指出其能发送邮件的能力，包括发送文本和附件功能。
   * 边界性（功能解耦）：意图必须有清晰的功能边界，避免与其他意图功能重叠或模糊，比如 ShareFile不能通过邮件分享。
   * 独立性：一个意图应只做一件事，如果功能可以拆解，应拆分为多个意图，每个意图各司其职。这样有助于保持结构简洁，功能独立，便于大语言模型的正确理解与使用。

   备注：意图描述中可以增加使用示例，举例说明使用者可以如何使用，更有利于大模型理解和分发调用。
3. **参数命名**

   参数命名应简洁且语义明确，采用小驼峰命名法，确保参数名能够直观反映其功能。

   * 语义明确：可简洁明了的看出参数用途。
4. **参数定义**

   参数定义包含参数的功能描述、参数类型（type）、必须参数（required）。

   * 功能描述：需详细描述每个参数的含义及其对意图功能的影响，每个参数应仅负责一个功能，避免单一参数混合多种用途。例如，modifyAttribute参数，不能同时具有修改属性和属性值的含义。
   * 参数类型（type）：定义参数的类型，如string、int、array等。
   * 必须参数（required）：定位意图的必须参数，使用某一意图时必须指定的参数。

以购买电影票为例，使用基于Link的装饰器来进行意图声明，实现的功能为通过deepLink的方式来拉起电影票购买页面，包含影院，影片名，时间三个自定义参数。

```
1. import { InsightIntentLink, LinkParamCategory } from "@ohos.app.ability.InsightIntentDecorator";
2. import { url } from "@kit.ArkTS";

4. @InsightIntentLink({
5. intentName: 'PurchaseMovieTickets',
6. domain: 'PurchaseTickets',
7. intentVersion: '1.0.1',
8. displayName: '购买电影票',
9. llmDescription: '用于在线购买电影票，允许用户选择指定影院、电影和场次时间进行购票。在用户明确表达购票需求，且已提供所有必要信息（cinema, film, time）时使用。如果信息不全或者用户只是查询电影信息、放映时间或票价，不应调用此工具。',
10. uri: 'decorator://ability.entry/main',
11. parameters: {
12. "type": "object",
13. "properties": {
14. "cinema": {
15. "type": "string",
16. "description": "目标影院名称，仅支持平台合作的影院"
17. },
18. "film": {
19. "type": "string",
20. "description": "目标电影名称，需为当前上映或即将上映且在影院排片列表中的电影"
21. },
22. "time": {
23. "type": "string",
24. "description": "放映时间，必须为未来的场次，且需为影院当天有效排片时间；时间格式应为'YYYY-MM-DD HH:MM'（例如'2025-07-01 19:30'）"
25. }
26. },
27. "required": ["cinema", "film", "time"]
28. },
29. paramMappings:[
30. {
31. paramName: 'cinema',
32. paramMappingName: 'location',
33. paramCategory: LinkParamCategory.LINK
34. },
35. {
36. paramName: 'film',
37. paramMappingName: 'title',
38. paramCategory: LinkParamCategory.LINK
39. },
40. {
41. paramName: 'time',
42. paramMappingName: 'time',
43. paramCategory: LinkParamCategory.LINK
44. }
45. ]
46. })
47. export class PurchaseMovieTicketsLinkIntent {
48. private purchaseMovieTickets(uri: string): void {
49. // 从want中获取传入的链接信息。
50. // 如传入的url为：decorator://ability.entry/main?location=XXX影城&title=XXX&time=2025.06.01
51. let urlObject = url.URL.parseURL(uri);
52. let location = urlObject.params.get('location');
53. if (location === "XXX影城") {
54. // ...
55. }
56. }
57. }
```
