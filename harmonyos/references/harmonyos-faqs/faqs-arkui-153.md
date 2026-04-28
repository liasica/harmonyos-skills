---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-153
title: Image或者ImageSpan传入一个string类型的路径时无法加载图片
breadcrumb: FAQ > 应用框架开发 > UI框架 > 方舟UI框架（ArkUI） > Image或者ImageSpan传入一个string类型的路径时无法加载图片
category: harmonyos-faqs
scraped_at: 2026-04-28T08:25:41+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:557162fa8cfdcf708108e7e161cb492c68457161d65e9c4461a850f62f0dbd58
---

目前规格上只支持常量，需要把string提取出来用$r( )包裹。例如：

```
1. localImageName = $r( 'app.media.icon' )
```

[ImageStrPath.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/ArkUI/entry/src/main/ets/pages/ImageStrPath.ets#L6-L6)
