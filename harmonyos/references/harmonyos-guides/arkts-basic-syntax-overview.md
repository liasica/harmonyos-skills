---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-basic-syntax-overview
title: 基本语法概述
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > 基本语法概述
category: harmonyos-guides
scraped_at: 2026-11-14T08:46:57+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:03488b30245ff8c52d530f53038aa6af85f013df08491508016e3eed2378073e
---

在初步了解ArkTS语言后，本指南将以具体的示例来说明ArkTS的基本组成。

如下图所示，点击“按钮”时，文本内容从“Hello World”变为“Hello ArkUI”。

**图1** 示例效果图

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/9nk9noNYTsOWkQ0_dpGkjA/zh-cn_image_0000002788306218.gif?HW-CC-KV=V1&HW-CC-Date=20261114T004520Z&HW-CC-Expire=31536000000&HW-CC-Sign=F9F543D78FB8EA962022032A865D39986F79867C0FAB2B4F6A41876FB653AB12)

本示例中，ArkTS的基本组成如下所示。

**图2** ArkTS的基本组成

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/Drwr0WS0RW2oCY-t0ytoow/zh-cn_image_0000002817425581.png?HW-CC-KV=V1&HW-CC-Date=20261114T004520Z&HW-CC-Expire=31536000000&HW-CC-Sign=24210F6E485A56A5999BD30DF8A86A1C8C1289AB7CF3F876A787457C49044404)

**说明** 

自定义变量不能与基础通用属性/事件名重复。

* [UI装饰器](arkts-decorator-overview.md)： 用于装饰类、结构、方法以及变量，并赋予其特殊的含义。如上述示例中@Entry、@Component和@State都是装饰器，[@Component](arkts-create-custom-components.md#component)表示自定义组件，[@Entry](arkts-create-custom-components.md#entry)表示该自定义组件为入口组件，[@State](arkts-state.md)表示组件中的状态变量，状态变量变化会触发UI刷新。
* [UI描述](arkts-declarative-ui-description.md)：以声明式的方式来描述UI的结构，例如build()方法中的代码块。
* [自定义组件](arkts-create-custom-components.md)：可复用的UI单元，可组合其他组件，如上述被@Component装饰的struct Hello。
* 系统组件：ArkUI框架中默认内置的基础和容器组件，可以直接调用，例如示例中的Column、Text、Divider、Button。
* [属性方法](../harmonyos-references/ts-component-general-attributes.md)：组件可以通过链式调用配置多项属性，如fontSize()、width()、height()、backgroundColor()等。
* [事件方法](../harmonyos-references/ts-component-general-events.md)：组件可以通过链式调用设置多个事件的响应逻辑，如跟随在Button后面的onClick()。

除此之外，ArkTS扩展了多种语法范式来使开发更加便捷：

* [@Builder](arkts-builder.md)/[@BuilderParam](arkts-builderparam.md)：特殊的封装UI描述的方法，细粒度的封装和复用UI描述。
* [@Extend](arkts-extend.md)/[@Styles](arkts-style.md)：扩展系统组件和封装属性样式，更灵活地组合系统组件。
* [stateStyles](arkts-statestyles.md)：多态样式，可以依据组件的内部状态的不同，设置不同样式。
