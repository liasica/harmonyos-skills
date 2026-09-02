---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1442
title: 解决不同路由页面存在相同组件id导致组件无法获焦的问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 解决不同路由页面存在相同组件id导致组件无法获焦的问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:f9ea6f473b29d70e3becf543d6e1650dd46b48a7b76811f10265f9a66d767740
---

## 问题现象

页面一使用requestFocus通过组件id获焦成功，然后路由至页面二，再然后路由至页面一，此时为什么无法使用requestFocus通过组件id获焦？

主页代码示例参考如下：

```ts
// 主页
@Entry
@Component
struct NavigationIndex {
  @Provide('pathInfos') pathInfos: NavPathStack = new NavPathStack();
  private listArray: string[] = ['WLAN', 'Connect & Share'];

  build() {
    Column() {
      Navigation(this.pathInfos) {
        TextInput({ placeholder: '输入关键字搜索' })
          .width('90%')
          .height(40)
          .margin({ bottom: 10 });
        // 通过List定义导航的一级界面
        List({ space: 12, initialIndex: 0 }) {
          ForEach(this.listArray, (item: string) => {
            ListItem() {
              Row() {
                Row() {
                  Text(`${item.slice(0, 1)}`)
                    .fontColor(Color.White)
                    .fontSize(14)
                    .fontWeight(FontWeight.Bold);
                }
                .width(30)
                .height(30)
                .backgroundColor('#a8a8a8')
                .margin({ right: 20 })
                .borderRadius(20)
                .justifyContent(FlexAlign.Center);

                Column() {
                  Text(item)
                    .fontSize(16)
                    .margin({ bottom: 5 });
                }
                .alignItems(HorizontalAlign.Start);

                Blank();
                Row()
                  .width(12)
                  .height(12)
                  .margin({ right: 15 })
                  .border({
                    width: { top: 2, right: 2 },
                    color: 0xcccccc
                  })
                  .rotate({ angle: 45 });
              }
              .borderRadius(15)
              .shadow({ radius: 100, color: '#ededed' })
              .width('90%')
              .alignItems(VerticalAlign.Center)
              .padding({ left: 15, top: 15, bottom: 15 })
              .backgroundColor(Color.White);
            }
            .width('100%')
            .onClick(() => {
              this.pathInfos.pushPathByName(`${item}`, '');
            });
          }, (item: string): string => item);
        }
        .listDirection(Axis.Vertical)
        .edgeEffect(EdgeEffect.Spring)
        .sticky(StickyStyle.Header)
        .chainAnimation(false)
        .width('100%');
      }
      .width('100%')
      .mode(NavigationMode.Auto)
      .title('设置'); // 设置标题文字
    }
    .size({ width: '100%', height: '100%' })
    .backgroundColor(0xf4f4f5);
  }
}
```

页面一代码示例参考如下：

```ts
// 页面一
@Builder
export function PageOneBuilder(name: string) {
  PageOne({ name: name });
}

@Component
struct PageOne {
  pathInfos: NavPathStack = new NavPathStack();
  name: string = '';
  @State isShow: boolean = false;

  @Builder
  textBuilder(id: string) {
    TextInput()
      .width('90%')
      .id(id)
      .onSubmit(() => {
        this.isShow = true;
      })
      .onAppear(() => {
        try {
          this.getUIContext().getFocusController().requestFocus(id);
          console.info(`Succeeded in appearing component. name: ${this.name}, id ${id}.`);
        } catch (e) {
          console.error(`Failed to appear component. code: ${e.code}, message: ${e.message}`);
        }
      });
  }

  build() {
    NavDestination() {
      Column({ space: 24 }) {
        this.textBuilder(`${this.name}1`);
        if (this.isShow) {
          this.textBuilder(`${this.name}2`);
        }
        Button('next')
          .width('50%')
          .height(40)
          .margin({ top: 50 })
          .onClick(() => {
            // 弹出路由栈栈顶元素，跳转'Connect & Share'页面
            this.pathInfos.pushPathByName(`Connect & Share`, '');
          });
      }
      .size({ width: '100%', height: '100%' });
    }
    .title(`${this.name}`)
    .onReady((ctx: NavDestinationContext) => {
      // NavDestinationContext获取当前所在的导航控制器
      this.pathInfos = ctx.pathStack;
    })
    .onShown(() => {
      this.isShow = false;
    });
  }
}
```

页面二跳转页面一代码示例参考如下：

```ts
// 页面二
@Builder
export function PageTwoBuilder(name: string) {
  PageTwo({ name: name });
}

@Component
struct PageTwo {
  pathInfos: NavPathStack = new NavPathStack();
  name: string = '';
  @State isShow: boolean = false;

  build() {
    NavDestination() {
      Column({ space: 5 }) {
        Button('next')
          .width('50%')
          .height(40)
          .margin({ top: 5 })
          .onClick(() => {
            // 跳转到WLAN
            this.pathInfos.pushPath({ name: 'WLAN', param: '' });
          });
      }
      .size({ width: '100%', height: '100%' });
    }
    .title(`${this.name}`)
    .onReady((ctx: NavDestinationContext) => {
      // NavDestinationContext获取当前所在的导航控制器
      this.pathInfos = ctx.pathStack;
    })
    .onShown(() => {
      this.isShow = false;
    });
  }
}
```

## 背景知识

* [Navigation](../harmonyos-references/ts-basic-components-navigation.md)组件是路由导航的根视图容器，一般作为Page页面的根容器使用，其内部默认包含了标题栏、内容区和工具栏。其中[NavPathStack](../harmonyos-references/ts-basic-components-navigation.md#navpathstack10)导航控制器提供多种跳转方式，具体参考[LaunchMode](../harmonyos-references/ts-basic-components-navigation.md#launchmode12枚举说明)。
* [组件标识（id）](../harmonyos-references/ts-universal-attributes-component-id.md)为组件的唯一标识，在整个应用内唯一。

## 问题定位

当由页面一路由至页面二后，页面二重新路由至页面一，传参保持不变，组件最后id为“WLAN1”和“WLAN2”，与路由栈内存在的页面一组件id一致，因此id赋值失败，requestFocus找不到对应组件。报错信息如下：

```shell
Error code: 150003, Error message: The component doesn't exist, is currently invisible, or has been disabled.
```

## 分析结论

路由栈内存在已有同id组件，因此新页面组件id赋值失败，requestFocus找不到对应组件。

## 修改建议

路由逻辑：主页跳转页面一，页面一跳转页面二，页面二跳转页面一。

**方案一**：消除同id组件。

* 方式一：页面一跳转页面二时，跳转方法使用replacePathByName，用新页面替换旧组件所在页面。

  ```ts
  // 弹出路由栈栈顶元素，跳转'Connect & Share'页面
  this.pathInfos.replacePathByName(`Connect & Share`, '详情页面参数');
  ```
* 方式二：页面二跳转页面一时，跳转模式MOVE\_TO\_TOP\_SINGLETON或者POP\_TO\_SINGLETON，使用原页面。

  ```ts
  // 跳转到WLAN
  this.pathInfos.pushPath({ name: 'WLAN', param: '' }, { launchMode: LaunchMode.MOVE_TO_TOP_SINGLETON });
  ```

**方案二**：使用新的组件id。

根据页面传入的不同数据，重新命名id。name参数或者param参数均可，如下例子为name参数。

主页跳转页面一：

```ts
this.pathInfos.pushPathByName('WLAN', '');
```

页面二跳转页面一：

```ts
this.pathInfos.pushPathByName('Bluetooth', '');
```

路由表router\_map.json如下：

```json
{
  "routerMap": [
    {
      "name": "WLAN",
      "pageSourceFile": "src/main/ets/pages/ProblemPage.ets",
      "buildFunction": "PageOneBuilder"
    },
    {
      "name": "Bluetooth",
      "pageSourceFile": "src/main/ets/pages/ProblemPage.ets",
      "buildFunction": "PageOneBuilder"
    },
    {
      "name": "Connect & Share",
      "pageSourceFile": "src/main/ets/pages/ProblemPage.ets",
      "buildFunction": "PageTwoBuilder"
    }
  ]
}
```

## 常见FAQ

Q：使用HMRouter三方库进行页面跳转是否也有上述问题？

A：有上述问题。[HMRouter](https://ohpm.openharmony.cn/#/cn/detail/@hadss%2Fhmrouter)三方库是基于Navigation实现的。

Q：为什么使用replace没有出现上述问题？

A：本质原因是路由栈中只有一个页面一，因此无重复使用同一id问题。首先页面一跳转页面二使用replace，此情况下栈中只存在页面二，下次跳转页面一后，栈中只有一个页面一。其次页面二跳转页面一使用MOVE\_TO\_TOP\_SINGLETON或者POP\_TO\_SINGLETON跳转模式，此模式为单例跳转，跳转后栈中只存在一个页面一。

## 总结

id为组件的唯一标识，在整个应用内唯一。其他组件不可使用已命名的id，同时id命名以最新的id为准。
