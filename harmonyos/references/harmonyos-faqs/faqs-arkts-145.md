---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-145
title: 如何在Index.ets中导出默认导出的对象
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 如何在Index.ets中导出默认导出的对象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:53+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:acdcedbd4c9cb96a0abc15f12ae322fa42e624fb2a3bc15b3c4a3f1e571960a4
---

**问题现象**

```typescript
// src/main/ets/api/AppInterfaces.ets
import { DemoService } from "../service/DemoService";
class AppInterfaces {
  demoService?: DemoService;
}
export default new AppInterfaces() as AppInterfaces;
// Index.ets
export AppInterfaces from './src/main/ets/api/AppInterfaces';
```

报错提示：Cannot find name 'AppInterfaces'. <ArkTSCheck>

**解决措施**

```ts
import { DemoService } from "../service/DemoService";
class AppInterfaces {
  demoService?: DemoService;
}
let test = new AppInterfaces()
export default test;
```
