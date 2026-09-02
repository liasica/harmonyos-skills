---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-779
title: removeByNavDestinationId如何被上一页面感知并传递参数给上一页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > removeByNavDestinationId如何被上一页面感知并传递参数给上一页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:23+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b743e5eb43fdb776816cf4f2d123846157bfbbb31a427fea87d5215de5cbefc4
---

## 问题现象

在同一个ets文件中，实现a，b，c三个页面，a页面跳转b页面，b页面跳转c页面后，如何使用removeByNavDestinationId将b页面移除，并把b页面数据传回到a页面？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/5cH7U7cJQFuGxoAzVvb5Aw/zh-cn_image_0000002658916943.png "点击放大")

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏，其中内容区默认首页显示导航内容（Navigation的子组件）或非首页显示（[NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)的子组件），首页和非首页通过路由进行切换。
* [NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)是Navigation导航控制器，从API version 12开始，NavPathStack允许被继承。开发者可以在派生类中新增属性方法，也可以重写基类NavPathStack的方法。派生类对象可以替代基类NavPathStack对象使用。
* [removeByNavDestinationId](../harmonyos-references/ts-basic-components-navigation.md#removebynavdestinationid12)用于将路由栈内指定navDestinationId的NavDestination页面删除。

## 解决方案

1. 通过继承NavPathStack，实现一个自定义的removeByNavDestinationId方法，在移除NavDestination页面之前，获取其对应的路由页面信息[NavPathInfo](../harmonyos-references/ts-basic-components-navigation.md#navpathinfo10)，执行onPop回调。
2. 使用pushPath将指定的NavDestination页面信息入栈，并设置onPop回调。
3. 在b页面跳转到c页面后，调用removeByNavDestinationId，删除b页面，并将b页面的页面信息返回给a页面。
4. 在a页面，触发onPop回调接收页面b的处理结果，通过弹窗的形式展示返回的信息。

完整示例参考如下：

* 自定义MyNavPathStack类并重写removeByNavDestinationId方法。

  ```ts
  class MyNavPathStack extends NavPathStack {
    removeByNavDestinationId(navDestinationId: string, result?: object): boolean {
      if (result) {
        this.notifyRemove(navDestinationId, result);
      }
      return super.removeByNavDestinationId(navDestinationId);
    }

    private notifyRemove(navDestinationId: string, result: object) {
      let remove = this.getPathStack().filter(item => item.navDestinationId === navDestinationId);
      if (remove.length <= 0) {
        return;
      }
      let info = remove[0];
      info.onPop?.({ info: info, result: result }); // 调用onPop回调
    }
  }
  ```
* 页面跳转逻辑代码如下：

  ```ts
  // 页面间传递的参数类型
  class PageParams {
    name = '';
    remove = '';

    constructor(name?: string, remove?: string) {
      this.name = name === undefined ? '' : name;
      this.remove = remove === undefined ? '' : remove;
    }
  }

  @Entry
  @Component
  struct NavigationPage {
    pathStack: MyNavPathStack = new MyNavPathStack();

    @Builder
    routeMap(param: string) {
      if (param === 'PageA') {
        PageA();
      } else if (param === 'PageB') {
        PageB();
      } else if (param === 'PageC') {
        PageC();
      }
    }

    build() {
      Navigation(this.pathStack) {
        Button('跳转')
          .onClick(() => {
            this.pathStack.pushPath({ name: 'PageA', param: new PageParams('A') });
          });
      }.navDestination(this.routeMap);
    }
  }

  @Component
  struct PageA {
    pathStack: MyNavPathStack = new MyNavPathStack();
    @State param: PageParams = new PageParams();

    build() {
      NavDestination() {
        Column({ space: 10 }) {
          Text(`当前页面：` + this.param.name);
          Text(`待移除id：` + (this.param.remove || '-'));
          Button('开启监听并跳转').onClick(() => {
            // 跳转PageB页面并设置onPop回调
            this.pathStack.pushPath({
              name: 'PageB', param: new PageParams('B'), onPop: (res) => {
                console.info('A页面触发移除方法');
                this.getUIContext()
                  .showAlertDialog({ message: `页面${this.param.name}中触发的回调，参数为:${JSON.stringify(res)}` });
              }
            });
          });
        };
      }.onReady(context => {
        this.param = context.pathInfo.param as PageParams;
        this.pathStack = context.pathStack as MyNavPathStack;
      });
    }
  }

  @Component
  struct PageB {
    pathStack: MyNavPathStack = new MyNavPathStack();
    @State param: PageParams = new PageParams('', '');
    private navDestinationId: string = '';

    build() {
      NavDestination() {
        Column({ space: 10 }) {
          Text(`当前页面：` + this.param.name);
          Text(`待移除id：` + (this.param.remove || '-'));
          Button('跳转页面C').onClick(() => {
            // 跳转PageC页面并传递PageB的navDestinationId
            this.pathStack.pushPath({ name: 'PageC', param: new PageParams('C', this.navDestinationId) });
          });
        };
      }.onReady(context => {
        this.param = context.pathInfo.param as PageParams;
        this.navDestinationId = context.navDestinationId!;
        this.pathStack = context.pathStack as MyNavPathStack;
      });
    }
  }

  @Component
  struct PageC {
    pathStack: MyNavPathStack = new MyNavPathStack();
    @State param: PageParams = new PageParams('', '');

    build() {
      NavDestination() {
        Column({ space: 10 }) {
          Text(`当前页面：` + this.param.name);
          Text(`待移除id：` + (this.param.remove || '-'));
          if (this.param.remove) {
            Button('移除上一页面').onClick(() => {
              // 移除PageB页面，需要设置传递的参数，否则onPop回调不会触发
              this.pathStack.removeByNavDestinationId(this.param.remove, new PageParams());
            });
          }
        };
      }.onReady(context => {
        this.param = context.pathInfo.param as PageParams;
        this.pathStack = context.pathStack as MyNavPathStack;
      });
    }
  }
  ```
