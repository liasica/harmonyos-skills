---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-885
title: 状态管理V1和V2适用场景介绍
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 状态管理V1和V2适用场景介绍
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:16+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:17868bc03b0fcd9a2472efe5020f95f9ac13437493dca4dea09c2aa7abcc6229
---

## 问题现象

状态管理存在V1和V2版本，那在实际开发过程中，状态管理是推荐用V1开发还是V2开发？

## 背景知识

ArkUI提供了[状态管理（V1）](../harmonyos-guides/arkts-state-management-v1.md)和[状态管理（V2）](../harmonyos-guides/arkts-state-management-v2.md)用于应用开发中状态变量的管理。状态管理V1使用代理观察数据，当创建一个状态变量时，同时也创建了一个数据代理观察者。状态管理V2将观察能力增强到数据本身，数据本身就是可观察的，更改数据会触发相应的视图的更新。两种状态管理方式存在的一些差异，可参考：[状态管理V1与V2能力对比](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1与v2能力对比)、[状态管理V1现状以及V2优点](../harmonyos-guides/arkts-state-management-overview.md#状态管理v1现状以及v2优点)、[V1状态变量更新和V2状态变量更新差异](../harmonyos-guides/arkts-v1-v2-update-difference.md#v1状态变量更新和v2状态变量更新差异)。

## 解决方案

针对应用开发过程中常见的场景，汇总如下表：

| 场景 | 状态管理选择说明 |
| --- | --- |
| 深度状态观测 | 为了对嵌套类对象属性直接观测，推荐使用V2。 |
| 计算属性重复计算 | 为了避免重用属性而重复计算导致的性能问题，推荐使用V2。 |
| 状态变量修改监听 | 为了对状态变量具有深度监听的能力，且能获取到变化前的值，推荐使用V2。 |
| 使用animateTo实现动画 | 由于在状态管理V2中使用animateTo可能出现动画效果异常，推荐使用V1，API22以后可以通过[applySync/flushUpdates/flushUIUpdates接口：同步刷新](../harmonyos-guides/arkts-new-applysync-flushupdates-flushuiupdates.md)辅助方法规避。 |
| 使用高级组件 | 由于在低版本API中状态管理V2中未提供部分高级组件，推荐使用V1。 从API version 18开始，系统预置UI组件支持在状态管理V2组件中使用。 |
| 自定义局部页面主题 | 由于在低版本API中状态管理V2中未提供WithTheme组件，推荐使用V1。从API version 18开始，该接口支持在状态管理V2组件中使用。 |
| 自定义组件复用 | 由于在低版本API中状态管理V2中未提供@Reusable装饰器，推荐使用V1。从API version 18开始，该装饰器支持在状态管理V2组件中使用。 |

**一、状态管理V2的优势与适用场景**。

1. **深度状态观测：** V2通过@ObservedV2和@Trace装饰器，支持对嵌套类对象属性的直接观测，无需像V1那样依赖@ObjectLink和自定义组件封装。例如，当修改对象的深层属性（如obj.a.b）时，V2能自动触发UI更新，而V1需要手动处理或依赖额外逻辑。

   场景案例对比如下：
   * 使用V1监控嵌套类对象属性的变化：

     ```ts
     @Observed
     class Father {
       son: Son;

       constructor(name: string, age: number) {
         this.son = new Son(name, age);
       }
     }

     @Observed
     class Son {
       name: string;
       age: number;

       constructor(name: string, age: number) {
         this.name = name;
         this.age = age;
       }
     }

     @Component
     struct Child {
       // 使用@ObjectLink装饰器与自定义组件来实现观测
       @ObjectLink son: Son;

       build() {
         Row() {
           Column() {
             Text(`name: ${this.son.name} age: ${this.son.age}`)
               .fontSize(50)
               .fontWeight(FontWeight.Bold)
               .onClick(() => {
                 this.son.age++;
               });
           }
           .width('100%');
         }
         .height('100%');
       }
     }

     @Component
     export struct NestedV1 {
       @State father: Father = new Father('John', 8);

       build() {
         Column() {
           Text('使用V1监控嵌套类对象属性的变化')
             .fontSize(20)
             .fontWeight(FontWeight.Bold);
           Child({ son: this.father.son });
         }
         .width('100%')
         .height('100%');
       }
     }
     ```
   * 使用V2监控嵌套类对象属性的变化：

     ```ts
     @ObservedV2
     class Son {
       // 在嵌套类中使用@Trace装饰的属性具有被观测变化的能力
       @Trace age: number = 100;
       name: string;

       constructor(name: string, age: number) {
         this.name = name;
         this.age = age;
       }
     }

     class Father {
       son: Son;

       constructor(name: string, age: number) {
         this.son = new Son(name, age);
       }
     }

     @ComponentV2
     export struct NestedV2 {
       father: Father = new Father('John', 8);

       build() {
         Column() {
           Text('使用V2监控嵌套类对象属性的变化')
             .fontSize(20)
             .fontWeight(FontWeight.Bold);
           Row() {
             Column() {
               Text(`name: ${this.father.son.name} age: ${this.father.son.age}`)
                 .fontSize(50)
                 .fontWeight(FontWeight.Bold)
                 .onClick(() => {
                   this.father.son.age++;
                 });
             }
             .width('100%');
           }
           .height('100%');
         }
         .height('100%')
         .width('100%')
         .height('100%');
       }
     }
     ```

   总结：通过V1这种方式虽然能够实现对嵌套类中属性变化的观测，但是当嵌套层级较深时，代码将会变得十分复杂，易用性差。采用V2的话，使用@ObservedV2装饰的嵌套类中被@Trace装饰的属性具有被观测变化的能力，当该属性值变化时，会触发该属性绑定的UI组件刷新，代码较简洁。
2. **属性重复计算优化：** V2通过@Computed计算属性在被计算的值变化的时候，只会计算一次，解决V1中多次重用该属性从而重复计算导致的性能问题。

   场景案例对比如下：
   * 使用V1重用属性导致重复计算：

     ```ts
     @Component
     export struct CalculationV1 {
       firstName: string = 'Li';
       @State lastName: string = 'Hua';

       build() {
         Column() {
           Text('使用V1重用属性导致重复计算')
             .fontSize(20)
             .fontWeight(FontWeight.Bold)
             .margin({ bottom: 50 });

           // 两个Text组件UI重复计算
           Text(this.firstName + ' ' + this.lastName)
             .margin({ bottom: 8 });
           Text(this.firstName + ' ' + this.lastName);
           Button('changed lastName')
             .margin({ top: 16 })
             .onClick(() => {
               this.lastName += 'a';
             });
         }
         .width('100%')
         .height('100%');
       }
     }
     ```
   * 使用V2计算属性解决重复计算：

     ```ts
     @ComponentV2
     export struct CalculationV2 {
       @Local firstName: string = 'Li';
       @Local lastName: string = 'Hua';

       @Computed
       get fullName() {
         console.info('Computed');
         return this.firstName + ' ' + this.lastName;
       }

       build() {
         Column() {
           Text('使用V2计算属性解决重复计算')
             .fontSize(20)
             .fontWeight(FontWeight.Bold)
             .margin({ bottom: 50 });

           // this.fullName被绑定在两个Text组件上，计算只发生了一次
           Text(this.fullName)
             .margin({ bottom: 8 });
           Text(this.fullName);
           Button('changed lastName')
             .margin({ top: 16 })
             .onClick(() => {
               this.lastName += 'a';
             });
         }
         .width('100%')
         .height('100%');
       }
     }
     ```

   总结：通过V1这种方式，对于前两个Text组件，this.lastName + ' '+ this.firstName这段逻辑被求解了两次。如果UI中有多处重复计算，会产生较大的性能开销。采用V2的话，this.fullName被绑定在两个Text组件上，计算只发生了一次，解决UI多次重用该属性从而重复计算导致的性能问题。
3. **状态变量修改监听：** V2引入的@Monitor状态变量修改监听装饰器，使得状态变量具有深度监听的能力。现有状态管理V1版本无法实现对对象、数组中某一单个属性或数组项变化的监听，且无法获取变化前的值。而V2中@Monitor可以监听深层属性的变化，并能够根据更改前后的值处理。场景案例对比如下：
   * 使用V1中@Watch监听状态变量修改：

     ```ts
     @Observed
     class Info {
       name: string = 'Tom';
       age: number = 25;
     }

     @Component
     export struct ModificationV1 {
       @State @Watch('onInfoChange') info: Info = new Info();

       // 更改info中的name或age属性时，均会触发info注册的@Watch回调
       onInfoChange() {
         console.info(`info after change name: ${this.info.name}, age: ${this.info.age} `);
       }

       build() {
         Column() {
           Text('使用V1中@Watch监听状态变量修改')
             .fontSize(20)
             .fontWeight(FontWeight.Bold);
           Row() {
             Column() {
               Text(`name: ${this.info.name}, age: ${this.info.age}`);
               Button('change info name')
                 .margin({ top: 16 })
                 .onClick(() => {
                   this.info.name = 'Jack';
                 });
               Button('change info age')
                 .margin({ top: 16 })
                 .onClick(() => {
                   this.info.age = 30;
                 });
             }
             .width('100%');
           }
           .height('100%');
         }
         .width('100%')
         .height('100%');
       }
     }
     ```
   * 使用V2中@Monitor监听状态变量修改：

     ```ts
     @ObservedV2
     class Info {
       @Trace name: string = 'Tom';
       @Trace age: number = 25;

       @Monitor('name')
       // 更改name属性时触发此回调
       onNameChange(monitor: IMonitor) {
         console.info(`name change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
       }

       @Monitor('age')
       // 更改age属性时触发此回调
       onAgeChange(monitor: IMonitor) {
         console.info(`age change from ${monitor.value()?.before} to ${monitor.value()?.now}`);
       }

       constructor(name: string, age: number) {
         this.name = name;
         this.age = age;
       }
     }

     @ComponentV2
     export struct ModificationV2 {
       @Local info: Info = new Info('Tom', 25);

       build() {
         Column() {
           Text('使用V2中@Monitor监听状态变量修改')
             .fontSize(20)
             .fontWeight(FontWeight.Bold);
           Row() {
             Column() {
               Text(`name: ${this.info.name}, age: ${this.info.age}`);
               Button('change info name')
                 .margin({ top: 16 })
                 .onClick(() => {
                   this.info.name = 'Jack';
                 });
               Button('change info age')
                 .margin({ top: 16 })
                 .onClick(() => {
                   this.info.age = 30;
                 });
             }
             .width('100%');
           }
           .height('100%');
         }
         .width('100%')
         .height('100%');
       }
     }
     ```

   总结：通过V1这种方式，更改info中的name或age属性时，均会触发info注册的@Watch回调。在这个回调中，由于无法获取数据更改前的值，在业务逻辑更加复杂的场景下，无法准确知道是哪一个属性或元素发生了变化而触发了@Watch事件，这不便于开发者对变量的更改进行准确监听。而对于通过V2的实现方式，准确监听了对象中每个属性的变化及其变化前后的值。
4. **更灵活的装饰器设计：** V2提出使用@Local替代@State，明确区分组件内部状态（不可由外部初始化）。采用@Param表示组件从外部传入的状态，使得父子组件之间的数据能够进行同步，统一了V1中@Prop、@Link等复杂的传参逻辑。为了实现子组件向父组件要求更新@Param装饰变量的能力，V2还提出了@Event装饰器。场景案例对比如下：
   * 使用V1在父子组件之间同步数据：

     ```ts
     @Component
     export struct DecoratorV1 {
       @State title: string = 'Title One';
       @State fontColor: Color = Color.Black;

       build() {
         Column() {
           Text('使用V1在父子组件之间同步数据')
             .fontSize(20)
             .fontWeight(FontWeight.Bold)
             .margin({ bottom: 50 });
           Child({
             title: this.title,
             fontColor: this.fontColor
           });
         }
         .width('100%')
         .height('100%');
       }
     }

     @Component
     struct Child {
       // @Link实现了父子组件双向数据绑定，子组件可以直接修改父组件的状态，可能会导致状态流向不清晰
       @Link title: string;
       @Prop fontColor: Color = Color.Red;

       build() {
         Column() {
           Text(`${this.title}`)
             .fontColor(this.fontColor);
           Button('change to Title Two')
             .margin({ top: 16 })
             .onClick(() => {
               this.changeFactory(2);
             });
           Button('change to Title One')
             .margin({ top: 16 })
             .onClick(() => {
               this.changeFactory(1);
             });
         };
       }

       changeFactory(type: number) {
         if (type == 1) {
           this.title = 'Title One';
         } else if (type == 2) {
           this.title = 'Title Two';
         }
       }
     }
     ```
   * 使用V2在父子组件之间同步数据：

     ```ts
     @ComponentV2
     export struct DecoratorV2 {
       @Local title: string = 'Title One';
       @Local fontColor: Color = Color.Black;

       build() {
         Column() {
           Text('使用V2在父子组件之间同步数据')
             .fontSize(20)
             .fontWeight(FontWeight.Bold)
             .margin({ bottom: 50 });
           Child({
             title: this.title,
             fontColor: this.fontColor,
             changeFactory: (type: number) => {
               if (type == 1) {
                 this.title = 'Title One';
               } else if (type == 2) {
                 this.title = 'Title Two';
               }
             }
           });
         }
         .width('100%')
         .height('100%');
       }
     }

     @ComponentV2
     struct Child {
       // @Param用于单向数据传递，子组件无法直接修改父组件的状态
       @Param title: string = '';
       @Param fontColor: Color = Color.Red;
       // 实现父子组件双向同步的能力，通过事件驱动的方式实现，状态流向更加明确
       @Event changeFactory: (x: number) => void = () => {
       };

       build() {
         Column() {
           Text(`${this.title}`)
             .fontColor(this.fontColor);
           Button('change to Title Two')
             .margin({ top: 16 })
             .onClick(() => {
               this.changeFactory(2);
             });
           Button('change to Title One')
             .margin({ top: 16 })
             .onClick(() => {
               this.changeFactory(1);
             });
         };
       }
     }
     ```

   总结：V1通过@Link实现了父子组件双向数据绑定，子组件可以直接修改父组件的状态，无需额外的事件处理，但可能会导致状态流向不清晰，尤其是在复杂组件中，维护成本较高。而V2使用@Param用于单向数据传递，子组件无法直接修改父组件的状态。为了实现父子组件双向同步的能力，通过事件驱动的方式实现，状态流向更加明确，代码结构更加清晰，维护成本较低。

完整示例：以上代码以自定义组件形式出现，想要成功运行，可参考以下入口示例测试。

```ts
import { NestedV1 } from '../views/Scene1/NestedV1';
import { NestedV2 } from '../views/Scene1/NestedV2';
import { CalculationV1 } from '../views/Scene2/CalculationV1';
import { CalculationV2 } from '../views/Scene2/CalculationV2';
import { ModificationV1 } from '../views/Scene3/ModificationV1';
import { ModificationV2 } from '../views/Scene3/ModificationV2';
import { DecoratorV1 } from '../views/Scene4/DecoratorV1';
import { DecoratorV2 } from '../views/Scene4/DecoratorV2';

@Entry
@Component
struct MainPage {
  @State currentIndexOut: number = 0;
  @State currentIndexIn1: number = 0;
  @State currentIndexIn2: number = 0;
  @State currentIndexIn3: number = 0;
  @State currentIndexIn4: number = 0;

  build() {
    Tabs({ index: this.currentIndexOut }) {
      TabContent() {
        Tabs() {
          TabContent() {
            NestedV1();
          }.tabBar('V1');

          TabContent() {
            NestedV2();
          }.tabBar('V2');
        }
        .height('100%')
        .width('100%')
        .scrollable(false)
        .barMode(BarMode.Fixed)
        .barBackgroundColor('#ffffff')
        .barPosition(BarPosition.Start)
        .onChange((index: number) => {
          this.currentIndexIn1 = index;
        });
      }.tabBar('场景一');

      TabContent() {
        Tabs() {
          TabContent() {
            CalculationV1();
          }.tabBar('V1');

          TabContent() {
            CalculationV2();
          }.tabBar('V2');
        }
        .height('100%')
        .width('100%')
        .scrollable(false)
        .barMode(BarMode.Fixed)
        .barBackgroundColor('#ffffff')
        .barPosition(BarPosition.Start)
        .onChange((index: number) => {
          this.currentIndexIn2 = index;
        });
      }.tabBar('场景二');

      TabContent() {
        Tabs() {
          TabContent() {
            ModificationV1();
          }.tabBar('V1');

          TabContent() {
            ModificationV2();
          }.tabBar('V2');
        }
        .height('100%')
        .width('100%')
        .scrollable(false)
        .barMode(BarMode.Fixed)
        .barBackgroundColor('#ffffff')
        .barPosition(BarPosition.Start)
        .onChange((index: number) => {
          this.currentIndexIn3 = index;
        });
      }.tabBar('场景三');

      TabContent() {
        Tabs() {
          TabContent() {
            DecoratorV1();
          }.tabBar('V1');

          TabContent() {
            DecoratorV2();
          }.tabBar('V2');
        }
        .height('100%')
        .width('100%')
        .scrollable(false)
        .barMode(BarMode.Fixed)
        .barBackgroundColor('#ffffff')
        .barPosition(BarPosition.Start)
        .onChange((index: number) => {
          this.currentIndexIn4 = index;
        });
      }.tabBar('场景四');
    }
    .height('100%')
    .width('100%')
    .scrollable(false)
    .barMode(BarMode.Fixed)
    .barBackgroundColor('#ffffff')
    .barPosition(BarPosition.End)
    .onChange((index: number) => {
      this.currentIndexOut = index;
    });
  }
}
```

**二、****状态管理V2的局限性及注意事项**。

1. **部分场景不支持[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)、[keyframeAnimateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#keyframeanimateto11)动画：** 详情可参考文档[在状态管理V2中使用animateTo动画效果异常](../harmonyos-guides/arkts-new-local.md#在状态管理v2中使用animateto动画效果异常)、[动效场景](../harmonyos-guides/arkts-new-applysync-flushupdates-flushuiupdates.md#动效场景)。
2. **在低版本API中高级组件缺失：** V2版本的部分高级功能在低版本API中未提供，仍在持续优化。例如：DownloadFileButton、ProgressButton、SegmentButton。从API version 18开始，系统预置UI组件支持在状态管理V2组件中使用。
3. **在低版本API中无法自定义局部页面主题：** V2版本在低版本API未提供WithTheme组件，因此无法设置应用局部页面自定义主题风格。从API version 18开始，该接口支持在状态管理V2组件中使用。
4. **在低版本API中组件复用能力受限：** V2版本在低版本API未提供@Reusable装饰器，无法复用自定义组件。因此，如果大量自定义组件从组件树上被移除，组件和其对应的JSView对象无法被放入复用缓存中，后续创建新自定义组件节点时，会消耗大量组件重新创建的时间。从API version 18开始，可以使用@ReusableV2装饰@ComponentV2装饰的自定义组件。

**三、状态管理混用与迁移场景介绍**。

1. **混用场景介绍**。

   从实际角度出发，V1提出时间较早，有很大的基础，开发者无法一次性迁移成V2，因此在V1的代码中使用V2的部分能力是允许的，V2中也没有完全禁止V1。状态管理V1与V2的混用开发可以参考[状态管理V1V2混用文档](../harmonyos-guides/v1v2-mixing.md)。API19新增的[makeV1Observed](../harmonyos-guides/arkts-v1-v2-mixusage.md#makev1observed)以及[enableV2Compatibility](../harmonyos-guides/arkts-v1-v2-mixusage.md#enablev2compatibility)接口完善了V1与V2混用能力。
2. **迁移场景介绍**。

   对希望将现有V1应用迁移到V2的开发者，可参考[V1V2能力对比及迁移简表](../harmonyos-guides/arkts-v1-v2-migration.md#v1与v2能力对照迁移表)进行迁移，更详细的装饰器迁移示例可参考[状态管理V1向V2迁移场景](../harmonyos-guides/arkts-state-management-v1-v2-migration-guide.md)。

## 常见FAQ

Q：@Event能实现的功能@Param都能实现，那为什么还要引入@Event？

A：一般来说，@Param主要用于变量传递，@Event用于函数传递，数据流向不一样，@Param是父传子，子组件不能更改父组件传递的数据，@Event是触发父组件更新数据。即使@Param传递的是函数，也必须赋初始值，而@Event不用初始化。

Q：AppStorage和AppStorageV2以及PersistentStorage和PersistentStorageV2是互通的吗？

A：AppStorage与AppStorageV2之间的数据互不共享，详情请参考[AppStorageV2: 应用全局UI状态存储](../harmonyos-guides/arkts-new-appstoragev2.md)。

没有PersistentStorageV2，只有PersistenceV2，PersistentStorage和PersistenceV2存在差别，PersistentStorage功能上耦合了AppStorage，并且数据在不同module中使用也会有问题，因此推荐使用PersistenceV2的globalConnect接口替换掉PersistentStorage的persistProp接口。
