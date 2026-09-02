---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-require
title: "@Require装饰器：校验构造传参"
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式基本语法 > @Require装饰器：校验构造传参
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:15+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c6503f7e5190398a516c1ae4f6af58251e477a69743438fe028c0fc3bc1e3039
---

[@Require](../harmonyos-references/ts-universal-require-dynamic.md#require)是校验@Prop、@State、@Provide、@BuilderParam、@Param和普通变量（无状态装饰器修饰的变量）是否需要构造传参的一个装饰器。

**说明** 

从API version 11开始对@Prop/@BuilderParam进行校验。

从API version 11开始，该装饰器支持在ArkTS卡片中使用。

从API version 11开始，该装饰器支持在元服务中使用。

从API version 12开始对@State/@Provide/@Param/普通变量（无状态装饰器修饰的变量）进行校验。

## 概述

当@Require装饰器和[@Prop](arkts-prop.md)、[@State](arkts-state.md)、[@Provide](arkts-provide-and-consume.md)、[@Param](arkts-new-param.md)、[@BuilderParam](arkts-builderparam.md)、普通变量（无状态装饰器修饰的变量）结合使用时，在构造该自定义组件时，@Prop、@State、@Provide、@Param、@BuilderParam和普通变量（无状态装饰器修饰的变量）必须在构造时传参。

## 限制条件

@Require装饰器仅用于装饰struct内的@Prop、@State、@Provide、@BuilderParam、@Param和普通变量（无状态装饰器修饰的变量）。

预览器的限制场景请参考[PreviewChecker检测规则](../harmonyos-guides-V5/ide-previewer-previewchecker-V5.md)。

## 使用场景

当Child组件内使用@Require装饰器和@Prop、@State、@Provide、@BuilderParam、@Param和普通变量（无状态装饰器修饰的变量）结合使用时，父组件SceneRequire在构造Child时必须传参，否则编译不通过。

```typescript
@Entry
@Component
struct SceneRequire {
  @State message: string = 'Hello World';

  @Builder
  buildTest() {
    Row() {
      Text('Hello, world')
        .fontSize(30)
    }
  }

  build() {
    Row() {
      // 构造Child时需传入所有@Require对应参数，否则编译失败。
      Child({
        regularValue: this.message,
        stateValue: this.message,
        provideValue: this.message,
        initMessage: this.message,
        message: this.message,
        buildTest: this.buildTest,
        initBuildTest: this.buildTest
      })
    }
  }
}

@Component
struct Child {
  @Require regularValue: string;
  @Require @State stateValue: string;
  @Require @Provide provideValue: string;
  @Require @BuilderParam buildTest: () => void;
  @Require @BuilderParam initBuildTest: () => void;
  @Require @Prop initMessage: string;
  @Require @Prop message: string;

  build() {
    Column() {
      Text(this.initMessage)
        .fontSize(30)
      Text(this.message)
        .fontSize(30)
      this.initBuildTest();
      this.buildTest();
    }
    .width('100%')
    .height('100%')
  }
}
```

使用[@ComponentV2](arkts-create-custom-components.md#componentv2)修饰的自定义组件ChildPage通过父组件ParentPage进行初始化，因为有@Require装饰@Param，所以父组件必须进行构造赋值。

```typescript
@ObservedV2
class Info {
  @Trace public name: string = '';
  @Trace public age: number = 0;
}

@ComponentV2
struct ChildPage {
  @Require @Param childInfo: Info;
  @Require @Param stateValue: string;

  build() {
    Column() {
      Text(`ChildPage childInfo name :${this.childInfo.name}`)
        .fontSize(15)
        .height(30)
      Text(`ChildPage childInfo age :${this.childInfo.age}`)
        .fontSize(15)
        .height(30)
      Text(`ChildPage stateValue :${this.stateValue}`)
        .fontSize(15)
        .height(30)
    }
  }
}

@Entry
@ComponentV2
struct ParentPage {
  info1: Info = { name: 'Tom', age: 25 };
  label1: string = 'Hello World';
  @Local info2: Info = { name: 'Tom', age: 25 };
  @Local label2: string = 'Hello World';

  build() {
    Column() {
      Text(`info1: ${this.info1.name}  ${this.info1.age}`) // Text1。
        .fontSize(25)
        .height(30)
      // 父组件ParentPage构造子组件ChildPage时进行了构造赋值。
      // 为ChildPage中被@Require @Param装饰的childInfo和stateValue属性传入了值。
      ChildPage({ childInfo: this.info1, stateValue: this.label1 }) // 创建自定义组件。
      Text(`info2: ${this.info2.name}  ${this.info2.age}`) // Text2。
        .fontSize(25)
        .height(30)
      // 同上，在父组件创建子组件的过程中进行构造赋值。
      ChildPage({ childInfo: this.info2, stateValue: this.label2 }) // 创建自定义组件。
      Button('change info1&info2')
        .onClick(() => {
          this.info1 = { name: 'Cat', age: 18 }; // Text1不会刷新，原因是info1没有装饰器装饰，监听不到值的改变。
          this.info2 = { name: 'Cat', age: 18 }; // Text2会刷新，原因是info2有装饰器装饰，能够监听到值的改变。
          this.label1 = 'Luck'; // 不会刷新，原因是label1没有装饰器装饰，监听不到值的改变。
          this.label2 = 'Luck'; // 会刷新，原因是label2有装饰器装饰，可以监听到值的改变。
        })
    }
    .width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/tET8_HOhRwu20I1vTsVnxw/zh-cn_image_0000002706833176.gif)

从API version 18开始，使用@Require装饰@State、@Prop、@Provide装饰的状态变量，可以在无本地初始值的情况下直接在组件内使用，不会编译报错。

```typescript
@Entry
@Component
struct PageOne {
  message: string = 'Hello World';

  build() {
    Column() {
      ChildIndex({ message: this.message })
    }
  }
}

@Component
struct ChildIndex {
  @Require @State message: string;

  build() {
    Column() {
      Text(this.message) // 从API version 18开始，可以编译通过。
    }
  }
}
```

## 常见问题

当状态管理V1组件内将@Require装饰器与@Prop、@State、@Provide、@BuilderParam、普通变量（无状态装饰器修饰的变量）结合使用时，若父组件Index在构造Child时未传递相应参数，则会导致编译失败。当状态管理V2组件内将@Require装饰器与@Param结合使用时，若父组件Index在构造ChildV2时未传递相应参数，则同样会导致编译失败。

【反例】

```ts
@Entry
@Component
struct Index {
  @State message: string = 'Hello World!';

  @Builder
  buildTest() {
    Row() {
      Text('Hello, world!!')
        .fontSize(30)
    }
  }

  build() {
    Row() {
      // 构造Child、ChildV2组件时没有传参，会导致编译不通过。
      Child()
      ChildV2()
    }
  }
}

@Component
struct Child {
  // 使用@Require必须构造时传参。
  @Require regularValue: string;
  @Require @State stateValue: string;
  @Require @Provide provideValue: string;
  @Require @BuilderParam initBuildTest: () => void;
  @Require @Prop initMessage: string;

  build() {
    Column() {
      Text(this.initMessage)
        .fontSize(30)
      this.initBuildTest();
    }
  }
}

@ComponentV2
struct ChildV2 {
  // 使用@Require必须构造时传参。
  @Require @Param message: string;

  build() {
    Column() {
      Text(this.message)
    }
  }
}
```

当父组件Example在构造ChildV1与ChildV2时传递了相应的参数，则编译通过。

【正例】

```typescript
@Entry
@Component
struct Example {
  @State message: string = 'Hello World!';

  @Builder
  buildTest() {
    Row() {
      Text('Hello, world!!')
        .fontSize(30)
    }
  }

  build() {
    Row() {
      // 构造ChildV1、ChildV2组件时传递相应参数，编译通过。
      ChildV1({
        regularValue: 'Hello',
        stateValue: 'Hello',
        provideValue: 'Hello',
        initBuildTest: this.buildTest,
        initMessage: 'Hello'
      })
      ChildV2({ message: this.message })
    }
  }
}

@Component
struct ChildV1 {
  // 使用@Require必须构造时传参。
  @Require regularValue: string;
  @Require @State stateValue: string;
  @Require @Provide provideValue: string;
  @Require @BuilderParam initBuildTest: () => void;
  @Require @Prop initMessage: string;

  build() {
    Column() {
      Text(this.initMessage)
        .fontSize(30)
      this.initBuildTest();
    }
  }
}

@ComponentV2
struct ChildV2 {
  // 使用@Require必须构造时传参。
  @Require @Param message: string;

  build() {
    Column() {
      Text(this.message)
    }
  }
}
```
