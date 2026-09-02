---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-706
title: 如何使侧滑关闭操作透传到其他页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何使侧滑关闭操作透传到其他页面
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:423b8dacb611072eb167b825782e9d9ee844b81cf6fda17f426aca5ba9475676
---

## 问题现象

使用[PromptAction](../harmonyos-references/arkts-apis-uicontext-promptaction.md)弹窗，监听到系统侧滑事件后，若当前弹窗禁止侧滑消失，如何让事件响应到其他弹窗或路由页面上？

## 背景知识

* [openCustomDialog](../harmonyos-references/arkts-apis-uicontext-promptaction.md#opencustomdialog12)：创建并弹出自定义弹窗。使用Promise异步回调返回对话框的id，可供closeCustomDialog使用。暂不支持isModal = true与showInSubWindow = true同时使用。如果同时设置为true时，则只生效showInSubWindow = true。
* [getAllPathName()](../harmonyos-references/ts-basic-components-navigation.md#getallpathname10)：获取栈中所有NavDestination页面的名称。

## 解决方案

有两种方式实现侧滑关闭操作透传到其他页面。

* **方案一：**
  1. 创建弹窗时获取弹窗的dialogId。
  2. 在onWillDismiss回调里对侧滑事件判断，当'dismissDialogAction.reason===DismissReason.PRESS\_BACK'时，通过dialogId关闭其他弹窗。

  ```ts
  import { PromptAction } from '@kit.ArkUI';

  @Entry
  @Component
  struct Example1 {
    private customDialogComponentId: number = 0;
    private customDialogComponentIdTWO: number = 0;
    private promptAction: PromptAction = this.getUIContext().getPromptAction();

    @Builder
    customDialogComponent() {
      Column() {
        Text('弹窗1').fontSize(30);
        Row({ space: 50 }) {
          Button('确认').onClick(() => {
            this.promptAction.closeCustomDialog(this.customDialogComponentId);
          })
          Button('取消').onClick(() => {
            this.promptAction.closeCustomDialog(this.customDialogComponentId);
          })
        }.padding({ bottom: 16 })

        Button('打开第二弹窗')
          .onClick(() => {
            this.promptAction.openCustomDialog({
              builder: () => {
                this.customDialogComponentTWO();
              },
              onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                  this.promptAction.closeCustomDialog(this.customDialogComponentId);
                }
              },
              autoCancel: false
            }).then((dialogId: number) => {
              this.customDialogComponentIdTWO = dialogId;
            });
          })
      }.height(200).padding(16).justifyContent(FlexAlign.SpaceBetween)
    }

    @Builder
    customDialogComponentTWO() {
      Column() {
        Text('弹窗2').fontSize(30)
        Row({ space: 50 }) {
          Button('确认').onClick(() => {
            this.promptAction.closeCustomDialog(this.customDialogComponentIdTWO);
          })
          Button('取消').onClick(() => {
            this.promptAction.closeCustomDialog(this.customDialogComponentIdTWO);
          })
        }
      }.height(200).padding(16).justifyContent(FlexAlign.SpaceBetween)
    }

    build() {
      Row() {
        Column({ space: 20 }) {
          Text('应用弹窗')
            .fontSize(30)
            .onClick(() => {
              this.promptAction.openCustomDialog({
                builder: () => {
                  this.customDialogComponent();
                },
                onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                  if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                    dismissDialogAction.dismiss();
                  }
                },
                autoCancel: false
              }).then((dialogId: number) => {
                this.customDialogComponentId = dialogId;
              });
            })
        }
        .width('100%')
      }
      .height('100%')
    }
  }
  ```

* **方案二**：

  Navigation页面，创建弹窗时，在onWillDismiss里，监听侧滑事件，当"dismissDialogAction.reason === DismissReason.PRESS\_BACK"时，使用getAllPathName()获取栈中所有NavDestination页面的名称，通过popToName实现指定返回。

  1. Example2.ets(路径：“entry>src>main>ets>pages”)：创建NavPathStack路由栈，实现Page1页面跳转。

     ```ts
     @Entry
     @Component
     struct Example2 {
       @Provide('pageStack') pageStack: NavPathStack = new NavPathStack();

       build() {
         Navigation(this.pageStack) {
           Text('跳转Page1')
             .fontSize(30)
             .fontWeight(FontWeight.Bold)
             .backgroundColor("#87ceeb")
             .onClick(() => {
               this.pageStack.pushPathByName('Page1', null, false);
             })
         }
         .height('100%')
         .width('100%')
       }
     }
     ```
  2. Page1.ets(路径：“entry>src>main>ets>pages”)：实现Page2页面跳转。

     ```ts
     @Component
     export struct Page1 {
       @Consume('pageStack') pageStack: NavPathStack;

       build() {
         NavDestination() {
           Text('跳转page2')
             .fontSize(30)
             .fontWeight(FontWeight.Bold)
             .backgroundColor("#87ceeb")
             .onClick(() => {
               this.pageStack.pushPathByName('Page2', null, false);
             })
         }
         .width('100%')
         .height('100%')
       }
     }

     @Builder
     export function getPage1RouterMap(): void {
       Page1();
     }
     ```
  3. Page2.ets(路径：“entry>src>main>ets>pages”)：打开弹窗，实现侧滑不关闭弹窗，返回指定页面。

     ```ts
     import { PromptAction } from '@kit.ArkUI';

     @Component
     export struct Page2 {
       @Consume('pageStack') pageStack: NavPathStack;
       private customDialogComponentIdTWO: number = 0;
       private promptAction: PromptAction = this.getUIContext().getPromptAction();

       @Builder
       customDialogComponentTWO() {
         Column() {
           Text('弹窗').fontSize(30)
           Row({ space: 50 }) {
             Button('确认').onClick(() => {
               this.promptAction.closeCustomDialog(this.customDialogComponentIdTWO);
             })
             Button('取消').onClick(() => {
               this.promptAction.closeCustomDialog(this.customDialogComponentIdTWO);
             })
           }
         }.height(200).padding(16).justifyContent(FlexAlign.SpaceBetween)
       }

       build() {
         NavDestination() {
           Text('打开弹窗')
             .fontSize(30)
             .fontWeight(FontWeight.Bold)
             .backgroundColor('#87ceeb')
             .onClick(() => {
               this.promptAction.openCustomDialog({
                 builder: () => {
                   this.customDialogComponentTWO();
                 },
                 onWillDismiss: (dismissDialogAction: DismissDialogAction) => {
                   if (dismissDialogAction.reason === DismissReason.PRESS_BACK) {
                     let pages: string[] = this.pageStack.getAllPathName();
                     if (pages.length > 1) {
                       this.pageStack.popToName(pages[0], false);
                     } else {
                       this.pageStack.clear();
                     }
                   }
                 }
               }).then((dialogId: number) => {
                 this.customDialogComponentIdTWO = dialogId;
               });
             })
         }
         .width('100%')
         .height('100%')
       }
     }

     @Builder
     export function getPage2RouterMap(): void {
       Page2();
     }
     ```
  4. [routerMap](../harmonyos-guides/module-configuration-file.md#routermap标签)：路由表的路径。

     **说明** 

     需要在module.json5配置文件的module标签中定义routerMap标签，指向定义的路由表配置文件，例如："routerMap": "$profile:router\_map"。

     ```json
     {
       "routerMap": [
         {
           "name": "Page1",
           "pageSourceFile": "src/main/ets/pages/Page1.ets",
           "buildFunction": "getPage1RouterMap"
         },
         {
           "name": "Page2",
           "pageSourceFile": "src/main/ets/pages/Page2.ets",
           "buildFunction": "getPage2RouterMap"
         }
       ]
     }
     ```
