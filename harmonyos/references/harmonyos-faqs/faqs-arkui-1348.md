---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1348
title: 实现页面栈中指定页面置底方法
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现页面栈中指定页面置底方法
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9dd9c0ca21db03b2dccb742d5740547b16ced2188a1e23065adc97651fe649c6
---

## 问题现象

HarmonyOS官方只提供了将指定的NavDestination页面移到栈顶的moveIndexToTop方法，并没有提供将指定页面移至栈底的方法，该如何自定义实现页面栈的moveIndexToBottom功能？

如下图所示，在页面跳转到PageE后，此时页面栈的顺序为ABCDE，此时要求将页面C置底，即将页面栈顺序改为CABDE，并依次返回。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/7IKFLqb4T7isWsYCD4gApg/zh-cn_image_0000002628601518.png "点击放大")

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件是路由导航的根视图容器，一般作为Page页面的根容器使用，[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)则用作子页面的根容器，用于显示Navigation的内容区。
* [NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)是Navigation路由栈，该组件的[moveIndexToTop](../harmonyos-references/ts-basic-components-navigation.md#moveindextotop10)方法用于将index指定的NavDestination页面移到栈顶，[removeByIndexes](../harmonyos-references/ts-basic-components-navigation.md#removebyindexes11)方法可用于将页面栈内索引值在indexes中的NavDestination页面删除。
* [setPathStack](../harmonyos-references/ts-basic-components-navigation.md#setpathstack19)将当前路由栈中的路由页面信息数组更新为指定内容，并实现路由转场。从API 19开始支持此方法。

## 解决方案

* **方案一**：在API 19之前，可以循环使用moveIndexToTop方法实现。
  1. 当Navigation跳转至页面E时，页面栈的顺序为ABCDE，此时使用pageStack的size方法获取页面栈的大小size。
  2. 将size-1作为参数传入removeByIndexes方法，移除当前页面，此时页面栈的顺序为ABCD。
  3. 将需要置底的页面C先使用moveIndexToTop方法置顶，此时页面栈的顺序为ABDC。
  4. 将剩下的页面依次置顶，因为每次置顶后页面栈的顺序都会改动，所以只需每次都将栈底的页面置顶即可，即每次传入的参数都为0，经过size-2次循环后，此时页面栈的顺序为CABD。

     ```ts
     const pageNameArr: string[] = ['PageA', 'PageB', 'PageC', 'PageD', 'PageE'];
     let curPageIndex: number = 0;

     @Entry
     @Component
     struct SetPathStackPage {
       navPathStack: NavPathStack = new NavPathStack();

       @Builder
       pageMap(name: string) {
         if (name === 'PageE') {
           PageE();
         } else {
           Page({ name: name });
         }
       }

       build() {
         Navigation(this.navPathStack) {
           Button('跳转NavDestination页面')
             .fontSize('20fp')
             .margin({ top: '50vp' })
             .onClick(() => {
               curPageIndex = this.navPathStack.size();
               this.navPathStack.pushPath({ name: pageNameArr[curPageIndex] });
             });
         }.hideToolBar(true)
         .navDestination(this.pageMap);
       }
     }

     @Component
     struct Page {
       name: string = 'Page';
       navPathStack: NavPathStack = new NavPathStack();

       build() {
         NavDestination() {
           Column() {
             Button('跳转下个页面')
               .onClick(() => {
                 curPageIndex = this.navPathStack.size();
                 this.navPathStack.pushPath({ name: pageNameArr[curPageIndex] });
               });
           }.height('100%').width('100%')
           .justifyContent(FlexAlign.Center);
         }.title(this.name)
         .onReady((context: NavDestinationContext) => {
           this.navPathStack = context.pathStack;
         });
       }
     }

     @Component
     struct PageE {
       navPathStack: NavPathStack = new NavPathStack();

       build() {
         NavDestination() {
           Column() {
             Button('实现将页面C置底', { stateEffect: true, type: ButtonType.Capsule })
               .width('80%')
               .height(40)
               .margin(20)
               .onClick(() => {
                 let size = this.navPathStack.size();
                 // 移除当前栈顶页面E
                 this.navPathStack.removeByIndexes([size - 1]);
                 // 将页面C（原索引2）置顶
                 this.navPathStack.moveIndexToTop(2);
                 // 循环调整剩余页面顺序
                 for (let i = 0; i < size - 2; i++) {
                   this.navPathStack.moveIndexToTop(0);
                 }
                 // 重新加载页面E，关闭动画效果
                 this.navPathStack.pushPath({ name: 'PageE' }, false);
               });
           }.width('100%').height('100%');
         }.title('PageE')
         .onReady((context: NavDestinationContext) => {
           this.navPathStack = context.pathStack;
         });
       }
     }
     ```

     **说明** 

     该方法在遍历过程中会移动页面栈中的所有页面，所以它的时间复杂度是O(n)，但鉴于n的规模不大，所以实际使用中对性能基本不会有影响。
* **方案二**：从API 19开始，可以使用setPathStack方法设置路由栈中页面的位置。

  只需修改PageE中Button点击回调中的逻辑即可：

  ```ts
  const pageNameArr: string[] = ['PageA', 'PageB', 'PageC', 'PageD', 'PageE'];
  let curPageIndex: number = 0;

  @Entry
  @Component
  struct SetPathStackPage {
    navPathStack: NavPathStack = new NavPathStack();

    @Builder
    pageMap(name: string) {
      Page({ name: name });
    }

    build() {
      Navigation(this.navPathStack) {
        Button('跳转NavDestination页面')
          .fontSize('20fp')
          .margin({ top: '50vp' })
          .onClick(() => {
            curPageIndex = this.navPathStack.size();
            this.navPathStack.pushPath({ name: pageNameArr[curPageIndex] });
          });
      }.hideToolBar(true)
      .navDestination(this.pageMap);
    }
  }

  @Component
  export struct Page {
    name: string = 'Page';
    navPathStack: NavPathStack = new NavPathStack();

    // PageA,B,C,D显示的内容
    @Builder
    content1() {
      Button('跳转下个页面')
        .onClick(() => {
          curPageIndex = this.navPathStack.size();
          this.navPathStack.pushPath({ name: pageNameArr[curPageIndex] });
        });
    }

    // PageE显示的内容
    @Builder
    content2() {
      Button('实现将页面C置底', { stateEffect: true, type: ButtonType.Capsule })
        .onClick(() => {
          // 获取栈中的页面信息（数组）
          let pathInfoArr: NavPathInfo[] = this.navPathStack.getPathStack();
          console.info(JSON.stringify(pathInfoArr));
          // 改变数组中元素的位置
          pathInfoArr = pathInfoArr.slice(2, 3).concat(pathInfoArr.slice(0, 2), pathInfoArr.slice(3));
          console.info(JSON.stringify(pathInfoArr));
          this.navPathStack.setPathStack(pathInfoArr, false); // 设置路由栈的页面数组
        });
    }

    build() {
      NavDestination() {
        Column() {
          if (this.name === 'PageE') {
            this.content2();
          } else {
            this.content1();
          }
        }.height('100%').width('100%')
        .justifyContent(FlexAlign.Center);
      }.title(this.name)
      .onReady((context: NavDestinationContext) => {
        this.navPathStack = context.pathStack;
      });
    }
  }
  ```
