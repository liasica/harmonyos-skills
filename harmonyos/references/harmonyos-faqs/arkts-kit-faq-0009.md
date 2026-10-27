---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkts-kit-faq-0009
title: ArkTS语言概念与关联关系常见问题
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 常见问题 > ArkTS语言概念与关联关系常见问题
category: harmonyos-faqs
scraped_at: 2026-10-28T07:46:51+08:00
doc_updated_at: 2026-10-27
content_hash: sha256:90289d53f7af1e926e6243f70970114e82a687f5dab9db590bdc69809db420ab
---

**Q：ArkTS文件和TS文件的区别是什么？**

**A**：ArkTS基于TS语法，兼容TS的大部分特性。ArkTS扩展了声明式UI能力，使开发者能够以更简洁、自然的方式开发高性能应用。推荐用ArkTS开发UI，用TS开发业务逻辑。

参考链接：[学习ArkTS语言](../harmonyos-guides/learning-arkts.md)。

**Q：ArkTS语言与ArkUI框架、HarmonyOS SDK/API的关系是什么？**

**A**：

* ArkTS和ArkUI的架构关系：

  在HarmonyOS应用开发生态中，ArkTS与ArkUI构成了基础编程语言与上层UI框架的协同体系：

  a.ArkTS作为HarmonyOS官方应用开发语言，提供静态类型系统、现代化语法结构及核心编程范式，主要负责业务逻辑实现与数据处理。

  b.ArkUI是基于ArkTS语言特性构建的声明式UI开发框架，专注于界面描述、组件化构建及渲染优化，通过@State/@Prop等响应式装饰器实现UI与数据的自动同步。

  ArkTS与ArkUI二者定位不同，是语言底座和上层框架的关系，ArkTS为ArkUI提供类型安全保障和高效运行时支持，ArkUI则通过DSL扩展提升UI开发效率，共同构建完整的应用开发解决方案。
* ArkTS语言和HarmonyOS SDK/API的架构关系：

  在HarmonyOS系统架构中，ArkTS作为核心开发语言，其运行时环境与工具链通常归属开发支持层；ArkUI等上层框架属于应用框架层，SDK则通过系统服务层提供的能力封装形成开发接口；ArkTS语言可以通过import语法加载并调用相应系统能力，让开发者更高效地开发HarmonyOS应用。
* HarmonyOS架构的ArkTS、ArkUI及HarmonyOS SDK框架层级：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/KXFtuSqPQCOcPKG08xC72Q/zh-cn_image_0000002802119545.png "点击放大")
