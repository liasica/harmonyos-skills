---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1440
title: 状态管理中对象属性变化时UI不刷新
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 状态管理中对象属性变化时UI不刷新
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:67e45060eb8f46d5b99fde5cc8707dacbe27f911d3c387edb64ac66dc774db3b
---

## 问题现象

场景一：嵌套对象或者对象数组的属性发生改变时，如何实现UI刷新？

场景二：@ObjectLink修改嵌套对象属性后List不刷新。

## 背景知识

ArkUI中[@Link装饰器](../harmonyos-guides/arkts-link.md#简单类型和类对象类型的link)是用于父子组件中的变量双向同步的。子组件通过@Link接收父组件传递的状态变量，当父组件/子组件任意一方发生改变时都会引起另一个同步变化。当装饰的是基本数据类型或者简单对象这类能直接被ArkUI框架观察到的就能触发页面实时渲染。对于复杂对象只能同步值的变化，无法触发UI渲染刷新。

[@Observed装饰器和@ObjectLink装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)用于实现嵌套对象或数组的双向数据同步。@ObjectLink接收的变量必须是@Observed装饰的类的实例，@ObjectLink仅能观察其直接绑定的对象属性变化，无法自动穿透到更深层的嵌套对象属性。

## 解决方案

场景一：

@Link装饰器只监听对象本身的地址以及第一层属性的地址变化。当装饰的对象为复杂类型，如对象数组时，其属性的变化不会让UI刷新。可以通过浅拷贝覆盖原来的值达到刷新UI的效果，但会导致不必要的渲染，不建议使用。

对于复杂对象的监听可以使用[@Observed装饰器和@ObjectLink装饰器](../harmonyos-guides/arkts-observed-and-objectlink.md)、[@ObservedV2装饰器和@Trace装饰器](../harmonyos-guides/arkts-new-observedv2-and-trace.md)、[@Monitor装饰器](../harmonyos-guides/arkts-new-monitor.md)，能观察到对象内部的其他对象发生改变，以实现刷新UI的功能。

场景二：

@ObjectLink修改嵌套对象属性后List不刷新，通常由以下几种情况导致：

1. 嵌套对象的类未加@Observed装饰器。@ObjectLink接收的变量必须是@Observed装饰的类的实例，否则框架会打印error日志，属性变化不会被观测到，UI不会更新。
2. 多级嵌套时，每一层的类都需要加@Observed，且每一层都需要抽离成独立子组件并用@ObjectLink绑定。@ObjectLink仅能观察其直接绑定的对象属性变化，无法自动穿透到更深层的嵌套对象属性。
3. ForEach的keyGenerator返回值未变化。当修改数组中对象的属性时，如果key没有变化，ForEach不会重建子组件，@ObjectLink仍然指向旧的对象引用，导致@State与@ObjectLink断链。
4. 嵌套对象未通过new实例化，而是直接赋值对象字面量。没有new创建的过程，无法激活@Observed的代理监听。

更多定位方法可参考[状态变量改变不触发组件刷新问题常用定位方法](../harmonyos-guides/troubleshooting-state-manage.md)。
