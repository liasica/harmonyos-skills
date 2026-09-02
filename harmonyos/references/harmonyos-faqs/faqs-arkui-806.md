---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-806
title: Navigation使用replacePath跳转后，如何携带数据返回到栈内上一个页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Navigation使用replacePath跳转后，如何携带数据返回到栈内上一个页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:770f13f749f6b0d91d80f6bc7d16452e16293bee61de28eb265cfd615e6d61a9
---

## 问题现象

PageA通过pushPath跳转到PageB，PageB通过replacePath方式跳转到PageB，如何在PageB回到PageA的时候把数据返回到PageA。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/bepPEnwaS9yNq4tpsNWu0g/zh-cn_image_0000002658797159.png "点击放大")

## 背景知识

* [pushPath](../harmonyos-references/ts-basic-components-navigation.md#pushpath12)：将指定的NavDestination页面信息入栈，通过NavigationOptions设置页面栈操作选项。
* [NavPathInfo](../harmonyos-references/ts-basic-components-navigation.md#navpathinfo10)：路由页面信息。
* [replacePath](../harmonyos-references/ts-basic-components-navigation.md#replacepath12)：将当前页面栈栈顶退出，将info指定的NavDestination页面信息入栈。
* onPop：接收入栈页面出栈时的返回结果。
* [onResult](../harmonyos-references/ts-basic-components-navdestination.md#onresult15)：NavDestination返回时触发该回调。

## 解决方案

* **方案一**：可以将onPop封装成通用方法，PageA跳转到PageB时，将此方法携带过去，当PageB通过replacePath方式跳转到PageB时，绑定的onPop使用传递进来的方法。

  ```ts
  import { PageA } from './PageAS1';
  import { PageB } from './PageBS1';

  @Entry
  @Component
  struct Solution1 {
    @Provide pathStack: NavPathStack = new NavPathStack();

    @Builder
    pageMap(params: string) {
      if (params === 'PageA') {
        PageA();
      } else if (params === 'PageB') {
        PageB();
      }
    }

    build() {
      Navigation(this.pathStack) {
        Column() {
          Button('Push PageA')
            .onClick(() => {
              this.pathStack.pushPathByName('PageA', null);
            });
        }.width('100%').height('100%')
        .justifyContent(FlexAlign.Center);
      }.navDestination(this.pageMap);
    }
  }
  ```

  ```ts
  @ObservedV2
  export class Params {
    @Trace num: number = 0;
    click: (popInfo: PopInfo) => void = () => {
    };
  }

  @Component
  export struct PageA {
    @Consume pathStack: NavPathStack;
    private param: Params = new Params();
    // 封装的onPop回调
    customOnPop = (popInfo: PopInfo) => {
      this.param.num = popInfo.result as number;
    };

    aboutToAppear(): void {
      // 初始化参数
      this.param.num = 0;
      this.param.click = this.customOnPop;
    }

    build() {
      NavDestination() {
        Column() {
          Column() {
            Text('One Page')
              .fontSize('30');
            Text(`${this.param.num}`)
              .fontSize('30');
          }
          .justifyContent(FlexAlign.Center)
          .size({ width: '100%', height: '60%' });

          Row() {
            Button('push PageB')
              .onClick(() => {
                this.pathStack.pushPath({
                  name: 'PageB', param: this.param, onPop: (popInfo) => {
                    this.param.click(popInfo); // 使用封装的onPop回调
                  }
                });
              });
          }.justifyContent(FlexAlign.SpaceAround)
          .alignItems(VerticalAlign.Center)
          .size({ width: '100%', height: '40%' });
        };
      }.width('100%').height('100%');
    }
  }
  ```

  ```ts
  import { Params } from './PageAS1';

  @Component
  export struct PageB {
    @Consume pathStack: NavPathStack;
    private param: Params = new Params();

    build() {
      NavDestination() {
        Column() {
          Row() {
            Text('Second Page')
              .fontSize('30');
          }
          .justifyContent(FlexAlign.Center)
          .alignItems(VerticalAlign.Center)
          .size({ width: '100%', height: '60%' });

          Column() {
            Button('Replace PageB')
              .onClick(() => {
                this.pathStack.replacePath({
                  name: 'PageB', onPop: (popInfo) => {
                    this.param.click(popInfo); // 使用传递过来的方法
                  }
                });
              });
            Button('pop back')
              .onClick(() => {
                this.pathStack.pop(10);
              });
          }.size({ width: '100%', height: '40%' });
        };
      }.width('100%').height('100%')
      .onReady((ctx: NavDestinationContext) => {
        this.param = ctx?.pathInfo?.param as Params; // 接收传递的参数
      });
    }
  }
  ```
* **方案二**：使用onResult来处理页面返回，在PageA的NavDestination添加onResult回调，用来接收返回到该页面时携带的数据。下述示例中Navigation页面代码同方案一。

  ```ts
  @ObservedV2
  export class Params {
    @Trace num: number = 0;
  }

  @Component
  export struct PageA {
    @Consume pathStack: NavPathStack;
    private param: Params = new Params();

    aboutToAppear(): void {
      this.param.num = 0;
    }

    build() {
      NavDestination() {
        Column() {
          Column() {
            Text('One Page')
              .fontSize('30');
            Text(`${this.param.num}`)
              .fontSize('30');
          }.justifyContent(FlexAlign.Center)
          .size({ width: '100%', height: '60%' });

          Row() {
            Button('push PageB')
              .onClick(() => {
                this.pathStack.pushPath({ name: 'PageB' });
              });
          }.justifyContent(FlexAlign.SpaceAround)
          .alignItems(VerticalAlign.Center)
          .size({ width: '100%', height: '40%' });
        };
      }
      .onResult((num: number) => {
        this.param.num = num; // 接收回到此页面携带的参数
      }).size({ width: '100%', height: '100%' });
    }
  }
  ```

  ```ts
  @Component
  export struct PageB {
    @Consume pathStack: NavPathStack;

    build() {
      NavDestination() {
        Column() {
          Row() {
            Text('Second Page')
              .fontSize('30');
          }
          .justifyContent(FlexAlign.Center)
          .alignItems(VerticalAlign.Center)
          .size({ width: '100%', height: '60%' });

          Column() {
            Button('Replace PageB')
              .onClick(() => {
                this.pathStack.replacePath({ name: 'PageB' });
              });

            Button('pop back')
              .onClick(() => {
                this.pathStack.pop(10);
              });
          }.size({ width: '100%', height: '40%' });
        };
      }.size({ width: '100%', height: '100%' });
    }
  }
  ```

## 常见FAQ

Q：Navigation使用pop跳转至单例页面时，如何重置目标页面的参数信息。

A：[pop](../harmonyos-references/ts-basic-components-navigation.md#pop11)不可以重置param参数，[pushPath](../harmonyos-references/ts-basic-components-navigation.md#pushpath12)默认的[路由栈操作模式](../harmonyos-references/ts-basic-components-navigation.md#launchmode12枚举说明)为STANDARD，将指定的NavDestination入栈，如果需要重置目标页面参数，需要使用pushPath指定页面栈操作模式为POP\_TO\_SINGLETON或MOVE\_TO\_TOP\_SINGLETON，并传递新的参数，就可以实现和pop一样的效果并且能够重置param参数。

Q：对于单例页面，如何处理单例页面的数据接收问题？

A：HarmonyOS的[onNewParam](../harmonyos-references/ts-basic-components-navdestination.md#onnewparam19)是当之前存在于栈中的NavDestination页面通过launchMode.MOVE\_TO\_TOP\_SINGLETON或launchMode.POP\_TO\_SINGLETON移动到栈顶时，触发该回调，可基于此接收新数据。
