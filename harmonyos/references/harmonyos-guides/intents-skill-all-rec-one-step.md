---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-one-step
title: 功能一步达场景方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 接入方案 > 功能一步达场景方案
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:93f54bd1cfa77d3fe55f3f002d4f3bf15e6a5c167816be89607197ab5251133e
---

## 方案概述

从5.1.0(18)开始，新增功能一步达接入方案，可通过该方案实现快速打开应用内功能页面。若应用中有“查找路线”和“扫一扫”两个功能需要注册到意图框架中，让用户通过小艺快速打开对应功能页面，比如“帮我打开XXX的查找路线”、“帮我打开XXX的扫一扫”或“帮我打开XXX的扫码”，则需要在意图声明文件中声明JumpFunctionPage意图，以及上述两个功能，并实现对应意图调用。

**意图名称：跳转App功能页 JumpFunctionPage（端侧前台意图调用）**

| **参数类别** | **参数（中文）** | **参数（英文）** | 是否必选 | **描述** | 类型 | **数据样例** |
| --- | --- | --- | --- | --- | --- | --- |
| **Input** | 功能页面标识 | pageId | 是 | 具体功能的标识，开发者自定义。 | string | 1、2、3… |
| **Output** | 结果码 | code | 是 | 意图调用的结果码。 | number | 0：成功  其他：失败（需提前与华为侧协商，不支持自定义） |
| **Output** | 结果体 | result | 是 | 意图调用返回的数据，如果无数据则返回空。 | Record<string, Object> | 详见意图调用示例代码。 |

## 意图声明

开发者需要编辑对应的意图配置insight\_intent.json文件实现意图注册。insight\_intent.json文件需要放置在module下面的指定目录：src/main/resources/base/profile/insight\_intent.json，并且整个工程中只能出现一个insight\_intent.json文件。

```
1. {
2. "insightIntents": [
3. {
4. "intentName": "JumpFunctionPage",    // 意图名称
5. "domain": "ToolsDomain",
6. "intentVersion": "1.0.1", // 意图本身的版本号
7. // 意图调用逻辑入口
8. "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
9. "uiAbility": {
10. // 意图所在ability
11. "ability": "EntryAbility",
12. // UIAbility支持前后台两种执行模式
13. "executeMode": [
14. "foreground"
15. ]
16. },
17. "inputParams": [{ // 部分意图开放意图参数定义，格式整体参考JSON-Schema。
18. "properties": { // 描述参数列表，后续可以同级别增加其他描述节点
19. "pageId": { // 具体功能的标识的key值
20. "type": "string", // 参数类型
21. "enum": [
22. {
23. "value": "1", // 具体功能的标识的value值
24. "displayName": "查找路线", // 功能名，用于匹配用户query
25. "keywords": [
26. "查路线","查询路线","路线查询","找路线"
27. ], // 参数枚举值别名，可以用于索引、过滤，最多不超过5个
28. "displayDescription": "查找到达目的地的路线", // 功能描述
29. "icon": "https://abc.xx" // 功能图标
30. },
31. {
32. "value": "2", // 具体功能的标识的value值
33. "displayName": "扫一扫", // 功能名，用于匹配用户query
34. "keywords": [
35. "扫码"
36. ], // 参数枚举值别名，可以用于索引、过滤
37. "displayDescription": "用于扫码", // 功能描述
38. "icon": "https://abc.xx" // 功能图标
39. }
40. ]
41. }
42. }
43. }]
44. }
45. ]
46. }
```

若intentName报错Intent 'xxxxxx' is not included in domain 'xxxxxx'. Select an intent from the list of suggestions.该报错不影响正常编译及运行，请忽略。

## 端侧前台意图调用

开发者需自己实现InsightIntentExecutor，并在对应回调实现打开落地页的能力。

步骤如下：

1. 继承InsightIntentExecutor。
2. 重写对应方法，例如目标拉起前台页面，则可重写onExecuteInUIAbilityForegroundMode方法。
3. 通过意图名称，识别跳转功能页面意图(JumpFunctionPage)，在对应的方法中传递意图参数（param），并拉起对应落地页。

```
1. import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. /**
5. * 意图调用样例 */
6. export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
7. private static readonly JUMP_FUNCTION_PAGE = 'JumpFunctionPage';
8. /**
9. * override 执行前台UIAbility意图
10. *
11. * @param name 意图名称
12. * @param param 意图参数
13. * @param pageLoader 窗口
14. * @returns 意图调用结果
15. */
16. onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
17. Promise<insightIntent.ExecuteResult> {
18. // 根据意图名称分发处理逻辑。接入方可根据实际业务实现页面跳转
19. switch (name) {
20. case InsightIntentExecutorImpl.JUMP_FUNCTION_PAGE:
21. return this.jumpFunctionPage(param, pageLoader);
22. default:
23. break;
24. }
25. return Promise.resolve({
26. code: -1,
27. result: {
28. message: 'unknown intent'
29. }
30. } as insightIntent.ExecuteResult)
31. }
32. /**
33. * 实现跳转目标页面的功能
34. *
35. * @param param 意图参数
36. * @param pageLoader 窗口
37. */
38. private jumpFunctionPage(param: Record<string, Object>, pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
39. return new Promise((resolve, reject) => {
40. let pageId: string = param?.pageId as string;
41. pageLoader.loadContent('pages/'+ pageId)
42. .then(() => {
43. resolve({
44. code: 0,
45. result: {
46. message: 'Intent execute success'
47. }
48. });
49. })
50. .catch((err: BusinessError) => {
51. // TODO 调用失败的情况
52. resolve({
53. code: -1,
54. result: {
55. message: 'Intent execute failed'
56. }
57. })
58. });
59. })
60. }
61. }
```
