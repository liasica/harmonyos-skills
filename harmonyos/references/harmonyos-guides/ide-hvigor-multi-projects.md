---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-multi-projects
title: 多工程构建
breadcrumb: 指南 > 构建应用 > 配置构建流程 > 多工程构建
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:56+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:3f4d93e8d547ad1c5da17d2ff87054e9c9ec4be23e63e376a2a731b47be938cd
---

为降低大型应用在多团队协作开发中的复杂度，提供多工程开发能力，提高协作开发效率。多工程开发能力支持将大型应用拆分为多个模块，每个模块对应一个单独工程。在每个工程分别编译生成HAP后，需统一打包生成一个APP，用于上架应用市场。

1. 分别在每个工程的工程级build-profile.json5配置文件中，设置multiProjects字段值为true。

   ```json5
   {
     "app": {
       "multiProjects": true,
     }
   }
   ```
2. 准备好HAP打包工具app\_packing\_tool.jar（在${DevEco Studio安装目录}/sdk/default/openharmony/toolchains/lib下）。
3. 在HAP打包工具目录下，执行命令将多个HAP进行打包，示例如下。更多关于打包工具的使用请参考[打包工具](packing-tool.md#多工程打包指令)。

   ```bash
   java -jar app_packing_tool.jar --mode multiApp --hap-list D:\project\MyApplication\1.hap,D:\project\MyApplication1\2.hap --out-path D:\project\final.app
   ```

   * hap-list：多个HAP文件路径，用逗号隔开。
   * out-path：生成的APP文件路径，如"D:\project\final.app"。
