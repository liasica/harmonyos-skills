---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1325
title: 长列表数据刷新闪烁
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 长列表数据刷新闪烁
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:08+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:bb2503ccd479b9b3efdfd23fc48fa2c6e681780fdebae79fe64154511e579101
---

## 问题现象

通过LazyForEach渲染列表，其中包含文字与图片，当修改了其中一条数据项的文字内容，或仅仅是进行了列表的上下滑动、列表拖拽等操作时，图片会发生闪烁现象。

## 背景知识

* [LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)为开发者提供了基于数据源渲染出一系列子组件的能力。具体而言，LazyForEach从数据源中按需迭代数据，并在每次迭代时创建相应组件。当在滚动容器中使用了LazyForEach，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会销毁并回收组件以降低内存占用。
* [@Observed装饰器和@ObjectLink装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)：@ObjectLink和@Observed类装饰器用于嵌套对象或数组的场景中进行双向数据同步。
* 设置图片缓存：使用图像加载缓存库[ImageKnife](https://gitcode.com/openharmony-tpc/ImageKnife)设置图片缓存，或者配置LazyForEach懒加载的缓存最大容量和数量，如[缓存列表项](../best-practices/bpta-best-practices-long-list.md#section11667144010222)。
* [@Reusable装饰器](../harmonyos-guides/arkts-reusable.md)：使用@Reusable装饰器时，表示该自定义组件可以复用。与[@Component](../harmonyos-guides/arkts-create-custom-components.md#component)装饰器结合使用，标记为@Reusable的自定义组件在从组件树中移除时，组件及其对应的JS对象将被放入复用缓存中。后续创建新自定义组件节点时，将复用缓存中的节点，从而节约组件重新创建的时间。

## 解决方案

* **场景一**：使用错误键值触发组件重建（必要检查场景）。
  + 原因：若LazyForEach使用了错误的键值（键值重复、键值跟随UI变化），当键值变化时，ArkUI框架将视为该数组元素已被替换或修改，触发组件重建。
  + 典型场景：交换列表项后，列表项中的图片短暂消失并重新加载，出现闪烁。
  + 修改方式：改用唯一的标识符作为键值。为每个数据项定义唯一ID，作为keyGenerator的返回值，确保组件复用稳定性。可以参考[键值使用建议](../harmonyos-guides/arkts-rendering-control-foreach.md#使用建议)。
* **场景二**：组件重建触发图片重载。
  + 原因：当数据源变更时，LazyForEach默认会销毁旧组件并重建新组件，导致图片重新加载。
  + 典型场景：
    - 增删改列表图文项，所有已有图片短暂消失再重新加载，出现闪烁。
    - 仅修改列表中图文项的文字信息，图片会出现闪烁。（直接更改列表项中的文本部分，并通过notifyDataChange或notifyDataReload进行通知，都仍然会造成同行图片闪烁问题，因为该方式会直接修改数据源，造成组件重新加载。）
  + 修改方式： 对数据类添加@Observed装饰器，子组件通过@ObjectLink绑定需响应的属性，仅更新变化部分。详细请见：[重渲染时图片闪烁](../harmonyos-guides/arkts-rendering-control-lazyforeach.md#重渲染时图片闪烁)。
* **场景三**：图片加载未缓存导致短暂空白。
  + 原因：图片加载需从资源或网络获取，若未启用缓存机制，重复加载会导致短暂空白或闪烁。
  + 典型场景：列表实时加载网络图片，来回滚动列表时，图片出现闪烁。
  + 修改方式：使用ImageKnife预加载图片时，这张图片会被缓存到内存当中，只要在它还没从内存中被清除之前，下次再加载这张图片都会直接从内存中读取，而不用重新从网络或硬盘上读取，大幅度提升图片的加载效率，确保图片展示时不会出现因加载导致的短暂空白。除此之外，若自动的内存缓存不能满足处理图片的需求，开发者还可以在RequestOption类中配置相应的参数，包括图片路径、图片大小、占位图及缓存策略等。
* **场景四**：数据量大时内存占用过大，渲染卡顿。
  + 原因：数据量极大，滑出可视区的数据不断重建，造成渲染卡顿、滑动丢帧。
  + 典型场景：长列表滚动卡顿，图片闪烁。
  + 修改方式：启用组件复用与缓存，通过@Reusable装饰器标记可复用列表项组件，滑出可视区后存入复用池，减少重建开销，详细原理请见：[组件复用](../best-practices/bpta-best-practices-long-list.md#section36781044162218)；同时配置缓冲区，预加载可视区前后N个项，降低滑动时的白屏概率，详细原理请见：缓存列表项。在缓存列表项的基础上增加组件复用，参考[场景案例](../best-practices/bpta-best-practices-long-list.md#section19482174122811)。

## 常见FAQ

Q：@ObjectLink和@Observed装饰的数据更新后界面并未刷新。

A：请参考[@ObjectLink与@Observed的详细使用方法和限制条件](../harmonyos-guides/arkts-observed-and-objectlink.md)。

Q：列表滚动配合LazyForEach中如何使用组件复用？

A：请参考指南：[列表滚动配合LazyForEach使用](../harmonyos-guides/arkts-reusable.md#列表滚动配合lazyforeach使用)。

Q：在使用@Reusable降低渲染卡顿、滑动丢帧的问题时，随着数据的增加，内存也在一直增长，直到触发到回收。

A：可以通过提高组件的复用率，来降低内存的增长速度：使用[aboutToRecycle](../harmonyos-references/ts-custom-component-lifecycle.md#abouttorecycle10)回调实现节点的复用，或者设置[freezeWhenInactive](../harmonyos-guides/arkts-custom-components-freeze.md)属性为true，启用自定义组件冻结功能。

Q：使用Swiper和LazyForEach展示列表数据，使用notifyDatasetChange动态添加数据时item会闪烁，如何解决？

A：notifyDatasetChange会直接修改数据源，造成组件重新加载，可以使用notifyDataAdd通知控制器数据增加。

Q：使用被@ObjectLink和@Observed装饰的数据发生变动时，图片刷新后仍然出现闪烁现象，其原因是什么？

A：@Observed类装饰器，需要放在class的定义前，使用new创建类对象，参考链接：[@Observed类装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)。不使用new创建类也会导致刷新时出现闪烁。

## 总结

LazyForEach触发图片闪烁的核心在于组件重建，通过精准更新数据源（@Observed/@ObjectLink）、启用缓存策略（图片与组件复用），可显著减少闪烁问题。对于复杂场景，建议结合@Reusable和cachedCount进一步优化性能。

| 问题场景 | 解决方案 |
| --- | --- |
| 1. 拖拽交换列表项顺序。 2. 列表数据重新排序（如按时间倒序排列）。 3. 动态增删列表项（如删除聊天消息列表中的某一项）。 | key值唯一且固定（必备条件）。 |
| 1. 点击按钮后批量替换数据源。 2. 局部属性变更（如文本、状态）错误。 | 配套使用@Observed/@ObjectLink精准更新。 |
| 1. 首次进入页面时加载图片。 2. 频繁切换图片URL。 3. 较多高清大图。 | 预加载图片。 |
| 长列表滑动。 | @Reusable标记可复用组件并配置缓冲区。 |
