---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-chain-install-prefetch
title: 调用跳链安装预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 调用预加载 > 调用跳链安装预加载
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:54+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:8b40029ba2bdde64d55d055d96a6f003ff7a8472e1fe0b75c202bef764b78baf
---

1. 导入相关模块。

   ```typescript
   import { GlobalContext } from '../common/GlobalContext';
   import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
   import { PrefetchWrapper } from '../PrefetchUtil/PrefetchWrapper';
   ```
2. 初始化全局上下文。

   ```typescript
   // 初始化全局上下文
   GlobalContext.initContext(this.context);
   ```
3. 在EntryAbility.ets文件的onCreate中调用预加载实现类[PrefetchWrapper](cloudfoundation-prefetch-implementation-class.md#prefetchwrapper)的doLinkPrefetch方法。方法内部会先调用[popDeferredLink](../harmonyos-references/applinking-deferredlink-api.md#popdeferredlink)接口获取延迟链接，再调用[getPrefetchResult](../harmonyos-references/cloudfoundation-cloudresprefetch.md#getprefetchresult)获取跳链安装预加载缓存数据。

   **说明** 

   跳链安装预加载缓存的是应用详情页数据，仅允许调用一次，被调用后将被销毁。

   ```typescript
   PrefetchWrapper.getInstance().doLinkPrefetch();
   ```
