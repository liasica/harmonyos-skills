---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/arkui-uimana-faq-0018
title: ArkUI页面路由跳转常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 常见问题 > ArkUI页面路由跳转常见问题
category: harmonyos-faqs
scraped_at: 2026-10-21T07:11:10+08:00
doc_updated_at: 2026-10-20
content_hash: sha256:3935e5172dc6f3562a711b448c8bc3373c02928093d90cc18149ef41b7331d4c
---

**Q：HAP如何跳转到HAR模块页面？HAR模块内页面如何跳至HAP模块页面？**

**A**：跨包跳转场景，以下是关键注意事项：

1. 模块类型限制：仅适用于HAR（静态库）或HSP（动态库）模块。
2. HAP跳转到其他HAP的页面，必须使用UIAbility的startAbility方法拉起目标HAP的Ability。参考[跨HAP包页面跳转方案](../architecture-guides/traffic-v1_1-ts_61-0000002386324576.md)。HAP和HAR之间页面跳转的两种实现方案：Navigation路由和Router路由。跳转示例：HAP包入口页面->HAR包CustomPage页面->HAP包Page页面。如下所示：
   * 方案一：Navigation路由配置。
     1. 在HAR模块内配置HAR页面的路由表：配置CustomPage的页面路由。即配置HAR中的module.json5文件和route\_map.json文件，详细可参考官网跨包路由的[系统路由表](../harmonyos-guides/arkts-navigation-navigation.md#系统路由表)实现。
     2. 在HAP模块配置Page页面路由，和第1步在HAR模块配置CustomPage页面路由类似。

        ```ts
        @Builder
        export function PageBuilder() {
          Page();
        }

        @Entry
        @Component
        struct Page {
          build() {
            NavDestination() {
              Column() {
                Text('Hello World')
                  .fontSize(20);
              }.height('100%').width('100%')
              .justifyContent(FlexAlign.Center);
            };
          }
        }
        ```

        ```ts
        {
          "routerMap": [
            {
              "name": "Page",
              "pageSourceFile": "src/main/ets/pages/Page.ets",
              "buildFunction": "PageBuilder"
            }
          ]
        }
        ```
     3. 在HAP模块的oh-package.json5文件中引用HAR模块。

        ```json
        "dependencies": {
            "testhar": "file:../testHar"
          },
        ```
     4. 从HAP模块入口页面跳转至HAR页面CustomPage：

        ```ts
        @Entry
        @Component
        struct NavigationSolution {
          @State pathStack: NavPathStack = new NavPathStack();

          build() {
            Navigation(this.pathStack) {
              Column() {
                Button('ToHarPage', { stateEffect: true, type: ButtonType.Capsule })
                  .width('80%')
                  .height(40)
                  .margin(20)
                  .onClick(() => {
                    // 跳转至目标testHar模块所在页面
                    this.pathStack.pushPathByName('CustomPage', null, false);
                  });
              }.width('100%').height('100%')
              .justifyContent(FlexAlign.Center);
            };
          }
        }
        ```
     5. 从HAR模块页面跳转至HAP模块Page页面。

        ```ts
        @Builder
        export function CustomPageBuilder() {
          CustomPage();
        }

        @Component
        export struct CustomPage {
          pathStack: NavPathStack = new NavPathStack();

          build() {
            NavDestination() {
              Column() {
                Button('跳转回HAP页面');
              }.width('100%').height('100%')
              .justifyContent(FlexAlign.Center)
              .onClick(() => {
                try {
                  this.pathStack.pushPathByName('Page', null, false); // 跳转到HAP下的页面
                } catch (error) {
                  console.error(`Failed to route. Code: ${error.code}, message:${error.message}`);
                }
              });
            }
            .onReady((context: NavDestinationContext) => {
              this.pathStack = context.pathStack;
            });
          }
        }
        ```

        ```json
        {
          "routerMap": [
            {
              "name": "CustomPage",
              "pageSourceFile": "src/main/ets/components/CustomPage2.ets",
              "buildFunction": "CustomPageBuilder"
            }
          ]
        }
        ```

* 方案二：Router路由配置。
  1. 在HAR模块内src/main/ets/components目录下创建CustomPage.ets文件，作为跳转目的页面，并给@Entry修饰的自定义组件[EntryOptions](../harmonyos-guides/arkts-create-custom-components.md)命名，内容如下：

     ```ts
     @Entry({ routeName: 'CustomPage' })
     @Component
     export struct CustomPage {
       build() {
         Column() {
           Button('跳转回HAP页面');
         }.width('100%').height('100%')
         .justifyContent(FlexAlign.Center)
         .onClick(() => {
           this.getUIContext().getRouter().pushUrl({
             url: 'pages/Page'
           });
         });
       }
     }
     ```
  2. HAR模块的Index.ets中导出组件。
  3. 在HAP模块的oh-package.json5文件中引用HAR模块。同方案一的步骤三。
  4. HAP模块的RouterSolution页面import引入HAR模块内跳转目标页面，并通过pushNamedRoute方法跳转。

     ```ts
     import 'testhar/src/main/ets/components/CustomPage';

     @Entry
     @Component
     struct RouterSolution {
       build() {
         Column() {
           Button('ToHarPage', { stateEffect: true, type: ButtonType.Capsule })
             .width('80%')
             .onClick(() => {
               // 跳转至目标testHar模块所在页面
               this.getUIContext().getRouter().pushNamedRoute({
                 name: 'CustomPage'
               });
             });
         }.width('100%').height('100%')
         .justifyContent(FlexAlign.Center);
       }
     }
     ```

**Q：使用pushNamedRoute跳转HAR页面时报100004错误（Named route error. The named route does not exist.）怎么办？**

**A**：该错误通常是因为未正确引入HAR中命名路由页面导致。请检查以下两点：

1. 确认当前应用包的oh-package.json5文件中已正确配置HAR模块依赖：

   ```json
   "dependencies": {
       "library": "file:../library"
   }
   ```
2. 确认执行跳转的页面中已import引入HAR中命名路由页面：

   ```json
   import 'library/Index';
   ```

**Q：如何实现Navigation和router的混用？**

A：对于router跳转到的页面需要使用Navigation作为根容器，才能在这个页面跳转到下个NavDestination页面。这是因为router跳转的是page页面，而NavDestination是Navigation的子组件，二者层次不同。以下为Navigation和router混用的三种常见场景：

* 场景一：Navigation页面与router页面间的跳转，如：入口页面->NavPageOne->RouterPageOne->NavPageTwo。该混用场景常见于"全局导航+局部导航"的页面设计，例如首页到隐私模块页面等。

  使用router跳转到RouterPageOne，RouterPageOne使用Navigation作为根容器跳转到NavPageTwo，这里RouterPageOne的Navigation和第一个Navigation相互独立，都有各自的路由栈，互不影响。开发者需参考[系统路由表](../harmonyos-guides/arkts-navigation-cross-package.md#系统路由表)配置Navigation路由，配置说明附在本文末尾。

  入口页面代码如下：需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

  ```ts
  @Entry
  @Component
  struct SceneOne {
    pageInfo: NavPathStack = new NavPathStack();

    build() {
      Navigation(this.pageInfo) {
        Column() {
          Button('ToNavDestinationOneByNavPathStack', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(24)
            .onClick(() => {
              this.pageInfo.pushPath({ name: 'NavPageOne' });
            });
        };
      }
      .title('NavIndex');
    }
  }
  ```

  NavPageOne页面代码如下：

  ```ts
  @Builder
  export function PageOneBuilder() {
    NavPageOne();
  }

  @Component
  struct NavPageOne {
    pageInfo: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Text('NavDestinationOne')
          .width('80%')
          .height(50)
          .margin(24);
        Button('ToRouterPage1ByRouter', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10)
          .onClick(() => {
            // 使用router跳转到下一个页面
            this.getUIContext().getRouter().pushUrl({
              url: 'pages/RouterPageOne'
            });
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  需注意router管理@Entry页面之间的跳转（页面级路由栈）。Navigation管理NavDestination组件之间的跳转（组件级路由栈），NavDestination作为Navigation的子组件存在，需搭配Navigation使用。若通过router跳转到一个需要承载NavDestination的页面，该页面（@Entry）必须用Navigation作为容器。

  RouterPageOne页面代码如下：需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

  ```ts
  @Entry
  @Component
  struct RouterPageOne {
    pageInfo: NavPathStack = new NavPathStack();

    build() {
      // 注意：使用NavDestination，会导致无法跳转到指定NavDestination
      // 使用Navigation，可以正常跳转
      Navigation(this.pageInfo) {
        Column() {
          Text('RouterPage1')
            .margin(24);
          Button('ToNavDestination2ByNavPathStack')
            .onClick(() => {
            this.pageInfo.pushPath({ name: 'NavPageTwo' });
          });
        };
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  NavPageTwo页面代码如下：

  ```ts
  @Builder
  export function PageTwoBuilder() {
    NavPageTwo();
  }

  @Component
  struct NavPageTwo {
    pageInfo: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Text('NavDestination2')
          .width('80%')
          .height(50)
          .margin(24);
        Button('pushPath', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(10);
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  | 无法跳转到NavPageTwo | 正常跳转到NavPageTwo |
  | --- | --- |
  |  |  |
  | RouterPageOne使用NavDestination作为根容器 | RouterPageOne使用Navigation作为根容器 |

* 场景二：使用router页面作为闪屏页，后续页面跳转由Navigation承载。

  使用router跳转到一个Navigation作为根容器的页面，然后清空router路由栈中的页面。

  闪屏页代码如下：需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

  ```ts
  @Entry
  @Component
  struct SceneTwo {
    @State message: string = '闪屏页';

    aboutToAppear(): void {
      setTimeout(() => {
        this.getUIContext().getRouter().replaceUrl({ url: 'pages/NavigationPage' });
      }, 2000);
    }

    build() {
      RelativeContainer() {
        Text(this.message)
          .id('HelloWorld')
          .fontSize($r('app.float.page_text_font_size'))
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          })
          .onClick(() => {
            this.message = 'Welcome';
          });
      }
      .height('100%')
      .width('100%');
    }
  }
  ```

  首页代码如下：需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

  ```ts
  @Entry
  @Component
  struct NavIndex {
    pageInfo: NavPathStack = new NavPathStack();

    build() {
      Navigation(this.pageInfo) {
        Column() {
          Button('ToNavDestinationOneByNavPathStack', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              this.pageInfo.pushPath({ name: 'pageOne' });
            });
        };
      }.title('NavIndex');
    }
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/64rJqDLRQdOdSCp5h0tyUg/zh-cn_image_0000002795328639.png "点击放大")

* 场景三：Navigation页面与router页面间的跳转为：入口页面->PageOne->pageTwo->RouterPage->PageThree。

  该混用场景常见于使用的三方SDK布局为router导航，且根容器不是Navigation。可以使用router的单例模式（[页面跳转](../harmonyos-guides/arkts-routing.md#页面跳转)的场景三）拉起Navigation首页，通过路由监听或者传参等方式控制Navigation首页跳转PageThree。

  入口页面代码如下：需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

  ```ts
  @Entry
  @Component
  struct SceneThree {
    pageInfos: NavPathStack = new NavPathStack();
    isUseInterception: boolean = false;

    onPageShow(): void {
      let rouNam: number | undefined = AppStorage.get('router');
      if (rouNam === 1) {
        this.getUIContext().getRouter().clear(); // 清除掉历史页面router
        this.pageInfos.pushDestination({ name: 'pageThree' }, false);
      }
    }

    build() {
      Stack() {
        Navigation(this.pageInfos) {
          Button('pageOne', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              this.pageInfos.pushPath({ name: 'pageOne' });
            });
        }
        .title('NavIndex')
        .titleMode(NavigationTitleMode.Mini);
      };
    }
  }
  ```

  PageOne页面代码如下：

  ```ts
  @Builder
  export function PageOneBuilder() {
    PageOne();
  }

  @Component
  export struct PageOne {
    pageInfos: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Column() {
          Button('pageTwo', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              this.pageInfos.pushPath({ name: 'pageTwo' });
            });
        }
        .width('100%')
        .height('100%');
      }
      .title('pageOne')
      .onBackPressed(() => {
        this.pageInfos.pop();
        return true;
      })
      .onReady((context: NavDestinationContext) => {
        this.pageInfos = context.pathStack;
      })
      .customTransition(null);
    }
  }
  ```

  PageTwo页面代码如下：

  ```ts
  @Builder
  export function PageTwoBuilder() {
    PageTwo();
  }

  @Component
  export struct PageTwo {
    pathStack: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Column() {
          Button('routerSDK客服页', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              this.getUIContext().getRouter().pushUrl({ url: 'pages/RouterPage' }, (err) => {
                if (err) {
                  console.error(`Failed to pushUrl, code is ${err.code}, message is ${err.message}`);
                  return;
                }
                console.info('Succeeded in pushUrl.');
              });
            });
          Button('pageThree', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              this.pathStack.pushDestination({ name: 'pageThree' });
            });

          Button('pop', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              this.pathStack.pop();
            });
        }
        .width('100%')
        .height('100%');
      }
      .title('pageTwo')
      .backgroundColor('#FFFFFF')
      .onBackPressed(() => {
        this.pathStack.pop();
        return true;
      })
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
      })
      .customTransition(null);
    }
  }
  ```

  RouterPage页面代码如下：需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

  ```ts
  import { router } from '@kit.ArkUI';

  @Entry
  @Component
  struct RouterPage {
    build() {
      Column() {
        Text('客服页');
        Button('router首页+拉起page3', { stateEffect: true, type: ButtonType.Capsule })
          .width('80%')
          .height(40)
          .margin(20)
          .onClick(() => {
            AppStorage.setOrCreate('router', 1);
            this.getUIContext().getRouter().pushUrl({ url: 'pages/SceneThree' }, router.RouterMode.Single, (err) => {
              if (err) {
                console.error(`Invoke pushUrl failed, code is ${err.code}, message is ${err.message}`);
                return;
              }
              console.info('Invoke pushUrl succeeded.');
            });
          });
      };
    }
  }
  ```

  PageThree页面代码如下：

  ```ts
  @Builder
  export function PageThreeBuilder() {
    PageThree();
  }

  @Component
  export struct PageThree {
    pathStack: NavPathStack = new NavPathStack();

    build() {
      NavDestination() {
        Column() {
          Button('pop', { stateEffect: true, type: ButtonType.Capsule })
            .width('80%')
            .height(40)
            .margin(20)
            .onClick(() => {
              AppStorage.delete('router');
              this.pathStack.pop();
            });
        }
        .width('100%')
        .height('100%');
      }
      .title('pageThree')
      .onBackPressed(() => {
        let rouNam: number | undefined = AppStorage.get('router');
        // 消除返回重影
        setTimeout(() => {
          this.pathStack?.pop();
        }, rouNam === 1 ? 500 : 0);
        if (rouNam === 1) {
          this.getUIContext().getRouter().clear(); // 清除掉历史页面router
          AppStorage.delete('router');
        }
        return true;
      })
      .onReady((context: NavDestinationContext) => {
        this.pathStack = context.pathStack;
      });
    }
  }
  ```

  上述场景的Navigation页面需进行路由配置，在src/main目录下的工程配置文件module.json5中的module字段里配置"routerMap": "$profile:router\_map"，并在src/main/resources/base/profile目录下新增router\_map.json文件。router\_map.json文件内容如下：

  ```json
  {
    "routerMap": [
      {
        "name": "pageOne",
        "pageSourceFile": "src/main/ets/pages/PageOne.ets",
        "buildFunction": "PageOneBuilder",
        "data": {
          "description": "this is pageOne"
        }
      },
      {
        "name": "pageTwo",
        "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
        "buildFunction": "PageTwoBuilder"
      },
      {
        "name": "pageThree",
        "pageSourceFile": "src/main/ets/pages/PageThree.ets",
        "buildFunction": "PageThreeBuilder"
      },
      {
        "name": "NavPageOne",
        "pageSourceFile": "src/main/ets/pages/SceneOne.ets",
        "buildFunction": "PageOneBuilder"
      },
      {
        "name": "NavPageTwo",
        "pageSourceFile": "src/main/ets/pages/SceneOne.ets",
        "buildFunction": "PageTwoBuilder"
      }
    ]
  }
  ```

  resources/base/profile/main\_pages.json配置如下：

  ```ts
  {
    "src": [
      "pages/SceneThree",
      "pages/RouterPageOne",
      "pages/SceneTwo",
      "pages/NavigationPage",
      "pages/SceneOne",
      "pages/RouterPage"
    ]
  }
  ```

  效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d4/v3/DeJPMs6_SI-nCZlgeJ1bBA/zh-cn_image_0000002795485233.png "点击放大")

**Q：页面使用组件导航实现路由跳转，期望自定义一个半屏组件能够始终保持在所有页面的顶部。**

**A**：

1. 若要实现顶层组件处于最顶层可以通过Stack层叠布局实现，在Stack内需要置顶的组件的[Z序控制（zIndex）](../harmonyos-references/ts-universal-attributes-z-order.md#zindex)值置为最高，如代码中Navigation组件的zIndex为1，TextInput组件的zIndex为2，那TextInput将会显示在Navigation上层。

   ```ts
   @Entry
   @Component
   struct NavigationExample {
     pageInfos: NavPathStack = new NavPathStack();

     build() {
       Column() {
         Stack() {
           Navigation(this.pageInfos) {
             Column({ space: 12 }) {
               Button('页面一', { stateEffect: true, type: ButtonType.Capsule })
                 .width('75%')
                 .height('30')
                 .onClick(() => {
                   // 点击筛选后的列表项跳转到展示页面
                   this.pageInfos.pushPathByName('PageOne', null);
                 })
               Button('页面二', { stateEffect: true, type: ButtonType.Capsule })
                 .width('75%')
                 .height('30')
                 .onClick(() => {
                   this.pageInfos.pushPathByName('PageTwo', null);
                 })
             }
             .width('100%')
             .height('100%')
             .justifyContent(FlexAlign.Start)
           }
           .title('Page')
           .zIndex(1)

           TextInput({ placeholder: '请输入内容' })
             .zIndex(2)
             .width('100%')
             .height(300)
             .position({ bottom: 0 })
             .alignSelf(ItemAlign.Center)
         }

       }
     }
   }
   ```
2. 在底层组件中通过[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)的[pushPathByName](../harmonyos-references/ts-basic-components-navigation.md#pushpathbyname10)传入指定页面实现跳转，同时保证顶层组件不变。

   页面一代码：

   ```ts
   @Builder
   export function PageOneBuilder() {
     PageOne()
   }

   @Entry
   @Component
   export struct PageOne {
     pageInfos: NavPathStack = new NavPathStack();
     keyWord: string = 'page one';

     build() {
       NavDestination() {
         Column({ space: 12 }) {
           Button('页面二', { stateEffect: true, type: ButtonType.Capsule })
             .width('75%')
             .height('30')
             .onClick(() => {
               this.pageInfos.pushPathByName('PageTwo', this.keyWord);
             })

         }
         .width('100%')
         .height('100%')
         .justifyContent(FlexAlign.Start)

       }
       .title('页面一')
       .onReady((context: NavDestinationContext) => {
         this.pageInfos = context.pathStack;
       })
     }
   }
   ```

   页面二代码：

   ```ts
   @Builder
   export function PageTwoBuilder() {
     PageTwo()
   }

   @Entry
   @Component
   export struct PageTwo {
     pageInfos: NavPathStack = new NavPathStack();
     keyWord: string = '';

     build() {
       NavDestination() {
         Column({ space: 12 }) {
           Button('页面一', { stateEffect: true, type: ButtonType.Capsule })
             .width('75%')
             .height('30')
             .onClick(() => {
               this.pageInfos.pushPathByName('PageOne', null);
             })
         }
         .width('100%')
         .height('100%')
         .justifyContent(FlexAlign.Start)
       }
       .title('页面二')
       .onReady((context: NavDestinationContext) => {
         this.pageInfos = context.pathStack;
       })
     }
   }
   ```

   router\_map.json配置如下：

   ```json
   {
     "routerMap": [
       {
         "name": "PageOne",
         "pageSourceFile": "src/main/ets/pages/PageOne.ets",
         "buildFunction": "PageOneBuilder"
       },
       {
         "name": "PageTwo",
         "pageSourceFile": "src/main/ets/pages/PageTwo.ets",
         "buildFunction": "PageTwoBuilder"
       }
     ]
   }
   ```

**Q：pushPathByName传入的路径为字符串，页面名称是否区分大小写？**

A：区分大小写，如果传入的页面名称和实际的页面名称不一致会导致需跳转页面无法显示。

**Q：如何实现跨模块的页面跳转功能？**

A：在业务体系庞大或复杂的情况下，会将业务拆分成多个子业务模块，每个子业务模块为一个HAR/HSP。在该场景下，存在从主业务入口跳转到不同子页面模块，或从一个子业务模块A页面跳转到另一个子业务模块B页面的需求。例如，从应用首页跳转到登录子业务模块页面。针对该场景，有以下三种解决方案：

* 方案一：使用router的命名路由接口router.pushNamedRoute()跳转。

  参考地址：[页面路由 (@ohos.router)](../harmonyos-guides/arkts-routing.md)。
* 方案二：使用navigation组件跳转。
  1. 以从应用入口模块的页面NavigationPage跳转到Login子业务模块页面LoginPage为例。主要包含以下步骤：

     在Login模块中开发自定义组件LoginPage作为路由跳转目的地，并对外导出。

     ```ts
     @Component
     export struct LoginPage {
       @Consume('pathStack') pathStack: NavPathStack;
       @State message: string = 'Login Page';

       build() {
         NavDestination() {
           Column() {
             Text(this.message)
               .fontSize(50)
               .fontWeight(FontWeight.Bold)
           }
           .width('100%')
           .height('100%')
         }
         .onBackPressed(() => {
           this.pathStack.pop();
           return true;
         })
       }
     }
     ```
  2. 在Login模块的入口文件Index.ets中导出自定义组件。export \{ LoginPage \} from './src/main/ets/pages/loginPage';。
  3. 在入口模块的oh-package.json5文件中添加对Login模块的依赖项。

     ```ts
     {
       // ...
       "dependencies": {
         "@ohos/login": "file:../LoginModule"
       }
     }
     ```
  4. 入口模块导入Login模块的自定义组件，并添加到Navigation组件的路由表中。

     ```ts
     // Import a custom component of the Login module
     import { LoginPage } from '@ohos/login';

     @Entry
     @Component
     struct NavigationPage {
       @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();

       @Builder
       pageMap(name: string) {
         if (name === 'loginPage') {
           LoginPage()
         }
       }

       build() {
         Navigation(this.pathStack) {
           Button('jump to login page')
             .onClick(() => {
               // The second parameter of NavPathInfo is a custom parameter that can be used for message transfer
               let pathInfo: NavPathInfo = new NavPathInfo('loginPage', new Object());
               this.pathStack.pushDestination(pathInfo, true);
             })
         }
         .navDestination(this.pageMap)
       }
     }
     ```

* 方案三：使用基于navigation组件的自定义路由框架跳转。

  方案二虽然可以实现跨模块跳转的功能，但当模块间跳转需求增多，各个模块间将存在非常复杂的依赖关系，甚至会导致多个HAR/HSP间循环依赖。为了解决模块间的强耦合关系，并且提升页面加载性能，推荐[跨包路由](../harmonyos-guides/arkts-router-to-navigation.md#跨包路由)。

**Q：通过卡片热启动应用，如何跳转至指定的Navigation路由栈中的页面？**

**A**：

方案一：作为Navigation的根页面，首页不会被销毁，且页面上含有NavPathStack变量，可以进行页面跳转操作。通过在页面生命周期函数中发布事件通知首页，进行页面跳转操作。热启动的示例代码如下：

1. 热启动：在被拉起方UIAbility的[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)方法中（若UIAbility文件无此方法，则自行增加即可），通过[EventHub.emit](../harmonyos-references/js-apis-inner-application-eventhub.md#eventhubemit)触发事件。

   ```ts
   this.context.eventHub.emit('navigation', want.parameters?.path?.toString());
   ```
2. 在Navigation的根页面通过[EventHub.on](../harmonyos-references/js-apis-inner-application-eventhub.md#eventhubon)订阅事件，跳转指定页面。

   ```ts
   aboutToAppear(): void {
       this.getUIContext().getHostContext()?.eventHub.on('navigation', (path: string) => {
         let paths = this.navPathStack.getAllPathName();
         if (paths.slice().pop() === path) {
           return;
         }
         this.navPathStack.pushPath({ name: path }, false);
       });
     }
   ```

方案二：封装NavPathStack，在onNewWant生命周期中通过getAllPathName获取栈中所有NavDestination页面的名称，判断当前页面是否为目标页面，再决定是否用NavPathStack将目标页面push至栈顶。

1. 封装全局的NavPathStack变量。RouterModule.ets文件。

   ```ts
   export class RouterModule {
     private static pathStack: NavPathStack = new NavPathStack();

     static setRouterStack(pathStack: NavPathStack) {
       RouterModule.pathStack = pathStack;
     }

     static getRouterStatic() {
       return RouterModule.pathStack;
     }
   }
   ```
2. 在被拉起方UIAbility的[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)方法中（若UIAbility文件无此方法，则自行增加即可），执行判断和跳转操作。

   ```ts
   const pathStack = RouterModule.getRouterStatic();
       let param = want.parameters as Record<string, Object>;
       let backPage = param.message as string;
       if (pathStack.getAllPathName().slice().pop() === backPage) {
         return;
       }
       const pathInfo = new NavPathInfo(backPage, null);
       pathStack.pushPath(pathInfo);
   ```

完整示例如下：

新增工程项目后，此时存在一个entry类型的HAP包（作为拉起方），再新增一个feature类型的HAP（被拉起方）。参考不同类型[HAP](../harmonyos-guides/hap-package.md)的说明。

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/sXztNa9TQkCE1WCu2nk55A/zh-cn_image_0000002766086698.png)

1. 拉起方（entry模块）的示例代码如下，请根据实际的HAP信息更新want参数：

   ```ts
   import { common } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   const BUNDLE_NAME: string = 'com.example.NewWantDemo'; // 在应用app.json5文件中'bundleName'节点获得
   const ABILITY_NAME: string = 'TargetAbility'; // 在HAP包的对应Ability文件中获得

   @Entry
   @Component
   struct HAPRouterDemo {
     private context?: common.UIAbilityContext; // 创建context实例

     aboutToAppear(): void {
       this.context = this.getUIContext().getHostContext() as common.UIAbilityContext; // 获取当前页面关联的UIAbilityContext
     }

     jumpHap() {
       if (this.context) {
         // 启动Ability，拉起HAP模块的UIAbility实例
         this.context.startAbility({
           bundleName: BUNDLE_NAME,
           abilityName: ABILITY_NAME,
           parameters: {
             'path': 'NavDesPage'
           }
         }).then(() => {
           console.info('start audio ability success');
         }).catch((error: BusinessError) => {
           console.error(`start audio ability failed, error: ${error}`);
         });
       }
     }

     build() {
       Column() {
         Button('startAbility跳转HAP')
           .onClick(() => {
             this.jumpHap();
           });
       }
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%');
     }
   }
   ```
2. 被拉起方（target模块）的示例代码如下：

   ```ts
   import { RouterModule } from './RouterModule';

   @Entry
   @Component
   struct Solution1 {
     navPathStack: NavPathStack = RouterModule.getRouterStatic();

     aboutToAppear(): void {
       this.getUIContext().getHostContext()?.eventHub.on('navigation', (path: string) => {
         let paths = this.navPathStack.getAllPathName();
         if (paths.slice().pop() === path) {
           return;
         }
         this.navPathStack.pushPath({ name: path }, false);
       });
     }

     @Builder
     pageMap(name: string) {
       if (name === 'NavDesPage') {
         NavDesPage();
       }
     }

     build() {
       Navigation(this.navPathStack) {
         Column() {
           Button('跳转NavDestination')
             .onClick(() => {
               this.navPathStack.pushPathByName('NavDesPage', null, false);
             });
         }.height('100%').width('100%').justifyContent(FlexAlign.Center);
       }.navDestination(this.pageMap)
       .height('100%').width('100%');
     }
   }

   @Component
   struct NavDesPage {
     navPathStack: NavPathStack = new NavPathStack();

     build() {
       NavDestination() {
         Text('NavDesPage')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           });
       }
       .onReady((ctx: NavDestinationContext) => {
         this.navPathStack = ctx.pathStack;
       })
       .height('100%')
       .width('100%');
     }
   }
   ```
3. 按照方案的描述修改被拉起方的UIAbility文件（示例中为TargetAbility.ets）的onNewWant方法（若UIAbility文件无此方法，则参照背景知识中介绍自行增加onNewWant即可）。
4. 分别编译target模块和entry模块，再运行entry模块即可。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/7ChPX1jFRJSDJBGbFTvL8A/zh-cn_image_0000002766086704.png)

**Q：热启动，如何每次启动都重新打开目标页面？**

**A**：可通过上述两种方案getAllPathName获取到栈中所有NavDestination页面的名称，判断目标页面是否在栈内，如在栈内则通过[removeByName](../harmonyos-references/ts-basic-components-navigation.md#removebyname11)将目标页面从页面栈内删除，再通过pushPath入栈，达到重新打开的效果。示例代码如下：结合上述方案二，在UIAbility文件的[onNewWant](../harmonyos-references/js-apis-app-ability-uiability.md#onnewwant)方法中增加以下代码（若UIAbility文件无此方法，则自行增加即可）。

```ts
const pathStack = RouterModule.getRouterStatic();
    let param = want.parameters as Record<string, Object>;
    let targetPage = param.message as string;
    const isPageBInStack = pathStack.getAllPathName().indexOf(targetPage) !== -1;
    if (isPageBInStack) {
      pathStack.removeByName(targetPage);
      const pathInfo = new NavPathInfo(targetPage, null);
      pathStack.pushPath(pathInfo);
    } else {
      const pathInfo = new NavPathInfo(targetPage, null);
      pathStack.pushPath(pathInfo);
    }
```
