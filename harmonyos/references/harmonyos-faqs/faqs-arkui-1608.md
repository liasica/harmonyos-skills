---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1608
title: 如何解决页面跳转后弹窗不关闭
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决页面跳转后弹窗不关闭
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:58+08:00
doc_updated_at: 2026-08-13
content_hash: sha256:1c5073b299dc07e2e25e45ed416275deb80dcc4c6ef4e2d87658ab3c81ccbf00
---

## 问题现象

在页面中的自定义弹窗中点击按钮进行页面跳转，跳转完成后，自定义弹窗不关闭，如下图所示：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/jY1Dfy3rTEmhM_itLVoG8w/zh-cn_image_0000002676782148.png "点击放大")

主页代码如下所示：

```ts
import { BusinessError } from '@kit.BasicServicesKit';

@CustomDialog
struct CustomDialogExample {
  controller?: CustomDialogController;

  build() {
    Column({ space: 5 }) {
      Text('这是自定义弹窗')
        .fontSize(30)
        .height(100);
      Button('跳转到其他页面').onClick(() => {
        this.getUIContext().getRouter()
          .pushUrl({
            url: 'pages/Page',
          })
          .then(() => {
            console.info('succeeded');
          })
          .catch((error: BusinessError) => {
            console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
          });
      });
    };
  }
}

@Entry
@Component
struct Index {
  dialogController: CustomDialogController | null = new CustomDialogController({
    builder: CustomDialogExample(),
    autoCancel: true,
    alignment: DialogAlignment.Center,
    customStyle: false,
    width: 300,
    height: 200,
    backgroundColor: Color.White,
  });

  aboutToDisappear() {
    this.dialogController = null;
  }

  build() {
    Column() {
      Button('click me')
        .onClick(() => {
          this.dialogController?.open();
        }).backgroundColor('#0A59F7');
    }
    .width('100%')
    .margin({ top: 5 });
  }
}
```

## 背景知识

* [router](../harmonyos-references/js-apis-router.md)提供通过不同的url访问不同的页面的功能，包括跳转到应用内的指定页面、同应用内的某个页面替换当前页面、返回上一页面或指定的页面等。
* [Navigation](../harmonyos-guides/arkts-navigation-navigation.md)主要用于实现页面间以及组件内部的页面跳转，支持在不同组件间传递跳转参数，提供灵活的跳转栈操作，从而更便捷地实现对不同页面的访问和复用。
* [CustomDialog](../harmonyos-references/ts-methods-custom-dialog-box.md)是自定义弹出框，可用于广告、中奖、警告、软件更新等与用户交互响应操作。开发者可以通过CustomDialogController类显示自定义弹出框。
* [页面级弹出框](../harmonyos-guides/arkts-embedded-dialog.md)能够在路由跳转后，弹出框随着前一个路由页面的切换而消失，并且路由返回后弹出框还能够继续正常显示。
* [bindSheet](../harmonyos-guides/arkts-sheet-page.md)是绑定半模态页面，通过isShow属性控制显示隐藏，路由跳转时需要主动将isShow置为false来关闭。

## 问题定位

ArkUI的弹出框默认设置为全局级别，弹窗节点作为页面根节点的子节点，显示层级高于应用中的所有路由/导航页面。当页面内进行路由跳转时，如果应用未主动调用close方法关闭弹出框，弹出框不会自动关闭，并且会在下一个跳转页面上继续显示。

## 分析结论

在页面跳转时未给跳转按钮添加关闭弹窗的方法，也未尝试使用页面级弹出框。

## 修改建议

* 方案一：在弹窗跳转之前调用[close](../harmonyos-references/ts-methods-custom-dialog-box.md#close)方法关闭弹窗。
  + 使用router跳转页面：创建CustomDialogController自定义弹窗控制器。在[pushUrl](../harmonyos-references/arkts-apis-uicontext-router.md#pushurl)方法之前使用controller的close方法，关闭页面弹窗。修改代码如下：

    ```ts
    import { BusinessError } from '@kit.BasicServicesKit';

    @CustomDialog
    struct CustomDialogExample {
      controller?: CustomDialogController;

      build() {
        Column({ space: 5 }) {
          Text('这是自定义弹窗')
            .fontSize(30)
            .height(100);
          // start solution1
          Button('跳转到其他页面').onClick(() => {
            this.controller?.close();
            this.getUIContext()
              .getRouter()
              .pushUrl({
                url: 'pages/Page',
              })
              .then(() => {
                console.info('succeeded');
              })
              .catch((error: BusinessError) => {
                console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
              });
          });
          // end solution1
        };
      }
    }

    @Entry
    @Component
    struct PageNavigationOne {
      dialogController: CustomDialogController | null = new CustomDialogController({
        builder: CustomDialogExample(),
        autoCancel: true,
        alignment: DialogAlignment.Center,
        customStyle: false,
        width: 300,
        height: 200,
        backgroundColor: Color.White,
      });

      aboutToDisappear() {
        this.dialogController = null;
      }

      build() {
        Column() {
          Button('click me')
            .onClick(() => {
              this.dialogController?.open();
            }).backgroundColor('#0A59F7');
        }
        .width('100%')
        .margin({ top: 5 });
      }
    }
    ```

    修改后的效果如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/1VpudQ7pS_SL_8saUsvGBg/zh-cn_image_0000002676623358.png "点击放大")
  + 在页面的生命周期回调函数[onPageHide](../harmonyos-references/ts-custom-component-lifecycle.md#onpagehide)中添加关闭弹框逻辑可以实现弹窗自动关闭。

    ```ts
    import { BusinessError } from '@kit.BasicServicesKit';

    @CustomDialog
    struct CustomDialogExample {
      controller: CustomDialogController = new CustomDialogController({
        builder: CustomDialogExample({}),
      });

      build() {
        Column() {
          Text('这是自定义弹窗')
            .fontSize(30)
            .height(100);
          Button('跳转到其他页面').onClick(() => {
            this.getUIContext()
              .getRouter()
              .pushUrl({
                url: 'pages/Page',
              })
              .then(() => {
                console.info('succeeded');
              })
              .catch((error: BusinessError) => {
                console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
              });
          });
        };
      }
    }

    @Entry
    @Component
    struct PageNavigationTwo {
      dialogController: CustomDialogController = new CustomDialogController({
        builder: CustomDialogExample(),
        autoCancel: true,
        alignment: DialogAlignment.Center,
        customStyle: false,
        width: 300,
        height: 200,
        backgroundColor: Color.White,
      });

      build() {
        Column() {
          Button('click me')
            .onClick(() => {
              this.dialogController.open();
            })
            .backgroundColor('#0A59F7');
        }.width('100%').margin({ top: 5 });
      }

      // 页面隐藏时关闭弹窗
      onPageHide(): void {
        this.dialogController?.close();
      }
    }
    ```
  + 使用Navigation跳转页面：创建CustomDialogController自定义弹窗控制器。在[pushPathByName](../harmonyos-references/ts-basic-components-navigation.md#pushpathbyname10)之前使用controller的close方法，关闭页面弹窗。使用Navigation时需注意，将主页面而不是弹窗界面压栈。代码示例如下：

    主页面：

    ```ts
    @Builder
    export function MainPageBuilder() {
     PageNavigationThree();
    }

    @CustomDialog
    struct CustomDialogExample {
     @Consume pageInfos: NavPathStack;
     controller?: CustomDialogController;

     build() {
       Column({ space: 5 }) {
         Text('这是自定义弹窗')
           .fontSize(30)
           .height(100);
         Button('跳转到其他页面').onClick(() => {
           this.controller?.close();
           this.pageInfos.pushPathByName('Page', null);
         });
       };
     }
    }

    @Entry
    @Component
    struct PageNavigationThree {
     @Provide('pageInfos') pageInfos: NavPathStack = new NavPathStack();
     dialogController: CustomDialogController | null = new CustomDialogController({
       builder: CustomDialogExample(),
       autoCancel: true,
       alignment: DialogAlignment.Center,
       customStyle: false,
       width: 300,
       height: 200,
       backgroundColor: Color.White,
     });

     aboutToDisappear() {
       this.dialogController = null;
     }

     build() {
       Navigation(this.pageInfos) {
         Column() {
           Button('click me')
             .onClick(() => {
               this.dialogController?.open();
             }).backgroundColor('#0A59F7');
         }
         .width('100%')
         .margin({ top: 5 });
       };
     }
    }
    ```

    目标跳转页面：

    ```ts
    @Builder
    export function MainPageBuilder() {
      Page();
    }

    @Entry
    @Component
    struct Page {
      @State message: string = 'Hello World';
      pageInfos: NavPathStack = new NavPathStack();

      build() {
        NavDestination() {
          RelativeContainer() {
            Text(this.message)
              .id('PageHelloWorld')
              .fontSize($r('app.float.page_text_font_size'))
              .fontWeight(FontWeight.Bold)
              .alignRules({
                center: { anchor: '__container__', align: VerticalAlign.Center },
                middle: { anchor: '__container__', align: HorizontalAlign.Center }
              })
              .onClick(() => {
                this.message = 'Welcome';
              });
          }
          .height('100%')
          .width('100%');
        };
      }
    }
    ```

    在src/main目录下的module.json5配置文件中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json。router\_map.json示例如下：

    ```json
    {
      "routerMap": [
        {
          "name": "Page",
          "pageSourceFile": "src/main/ets/pages/Page.ets",
          "buildFunction": "MainPageBuilder",
          "data": {
            "description": "This is secondPage"
          }
        }
      ]
    }
    ```

    效果如下：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/eeDZpV46TCi5Q_er-H5dow/zh-cn_image_0000002706383601.png "点击放大")
* 方案二：使用页面级弹出框。在弹出框的options入参中设置levelMode属性，值为LevelMode.EMBEDDED表示开启页面级弹出框能力，该方法仅支持API15及以上版本。目标跳转页面同方案一，主页面示例代码为：

  ```ts
  import { BusinessError } from '@kit.BasicServicesKit';
  import { ImmersiveMode, LevelMode } from '@kit.ArkUI';

  @CustomDialog
  struct CustomDialogExample {
    controller?: CustomDialogController;

    build() {
      Column({ space: 5 }) {
        Text('这是自定义弹窗')
          .fontSize(30)
          .height(100);
        Button('跳转到其他页面').onClick(() => {
          this.getUIContext()
            .getRouter()
            .pushUrl({
              url: 'pages/Page',
            })
            .then(() => {
              console.info('succeeded');
            })
            .catch((error: BusinessError) => {
              console.error(`pushUrl failed, code is ${error.code}, message is ${error.message}`);
            });
        });
      };
    }
  }

  @Entry
  @Component
  struct PageNavigationFour {
    dialogController: CustomDialogController | null = new CustomDialogController({
      builder: CustomDialogExample(),
      autoCancel: true,
      alignment: DialogAlignment.Center,
      customStyle: false,
      width: 300,
      height: 200,
      backgroundColor: Color.White,
      levelMode: LevelMode.EMBEDDED, // 启用页面级弹出框
      immersiveMode: ImmersiveMode.EXTEND, // 设置页面级弹出框蒙层的显示模式
    });

    aboutToDisappear() {
      this.dialogController = null;
    }

    build() {
      Column() {
        Button('click me')
          .onClick(() => {
            this.dialogController?.open();
          }).backgroundColor('#0A59F7');
      }
      .width('100%')
      .margin({ top: 5 });
    }
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/_ijaQmPzT5ahK80fszSaWg/zh-cn_image_0000002676783616.png "点击放大")

  **说明** 

  使用Navigation跳转页面时，通过CustomDialogController配置LevelMode.EMBEDDED后，弹窗会挂载在Page根节点下，层级高于Navigation内所有NavDestination页面，路由跳转后弹窗仍然显示在最上层。此时需要通过[openCustomDialog](../harmonyos-guides/arkts-uicontext-custom-dialog.md)接口打开弹窗，并配置LevelMode.EMBEDDED和levelUniqueId属性，将弹窗节点挂载到NavDestination下，实现页面级弹窗。

  另外，[bindSheet](../harmonyos-guides/arkts-sheet-page.md)由isShow属性控制显示隐藏，路由跳转不会自动关闭，需要在跳转前将isShow置为false。CustomDialog默认是模态弹窗，有蒙层，蒙层下方控件不会被点击穿透；如果设置了isModal: false，外层页面可以继续交互。凡是弹窗或sheet内触发Navigation跳转，都应先关闭弹层，再做路由跳转。

## 常见FAQ

Q：设置levelMode属性后，页面级弹出框未生效，可能是什么原因导致的？

A：当且仅当弹出框为非子窗模式时，页面级能力才会生效，即showInSubWindow参数不设置或设置为false。

Q：在Navigation路由下使用CustomDialogController配置LevelMode.EMBEDDED后，路由跳转后弹窗仍然显示在最上层，如何解决？

A：CustomDialogController配置LevelMode.EMBEDDED后，弹窗会挂载在Page根节点下，层级高于Navigation内所有NavDestination页面。在Navigation路由下实现页面级弹窗，需要通过[openCustomDialog](../harmonyos-guides/arkts-uicontext-custom-dialog.md)接口打开弹窗，并配置LevelMode.EMBEDDED和levelUniqueId属性，将弹窗节点正确挂载到NavDestination下。

Q：bindSheet半模态页面在路由跳转后仍然显示，如何解决？

A：bindSheet由isShow属性控制显示隐藏，路由跳转不会自动关闭。在触发路由跳转前，需要先将isShow置为false，再执行路由跳转。
