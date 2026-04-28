---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/hsp-to-har
title: HSP转HAR指导
breadcrumb: 指南 > 基础入门 > 开发基础知识 > 典型场景的开发指导 > HSP转HAR指导
category: harmonyos-guides
scraped_at: 2026-04-28T07:37:32+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:fc02b14dc8f85e630048fbb4ee4210bf24e2396b991c86828075d7ee19db5777
---

HSP对bundleName和签名有一致性要求，在调试阶段需要先安装HSP包，这导致多模块集成开发场景下容易出现多种集成问题。在此场景下，建议使用HAR包来提供所需功能。本文通过配置项的变更将HSP工程变成HAR工程。

说明

阅读本文前，请开发者完成[HSP](in-app-hsp.md)、[HAR](har-package.md)、[module.json5](module-configuration-file.md)、[hvigorfile.ts](ide-hvigor-config-ohos-guide.md)、[oh-package.json5](ide-oh-package-json5.md)、[build-profile.json5](ide-hvigor-build-profile-app.md)学习。

部分组件和模块在HAP、HSP、HAR中集成使用时存在差异，例如[加载HAR中Worker线程文件相比HSP存在单独的使用约束](worker-introduction.md#文件路径注意事项)，因此按照如下步骤完成HSP转HAR后，请关注对应组件和模块介绍并进行适配。

## HSP转HAR的操作步骤

1. 修改HSP模块下的module.json5文件，将type字段值改为har，删除deliveryWithInstall和pages字段。

   ```
   1. {
   2. "module": {
   3. "name": "har",
   4. "type": "har",
   5. "deviceTypes": [
   6. "tablet",
   7. "2in1"
   8. ]
   9. }
   10. }
   ```

   [module.json5](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HspToHar/library/src/main/module.json5#L16-L27)
2. 在resource\base\profile文件夹下，删除main\_pages.json文件。
3. 修改HSP模块的hvigorfile.ts文件，将内容替换为以下内容。

   ```
   1. // MyApplication\library\hvigorfile.ts
   2. import { harTasks } from '@ohos/hvigor-ohos-plugin';

   4. export default {
   5. system: harTasks,  // 编译修改成HAR的任务
   6. plugins:[]
   7. }
   ```

   [hvigorfile.ts](https://gitcode.com/HarmonyOS_Samples/guide-snippets/blob/HarmonyOS-feature-20260112/bmsSample/HspToHar/library/hvigorfile.ts#L16-L24)
4. 修改HSP模块的oh-package.json5文件，删除packageType配置。
5. 修改项目级的配置文件 build-profile.json5，在 modules 模块下找到 HSP 的配置信息，删除 HSP 配置下的 targets。
