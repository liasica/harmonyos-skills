---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-38
title: Native侧如何获取可操作的文件目录
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何获取可操作的文件目录
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:57+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f723fa506e660a95f16ef2828cdc519f8094a3758bcc88a3675fd87e3f26f499
---

当前native侧暂无可直接获取文件目录的接口，可以通过ArkTS侧获取相关路径信息，然后传递到native侧使用。

ArkTS侧获取路径信息代码示例：

```ts
import { common } from '@kit.AbilityKit';

const context = AppStorage.get("context") as UIContext;
let hostContext = context.getHostContext() as common.UIAbilityContext;
let filesDir = hostContext.filesDir;
```
