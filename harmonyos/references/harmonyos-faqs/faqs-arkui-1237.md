---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1237
title: 如何实现打开新页面不关闭模态转场页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现打开新页面不关闭模态转场页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:24+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2e4c2cc294e35343d9ea97cc5bff796d1c3fde283c302140107dcf657e0378b7
---

## 问题现象

如何实现打开新页面不关闭模态转场页面，从新页面返回时保持原样？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/FES94PQaTSyMZ31ccSP2yg/zh-cn_image_0000002658953257.png "点击放大")

## 背景知识

* 模态转场限制：HarmonyOS默认的[模态转场](../harmonyos-guides/arkts-modal-transition.md)（bindContentCover或bindSheet）在跳转新页面时会自动关闭模态层，因其设计为单层弹窗栈。
* [onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)作用域：仅@Entry修饰的页面可监听物理返回键/侧滑事件，自定义组件需通过控制器（如ChildController）代理拦截。

## 解决方案

使用if条件渲染+控制器拦截返回，其次通过@State控制模态显示隐藏，然后子组件通过Controller向父页面注册返回拦截，最后父页面onBackPress调用子组件拦截方法实现效果。

步骤如下：

1. 定义子组件控制器（关键通信桥梁）。

   ```ts
   // 1. 定义子组件控制器（核心通信桥梁）
   class ChildController {
     // 子组件注册的返回拦截回调
     onBackPress: () => boolean = () => false;
   }
   ```
2. 子组件声明模态显示隐藏状态&绑定控制器。

   ```ts
   // 2. 子组件（包含模态层）
   @Component
   struct ModalTransitionWithIf {
     // 控制模态层显隐
     @State isShowShare: boolean = false;
     // 接收父页面传入的控制器
     private controller: ChildController = new ChildController();

     aboutToAppear(): void {
       // 向控制器注册子组件的返回拦截逻辑
       this.controller.onBackPress = (): boolean => {
         return this.handleChildBackPress();
       };
     }

     // 子组件返回事件处理（核心拦截逻辑）
     private handleChildBackPress(): boolean {
       if (this.isShowShare) {
         console.info('拦截返回：关闭模态层');
         this.isShowShare = false;
         return true; // 拦截系统返回
       }
       return false; // 不拦截
     }

     // 跳转到新页面（不关闭模态层）
     private jumpToNewPage() {
       this.getUIContext().getRouter().pushUrl({ url: 'pages/SecondPage' });
     }

     build() {
       Stack() {
         Column() {
           Button('打开模态层')
             .onClick(() => this.isShowShare = true)
             .margin(20);
         }
         .width('100%')
         .height('100%')
         .justifyContent(FlexAlign.Start);

         // 条件渲染的模态层（关键实现）
         if (this.isShowShare) {
           Column() {
             Column() {
               Text('模态层内容').fontSize(20).margin(20);
               Button('跳转新页面')
                 .onClick(() => this.jumpToNewPage());
             }
             .width('100%')
             .height('50%')
             .borderRadius(20)
             .backgroundColor('#FFF')
             .shadow(ShadowStyle.OUTER_DEFAULT_XS)
             .position({ x: 0, y: '60%' });
           }
           .width('100%')
           .height('100%')
           .backgroundColor(this.isShowShare ? '#99000000' : '')
           .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP]);
         }
       }
       .width('100%')
       .height('100%');
     }
   }
   ```
3. 父页面（@Entry）集成子组件&全局返回拦截。

   ```ts
   // 3. 父页面（入口组件）
   @Entry
   @Component
   struct MainPage {
     // 创建控制器实例（父子通信枢纽）
     private childController: ChildController = new ChildController();

     // 全局返回拦截（核心）
     onBackPress(): boolean {
       console.info('父页面收到返回事件');
       return this.childController.onBackPress();
     }

     build() {
       Column() {
         // 传递控制器给子组件
         ModalTransitionWithIf({ controller: this.childController });
       }
       .width('100%')
       .height('100%');
     }
   }
   ```

完整示例代码如下：

主页面代码（@Entry入口页面）：

```ts
// 1. 定义子组件控制器（核心通信桥梁）
class ChildController {
  // 子组件注册的返回拦截回调
  onBackPress: () => boolean = () => false;
}

// 2. 子组件（包含模态层）
@Component
struct ModalTransitionWithIf {
  // 控制模态层显隐
  @State isShowShare: boolean = false;
  // 接收父页面传入的控制器
  private controller: ChildController = new ChildController();

  aboutToAppear(): void {
    // 向控制器注册子组件的返回拦截逻辑
    this.controller.onBackPress = (): boolean => {
      return this.handleChildBackPress();
    };
  }

  // 子组件返回事件处理（核心拦截逻辑）
  private handleChildBackPress(): boolean {
    if (this.isShowShare) {
      console.info('拦截返回：关闭模态层');
      this.isShowShare = false;
      return true; // 拦截系统返回
    }
    return false; // 不拦截
  }

  // 跳转到新页面（不关闭模态层）
  private jumpToNewPage() {
    this.getUIContext().getRouter().pushUrl({ url: 'pages/SecondPage' });
  }

  build() {
    Stack() {
      Column() {
        Button('打开模态层')
          .onClick(() => this.isShowShare = true)
          .margin(20);
      }
      .width('100%')
      .height('100%')
      .justifyContent(FlexAlign.Start);

      // 条件渲染的模态层（关键实现）
      if (this.isShowShare) {
        Column() {
          Column() {
            Text('模态层内容').fontSize(20).margin(20);
            Button('跳转新页面')
              .onClick(() => this.jumpToNewPage());
          }
          .width('100%')
          .height('50%')
          .borderRadius(20)
          .backgroundColor('#FFF')
          .shadow(ShadowStyle.OUTER_DEFAULT_XS)
          .position({ x: 0, y: '60%' });
        }
        .width('100%')
        .height('100%')
        .backgroundColor(this.isShowShare ? '#99000000' : '')
        .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP]);
      }
    }
    .width('100%')
    .height('100%');
  }
}

// 3. 父页面（入口组件）
@Entry
@Component
struct MainPage {
  // 创建控制器实例（父子通信枢纽）
  private childController: ChildController = new ChildController();

  // 全局返回拦截（核心）
  onBackPress(): boolean {
    console.info('父页面收到返回事件');
    return this.childController.onBackPress();
  }

  build() {
    Column() {
      // 传递控制器给子组件
      ModalTransitionWithIf({ controller: this.childController });
    }
    .width('100%')
    .height('100%');
  }
}
```

模态跳转新页面代码（SecondPage页面）：

```ts
//SecondPage页面
@Entry
@Component
struct SecondPage {
  build() {
    Column() {
      Text('新页面内容').fontSize(25).margin(30);
      Button('返回模态层')
        .onClick(() => this.getUIContext().getRouter().back());
    }
    .width('100%')
    .height('100%')
    .justifyContent(FlexAlign.Center);
  }
}
```
