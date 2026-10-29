---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0033
title: 构建任务与文件冲突报错
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > 构建任务与文件冲突报错
category: harmonyos-faqs
scraped_at: 2026-10-30T07:59:14+08:00
doc_updated_at: 2026-10-29
content_hash: sha256:5ecaf47db7678853b5992ac4479527569233c4d9f0275c89634c757b54699007
---

**Q：构建报错"Cannot read properties of undefined(reading 'XXX')"时如何排查和解决？**

**A**：请先根据XXX的值从以下场景排查，没解决问题再参考最终方案。

* 场景一：

  问题现象：编译构建时，出现报错"Cannot read properties of undefined(reading 'setEnabled')"。

  问题确认：

  1. hvigorfile.ts里有如下代码：

     ```ts
     import { hvigor, getHvigorNode } from "@ohos/hvigor"
     import { hapTasks} from '@ohos/hvigor-ohos-plugin';
     // Problem Code
     getHvigorNode(__filename).getTaskByName('XXX').setEnabled(false);
     export default {
         system: hapTasks, /* Built-in plugin of Hvigor. It cannot be modified. */
         plugins:
     ```
  2. 确保getTaskByName的使用位置是在Hvigor的配置阶段及之后的生命周期里，包括beforeNodeEvaluate、afterNodeEvaluate、nodesEvaluated、taskGraphResolved、buildFinished。

  参考链接：[生命周期及hook点](../harmonyos-guides/ide-hvigor-life-cycle.md#section746253616316)。
* 场景二：

  问题现象：编译构建时，出现报错"Cannot read properties of undefined(reading 'isSO')"。

  解决措施：升级到DevEco Studio 5.1.0.840及以上的版本。
* 场景三：

  问题现象：编译构建时，出现报错"Cannot read properties of undefined(reading 'getPluginId')"。

  解决措施：

  1. 确保hvigorfile.ts里export default的对象中的字段system的值是appTasks/hapTasks/hspTasks/harTasks之一。

     ```ts
     import { harTasks } from '@ohos/hvigor-ohos-plugin';

     export default {
         system: harTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
         plugins:
     ```
  2. 确认DevEco Studio是否有使用安全加固等三方插件。如果有，可以先禁用三方插件，看是否会复现问题，还能复现就参考下面的最终方案。
* 场景四：

  问题现象：执行hap覆盖率测试时，出现报错："Error Message: Cannot read properties of undefined (reading 'module')"。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/407-MTJyQ22SfFb8xDlFLA/zh-cn_image_0000002774299982.png "点击放大")

  可能原因：工程下hap和hsp模块的build-profile.json5中targets包含ohosTest，但是ohosTest目录不存在，导致构建过程获取模块的ohosTest信息失败。

  解决措施：检查工程所有模块，如果build-profile.json5下targets里配置了ohosTest，模块内确保有src/ohosTest目录及目录对应结构；如不需要ohosTest，则在targets内删除ohosTest。

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/n3Gv6S9aQ7CU-VMgeQVqZQ/zh-cn_image_0000002774459966.png "点击放大")

最终方案：

如果以上场景都不符合，打开堆栈后，根据堆栈信息排查代码。

堆栈打开方法：工程根目录hvigor/hvigor-config.json5文件中配置如下内容。

```json
{
  "debugging": {
    "stacktrace": true
    /* Disable stacktrace compilation. Value: [ true | false ]. Default: false */
  },
}
```

优先排查hvigorconfig.ts文件和hvigorfile.ts文件，其他代码次之。

如果上述文件中并未排查出问题，请及时提单反馈。

请按照如下步骤进行操作：[提单链接](https://developer.huawei.com/consumer/cn/support/)，在线提单 -> 问题分类选择"HarmonyOS NEXT / 开发工具 / DevEco Studio"。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/C07biiJ0SyaHj6nhVZTOTA/zh-cn_image_0000002803779695.png "点击放大")

**Q：命令行手动执行构建命令时，如果构建失败并提示"ERROR: Task xxx was not found in the project xxx"，应该如何处理？**

**A**：请检查以下内容：

* 确认任务名称是否正确。
* 确认项目中是否包含该任务。
* 确认项目路径是否正确。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/mX7YPlkLQLiq575peNm6vg/zh-cn_image_0000002803619777.png "点击放大")

问题确认：

1. 执行hvigor tasks命令，查看该命令是否存在。
2. 查看对应工程中module.json5文件中"type"字段是否为命令执行模块。比如图中执行assembleHar命令，是对工程中的har模块进行打包，若module.json5文件中的"type"字段不是"har"类型，则会出现上述错误提示。

解决措施：

1. 执行正确命令。
2. 查看工程中 module.json5 文件的"type"字段，执行相应命令。

**Q：编译构建时，出现错误信息"Duplicated files found in module xxx. This may cause unexpected errors at runtime"。**

**A**：构建时存在不同版本的同名SO文件会导致问题。例如，将har模块产物中的SO文件拷贝到entry模块的libs目录下，此时har模块和entry模块中都有一个名为libhar.so的文件。如果再配置entry依赖har，构建entry时就会出现错误。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/-PFcxDnMSaWqyah44VALXg/zh-cn_image_0000002774299996.png "点击放大")

使用select、pickFirsts、pickLasts等配置项选择要使用的.so文件。select提供对 native 产物的精准选择，优先级高于excludes、pickFirsts等配置项。pickFirsts和pickLasts按照.so文件的优先级顺序打包，优先级顺序基于依赖收集的顺序，越晚被收集的优先级越高。

具体可参考：[模块级build-profile.json5文件](../harmonyos-guides/ide-hvigor-build-profile.md)。

在entry/build-profile.json5中，配置select选中har模块中的so文件，package选中包名为har的模块，include选中libhar.so文件。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/BxzPlPfvS2W0x1F-xq8kew/zh-cn_image_0000002774300002.png "点击放大")
