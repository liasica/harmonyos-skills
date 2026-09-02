---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-64
title: 如何写har包的编译脚本
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何写har包的编译脚本
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:54+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:6dfef6e8f1e007f9ca59c886ffe15cd1b35401a8d2e95dd1f18381c7b9eadd09
---

在har包目录下的hvigorfile.ts文件中编写代码如下：

```typescript
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
