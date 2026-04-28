---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-compiling-and-building-3
title: 编译告警“The re-export name 'xx' need to be marked as type”
breadcrumb: FAQ > DevEco Studio > 编译构建 > 编译告警“The re-export name 'xx' need to be marked as type”
category: harmonyos-faqs
scraped_at: 2026-04-28T08:29:08+08:00
doc_updated_at: 2026-03-10
content_hash: sha256:807759f9273a60317982ae78df450c9da6a3ee587cb5dbdc560818620d0c359e
---

**问题现象**

升级DevEco Studio至3.1 Beta2 Release版本后，API 9的Stage工程编译时出现告警，提示“The re-export name 'T' need to be marked as type, please use 'export type'”。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/KczJw0zlRrWyW8NqqYItIw/zh-cn_image_0000002229604241.png?HW-CC-KV=V1&HW-CC-Date=20260428T002907Z&HW-CC-Expire=86400&HW-CC-Sign=D4FBCE7D4362A85E1D316971D209D86D1CCD315CA17966C2ABA2D13446F6794B)

**解决措施**

DevEco Studio 3.1 Beta2 Release版本默认启用模块化编译。如果应用中存在re-export语法，将会触发告警。反例如下：

```
1. // index.ets
2. import {test} from "./test"
3. export {test}
4. let b : test = {a : 'index'}

6. // test.ets
7. export interface test {
8. a: string
9. }
10. let obj : test = {a : 'string'}
```

由于ets/ts模块声明的类型符号在编译为js模块时会被消除，而import语句本身会被保留。如果未使用`type`显式声明类型引用，会导致运行时找不到对应的类型符号。

如编译构建期间提示上述告警信息，请根据提示信息进行以下修改：添加type显式声明类型符号的引用，以使编译转换后的JS模块能够消除类型符号的引用。

```
1. import type {test} from "./test"  //Here, add a type declaration
2. export {test}
3. let b : test = {a : 'index'}
```

[Index.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/src/main/ets/pages/Index.ets#L20-L22)

```
1. // test.ets
2. export interface test {
3. a: string
4. }
5. let obj : test = {a : 'string'}
```

[test.ets](https://gitcode.com/harmonyos_samples/faqsnippets/blob/master/CompilingAndBuilding/entry/src/main/ets/pages/test.ets#L29-L33)
