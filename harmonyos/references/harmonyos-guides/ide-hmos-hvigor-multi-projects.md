---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hmos-hvigor-multi-projects
title: 多工程构建
breadcrumb: 指南 > DevEco Studio（鸿蒙电脑版） > 构建应用 > 配置构建流程 > 多工程构建
category: harmonyos-guides
scraped_at: 2026-10-09T08:15:34+08:00
doc_updated_at: 2026-10-08
content_hash: sha256:854888e70f2f46e1274b2e715c9122a301cf4de10210df2721a99fffb3916d38
---

为降低大型应用在多团队协作开发中的复杂度，提供多工程开发能力，提高协作开发效率。多工程开发能力支持将大型应用拆分为多个模块，每个模块对应一个单独工程。在每个工程分别编译生成HAP后，需统一打包生成一个APP，用于上架应用市场。

1. 分别在每个工程的build-profile.json5配置文件中，设置multiProjects字段值为true。

   ```screen
   {
     "app": {
       "multiProjects": true,
     }
   }
   ```
2. 准备好HAP打包工具ohos\_packing\_tool（在/data/service/hnp/hmos-clt.org/hmos-clt.x.x.x/sdk/default/openharmony/toolchains/lib下，x.x.x是版本号）。
3. 在HAP打包工具目录下，执行命令将多个HAP进行打包，示例如下。

   ```screen
   ohos_packing_tool pack --mode multiApp --hap-list 1.hap,2.hap --out-path final.app
   ```

   * hap-list：多个HAP文件路径，用逗号隔开。
   * out-path：生成的APP文件路径，如"final.app"。
