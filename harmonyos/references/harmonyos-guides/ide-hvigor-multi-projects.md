---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-multi-projects
title: 多工程构建
breadcrumb: 指南 > 构建应用 > 配置构建流程 > 多工程构建
category: harmonyos-guides
scraped_at: 2026-04-28T07:57:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:45560af072795681b5ca6d5467ce0168087feb0eec7280f78bd1b9e532e1667d
---

为降低大型应用多个团队协作开发的复杂度，提供多工程开发模式，提高协作开发效率。多工程开发能力支持将大型应用拆分为多个模块，每个模块对应一个单独工程。在每个工程分别编译生成HAP后，需统一打包生成一个APP，用于上架应用市场。

1. 分别在每个工程的工程级build-profile.json5配置文件中，设置multiProjects字段值为true。

   ```
   1. {
   2. "app": {
   3. "multiProjects": true,
   4. }
   5. }
   ```
2. 准备好HAP打包工具app\_packing\_tool.jar（在 $DevEco Studio安装目录/sdk/default/openharmony/toolchains/lib下）。
3. 在HAP打包工具目录下，执行命令将多个HAP进行打包，示例如下。更多关于打包工具的使用请参考[打包工具](packing-tool.md#多工程打包指令)。

   ```
   1. java -jar app_packing_tool.jar --mode multiApp --hap-list D:\project\MyApplication\1.hap,D:\project\MyApplication1\2.hap --out-path D:\project\final.app
   ```

   * hap-list：多个HAP文件路径，用逗号隔开。
   * out-path：生成的APP文件路径，如"D:\project\final.app"。
