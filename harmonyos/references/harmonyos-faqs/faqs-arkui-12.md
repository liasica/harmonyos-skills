---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-12
title: 如何在Navigation跳转页面时返回传参
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何在Navigation跳转页面时返回传参
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:58+08:00
doc_updated_at: 2026-06-15
content_hash: sha256:e1950e4b619e6264a8244f563dd66019f4fc6fd281a0c030d4874871833fb362
---

在页面跳转时使用[pushPath()](../harmonyos-references/ts-basic-components-navigation.md#pushpath12)，添加onPop回调接收入栈页面出栈时的返回结果。当页面返回时，通过[pop()](../harmonyos-references/ts-basic-components-navigation.md#pop11)设置result参数并传递给目标页面，由onPop回调接收返回参数。示例代码如下：

```screen
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
