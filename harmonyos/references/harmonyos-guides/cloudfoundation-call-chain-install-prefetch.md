---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-chain-install-prefetch
title: 调用跳链安装预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 调用预加载 > 调用跳链安装预加载
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:7ff69f4539a4995a8856198161125a9f72f6109b9203c4c97303facf5b1a5cc5
---

在项目的EntryAbility.ets文件中导入预加载实现类[PrefetchWrapper](cloudfoundation-prefetch-implementation-class.md#prefetchwrapper)，并在onCreate中调用PrefetchWrapper的doLinkPrefetch方法。方法内部会先调用[popDeferredLink](../harmonyos-references/applinking-deferredlink-api.md#popdeferredlink)接口获取延迟链接，再调用[getPrefetchResult](../harmonyos-references/cloudfoundation-cloudresprefetch.md#getprefetchresult)获取跳链安装预加载缓存数据。

说明

跳链安装预加载缓存的是应用详情页数据，仅允许调用一次，被调用后将被销毁。

```
1. import { GlobalContext } from '../common/GlobalContext';
2. import { PrefetchWrapper } from '../prefetchUtil/PrefetchWrapper';

4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
5. GlobalContext.initContext(this.context); // 初始化全局上下文
6. PrefetchWrapper.getInstance().doLinkPrefetch();
7. }
```
