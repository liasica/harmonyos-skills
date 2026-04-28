---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-57
title: 怎样在编译配置中设置excludes文件
breadcrumb: FAQ > DevEco Studio > 编译构建 > 怎样在编译配置中设置excludes文件
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:20+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:c95b22b0ed4b12dc5dc10aee1d27b3d5bf7105cd0c487abfb5022bbf16597861
---

在模块级build-profile.json5中如下进行配置：

```
1. "nativeLib": {
2. "debugSymbol": {
3. "strip": true,
4. "exclude": [
5. "**/3.so"
6. ]
7. }
8. },
```

[build-profile.json5](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CompilingAndBuilding/entry/build-profile.json5#L32-L39)
