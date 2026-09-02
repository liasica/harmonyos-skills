---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-771
title: "@ComponentV2自定义弹窗传参失败"
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > @ComponentV2自定义弹窗传参失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:22+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:1a46e4e08855d269962ae88ff2895074df5d3efdcd30621e64af78f65a2c48a6
---

## 问题现象

在@ComponentV2组件中无法直接将数据传递给@CustomDialog组件。

问题代码如下：

```ts
@ComponentV2
export struct Page {
  @Local selectIndex: number = 0;
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: AccountSafeDialog({
      selectIndex: this.selectIndex,
    }),
  })
  // ...
}
```

```ts
// 定义弹窗
@CustomDialog
export struct AccountSafeDialog {
  controller?: CustomDialogController;
  @Link selectIndex: number;
  // ...
}
```

## 背景知识

[@ComponentV2装饰器](../harmonyos-guides/arkts-create-custom-components.md#componentv2)为搭配V2状态变量使用的自定义组件装饰器。[@Link装饰器](../harmonyos-guides/arkts-link.md)装饰的变量与其父组件中的数据源共享相同的值，[自定义弹窗CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)通过CustomDialogController类显示自定义弹窗，二者均仅在状态管理V1中使用。

## 问题定位

运行代码报错：

```ts
error message:undefined 'selectIndex'[-21]
<@Component 'AccountSafeDialog'[375]>:
constructor: source variable in parent/ancestor @Component must be defined. Application error!
```

报错信息显示无法找到变量selectIndex，代码中使用@Local修饰了selectIndex，说明该变量为父组件传递，检查父组件发现为@ComponentV2修饰组件，与子组件的@CustomDialog装饰器存在不同的状态管理版本。

## 分析结论

@ComponentV2装饰器的组件与使用@CustomDialog装饰器的自定义弹窗组件之间存在状态管理版本不兼容，导致数据无法正确传递给使用@CustomDialog装饰器的自定义弹窗组件。

## 修改建议

可使用@ComponentV2的Page替换@CustomDialog，使用Navigation的Dialog模式实现弹窗。

示例代码如下：

1. Index.ets，通过[pushPathByName](../harmonyos-references/ts-basic-components-navigation.md#pushpathbyname11)方法将指定的NavDestination页面信息入栈。

   ```ts
   @Entry
   @ComponentV2
   struct NavigationExample {
     pageInfos: NavPathStack = new NavPathStack();
     @Local selectIndex: number = 10;

     build() {
       Navigation(this.pageInfos) {
         Column() {
           Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
             .width('80%')
             .height(40)
             .margin(20)
             .onClick(() => {
               this.pageInfos.pushPathByName('pageOne', this.selectIndex, () => {
               }, false); // 将name指定的NavDestination页面信息入栈
             });
         };
       }.title('NavIndex');
     }
   }
   ```
2. 创建PageOne.ets，作为弹窗页面，并设置NavDestination的mode为DIALOG模式。

   ```ts
   @Builder
   export function PageOneBuilder() {
     PageOne();
   }

   @ComponentV2
   export struct PageOne {
     pageInfos: NavPathStack = new NavPathStack();
     @Local selectIndex: number = 0;

     build() {
       NavDestination() {
         Column() {
           Text(this.selectIndex.toString());
         };
       }
       .onReady(context => {
         this.selectIndex = context.pathInfo.param as number;
       })
       .position({ left: 50, top: 200 })
       .backgroundColor(Color.Pink)
       .width(300)
       .height(300)
       .mode(NavDestinationMode.DIALOG)
       .hideBackButton(true);
     }
   }
   ```
3. 在src/main目录下的[module.json5配置文件](../harmonyos-guides/module-configuration-file.md)中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下：

   ```ts
   {
     "routerMap": [
       {
         "name": "pageOne",
         "pageSourceFile": "src/main/ets/pages/PageOne.ets",
         "buildFunction": "PageOneBuilder",
         "data": {
           "description": "this is pageOne"
         }
       }
     ]
   }
   ```
