---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-64
title: 如何写har包的编译脚本
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何写har包的编译脚本
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:21+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:f607b76ada88f0329f7038903a9800c869e942b65a1b70945597928ee14d967a
---

在har包目录下的hvigorfile.ts文件中编写代码如下：

```
1. import { harTasks } from '@ohos/hvigor-ohos-plugin';

4. function harTask(): HvigorPlugin {
5. return {
6. pluginId: 'harTask',
7. apply(node: HvigorNode) {
8. console.log('hello harTasks!');
9. }
10. }
11. }

14. export default {
15. system: harTasks,
16. plugins: [harTask()]
17. }
```

[hvigorfile.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CompilingAndBuilding/library/hvigorfile.ts#L3-L20)
