---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1078
title: "@Builder装饰器参数传递限制与使用方式介绍"
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > @Builder装饰器参数传递限制与使用方式介绍
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c556358d5b08e13dbf01a172cf5da72aa1072f73a81f14b15c9a1dba11f254e1
---

## 问题现象

ArkUI提供@Builder装饰器来实现轻量UI元素复用，@Builder装饰器适用于哪些场景以及有哪些限制？

## 背景知识

[@Builder装饰器](../harmonyos-guides/arkts-builder.md)用于封装可复用的UI结构，通过提取重复的布局代码提高开发效率。该装饰器严格禁止在其内部定义状态变量或使用生命周期函数，全局自定义构建函数必须通过参数传递的方式完成数据交互，私有自定义构建函数可以在函数内通过this直接调用Component组件内的变量。

## 解决方案

**一、@Builder装饰器使用方式介绍：**

| 适用范围 | 参数传递 | 参数改变时，是否可以UI刷新 |
| --- | --- | --- |
| 私有自定义构建函数 | 按值传递 | 不可以 |
| 按引用传递 | 可以 |
| 按回调传递参数 | 可以 |
| 全局自定义构建函数 | 按值传递 | 不可以 |
| 按引用传递 | 可以 |
| 按回调传递参数 | 可以 |

1. 私有自定义构建函数-按值传递：在自定义组件内部构建函数，调用@Builder装饰的函数默认按值传递。示例代码：

   ```ts
   @Entry
   @Component
   struct PrivateValueCopyConstructor {
     // 在自定义组件内部

     // 无参数
     @Builder
     showTextBuilder() {
       Text('Hello World');
     }

     // 有参数
     @Builder
     showTextValueBuilder(param: string) {
       Text(param);
     }

     build() {
       Column() {
         // 无参数
         this.showTextBuilder();
         // 有参数
         this.showTextValueBuilder('Hello @Builder');
       };
     }
   }
   ```
2. 私有自定义构建函数-按引用传递：在自定义组件内部构建函数，当传入一个参数且该参数直接传入对象字面量时会触发按引用传递。示例代码：

   ```ts
   class TmpPrivateReferenceCopyConstructor {
     param: string = '';
   }

   @Entry
   @Component
   struct PrivateReferenceCopyConstructor {
     // 在自定义组件内部
     @Builder
     showTextBuilder(tmp: TmpPrivateReferenceCopyConstructor) {
       Row() {
         Text(`UseStateVarByReference: ${tmp.param} `);
       };
     }

     build() {
       Column() {
         // 按引用传递
         this.showTextBuilder({ param: 'hihi' });
       };
     }
   }
   ```
3. 私有自定义构建函数-按回调传递参数：在自定义组件内部构建函数，可以是状态变量刷新Builder且传入额外回调后能在Builder内修改状态变量。示例代码：

   ```ts
   import { Binding, MutableBinding, UIUtils } from '@kit.ArkUI';

   @Entry
   @ComponentV2
   struct PrivateCallBackConstructor {
     @Local numberOne: number = 5;
     @Local numberTwo: number = 12;

     @Builder
     PrivateCallBackBuilder(numOne: Binding<number>, numTwo: MutableBinding<number>) {
       Row() {
         Column() {
           Text(`numberOne: ${numOne.value}, numberTwo: ${numTwo.value}`);
           Button(`only change numberTwo`)
             .onClick(() => {
               // 赋值MutableBinding类型传递该修改到父组件中。
               numTwo.value += 1;
             });
         };
       };
     }

     build() {
       Column() {
         Button(`change numberOne and numberTwo`)
           .onClick(() => {
             this.numberOne++;
             this.numberTwo++;
           });
         this.PrivateCallBackBuilder(
           // 使用makeBinding传入参数，需要传入读回调，返回Binding类型，支持@Builder内组件UI刷新。
           UIUtils.makeBinding<number>(() => this.numberOne),
           // makeBinding额外传入写回调时返回MutableBinding类型，支持@Builder内组件UI刷新并且同步属性修改。
           UIUtils.makeBinding<number>(
             () => this.numberTwo,
             (val: number) => {
               this.numberTwo = val;
             })
         );
       };
     }
   }
   ```
4. 全局自定义构建函数-按值传递：在全局定义的构建函数，允许在build函数和其他自定义构建函数中调用。调用@Builder装饰的函数默认按值传递。示例代码：

   ```ts
   @Entry
   @Component
   struct PublicValueCopyConstructor {
     build() {
       Column() {
         // 无参数
         showTextBuilderPublic();
         // 有参数
         showTextValueBuilderPublic('Hello @Builder');
       };
     }
   }

   // 全局定义

   // 无参数
   @Builder
   function showTextBuilderPublic() {
     Text('Hello World');
   }

   // 有参数
   @Builder
   function showTextValueBuilderPublic(param: string) {
     Text(param);
   }
   ```
5. 全局自定义构建函数-按引用传递：在全局定义的构建函数，当传入一个参数且该参数直接传入对象字面量时会触发按引用传递。示例代码：

   ```ts
   class TmpPublicReferenceCopyConstructor {
     param: string = '';
   }

   @Entry
   @Component
   struct PublicReferenceCopyConstructor {
     build() {
       Column() {
         // 按引用传递
         showTextBuilder({ param: 'hihi' });
       };
     }
   }

   // 全局定义
   @Builder
   function showTextBuilder(tmp: TmpPublicReferenceCopyConstructor) {
     Row() {
       Text(`UseStateVarByReference: ${tmp.param} `);
     };
   }
   ```
6. 全局自定义构建函数-按回调传递参数：在自定义组件内部构建函数，可以是状态变量刷新Builder且传入额外回调后能在Builder内修改状态变量。示例代码：

   ```ts
   import { Binding, MutableBinding, UIUtils } from '@kit.ArkUI';

   @Builder
   function PublicCallBackBuilder(numOne: Binding<number>, numTwo: MutableBinding<number>) {
     Row() {
       Column() {
         Text(`numberOne: ${numOne.value}, numberTwo: ${numTwo.value}`);
         Button(`only change numberTwo`)
           .onClick(() => {
             // 赋值MutableBinding类型传递该修改到父组件中。
             numTwo.value += 1;
           });
       };
     };
   }

   @Entry
   @ComponentV2
   struct PublicCallBackConstructor {
     @Local numberOne: number = 5;
     @Local numberTwo: number = 12;

     build() {
       Column() {
         Button(`change numberOne and numberTwo`)
           .onClick(() => {
             this.numberOne++;
             this.numberTwo++;
           });
         PublicCallBackBuilder(
           // 使用makeBinding传入参数，需要传入读回调，返回Binding类型，支持@Builder内组件UI刷新。
           UIUtils.makeBinding<number>(() => this.numberOne),
           // makeBinding额外传入写回调时返回MutableBinding类型，支持@Builder内组件UI刷新并且同步属性修改。
           UIUtils.makeBinding<number>(
             () => this.numberTwo,
             (val: number) => {
               this.numberTwo = val;
             })
         );
       };
     }
   }
   ```

总结：@Builder装饰器有两种使用方式，分别是定义在自定义组件内部的私有自定义构建函数和定义在全局的全局自定义构建函数。自定义构建函数的参数传递有按值传递、按引用传递、以及按回调传递三种，按值传递时状态变量的改变不会触发UI刷新，所以当使用状态变量的时候，推荐使用按回调传递或按引用传递。

**二、@Builder装饰器参数传递限制**：

1. 在@Builder装饰的函数内部，不允许改变参数值。@Builder装饰的函数内部不允许修改参数值，否则框架会抛出运行时错误，错误码[140109](../harmonyos-references/errorcode-statemanagement.md#section140109-builder非法触发参数属性赋值)。错误示例如下：

   ```ts
   class TmpErrorChangeValue {
     param: string = '';
   }

   @Entry
   @Component
   struct ErrorChangeValue {
     @Builder
     showTextBuilder(tmp: TmpErrorChangeValue) {
       Row() {
         Text(`UseStateVarByReference: ${tmp.param} `)
           .onClick(() => {
             // 修改对象属性值
             tmp.param = 'dddddddd';
           });
       };
     }

     build() {
       Column() {
         // 引用传递
         this.showTextBuilder({ param: 'hello' });
       };
     }
   }
   ```
2. @Builder按引用传递且仅传入一个参数时，且参数必须按照对象字面量的形式，把所需属性一一传入，才会触发动态渲染UI。触发UI渲染的条件较苛刻，缺一不可。以下分别展示，未满足条件导致UI渲染失败的案例：
   * @Builder参数为按值传递，UI刷新失败。

     ```ts
     @Entry
     @Component
     struct ErrorInValuePassing {
       @State myParam: string = '我的自定义';

       // 在自定义组件内部
       @Builder
       showTextBuilder(tmp: string) {
         Row() {
           Text(`UseStateVarByReference: ${tmp} `);
         };
       }

       build() {
         Column() {
           Text(`UseStateVarByReference: ${this.myParam} `);
           this.showTextBuilder(this.myParam);
           Button('修改我的自定义').onClick(() => {
             this.myParam = '修改后我的自定义';
           });
         };
       }
     }
     ```
   * @Builder同时传入多个参数，UI刷新失败。

     ```ts
     class TmpErrorMultipleParameters {
       param: string = '';
     }

     @Entry
     @Component
     struct ErrorMultipleParameters {
       @State myParam: string = '我的自定义';

       // 在自定义组件内部,同时传入多个参数
       @Builder
       showTextBuilder(tmp: TmpErrorMultipleParameters, size: number) {
         Row() {
           Text(`UseStateVarByReference: ${tmp.param},${size} `);
         };
       }

       build() {
         Column() {
           Text(`UseStateVarByReference: ${this.myParam} `);
           // 多个参数
           this.showTextBuilder({ param: this.myParam }, 12);

           Button('修改我的自定义').onClick(() => {
             this.myParam = '修改后我的自定义';
           });
         };
       }
     }
     ```
   * @Builder采用构造方法创建对象作为实参，UI刷新失败。

     ```ts
     class TmpErrorObjectConstruction {
       param: string = '默认值';

       constructor(param: string) {
         this.param = param;
       }
     }

     @Entry
     @Component
     struct ErrorObjectConstruction {
       @State myParam: string = '我的自定义';

       // 在自定义组件内部
       @Builder
       showTextBuilder(tmp: TmpErrorObjectConstruction) {
         Row() {
           Text(`UseStateVarByReference: ${tmp.param} `);
         };
       }

       build() {
         Column() {
           Text(`UseStateVarByReference: ${this.myParam} `);
           // 使用构造方法，创建对象
           this.showTextBuilder(new TmpErrorObjectConstruction(this.myParam));

           Button('修改我的自定义').onClick(() => {
             this.myParam = '修改后我的自定义';
           });
         };
       }
     }
     ```

总结：@Builder装饰器的参数必须按照对象字面量的形式，把所需属性一一传入，才会触发动态渲染UI。即如果需要传入状态变量实现刷新，需要将状态变量封装成对象的属性；如果需要传递多个参数，也需要将多余的参数封装成对象。正确的示例代码为：

```ts
class Tmp {
  param: string = '默认值';
  // 多余的参数，封装到类中
  size: number = 0;
}

@Entry
@Component
struct CorrectImplementationExample {
  @State myParam: string = '我的自定义';

  // 在自定义组件内部
  @Builder
  showTextBuilder(tmp: Tmp) {
    Row() {
      Text(`UseStateVarByReference: ${tmp.param} `)
        .fontSize(tmp.size);
    };
  }

  build() {
    Column({ space: 10 }) {
      Text(`UseStateVarByReference: ${this.myParam} `);
      // 对象字面量  状态变量封装至对象中
      this.showTextBuilder({ param: this.myParam, size: 18 });

      Button('修改我的自定义').onClick(() => {
        this.myParam = '修改后我的自定义';
      });
    }.width('100%')
    .height('100%');
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/YQnOxhbNRq2V0SoL_bmjAA/zh-cn_image_0000002658806605.png "点击放大")

## 常见FAQ

Q：@Builder组件UI不刷新，该如何排查？

A：@Builder的参数必须按照对象字面量的形式，把所需属性一一传入，才会触发动态渲染UI。因此需要排查传入的参数是否为按值传递、是否传入多个参数、是否以对象字面量形式传入参数。

Q：@Builder如何给参数设置默认值？

A：可以给@Builder修饰的函数按照showTextBuilder(size: number = 2)的形式设置默认值。

Q：wrapBuilder封装的全局自定义构建函数UI不刷新的原因是什么？

A：详情查看上文@Builder装饰器使用方式介绍，检查是否使用的值传递导致的不刷新。

Q：@Builder编译错误“Object literal must correspond to some explicitly declared class or interface”？

A：使用了未明确声明类型的对象字面量，需要保证引用传递的对象字面量有对应的class或interface声明。

Q：使用@Builder装饰器包含自定义组件的方法与普通方法的区别是什么？

A：普通方法中不使用@Builder装饰，无法容纳UI组件。
