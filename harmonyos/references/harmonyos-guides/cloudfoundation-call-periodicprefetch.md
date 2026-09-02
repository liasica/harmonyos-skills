---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-periodicprefetch
title: 调用周期性预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 调用预加载 > 调用周期性预加载
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:54+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:63c34386879c9ea03f301fa10f651bbcd5406c03a9bb22d870df21820dfc8d42
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
3. 在EntryAbility.ets文件的onCreate中调用预加载实现类[PrefetchWrapper](cloudfoundation-prefetch-implementation-class.md#prefetchwrapper)的doPeriodicPrefetch方法。方法内部会先调用[registerPrefetchTask](../harmonyos-references/cloudfoundation-cloudresprefetch.md#registerprefetchtask)方法注册周期性预加载任务，12h后将调用[getPrefetchResult](../harmonyos-references/cloudfoundation-cloudresprefetch.md#getprefetchresult)获取周期性预加载数据。

   **说明** 

   * 系统会结合应用活跃情况进行任务清理。应用不活跃后，如果当前时间 – 任务注册时间 > 72h，则任务将直接从队列移除。移除任务时不立即清理已加载的数据，数据会被定期清理，应用启动时仍然可尝试获取此前已加载的缓存数据，并结合数据时间戳决定是否呈现内容。
   * 获取周期性预加载数据的间隔周期是12h，如果打开应用的时间间隔低于12h，可能将无法获取到最新的预加载数据。
   * 由于系统每隔12h才会拉取一次周期性预加载数据，不方便调试周期性预加载功能，为此，系统提供了[命令行工具](cloudfoundation-commandtool-debug.md)，可以实时拉取周期性预加载数据。

   ```typescript
   PrefetchWrapper.getInstance().doPeriodicPrefetch();
   ```
