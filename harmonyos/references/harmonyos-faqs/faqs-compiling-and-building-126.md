---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-126
title: 如何解决编译报错“Indexed access is not supported for fields(arkts-no-props-by-index)”的问题
breadcrumb: FAQ > DevEco Studio > 编译构建 > 如何解决编译报错“Indexed access is not supported for fields(arkts-no-props-by-index)”的问题
category: harmonyos-faqs
scraped_at: 2026-04-29T14:20:50+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:2c6fb3c8bd3d3e61d54787a9e9cd438f8a7508744e6c0e6d36972c9baf7efb9e
---

**问题现象**

动态调用类或接口的字段会导致编译报错：Indexed access is not supported for fields (arkts-no-props-by-index)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/Xee2mRXNTm-O9V0td2eJUA/zh-cn_image_0000002229604089.png)

**解决方案**

修改代码：

```
1. getValue(breakpoint: string): T {
2. return Reflect.get(this.options, breakpoint) as T;
3. }
```

[BreakPointType.ets](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/CompilingAndBuilding/entry/src/main/ets/commpent/BreakPointType.ets#L19-L21)
