---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-control-rendering-range
title: 渲染范围控制
breadcrumb: 最佳实践 > 性能 > 性能优化 > 渲染范围控制
category: best-practices
scraped_at: 2026-04-28T08:22:23+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:20194e4473fbc826febbdb15bbec8b83403dcc0f0fb9b9a3f8e210349ebbf03e
---

在应用开发中，控制UI渲染范围，防止界面卡顿或掉帧。

## 合理控制元素显示与隐藏

控制元素显示与隐藏是一种常见的场景，使用Visibility.None、if条件判断等都能够实现该效果。其中if条件判断控制的是组件的创建、布局阶段，visibility属性控制的是元素在布局阶段是否参与布局渲染。若使用方式不当，将引起性能问题。具体案例与实验数据请参阅[合理控制元素显示与隐藏](bpta-improve-layout-performance.md#section14111154271)。

## 懒加载

[懒加载LazyForEach](bpta-lazyforeach-optimization.md)是一种延迟加载的技术，它是在需要的时候才加载数据或资源，并在每次迭代过程中创建相应的组件，而不是一次性将所有内容都加载出来。通常应用于[长列表优化](bpta-best-practices-long-list.md#section182645364229)、[瀑布流优化](bpta-waterflow-performance-optimization.md#section125201667329)等数据量较大、子组件可重复使用的场景，当用户滚动页面到相应位置时，才会触发资源的加载，以减少组件的加载时间，提高应用性能，提升用户体验。

懒加载可以通过设置cachedCount来指定缓存数量，除屏幕内显示的Item组件外，还会预先将屏幕可视区外指定数量的数据缓存。具体的原理与优化案例请参阅[缓存列表项](bpta-best-practices-long-list.md)。

## 组件复用

组件复用通过重用已有组件节点减少创建开销，显著提升UI线程响应速度。组件复用针对的是自定义组件，只要发生了相同自定义组件销毁和再创建的场景，都可以使用组件复用，例如[长列表优化](bpta-best-practices-long-list.md#section36781044162218)、[瀑布流优化](bpta-waterflow-performance-optimization.md#section189041489339)、[Swiper组件优化](bpta-swiper_high_performance_development_guide.md#section10363132882518)等场景，会出现大量重复布局的创建，使用组件复用可以大幅度降低了因频繁创建与销毁组件带来的性能损耗。组件复用的基本原理请参阅[组件复用最佳实践](bpta-component-reuse.md)。

## 分帧渲染

在应用开发中，页面内列表结构复杂，每个列表项包含的组件较多，就会导致嵌套层级较深，从而引起组件负载加重，绘制耗时增长。在这种情况下，转场或者列表滑动的时候列表项就会一次性加载大量的数据，此时可以采用分帧渲染，将本来一帧内加载的数据分成多帧加载，但是分帧渲染需要开发者计算每帧中加载多少数据，操作复杂，因此在必要的情况下才推荐使用。具体的原理与优化案例请参阅[高负载场景下分帧渲染](bpta-dispose-highly-loaded-component-render.md)。
