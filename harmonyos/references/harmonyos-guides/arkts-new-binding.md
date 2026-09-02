---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-new-binding
title: "!!语法：双向绑定"
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 语法糖 > !!语法：双向绑定
category: harmonyos-guides
scraped_at: 2026-09-02T14:59:16+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:8b6fe3ce5bb2757c773873fc7836f1f862e7d949b7c2f3a967559f0c720c4b29
---

在状态管理V1中，推荐使用[$$](arkts-two-way-sync.md)实现系统组件的双向绑定。

在状态管理V2中，推荐使用!!语法糖统一处理双向绑定。

**说明** 

!!语法从API version 12开始支持。

## 概述

!!双向绑定语法，是一个语法糖，方便开发者实现数据双向绑定，用于初始化子组件的[@Param](arkts-new-param.md)装饰的属性和[@Event](arkts-new-event.md)装饰的事件。其中@Event方法名需要声明为“$”+ @Param属性名，详见[使用场景](arkts-new-binding.md#使用场景)。

* 如果使用了!!双向绑定语法，表明父组件的变化会同步给子组件，子组件的变化也会同步给父组件。
* 父组件未使用!!时，变化是单向的。

## 使用场景

### 自定义组件间双向绑定

1. 在Index中构造Star子组件，双向绑定父子组件中的value属性，并初始化子组件的@Param value和@Event $value。

   @Param与@Event装饰器配合使用的双向绑定语法糖。

   ```typescript
   Star({ value: this.value, $value: (val: number) => { this.value = val; } })
   ```

   上述语法可以简化为!!双向绑定语法糖。

   ```typescript
   Star({ value: this.value!! })
   ```
2. 使用@Param value与@Event $value语法实现自定义组件双向绑定。

   ```typescript
   @Entry
   @ComponentV2
   struct Index {
     @Local value: number = 0;

     build() {
       Column() {
         Text(`${this.value}`)
         // 点击Index中的Button改变value值，父组件Index和子组件Star中的Text将同步更新。
         Button(`change value in parent component`).onClick(() => {
           this.value++;
         })
         // 使用@Param与@Event语法实现自定义组件双向绑定。
         Star({ value: this.value, $value: (val: number) => { this.value = val; } })
         // ...
       // ...
       }
     }
   }

   @ComponentV2
   struct Star {
     @Param value: number = 0;
     @Event $value: (val: number) => void = (val: number) => {};

     build() {
       Column() {
         Text(`${this.value}`)
         // 点击子组件Star中的Button，调用`this.$value(10)`方法，父组件Index和子组件Star中的Text将同步更新。
         Button(`change value in child component`).onClick(() => {
           this.$value(10);
         })
       }
     }
   }
   ```
3. 使用!!语法糖实现自定义组件双向绑定。

   ```typescript
   @Entry
   @ComponentV2
   struct Index {
     @Local value: number = 0;

     build() {
       Column() {
         Text(`${this.value}`)
         // 点击Index中的Button改变value值，父组件Index和子组件Star中的Text将同步更新。
         Button(`change value in parent component`).onClick(() => {
           this.value++;
         })
         // 使用!!语法糖实现自定义组件双向绑定。
         Star({ value: this.value!! })
         // ...
       }
     }
   }

   @ComponentV2
   struct Star {
     @Param value: number = 0;
     @Event $value: (val: number) => void = (val: number) => {};

     build() {
       Column() {
         Text(`${this.value}`)
         // 点击子组件Star中的Button，调用`this.$value(10)`方法，父组件Index和子组件Star中的Text将同步更新。
         Button(`change value in child component`).onClick(() => {
           this.$value(10);
         })
       }
     }
   }
   ```

**使用限制**

* !!双向绑定语法不支持多层父子组件传递。
* 不支持与@Event混用。从API version 18开始，当使用!!双向绑定语法给子组件传递参数时，给对应的@Event方法传参会编译报错。
* 当使用3个或更多感叹号（!!!、!!!!、!!!!!等）时，不支持双向绑定功能。

### 系统组件参数双向绑定

!!运算符为系统组件提供TS变量的引用，使得TS变量和系统组件的内部状态保持同步。添加方式是在变量名后添加，例如isShow!!。

内部状态的含义由组件或属性决定。例如：[bindMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu11)属性的isShow参数。

```typescript
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG: string = 'click show Menu';
const DOMAIN = 0xFF00;

@Entry
@ComponentV2
struct BindMenuInterface {
  @Local isShow: boolean = false;

  build() {
    Column() {
      Row() {
        Text('click show Menu')
          .bindMenu(this.isShow!!, // 双向绑定。
            [
              {
                value: 'Menu1',
                action: () => {
                  hilog.info(DOMAIN, TAG, 'handle Menu1 click');
                }
              },
              {
                value: 'Menu2',
                action: () => {
                  hilog.info(DOMAIN, TAG, 'handle Menu2 click');
                }
              },
            ])
      }.height('50%')
      
      Text('isShow: ' + this.isShow).fontSize(18).fontColor(Color.Red)
      Row() {
        Button('Click')
          .onClick(() => {
            this.isShow = true;
          })
          .width(100)
          .fontSize(20)
          .margin(10)
      }
    }.width('100%')
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/PFiQbwdxTEiZOfSYvQOD3Q/zh-cn_image_0000002736432453.gif)

**使用规则**

* 当前!!双向绑定支持基础类型变量，当该变量使用[@State](arkts-state.md)等状态管理V1装饰器装饰，或者[@Local](arkts-new-local.md)等状态管理V2装饰器装饰时，变量值的变化会触发UI刷新。

  | 属性 | 支持的参数 | 起始API版本 |
  | --- | --- | --- |
  | [bindMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindmenu11) | isShow | 18 |
  | [bindContextMenu](../harmonyos-references/ts-universal-attributes-menu.md#bindcontextmenu12) | isShown | 18 |
  | [bindPopup](../harmonyos-references/ts-universal-attributes-popup.md#bindpopup) | show | 18 |
  | [TextInput](../harmonyos-references/ts-basic-components-textinput.md#textinputoptions对象说明) | text | 18 |
  | [TextArea](../harmonyos-references/ts-basic-components-textarea.md#textareaoptions对象说明) | text | 18 |
  | [Search](../harmonyos-references/ts-basic-components-search.md#searchoptions18对象说明) | value | 18 |
  | [bindSheet](../harmonyos-references/ts-universal-attributes-sheet-transition.md#bindsheet) | isShow | 18 |
  | [bindContentCover](../harmonyos-references/ts-universal-attributes-modal-transition.md#bindcontentcover) | isShow | 18 |
  | [SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md) | [sideBarWidth](../harmonyos-references/ts-container-sidebarcontainer.md#sidebarwidth) | 18 |
  | [Navigation](../harmonyos-references/ts-basic-components-navigation.md) | [navBarWidth](../harmonyos-references/ts-basic-components-navigation.md#navbarwidth9) | 18 |
  | [Toggle](../harmonyos-references/ts-basic-components-toggle.md#toggleoptions18对象说明) | isOn | 18 |
  | [Checkbox](../harmonyos-references/ts-basic-components-checkbox.md) | [select](../harmonyos-references/ts-basic-components-checkbox.md#select) | 18 |
  | [CheckboxGroup](../harmonyos-references/ts-basic-components-checkboxgroup.md) | [selectAll](../harmonyos-references/ts-basic-components-checkboxgroup.md#selectall) | 18 |
  | [Radio](../harmonyos-references/ts-basic-components-radio.md) | [checked](../harmonyos-references/ts-basic-components-radio.md#checked) | 18 |
  | [Rating](../harmonyos-references/ts-basic-components-rating.md#ratingoptions18对象说明) | rating | 18 |
  | [Slider](../harmonyos-references/ts-basic-components-slider.md#slideroptions对象说明) | value | 18 |
  | [Select](../harmonyos-references/ts-basic-components-select.md) | [selected](../harmonyos-references/ts-basic-components-select.md#selected) | 18 |
  | Select | [value](../harmonyos-references/ts-basic-components-select.md#value) | 18 |
  | [MenuItem](../harmonyos-references/ts-basic-components-menuitem.md) | [selected](../harmonyos-references/ts-basic-components-menuitem.md#selected) | 18 |
