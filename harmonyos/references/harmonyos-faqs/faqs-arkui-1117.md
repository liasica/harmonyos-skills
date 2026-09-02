---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1117
title: 如何拦截页面跳转
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何拦截页面跳转
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3e93a92ffdc3fced550cf77f8969f3418a47cf09514827eec9fd0f182c599f56
---

## 问题现象

Navigation如何实现侧滑手势拦截与路由跳转前拦截？

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)：路由导航的根视图容器。
* [NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)：作为子页面的根容器，用于显示Navigation的内容区。
* [onBackPressed](../harmonyos-references/ts-basic-components-navdestination.md#onbackpressed10)：当与Navigation绑定的页面栈中存在内容时，此回调生效。当点击返回键时，触发该回调。返回值为true时，表示重写返回键逻辑，返回值为false时，表示回退到上一个页面。
* [setInterception](../harmonyos-references/ts-basic-components-navigation.md#setinterception12)：设置Navigation页面跳转拦截回调。

## 解决方案

* **方案一：通过NavDestination组件的onBackPressed回调对返回事件进行拦截。**

  该方案支持拦截系统侧滑及NavDestination标题栏的返回事件，但不支持拦截NavPathStack.pop()操作。参考代码如下：

  ```ts
  .onBackPressed(() => {
    // 此处可添加拦截处理逻辑，然后return true放行
    this.getUIContext().getPromptAction().showDialog({
      message: '是否返回',
      alignment: DialogAlignment.Center,
      buttons: [
        {
          text: '取消',
          color: '#0000FF'
        },
        {
          text: '确认',
          color: '#0000FF'
        }
      ]
    }).then((data: ShowDialogSuccessResponse) => {
      // 操作菜单的响应结果,选中按钮在buttons数组中的索引，从0开始,第二个索引为1
      // 点击取消按钮，留在此页面
      if (data.index === 0) {
        console.info(`Succeeded in cancelling.`);
      }
      // 点击确认按钮，返回上层页面
      if (data.index === 1) {
        // 未传入拦截的参数正常返回
        RouterManager.getInstance().pop();
        console.info(`Succeeded in confirming.`);
      }
    });
    return true;
  });
  ```
* **方案二：通过封装自定义路由工具类实现。**
  1. 通过自定义路由管理单例，将所有的push事件都用路由管理单例执行，在需要拦截时统一处理。
  2. 在页面中绑定单例并实现跳转。

  参考代码如下：

  ```ts
  import { Prompt, ShowDialogSuccessResponse } from '@kit.ArkUI';

  // 自定义路由管理工具类，以push和pop为例
  export class RouterManager {
    private static instance: RouterManager;
    private navPathStack: NavPathStack | null = null;

    public static getInstance(): RouterManager {
      if (!RouterManager.instance) {
        RouterManager.instance = new RouterManager();
      }
      return RouterManager.instance;
    }

    public bindNavPathStack(stack: NavPathStack) {
      this.navPathStack = stack;
    }

    // 跳转
    public push(name: string, params?: object) {
      if (!this.navPathStack) {
        console.error('Failed to bind NavPathStack.');
        return;
      }
      // 拦截处理
      if (params && params['data']) {
        const allow = this.dataInterception(params);
        if (allow) {
          // 执行跳转
          this.navPathStack.pushPathByName(name, params, false);
        } else {
          console.error(`Failed to push.`);
          Prompt.showToast({ message: '被拦截' });
          return;
        }
      } else {
        this.navPathStack.pushPathByName(name, null, false);
      }
    }

    // 返回
    public pop(params?: object) {
      // 拦截处理
      if (params && params['data']) {
        const allow = this.dataInterception(params);
        if (allow) {
          // 执行返回
          this.navPathStack?.pop();
        } else {
          console.error(`Failed to pop.`);
          Prompt.showToast({ message: '被拦截' });
          return;
        }
      } else {
        // 执行返回
        this.navPathStack?.pop();
      }
    }

    // 数据拦截
    private dataInterception(param: object): boolean {
      if (param['data'] && param['data'] === '1') {
        return false;
      }
      return true;
    };

    // 获取参数
    public getParam(): object {
      let params = this.navPathStack?.getParamByIndex(this.navPathStack?.getAllPathName().length - 1) as object;
      return params;
    }
  }
  ```
* **方案三：使用setInterception拦截Navigation页面跳转。**

  [setInterception](../harmonyos-references/ts-basic-components-navigation.md#setinterception12)的willShow回调和interception回调可实现页面跳转前路由拦截，具体使用开发者可参考[示例2（使用导航控制器方法）](../harmonyos-references/ts-basic-components-navigation.md#示例2使用导航控制器方法)和[示例17（使用新增导航控制器方法）](../harmonyos-references/ts-basic-components-navigation.md#示例17使用新增导航控制器方法)。

方案一和方案二的完整代码如下所示：

```ts
import { Prompt, ShowDialogSuccessResponse } from '@kit.ArkUI';

// 自定义路由管理工具类，以push和pop为例
export class RouterManager {
  private static instance: RouterManager;
  private navPathStack: NavPathStack | null = null;

  public static getInstance(): RouterManager {
    if (!RouterManager.instance) {
      RouterManager.instance = new RouterManager();
    }
    return RouterManager.instance;
  }

  public bindNavPathStack(stack: NavPathStack) {
    this.navPathStack = stack;
  }

  // 跳转
  public push(name: string, params?: object) {
    if (!this.navPathStack) {
      console.error('Failed to bind NavPathStack.');
      return;
    }
    // 拦截处理
    if (params && params['data']) {
      const allow = this.dataInterception(params);
      if (allow) {
        // 执行跳转
        this.navPathStack.pushPathByName(name, params, false);
      } else {
        console.error(`Failed to push.`);
        Prompt.showToast({ message: '被拦截' });
        return;
      }
    } else {
      this.navPathStack.pushPathByName(name, null, false);
    }
  }

  // 返回
  public pop(params?: object) {
    // 拦截处理
    if (params && params['data']) {
      const allow = this.dataInterception(params);
      if (allow) {
        // 执行返回
        this.navPathStack?.pop();
      } else {
        console.error(`Failed to pop.`);
        Prompt.showToast({ message: '被拦截' });
        return;
      }
    } else {
      // 执行返回
      this.navPathStack?.pop();
    }
  }

  // 数据拦截
  private dataInterception(param: object): boolean {
    if (param['data'] && param['data'] === '1') {
      return false;
    }
    return true;
  };

  // 获取参数
  public getParam(): object {
    let params = this.navPathStack?.getParamByIndex(this.navPathStack?.getAllPathName().length - 1) as object;
    return params;
  }
}
interface DataInterface {
  data: string;
}

@Entry
@Component
struct RouterManagerPage {
  pageInfo: NavPathStack = new NavPathStack();
  controller: TextAreaController = new TextAreaController();
  text: string = '';
  params: DataInterface = { data: this.text };

  @Builder
  pageMap(name: string) {
    if (name === 'SubPage') {
      SubPage();
    }
  }

  aboutToAppear(): void {
    RouterManager.getInstance().bindNavPathStack(this.pageInfo);
  }

  build() {
    Navigation(this.pageInfo) {
      Column({ space: 16 }) {
        TextArea({
          text: this.text,
          placeholder: 'input your word...',
          controller: this.controller
        })
          .width('80%')
          .onChange((value: string) => {
            this.text = value;
            this.params.data = this.text;
          });
        Button('push')
          .onClick(() => {
            RouterManager.getInstance().push('SubPage', this.params);
            console.info(`Succeeded in getting text:${this.text}`);
          });
      }
      .padding({top:32})
      .justifyContent(FlexAlign.Start)
      .width('100%')
      .height('100%');
    }
    .navDestination(this.pageMap)
    .width('100%')
    .height('100%');
  }
}
@Component
struct SubPage {
  build() {
    NavDestination() {
      Column({ space: 16 }) {
        Button('onBackPressed不支持使用pop()拦截返回。')
          .onClick(() => {
            // 未传入拦截的参数
            RouterManager.getInstance().pop();
          });
        Button('pop添加拦截功能')
          .onClick(() => {
            let param = { data: '1' } as DataInterface;
            // 传入拦截参数
            RouterManager.getInstance().pop(param);
          });
      }
      .padding({ top: 32 })
      .justifyContent(FlexAlign.Start)
      .width('100%')
      .height('100%');
    }
    .onBackPressed(() => {
      // 此处可添加拦截处理逻辑，然后return true放行
      this.getUIContext().getPromptAction().showDialog({
        message: '是否返回',
        alignment: DialogAlignment.Center,
        buttons: [
          {
            text: '取消',
            color: '#0000FF'
          },
          {
            text: '确认',
            color: '#0000FF'
          }
        ]
      }).then((data: ShowDialogSuccessResponse) => {
        // 操作菜单的响应结果,选中按钮在buttons数组中的索引，从0开始,第二个索引为1
        // 点击取消按钮，留在此页面
        if (data.index === 0) {
          console.info(`Succeeded in cancelling.`);
        }
        // 点击确认按钮，返回上层页面
        if (data.index === 1) {
          // 未传入拦截的参数正常返回
          RouterManager.getInstance().pop();
          console.info(`Succeeded in confirming.`);
        }
      });
      return true;
    });
  }
}
```

效果图如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/SYrTvdwpS46L5JNHjbaZMg/zh-cn_image_0000002658806751.png "点击放大")

## 常见FAQ

Q：@Entry装饰的页面如何实现返回拦截？

A：使用@Entry装饰的页面可通过[onBackPress](../harmonyos-references/ts-custom-component-lifecycle.md#onbackpress)实现返回拦截，返回true表示页面自己处理返回逻辑，不进行页面路由；返回false表示使用默认的路由返回逻辑，不设置返回值按照false处理。
