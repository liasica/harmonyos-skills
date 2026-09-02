---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1449
title: Navigation跨包跳转报错hap path error
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Navigation跨包跳转报错hap path error
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:10+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:0f5db9b73619104c2f58ff0e05c6b536fe0478c24bc2a660d7dba455871911f6
---

## 问题现象

在进行跨模块跳转时，发生报错hap path error，具体报错内容如下：

```screen
11-25 10:48:06.833   1394-1394     C03f00/ArkCompiler              com.examp...20596468  F     [default] [LoadJSPandaFile:113] resolveBufferCallback get hsp buffer failed, hsp path:/data/storage/el1/bundle/feature/ets/modules.abc, errorMsg:hap path error: /data/storage/el1/bundle/feature.hsp
```

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件适用于模块内和跨模块的路由切换，通过组件级路由能力实现更加自然流畅的转场体验。
* [跨包路由](../harmonyos-guides/arkts-navigation-cross-package.md)：动态路由设计的初衷旨在解决多个模块（HAR/HSP）能够复用相同的业务逻辑，实现各业务模块间的解耦，同时支持路由功能的扩展与整合。

## 问题定位

1. 查看路由表配置，路由表配置正确。
2. 找到跳转的页面，查看是否使用NavDestination组件，发现没有使用NavDestination组件。
3. 根据报错提示是HAP模块，查看对应模块中module.json5中的type类型为feature，发现该模块是HAP模块。

   ```screen
   // module.json5文件
   {
      "module": {
       "name": "feature",
       "type": "feature"  // type类型为feature，此模块为HAP模块
     }
   }
   ```

## 分析结论

查看对应模块中module.json5中的type为feature类型，该模块是HAP模块，而跨模块仅跳转支持HAR/HSP模块，不支持HAP模块。此外，目标页面未使用NavDestination组件，即使配置都正确页面也会显示空白，需要使用NavDestination组件包裹。

## 修改建议

1. 路由表配置时，可以根据[系统路由表](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)步骤逐步进行来配置。
2. 路由表中的页面，需要使用NavDestination组件才能展示页面。
3. HAR/HSP模块才可以跳转，可以通过module.json5文件查看type类型是否为har或者shared。
