---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-function-search
title: 功能搜索方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 本地搜索方案 > 接入方案 > 功能搜索方案
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:43+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:ae799bf341e312788c46012a8c5dfc2c123f194a05c6c46b627cb4348542c282
---

## 方案概述

从5.1.0(18)开始，新增功能搜索接入方案，可通过该方案实现快速打开应用内功能页面。开发者将应用内的功能在意图声明文件中声明，并实现对应的意图调用，即可实现用户在小艺搜索入口直接搜索到应用内功能，点击后可直接拉起应用，直达功能页面。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/cJ8tcoF0R3-Gw0u1pkNFlg/zh-cn_image_0000002583479339.png?HW-CC-KV=V1&HW-CC-Date=20260427T235342Z&HW-CC-Expire=86400&HW-CC-Sign=75553A5534015546A0F4330CA2D4953541075D7F57BB67AF2A818CB4F6C0439C)

**意图名称：跳转App功能页 JumpFunctionPage（端侧前台意图调用）**

| **参数类别** | **参数（中文）** | **参数（英文）** | 是否必选 | **描述** | 类型 | **数据样例** |
| --- | --- | --- | --- | --- | --- | --- |
| **Input** | 功能页面标识 | pageId | 是 | 具体功能的标识，开发者自定义。 | string | 1、2、3…。 |
| **Output** | 结果码 | code | 是 | 意图调用的结果码。 | number | 0：成功。  其他：失败（需提前与华为侧协商，不支持自定义）。 |
| **Output** | 结果体 | result | 是 | 意图调用返回的数据，如果无数据则返回空。 | Record<string, Object> | 详见意图调用示例代码。 |

## 意图声明

开发者需要编辑对应的意图配置insight\_intent.json文件实现意图注册。insight\_intent.json文件需要放置在module下面的指定目录：src/main/resources/base/profile/insight\_intent.json，并且整个工程中只能存在一个insight\_intent.json文件。

```
1. {
2. "insightIntents": [
3. {
4. "intentName": "JumpFunctionPage",    // 功能搜意图
5. "domain": "ToolsDomain",
6. "intentVersion": "1.0.1", // 意图版本号
7. // 意图调用逻辑入口
8. "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
9. "uiAbility": {
10. // 意图所在ability
11. "ability": "EntryAbility",
12. // UIAbility仅支持前台执行模式
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
24. "displayName": "查找路线", // 功能名，小艺搜索展示
25. "keywords": [
26. "查路线"
27. ], // 参数枚举值别名，可以用于索引、过滤，最多不超过5个
28. "displayDescription": "查找到达目的地的路线", // 功能描述，小艺搜索展示
29. "icon": "https://abc.xx" // 功能图标，小艺搜索展示
30. },
31. {
32. "value": "2", // 具体功能的标识的value值
33. "displayName": "扫一扫", // 功能名，小艺搜索展示
34. "keywords": [
35. "扫码"
36. ], // 参数枚举值别名，可以用于索引、过滤
37. "displayDescription": "用于扫码", // 功能描述，小艺搜索展示
38. "icon": "https://abc.xx" // 功能图标，小艺搜索展示
39. }
40. ]
41. }
42. }
43. }]
44. }
45. ]
46. }
```

## 端侧前台意图调用

开发者自行实现InsightIntentExecutor，并在对应回调实现打开落地页的能力。

步骤如下：

1. 继承InsightIntentExecutor。
2. 重写对应方法，例如目标拉起前台页面，则可重写onExecuteInUIAbilityForegroundMode方法。
3. 通过意图名称，识别跳转功能页面意图（JumpFunctionPage），在对应的方法中传递意图参数（param），并拉起对应落地页。

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
