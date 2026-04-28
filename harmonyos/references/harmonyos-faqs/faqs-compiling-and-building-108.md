---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-108
title: 构建报错"Cannot read properties of undefined(reading 'XXX')"
breadcrumb: FAQ > DevEco Studio > 编译构建 > 构建报错"Cannot read properties of undefined(reading 'XXX')"
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:30+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:353e9f04b74c6370f28901d9928392d864f28c94c2c973457a12fba4d986553e
---

请先根据XXX的值从以下场景排查，没解决问题再参考最终方案。

* **场景一：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'setEnabled')”。

  **问题确认**

  hvigorfile.ts里有如下代码：

  ```
  1. import { hvigor, getHvigorNode } from "@ohos/hvigor"
  2. import { hapTasks} from '@ohos/hvigor-ohos-plugin';
  3. // Problem Code
  4. getHvigorNode(__filename).getTaskByName('XXX').setEnabled(false)；
  5. export default {
  6. system: hapTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
  7. plugins: []         /* Custom plugin to extend the functionality of Hvigor. */
  8. }
  ```

  **解决措施**

  1. 确保XXX是当前的HvigorNode里存在的任务。

     假设是entry模块的hvigorfile.ts中的代码导致的问题 ，XXX的有效值就是下图中的“default@SignHap”、“default@CollectDebugSymbol”、“assembleHap”等值。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/m6sJrRo5Rq218RfAESIcwA/zh-cn_image_0000002289418625.png?HW-CC-KV=V1&HW-CC-Date=20260428T002929Z&HW-CC-Expire=86400&HW-CC-Sign=C231DAE0040006F6F12D6850ADA5B0C47F0534EF7B722BE71BC59744417B7BFA)
  2. 确保getTaskByName的使用位置是在Hvigor的配置阶段及之后的生命周期里，包括beforeNodeEvaluate、afterNodeEvaluate、nodesEvaluated、taskGraphResolved、buildFinished。

  **参考链接**

  [生命周期及hook点](../harmonyos-guides/ide-hvigor-life-cycle.md#section746253616316)
* **场景二：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'isSO')”。

  **解决措施**

  升级到DevEco Studio 5.1.0.840及以上的版本。
* **场景三：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'getPluginId')”**。**

  **解决措施**

  确保hvigorfile.ts里export default的对象中的字段system的值是appTasks/hapTasks/hspTasks/harTasks之一。

  ```
  1. import { harTasks } from '@ohos/hvigor-ohos-plugin';

  3. export default {
  4. system: harTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
  5. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
  6. }
  ```

  [hvigorfile.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CompilingAndBuilding/library2/hvigorfile.ts#L3-L8)
* **场景四：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'getNeedExecTargetServiceList')”**。**

  **解决措施**

  确保模块下的module.json5的type字段的值和hvigorfile.ts中export default的对象的system字段符合以下对应关系：

  **表1**

  | module.json5的type字段 | hvigorfile.ts中export default的对象的system字段 |
  | --- | --- |
  | entry | hapTasks |
  | feature | hapTasks |
  | shared | hspTasks |
  | har | harTasks |
* **场景五：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'app')”。

  **解决措施**

  确保工程目录下AppScope/app.json5文件存在。
* **场景六：**

  **问题现象**

  Linux环境下，执行单元测试，出现报错“Cannot read properties of undefined(reading 'toString')”。

  **解决措施**

  Linux环境暂不支持单元测试。
* **场景七：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'kind')”。

  **解决措施**

  检查ArkTS代码是否有如下写法：

  ```
  1. // Incorrect writing: empty array
  2. class w {
  3. public a: [][] = []
  4. test() {
  5. console.log("1", this.a[0])
  6. }
  7. }
  ```

  ```
  1. // Correct writing
  2. class w {
  3. public a: string[][] = []
  4. test() {
  5. console.log("1", this.a[0])
  6. }
  7. }
  ```

  [w.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/library3/src/main/ets/components/w.ets#L3-L9)
* **场景八：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'getltem')”。

  **解决措施**

  在加载webview的controller中加入.domStorageAccess(true)。
* **场景九：**

  **问题现象**

  编译构建时，出现报错“Cannot read properties of undefined(reading 'clear')”。

  **问题确认**

  在工程根目录hvigor/hvigor-config.json5文件中配置如下内容打开堆栈。

  ```
  1. {
  2. "debugging": {
  3. "stacktrace": true
  4. /* Disable stacktrace compilation. Value: [ true | false ]. Default: false */
  5. },
  6. }
  ```

  [hvigor-config\_xx.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/hvigor/hvigor-config_xx.json5#L3-L8)

  确认堆栈内容是否如下。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/RBOT8QvTR02PjXDFaNSaAw/zh-cn_image_0000002289305561.png?HW-CC-KV=V1&HW-CC-Date=20260428T002929Z&HW-CC-Expire=86400&HW-CC-Sign=EB703379029C10D834DB0500DFFB5AF359EEE7FCD2F9E1C31F4A6FD4E57A51C1)

  **解决措施**

  确认DevEco Studio是否有使用安全加固等三方插件。如果有，可以先禁用三方插件，看是否会复现问题，还能复现就参考下面的最终方案。
* **场景十**

  **问题现象**

  执行hap覆盖率测试时，出现报错：“Error Message: Cannot read properties of undefined (reading 'module')”。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/aXa4N4eNRbWIBML7RttzDA/zh-cn_image_0000002523012117.png?HW-CC-KV=V1&HW-CC-Date=20260428T002929Z&HW-CC-Expire=86400&HW-CC-Sign=0E5E1B1DC1C472799FC214CF87A7C48A0D8EC8FA0F6035AAB742657C9DAA9E4F)

  **可能原因**

  工程下hap和hsp模块的build-profile.json5中targets包含ohosTest，但是ohosTest目录不存在，导致构建过程获取模块的ohosTest信息失败。

  **解决措施**

  检查工程所有模块，如果build-profile.json5下targets里配置了ohosTest，模块内确保有src/ohosTest目录及目录对应结构；如不需要ohosTest，则在targets内删除ohosTest。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/KGWwij54T1u98UUtnW6xhA/zh-cn_image_0000002490972342.png?HW-CC-KV=V1&HW-CC-Date=20260428T002929Z&HW-CC-Expire=86400&HW-CC-Sign=39C99399A38069246D86A954E288EFE5622B151B1EE6B0BB3DBB9D6C9F934F0F)
* **最终方案：**

  如果以上场景都不符合，打开堆栈后，根据堆栈信息排查代码。

  堆栈打开方法：工程根目录hvigor/hvigor-config.json5文件中配置如下内容。

  ```
  1. {
  2. "debugging": {
  3. "stacktrace": true
  4. /* Disable stacktrace compilation. Value: [ true | false ]. Default: false */
  5. },
  6. }
  ```

  [hvigor-config\_xx.json5](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/hvigor/hvigor-config_xx.json5#L3-L8)

  优先排查hvigorconfig.ts文件和hvigorfile.ts文件，其他代码次之。

  如果上述文件中并未排查出问题，请及时向我们提单反馈。

  请按照如下步骤进行操作：[提单链接](https://developer.huawei.com/consumer/cn/support/)，在线提单 -> 问题分类选择"HarmonyOS NEXT / 开发工具 / DevEco Studio"。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/1YKcbaGQSsKjAQ53S_C6mw/zh-cn_image_0000002254825302.png?HW-CC-KV=V1&HW-CC-Date=20260428T002929Z&HW-CC-Expire=86400&HW-CC-Sign=F1F380E122D667B2AD4DD22A819A3B3C74049E8F83DEBABAE987B8A94072D548)
