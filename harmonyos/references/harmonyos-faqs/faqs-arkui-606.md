---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-606
title: 如何使用template设置多个模板并解决渲染异常问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何使用template设置多个模板并解决渲染异常问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:02+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:5004740b7a44025cc547ab0cb293ea5cca34bd760d099e0582403156876277bc
---

## 问题现象

使用Repeat渲染长列表时，当列表项存在多种不同模板类型时，通常会使用渲染模板（template）进行处理。一般有下面几种常见的问题场景：

* 场景一：模板数量多的情况如何处理？

  是否需要对每个模板都单独设置template，对于模板多的情况是否有其他方式减少重复设置template，例如下面场景：

  ```ts
  // ...
  Repeat<string>(this.message)
    .virtualScroll() // 开启虚拟滚动
    .each((item: RepeatItem<string>) => {
      // ...
    })
    .key((item: string, index: number) => {
      return item + '_' + index;
    })
    .templateId((item: string, index: number): string => {
      return item;
    })
      // 由template type渲染对应的template子组件
    .template('1', (item: RepeatItem<string>) => {
      // 模板1
    })
    .template('2', (item: RepeatItem<string>) => {
      // 模板2
    })
    .template('3', (item: RepeatItem<string>) => {
      // 模板3
    })
    .template('4', (item: RepeatItem<string>) => {
      // 模板4
    })
    .template('5', (item: RepeatItem<string>) => {
      // 模板5
    })
      // ...
    .template('100', (item: RepeatItem<string>) => {
      // 模板100
    });
  ```
* 场景二：刷新数据源，数据项未按照设定模板进行渲染如何处理？

  首次渲染时，按照template type渲染对应的template子组件，但刷新数据源后，数据项的template type变化，对应的数据项未按照对应的template进行渲染，仍显示首次渲染的模板，问题代码如下：

  ```ts
  @Entry
  @ComponentV2
  struct RepeatPage {
    @Local message: string[] = ['1', '1', '1', '1', '1', '1', '1', '1'];

    build() {
      Column() {
        // 刷新数据源
        Button('refresh')
          .onClick(() => {
            this.message = ['2', '3', '2', '3', '2', '3', '2', '2', '3', '2', '3', '2', '3', '2'];
          })
          .margin({
            left: 16,
            top: 16,
            bottom: 16,
            right: 16
          });

        List({ space: 18 }) {
          Repeat<string>(this.message)
            .each((item: RepeatItem<string>) => {
              ListItem() {
                Text(`each: ${item.item}`)
                  .backgroundColor('#f1f3f5')
                  .margin({
                    left: 16,
                    right: 16
                  });
              };
            })
            .key((item: string, index: number) => {
              return item + '_' + index;
            })
            .templateId((item: string, index: number): string => {
              console.info(`item = ${item}, index = ${index}`);
              return item;
            })
              // 由template type渲染对应的template子组件
            .template('1', (item: RepeatItem<string>) => {
              ListItem() {
                Text(`template_1: ${item.item}`)
                  .backgroundColor('#f1f3f5')
                  .margin({
                    left: 16,
                    right: 16
                  });
              };
            }, { cachedCount: 2 })
            .template('2', (item: RepeatItem<string>) => {
              ListItem() {
                Text(`template_2: ${item.item}`)
                  .backgroundColor('#f1f3f5')
                  .margin({
                    left: 16,
                    right: 16
                  });
              };
            }, { cachedCount: 2 });
        }
        .layoutWeight(1)
        .width('100%');
      };
    }
  }
  ```

## 背景知识

* Repeat：[可复用的循环渲染](../harmonyos-guides/arkts-new-rendering-control-repeat.md)，基于数组类型数据来进行循环渲染，一般与滚动容器组件配合使用。
* [循环渲染能力](../harmonyos-guides/arkts-new-rendering-control-repeat.md#节点更新复用能力说明)：Repeat子组件由.each()和.template()属性定义，只允许包含一个子组件。
* [each](../harmonyos-references/ts-rendering-control-repeat.md#each)：组件生成函数。当所有.template()的type和.templateId()返回值不匹配（即当前item不适用任何template定义的样式）时，将使用.each()处理数据项。
* [virtualScroll](../harmonyos-references/ts-rendering-control-repeat.md#virtualscroll)：Repeat开启虚拟滚动。
* [templateId](../harmonyos-references/ts-rendering-control-repeat.md#templateid)：为当前数据项分配template type。
* [template](../harmonyos-references/ts-rendering-control-repeat.md#template)：由template type渲染对应的template子组件。
* Repeat提供渲染模板（template）能力，可以在同一个数据源中渲染多种子组件。每个数据项会根据.templateId()得到template type，从而渲染type对应的.template()中的子组件。
* if/else：[条件渲染](../harmonyos-guides/arkts-rendering-control-ifelse.md)可根据应用状态，使用if、else和else if渲染相应的UI内容。
* [visibility](../harmonyos-references/ts-universal-attributes-visibility.md#visibility)：控制组件的显示或隐藏。当未设置visibility时，组件默认为显示。

## 解决方案

场景一：模板数量多的情况。

1. Repeat的渲染模板（template）能力，需要通过.templateId()方法为每个数据项指定模板类型，并在.template()中定义对应的渲染逻辑。不同模板类型对应不同的子组件结构，Repeat会根据类型自动复用相同模板的组件节点。详细参考：[循环渲染能力说明](../harmonyos-guides/arkts-new-rendering-control-repeat.md#节点更新复用能力说明)。
2. 若模板数量多时，不希望重复设置template定义多个模板，避免代码重复。可以考虑把结构相似的子组件放在一个template中处理，将数据项相关信息（例如item，index等）作为参数传给@Builder函数，在@Builder内使用visibility、if/else条件渲染等方式进行处理。例如通过visibility控制子组件内部组件的显示隐藏：

   ```ts
   @Entry
   @ComponentV2
   struct TemplatePageOne {
     @Local message: string[] = ['1', '2', '1', '2', '3', '3', '4', '4', '5', '5',];

     build() {
       Column() {
         List({ space: 18 }) {
           Repeat<string>(this.message)
             .virtualScroll() // 开启虚拟滚动
             .each((item: RepeatItem<string>) => {
               ListItem() {
                 Text(`each: ${item.item}`)
                   .backgroundColor('#f1f3f5')
                   .margin({
                     left: 16,
                     right: 16
                   });
               };
             })
             .key((item: string, index: number) => {
               return item + '_' + index;
             })
             .templateId((item: string, index: number): string => {
               console.info(`item = ${item}, index = ${index}`);
               if (item == '3' || item == '4') {
                 return 'other';
               }
               return item;
             })
               // 由template type渲染对应的template子组件
             .template('1', (item: RepeatItem<string>) => {
               ListItem() {
                 Text(`template_1: ${item.item}`)
                   .backgroundColor('#f1f3f5')
                   .margin({
                     left: 16,
                     right: 16
                   });
               };
             }, { cachedCount: 2 })
             .template('2', (item: RepeatItem<string>) => {
               ListItem() {
                 Text(`template_2: ${item.item}`)
                   .backgroundColor('#f1f3f5')
                   .margin({
                     left: 16,
                     right: 16
                   });
               };
             }, { cachedCount: 2 })
             .template('other', (item: RepeatItem<string>) => {
               ListItem() {
                 Row() {
                   Text(`template_other: `)
                     .backgroundColor('#f1f3f5')
                     .margin({
                       left: 16,
                       right: 16
                     });
                   // 通过visibility控制组件显示隐藏
                   Text(`this is template 3`)
                     .backgroundColor('#f1f3f5')
                     .visibility(item.item == '3' ? Visibility.Visible : Visibility.None)
                     .margin({
                       left: 16,
                       right: 16
                     });
                   Text(`this is template 4`)
                     .backgroundColor('#f1f3f5')
                     .visibility(item.item == '4' ? Visibility.Visible : Visibility.None)
                     .margin({
                       left: 16,
                       right: 16
                     });
                 }
               };
             }, { cachedCount: 2 });

         }
         .layoutWeight(1)
         .width('100%');
       };
     }
   }
   ```

场景二：刷新数据源，数据项未按照设定模板进行渲染。

1. template渲染模板能力需要启用虚拟滚动（virtualScroll）。
2. 当未开启virtualScroll()时，Repeat会一次性渲染全部数据项对应的组件，template的复用失效。详细参考：[关闭懒加载](../harmonyos-guides/arkts-new-rendering-control-repeat.md#懒加载能力说明)。
3. 所以刷新数据源后，虽然template type变化，但是template的复用失效，仍显示首次渲染的模板。需要手动设置.virtualScroll()，完整示例如下：

   ```ts
   @Entry
   @ComponentV2
   struct TemplatePageTwo {
     @Local message: string[] = ['1', '1', '1', '1', '1', '1', '1', '1'];

     build() {
       Column() {
         // 刷新数据源
         Button('refresh')
           .onClick(() => {
             this.message = ['2', '3', '2', '3', '2', '3', '2', '2', '3', '2', '3', '2', '3', '2'];
           })
           .margin({
             left: 16,
             top: 16,
             bottom: 16,
             right: 16
           });

         List({ space: 18 }) {
           Repeat<string>(this.message)
             .virtualScroll() // 开启虚拟滚动
             .each((item: RepeatItem<string>) => {
               ListItem() {
                 Text(`each: ${item.item}`)
                   .backgroundColor('#f1f3f5')
                   .margin({
                     left: 16,
                     right: 16
                   });
               };
             })
             .key((item: string, index: number) => {
               return item + '_' + index;
             })
             .templateId((item: string, index: number): string => {
               console.info(`item = ${item}, index = ${index}`);
               return item;
             })
               // 由template type渲染对应的template子组件
             .template('1', (item: RepeatItem<string>) => {
               ListItem() {
                 Text(`template_1: ${item.item}`)
                   .backgroundColor('#f1f3f5')
                   .margin({
                     left: 16,
                     right: 16
                   });
               };
             }, { cachedCount: 2 })
             .template('2', (item: RepeatItem<string>) => {
               ListItem() {
                 Text(`template_2: ${item.item}`)
                   .backgroundColor('#f1f3f5')
                   .margin({
                     left: 16,
                     right: 16
                   });
               };
             }, { cachedCount: 2 });
         }
         .layoutWeight(1)
         .width('100%');
       };
     }
   }
   ```
