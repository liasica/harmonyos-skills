---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-920
title: 系统组件双向同步语法对深层对象是否兼容
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 系统组件双向同步语法对深层对象是否兼容
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8ac0199a9883085381ccd31a9db0b1b839617f8fa6d0e1ef82f329ae855be7ed
---

## 问题现象

系统组件双向同步语法是否兼容深层嵌套对象？

## 背景知识

* [$$语法：系统组件双向同步](../harmonyos-guides/arkts-two-way-sync.md)：$$运算符为系统组件提供TS变量的引用，使得TS变量和系统组件的内部状态保持同步。
* [!!语法：双向绑定](../harmonyos-guides/arkts-new-binding.md)：在状态管理V1中，使用$$实现系统组件的双向绑定。在状态管理V2中，使用!!语法糖统一处理双向绑定。

## 解决方案

ArkUI完全支持深层对象的双向同步，可以通过以下两种方案来实现：

1. 方案一：在状态管理V1中，推荐使用[$$](../harmonyos-guides/arkts-two-way-sync.md)实现系统组件的双向绑定。
   * 当前$$支持基础类型变量，当该变量使用@State、@Link、@Prop、@Provide等状态管理V1装饰器装饰，或者@Local等状态管理V2装饰器装饰时，变量值的变化会触发UI刷新。
   * 当前$$支持的组件：

     | 组件 | 支持的参数/属性 | 起始API版本 |
     | --- | --- | --- |
     | [Checkbox](../harmonyos-references/ts-basic-components-checkbox.md) | select | 10 |
     | [CheckboxGroup](../harmonyos-references/ts-basic-components-checkboxgroup.md) | selectAll | 10 |
     | [DatePicker](../harmonyos-references/ts-basic-components-datepicker.md) | selected | 10 |
     | [TimePicker](../harmonyos-references/ts-basic-components-timepicker.md) | selected | 10 |
     | [MenuItem](../harmonyos-references/ts-basic-components-menuitem.md) | selected | 10 |
     | [Panel](../harmonyos-references/ts-container-panel.md) | mode | 10 |
     | [Radio](../harmonyos-references/ts-basic-components-radio.md) | checked | 10 |
     | [Rating](../harmonyos-references/ts-basic-components-rating.md) | rating | 10 |
     | [Search](../harmonyos-references/ts-basic-components-search.md) | value | 10 |
     | [SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md) | showSideBar | 10 |
     | [Slider](../harmonyos-references/ts-basic-components-slider.md) | value | 10 |
     | [Stepper](../harmonyos-references/ts-basic-components-stepper.md) | index | 10 |
     | [Swiper](../harmonyos-references/ts-container-swiper.md) | index | 10 |
     | [Tabs](../harmonyos-references/ts-container-tabs.md) | index | 10 |
     | [TextArea](../harmonyos-references/ts-basic-components-textarea.md) | text | 10 |
     | [TextInput](../harmonyos-references/ts-basic-components-textinput.md) | text | 10 |
     | [TextPicker](../harmonyos-references/ts-basic-components-textpicker.md) | selected、value | 10 |
     | [Toggle](../harmonyos-references/ts-basic-components-toggle.md) | isOn | 10 |
     | [AlphabetIndexer](../harmonyos-references/ts-container-alphabet-indexer.md) | selected | 10 |
     | [Select](../harmonyos-references/ts-basic-components-select.md) | selected、value | 10 |
     | [BindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet) | isShow | 10 |
     | [BindContentCover](../harmonyos-references/ts-universal-attributes-modal-transition.md#bindcontentcover) | isShow | 10 |
     | [Refresh](../harmonyos-references/ts-container-refresh.md) | refreshing | 8 |
     | [GridItem](../harmonyos-references/ts-container-griditem.md) | selected | 10 |
     | [ListItem](../harmonyos-references/ts-container-listitem.md) | selected | 10 |

   示例代码如下：

   ```screen
   @Component
   struct SyncPage {
     @State model: modelFirst = new modelFirst();
     @State message: string = '';

     build() {
       Column({ space: 20 }) {
         Text(this.message);
         TextInput({ text: $$this.model.modelThird.modelForth })
           .placeholderColor(Color.Grey)
           .placeholderFont({ size: 14, weight: 400 })
           .caretColor(Color.Blue)
           .width(300)
           .onChange(() => {
             this.message = this.model.modelThird.modelForth;
           });
       }.width('100%').justifyContent(FlexAlign.Center);
     }
   }
   ```

   实体类：

   ```screen
   interface ModelInterfaceFir {
     modelForth: string;
   }

   export class modelFirst {
     modelFirst: string = '';
     modelSecond: number = 0;
     modelThird: ModelInterfaceFir = { modelForth: 'modelForth' };
   }
   ```
2. 方案二：在状态管理V2中，推荐使用[!!](../harmonyos-guides/arkts-two-way-sync.md)语法糖统一处理双向绑定。
   * !!双向绑定语法不支持多层父子组件传递。
   * 不支持与@Event混用。从API version 18开始，当使用!!双向绑定语法给子组件传递参数时，给对应的@Event方法传参会编译报错。
   * 当使用3个或更多感叹号（!!!、!!!!、!!!!!等）时，不支持双向绑定功能。

   示例代码如下：

   ```screen
   @ComponentV2
   struct LocalChangePage {
     @Param model: modelSecond = new modelSecond('modelFirst', 10, new ModelInterfaceSec('modelForth'), new ModelIn(10));
     @Event $value: (val: modelSecond) => void = () => {
     };
     message: string = '';

     build() {
       Column({ space: 20 }) {
         Text(this.model.modelThird.modelForth);
         TextInput({ text: this.model.modelThird.modelForth!! })
           .placeholderColor(Color.Grey)
           .placeholderFont({ size: 14, weight: 400 })
           .caretColor(Color.Blue)
           .width(300)
           .onChange(() => {
             this.message = this.model.modelThird.modelForth;
           });
       };
     };
   }
   ```

   实体类：

   ```screen
   @ObservedV2
   export class ModelInterfaceSec {
     @Trace
     modelForth: string;

     constructor(modelForth: string) {
       this.modelForth = modelForth;
     }
   }

   @ObservedV2
   export class ModelIn {
     @Trace
     modelFifth: number;

     constructor(modelFifth: number) {
       this.modelFifth = modelFifth;
     }
   }

   @ObservedV2
   export class modelSecond {
     @Trace
     modelFirst: string = '';
     @Trace
     modelSecond: number = 0;
     @Trace
     modelThird: ModelInterfaceSec = new ModelInterfaceSec('modelForth');
     @Trace
     modelSixth: ModelIn = new ModelIn(10);

     constructor(modelFirst: string, modelSecond: number, modelThird: ModelInterfaceSec, modelSixth: ModelIn) {
       this.modelFirst = modelFirst;
       this.modelSecond = modelSecond;
       this.modelThird = modelThird;
       this.modelSixth = modelSixth;
     }
   }
   ```

   全量代码如下：

   ```screen
   interface ModelInterfaceFir {
     modelForth: string;
   }

   export class modelFirst {
     modelFirst: string = '';
     modelSecond: number = 0;
     modelThird: ModelInterfaceFir = { modelForth: 'modelForth' };
   }

   @ObservedV2
   export class ModelInterfaceSec {
     @Trace
     modelForth: string;

     constructor(modelForth: string) {
       this.modelForth = modelForth;
     }
   }

   @ObservedV2
   export class ModelIn {
     @Trace
     modelFifth: number;

     constructor(modelFifth: number) {
       this.modelFifth = modelFifth;
     }
   }

   @ObservedV2
   export class modelSecond {
     @Trace
     modelFirst: string = '';
     @Trace
     modelSecond: number = 0;
     @Trace
     modelThird: ModelInterfaceSec = new ModelInterfaceSec('modelForth');
     @Trace
     modelSixth: ModelIn = new ModelIn(10);

     constructor(modelFirst: string, modelSecond: number, modelThird: ModelInterfaceSec, modelSixth: ModelIn) {
       this.modelFirst = modelFirst;
       this.modelSecond = modelSecond;
       this.modelThird = modelThird;
       this.modelSixth = modelSixth;
     }
   }

   @Entry
   @ComponentV2
   struct LineBreakStrategyExample {
     build() {
       Column() {
         Column({ space: 15 }) {
           Text('方案一');
           SyncPage();
         }
         .height('50%')
         .margin({
           top: 30
         });

         Column({ space: 15 }) {
           Text('方案二');
           LocalChangePage();
         }
         .height('50%');
       };
     }
   }

   @ComponentV2
   struct LocalChangePage {
     @Param model: modelSecond = new modelSecond('modelFirst', 10, new ModelInterfaceSec('modelForth'), new ModelIn(10));
     @Event $value: (val: modelSecond) => void = () => {
     };
     message: string = '';

     build() {
       Column({ space: 20 }) {
         Text(this.model.modelThird.modelForth);
         TextInput({ text: this.model.modelThird.modelForth!! })
           .placeholderColor(Color.Grey)
           .placeholderFont({ size: 14, weight: 400 })
           .caretColor(Color.Blue)
           .width(300)
           .onChange(() => {
             this.message = this.model.modelThird.modelForth;
           });
       };
     };
   }

   @Component
   struct SyncPage {
     @State model: modelFirst = new modelFirst();
     @State message: string = '';

     build() {
       Column({ space: 20 }) {
         Text(this.message);
         TextInput({ text: $$this.model.modelThird.modelForth })
           .placeholderColor(Color.Grey)
           .placeholderFont({ size: 14, weight: 400 })
           .caretColor(Color.Blue)
           .width(300)
           .onChange(() => {
             this.message = this.model.modelThird.modelForth;
           });
       }.width('100%').justifyContent(FlexAlign.Center);
     }
   }
   ```
