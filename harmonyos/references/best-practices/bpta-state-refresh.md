---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-state-refresh
title: 状态刷新控制
breadcrumb: 最佳实践 > 性能 > 性能优化 > 状态刷新控制
category: best-practices
scraped_at: 2026-11-10T10:42:07+08:00
doc_updated_at: 2026-11-09
content_hash: sha256:4e770d6b1a3dc381ba0188b4b5d05af56b0e3317f5285993db9f124b4feaf5bb
---

在声明式UI编程范式中，UI是应用程序状态的函数，应用程序状态的修改会更新相应的UI界面。ArkUI采用了[MVVM](../harmonyos-guides/arkts-mvvm.md)MVVM模式作为UI范式，其中ViewModel将数据与视图绑定在一起，更新数据的时候直接更新视图。具体参考，[MVVM模式（V1）](../harmonyos-guides/arkts-mvvm.md)和[MVVM模式（V2）](../doccenter-capabilities/arkts-mvvm-v2.md)。

**图1** ArkUI的MVVM模式

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/LBkgopnqT8OrJm05e78qNQ/zh-cn_image_0000002229336545.png "点击放大")

ArkUI提供了一系列装饰器实现ViewModel的能力，如[@Prop装饰器：父子单向同步](../harmonyos-guides/arkts-prop.md)、[@Link装饰器：父子双向同步](../harmonyos-guides/arkts-link.md)、[@Provide装饰器和@Consume装饰器：与后代组件双向同步](../harmonyos-guides/arkts-provide-and-consume.md)、[LocalStorage：页面级UI状态存储](../harmonyos-guides/arkts-localstorage.md)等。当自定义组件内变量被装饰器装饰时变为状态变量，状态变量的改变会引起UI的渲染刷新。

## 避免不必要的状态变量使用

* 状态变量的管理有一定的开销，应在合理场景使用，普通的变量用状态变量标记可能会导致性能劣化，应删除冗余的状态变量标记。
* 通过使用临时变量的计算代替直接操作状态变量，可以使ArkUI仅在最后一次状态变量变更时查询并渲染组件，建议使用临时变量替换状态变量，减少不必要的行为，从而提高应用性能。

具体参考[避免不必要的状态变量的使用](bpta-status-management.md#section2674939304)。

## 最小化状态共享范围

* 状态变量使用范围不当，可能会带来组件冗余刷新导致的性能问题，具体可参考[组件冗余刷新解决方案](bpta-redundancy-refresh-guide.md)。

* 在没有强烈的业务需求下，尽可能按照状态需要共享的最小范围选择合适的装饰器实现最小化状态共享范围。应用开发过程中，按照组件颗粒度，状态一般分为组件内独享的状态和组件间需要共享的状态。

## 减少不必要的参数层层传递

当共享状态的组件间层级相差较大时，会出现状态层层传递的现象。对于状态传递过程中途经的全部组件，都需要增加入参接收该状态再将状态传递给子组件，因此应减少不必要的参数层层传递并按照状态复杂度选择装饰器。

## 精细化拆分复杂状态

对于AppStorage的使用，由于其作用范围最广，开发者为了方便开发容易将各种状态存入其中以达到共享的目的，这通常会造成大量的性能损失。具体的精细化拆分复杂操作案例请参阅[AppStorage：应用全局的UI状态存储](../doccenter-capabilities/arkts-appstorage.md)。

## 集中化状态修改逻辑

当多个子组件修改状态的逻辑基本相同时，建议将状态的修改集中到单个函数中，以提升逻辑的可复用性、代码的可维护性和可测试性。具体的集中化状态修改逻辑案例请参阅[学习UI范式状态管理](../doccenter-capabilities/arkts-state-management.md)。

## 使用监听和订阅精准控制组件刷新

在多个组件依赖同一数据源时，直接关联数据源会导致每次数据源变化都刷新所有组件。为精准控制组件刷新，可采取以下策略：

* 在组件中使用[@Watch装饰器：状态变量更改通知](../doccenter-capabilities/arkts-watch.md)，当数据变化时执行业务逻辑，确保只有满足条件的组件进行刷新。
* 当组件关系复杂或跨越层级过多时，推荐使用[EventHub](../harmonyos-references/js-apis-inner-application-eventhub.md)或者[Emitter](../doccenter-references/api/js-apis-emitter.md#emitter22)实现自定义事件发布订阅。当数据源改变时发布事件，依赖该数据源的组件通过订阅事件来获取数据源的改变，完成业务逻辑的处理，从而实现组件的精准刷新。
