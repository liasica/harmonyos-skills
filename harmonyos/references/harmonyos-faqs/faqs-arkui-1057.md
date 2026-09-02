---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1057
title: 如何监听Tabs切换
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何监听Tabs切换
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:95f261f609886b53abc102e34ee06266014255ff2e37376988efede8caa83fc1
---

## 问题现象

在多标签页应用中，可以通过监听Tabs页签切换，来实现数据按需加载的能力，如：切换到新页签时，暂停当前页的视频、音频播放等。常见的监听Tabs切换场景如下：

场景一：如何在Tabs组件切换时实现全局监听？

场景二：如何实现对TabContent组件可见状态变化的监听？

## 背景知识

* [Tabs](../harmonyos-references/ts-container-tabs.md)：通过页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
* [uiObserver.on('tabContentUpdate')](../harmonyos-references/js-apis-arkui-observer.md#uiobserverontabcontentupdate12-1)：监听指定Tabs组件id的TabContent页面切换事件。
* [onVisibleAreaChange](../harmonyos-references/ts-universal-component-visible-area-change-event.md#onvisibleareachange)：组件可见区域的时候触发该回调。
* [onWillShow](../harmonyos-references/ts-container-tabcontent.md#onwillshow12)：TabContent将要显示的时候触发该回调。
* [onWillHide](../harmonyos-references/ts-container-tabcontent.md#onwillhide12)：TabContent将要隐藏的时候触发该回调。

## 解决方案

实现方案如下：

|  |  |  |  |
| --- | --- | --- | --- |
| 应用场景 | 实现方案 | 实现效果 | 方案对比 |
| **场景一：在Tabs组件切换时实现全局监听。** | 方案：使用uiObserver.on('tabContentUpdate')实现监听。 | 不依赖组件内部逻辑，实现全局解耦。可获取TabContent的tabContentId、state、index等切换信息。 | / |
| **场景二：实现对TabContent组件可见状态变化的监听。** | 方案一：使用onWillShow和onWillHide实现监听。 | onWillShow在TabContent即将完全显示前打开视频，onWillHide在TabContent即将完全隐藏前关闭视频。 | 仅支持监听所绑定的单个TabContent显隐。 |
| 方案二：使用onVisibleAreaChange实现监听。 | 进入监听范围开启视频，离开监听范围关闭视频。 | 可精细监听组件在屏幕内的可见区域变化。 |
| 方案三：使用uiObserver.on('tabContentUpdate')实现监听。 | TabContent组件的状态state为ON\_SHOW打开视频，为ON\_HIDE关闭视频。 | 监听Tabs内所有TabContent的信息监听。 |

* **场景一：在Tabs组件切换时实现全局监听。**
  + **方案：使用uiObserver.on('tabContentUpdate')实现监听。**

    uiObserver.on('tabContentUpdate')在TabContent显示状态变化时自动触发回调。该机制不依赖组件内部逻辑，实现全局解耦。参考代码如下：

    ```ts
    import { uiObserver } from '@kit.ArkUI';

    @Entry
    @Component
    struct GlobalPage {
      tabList: string[] = ['首页', '发现', '推荐', '我的'];

      aboutToAppear(): void {
        uiObserver.on('tabContentUpdate', { id: 'tabsId' }, (info: uiObserver.TabContentInfo) => {
          console.info(`Succeeded in getting information.tabContentId:${info.tabContentId},state:${info.state},index:${info.index}.`);
        });
      }

      aboutToDisappear(): void {
        uiObserver.off('tabContentUpdate');
      }

      build() {
        Tabs({ barPosition: BarPosition.End }) {
          ForEach(this.tabList, (item: string, index: number) => {
            TabContent() {
              Text(item)
                .fontSize(18);
            }
            .id(`tabsId${index}`)
            .tabBar(`${item}`);
          });
        }
        .id('tabsId')
        .width('100%')
        .height('100%');
      }
    }
    ```
* **场景二：实现对TabContent组件可见状态变化的监听。**

  本场景以页签切换时根据TabContent组件的可见性变化，实现对视频组件播放状态的动态控制为例进行说明。视频组件代码如下：

  ```ts
  @Reusable
  @Component
  export struct VideoComponent {
    @Prop item: number = 0;
    controller: VideoController | undefined = undefined;

    build() {
      Column() {
        Text(`第${(this.item + 1)}个组件页`)
          .width('100%')
          .textAlign(TextAlign.Center)
          .fontSize(30)
          .margin({ bottom: 30 });
        Video({
          // 此处地址实际使用过程中替换为真实地址
          src: 'xx.xx.xx',
          controller: this.controller
        })
          .objectFit(ImageFit.Cover)
          .controls(true)
          .autoPlay(false)
          .loop(true)
          .width('80%')
          .height(200);
      };
    }
  }
  ```

  + **方案一：使用onWillShow和onWillHide实现监听。**

    onWillShow和onWillHide可对指定Tabs子组件可见性变化进行监听，onWillShow在TabContent即将完全显示前触发，打开视频。onWillHide在TabContent即将完全隐藏前触发，关闭视频。参考代码如下：

    ```ts
    import { VideoComponent } from './VideoComponent';

    @Entry
    @Component
    struct ShowHidePage {
      tabList: string[] = ['首页', '发现', '推荐'];
      controllerList: VideoController[] =
        [new VideoController(), new VideoController(), new VideoController(), new VideoController()];

      build() {
        Tabs({ barPosition: BarPosition.End }) {
          ForEach(this.tabList, (item: string, index: number) => {
            TabContent() {
              VideoComponent({ item: index, controller: this.controllerList[index] });
            }
            .tabBar(`${item}`)
            .onWillShow(() => {
              this.controllerList[index].start();
              console.info(`Succeeded in starting Video${index + 1}.`);
            })
            .onWillHide(() => {
              this.controllerList[index].pause();
              console.info(`Succeeded in pausing Video${index + 1}.`);
            });
          });
          TabContent() {
            VideoComponent({ item: 3, controller: this.controllerList[3] });
          }
          .tabBar('我的');
        }
        .width('100%')
        .height('100%');
      }
    }
    ```
  + **方案二：使用onVisibleAreaChange实现监听。**

    onVisibleAreaChange通过监听组件可见区域面积与自身面积的比值变化实现监听，可通过ratio取值范围设置监听触发的阈值。设置组件可见区域面积与自身面积的比值变大，并且在阈值范围内打开视频。组件可见区域面积与自身面积的比值变小，并且小于最低阈值时关闭视频。参考代码如下：

    ```ts
    import { VideoComponent } from './VideoComponent';

    @Entry
    @Component
    struct VisibleChangePage {
      tabList: string[] = ['首页', '发现', '推荐'];
      controllerList: VideoController[] =
        [new VideoController(), new VideoController(), new VideoController(), new VideoController()];

      build() {
        Tabs({ barPosition: BarPosition.End }) {
          ForEach(this.tabList, (item: string, index: number) => {
            TabContent() {
              Tabs() {
                VideoComponent({ item: index, controller: this.controllerList[index] });
              };
            }
            .tabBar(`${item}`)
            .onVisibleAreaChange([0.5, 1.0], (isExpanding: boolean, currentRatio: number) => {
              if (isExpanding && currentRatio >= 0.5 && currentRatio <= 1) {
                this.controllerList[index].start();
                console.info(`Succeeded in starting Video${index + 1}.`);
              }
              if (!isExpanding && currentRatio <= 0.5) {
                this.controllerList[index]?.pause();
                console.info(`Succeeded in pausing Video${index + 1}.`);
              }
            });
          });
          TabContent() {
            VideoComponent({ item: 3, controller: this.controllerList[3] });
          }
          .tabBar('我的');
        }
        .width('100%')
        .height('100%');
      }
    }
    ```
  + **方案三：使用uiObserver.on('tabContentUpdate')实现监听。**

    在uiObserver.on('tabContentUpdate')监听过程中，TabContent的组件的状态state能够反映该组件的显示与隐藏状态。参考代码如下：

    ```ts
    import { VideoComponent } from './VideoComponent';
    import { uiObserver } from '@kit.ArkUI';

    @Entry
    @Component
    struct TabContentUpdatePage {
      tabList: string[] = ['首页', '发现', '推荐', '我的'];
      controllerList: VideoController[] =
        [new VideoController(), new VideoController(), new VideoController(), new VideoController()];

      aboutToAppear(): void {
        uiObserver.on('tabContentUpdate', { id: 'tabsId' }, (info: uiObserver.TabContentInfo) => {
          if (info.state === 0 && info.index === 0) {
            this.controllerList[info.index].start();
            console.info(`Succeeded in starting Video1.`);
          } else if (info.state === 1 && info.index === 0) {
            this.controllerList[info.index].pause();
            console.info(`Succeeded in pausing Video1.`);
          }
        });
      }

      aboutToDisappear(): void {
        uiObserver.off('tabContentUpdate');
      }

      build() {
        Tabs({ barPosition: BarPosition.End }) {
          ForEach(this.tabList, (item: string, index: number) => {
            TabContent() {
              VideoComponent({ item: index, controller: this.controllerList[index] });
            }
            .id(`tabsId${index}`)
            .tabBar(`${item}`);
          });
        }
        .id('tabsId')
        .width('100%')
        .height('100%');
      }
    }
    ```

## 常见FAQ

Q：observer.on('tabContentUpdate')首次进入页面，为什么无法监听到ON\_SHOW？

A：uiObserver.on('tabContentUpdate')：监听TabContent页面的切换事件。只有在页面点击切换或者滑动切换的时候才能监听到，TabContent首次显示的时候，是不会监听到的。从API version 22开始，[on('tabChange')](../harmonyos-references/arkts-apis-uicontext-uiobserver.md#ontabchange22-1)支持监听Tabs组件初始化时，显示首个页签的事件。

Q：当tab切换时，为什么onWillShow会比上一个页面的onWillHide先触发？

A：每个TabContent的生命周期相互独立，系统优先处理新页面显示逻辑（触发onWillShow）。若需在上一个页面的onWillHide之后触发当前页面的onWillShow，可通过添加延时操作实现，参考代码如下：

```ts
TabContent() {
  // TabContent内容
}
.onWillShow(() => {
  setTimeout(() => {
    console.info('Succeeded in getting information.');
  }, 300);
});
```
