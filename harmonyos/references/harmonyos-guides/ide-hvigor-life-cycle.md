---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-life-cycle
title: 构建系统生命周期
breadcrumb: 指南 > 构建应用 > 概述 > 构建系统生命周期
category: harmonyos-guides
scraped_at: 2026-04-29T13:47:08+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:18522fc039d7d5e45f5a3a808a4d1496f546deaa4e318724e9e8c56802647a0c
---

本文档对Hvigor编译构建系统结构及生命周期进行简要讲解，首先介绍Hvigor对工程结构模型的定义，随后介绍什么是任务（Task），最后会介绍Hvigor的构建生命周期以及它是如何依赖hvigor-ohos-plugin一起完成自动化编译构建流程的。

## 工程结构定义

Hvigor将工程解析为一个树形结构，项目为树的根节点，项目中的每个模块为树的叶子节点，树最多为两层，模块中不能包含其他模块，在Hvigor的定义中统称项目或模块为一个node(节点)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/ELYBkFnHTz6blVAXuBdsVg/zh-cn_image_0000002530913018.png?HW-CC-KV=V1&HW-CC-Date=20260429T054707Z&HW-CC-Expire=86400&HW-CC-Sign=F032102D48B44B405AEE4FC24D74E81869968ED853962A988D7D4D8840F3DF6A)

在构建最开始的[初始化阶段](ide-hvigor-life-cycle.md#section19246144681710)，会通过[hvigorconfig.ts文件](ide-hvigor-life-cycle.md#section810245135914)以及工程级build-profile.json5文件中的配置来构造出一个树形结构存储项目的工程结构，工程级build-profile.json5文件和hvigorconfig.ts文件均可以[配置多模块](ide-hvigor-multi-module.md#section99251918477)。

## Hvigor脚本文件

构建的[生命周期](ide-hvigor-life-cycle.md#section8207184919159)中Hvigor使用两个脚本文件来完成插件、任务以及生命周期hook的注册：

* **hvigorconfig.ts**：此文件在整个项目中只有根目录下存在一份，不是构建必须的文件并且默认不存在，如有需要可自行创建，此文件被解析执行的时间较早，可用于在Hvigor生命周期刚开始时操作某些数据。
* **hvigorfile.ts**：此文件在每个node下都有一份，是构建的必须文件，在此文件中可以注册插件、任务以及生命周期hook等操作。

## 任务与任务依赖图

Hvigor是基于任务对您的项目进行自动化构建的，任务（Task）是Hvigor构建过程中的基本工作单元，它定义了构建项目时需要执行的具体工作。任务可以完成多种操作，比如源码编译任务，打包任务或签名任务等。每一种任务的执行逻辑由插件（plugin）提供，插件可以是由[hvigor-ohos-plugin](ide-hvigor-life-cycle.md#section199818016213)提供的默认任务逻辑，也可由您个性化定制。

需要注意的一点是，任务是存在依赖关系的，Hvigor在执行任何任务之前会构建任务依赖图，所有任务会形成一个有向无环图（DAG），如下示例图，任务之间的依赖关系用箭头进行表示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/uFoGsTb5RfuNKRyN4k9Jzw/zh-cn_image_0000002530913020.png?HW-CC-KV=V1&HW-CC-Date=20260429T054707Z&HW-CC-Expire=86400&HW-CC-Sign=92DF0F24D1468DE253B889BAB5CF1BA3281C81DFF4E6575C07FF61B378D173E6)

hvigor插件（hvigor-ohos-plugin）和hvigorfile.ts文件中的构建脚本都将通过任务依赖机制对任务依赖图做出影响。

## hvigor-ohos-plugin

hvigor-ohos-plugin是默认的构建插件，为任务（Task）的完成提供业务逻辑支持，比如为Hvigor提供HAP、HAR和HSP打包服务等任务，每一种任务的具体执行逻辑由本模块中不同的插件来提供。

### Hvigor与hvigor-ohos-plugin的关系

[概述](ide-hvigor.md)部分提到了Hvigor提供任务注册编排以及配置管理等任务管理机制，它负责控制任务的执行流程，但是并不包含每一个任务的具体业务逻辑，具体逻辑是由hvigor-ohos-plugin提供的。

Hvigor和hvigor-ohos-plugin的关系可以通过下图来说明，Hvigor接受任务的注册并编排任务执行顺序，并按照顺序依次调用hvigor-ohos-plugin中的插件来执行任务。如果您定制了自己的任务逻辑插件并将其注册，Hvigor也会调用您的个性化插件来完成编译构建流程。

在Hvigor执行构建的过程中，hvigor-ohos-plugin会向Hvigor进行任务的注册，Hvigor会根据构建的[任务依赖图](ide-hvigor-life-cycle.md#section194191858161220)依次调用对应的插件来执行相应任务，在完成编译、打包、签名等一系列任务后，Hvigor也就正式完成了构建。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/AHfwwbIzRwujMi2rKpx35Q/zh-cn_image_0000002561832945.png?HW-CC-KV=V1&HW-CC-Date=20260429T054707Z&HW-CC-Expire=86400&HW-CC-Sign=D592F4CE9198E0BC9005A5418AF2A6F537972AC0801C9696F059D031889B2EE6)

## Hvigor生命周期

生命周期展示了Hvigor编译构建系统如何进行一次完整的编译构建流程。Hvigor的编译构建过程有三个不同的阶段，分为初始化、配置和执行，Hvigor会按顺序运行这些阶段。

### 初始化

说明

此阶段主要目的为初始化项目的编译参数，构造出项目结构的树形数据模型，每个node为一个[HvigorNode](ide-hvigor-api.md#section14832104719474)对象。

1. 根据命令参数和hvigor-config.json5文件中的配置，设置Hvigor的构建参数，并构造出hvigor对象和hvigorConfig对象：
   * hvigor对象贯穿整个hvigor生命周期，从最开始创建出来一直到此次构建结束才被销毁；
   * hvigorConfig对象用于表示hvigor对项目结构的抽象，是hvigor的简单配置对象，用于动态添加或删除节点，它也会保存对每个节点的描述对象（nodeDescriptor对象）。
2. 通过项目根目录下的build-profile.json5文件，创建出[rootNodeDescriptor](ide-hvigor-api.md#section1914012226435)实例，并通过其中的modules字段，来初始化工程中所有模块的[NodeDescriptor](ide-hvigor-api.md#section1914012226435)对象实例。
3. 执行项目根目录下的hvigorconfig.ts文件，可以在此文件中通过hvigor的相关API来为生命周期注册hook或在构建开始时进行其他处理。
4. 根据节点描述对象构造出每个节点的HvigorNode对象实例。

### 配置

说明

此阶段开始时，所有的node都已经加载完毕，但每个node中还没有加载插件（plugin）、任务（task）和DAG图，此阶段的主要目的就是加载出这些内容。

1. 执行每个node中的hvigorfile.ts文件，为每个node添加插件（向Hvigor注册任务），执行插件的apply方法，并添加插件的上下文。
2. 基于上一步加载的插件和任务，根据任务执行的依赖关系构造出DAG图。

### 执行

* 执行选定的任务。
* 任务之间的依赖关系决定了任务执行顺序。
* 任务可以并行执行。

### 生命周期及hook点

在Hvigor的生命周期中，以下多个hook点可供您使用，便于您在对应的时机调用某些逻辑。

在下图中所有绿色标记的线框为可以使用的hook点。每个hook点的使用方式请参考[基础构建能力](ide-hvigor-api.md)。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/Cqirj5ahT1q5SSsCjtDBAg/zh-cn_image_0000002573888241.png?HW-CC-KV=V1&HW-CC-Date=20260429T054707Z&HW-CC-Expire=86400&HW-CC-Sign=1572E9402EF9010F4E00A1D7851B0FDD472C6A5672934EB75CB9F99BC1779028)
