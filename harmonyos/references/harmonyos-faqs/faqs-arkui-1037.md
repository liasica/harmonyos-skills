---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1037
title: 如何实现V1、V2版本之间父子组件的数据传递与共享
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现V1、V2版本之间父子组件的数据传递与共享
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:04+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:460e6b66b086aee11f999e194248d8c5ed846c1f5e2e8f5bb7d06b299137f4af
---

## 问题现象

场景一：如何实现V1版本组件向V2版本组件传递与共享数据？

场景二：如何实现V2版本组件向V1版本组件传递与共享数据？

## 背景知识

* [状态管理（V1）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1)：ArkUI状态管理V1提供了多种装饰器，通过使用这些装饰器，状态变量不仅可以观察组件内的改变，还可以在不同组件层级间传递，比如父子组件、跨组件层级，也可以观察全局范围内的变化。
* [状态管理（V2）](../harmonyos-guides/arkts-state-management-overview.md#状态管理v2)：为了增强状态管理V1版本的部分能力，例如深度观察、属性级更新等，ArkUI推出状态管理V2供开发者使用。
* 在实现V1、V2版本之间父子组件的数据传递与共享的功能前，应先了解V1、V2版本混用的规则：

1. API19前，详见官方文档状态管理V1和V2混用指导（API version 19前）：[概述](../harmonyos-guides/arkts-v1-v2-mixusage-before-api-version.md#概述)、[限制条件](../harmonyos-guides/arkts-v1-v2-mixusage-before-api-version.md#限制条件)。
2. API19后，详见官方文档状态管理V1和V2混用指导（API version 19及之后）：[限制条件](../harmonyos-guides/arkts-v1-v2-mixusage.md#限制条件)。

* [UIUtils.enableV2Compatibility](../harmonyos-references/js-apis-statemanagement.md#enablev2compatibility19)：API19新增的方法，用于实现V1版本的数据可以在V2版本中使用的能力。若想要将V2版本的数据传递到V1版本的子组件，可以通过将V1版本的数据声明在V2版本的组件中，然后传递给V1版本的子组件使用。

## 解决方案

根据混用规则总结可实现的方案如下：

|  |  |  |  |
| --- | --- | --- | --- |
| 传递方向 | API | 方案 | 实现方式 |
| V1->V2 | API 19以后 | 使用UIUtils.enableV2Compatibility | 在V1组件向V2组件传递参数时，通过UIUtils.enableV2Compatibility方法把V1的数据转化为能被V2装饰器@Param装饰器接收的数据。 |
| API 19以前 | 使用AppStorage/AppStorageV2 | 使用AppStorageV2.connect传递。 |
| 使用参数传递 | 方式一：在V1组件内直接声明V2装饰器装饰的实例，不使用V1装饰器初始化，该实例可直接传递给V2版本的子组件。 |
| 方式二：创建一个不带任何装饰器装饰的类，内部再嵌套一个V2装饰器装饰的类。 |
| 方式三：在V1组件内通过V1版本装饰器声明的变量，在传递至V2版本的子组件时，用“{}”在外部构造为新的对象后，再传递给V2版本子组件。 |
| V2->V1 | API 19以后 | 使用UIUtils.enableV2Compatibility | 在V2组件向V1组件传递参数时，通过UIUtils.enableV2Compatibility方法将V1版本@Observed装饰器装饰的类转化为能被@Local装饰器直接声明的数据。 |
| API 19以前 | 使用AppStorage/AppStorageV2 | 使用AppStorageV2.connect传递。 |
| 使用参数传递 | 方式一：在V2组件内直接声明V1装饰器装饰的实例，不使用V2装饰器初始化，该实例可直接传递给V1版本的子组件。 |
| 方式二：创建一个不带任何装饰器装饰的类，内部再嵌套一个V2装饰器装饰的类。 |
| 方式三：在V2组件内通过V2版本装饰器声明的变量，在传递至V1版本的子组件时，用“{}”在外部构造为新的对象后，再传递给V1版本子组件。 |

* 场景一：实现V1版本组件向V2版本组件传递与共享数据。
  + 方案一：API19及以后，使用UIUtils.enableV2Compatibility方法，详情参考官网链接：[V1中使用V2的自定义组件](../harmonyos-guides/arkts-v1-v2-mixusage.md#v1中使用v2的自定义组件)。
  + 方案二：全局获取方式，通过[AppStorage](../harmonyos-guides/arkts-appstorage.md)/[AppStorageV2](../harmonyos-guides/arkts-new-appstoragev2.md)实现，适用于API19以前，API19以后建议使用方案一。实现思路如下：
    1. 由于AppStorage中的[@StorageLink](../harmonyos-guides/arkts-appstorage.md#storagelink)只能在V1组件中使用，所以AppStorage在V1向V2传递的场景下，V2版本的子组件不能自动同步更新，只能通过[AppStorage.get](../harmonyos-references/ts-state-management.md#get10)手动获取。建议通过AppStorageV2实现V1版本组件向V2版本组件传递与共享数据的功能。
    2. 在使用AppStorageV2时，可以搭配[@ObservedV2/@Trace](../harmonyos-guides/arkts-new-observedv2-and-trace.md)实现深度观测。
    3. 由于AppStorageV2和@ObservedV2/@Trace是V2版本的装饰器，所以他们修饰的数据在V1子组件内初始化时，不能用V1的装饰器装饰。

       完整示例代码如下：

       ```ts
       import { AppStorageV2 } from '@kit.ArkUI';

       @ObservedV2
       class V1ToV2ExampleTwo {
         @Trace text: string = '1';

         constructor(text: string) {
           this.text = text;
         }
       }

       @Entry
       @Component
       struct V1ToV2Two {
         exampleAppStorageV2: V1ToV2ExampleTwo =
           AppStorageV2.connect<V1ToV2ExampleTwo>(V1ToV2ExampleTwo, () => new V1ToV2ExampleTwo('1'))!; // 不可直接使用V1装饰器装饰

         build() {
           Column({ space: 10 }) {
             Text(`V1父组件，AppStorageV2:${this.exampleAppStorageV2.text}`);
             Button('V1 中修改')
               .onClick(() => {
                 this.exampleAppStorageV2.text += '1';
               });
             Column() {
             }
             .height(50);

             V1ToV2TwoChild();
           }.width('100%');
         }
       }

       @ComponentV2
       struct V1ToV2TwoChild {
         @Local exampleAppStorageV2: V1ToV2ExampleTwo =
           AppStorageV2.connect<V1ToV2ExampleTwo>(V1ToV2ExampleTwo, () => new V1ToV2ExampleTwo('1'))!;

         build() {
           Column({ space: 10 }) {
             Text(`V2子组件，AppStorageV2:${this.exampleAppStorageV2.text}`);
             Button('V2 中修改')
               .onClick(() => {
                 this.exampleAppStorageV2.text += '1';
               });
           };
         }
       }
       ```

       实现效果如下：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/pDqkdJ_5R4aXKWA3MZyIvA/zh-cn_image_0000002658924035.png "点击放大")
  + 方案三：传参方式，该方案一共三种传递形式，适用于API19以前，API19以后建议使用方案一。

    该场景下由于[@Observed/@ObjectLink](../harmonyos-guides/arkts-observed-and-objectlink.md)装饰器需要搭配使用，但是V2版本的子组件不能使用@ObjectLink装饰器，所以该场景下，不建议使用@Observed装饰器装饰的类作为传递的参数。使用ObservedV2/@Trace装饰器装饰的类，作为传递的参数。实现思路如下：
    1. 方式一：在V1组件内直接声明V2装饰器装饰的实例，不使用V1装饰器初始化，该实例可直接传递给V2版本的子组件。
    2. 方式二：创建一个不带任何装饰器装饰的类，内部再嵌套一个V2装饰器装饰的类，就可以实现在V1组件内用V1装饰器实例化该嵌套类。传递给V2版本的子组件时，将该嵌套对象内部的对象单独传递给V2版本的子组件即可。
    3. 方式三：在V1组件内通过V1版本装饰器声明的变量，在传递至V2版本的子组件时，用“{}”在外部构造为新的对象后，就可以允许传递给V2版本子组件。

       **须知** 

       - 若方式三在V1组件内通过V1版本装饰器声明的变量是简单类型如string、number等，要实现在子组件中能修改父组件的变量，需要在父组件内实现一个修改该变量的函数，传递给子组件。子组件通过[@Event](../harmonyos-guides/arkts-new-event.md)接收，需要修改时直接调用该函数即可。
       - 若方式三传递的是对象，由于@ObservedV2/@Trace装饰器装饰的类不能在V1组件内用V1版本的装饰器初始化，所以需要创建一个不带装饰器的类，然后才能用V1装饰器在V1组件内初始化。

  完整示例代码如下：

  ```ts
  @ObservedV2
  class V1ToV2ExampleThreeV2 {
    @Trace text: string = '1';

    constructor(text: string) {
      this.text = text;
    }
  }

  class V1ToV2ExampleThree {
    text: string = '1';

    constructor(text: string) {
      this.text = text;
    }
  }

  class V1ToV2ExampleThreeFather {
    example: V1ToV2ExampleThreeV2 = new V1ToV2ExampleThreeV2('1');
  }

  interface V1ToV2ExampleThreeFace {
    text: string;
  }

  interface V1ToV2ExampleThreeFatherFace {
    example: V1ToV2ExampleThree;
  }

  @Entry
  @Component
  struct V1ToV2Three {
    // 方式一，不使用V1装饰器在V1组件内初始化V2装饰器@ObservedV2/@Trace装饰的类
    exampleOne: V1ToV2ExampleThreeV2 = new V1ToV2ExampleThreeV2('1');
    // 方式二，将V2装饰器@ObservedV2/@Trace装饰的类嵌套进不带任何装饰器装饰的类里，再进行初始化
    @State exampleTwo: V1ToV2ExampleThreeFather = new V1ToV2ExampleThreeFather();
    // 方式三，传递简单类型
    @State text: string = '1';
    // 方式三，传递对象
    @State exampleThreeChange: V1ToV2ExampleThree = new V1ToV2ExampleThree('1');

    build() {
      Column({ space: 10 }) {
        Text(`V1父组件，方式一，参数传递:${this.exampleOne.text}`);
        Text(`V1父组件，方式二，参数传递:${this.exampleTwo.example.text}`);
        Text(`V1父组件，方式三，简单类型参数传递:${this.text}`);
        Text(`V1父组件，方式三，对象参数传递:${this.exampleThreeChange.text}`);
        Button('V1 中修改')
          .onClick(() => {
            // 方式一，数据在V1子组件中修改方式
            this.exampleOne.text += '1';
            // 方式二，数据在V1子组件中修改方式
            this.exampleTwo.example.text += '1';
            // 方式三，传递简单类型在V1子组件中修改方式
            this.text += '1';
            // 方式三，传递对象在V1子组件中修改方式
            this.exampleThreeChange.text += '1';
          });
        Column() {
        }
        .height(20);

        V1ToV2ThreeChild({
          // 方式一，可直接传递
          exampleOne: this.exampleOne,
          // 方式二，需要传递的数据为属性
          exampleTwo: this.exampleTwo.example,
          // 方式三，将字符串作为对象的属性传递
          exampleThree: {
            text: this.text
          },
          changeText: () => {
            this.text += '1';
          },
          // 方式三，将声明的对象作为属性传递
          exampleThreeChange: {
            example: this.exampleThreeChange
          }
        });
      }.width('100%');
    }
  }

  @ComponentV2
  struct V1ToV2ThreeChild {
    // 方式一接收的数据
    @Param @Require exampleOne: V1ToV2ExampleThreeV2;
    // 方式二接收的数据
    @Param @Require exampleTwo: V1ToV2ExampleThreeV2;
    // 方式三（传递简单类型）接收的数据
    @Param @Require exampleThree: V1ToV2ExampleThreeFace;
    // 父组件传递的是简单类型变量时必备，不然无法同步修改父组件字符串内容
    @Event changeText: () => void = () => {
    };
    // 方式三（传递对象）接收的数据
    @Param @Require exampleThreeChange: V1ToV2ExampleThreeFatherFace;

    build() {
      Column({ space: 10 }) {
        Text(`V2子组件，方式一，参数传递:${this.exampleOne.text}`);
        Text(`V2子组件，方式二，参数传递:${this.exampleTwo.text}`);
        Text(`V2子组件，方式三，简单类型参数传递:${this.exampleThree.text}`);
        Text(`V2子组件，方式三，对象参数传递:${this.exampleThreeChange.example.text}`);
        Button('V2 中修改')
          .onClick(() => {
            // 方式一，数据在V2子组件中修改方式
            this.exampleOne.text += '1';
            // 方式二，数据在V2子组件中修改方式
            this.exampleTwo.text += '1';
            // 方式三，传递简单类型在V2子组件中修改方式
            this.changeText();
            // 方式三，传递对象在V2子组件中修改方式
            this.exampleThreeChange.example.text += '1';
          });
      };
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/Zc2e6IYeTUe9529QzTVGWQ/zh-cn_image_0000002628404826.png "点击放大")
* 场景二：实现V2版本组件向V1版本组件传递与共享数据。
  + 方案一：API19之后，使用UIUtils.enableV2Compatibility方法，详情可参考官网链接：[V2中使用V1的自定义组件](../harmonyos-guides/arkts-v1-v2-mixusage.md#v2中使用v1的自定义组件)。
  + 方案二：全局获取方式，通过AppStorage/AppStorageV2实现，适用于API19以前，API19以后建议使用方案一。

    该方案与场景一中方案二实现思路基本一致，额外补充如下：

    V2版本的父组件不能通过AppStorage中的@StorageLink自动同步刷新，只能通过AppStorage.get手动获取，建议通过AppStorageV2实现。

    完整示例代码如下：

    ```ts
    import { AppStorageV2 } from '@kit.ArkUI';

    @ObservedV2
    class V2ToV1ExampleTwoV2 {
      @Trace text: string = '1';

      constructor(text: string) {
        this.text = text;
      }
    }

    @Entry
    @ComponentV2
    struct V2ToV1Two {
      @Local exampleAppStorageV2: V2ToV1ExampleTwoV2 =
        AppStorageV2.connect<V2ToV1ExampleTwoV2>(V2ToV1ExampleTwoV2, () => new V2ToV1ExampleTwoV2('1'))!;

      build() {
        Column({ space: 10 }) {
          Text(`V2父组件，AppStorageV2:${this.exampleAppStorageV2.text}`);
          Button('V2 中修改')
            .onClick(() => {
              this.exampleAppStorageV2.text += '1';
            });
          Column() {
          }
          .height(50);

          V2ToV1TwoChild();
        }.width('100%');
      }
    }

    @Component
    struct V2ToV1TwoChild {
      exampleAppStorageV2: V2ToV1ExampleTwoV2 =
        AppStorageV2.connect<V2ToV1ExampleTwoV2>(V2ToV1ExampleTwoV2, () => new V2ToV1ExampleTwoV2('1'))!; // 不可直接使用V1装饰器装饰

      build() {
        Column({ space: 10 }) {
          Text(`V1子组件，AppStorageV2:${this.exampleAppStorageV2.text}`);
          Button('V1 中修改')
            .onClick(() => {
              this.exampleAppStorageV2.text += '1';
            });
        };
      }
    }
    ```

    实现效果如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/zIkGtqVWTh6cvgbVr0GtQw/zh-cn_image_0000002658804093.png "点击放大")

* 方案三：传参方式，适用于API19以前，API19以后建议使用方案一。

  该方案与场景一中方案三实现思路基本一致，额外补充如下：
  1. 该场景下V2组件作为父组件，V1组件作为子组件。@ObjectLink装饰器可以在V1子组件内使用，所以传递的参数既可以是@Observed装饰器装饰的类，也可以是@ObservedV2/@Trace装饰器装饰的类（@ObservedV2/@Trace装饰器的场景参考下文“方式三，对象参数传递”的场景）。
  2. V2组件作为子组件时，只能通过@Param装饰器接收参数，但是当V1组件作为子组件时，可以通过[@Prop](../harmonyos-guides/arkts-prop.md)、@ObjectLink、[@Link](../harmonyos-guides/arkts-link.md)三种装饰器接收参数。但是根据知识背景中的混用校验规则，@Link只能被V1状态变量初始化，详情见[@Link变量的传递/访问规则说明](../harmonyos-guides/arkts-link.md#变量的传递访问规则说明)，所以使用@Prop、@ObjectLink接收V2父组件传递来的参数。
  3. 在实现“方式三，对象参数传递”的场景时，由于@ObservedV2/@Trace装饰的类可以直接在V2组件内声明，所以将@ObservedV2/@Trace装饰的类实例化后作为属性传递即可。

     完整示例代码如下：

     ```ts
     @Observed
     class V2ToV1ExampleThreeV1 {
       text: string = '1';

       constructor(text: string) {
         this.text = text;
       }
     }

     class V2ToV1ExampleThreeFather {
       example: V2ToV1ExampleThreeV1 = new V2ToV1ExampleThreeV1('1');
     }

     @ObservedV2
     class V2ToV1ExampleThreeV2 {
       @Trace text: string = '1';

       constructor(text: string) {
         this.text = text;
       }
     }

     interface V2ToV1ExampleThreeFatherV2Face {
       example: V2ToV1ExampleThreeV2;
     }

     interface V2ToV1ExampleThreeFace {
       text: string;
     }

     @Entry
     @ComponentV2
     struct V2ToV1Three {
       // 方式一，不使用V2装饰器在V2组件内初始化V1装饰器@Observed装饰的类
       exampleOne: V2ToV1ExampleThreeV1 = new V2ToV1ExampleThreeV1('1');
       // 方式二，将V1装饰器@Observed装饰的类嵌套进不带任何装饰器装饰的类里，再进行初始化
       @Local exampleTwo: V2ToV1ExampleThreeFather = new V2ToV1ExampleThreeFather();
       // 方式三，传递简单类型
       @Local text: string = '1';
       // 方式三，@ObservedV2装饰的类的实例化后传递
       @Local exampleFour: V2ToV1ExampleThreeV2 = new V2ToV1ExampleThreeV2('1');

       build() {
         Column({ space: 10 }) {
           Text(`V2父组件，方式一，参数传递:${this.exampleOne.text}`); // 不刷新
           Text(`V2父组件，方式二，参数传递:${this.exampleTwo.example.text}`); // 不刷新
           Text(`V2父组件，方式三，简单类型参数传递:${this.text}`); // 刷新
           Text(`V2父组件，方式三，对象参数传递:${this.exampleFour.text}`); // 刷新
           Button('V2 中修改')
             .onClick(() => {
               // 方式一，数据在V2父组件中修改方式
               this.exampleOne.text += '1';
               // 方式二，数据在V2父组件中修改方式
               this.exampleTwo.example.text += '1';
               // 方式三，传递简单类型在V2父组件中修改方式
               this.text += '1';
               // 方式三，传递@ObservedV2装饰的对象在V2父组件中修改方式
               this.exampleFour.text += '1';
             });
           Column() {
           }
           .height(20);

           V2ToV1ThreeChild({
             // 方式一，可直接传递
             exampleOne: this.exampleOne,
             // 方式二，传递的是封装后的属性
             exampleTwo: this.exampleTwo.example,
             // 方式三，将字符串作为对象的属性传递
             exampleThree: {
               text: this.text
             },
             changeText: () => {
               this.text += '1';
             },
             // 方式三，将声明的@ObservedV2装饰的对象作为属性传递
             exampleFour: {
               example: this.exampleFour
             }
           });
         }.width('100%');
       }
     }

     @Component
     struct V2ToV1ThreeChild {
       // 方式一接收的数据
       @Prop exampleOne: V2ToV1ExampleThreeV1;
       // 方式二接受的数据
       @ObjectLink exampleTwo: V2ToV1ExampleThreeV1;
       // 方式三（传递简单类型）接收的数据
       @Prop exampleThree: V2ToV1ExampleThreeFace;
       // 父组件传递的是简单类型变量时必备，不然无法同步修改父组件字符串内容
       changeText: () => void = () => {
       };
       // 方式三（传递对象）接收的数据
       @ObjectLink exampleFour: V2ToV1ExampleThreeFatherV2Face;

       build() {
         Column({ space: 10 }) {
           Text(`V1子组件，方式一，参数传递:${this.exampleOne.text}`);
           Text(`V1子组件，方式二，参数传递:${this.exampleTwo.text}`);
           Text(`V1子组件，方式三，简单类型参数传递:${this.exampleThree.text}`);
           Text(`V1子组件，方式三，对象参数传递:${this.exampleFour.example.text}`);
           Button('V1 中修改')
             .onClick(() => {
               // 方式一，数据在V1子组件中修改方式
               this.exampleOne.text += '1';
               // 方式二，数据在V1子组件中修改方式
               this.exampleTwo.text += '1';
               // 方式三，传递简单类型在V1子组件中修改方式
               this.changeText();
               // 方式三，传递对象在V1子组件中修改方式
               this.exampleFour.example.text += '1';
             });
         };
       }
     }
     ```

     实现效果如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/RBQZp8DTRhWpP6qvlSYQTg/zh-cn_image_0000002628564732.png "点击放大")

     **须知** 

     @Observed/@ObjectLink可以实现父组件修改深层属性后，刷新子组件对应属性绑定的UI的功能，但是当子组件内修改深层属性，父组件并不会刷新对应属性绑定的UI。所以除了通过方式三以外的方式一、方式二不会刷新父组件绑定的对应属性的UI。

## 常见FAQ

Q：使用Navigation导航的应用在V1版本中用的是@Provide/@Consume装饰器传递的NavPathStack路由栈。在V1迁移V2过程中，Navigation主页被修改为V2版本，子页依旧是保持的V1版本。此时应该怎样传递NavPathStack路由栈给子页面？

A：由于@ComponentV2内不能使用V1版本的[@Provide/@Consume装饰器](../harmonyos-guides/arkts-provide-and-consume.md)，@Component内不能使用V2版本的[@Provider/@Consumer装饰器](../harmonyos-guides/arkts-new-provider-and-consumer.md)，所以当父子组件分别属于V1、V2版本时，不能使用@Provider/@Consumer、@Provide/@Consume去实现组件见页面的共享与数据传递。可参考解决方案如下：

1. 使用AppStorage存储或者获取数据：在[Navigation](../harmonyos-references/ts-basic-components-navigation.md)主页面通过AppStorage.setOrCreate进行全局存储，在V1版本的[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)子页面内直接通过@StorageLink进行全局路由栈获取。
2. 使用AppStorageV2存储或者获取数据：分别在父组件与子组件通过pathStack: NavPathStack = AppStorageV2.connect(NavPathStack, () => new NavPathStack())!;创建或获取全局路由栈。
3. 如果页面中使用了NavDestination组件，可以通过[onReady](../harmonyos-references/ts-basic-components-navdestination.md#onready11)事件获取路由栈：.onReady((context: NavDestinationContext) => {this.pathInfos = context.pathStack})，从而避免状态管理版本冲突的问题。
4. 通过自定义组件查询接口获取，也可以避免状态管理传递冲突的问题，参考[queryNavigationInfo](../harmonyos-references/ts-custom-component-api.md#querynavigationinfo12)。

Q：在V1迁移V2的过程中，存在部分三方库是V1版本实现，还没适配V2版本，应该如何将V2版本的数据传递给V1版本三方库？

A：建议参考场景二中方案一，方案三实现。该场景下，方案二AppStorageV2.connect没办法写进三方库内。

## 总结

在API19之后，优先推荐使用官方提供的UIUtils.enableV2Compatibility方法实现V1、V2版本之间父子组件的数据传递与共享。
