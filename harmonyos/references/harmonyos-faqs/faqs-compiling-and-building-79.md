---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-79
title: 编译命令行中如何传递参数并且在Hvigor编译阶段扩展插件中获取到
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译命令行中如何传递参数并且在Hvigor编译阶段扩展插件中获取到
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:24+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:ed6c8efd571900faf9b125ceaa4028e59df7441cb5913dfdf0cef2fd412bf806
---

使用hvigor命令：

```
1. > hvigorw -s -p key1=value2222
```

获取自定义参数代码：

```
1. // hvigorfile.ts
2. import { harTasks } from '@ohos/hvigor-ohos-plugin';
3. import { hvigor } from '@ohos/hvigor';

5. export default {
6. system: harTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
7. plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
8. }
9. console.log('value===', hvigor.getParameter().getExtParam('key1'));
```

[hvigorfile.ts](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/library1/hvigorfile.ts#L3-L11)
