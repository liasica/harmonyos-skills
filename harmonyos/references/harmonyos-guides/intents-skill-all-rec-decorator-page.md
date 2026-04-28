---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-decorator-page
title: 基于Page的装饰器方案
breadcrumb: 指南 > AI > Intents Kit（意图框架服务） > 技能调用方案 > 接入方案 > 任务执行类场景方案（装饰器接入方式） > 基于Page的装饰器方案
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:e6139f751996aee9db36cc6040ba116a169574bc42ad2fb705169b90b1825ca6
---

开发者使用@InsightIntentPage装饰器进行基于Page的意图声明，可快速将已有的Page页面接入意图框架，以购买电影票的意图为例，详细说明如下：

1. 装饰器添加位置：基于Page的装饰器需要添加在Entry页面组件上，建议在目标页面中进行声明。

   ```
   1. import { InsightIntentPage } from "@kit.AbilityKit";

   3. @Builder
   4. export function PurchaseMovieTicketsIntentPageBuilder(pageName: string, param: object) {
   5. PurchaseMovieTicketsIntentPage({ param: param });
   6. }

   8. @InsightIntentPage({
   9. intentName: 'PurchaseMovieTickets',
   10. domain: 'PurchaseTickets',
   11. intentVersion: '1.0.1',
   12. displayName: '购买电影票',
   13. llmDescription: '用于在线购买电影票，允许用户选择指定影院、电影和场次时间进行购票。在用户明确表达购票需求，且已提供所有必要信息（cinema, film, time）时使用。如果信息不全或者用户只是查询电影信息、放映时间或票价，不应调用此工具。',
   14. uiAbility: 'EntryAbility',
   15. pagePath: './ets/pages/MainPage',
   16. navDestinationName: 'PurchaseMovieTicketsIntentPage',
   17. parameters: {
   18. "type": "object",
   19. "properties": {
   20. "cinema": {
   21. "type": "string",
   22. "description": "目标影院名称，仅支持平台合作的影院"
   23. },
   24. "film": {
   25. "type": "string",
   26. "description": "目标电影名称，需为当前上映或即将上映且在影院排片列表中的电影"
   27. },
   28. "time": {
   29. "type": "string",
   30. "description": "放映时间，必须为未来的场次，且需为影院当天有效排片时间；时间格式应为'YYYY-MM-DD HH:MM'（例如'2025-07-01 19:30'）"
   31. }
   32. },
   33. "required": ["cinema", "film", "time"]
   34. }
   35. })
   36. @Entry
   37. @Component
   38. struct PurchaseMovieTicketsIntentPage {
   39. param: object = new Object();
   40. cinema: string = '';
   41. film: string = '';
   42. time: string = '';
   43. aboutToAppear(): void {
   44. this.cinema= this.param?.['cinema'];
   45. this.film = this.param?.['film'];
   46. this.time = this.param?.['time'];
   47. }
   48. build() {
   49. NavDestination(){
   50. Text(`${this.cinema} ${this.film} ${this.time}`)
   51. .fontSize(30)
   52. .fontWeight(FontWeight.Bolder)
   53. }
   54. .title('IntentPage')
   55. .width('100%')
   56. }
   57. }
   ```
2. 装饰器的字段说明以及示例：@InsightIntentPage字段以及具体说明如下。

   | 字段名称 | 类型 | 必选 | 说明 |
   | --- | --- | --- | --- |
   | intentName | string | 是 | 意图名称，最大长度：64。 |
   | domain | string | 是 | 意图所属的功能垂域。 |
   | intentVersion | string | 是 | 意图的版本号，用于兼容性管理。 |
   | displayName | string | 是 | 意图的展示名称，用于界面显示，最大长度：64。 |
   | llmDescription | string | 否 | 意图的描述，详细描述该意图可实现的能力，便于大模型理解并调用。 |
   | parameters | Record<string, object> | 否 | 意图参数定义，描述参数类型以及含义。 |
   | uiAbility | string | 否 | 页面依赖的UiAbility名，如果不传递默认使用EntryAbility。 |
   | pagePath | string | 是 | Navigation组件所在页面的路径，路径基于Module的根目录的相对路径。 |
   | navDestinationName | string | 否 | Navigation子页面名称，如果不填写，则跳转到pagePath指定的页面。 |

   为便于大模型理解和调用，相关参数定义需要遵照[自定义意图相关信息定义规范](intents-skill-all-rec-specification.md)。
3. 装饰器的添加方式：装饰器可以直接手动添加，同时也支持一键生成装饰器，建议使用后者，此方式需要安装相应插件，详细步骤如下。

   1. 打开CodeGenie插件：在DevEco Studio右侧边栏点击CodeGenie或输入快捷键Alt/Option+U，可以进入DevEco CodeGenie。若使用非最新版本的DevEco Studio，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取并使用相关功能，具体请参考[插件获取及安装](ide-codegenie.md#section18337533718)。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/ARSHp_HsQnus3WCUwrhHRw/zh-cn_image_0000002583439369.png?HW-CC-KV=V1&HW-CC-Date=20260427T235337Z&HW-CC-Expire=86400&HW-CC-Sign=DE118BA01ED084E190F6BF9137EF565060BC93B32F65FED09ADDD413487B5A46)
   2. 框选想要接入意图框架功能的代码。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/QnFN8oAHR--EZds4FjvX4w/zh-cn_image_0000002552959324.png?HW-CC-KV=V1&HW-CC-Date=20260427T235337Z&HW-CC-Expire=86400&HW-CC-Sign=DC8545084F7AAA3815A2B7C6063670B00F7723D49F20FE3AE1358300CA1AA0E0)
   3. 在选中的代码块上右键CodeGenie > Insight Intent > 选择适合的装饰器。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/ZNi-3uCtSAaR_EpusagWVg/zh-cn_image_0000002583479325.png?HW-CC-KV=V1&HW-CC-Date=20260427T235337Z&HW-CC-Expire=86400&HW-CC-Sign=51E9FC9FBF21152AAFE9365F3F514A726CF26DC8DE63F5D150AC6A1EC6FE515B)
   4. 在DevEco CodeGenie对话框中对意图定义，功能，参数等进行描述。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/NK6d3cLvQ3CH74KwRiuQ3A/zh-cn_image_0000002552799676.png?HW-CC-KV=V1&HW-CC-Date=20260427T235337Z&HW-CC-Expire=86400&HW-CC-Sign=FF82B3E893404E3C085B60178CE3C1F3DF4D3B5CDE56A90541AFF80349D47AF1)
   5. 回车或者点击发送按钮，即可生成对应的装饰器内容。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/5Ut3sgFUTcWVL6Y1IsJxlg/zh-cn_image_0000002583439371.png?HW-CC-KV=V1&HW-CC-Date=20260427T235337Z&HW-CC-Expire=86400&HW-CC-Sign=6511B87446CCADBF37650B448D0F30D6DE8A8D2E39890ED4EF44EC1C8010DFC5)
   6. 将光标放置于要插入装饰器的位置，点击插入图标，即可在对应位置插入装饰器。

      插入前：

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/kMvNx4jLQty7x4LQr6QVAA/zh-cn_image_0000002552959326.png?HW-CC-KV=V1&HW-CC-Date=20260427T235337Z&HW-CC-Expire=86400&HW-CC-Sign=FDA350B81A1CD7F0EF76BA59DD5F7FB9DAE0C042EDED971DDA336E4722E84A7B)

      插入后：

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/R-h4hd3VRH-Q1Iqf_tkvFw/zh-cn_image_0000002583479327.png?HW-CC-KV=V1&HW-CC-Date=20260427T235337Z&HW-CC-Expire=86400&HW-CC-Sign=7A34D09FF1BEC1CE3096FEBF8ED79D70427229AA40D0FD78C5456E6655B6A2EF)
4. 装饰器的使用约束和说明：

   * 仅支持Navigation页面架构跳转。
   * 该跳转不能有自定义上下文依赖，比如必须打开前置页面才能跳转，开发者需要进行验证，确认兜底策略。
   * 跳转页面时，默认使用Navigation页面栈进行push，如果开发者需要实现其他跳转逻辑，则需要自行适配。
