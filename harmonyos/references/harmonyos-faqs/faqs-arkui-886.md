---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-886
title: Navigation传参返回参数形式差异的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Navigation传参返回参数形式差异的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fd2ea0bd6c561b9db9197474fae179230094461363d661502128d093a88082dc
---

## 问题现象

使用Navigation进行页面导航，传参时只传了一个参数，为什么接收参数的时候返回的是一个数组？

## 背景知识

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)导航中获取页面参数信息的方式如下：

* [getParamByName](../harmonyos-references/ts-basic-components-navigation.md#getparambyname10)：通过页面名称来获取路由栈内的页面参数信息。
* [getParamByIndex](../harmonyos-references/ts-basic-components-navigation.md#getparambyindex10)：通过路由栈内的页面索引位置获取索引位置的页面信息。

## 问题定位

使用getParamByName会获取全部名为name的NavDestination页面的参数信息。由于页面路由栈中可能存在多个相同name的页面：比如对Page1页面进行多次push入栈操作，并且未对栈内页面清理的情况下，此时页面栈中就有多个Page1，且每个Page1页面都可能携带参数信息，所以getParamByName返回结果为数组。

## 分析结论

getParamByName方式获取页面参数返回数组的原因是路由栈内可能会同时存在多个同名页面，该方式默认会以数组的方式返回所有同名的页面参数信息。

## 修改建议

* **方案一**：由于返回的是一个数组，可以指定数组内某个索引位置的参数接收。
* **方案二**：确保路由栈内只存在一个Page1页面。

  该方案存在两种实现方式：
  1. 采用单例模式，详情请参考Navigation导航中的[LaunchMode](../harmonyos-references/ts-basic-components-navigation.md#launchmode12枚举说明)枚举说明。其中，MOVE\_TO\_TOP\_SINGLETON和POP\_TO\_SINGLETON均为单例模式，只允许页面栈中只能存在一个同名实例页面。
  2. 采用手动删除同名页面的方式，在推送Page1页面之前，采用[removeByName](../harmonyos-references/ts-basic-components-navigation.md#removebyname11)等方式先删除路由栈中的同名页面。虽然通过getParamByName获取页面信息返回的也还是数组，但是数组内只有一个元素。
* **方案三**：采用getParamByIndex的方式获取页面信息。

  该方式是根据页面所在的路由栈的索引位置返回的参数，因为索引位置唯一性，所以该方式返回的页面信息也不再是以数组的方式返回，而是直接以传入的参数直接返回。

  此方案三需要明确自己需要实际接收的是页面在路由栈的哪一个位置。
