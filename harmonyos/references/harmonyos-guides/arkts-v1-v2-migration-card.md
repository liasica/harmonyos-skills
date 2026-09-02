---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-v1-v2-migration-card
title: 卡片状态变量迁移
breadcrumb: 指南 > 应用框架 > ArkUI（方舟UI框架） > UI开发 (ArkTS声明式开发范式) > 学习UI范式状态管理 > 状态管理V1-V2迁移指导 > 状态管理V1向V2迁移场景 > 卡片状态变量迁移
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:48+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:bda154d5c9741c8f4f4b305e2387671670dd2dc54b51aded77da6fd3a6c46642
---

从API version 23开始，ArkTS卡片支持使用状态管理V2开发，建议开发者使用[V2装饰器](arkts-state-management-overview.md#装饰器总览-1)替代[V1装饰器](arkts-state-management-overview.md#装饰器总览)进行状态管理，以获得更优的组件渲染性能和状态同步能力。

卡片的状态管理迁移与普通应用页面基本一致，组件内、数据对象等通用场景的迁移可参见[组件内状态变量迁移](arkts-v1-v2-migration-inner-component.md)和[数据对象状态变量迁移](arkts-v1-v2-migration-inner-class.md)。本文仅针对卡片独有的差异点进行说明，即卡片提供方与卡片UI之间的数据接收机制。

场景对比表格如下：

| 卡片场景 | V1装饰器 | V2装饰器 |
| --- | --- | --- |
| 卡片入口组件 | [@Component](arkts-create-custom-components.md#component) | [@ComponentV2](arkts-create-custom-components.md#componentv2) |
| 接收卡片提供方刷新数据 | [@LocalStorageProp](arkts-localstorage.md#localstorageprop) | [@Local](arkts-new-local.md)、[@Provider](arkts-new-provider-and-consumer.md)等 |
| 卡片内部状态变量 | [@State](arkts-state.md) | [@Local](arkts-new-local.md) |
| 嵌套数据对象 | [@Observed](arkts-observed-and-objectlink.md)/[@ObjectLink](arkts-observed-and-objectlink.md) | [@ObservedV2](arkts-new-observedv2-and-trace.md)/[@Trace](arkts-new-observedv2-and-trace.md) |

## 卡片数据接收机制差异

卡片UI（widget页面）运行在系统的卡片渲染服务进程中，与卡片提供方应用（FormExtensionAbility）相互独立。两者之间的数据交互只能通过[updateForm](../harmonyos-references/js-apis-app-form-formprovider.md#formproviderupdateform)接口实现：卡片提供方调用updateForm推送数据，卡片UI接收数据后刷新界面。

V1与V2在数据接收上的核心差异在于匹配规则：

* V1：卡片UI通过[@LocalStorageProp](arkts-localstorage.md#localstorageprop)接收刷新数据。匹配依据是@LocalStorageProp装饰器的入参key值，即@LocalStorageProp('title')匹配updateForm数据中key为'title'的字段。卡片入口组件需要使用@Entry(storage)传入LocalStorage实例。
* V2：卡片UI支持通过@Local、@Provider等可被通知的状态装饰器直接接收刷新数据。匹配依据是变量名，即@Local title匹配updateForm数据中key为'title'的字段。卡片入口组件使用@Entry即可，无需再传入LocalStorage实例。

## 限制条件

* 卡片仅支持[ArkTS声明式开发范式](arkts-ui-widget-page-overview.md)的部分组件、事件、动效、数据管理和状态管理能力。开发时请留意相关接口是否标注"卡片能力"（如：从API version 12开始，该接口支持在ArkTS卡片中使用）。
* 卡片支持的状态管理V2装饰器以接口标注的"卡片能力"为准。若某V2接口未标注支持在ArkTS卡片中使用，则在卡片中不可用。
* 卡片入口组件迁移为[@ComponentV2](arkts-create-custom-components.md#componentv2)后，@ComponentV2不支持LocalStorage相关能力。卡片场景下，支持通过变量名将updateForm刷新数据直接通知到@Local、@Provider等V2状态装饰器，因此卡片入口组件无需再使用LocalStorage。
* 更多卡片开发约束请参见[ArkTS卡片概述](arkts-form-overview.md#约束与限制)。

## 卡片数据接收迁移

**迁移规则：**

* 入口组件由@Entry(storage) @Component迁移为@Entry @ComponentV2，不再需要创建和传入LocalStorage实例。
* @LocalStorageProp按需迁移为@Local（组件内使用）或@Provider（需跨组件共享）等V2状态装饰器。
* 迁移时需确保V2装饰器的变量名与卡片提供方updateForm推送数据的key值一致。若原V1代码中@LocalStorageProp的入参key与变量名不同，迁移时应统一为相同名称。
* 卡片提供方FormExtensionAbility的updateForm调用逻辑无需改动。

以卡片主动刷新场景为例：卡片上展示标题和详情信息，点击刷新按钮后通过[postCardAction](../harmonyos-references/js-apis-postcardaction.md#postcardaction-1)触发message事件，FormExtensionAbility在[onFormEvent](../harmonyos-references/js-apis-app-form-formextensionability.md#formextensionabilityonformevent)回调中调用updateForm刷新卡片数据。

**V1实现代码如下：**

卡片入口组件使用@Entry(storage)传入LocalStorage，并通过@LocalStorageProp('title')、@LocalStorageProp('detail')接收刷新数据，匹配依据为装饰器入参key值。

```typescript
// 创建LocalStorage实例，用于在卡片入口组件与卡片提供方之间传递刷新数据
let storage = new LocalStorage();

// V1卡片入口组件需通过@Entry传入LocalStorage实例，用于接收卡片提供方updateForm推送的数据
@Entry(storage)
@Component
struct WidgetCardV1 {
  // 通过@LocalStorageProp的入参key值匹配updateForm数据中的对应字段
  // 此处入参key为'title'，将匹配updateForm数据中key为'title'的字段
  @LocalStorageProp('title') title: string = 'Default title';
  @LocalStorageProp('detail') detail: string = 'Default detail';

  build() {
    Column() {
      Column() {
        Text(this.title)
          .fontSize(14)
          .margin({ top: '8%', left: '10%' })
        Text(this.detail)
          .fontSize(12)
          .margin({ top: '5%', left: '10%' })
      }
      .width('100%')
      .height('50%')
      .alignItems(HorizontalAlign.Start)

      Button('update')
        .margin({ top: '15%' })
        .onClick(() => {
          // 点击按钮通过postCardAction触发message事件
          // 该事件会被卡片提供方FormExtensionAbility的onFormEvent回调接收
          postCardAction(this, {
            'action': 'message',
            'params': { 'msgTest': 'messageEvent' }
          });
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

**V1迁移V2：**

入口组件迁移为@Entry @ComponentV2，移除LocalStorage实例的创建与传入；@LocalStorageProp迁移为@Local，变量名title、detail分别与updateForm推送数据的key保持一致，系统据此将刷新数据直接通知到对应装饰器。

```typescript
// V2迁移后入口组件使用@ComponentV2，无需再传入LocalStorage实例
@Entry
@ComponentV2
struct WidgetCard {
  // @LocalStorageProp迁移为@Local，系统改为按变量名匹配updateForm数据
  // 此处变量名为title，将匹配updateForm数据中key为'title'的字段
  @Local title: string = 'Default title';
  @Local detail: string = 'Default detail';

  build() {
    Column() {
      Column() {
        Text(this.title)
          .fontSize(14)
          .margin({ top: '8%', left: '10%' })
        Text(this.detail)
          .fontSize(12)
          .margin({ top: '5%', left: '10%' })
      }
      .width('100%')
      .height('50%')
      .alignItems(HorizontalAlign.Start)

      Button('update')
        .margin({ top: '15%' })
        .onClick(() => {
          // 点击按钮通过postCardAction触发message事件
          // 该事件会被卡片提供方FormExtensionAbility的onFormEvent回调接收
          postCardAction(this, {
            'action': 'message',
            'params': { 'msgTest': 'messageEvent' }
          });
        })
    }
    .width('100%')
    .height('100%')
  }
}
```

卡片提供方FormExtensionAbility的实现无需改动，updateForm推送的数据key与V2卡片中的变量名一致即可生效。

```typescript
// 卡片提供方接收到卡片页面postCardAction触发的message事件后，在此回调中处理刷新逻辑
onFormEvent(formId: string, message: string) {
  class FormDataClass {
    // 变量名与卡片页面中接收数据的变量名保持一致
    // 卡片UI侧（V2）通过变量名匹配这些字段，V1则通过@LocalStorageProp的入参key匹配
    title: string = 'Title Update.';
    detail: string = 'Description update success.';
  }

  let formData = new FormDataClass();
  // 将业务数据封装为卡片可识别的FormBindingData格式
  let formInfo: formBindingData.FormBindingData = formBindingData.createFormBindingData(formData);
  // 调用updateForm将刷新数据推送到指定卡片（formId），卡片UI接收后自动刷新界面
  formProvider.updateForm(formId, formInfo).then(() => {
    hilog.info(DOMAIN_NUMBER, TAG, 'FormAbility updateForm success.');
  }).catch((error: BusinessError) => {
    hilog.error(DOMAIN_NUMBER, TAG, `Operation updateForm failed. Cause: ${JSON.stringify(error)}`);
  });
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/23jL8G6GQfuTVg2Z12-9Zw/zh-cn_image_0000002736432471.gif)

## 卡片跨组件数据共享迁移

**迁移规则：**

在V1中，卡片多个组件可通过各自的@LocalStorageProp读取同一LocalStorage中的数据实现共享。迁移至V2后，卡片入口组件可使用@Provider接收刷新数据，子组件通过@Consumer自动同步，无需再依赖LocalStorage。

下例中，detail变量需要跨组件共享。

**V1实现代码如下：**

入口组件与子组件均通过@LocalStorageProp读取LocalStorage中的同一份数据实现共享。

```typescript
// 创建LocalStorage实例，用于在卡片入口组件、子组件与卡片提供方之间传递共享数据
let storage = new LocalStorage();

// V1卡片入口组件需通过@Entry传入LocalStorage实例
@Entry(storage)
@Component
struct ShareWidgetCardV1 {
  // 通过@LocalStorageProp的入参key值匹配updateForm数据
  @LocalStorageProp('title') title: string = 'Default title';
  @LocalStorageProp('detail') detail: string = 'Default detail';

  build() {
    Column() {
      Column() {
        Text(this.title)
          .fontSize(14)
          .margin({ top: '8%', left: '10%' })
        Text(this.detail)
          .fontSize(12)
          .margin({ top: '5%', left: '10%' })
        // 引用子组件，子组件内部通过同key的@LocalStorageProp读取同一LocalStorage中的共享数据
        ChildComp1()
      }
      .width('100%')
      .height('50%')
      .alignItems(HorizontalAlign.Start)

      Button('update')
        .margin({ top: '15%' })
        .onClick(() => {
          // 点击按钮通过postCardAction触发message事件，由卡片提供方处理刷新
          postCardAction(this, {
            'action': 'message',
            'params': { 'msgTest': 'messageEvent' }
          });
        })
    }
    .width('100%')
    .height('100%')
  }
}

@Component
struct ChildComp1 {
  // 子组件同样通过@LocalStorageProp读取LocalStorage中的共享数据
  // 入参key为'detail'，与入口组件保持一致，从而读取到同一份数据
  @LocalStorageProp('detail') detail: string = 'Default detail';

  build() {
    Text(this.detail)
      .fontSize(12)
      .margin({ top: '3%', left: '10%' })
  }
}
```

**V1迁移V2：**

入口组件移除LocalStorage，仅组件内部使用的title迁移为@Local；需要跨组件共享的detail迁移为@Provider，子组件通过@Consumer同步数据。updateForm推送数据的key为detail，与@Provider的变量名一致，数据更新后通过[@Provider](arkts-new-provider-and-consumer.md)/[@Consumer](arkts-new-provider-and-consumer.md)自动同步给子组件。

```typescript
// V2迁移后入口组件使用@ComponentV2，无需再传入LocalStorage实例
@Entry
@ComponentV2
struct ShareWidgetCard {
  // 仅组件内部使用的变量迁移为@Local
  @Local title: string = 'Default title';
  // 需跨组件共享的变量迁移为@Provider，系统按变量名匹配updateForm数据
  // updateForm推送key为'detail'的数据后，会自动更新此处@Provider，并同步给后代组件中@Consumer
  @Provider() detail: string = 'Default detail';

  build() {
    Column() {
      Column() {
        Text(this.title)
          .fontSize(14)
          .margin({ top: '8%', left: '10%' })
        Text(this.detail)
          .fontSize(12)
          .margin({ top: '5%', left: '10%' })
        // 引用子组件，子组件通过@Consumer自动同步父组件@Provider提供的detail数据
        ChildComp()
      }
      .width('100%')
      .height('50%')
      .alignItems(HorizontalAlign.Start)

      Button('update')
        .margin({ top: '15%' })
        .onClick(() => {
          // 点击按钮通过postCardAction触发message事件，由卡片提供方处理刷新
          postCardAction(this, {
            'action': 'message',
            'params': { 'msgTest': 'messageEvent' }
          });
        })
    }
    .width('100%')
    .height('100%')
  }
}

@ComponentV2
struct ChildComp {
  // 子组件通过@Consumer同步@Provider提供的数据
  // @Consumer与祖先组件中同名变量的@Provider自动建立连接，无需手动传参
  @Consumer() detail: string = 'Default detail for Consumer';

  build() {
    Text(this.detail)
      .fontSize(12)
      .margin({ top: '3%', left: '10%' })
  }
}
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/d85iCyzITb2iAmNwV23hJQ/zh-cn_image_0000002706833318.gif)
