---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/cloudfoundation-call-install-and-periodic-prefetch
title: 调用全部预加载
breadcrumb: 指南 > 应用服务 > Cloud Foundation Kit（云开发服务） > 预加载 > 调用预加载 > 调用全部预加载
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:25+08:00
doc_updated_at: 2026-09-01
content_hash: sha256:bd99f5d6f0f98885009caad3ce2dc416b49c20a709590247bcd7ec478a98739d
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
3. 在EntryAbility.ets文件的onCreate中调用预加载实现类[PrefetchWrapper](cloudfoundation-prefetch-implementation-class.md#prefetchwrapper)的doPrefetch方法。应用安装后首次打开时，跳转应用详情页调用跳链安装预加载，跳转首页调用安装预加载；应用安装后非首次打开时，则调用周期性预加载。

   ```typescript
   PrefetchWrapper.getInstance().doPrefetch();
   ```
