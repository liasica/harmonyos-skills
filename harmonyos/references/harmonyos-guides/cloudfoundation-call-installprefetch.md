---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-installprefetch
title: 调用安装预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 调用预加载 > 调用安装预加载
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:54+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:1bf6f557c1ca2925b995f36b5ff094cf4656a9df901924cf4c82487926a6cc0b
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
3. 在EntryAbility.ets文件的onCreate中调用预加载实现类[PrefetchWrapper](cloudfoundation-prefetch-implementation-class.md#prefetchwrapper)的doInstallPrefetch方法。方法内部会调用[getPrefetchResult](../harmonyos-references/cloudfoundation-cloudresprefetch.md#getprefetchresult)获取安装预加载缓存数据。

   **说明** 

   * 安装预加载缓存数据，仅允许调用一次，被调用后将被销毁。
   * 应用安装开始时，系统会拉取安装预加载云侧数据并缓存到本地。

   ```typescript
   PrefetchWrapper.getInstance().doInstallPrefetch();
   ```

   **说明** 

   调用安装预加载过程中，可参考[FAQ](cloudfoundation-faq-5.md)定位预加载问题。
