---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1059
title: "@Param和@Once相较于@Prop、@Link的使用场景及优势"
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > @Param和@Once相较于@Prop、@Link的使用场景及优势
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:32073d200b57000f1045974d0cff8101ccb2f33cdd562db1edb20af8aa5f5e8a
---

## 问题现象

* 场景一：父组件传入子组件的变量不是状态变量时，如何刷新子组件内@Param装饰的参数？问题代码如下：

  ```ts
  @Entry
  @ComponentV2
  struct SceneOne {
    // 点击的次数
    count: number = 0;

    build() {
      Column({ space: 5 }) {
        Button('父组件改变初始数据')
          .onClick(() => {
            // 对数据源的更改不会同步给子组件
            this.count++;
          });
        Column({ space: 20 }) {
          SceneOneChild({
            count: this.count,
          });
        };
      }.width('100%');
    }
  }

  @ComponentV2
  struct SceneOneChild {
    @Param count: number = 9999;

    build() {
      Column({ space: 5 }) {
        Text(`@Param count ${this.count}`);
      };
    }
  }
  ```

  场景一问题现象如下（当传递普通变量时，在父组件修改不会触发子组件刷新）：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/v5LoB_--RQW1UMhxBSI7-Q/zh-cn_image_0000002658806467.png "点击放大")
* 场景二：如何将V1的@Prop、@Link迁移至V2的@Param？
* 场景三：状态管理V1中由于@State、@Prop、@Link、@Provide等装饰器均能接收参数，当多人协作开发时，复用他人组件的过程中若存在过多的参数，应该如何分辨哪些@State、@Provide装饰的参数需要传递？问题代码如下：

  ```ts
  @Entry
  @Component
  struct Index {
    // 已知需要传递三个参数需要传递给子组件
    @State countOne: number = 999;
    @State countTwo: number = 999;
    @State countThree: number = 999;

    build() {
      Column({ space: 5 }) {
        Button('父组件改变初始数据')
          .onClick(() => {
            this.countOne++;
            this.countTwo++;
            this.countThree++;
          });
        Column({ space: 20 }) {
          /**
           * linkCount、propCount分别采用@Link、@Prop装饰器装饰，则表示需要通过外部传参，
           * 假设this.countTwo需要传递给propCount，this.countThree需要传递给linkCount，
           * 在未被明确告知this.countOne需要传递给谁的情况下，this.countOne存在以下几种可能：
           */
          Child({
            countOne: this.countOne,
            propCount: this.countTwo,
            linkCount: this.countThree
          });
          Child({
            countTwo: this.countOne,
            propCount: this.countTwo,
            linkCount: this.countThree
          });
          Child({
            countThree: this.countOne,
            propCount: this.countTwo,
            linkCount: this.countThree
          });
          Child({
            propCount: this.countTwo,
            linkCount: this.countThree
          });
        };
      }.width('100%');
    }
  }

  @Component
  struct Child {
    @State countOne: number = 0;
    countTwo: number = 0;
    @Provide('countThree') countThree: number = 0;
    @Prop propCount: number = 0;
    @Link linkCount: number;

    build() {
      Column({ space: 5 }) {
        Text(`@State countOne ${this.countOne}`);
        Text(`countTwo ${this.countTwo}`);
        Text(`@Provide('countThree') countThree ${this.countThree}`);
        Text(`@Prop propCount ${this.propCount}`);
        Text(`@Link linkCount ${this.linkCount}`);
      }
      .width('90%')
      .borderRadius(25)
      .backgroundColor('#0A59F7')
      .padding({ top: 20, bottom: 20 });
    }
  }
  ```

## 背景知识

状态管理V2中组件内状态变量装饰器，相较于状态管理V1中组件内状态变量装饰器更加注重本地初始化数据和传入数据的限制与区分：

* [@Local](../harmonyos-guides/arkts-new-local.md)：表示组件内部的状态，使得自定义组件内部的变量具有观察变化的能力。同时被@Local装饰的状态变量只允许本地初始化，不允许外部传参。
* [@Param](../harmonyos-guides/arkts-new-param.md)：表示组件从外部传入的状态，使得父子组件之间的数据能够进行同步。简单类型变量的同步需要搭配[@Event](../harmonyos-guides/arkts-new-event.md)装饰器一起使用。当搭配[@Require](../harmonyos-guides/arkts-require.md)装饰器时，表示该变量不允许本地初始化，只能通过外部传入初始化。@Param使用场景详见官网链接：[使用场景](../harmonyos-guides/arkts-new-param.md#使用场景)。
* [@Once](../harmonyos-guides/arkts-new-once.md)：只在变量初始化时接受外部传入值进行初始化，后续数据源更改不会同步给子组件。同时该装饰器与@Param一起使用时可以实现类似@Local装饰器的同时，允许外部传递参数。@Once使用场景详见官网链接：[使用场景](../harmonyos-guides/arkts-new-once.md#使用场景)。

## 解决方案

问题现象中的场景与解决方案总结如下：

| 场景 | 场景描述 | 解决方案 |
| --- | --- | --- |
| 场景一 | 父组件传入子组件的变量不是状态变量时，如何刷新子组件内@Param装饰的参数？ | 1. 通过其它状态变量的改变强制刷新子组件内普通变量。2. 将普通变量的数据封装到@ObservedV2/@Trace装饰的类里，通过@Trace刷新子组件UI。 |
| 场景二 | @Param与[@Prop](../harmonyos-guides/arkts-prop.md)、[@Link](../harmonyos-guides/arkts-link.md)之间的差异，以及如何将V1的@Prop、@Link迁移至V2的@Param？ | 参考[@Prop->@Param](../harmonyos-guides/arkts-v1-v2-migration-inner-component.md#prop---param)、[@Link->@Param/@Event](../harmonyos-guides/arkts-v1-v2-migration-inner-component.md#link---paramevent)。 |
| 场景三 | 状态管理V1中由于@State、@Prop、@Link、@Provide等装饰器均能接收参数，应该如何分辨哪些参数需要传递？ | 使用状态管理V2的@Param装饰器接收外部传入的参数、@Local等装饰器初始化本地参数，从而有效区分哪些参数需要外部传入，哪些参数是本地初始化。 |

* 场景一：父组件传入子组件的变量不是状态变量时，如何刷新子组件内@Param装饰的参数。

  该场景下存在两种解决方案：

  1. 方案一：通过其它状态变量的改变强制刷新子组件内普通变量。
  2. 方案二：将普通变量的数据封装到@ObservedV2装饰的类里，通过@Trace刷新子组件UI。

     ```ts
     @Entry
     @ComponentV2
     struct SceneOne {
       count: number = 0; // 声明为普通变量
       @Local localCount: number = 0; // 声明为状态变量
       test: Test = new Test(); // 声明为普通变量，内部count被@Trace修饰，可刷新子组件UI

       build() {
         Column({ space: 5 }) {
           Button('父组件改变初始数据')
             .onClick(() => {
               this.count++;
               this.localCount++;
               this.test.count++;
             });
           Column({ space: 20 }) {
             // 方式一：通过其它状态变量的改变强制刷新子组件内count变化
             SceneOneChild({
               count: this.count,
               localCount: this.localCount
             });
             // 方式二：将count数据封装到@ObservedV2/@Trace装饰的类里
             SceneOneChildTwo({
               test: this.test
             });
           };
         }.width('100%');
       }
     }

     @ComponentV2
     struct SceneOneChild {
       @Param count: number = 9999;
       @Param localCount: number = 9999;

       build() {
         Column({ space: 5 }) {
           Text('方式一');
           Text(`@Param count ${this.count}`);
           Text(`@Param localCount ${this.localCount}`);
         };
       }
     }

     @ComponentV2
     struct SceneOneChildTwo {
       @Param test: Test = new Test();

       build() {
         Column({ space: 5 }) {
           Text('方式二');
           Text(`@Param test.count ${this.test.count}`);
         };
       }
     }

     @ObservedV2
     class Test {
       @Trace count: number = 0;
     }
     ```

     场景一实现效果如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/dnySUttZTjay0ndOuWHIbg/zh-cn_image_0000002628567114.png "点击放大")

* 场景二：V1版@Prop、@Link迁移至V2版@Param的方案。

  @Param与@Prop、@Link的差异与迁移方案详见官网：[@Prop->@Param](../harmonyos-guides/arkts-v1-v2-migration-inner-component.md#prop---param)、[@Link->@Param/@Event](../harmonyos-guides/arkts-v1-v2-migration-inner-component.md#link---paramevent)。
* 场景三：使用状态管理V2区分需要传递的参数与不需要传递的参数。
  1. 如场景二的官网示例中由于@Param装饰的状态变量必须先本地初始化，所以需要先在子组件内为@Param赋予初值，若希望实现子组件@Param与@Link一样只能通过外部传参初始化时，需要搭配@Require装饰器一起使用。
  2. 若希望实现类似@State装饰的状态变量，既可以只接收一次外部传入的数据，又可以本地修改，需要在@Param的基础上加上@Once处理。

     完整示例代码如下：

     ```ts
     @Entry
     @ComponentV2
     struct SceneThree {
       // 需要传递的三个参数
       @Local countOne: number = 999;
       @Local countTwo: number = 999;
       @Local countThree: number = 999;

       build() {
         Column({ space: 5 }) {
           Button('父组件改变初始数据')
             .onClick(() => {
               this.countOne++;
               this.countTwo++;
               this.countThree++;
             });
           Column({ space: 20 }) {
             /**
              * 状态管理V2中只有被@Param装饰器装饰的变量可以进行外部传参初始化
              * 未被@Param装饰器装饰的变量，localCount、count、providerCount均不能通过外部传入参数初始化
              * 有效的区分了哪些参数需要外部传入初始化，哪些参数不需要外部传入初始化。
              */
             SceneThreeChild({
               countOne: this.countOne,
               countTwo: this.countTwo,
               countThree: this.countThree,
               change: () => {
                 this.countOne++;
                 this.countTwo++;
                 this.countThree++;
               }
             });
           };
         }.width('100%');
       }
     }

     @ComponentV2
     struct SceneThreeChild {
       @Local localCount: number = 0;
       count: number = 0;
       @Provider('providerCount') providerCount: number = 0;
       @Param @Once countOne: number = 0; // 代表需要外部传参一次，且可以本地修改，类似V1版本中的@State/@Provide可以外部初始化一次
       @Param @Require countTwo: number; // 搭配@Event实现类似@Prop/@Link功能，并且不能本地修改该变量
       @Param countThree: number = 0;
       @Event change: () => void = () => {
       };

       build() {
         Column({ space: 5 }) {
           Text(`@Local localCount ${this.localCount}`);
           Text(`count ${this.count}`);
           Text(`@Provider('providerCount') providerCount ${this.providerCount}`);
           Text(`@Param @Once countOne ${this.countOne}`);
           Text(`@Param @Require countTwo ${this.countTwo}`);
           Text(`@Param countThree ${this.countThree}`);
           Button('子组件改变初始数据')
             .onClick(() => {
               this.change();
             });
         }
         .width('90%')
         .borderRadius(25)
         .backgroundColor('#F1F3F5')
         .padding({ top: 20, bottom: 20 });
       }
     }
     ```

## 常见FAQ

Q：使用@CustomDialog装饰器装饰自定义组件，在该组件中使用@Param后报错。

A：@Param装饰器可增强子组件接受外部参数输入的能力，但@Param装饰器只能在@ComponentV2装饰器的自定义组件中使用，可参考链接：[@Param的使用限制](../harmonyos-guides/arkts-new-param.md#限制条件)。

Q：@Param支持本地默认初始化，@Link是否也可以？

A：@Link不支持本地初始化，必须通过外部传入初始化。

Q：@Param装饰器处理外部输入时出现了错误，该如何排查？

A：参考排查如下：

1. 检查输入参数类型：确保传递给@Param装饰器的参数类型与预期一致。不匹配的数据类型可能会导致运行时错误。
2. 验证参数值的有效性：确保所有通过@Param装饰器传递的参数值都是有效的，并且符合业务逻辑的要求。

## 总结

@Link、@Prop与@Param分别为状态管理V1和状态管理V2的主要接收参数的装饰器，其差异与对比如下：

| 装饰器 | @Link | @Prop | @Param |
| --- | --- | --- | --- |
| 状态管理版本 | 状态管理V1 | 状态管理V1 | 状态管理V2 |
| 初始化规则 | @Link装饰的变量不能本地初始化，只能通过父组件传入，若父组件未传入则会校验报错。 | @Prop装饰的变量允许本地初始化，若无本地初始化则必须从外部传入初始化。当同时存在本地初始值与外部传入值时，优先使用外部传入值进行初始化。 | 1. @Param装饰的变量允许本地初始化，若无本地初始化则必须从外部传入初始化。当同时存在本地初始值与外部传入值时，优先使用外部传入值进行初始化。2. 当@Param搭配@Require一起使用时，不允许本地初始化，只能通过父组件传入，若父组件未传入则会校验报错。 |
| 同步规则 | 双向同步。父组件状态变量与子组件@Link建立双向同步，当其中一方改变时，另一方也会同步更新。 | 单向同步。对父组件状态变量值的修改，将同步给子组件@Prop装饰的变量，子组件@Prop装饰的变量的修改不会同步到父组件的状态变量上。 | 1. 单向同步。对父组件状态变量值的修改，将同步给子组件@Param装饰的变量。2. 双向同步。@Param搭配@Event装饰器在子组件内调用父组件传递的函数，修改父组件的变量（若接收的是对象，且改变的是对象属性时，无需搭配@Event，可以通过@ObservedV2/@Trace装饰的数据源实现双向同步，详见官网：[使用限制](../harmonyos-guides/arkts-new-param.md#限制条件)）。3. 单向首次同步。搭配@Once只接收第一次父组件向子组件传递的参数，父组件后续的修改，将不会再同步给子组件。 |

通过上述差异对比，状态管理V1与状态管理V2在参数传递方面优缺点如下：

| 状态管理版本 | 状态管理V1 | 状态管理V2 |
| --- | --- | --- |
| 优缺点 | @Link、@Prop分别支持双向与单向传递，但是不支持单向首次同步。只能通过@State、@Provide等装饰的状态变量以及没有装饰器装饰的普通变量接收外部传参实现单向首次同步，导致@State、@Provide等其它本地化初始化的变量与需要单向首次同步的变量无法区分，组件内参数较多时，维护成本高。 | 通过在@Param的基础上搭配不同装饰器可分别实现单向同步、双向同步、单向首次同步。实现与@Local、@Provider等本地初始化变量的有效区分。组件内参数较多时，维护成本较低。 |
