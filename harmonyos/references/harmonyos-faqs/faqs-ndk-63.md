---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-63
title: 如何通过多个xxx.d.ts文件导出Native侧接口
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何通过多个xxx.d.ts文件导出Native侧接口
category: harmonyos-faqs
scraped_at: 2026-04-29T14:15:58+08:00
doc_updated_at: 2026-03-17
content_hash: sha256:7dad007deceb160c96e25a42fba629d48aaf50d1d401197cc9ca810f1871e9a3
---

**问题现象**

由于底层C++库规模较大，向外暴露的接口数量较多，建议将其拆分成多个.d.ts文件以便归类。

**解决措施**

在oh-package.json5中的types字段只能指定一个出口。如果需要封装多个.d.ts文件中的接口，可以使用重导出的方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/_39YHD1pTQWXM9oQi2ACaA/zh-cn_image_0000002194318472.png "点击放大")

实现方式：

在index1.d.ts文件中声明Native侧导出接口，然后通过index.d.ts文件重导出到ArkTS侧使用。

在index1.d.ts文件中导出接口。

```
1. export const sub: (a: number, b: number) => number;
```

[index1.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/Modulea/src/main/cpp/types/libmodulea/index1.d.ts#L5-L5)

在index.d.ts文件中重导出这些接口。

```
1. export {sub} from './index1'
2. export const add: (a: number, b: number) => number;
```

[Index.d.ts](https://gitcode.com/HarmonyOS_Samples/faqsnippets/blob/master/Ndk/ndk1/Modulea/src/main/cpp/types/libmodulea/Index.d.ts#L5-L6)
