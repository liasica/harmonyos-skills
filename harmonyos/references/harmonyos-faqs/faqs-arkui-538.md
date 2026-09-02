---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-538
title: 分栏模式下，页面切换无响应
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 分栏模式下，页面切换无响应
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:01+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b2269686e79028e49f475e231dfc4c7a3b2adac10343c95d1b280a0c5eaa5cda
---

## 问题现象

在分栏模式下，点击左侧新闻时，右侧页面能正常显示该新闻；但点击另一条新闻后，右侧页面仍保持显示上一条新闻内容。

## 背景知识

* [onNewParam](../harmonyos-references/ts-basic-components-navdestination.md#onnewparam19)栈中的NavDestination页面通过launchMode.MOVE\_TO\_TOP\_SINGLETON或launchMode.POP\_TO\_SINGLETON移动到栈顶时，触发该回调。
* [pushPath](../harmonyos-references/ts-basic-components-navigation.md#pushpath10)将info指定的NavDestination页面信息入栈。
* 应用在平板设备上支持单双栏、三分栏布局，组合使用[Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件和[SideBarContainer](../harmonyos-references/ts-container-sidebarcontainer.md)组件即可实现，更多请参考[一多分栏开发实践](https://gitee.com/harmonyos_samples/multi-columns)。

## 问题定位

左侧是一个列表组件，点击跳转后右侧显示web页面内容。发现使用的是router跳转且每次跳转的都是同一个页面url。

第一次点击跳转时，有页面跳转日志：

```screen
[(100000:100000:scope)] Click accepted, tag: Row
[(100000:100000:scope)] Page router manager is creating page[7]: url: pages/ArtContentPage path: pages/ArtContentPage.js, recoverable: yes, namedRouter: no
[(100000:100000:scope)] build ohmUrl for forward compatibility
```

第二次点击时，没有页面跳转的日志：

```screen
[(100000:100000:scope)] Click try accept
[(100000:100000:scope)] Click accepted, tag: Row
[(100000:100000:scope)] Move page to front to index: 1
```

需要查看代码是否使用了[MOVE\_TO\_TOP\_SINGLETON模式](../harmonyos-references/ts-basic-components-navigation.md#launchmode12枚举说明)，这个模式下，从栈底向栈顶查找，如果指定的名称已经存在，则将对应的NavDestination页面移到栈顶，不会触发onShown事件。

```screen
interface MyParam {
  content?: string
}

@Entry
@Component
export struct Index {
  pathStack: NavPathStack = new NavPathStack()
  @State content: string = 'content1'; // 传递给子页的参数

  @Builder
  pageMap(name: string) {
    if (name === "TestPage1") {
      TestPage1();
    }
  }

  build() {
    Navigation(this.pathStack) {
      Column({ space: 24 }) {
        Button('单例跳转子页')
          .onClick(() => {
            // 单例
            this.pathStack.pushPath({ name: 'TestPage1', param: { content: this.content } as MyParam },
              { launchMode: LaunchMode.MOVE_TO_TOP_SINGLETON, animated: true })
          })

        Button('改变入参')
          .onClick(() => {
            this.content = 'content2'
          })
      }.width('100%').height('100%').justifyContent(FlexAlign.Center)
    }.navBarWidth('35%')
    .mode(NavigationMode.Split)
    .navDestination(this.pageMap)
    .hideTitleBar(true)
  }
}

@Component
struct TestPage1 {
  navPathStack: NavPathStack = new NavPathStack()
  @State content: string = '';

  build() {
    NavDestination() {
      Stack({ alignContent: Alignment.Center }) {
        Text(this.content).fontSize(20).fontColor(Color.Red)
      }.width('100%').height('100%')
    }
    .height('100%')
    .width('100%')
    .backgroundColor(Color.Blue)
    .onReady((ctx: NavDestinationContext) => {
      this.navPathStack = ctx.pathStack
    })
    .onShown(() => {
      // 子页从隐藏到显示会触发回调，可用于接收参数
      this.onPageShow()
    })
  }

  onPageShow(): void {
    const params: ESObject[] = this.navPathStack.getParamByName('TestPage1');
    if (params.length > 0) {
      let myParam = params[params.length - 1] as MyParam;
      let content = myParam?.content || '';
      this.content = content
    }
  }
}
```

## 分析结论

设置了单实例页面模式，由于web页面名称相同，导致页面未重新加载，内容未更新。

## 修改建议

使用onNewParam回调获取POP\_TO\_SINGLETON跳转传递的参数并刷新页面。具体代码参考：

```screen
interface MyParam {
  content?: string
}

@Entry
@Component
export struct Index {
  pathStack: NavPathStack = new NavPathStack()
  @State content: string = 'content1'; // 传递给子页的参数

  @Builder
  pageMap(name: string) {
    if (name === "TestPage1") {
      TestPage1();
    }
  }

  build() {
    Navigation(this.pathStack) {
      Column({ space: 24 }) {
        Button('单例跳转子页')
          .onClick(() => {
            // 单例
            this.pathStack.pushPath({ name: 'TestPage1', param: { content: this.content } as MyParam },
              { launchMode: LaunchMode.MOVE_TO_TOP_SINGLETON, animated: true })
          })

        Button('改变入参')
          .onClick(() => {
            this.content = 'content2'
          })
      }.width('100%').height('100%').justifyContent(FlexAlign.Center)
    }.navBarWidth('35%')
    .mode(NavigationMode.Split)
    .navDestination(this.pageMap)
    .hideTitleBar(true)
  }
}

@Component
struct TestPage1 {
  navPathStack: NavPathStack = new NavPathStack()
  @State content: string = '';

  build() {
    NavDestination() {
      Stack({ alignContent: Alignment.Center }) {
        Text(this.content).fontSize(20).fontColor(Color.Red)
      }.width('100%').height('100%')
    }
    .height('100%')
    .width('100%')
    .backgroundColor(Color.Blue)
    .onReady((ctx: NavDestinationContext) => {
      this.navPathStack = ctx.pathStack
    })
    .onShown(() => {
      // 子页从隐藏到显示会触发回调，可用于接收参数
      this.onPageShow()
    })
    .onNewParam((info: ESObject) => {
      // 若页面就在栈顶，跳转页面不会有页面隐藏到显示的过程，不会触发onShown回调
      // 可以在onNewParam中获取新的参数
      console.info(`onNewParam： ${JSON.stringify(info)}`)
      this.content = info.content
    })
  }

  onPageShow(): void {
    const params: ESObject[] = this.navPathStack.getParamByName('TestPage1');
    if (params.length > 0) {
      let myParam = params[params.length - 1] as MyParam;
      let content = myParam?.content || '';
      this.content = content
    }
  }
}
```
