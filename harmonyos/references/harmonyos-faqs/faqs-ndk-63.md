---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ndk-63
title: 如何通过多个xxx.d.ts文件导出Native侧接口
breadcrumb: FAQ > 应用框架开发 > NDK开发 > NDK开发 > 如何通过多个xxx.d.ts文件导出Native侧接口
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:57+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:9f03f092b9946fd4f054f02c7f7dff588574dbd9ace0e4197f6d5c7bc8777634
---

**问题现象**

由于底层C++库规模较大，向外暴露的接口数量较多，建议将其拆分成多个.d.ts文件以便归类。

**解决措施**

在oh-package.json5中的types字段只能指定一个出口。如果需要封装多个.d.ts文件中的接口，可以使用重导出的方式。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/Bf_pSfyJQgCL0vstEgfbyw/zh-cn_image_0000002654835215.png "点击放大")

实现方式：

在index1.d.ts文件中声明Native侧导出接口，然后通过index.d.ts文件重导出到ArkTS侧使用。

在index1.d.ts文件中导出接口。

```ts
export const sub: (a: number, b: number) => number;
```

在index.d.ts文件中重导出这些接口。

```ts
export {sub} from './index1'
export const add: (a: number, b: number) => number;
```
