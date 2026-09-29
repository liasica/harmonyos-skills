---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/standard-foreground-render
title: 前台绘制渲染
breadcrumb: 指南 > 应用体验建议 > 应用功耗体验建议 > 前台场景 > 前台绘制渲染
category: harmonyos-guides
scraped_at: 2026-09-30T07:35:45+08:00
doc_updated_at: 2026-09-29
content_hash: sha256:86736c5d40012d4bc37f5a0ad2b132a726314bf4d73c6f011abec31bc60204aa
---

## 内容布局使用建议

|  |  |
| --- | --- |
| 描述 | 1. 使用扁平化的布局嵌套层级，避免冗余嵌套，删除无效容器节点。 2. 合理使用容器节点，频繁创建和销毁的组件会影响容器布局，导致容器所有组件刷新，可以尝试在内部再添加容器隔离组件，减少更新范围。 3. 容器内的节点按需加载，例如List列表中的组件。 |
| 类型 | 建议 |
| 适用设备 | 手机、平板 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [减少布局节点](../best-practices-V5/bpta-reduce-layout-nodes-V5.md) |

## UI资源使用建议

|  |  |
| --- | --- |
| 描述 | 1. 使用组件复用机制降低系统负载。 2. 精准控制组件更新范围。 3. 建议使用高能效高性能的组件。 |
| 类型 | 建议 |
| 适用设备 | 手机、平板 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [组件复用最佳实践](../best-practices-V5/bpta-component-reuse-V5.md)  [控制状态刷新](../best-practices-V5/bpta-state-refresh-V5.md) |

## 动效使用建议

|  |  |
| --- | --- |
| 描述 | 1. 合理使用animateTo、animator、animation动画，对于不可见动画应及时停止以释放资源。 2. 应用、元服务切入后台，或者灭屏场景，用户不可见的绘制或动效应当立刻停止。 |
| 类型 | 规则 |
| 适用设备 | 手机、平板 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [不可见组件低功耗建议](../best-practices/low-power-consumption-suggestions.md) |

## 缓存使用建议

|  |  |
| --- | --- |
| 描述 | 将重复利用的组件渲染内容进行缓存，便于复用，减少渲染个数。 |
| 类型 | 建议 |
| 适用设备 | 手机、平板 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [缓存使用建议](../best-practices/bpta-low-power-design-in-dark-mode.md)  [使用懒加载优化性能](../best-practices-V5/bpta-lazyforeach-optimization-V5.md)  [组件复用最佳实践](../best-practices-V5/bpta-component-reuse-V5.md) |

## 视效使用建议

|  |  |
| --- | --- |
| 描述 | 若界面内多个组件的视效参数一致，合并视效以减少计算次数，减少场景视觉效果渲染复杂度。 |
| 类型 | 建议 |
| 适用设备 | 手机、平板 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [视效使用建议](../best-practices/bpta-utilize-hwc-efficiently.md)  [特效绘制合并](../harmonyos-references/ts-universal-attributes-use-effect.md) |

## 脏区使用建议

|  |  |
| --- | --- |
| 描述 | 尽量让脏区只包含变化的组件，减少渲染大小。 |
| 类型 | 建议 |
| 适用设备 | 手机、平板 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [脏区使用建议](../best-practices/bpta-utilize-hwc-efficiently.md) |

## 合成使用建议

|  |  |
| --- | --- |
| 描述 | 按需创建图层及使用旋转图层，过多的图层会导致硬件叠加功能失效，造成系统额外功耗开销。 |
| 类型 | 建议 |
| 适用设备 | 手机、平板 |
| 应用形态适用性 | 鸿蒙应用，鸿蒙元服务 |
| 说明 | [合成使用建议](../best-practices/bpta-utilize-hwc-efficiently.md) |
