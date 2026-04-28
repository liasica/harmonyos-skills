---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-installprefetch
title: 调用安装预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 调用预加载 > 调用安装预加载
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:47+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:93dd2d9b575701153a4819422e1389e5aaeff78fdb326f935f69c6d2423b1a53
---

在项目的EntryAbility.ets文件中导入预加载实现类[PrefetchWrapper](cloudfoundation-prefetch-implementation-class.md#prefetchwrapper)，并在onCreate中调用PrefetchWrapper的doInstallPrefetch方法。方法内部会调用[getPrefetchResult](../harmonyos-references/cloudfoundation-cloudresprefetch.md#getprefetchresult)获取安装预加载缓存数据。

说明

* 安装预加载缓存数据，仅允许调用一次，被调用后将被销毁。
* 应用安装开始时，系统会拉取安装预加载云侧数据并缓存到本地。

```
1. import { GlobalContext } from '../common/GlobalContext';
2. import { PrefetchWrapper } from '../prefetchUtil/PrefetchWrapper';

4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
5. GlobalContext.initContext(this.context); // 初始化全局上下文
6. PrefetchWrapper.getInstance().doInstallPrefetch();
7. }
```

说明

调用安装预加载过程中，可参考[FAQ](cloudfoundation-faq-5.md)定位预加载问题。
