---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/compiling-and-building-faq-0002
title: HAR包编译脚本编写常见问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 常见问题 > HAR包编译脚本编写常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:12:39+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:a7a756dec723f0d0a568555f146b7c9d22f231022097c13c25f782bc05b3ed6f
---

**Q：如何写har包的编译脚本？**

**A**：在har包目录下的hvigorfile.ts文件中编写代码如下：

```ts
import { harTasks } from '@ohos/hvigor-ohos-plugin';

function harTask(): HvigorPlugin {
    return {
        pluginId: 'harTask',
        apply(node: HvigorNode) {
            console.log('hello harTasks!');
        }
    }
}

export default {
    system: harTasks,
    plugins: [harTask()]
}
```
