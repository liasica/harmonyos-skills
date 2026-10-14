---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-kit-faq-0004
title: Navigation传参与导航栏设置常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 常见问题 > Navigation传参与导航栏设置常见问题
category: harmonyos-faqs
scraped_at: 2026-10-15T07:13:52+08:00
doc_updated_at: 2026-10-14
content_hash: sha256:4aa9f16b75c907bc54b03d21981dda405877710ac07794e9714a68f0d5c3b578
---

**Q：如何使用Navigation的navPathStack参数？**

**A**：在已通过navPathStack获取到NavDestination集合后，可通过以下方法查询参数：

* 使用[getParamByIndex](../harmonyos-references/ts-basic-components-navigation.md#getparambyindex10)获取指定索引的NavDestination页面的参数信息；
* 使用[getParamByName](../harmonyos-references/ts-basic-components-navigation.md#getparambyname10)获取所有名为name的NavDestination页面的参数信息。

参考链接：[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)。

**Q：Navigation设置了隐藏属性，仍然出现空白导航栏，跳转至新页面后，导航栏会重新出现，如何解决？**

**A**：需同时设置Navigation组件及其NavDestination子组件的hideTitleBar属性为true才能完全隐藏导航栏。

参考链接：[Navigation](../harmonyos-references/ts-basic-components-navigation.md#navigation10)。

**Q：如何在Navigation跳转页面时返回传参？**

**A**：在页面跳转时使用[pushPath()](../harmonyos-references/ts-basic-components-navigation.md#pushpath12)，添加onPop回调接收入栈页面出栈时的返回结果。当页面返回时，通过[pop()](../harmonyos-references/ts-basic-components-navigation.md#pop11)设置result参数并传递给目标页面，由onPop回调接收返回参数。示例代码如下：

```ts
interface paramType {
  param: string
}

let paramA: paramType = {
  param: 'test1'
}

@Entry
@Component
struct Index {
  @Provide('pathInfos') pathInfos: NavPathStack = new NavPathStack();

  @Builder
  myRouter(name: string) {
    if (name === 'MyFirstNavDestination') {
      MyFirstNavDestination()
    } else if (name === 'MySecondNavDestination') {
      MySecondNavDestination()
    }
  }

  build() {
    Navigation(this.pathInfos) {
      Row() {
        Column() {
          Text('hello world')
        }
        .height('100%')
      }
      .onClick(() => {
        this.pathInfos.pushPathByName('MyFirstNavDestination', paramA);
      })
    }
    .navDestination(this.myRouter)
  }
}

@Component
export struct MyFirstNavDestination {
  @Consume('pathInfos') pathInfos: NavPathStack;

  getParamsPrint() {
    console.info('param is ' + JSON.stringify(this.pathInfos.getParamByName('MyFirstNavDestination')));
  }

  build() {
    NavDestination() {
      Row() {
        Column() {
          Text('MyFirstNavDestination')
        }
        .width('100%')
      }
      .height('100%')
      .onClick(() => {
        this.pathInfos.pushPath({
          name: 'MySecondNavDestination', param: null, onPop: (popInfo: PopInfo) => {
            console.info(`[pushPath]last page is: ${popInfo.info.name},result: ${JSON.stringify(popInfo.result)}`);
          }
        });
      })
    }.onShown(() => {
      this.getParamsPrint();
    })
  }
}

@Component
export struct MySecondNavDestination {
  @Consume('pathInfos') pathInfos: NavPathStack;
  private routerParams: paramType = { param: 'test 2' };

  build() {
    NavDestination() {
      Row() {
        Text('MySecondNavDestination')
      }
      .height('100%')
    }.onBackPressed(() => {
      this.pathInfos.pop(this.routerParams);
      return true;
    })
  }
}
```
