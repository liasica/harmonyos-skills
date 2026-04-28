---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-install-and-periodic-prefetch
title: 调用全部预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 调用预加载 > 调用全部预加载
category: harmonyos-guides
scraped_at: 2026-04-28T07:48:48+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:28c9ae51b215657754bd176a436d50376cede5fddc5faed943007aa4adec218c
---

在项目的EntryAbility.ets文件中导入预加载实现类[PrefetchWrapper](cloudfoundation-prefetch-implementation-class.md#prefetchwrapper)，并在onCreate中调用PrefetchWrapper的doPrefetch方法。应用安装后首次打开时，跳转应用详情页调用跳链安装预加载，跳转首页调用安装预加载；应用安装后非首次打开时，调用周期性预加载。

```
1. import { GlobalContext } from '../common/GlobalContext';
2. import { PrefetchWrapper } from '../prefetchUtil/PrefetchWrapper';

4. onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
5. GlobalContext.initContext(this.context); // 初始化全局上下文
6. PrefetchWrapper.getInstance().doPrefetch();
7. }
```
