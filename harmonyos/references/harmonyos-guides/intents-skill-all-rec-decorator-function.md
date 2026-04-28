---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/intents-skill-all-rec-decorator-function
title: 基于函数的装饰器方案
category: harmonyos-guides
scraped_at: 2026-04-28T07:53:40+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:b5a79c0b3d706c409be339d480983faf33c9450856fb3a05321a13a1bd02a5f6
---

开发者使用@InsightIntentFunction和@InsightIntentFunctionMethod装饰器进行基于函数的意图声明，可快速将已有的函数功能接入意图框架，以购买电影票的意图为例，详细说明如下：

1. 装饰器添加位置：在目标执行函数上添加@InsightIntentFunctionMethod装饰器，以及在目标执行函数所属Class上添加@InsightIntentFunction进行意图声明，且仅支持在静态方法上使用。

   ```
   1. import { insightIntent, InsightIntentFunction, InsightIntentFunctionMethod } from '@kit.AbilityKit';

   3. @InsightIntentFunction()
   4. export class PurchaseMovie {

   6. @InsightIntentFunctionMethod ({
   7. intentName: 'PurchaseMovieTickets',
   8. domain: 'PurchaseTickets',
   9. intentVersion: '1.0.1',
   10. displayName: '购买电影票',
   11. llmDescription: '用于在线购买电影票，允许用户选择指定影院、电影和场次时间进行购票。在用户明确表达购票需求，且已提供所有必要信息（cinema, film, time）时使用。如果信息不全或者用户只是查询电影信息、放映时间或票价，不应调用此工具。',
   12. parameters: {
   13. "type": "object",
   14. "properties": {
   15. "cinema": {
   16. "type": "string",
   17. "description": "目标影院名称，仅支持平台合作的影院"
   18. },
   19. "film": {
   20. "type": "string",
   21. "description": "目标电影名称，需为当前上映或即将上映且在影院排片列表中的电影"
   22. },
   23. "time": {
   24. "type": "string",
   25. "description": "放映时间，必须为未来的场次，且需为影院当天有效排片时间；时间格式应为'YYYY-MM-DD HH:MM'（例如'2025-07-01 19:30'）"
   26. }
   27. },
   28. "required": ["cinema", "film", "time"]
   29. }
   30. })
   31. static executePurchaseMovieIntent(cinema: string, film: string, time: string): insightIntent.ExecuteResult {
   32. return {
   33. code: 0, //意图执行成功时code必须为0
   34. result: {
   35. orderNumber: "XXXXXX",
   36. resultDesc:`电影票${film}购买成功`
   37. }
   38. };
   39. }
   40. }
   ```

   函数返回结果必须为insightIntent.ExecuteResult结构，且该结构result对象中需增加resultDesc字段对结果进行描述，模型依据此描述生成该意图执行结果的小艺回复话术。请参考上述示例代码。
2. 装饰器的字段说明以及示例：@InsightIntentFunction不涉及参数，@InsightIntentFunctionMethod字段以及具体说明如下。

   | 字段名称 | 类型 | 必选 | 说明 |
   | --- | --- | --- | --- |
   | intentName | string | 是 | 意图名称，最大长度：64。 |
   | domain | string | 是 | 意图所属的功能垂域。 |
   | intentVersion | string | 是 | 意图的版本号，用于兼容性管理。 |
   | displayName | string | 是 | 意图的展示名称，用于界面显示，最大长度：64。 |
   | llmDescription | string | 否 | 意图的描述，详细描述该意图可实现的能力，便于大模型理解并调用。 |
   | parameters | Record<string, object> | 否 | 意图参数定义，描述参数类型以及含义。 |

   为便于大模型理解和调用，相关参数定义需要遵照[自定义意图相关信息定义规范](intents-skill-all-rec-specification.md)进行设定。
3. 装饰器的添加方式：装饰器可以直接手动添加，同时也支持一键生成装饰器，建议使用后者，此方式需要安装相应插件，详细步骤如下。

   1. 打开CodeGenie插件：在DevEco Studio右侧边栏点击CodeGenie或输入快捷键Alt/Option+U，可以进入DevEco CodeGenie。若使用非最新版本的DevEco Studio，可通过[下载中心](https://developer.huawei.com/consumer/cn/download/deveco-codegenie)获取并使用相关功能，具体请参考[插件获取及安装](ide-codegenie.md#section18337533718)。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/l9heM5QASBuDyjsLYoXyzg/zh-cn_image_0000002552799678.png?HW-CC-KV=V1&HW-CC-Date=20260427T235337Z&HW-CC-Expire=86400&HW-CC-Sign=9BBC8FD3A2EEEA03566AE4C7CD79BDAE7FD70836A33ADC7DA0C9DA8CE28B5AED)
   2. 框选想要接入意图框架功能的代码。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/J4OvdUBeSfaikDgNnJ4DRg/zh-cn_image_0000002583439373.png?HW-CC-KV=V1&HW-CC-Date=20260427T235337Z&HW-CC-Expire=86400&HW-CC-Sign=05E2A6DCDE7A7839071C54E9C25506E4CF4D8C429B04E8480212B798E39D9B30)
   3. 在选中的代码块上右键CodeGenie > Insight Intent > 选择适合的装饰器。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/K6QRpi3XQWmPHUta2wZvSA/zh-cn_image_0000002552959328.png?HW-CC-KV=V1&HW-CC-Date=20260427T235337Z&HW-CC-Expire=86400&HW-CC-Sign=9117AF0CC62F27D988B91589C3B8CBDA3CBD84419AD1180C4A75D5E72B658E4C)
   4. 在DevEco CodeGenie对话框中对意图定义，功能，参数等进行描述。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/va5HURULTHetGDnTDgh2-Q/zh-cn_image_0000002583479329.png?HW-CC-KV=V1&HW-CC-Date=20260427T235337Z&HW-CC-Expire=86400&HW-CC-Sign=45DEB48B18AEFF9B330108BCFEC721E433F894C427C162853EDC8259EEFE83D8)
   5. 回车或者点击发送按钮，即可生成对应的装饰器内容。

      ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/AYLTWKOEShCW_reuBSUKuA/zh-cn_image_0000002552799680.png?HW-CC-KV=V1&HW-CC-Date=20260427T235337Z&HW-CC-Expire=86400&HW-CC-Sign=8BC65484DBB6B41F59552B1575AB1D5A456C0EDDF150EC63D7E03AF7E537B8BB)
   6. 将光标放置于要插入装饰器的位置，点击插入图标，即可在对应位置插入装饰器。

   插入前：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/QtQP2cFWRXuS1apXx6XzOQ/zh-cn_image_0000002583439375.png?HW-CC-KV=V1&HW-CC-Date=20260427T235337Z&HW-CC-Expire=86400&HW-CC-Sign=24545AD23D1D610C5FDB050A0A3D5760D8E79D2234C56E401A72C00CEADB1C57)

   插入后：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/xroMPHyjT56LyAtepN0e8Q/zh-cn_image_0000002552959330.png?HW-CC-KV=V1&HW-CC-Date=20260427T235337Z&HW-CC-Expire=86400&HW-CC-Sign=37559158C5597D6A6A892EC133B166CC744363F72CC6B7A2B688191536D01FD5)

   装饰器的使用约束和说明：

   * 仅限无其他依赖，可以直接拉起调用的全局函数。
   * 支持将函数参数作为意图参数进行声明，参数类型支持基本类型。
   * 装饰器所在函数不应该参与混淆，否则无法调用。
   * 仅支持在export的类上添加装饰器。
