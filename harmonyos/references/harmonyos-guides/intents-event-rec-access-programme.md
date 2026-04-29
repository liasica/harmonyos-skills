---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-event-rec-access-programme
title: 接入方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 事件推荐方案 > 接入方案
category: harmonyos-guides
scraped_at: 2026-04-29T13:43:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:07dfdde998150fd9d013ea4e41a7e630d639c525834186a000ca8fd8da5288ad
---

## 方案概述

当开发者有事件想要通知到用户时，可通过应用/元服务的云侧服务器向智慧分发平台推送事件内容（意图共享）。系统通过智慧决策判断事件发生的条件，在满足条件时，向用户推荐事件提醒卡片，当用户点击卡片后，可跳转到应用/元服务的详情页查看事件详情（意图调用）。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/TaLYFCLAS4u30fHwolBdGg/zh-cn_image_0000002589245627.png?HW-CC-KV=V1&HW-CC-Date=20260429T054331Z&HW-CC-Expire=86400&HW-CC-Sign=819AE613BD5C85B73DBED3BC64044A1A8142BFAD74E6677952BF95F31121A522)

## 流程图

1. 开发者获取云侧事件捐赠所需的SID（Service OpenID）。
2. 当用户有订单事件后，开发者云将事件内容和SID同步到业务云。
3. 华为内部会根据事件和具体场景制定事件服务推出规则和时机。
4. 在满足制定规则场景下展示对应用户事件，增加服务曝光率。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/-jcCO2nZRJSNDmlxyFkAiw/zh-cn_image_0000002558765818.png?HW-CC-KV=V1&HW-CC-Date=20260429T054331Z&HW-CC-Expire=86400&HW-CC-Sign=0AB6B95D991AC765A106A31D359B8BBB4DBF631F3FFD449F50F219A04CE4BB99)

## 意图注册

以还款待办事件提醒特性为例，首先要注册查看还款意图（ViewRepayment），详见[各垂域意图Schema](../service/intents-schema-0000001901962713.md)。

开发者需要编辑对应的意图配置insight\_intent.json文件实现意图声明。insight\_intent.json文件需要放置在任意一个module下面的指定目录：src/main/resources/base/profile/insight\_intent.json，并且整个工程中只能存在一个insight\_intent.json文件。

```
1. {
2. // 应用支持的意图列表
3. // 必须声明应用支持插件包含的必选意图，应用上架时会进行校验
4. "insightIntents": [
5. {
6. // 意图名称
7. // 名称应当遵循意图框架规范，当前仅支持预置垂域意图，不允许自定义
8. // 应用内意图名称唯一，不允许出现相同的名称定义
9. "intentName": "ViewRepayment",
10. // 意图所属的垂域
11. "domain": "BankingDomain",
12. // 意图版本号
13. // 插件引用意图时会校验该版本号，只有和插件定义的版本号一致才能正常调用
14. "intentVersion": "1.0.1",
15. // 意图调用逻辑入口
16. "srcEntry": "./ets/entryability/InsightIntentExecutorImpl.ets",
17. "uiAbility": {
18. // 意图所在ability
19. "ability": "EntryAbility",
20. // UIAbility支持前后台两种执行模式
21. "executeMode": [
22. "background",
23. "foreground"
24. ]
25. }
26. }
27. ]
28. }
```

## 获取SID

说明

API文档参见：[意图框架API参考 > getSid](../harmonyos-references/intents-arkts-api-insightintent.md#insightintentgetsid)。

云侧事件捐赠凭证SID（Service OpenID）优先从缓存获取，当缓存获取失败可以强制从云侧获取新的SID。

```
1. import { insightIntent } from '@kit.IntentsKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. // 根据实际代码上下文自行传入合适的context
5. insightIntent.getSid(context, false) // 优先获取缓存SID，改为true则强制从云侧获取新SID
6. .then((sid: string) => {
7. // 获取SID成功
8. console.info('getSid succeed!');
9. }).catch((error: BusinessError) => {
10. // 获取SID失败
11. console.error(`getSid failed! error=${error.code} reason=${error.message}`);
12. });
```

## 云侧意图共享

### 意图共享接口调用

应用/元服务通过[云侧意图共享接口](../harmonyos-references/intents-rest-api-intent-share.md#功能介绍)，把对应意图的相关事件数据共享给Intents Kit，用于事件提醒服务。

### 事件撤销接口调用

当应用/元服务共享的意图相关事件数据超过时效期，Intents Kit需要通过[云侧事件撤销接口](../harmonyos-references/intents-rest-api-revoke-event.md)把相关事件数据撤销，以避免触发超过时效期的事件提醒。

## 端侧意图调用

开发者需要自己实现InsightIntentExecutor，并在对应回调实现打开落地页（点击推荐卡片跳转的界面）的能力，ViewRepayment的意图调用字段定义见对应[垂域意图Schema](../service/intents-schema-0000001901962713.md)定义表。

步骤如下：

1. 继承InsightIntentExecutor。
2. 重写对应方法，例如目标拉起前台页面，则可重写onExecuteInUIAbilityForegroundMode方法。
3. 通过意图名称，识别查看还款意图（ViewRepayment）。
4. 在对应的方法中传递意图参数（param），并拉起对应落地页（如还款页面）。

   ```
   1. import { insightIntent, InsightIntentExecutor } from '@kit.AbilityKit';
   2. import { window } from '@kit.ArkUI';
   3. import { BusinessError } from '@kit.BasicServicesKit';

   5. /**
   6. * 意图调用样例 */
   7. export default class InsightIntentExecutorImpl extends InsightIntentExecutor {
   8. private static readonly VIEW_REPAYMENT = 'ViewRepayment';
   9. /**
   10. * override 执行前台UIAbility意图
   11. *
   12. * @param name 意图名称
   13. * @param param 意图参数
   14. * @param pageLoader 窗口
   15. * @returns 意图调用结果
   16. */
   17. onExecuteInUIAbilityForegroundMode(name: string, param: Record<string, Object>, pageLoader: window.WindowStage):
   18. Promise<insightIntent.ExecuteResult> {
   19. // 根据意图名称分发处理逻辑。接入方可根据实际业务实现页面跳转
   20. switch (name) {
   21. case InsightIntentExecutorImpl.VIEW_REPAYMENT:
   22. return this.viewRepayment(param, pageLoader);
   23. default:
   24. break;
   25. }
   26. return Promise.resolve({
   27. code: -1,
   28. result: {
   29. message: 'unknown intent'
   30. }
   31. } as insightIntent.ExecuteResult)
   32. }

   34. /**
   35. * 实现调用查看还款功能
   36. *
   37. * @param param 意图参数
   38. * @param pageLoader 窗口
   39. */
   40. private viewRepayment(param: Record<string, Object>, pageLoader: window.WindowStage): Promise<insightIntent.ExecuteResult> {
   41. return new Promise((resolve, reject) => {
   42. let para: Record<string, string> = {
   43. 'result': JSON.stringify(param)
   44. };
   45. let localStorage: LocalStorage = new LocalStorage(para);
   46. // TODO 实现意图调用，loadContent的入参为查看还款落地页路径，例如：'pages/Index'
   47. pageLoader.loadContent('pages/Index', localStorage)
   48. .then(() => {
   49. let entityId: string = (param.items as Array<object>)?.[0]?.['entityId'];
   50. // TODO 调用成功的情况，此处可以打印日志
   51. resolve({
   52. code: 0,
   53. result: {
   54. message: 'Intent execute succeed'
   55. }
   56. });
   57. })
   58. .catch((err: BusinessError) => {
   59. // TODO 调用失败的情况
   60. resolve({
   61. code: -1,
   62. result: {
   63. message: 'Intent execute failed'
   64. }
   65. })
   66. });
   67. })
   68. }
   69. }
   ```
