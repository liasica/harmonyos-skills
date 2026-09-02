---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1094
title: Navigation加载启动页方案
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Navigation加载启动页方案
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c83c5eaf231c057c298967617684768ebb6c0bc60fc924d688632f26ffb97692
---

## 问题现象

在程序开发中，启动页（如闪屏页、广告页、登录页等）是常见的页面加载场景。当用户从启动页进入主页后，若通过点击返回键或侧滑操作尝试返回，系统并不会导航回启动页，而是直接退出应用，返回至桌面。

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)：路由导航的根视图容器，一般作为Page页面的根容器使用。
* [NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)：Navigation导航控制器，以栈的数据结构管理Navigation中所有的子页面，并提供栈操作的方法用于控制Navigation中子页面的切换。
* [NavDestination](../harmonyos-references/ts-basic-components-navdestination.md)：Navigation子页面的根容器，通过[onBackPressed](../harmonyos-references/ts-basic-components-navdestination.md#onbackpressed10)方法可以重写返回键逻辑。

## 解决方案

| 解决方案 | 对比 |
| --- | --- |
| 方案一：通过隐藏导航页和路由拦截实现不返回开屏页。 | 平板分栏模式下左侧闪屏页、右侧空白。 |
| 方案二：通过销毁作为开屏页的NavDestination页面，实现不返回开屏页。 | 平板分栏模式下左侧主页、右侧闪屏页。 |
| 方案三：使用Router页面做闪屏页，主页及后续页面由Navigation路由承载，通过clear清除闪屏页。 | 不受平板分栏的影响。 |

* **方案一**：通过隐藏导航页和路由拦截实现不返回开屏页。
  1. 开屏页通过导航页Navigation容器组件实现。
  2. Navigation启动时，通过this.pathStack.pushPathByName直接跳转到MainPage界面。
  3. 添加路由拦截，当路由目标页面名称为navBar（Navigation首页名字）时，就跳转到MainPage界面。
  4. 设置Navigation属性hideNavBar为true，隐藏返回导航页。

  ```ts
  @Entry
  @Component
  struct InterceptionSolution {
    pathStack: NavPathStack = new NavPathStack();
    @State hideNavBar: boolean = false;

    aboutToAppear(): void {
      setTimeout(() => {
        this.pathStack.pushPathByName('MainPage', undefined, false);
        this.hideNavBar = true;
        // 添加路由拦截功能
        this.pathStack.setInterception({
          willShow: (from: NavDestinationContext | NavBar, to: NavDestinationContext | NavBar,
            operation: NavigationOperation, isAnimated: boolean) => {
            // 如果返回到首页，就跳转为MainPage页面
            if (to == 'navBar') {
              console.info(`${from} ${to} ${operation} ${isAnimated}`);
              this.getUIContext().getPromptAction().showToast({ message: '无法返回到首页' });
              this.pathStack.pushPathByName('MainPage', undefined, false);
            }
          }
        });
      }, 2000);
    }

    @Builder
    pagesMap(name: string) {
      if (name == 'MainPage') {
        MainPage();
      } else if (name == 'Page') {
        Page();
      }
    }

    build() {
      Navigation(this.pathStack) {
        Text('欢迎进入APP').fontSize(30);
      }.title('启动页')
      .hideNavBar(this.hideNavBar)
      .navDestination(this.pagesMap);
    }
  }

  @Component
  struct MainPage {
    pageName: string = '';
    pathStack: NavPathStack | undefined = undefined;

    build() {
      NavDestination() {
        Column() {
          Text('this is MainPage').fontSize(24);
          Button(`push Page`).width('80%').margin({ top: 10, bottom: 10 })
            .onClick(() => {
              this.pathStack?.pushPathByName('Page', '');
            });
          Button(`pop`).width('80%').margin({ top: 10, bottom: 10 })
            .onClick(() => {
              this.pathStack?.pop();
            });
        };
      }.title('MainPage')
      .onReady((context: NavDestinationContext) => {
        this.pageName = context.pathInfo.name;
        this.pathStack = context.pathStack;
      });
    }
  }

  @Component
  struct Page {
    pageName: string = '';
    pathStack: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Column() {
          Text('this is Page').fontSize(24);
          Button(`pop`).width('80%').margin({ top: 10, bottom: 10 })
            .onClick(() => {
              this.pathStack?.pop();
            });
        };
      }.title('Page')
      .onReady((context: NavDestinationContext) => {
        this.pageName = context.pathInfo.name;
        this.pathStack = context.pathStack;
      });
    }
  }
  ```
* **方案二**：通过销毁作为开屏页的NavDestination页面，实现不返回开屏页。
  1. 首页使用Navigation作为根容器，闪屏页使用NavDestination作为根容器。
  2. 在首页的aboutToAppear回调中跳转到闪屏页。
  3. 闪屏页在定时器setTimeout回调中通过pop返回首页，此时闪屏页被销毁。

  ```ts
  @Entry
  @Component
  struct RemoveSolution {
    @Provide('navPathStack') navPathStack: NavPathStack = new NavPathStack();

    @Builder
    pageMap(name: string) {
      if (name === 'Splash') {
        Splash();
      }
    }

    aboutToAppear(): void {
      this.navPathStack.pushPathByName('Splash', null, false);
    }

    build() {
      Navigation(this.navPathStack) {
        Column() {
          Text('首页');
        }
        .width('100%')
        .height('100%')
        .justifyContent(FlexAlign.Center);
      }
      .hideToolBar(true)
      .navDestination(this.pageMap);
    }
  }

  @Component
  export struct Splash {
    @Consume('navPathStack') navPathStack: NavPathStack;

    aboutToAppear(): void {
      setTimeout(() => {
        this.navPathStack.pop(false);
      }, 2000);
    }

    build() {
      NavDestination() {
        Column() {
          Text('闪屏页');
        }
        .width('100%')
        .height('100%')
        .justifyContent(FlexAlign.Center);
      }
      .hideTitleBar(true);
    }
  }
  ```
* **方案三**：使用Router页面做闪屏页，主页及后续页面由Navigation路由承载，通过clear清除闪屏页。
  1. 闪屏页使用Entry页面，设置定时或用户同意隐私协议后通过[pushUrl](../harmonyos-references/arkts-apis-uicontext-router.md#pushurl)、[replaceUrl](../harmonyos-references/arkts-apis-uicontext-router.md#replaceurl)等方法跳转Navigation主页。
  2. 若使用pushUrl方法跳至Navigation页面，则需要[onPageShow](../harmonyos-references/ts-custom-component-lifecycle.md#onpageshow)生命周期中使用[clear](../harmonyos-references/arkts-apis-uicontext-router.md#clear)清除闪屏页。
  3. Router闪屏页代码：

     ```ts
     @Entry
     @Component
     struct RouterSolution {
       build() {
         RelativeContainer() {
           Text('闪屏页')
             .fontSize($r('app.float.page_text_font_size'))
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
             .onClick(() => {
               // 确定用户同意后跳转首页
               this.getUIContext().getRouter().pushUrl({ url: 'pages/NavigationPage' });
             });
         }
         .height('100%')
         .width('100%');
       }
     }
     ```
  4. Navigation首页：

     ```ts
     @Entry
     @Component
     struct NavigationPage {
       private stack: NavPathStack = new NavPathStack();

       onPageShow(): void {
         // 清除闪屏页，防止返回上一页
         this.getUIContext().getRouter().clear();
       }

       build() {
         // 在这里配置主页NavDestination信息
         Navigation(this.stack) {
           Column() {
             Text('Navigation首页，后续使用Navigation实现路由');
           }.width('100%').height('100%')
           .justifyContent(FlexAlign.Center);
         }
         .width('100%').height('100%');
       }
     }
     ```
