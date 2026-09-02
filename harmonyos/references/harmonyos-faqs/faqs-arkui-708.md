---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-708
title: Navigation如何携带参数返回首页
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Navigation如何携带参数返回首页
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:40+08:00
doc_updated_at: 2026-07-15
content_hash: sha256:a3dc5896e06fd7f30adc5ce27ed70b015c123ec6682b7e1d825606b08be99cd5
---

## 问题现象

使用Navigation实现页面导航功能，从首页跳转到其他非首页之后，再次返回首页，如何将数据传递回首页？

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部可分为首页和子页。

  首页又称为导航栏（NavBar），由三部分组成：标题栏、内容区（Navigation子组件）、工具栏；

  子页则通过[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)承载，由两部分组成：标题栏、内容区（NavDestination子组件）。
* Navigation路由相关的操作都是基于页面栈[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)提供的方法进行，每个Navigation都需要创建并传入一个NavPathStack对象，用于管理页面。主要涉及页面跳转、页面返回、页面替换、页面删除、参数获取、路由拦截等功能。

  **说明** 

  首页并不属于路由栈（[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)）管理，路由栈只能控制NavDestination页面的入栈出栈。
* [pushPathByName](../harmonyos-references/ts-basic-components-navigation.md#pushpathbyname11)：将name指定的NavDestination页面信息入栈，传递的数据为param，添加onPop回调接收入栈页面出栈时的返回结果，并进行处理。
* [@ohos.events.emitter](../harmonyos-references/js-apis-emitter.md)：支持持续订阅事件、单次订阅事件、取消订阅事件及发送事件到事件队列。
* [hideNavBar](../harmonyos-references/ts-basic-components-navigation.md#hidenavbar9)：设置是否隐藏导航栏。设置为true时，隐藏Navigation的导航栏，包括标题栏、内容区和工具栏。如果此时路由栈中存在NavDestination页面，则直接显示栈顶NavDestination页面，反之显示空白。

返回首页一般存在两种方式：

1. 通过NavPathStack的pop方法一步步回退至首页，最简单的场景是：**首页->PageOne->首页**。
2. 首页跳转至其他页面之后，经过其他页面多次跳转，再立马返回首页。一个简单的场景是：**首页->PageOne->PageTwo->首页**。

## 解决方案

* 场景1：从其他页面一步步回退至首页。

  直接在首页通过pushPathByName等方法跳转到PageOne页面，同时添加onPop回调接收PageOne页面返回的参数即可。

  ```ts
  @Entry
  @Component
  struct NavPopSolution {
    pathStack: NavPathStack = new NavPathStack();
    @State message: string = '展示返回参数';

    @Builder
    pageMap(name: string) {
      if (name === 'PageOne') {
        PageOne();
      }
    }

    build() {
      Navigation(this.pathStack) {
        Column({ space: 16 }) {
          Text(this.message);
          Button('跳转到PageOne', { stateEffect: true, type: ButtonType.Capsule })
            .onClick(() => {
              this.pathStack.pushPathByName('PageOne', '', (data) => {
                // 用于页面出栈时触发该回调处理返回结果。
                this.message = JSON.stringify(data.result);
              });
            });
        };
      }.title('首页')
      .navDestination(this.pageMap);
    }
  }

  @Component
  struct PageOne {
    pathStack: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Column() {
          Button('携带参数回退首页', { stateEffect: true, type: ButtonType.Capsule })
            .onClick(() => {
              this.pathStack.pop({ 'content': 'c' });
            });
        };
      }.title('PageOne')
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
      });
    }
  }
  ```

  效果预览：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/LhxJ-6l-TKCduwZ4m13Nsg/zh-cn_image_0000002669866387.png "点击放大")
* 场景2：首页跳转至其他页面之后，经过其他页面多次跳转，再立马返回首页。

  由于需要立马返回首页，无法一步步将路由栈中页面逐个出栈，所以无法通过出栈时的onPop回调，拿到上一个页面出栈时携带的参数。且首页无法推入路由栈，不能使用push类方法跳转，也没有onReady生命周期，所以也无法在onReady接收其他子页的传参。

  现提供两种方式完成跳转，并将参数携带回首页。

  + 方案1：不使用默认的首页，将一个NavDestination自定义为首页。在返回自定义首页MainPage时，先调用[clear](../harmonyos-references/ts-basic-components-navigation.md#clear10)方法清除路由栈中的页面，然后重新将MainPage页入栈，即可在MainPage页[onReady](../harmonyos-references/ts-basic-components-navdestination.md#onready11)方法中接收返回的参数。
    1. 在Navigation首页设置hideNavBar为true，在aboutToAppear方法中将MainPage入栈，设置为自定义首页。通过[setInterception](../harmonyos-references/ts-basic-components-navigation.md#setinterception12)拦截所有返回到Navigation首页的操作，重定向到自定义首页。
    2. 从PageTwo页面跳转至MainPage，先使用clear()清除路由栈，再主动调用pushPath跳转到自定义首页MainPage。MainPage页面通过onReady方法获取传递参数。

       ```ts
       @Entry
       @Component
       struct NavMainPageExample {
         pathStack: NavPathStack = new NavPathStack();

         aboutToAppear() {
           // 将MainPage设置成自定义首页
           this.pathStack.pushPathByName('MainPage', '', false);
           // 设置Navigation页面跳转拦截回调
           this.pathStack.setInterception({
             willShow: (from: NavDestinationContext | 'navBar', to: NavDestinationContext | 'navBar',
               operation: NavigationOperation, animated: boolean) => {
               console.info(`${from} ${to} ${operation} ${animated}`);
               // 如果要返回到首页，就push名为MainPage的子页面
               if (to === 'navBar') {
                 this.pathStack.pushPathByName('MainPage', '', false);
               }
             }
           });
         }

         @Builder
         pageMap(name: string) {
           if (name === 'MainPage') {
             MainPage();
           } else if (name === 'PageOne') {
             PageOne();
           } else if (name === 'PageTwo') {
             PageTwo();
           }
         }

         build() {
           Navigation(this.pathStack) {
           }.hideNavBar(true) // 隐藏首页
           .navDestination(this.pageMap);
         }
       }

       // NavDestination作为首页
       @Component
       struct MainPage {
         @State message: string = '';
         pathStack: NavPathStack = new NavPathStack();

         build() {
           NavDestination() {
             Column({ space: 16 }) {
               Text(this.message);
               Button('跳转到PageOne', { stateEffect: true, type: ButtonType.Capsule })
                 .onClick(() => {
                   this.pathStack.pushPathByName('PageOne', null, true);
                 });
             };
           }.title('MainPage')
           .onReady((ctx: NavDestinationContext) => {
             this.pathStack = ctx.pathStack;
             this.message = JSON.stringify(this.pathStack.getParamByName('MainPage'));
           });
         }
       }

       @Component
       export struct PageOne {
         pathStack: NavPathStack = new NavPathStack();

         build() {
           NavDestination() {
             Column() {
               Button('跳转到PageTwo', { stateEffect: true, type: ButtonType.Capsule })
                 .onClick(() => {
                   this.pathStack.pushPathByName('PageTwo', null, true);
                 });
             };
           }.title('PageOne')
           .onReady((context: NavDestinationContext) => {
             this.pathStack = context.pathStack;
           });
         }
       }

       @Component
       struct PageTwo {
         pathStack: NavPathStack = new NavPathStack();

         build() {
           NavDestination() {
             Column() {
               Button('携带参数回退首页', { stateEffect: true, type: ButtonType.Capsule })
                 .onClick(() => {
                   this.pathStack.clear(); // 清除路由栈
                   this.pathStack.pushPath({ name: 'MainPage', param: 'context' }); // 跳转到自定义首页
                 });
             };
           }.title('PageTwo')
           .onReady((context: NavDestinationContext) => {
             this.pathStack = context.pathStack;
           });
         }
       }
       ```

       **说明** 

       连续调用多个页面栈操作方法时，中间过程会被忽略，显示最终的栈操作结果。

       效果预览：

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/d06TsV_ITdCLnVxFjHuR9g/zh-cn_image_0000002669990323.png "点击放大")
  + 方案2：在首页的aboutToAppear订阅事件，在clear清除路由栈时通过订阅的事件将参数传递回首页。

    ```ts
    import emitter from '@ohos.events.emitter';

    @Entry
    @Component
    struct EmitterSolution {
      pathStack: NavPathStack = new NavPathStack();
      @State message: emitter.EventData = {};

      aboutToAppear() {
        // 监听back事件，获取参数
        emitter.on('back', (data) => {
          this.message = data;
        });
      }

      aboutToDisappear() {
        emitter.off('back'); // 取消监听
      }

      @Builder
      pageMap(name: string) {
        if (name === 'PageOne') {
          PageOne();
        } else if (name === 'PageTwo') {
          PageTwo();
        }
      }

      build() {
        Navigation(this.pathStack) {
          Column({ space: 16 }) {
            Text(JSON.stringify(this.message));
            Button('跳转到PageOne', { stateEffect: true, type: ButtonType.Capsule })
              .onClick(() => {
                this.pathStack.pushPathByName('PageOne', null, true);
              });
          };
        }.title('首页')
        .navDestination(this.pageMap);
      }
    }

    @Component
    struct PageOne {
      pathStack: NavPathStack = new NavPathStack();

      build() {
        NavDestination() {
          Column() {
            Button('跳转到PageTwo', { stateEffect: true, type: ButtonType.Capsule })
              .onClick(() => {
                this.pathStack.pushPathByName('PageTwo', null, true);
              });
          };
        }.title('PageOne')
        .onReady((context: NavDestinationContext) => {
          this.pathStack = context.pathStack;
        });
      }
    }

    @Component
    struct PageTwo {
      pathStack: NavPathStack = new NavPathStack();

      build() {
        NavDestination() {
          Column() {
            Button('回退到首页，通过emitter传递参数', { stateEffect: true, type: ButtonType.Capsule })
              .onClick(() => {
                this.pathStack.clear();
                let eventData: emitter.EventData = { data: { 'content': 'c', 'id': '1' } };
                emitter.emit('back', eventData); // 传递back事件给首页
              });
          };
        }.title('PageTwo').onReady((context: NavDestinationContext) => {
          this.pathStack = context.pathStack;
        });
      }
    }
    ```

    效果预览：

    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/qTF6H_buTmykzChGBfUAQA/zh-cn_image_0000002639837140.png "点击放大")

## 常见FAQ

Q：Navigation如何直接返回首页？

A：首页不存在页面栈中，可看作在栈中的位置为-1，使用this.pathStack.clear()清空栈即可返回首页。

## 总结

| 场景 | 方案 | 说明 |
| --- | --- | --- |
| 从其他页面一步步回退至首页 | 使用onPop回调链式接收 | 适合页面逐级返回的场景。 |
| 多次跳转之后立马返回 | 自定义首页 | 1. 无法适配导航栏分栏显示模式。  2. 需要对自定义首页进行路由管理。  3. 导航栏等需要自定义实现。 |
| 多次跳转之后立马返回 | 事件订阅 | 1. 页面销毁时未正确销毁监听，可能会导致内存泄露。  2. 需要新增一个订阅事件，造成订阅事件过多。 |
