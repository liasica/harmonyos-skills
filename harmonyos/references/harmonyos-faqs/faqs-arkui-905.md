---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-905
title: 如何解决Navigation路由调用pop后onPop回调代码不执行的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何解决Navigation路由调用pop后onPop回调代码不执行的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a644a957571797528c0d5a17acc92eccec6aba2e1f70f9edd44845f21db01cbc
---

## 问题现象

使用Navigation构建路由，从pageOne通过pushPath跳转到pageTwo，期望pageOne的onPop回调在pageTwo返回时被触发，但效果未达预期。

问题代码示例参考如下：

```ts
class ParamWithOp {
  operation: number = 1
  count: number = 10
}

@Entry
@Component
struct PageOne {
  pageInfo: NavPathStack = new NavPathStack();
  @State message: string = 'Hello World'

  @Builder
  pageMap(name: string, params: Object) {
    if (name === 'pageTwo') {
      PageTwo()
    }
  }

  build() {
    Navigation(this.pageInfo) {
      Column() {
        Text(this.message)
          .width('80%')
          .height(50)
          .margin(10)

        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            // 将name指定的NavDestination页面信息入栈，传递的数据为param，添加接收处理结果的onPop回调。
            this.pageInfo.pushPath({
              name: 'pageTwo', param: new ParamWithOp(), onPop: (popInfo: PopInfo) => {
                this.message = `[pushPath]last page is: ${popInfo.info.name} result: ${JSON.stringify(popInfo.result)}`
              }
            });
          })
      }.width('100%').height('100%')
    }.navDestination(this.pageMap)
    .title('pageOne')
  }
}

@Component
struct PageTwo {
  pathStack: NavPathStack = new NavPathStack()

  build() {
    NavDestination() {
      Column() {
        Button('pop', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            // 回退到上一个页面，此处代码，在pop回pageOne页面时，未传参数
            this.pathStack.pop();
          })
      }.width('100%').height('100%')
    }.title('pageTwo')
    .onReady((context: NavDestinationContext) => {
      this.pathStack = context.pathStack
    })
  }
}
```

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/L1st2PbJQN2h_zwlQFeIug/zh-cn_image_0000002628559672.png "点击放大")

## 背景知识

[Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件是路由导航的根视图容器，结合导航控制器[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)可实现组件导航。

* [pushPath](../harmonyos-references/ts-basic-components-navigation.md#pushpath10)：将info指定的NavDestination页面信息入栈。可设置onPop回调函数来接收参数。
* [pop](../harmonyos-references/ts-basic-components-navigation.md#pop11)：弹出路由栈栈顶元素，并触发onPop回调传入页面处理结果。

## 问题定位

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/gHjW6MhLRum804WO12pxMg/zh-cn_image_0000002658918979.png "点击放大")

查阅官方文档关于pushPath方法的[NavPathInfo](../harmonyos-references/ts-basic-components-navigation.md#navpathinfo10)入参说明，其中的onPop回调函数仅pop、[popToName](../harmonyos-references/ts-basic-components-navigation.md#poptoname11)、[popToIndex](../harmonyos-references/ts-basic-components-navigation.md#poptoindex11)中设置result参数后触发。

## 分析结论

onPop回调函数需要使用pop、popToName、popToIndex方法返回时设置result参数才会触发，否则不会执行onPop回调。

## 修改建议

按上节所述，只需在pageTwo中调用pop方法时，传入result参数，即可在pageOne中成功收到onPop的回调。修改问题代码如下：

```ts
// 回退到上一个页面，随便传个result即可触发onPop回调
this.pathStack.pop(1);
```

修改后的运行效果参见效果预览，可以看到，当pageTwo调用pop返回时传入了result参数，在pageOne成功执行了onPop回调，并接收到相关参数。
