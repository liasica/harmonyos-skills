---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/eldercare-appconfig
title: 应用声明接入系统关怀模式
breadcrumb: 指南 > 应用框架 > Accessibility Kit（无障碍服务） > 应用长辈关怀功能体验 > 应用声明接入系统关怀模式
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:44+08:00
doc_updated_at: 2026-06-12
content_hash: sha256:e02b9099ff562b5ac75f30dfe0b5d02bd4d71b6e6ee9422ccb26f6d3a31a5b27
---

从API版本26.0.0开始，已实现独立关怀模式功能（或称长辈模式、长辈版、关爱版、关怀版、大字版、敬老版等）的应用，可以通过在应用工程module.json5对应module声明如下metadata，让用户可以在设备“设置>关怀和无障碍>关怀模式>应用管理”里查看本应用，并自由切换关怀模式开关状态。需要注意的是，如果用户在设置里关闭了系统关怀模式开关，应用内关怀模式也会随之关闭，重新开启系统关怀模式，原先被关闭的应用会同步开启。

为实现应用内关怀模式状态与系统设置页面的开关状态保持实时同步，建议参照[应用内关怀模式与系统设置同步](eldercare-senior-mode-description.md)完成配置。

建议声明在有关怀模式功能的module下：

```typescript
{
  "module": {
    // 其他声明此处省略
    "metadata": [{
      "name": "senior_mode",
      "value": "independent_control"
    }]
  }
}
```

如应用内没有独立关怀模式开关，可参照[获取系统关怀模式状态](eldercare-description.md)以实现跟随系统关怀模式变化。
