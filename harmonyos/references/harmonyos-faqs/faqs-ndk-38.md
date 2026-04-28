---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-38
title: Native侧如何获取可操作的文件目录
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > Native侧如何获取可操作的文件目录
category: harmonyos-faqs
scraped_at: 2026-04-28T08:24:36+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:77cd4dc7ef1d1f38e03697eb8eb878e6d923e09421fa54e985dc5bb0b966f827
---

当前native侧暂无可直接获取文件目录的接口，可以通过ArkTS侧获取相关路径信息，然后传递到native侧使用。

ArkTS侧获取路径信息代码示例：

```
1. import { common } from '@kit.AbilityKit';

3. const context = AppStorage.get("context") as UIContext;
4. let hostContext = context.getHostContext() as common.UIAbilityContext;
5. let filesDir = hostContext.filesDir;
```

[NativeSideOperableFileDirectory.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/entry/src/main/ets/pages/NativeSideOperableFileDirectory.ets#L21-L25)
