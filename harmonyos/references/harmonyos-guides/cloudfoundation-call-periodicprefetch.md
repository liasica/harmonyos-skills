---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-periodicprefetch
title: 调用周期性预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 调用预加载 > 调用周期性预加载
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:bfae7983d69afd2c90f8c17b6a64d427af0b95994234e79b3d6c572e3a59e1d7
---

在项目的EntryAbility.ets文件中导入预加载实现类[PrefetchWrapper](cloudfoundation-prefetch-implementation-class.md#prefetchwrapper)，并在onCreate中调用PrefetchWrapper的doPeriodicPrefetch方法。方法内部会先调用[registerPrefetchTask](../harmonyos-references/cloudfoundation-cloudresprefetch.md#registerprefetchtask)方法注册周期性预加载任务，12小时后将调用[getPrefetchResult](../harmonyos-references/cloudfoundation-cloudresprefetch.md#getprefetchresult)获取周期性预加载数据。

说明

* 系统会结合应用活跃情况进行任务清理。应用不活跃后，如果当前时间 – 任务注册时间 > 72小时，则任务将直接从队列移除。移除任务时不立即清理已加载的数据，数据会被定期清理，应用启动时仍然可尝试获取此前已加载的缓存数据，并结合数据时间戳决定是否呈现内容。
* 获取周期性预加载数据的间隔周期是12小时，如果打开应用的时间间隔低于12小时，可能将无法获取到最新的预加载数据。
* 由于系统每隔12小时才会拉取一次周期性预加载数据，不方便调试周期性预加载功能，为此，系统提供了[命令行工具](cloudfoundation-commandtool-debug.md)，可以实时拉取周期性预加载数据。

```
1. import { GlobalContext } from '../common/GlobalContext';
2. import { PrefetchWrapper } from '../prefetchUtil/PrefetchWrapper';

4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
5. GlobalContext.initContext(this.context); // 初始化全局上下文
6. PrefetchWrapper.getInstance().doPeriodicPrefetch();
7. }
```
