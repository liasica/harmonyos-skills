---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-58
title: 如何在编译过程中添加自定义任务
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何在编译过程中添加自定义任务
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c7da1e809c89235aff1592932598da37d95b88e3a33f465ce312661856641128
---

1. 打开模块级的hvigorfile.ts文件。
2. 使用 pluginContext的registerTask方法注册自定义任务，开发者在run方法内编写自定义任务。

   ```
   1. import { hapTasks } from '@ohos/hvigor-ohos-plugin';
   2. import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

   5. const node = getNode(__filename);
   6. node.registerTask({
   7. name: 'customTask',
   8. run() {
   9. console.log('this is Task');
   10. }});
   ```

   [hvigorfile.ts](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/hvigorfile.ts#L3-L12)
3. 在终端中输入以下代码执行任务。

   ```
   1. ./hvigorw customTask
   ```

**参考链接**

[开发hvigor任务](../harmonyos-guides/ide-hvigor-task.md)
