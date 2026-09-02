---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-58
title: 如何在编译过程中添加自定义任务
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何在编译过程中添加自定义任务
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:94228d104f55892574f56a73d370e1bbb098d18d1f764884def670193caa5784
---

1. 打开模块级的hvigorfile.ts文件。
2. 使用 pluginContext的registerTask方法注册自定义任务，开发者在run方法内编写自定义任务。

   ```json
   import { hapTasks } from '@ohos/hvigor-ohos-plugin';
   import { getNode, HvigorNode, HvigorTask } from '@ohos/hvigor';

   const node = getNode(__filename);
   node.registerTask({
       name: 'customTask',
       run() {
           console.log('this is Task');
       }});
   ```
3. 在终端中输入以下代码执行任务。

   ```powershell
   ./hvigorw customTask
   ```

**参考链接**

[开发hvigor任务](../harmonyos-guides/ide-hvigor-task.md)
