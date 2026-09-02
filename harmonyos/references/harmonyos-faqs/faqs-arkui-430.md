---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-430
title: NavPathStack清空页面栈或者按返回键，为什么显示的是导航栏，如何实现退出Navigation所在的页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > NavPathStack清空页面栈或者按返回键，为什么显示的是导航栏，如何实现退出Navigation所在的页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:00+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2eeb6d6103b9093d589b9346a9fa03ba38a018c138bca93f9a72d08bb78a5b1f
---

**问题描述**

NavPathStack清空页面栈或者按返回键，为什么没有退出Navigation所在的页面，而是显示导航栏。

**解决措施**

因为Navigation隐藏导航栏的属性hideNavBar默认值为false，调用路由栈的pop时均会返回到导航栏NavBar，由于hideNavBar默认false，当调用pop()时系统会优先显示Navigation组件自带的导航栏，而非完全退出页面栈。

开发者可通过隐藏导航栏或重写返回键的方法，实现不返回导航栏。

* 设置Navigation属性[hideNavBar](../harmonyos-references/ts-basic-components-navigation.md#hidenavbar9)为true，隐藏返回导航栏。
* 使用[onBackPressed()](../harmonyos-references/ts-basic-components-navdestination.md#onbackpressed10)方法重写返回键逻辑，通过[router.back()](../harmonyos-references/arkts-apis-uicontext-router.md#back)退出Navigation所在的页面。

  ```ts
  @Entry
  @Component
  struct NavPathStackExitsTheNavigationPage {
    @Provide('pathInfos') pathInfos: NavPathStack = new NavPathStack();

    @Builder
    myRouter(name: string) {
      if (name === 'PageOne') {
        PageOne()
      }
    }

    aboutToAppear(): void {
      this.pathInfos.pushPath({ name: 'PageOne' });
    }

    build() {
      Navigation(this.pathInfos) {
        Column() {
          Button('Jump to PageOne')
            .width('100%')
            .borderRadius(20)
            .margin({ bottom: 16 })
            .backgroundColor('#0A59F7')
            .onClick(() => {
              this.pathInfos.pushPath({ name: 'PageOne' });
            })
        }
        .width('100%')
        .height('100%')
        .padding({
          left: 16,
          right: 16
        })
        .justifyContent(FlexAlign.End)
        .alignItems(HorizontalAlign.Center)
      }
      .width('100%')
      .mode(NavigationMode.Auto)
      .title('title')
      .titleMode(NavigationTitleMode.Mini)
      .navDestination(this.myRouter)
      .hideBackButton(true)
      .hideNavBar(true) // Set the Navigation property's hideNavBar to true.
    }
  }

  @Component
  export struct PageOne {
    @Consume('pathInfos') pathInfos: NavPathStack;

    build() {
      NavDestination() {
        Column() {
          Text('PageOne')
            .width('100%')
            .fontSize(20)
            .fontColor(0x333333)
            .textAlign(TextAlign.Center)
        }
        .size({ width: '100%', height: '100%' })
        .alignItems(HorizontalAlign.Center)
        .justifyContent(FlexAlign.Center)
      }
      .title('PageOne')
      .onBackPressed(() => {
        this.getUIContext().getRouter().back(); // Override the return button logic to exit the navigation page.
        return true;
      })
    }
  }
  ```
