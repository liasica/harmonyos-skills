---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-once
title: "@Once装饰器：初始化同步一次"
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理（V2） > 管理组件拥有的状态 > @Once装饰器：初始化同步一次
category: harmonyos-guides
scraped_at: 2026-09-10T06:22:01+08:00
doc_updated_at: 2026-09-09
content_hash: sha256:b2e2db4abf9ede00318d5cdcb95cfb137e9c3d2a26ca42a0066c546b9a51cbe5
---

想要实现仅从外部初始化一次且不接受后续同步变化的能力，可以使用[@Once](../harmonyos-references/ts-state-management-once.md#once)装饰器搭配@Param装饰器。

阅读本文档前，请先阅读[@Param](arkts-new-param.md)。

**说明** 

从API version 12开始，在@ComponentV2装饰的自定义组件中支持使用@Once装饰器。

从API version 12开始，该装饰器支持在元服务中使用。

从API version 23开始，该装饰器支持在ArkTS卡片中使用。

## 概述

@Once装饰器在变量初始化时接受外部传入值进行初始化，后续数据源更改不会同步给子组件：

* @Once必须搭配@Param使用，单独使用或搭配其他装饰器使用都是不允许的。
* @Once不影响@Param的观测能力，仅针对数据源的变化做拦截。
* @Once与@Param装饰变量的先后顺序不影响使用功能。
* @Once与@Param搭配使用时，可以在本地修改@Param变量的值。

## 装饰器使用规则说明

@Once装饰器作为辅助装饰器，本身没有装饰类型要求和变量观察能力。

| @Once变量装饰器 | 说明 |
| --- | --- |
| 装饰器参数 | 无。 |
| 使用条件 | 无法单独使用，必须配合@Param装饰器使用。 |

## 限制条件

* @Once仅在[@ComponentV2](arkts-create-custom-components.md#componentv2)装饰的自定义组件中与@Param搭配使用。

  ```typescript
  @ComponentV2
  struct MyComponent {
    @Param @Once onceParam: string = 'onceParam'; // 正确用法
    // ...
  }
  ```
* @Once与@Param的先后顺序无关，可以写成@Param @Once也可以写成@Once @Param。

  ```typescript
  @ComponentV2
  struct MyComponent {
  // ···
    @Param @Once param1: number = 0;
    @Once @Param param2: number = 0;
  // ···
  }
  ```

## 使用场景

### 变量仅初始化同步一次

@Once用于期望变量仅初始化同步数据源一次，之后不再继续同步变化的场景。

```typescript
@ComponentV2
struct ChildComponent {
  // @Once装饰的onceParam仅初始化同步一次
  @Param @Once onceParam: string = '';

  build() {
    Column() {
      Text(`onceParam: ${this.onceParam}`)
        .fontSize(20)
        .margin(10)
    }
    .width('100%')
  }
}

@Entry
@ComponentV2
struct MyComponent {
  // ...
  @Local message: string = 'Hello World';

  build() {
    Column() {
      Text(`Parent message: ${this.message}`)
        .fontSize(20)
        .margin(10)
      Button('change message')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.message = 'Hello Tomorrow';
        })
      ChildComponent({ onceParam: this.message })
    }
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/LqKLYd5BTxqt6EtLdlLVZA/zh-cn_image_0000002747290061.gif)

### 本地修改@Param变量

当@Once与@Param结合使用时，可以解除@Param无法在本地修改的限制，并能够触发UI刷新。此时，使用@Param和@Once的效果类似于[@Local](arkts-new-local.md)，但@Param和@Once还能接收外部传入的初始值。

```typescript
@ObservedV2
class Info {
  @Trace name: string;
  constructor(name: string) {
    this.name = name;
  }
}
@ComponentV2
struct Child {
  // @Once与@Param结合使用时，可以在本地修改，并能够触发UI刷新
  @Param @Once onceParamNum: number = 0;
  @Param @Once @Require onceParamInfo: Info;

  build() {
    Column() {
      Text(`Child onceParamNum: ${this.onceParamNum}`)
        .fontSize(20)
        .margin(10)
      Text(`Child onceParamInfo: ${this.onceParamInfo.name}`)
        .fontSize(20)
        .margin(10)
      Button('changeOnceParamNum')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.onceParamNum++;
        })
      Button('changeParamInfo')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.onceParamInfo = new Info('Cindy');
        })
    }
    .width('100%')
  }
}
@Entry
@ComponentV2
struct Index {
  @Local localNum: number = 10;
  @Local localInfo: Info = new Info('Tom');

  build() {
    Column() {
      Text(`Parent localNum: ${this.localNum}`)
        .fontSize(20)
        .margin(10)
      Text(`Parent localInfo: ${this.localInfo.name}`)
        .fontSize(20)
        .margin(10)
      Button('changeLocalNum')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.localNum++;
        })
      Button('changeLocalInfo')
        .width(300)
        .margin(10)
        .onClick(() => {
          this.localInfo = new Info('Cindy');
        })
      Child({
        onceParamNum: this.localNum,
        onceParamInfo: this.localInfo
      })
    }
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/IpJMoX_USsKdgQLO9Hb4-A/zh-cn_image_0000002747209979.gif)
