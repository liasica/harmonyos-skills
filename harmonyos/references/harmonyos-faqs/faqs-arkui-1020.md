---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1020
title: Tabs预加载的实现方式及常见问题
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > Tabs预加载的实现方式及常见问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:05+08:00
doc_updated_at: 2026-08-19
content_hash: sha256:ad6f1ac2867a3fd17388072e7d42ba4e31953ef7aae603fa4c6c468f33e39ab5
---

## 问题现象

使用Tabs组件承载内容视图时，为了优化页面加载速度、提高用户体验，通常会考虑对子页内容预加载。在实现预加载的过程中，可能会遇到以下问题场景：

* 场景一：在aboutToAppear生命周期中使用preloadItems方法预加载TabContent未生效。

  案例代码如下，被预加载子组件的aboutToAppear函数未执行，说明预加载未生效。MyComponent组件实现代码见文末。

  ```ts
    @Entry
    @Component
    struct PreloadOnAppear {
      @State currentIndex: number = 1;
      private tabsController: TabsController = new TabsController();
      contentList: string[] = ['飞机', '铁路', '自驾', '地铁'];

      aboutToAppear(): void {
        // 预加载第0、2、3个子节点，提高滑动或点击切换至这些节点时的性能
        this.tabsController.preloadItems([0, 2, 3]);
      }

      build() {
        Column() {
          Tabs({ index: this.currentIndex, controller: this.tabsController }) {
            ForEach(this.contentList, (item: string, index: number) => {
              TabContent() {
                MyComponent({ info: item });
              }.tabBar(SubTabBarStyle.of(`页签${index}`));
            });
          }
          .onChange((index: number) => {
            this.currentIndex = index;
          });
        }.width('100%').height('100%');
      }
    }
  ```
* 场景二：当TabContent数量较多时，一次性预加载全部TabContent对性能压力大，如何分批加载子节点。
* 场景三：使用preloadItems预加载Tabs子节点时，tabBar使用@Builder（CustomBuilder类型）自定义构建，预加载过程中CustomBuilder会重建，导致tabBar组件出现闪烁。

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
* [TabContent](../harmonyos-references/ts-container-tabcontent.md)：仅在Tabs中使用，对应一个切换页签的内容视图。
* [preloadItems](../harmonyos-references/ts-container-tabs.md#preloaditems12)：控制Tabs预加载指定子节点。调用该接口后会一次性加载所有指定的子节点，因此为了性能考虑，建议分批加载子节点。
  + Tabs的preloadItems需要在Tabs创建之后去调用，首次预加载推荐在Tabs的[onAppear](../harmonyos-references/ts-universal-events-show-hide.md#onappear)生命周期中去控制。
  + 如果[TabsController](../harmonyos-references/ts-container-tabs.md#tabscontroller)对象未绑定任何Tabs组件，直接调用该接口，会抛出JS异常。因此使用该接口时，建议通过try-catch捕获异常。
* [CustomBuilder](../harmonyos-references/ts-types.md#custombuilder8)：一种用于自定义构建内容的类型，通常通过[@Builder](../harmonyos-guides/arkts-extend-components-overview.md#builder装饰器)装饰的函数实现。在使用preloadItems预加载时，CustomBuilder类型的tabBar会重建，可能导致组件闪烁。
* [ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)：用于封装组件内容的对象，可作为tabBar的参数类型，在预加载场景下不会出现重建问题。

## 解决方案

| 问题场景 | 问题描述 | 解决方案 |
| --- | --- | --- |
| 场景一 | 在aboutToAppear生命周期中使用preloadItems方法预加载TabContent未生效。 | 确保预加载在Tabs和TabsController绑定后执行，如在onAppear中执行预加载逻辑。 |
| 场景二 | 当TabContent数量较多时，一次性预加载全部TabContent对性能压力大，如何分批加载子节点。 | 和页签切换事件绑定，切换至某页签时，预加载当前页签的前后N项子页内容。 |
| 场景三 | 使用preloadItems预加载时，tabBar使用@Builder自定义构建导致组件闪烁。 | 使用BottomTabBarStyle、SubTabBarStyle或ComponentContent替代CustomBuilder实现tabBar。 |

**说明**：下述方案中使用的MyComponent代码附在文章末尾。

**场景一**：在aboutToAppear生命周期中使用preloadItems方法预加载TabContent未生效。

* 原因：预加载时机错误，[aboutToAppear](../harmonyos-references/ts-custom-component-lifecycle.md#abouttoappear)在build()函数执行前调用，此时Tabs组件未和TabsController绑定，预加载会失效。
* 解决方案：确保预加载操作在Tabs与TabsController绑定之后执行，可参考以下生命周期函数进行实现。
  + 自定义组件的[onDidBuild](../harmonyos-references/ts-custom-component-lifecycle.md#ondidbuild12)周期函数，在自定义组件的build()函数执行后调用。
  + Tabs的[onAppear](../harmonyos-references/ts-universal-events-show-hide.md#onappear)生命周期，Tabs组件挂载完成后触发。

以在onAppear中预加载为例：PreloadOnAppear.ets文件代码如下，@Entry页面需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { MyComponent } from './MyComponent';

@Entry
@Component
struct PreloadOnAppear {
  @State currentIndex: number = 1;
  private tabsController: TabsController = new TabsController();
  contentList: string[] = ['飞机', '铁路', '自驾', '地铁'];

  build() {
    Column() {
      Tabs({ index: this.currentIndex, controller: this.tabsController }) {
        ForEach(this.contentList, (item: string, index: number) => {
          TabContent() {
            MyComponent({ info: item });
          }.tabBar(SubTabBarStyle.of(`页签${index}`));
        });
      }
      .onAppear(() => {
        // 预加载第0、2、3个子节点，提高滑动或点击切换至这些节点时的性能
        this.tabsController.preloadItems([0, 2, 3])
          .then(() => {
            console.info('preloadItems success.');
          })
          .catch((error: BusinessError) => {
            console.error(`preloadItems failed, error code: ${error.code}, error message: ${error.message}`);
          });
      })
      .onChange((index: number) => {
        this.currentIndex = index;
      });
    }.width('100%').height('100%');
  }
}
```

**场景二**：当TabContent数量较多时，一次性预加载全部TabContent对性能压力大，如何分批加载子节点。

* 解决方案：和页签切换[onChange](../harmonyos-references/ts-container-tabs.md#onchange)事件绑定，跳转指定页签后，加载当前页签前后N项子节点。

以加载当前页签前后1项子节点为例：PreloadByBatches.ets文件代码如下，@Entry页面需在resources/base/profile/main\_pages.json配置，参考[pages标签](../harmonyos-guides/module-configuration-file.md#pages标签)。

```ts
import { BusinessError } from '@kit.BasicServicesKit';
import { MyComponent } from './MyComponent';

@Entry
@Component
struct PreloadByBatches {
  @State currentIndex: number = 0;
  private tabsController: TabsController = new TabsController();
  contentList: string[] = ['飞机', '铁路', '自驾', '地铁', '公交', '骑行', '跑步', '轮船'];

  build() {
    Column() {
      Tabs({ index: this.currentIndex, controller: this.tabsController }) {
        ForEach(this.contentList, (item: string, index: number) => {
          TabContent() {
            MyComponent({ info: item });
          }.tabBar(SubTabBarStyle.of(`页签${index}`));
        });
      }
      .barMode(BarMode.Scrollable)
      .onChange((index: number) => {
        this.currentIndex = index;
        let arr: number[] = [];
        if (index > 0) {
          arr.push(index - 1);
        }
        if (index < this.contentList.length - 1) {
          arr.push(index + 1);
        }
        // 预加载当前页签的前一项和后一项，边界页签除外
        this.tabsController.preloadItems(arr)
          .then(() => {
            console.info('preloadItems success.');
          })
          .catch((error: BusinessError) => {
            console.error(`preloadItems failed, error code: ${error.code}, error message: ${error.message}`);
          });
      });
    }.width('100%').height('100%');
  }
}
```

**场景三**：使用preloadItems预加载Tabs子节点时，tabBar使用@Builder自定义构建导致组件闪烁。

* 原因：使用preloadItems预加载时，tabBar参数类型为CustomBuilder的场景下，CustomBuilder会重建，导致组件出现闪烁。
* 解决方案：使用[BottomTabBarStyle](../harmonyos-references/ts-container-tabcontent.md#bottomtabbarstyle9)、[SubTabBarStyle](../harmonyos-references/ts-container-tabcontent.md#subtabbarstyle9)或[ComponentContent](../harmonyos-references/js-apis-arkui-componentcontent.md)替代CustomBuilder实现tabBar内容，避免预加载时的重建闪烁问题。通过ComponentContent预加载子节点的示例可参考[通过ComponentContent预加载子节点](../harmonyos-references/ts-container-tabcontent.md#示例10通过componentcontent预加载子节点)。

上述方案使用的MyComponent.ets文件代码如下：

```ts
@Component
export struct MyComponent {
  private info: string = '';

  // 预加载组件的aboutToAppear函数会被调用
  aboutToAppear(): void {
    console.info(`aboutToAppear: ${this.info}`);
  }

  aboutToDisappear(): void {
    console.info(`aboutToDisappear: ${this.info}`);
  }

  build() {
    Column() {
      Text(this.info);
    }.justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%');
  }
}
```

## 常见FAQ

Q：Tabs预加载的适用场景？

A：TabContent加载数据较多时，或者有网络请求等，通过预加载可以避免切换卡顿、子页加载缓慢等问题。

Q：在Tabs组件中添加多个TabContent时，节点树中TabBar的子节点数量始终比实际TabContent的数量多两个，但TabContent的数量是正确的。这种现象的原因是什么？

A：当使用ForEach动态生成TabBar时，框架会默认创建2个额外的缓存节点用于预加载优化，额外节点不会影响功能逻辑和性能。

Q：Tabs组件预加载生效之后会调用子组件的aboutToAppear方法吗？

A：被预加载的TabContent中的对应控件的aboutToAppear方法会被调用，可以添加日志来验证。

Q：为什么页面组件在TabContent加载的时候只调用aboutToAppear，不调用onPageShow？

A：onPageShow是@Entry页面的生命周期，Tabs切换触发的是组件级的生命周期aboutToAppear。
