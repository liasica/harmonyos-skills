---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-79
title: 编译命令行中如何传递参数并且在Hvigor编译阶段扩展插件中获取到
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译命令行中如何传递参数并且在Hvigor编译阶段扩展插件中获取到
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9af5a55d48b1be0fbe858c620455352b931eb1c299d2553fd4c31d75ca6a0531
---

使用hvigor命令：

```powershell
 > hvigorw -s -p key1=value2222
```

获取自定义参数代码：

```typescript
// hvigorfile.ts
import { harTasks } from '@ohos/hvigor-ohos-plugin';
import { hvigor } from '@ohos/hvigor';

export default {
    system: harTasks,  /* Built-in plugin of Hvigor. It cannot be modified. */
    plugins:[]         /* Custom plugin to extend the functionality of Hvigor. */
}
console.log('value===', hvigor.getParameter().getExtParam('key1'));
```
