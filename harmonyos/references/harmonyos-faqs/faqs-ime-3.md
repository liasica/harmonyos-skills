---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-ime-3
title: 自定义键盘如何实现搜索等功能键
breadcrumb: FAQ > 应用框架开发 > 输入法框架 > 输入法开发（IME） > 自定义键盘如何实现搜索等功能键
category: harmonyos-faqs
scraped_at: 2026-09-02T15:04:06+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b40b774ea805b6b90e73ceef9bfde588c3ae70e7daf1c2735fb256fd52f1608d
---

## 问题现象

当采用自定义键盘时，如何实现Entry功能键，实现搜索框的搜索功能？

## 背景知识

* [Search](../harmonyos-references/ts-basic-components-search.md)：该组件是官方提供的搜索组件，可以通过[onSubmit](../harmonyos-references/ts-basic-components-search.md#onsubmit)等事件实现键盘Entry等事件的响应。
* [@ohos.inputMethodEngine (输入法服务)](../harmonyos-references/js-apis-inputmethodengine.md)：本模块面向输入法应用（包括系统输入法应用、三方输入法应用），为输入法应用提供能力，包括：创建软键盘窗口、插入/删除字符、选中文本、监听物理键盘按键事件等。

## 解决方案

* **场景一：Search通过[customKeyboard](../harmonyos-references/ts-basic-components-search.md#customkeyboard10)属性，采用应用内的自定义键盘组件，实现搜索事件。**
  1. 自定义键盘，实现搜索按钮，并实现搜索逻辑。
  2. customKeyboard绑定自定义键盘。

     ```ts
     @Entry
     @Component
     struct SearchExample {
       controller: SearchController = new SearchController();
       @State inputValue: string = '';

       // 自定义键盘组件
       @Builder
       CustomKeyboardBuilder() {
         Column() {
           Grid() {
             ForEach([1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#'], (item: number | string) => {
               GridItem() {
                 Button(item + '')
                   .width(110)
                   .onClick(() => {
                     this.inputValue += item;
                   });
               };
             });
           }.maxCount(3).columnsGap(10).rowsGap(10).padding(5);

           Button('搜索')
             .onClick(() => {
               // 关闭自定义键盘
               this.controller.stopEditing();
               // 执行搜索事件，此处弹窗事件替代搜索
               this.getUIContext().getPromptAction().showToast({
                 message: '触发搜索功能，搜索：' + this.inputValue,
                 duration: 2000
               });
             });
         }
         .backgroundColor(Color.Gray);
       }

       build() {
         Column() {
           Search({ controller: this.controller, value: this.inputValue })
             .customKeyboard(this.CustomKeyboardBuilder()) // 绑定自定义键盘
             .margin(10)
             .border({ width: 1 });
         };
       }
     }
     ```

     实现效果如下：

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/sWNjNp8GTRyvAs1NTvMTOg/zh-cn_image_0000002659020195.png "点击放大")

* **场景二：Search通过应用外第三方输入法实现搜索事件。**
  1. 该场景下Search组件需要绑定onSubmit事件执行搜索操作（小艺输入法只需绑定onSubmit事件即可）。

     ```ts
     @Entry
     @Component
     struct Index {
       controller: SearchController = new SearchController();
       inputValue: string = '';

       build() {
         Column() {
           Search({ controller: this.controller, value: $$this.inputValue })
             .margin(10)
             .border({ width: 1 })
             .onSubmit((value: string) => {
               // 关闭自定义键盘
               this.controller.stopEditing();
               // 执行搜索事件，此处用弹窗代替
               this.getUIContext().getPromptAction().showToast({
                 message: '触发搜索功能，搜索：' + value,
                 duration: 2000
               });
             });
         };
       }
     }
     ```
  2. 第三方输入法需要采用@ohos.inputMethodEngine (输入法服务)中的[sendKeyFunction](../harmonyos-references/js-apis-inputmethodengine.md#sendkeyfunction9)事件，给Search组件发送功能键的类别，执行指定操作。
     + sendKeyFunction中介绍的参数不全，只有0和1，其参数可参照官网功能键值设置：[常量](../harmonyos-references/js-apis-inputmethodengine.md#常量)。
     + 第三方输入法实现方式参考：[实现一个输入法应用示例](../harmonyos-guides/inputmethod-application-guide.md)。

       参考应用示例搜索功能修改如下：
     1. KeyboardController.ts文件增加搜索功能，封装sendKeyFunction接口：

        ```ts
        public search(value: number): void {
          if (this.textInputClient) {
            try {
              this.textInputClient.sendKeyFunction(value, (err: BusinessError, result: boolean) => {
                if (err) {
                  console.error(`Failed to sendKeyFunction: ${JSON.stringify(err)}`);
                  return;
                }
                if (result) {
                  console.info('Succeeded in sending key function.');
                } else {
                  console.error('Failed to sendKeyFunction.');
                }
              });
            } catch (err) {
              console.error(`Failed to sendKeyFunction: ${JSON.stringify(err)}`);
            }
          }
        }
        ```
     2. 实现搜索按钮并调用sendKeyFunction接口。

        ```ts
        .onClick(() => {
          keyboardController.search(3);
        });
        ```
     3. 系统设置中设置第三方应用为默认输入法：

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/z7-vF62jTqytLn3yBel4bQ/zh-cn_image_0000002628661004.png "点击放大")

        实现效果如下：

        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/2WVePvoUQYyK027eHZS0VQ/zh-cn_image_0000002659060265.png "点击放大")

        **须知** 

        注意：若场景二中三方输入法无法触发输入框的搜索事件，请检查sendKeyFunction中的参数是否是对应的功能键**常量**值。

## 常见FAQ

Q：当搜索功能键设置为sendKeyFunction(1)时，如何解决搜索框无响应的问题？

A：设置为sendKeyFunction(3)即可。

## 总结

对于应用内的自定义键盘只需要在键盘按钮中实现搜索等对应的页面逻辑即可，但是对于第三方输入法应用，想要实现页面的搜索等逻辑，Search组件需要绑定onSubmit事件，同时第三方自定义的输入法键盘的sendKeyFunction接口需要正确调用功能键**常量**值。
