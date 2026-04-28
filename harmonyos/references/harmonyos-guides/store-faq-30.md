---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/store-faq-30
title: 按需加载场景中，用户在加载指定模块后是否可以卸载，然后重新发起请求？
breadcrumb: 指南 > 应用服务 > AppGallery Kit（应用市场服务） > AppGallery Kit常见问题 > 按需加载场景中，用户在加载指定模块后是否可以卸载，然后重新发起请求？
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:28+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:8fefc6ec1b2ba67911e4b5c6d8221e40bf47735229b3f80eba867dcbe98bac85
---

可以卸载指定模块后重新调用[fetchModules](../harmonyos-references/store-moduleinstallmanager.md#moduleinstallmanagerfetchmodules)接口发起按需加载请求。

使用hdc指令卸载指定应用的指定模块后重新发起请求，卸载命令请参考：hdc shell bm uninstall -n com.xxxx.instantdownloaddemo -m modulelibName。
