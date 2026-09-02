---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1195
title: 实现List下拉刷新和上拉加载更多
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 实现List下拉刷新和上拉加载更多
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:27+08:00
doc_updated_at: 2026-08-26
content_hash: sha256:dd721b0534a9a0feb4cd180c73826123e21cd2cdf4a4771ea066092b662fbbbd
---

## 问题现象

在List组件中，如何实现下拉刷新和上拉加载的功能？

## 背景知识

* [PullToRefresh](https://ohpm.openharmony.cn/#/cn/detail/@ohos%2Fpulltorefresh)是一款OpenHarmony环境下可用的下拉刷新、上拉加载组件。支持设置内置动画的各种属性，支持设置自定义动画，支持lazyForEach的数据作为数据源。

  PullToRefresh使用限制：

  1、目前只支持List、Scroll、Tabs、Grid和WaterFlow系统容器组件；

  2、暂不支持设置系统容器组件的弹簧效果和阴影效果，使用时需要将系统组件edgeEffect属性的值设置为(EdgeEffect.None)；

  3、暂不支持页面触底时自动触发上拉加载功能；

  4、暂不支持在页面数据不满一屏时触发上拉加载功能；

  5、暂不支持通过代码的方式去触发下拉刷新功能；

  6、暂不支持在下拉刷新动画结束时提供手势结束的回调。
* [Refresh：](../harmonyos-references/ts-container-refresh.md)可以进行页面下拉操作并显示刷新动效的容器组件。
* [List组件：](../harmonyos-references/ts-container-list.md)列表包含一系列相同宽度的列表项。
* [Button组件：](../harmonyos-guides/arkts-common-components-button.md)按钮组件通常用于响应用户的点击操作，其类型包括胶囊按钮、圆形按钮、普通按钮、圆角矩形按钮。Button作为容器使用时可以通过添加子组件实现包含文字、图片等元素的按钮。
* [$$运算符：](../harmonyos-guides/arkts-two-way-sync.md)$$运算符为系统组件提供TS变量的引用，使得TS变量和系统组件的内部状态保持同步。

## 解决方案

* 场景一：通过List的滚动实现下拉刷新、上拉加载的效果。

  在目录entry/src/oh-package.json5文件中配置PullToRefresh依赖，本示例PullToRefresh三方库版本为2.1.2：

  ```json
  {
    "name": "entry",
    "version": "1.0.0",
    "description": "Please describe the basic information.",
    "main": "",
    "author": "",
    "license": "",
    "dependencies": {
      "@ohos/pulltorefresh": "^2.1.2"
    }
  }
  ```

  完整示例代码如下：

  ```ts
  import { PullToRefresh } from '@ohos/pulltorefresh';

  @Entry
  @Component
  struct ListStickyHeaderOne {
    scroller: Scroller = new Scroller();
    private tabscroller: Scroller = new Scroller();
    @State itemData: Array<number> = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
    tabTitles: Array<string> = ['Tab1', 'Tab2', 'Tab3'];

    @Builder
    private getListView() {
      List({ scroller: this.tabscroller }) {
        ForEach(this.itemData, (item: number) => {
          ListItem() {
            Text(`${item}`)
              .height(100)
              .width('100%')
              .borderRadius(10)
              .textAlign(TextAlign.Center)
              .backgroundColor('#f1f3f5')
              .margin({ bottom: 16 });
          };
        });
      }
      .nestedScroll({
        scrollForward: NestedScrollMode.PARENT_FIRST,
        scrollBackward: NestedScrollMode.SELF_FIRST
      })
      .backgroundColor('#ffffffff')
      // .divider({ strokeWidth: 1, color: 0x222222 })
      .edgeEffect(EdgeEffect.None); // 必须设置列表为滑动到边缘无效果
    }

    @Builder
    tabContentData(tabTitle: string) {
      TabContent() {
        Column() {
          PullToRefresh({
            data: this.itemData,
            scroller: this.tabscroller,
            customList: () => {
              this.getListView();
            },
            // 可选项，下拉刷新回调
            onRefresh: () => {
              return new Promise<string>((resolve) => {
                // 模拟网络请求操作，请求网络2秒后得到数据，通知组件，变更列表数据
                setTimeout(() => {
                  resolve('刷新成功');
                  let num = this.itemData.length;
                  this.itemData.push(num);
                }, 500);
              });
            },
            // 可选项，上拉加载更多回调
            onLoadMore: () => {
              return new Promise<string>((resolve) => {
                setTimeout(() => {
                  resolve('');
                  let num = this.itemData.length;
                  this.itemData.push(num);
                }, 2000);
              });
            },
            customLoad: null,
            customRefresh: null,
          });
        };
      }
      .tabBar(tabTitle)
      .padding({ top: 5, bottom: 5 });
    }

    build() {
      Column({ space: 10 }) {
        Scroll(this.scroller) {
          Column() {
            Tabs() {
              ForEach(this.tabTitles, (title: string) => {
                this.tabContentData(title);
              });
            };
          }.width('92%').alignItems(HorizontalAlign.Center);
        }.width('100%').align(Alignment.Center).scrollBar(BarState.Off);
      }.backgroundColor('#ffffffff')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM, SafeAreaEdge.TOP]);
    }
  }
  ```
* 场景二：通过点击按钮实现List列表下拉刷新。

  可以使用[$$](../harmonyos-guides/arkts-two-way-sync.md)双向绑定Refresh组件参数refreshing，点击按钮手动控制组件刷新状态实现，示例代码如下：

  ```ts
  @Entry
  @Component
  struct RefreshExample {
    @State isRefreshing: boolean = false;
    @State arr: String[] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];

    build() {
      Column() {
        Row() {
          Button('开始刷新')
            .margin(16)
            .onClick(() => {
              // 手动开始刷新
              this.isRefreshing = true;
            });
          Button('结束刷新')
            .margin(16)
            .onClick(() => {
              // 手动停止刷新
              this.isRefreshing = false;
            });
        };

        Refresh({ refreshing: $$this.isRefreshing }) {
          List() {
            ForEach(this.arr, (item: string) => {
              ListItem() {
                Text('' + item)
                  .width('92%')
                  .height(100)
                  .textAlign(TextAlign.Center)
                  .fontSize(16)
                  .margin({ bottom:16 ,left:16,right:16})
                  .borderRadius(10)
                  .backgroundColor('#f1f3f5');
              };
            }, (item: string) => item);
          };
        }
        .onRefreshing(() => {
          // 2秒后自动结束刷新
          setTimeout(() => {
            this.isRefreshing = false;
          }, 2000);
        })
        .backgroundColor('#ffffffff');
      }.backgroundColor('#ffffffff').expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.BOTTOM, SafeAreaEdge.TOP]);
    }
  }
  ```
* 场景三：在List嵌套List场景下实现外层List的下拉刷新，内层List的上拉加载更多。

  可以在外层List使用Refresh组件实现上拉刷新，内层List使用PullToRefresh进行下拉加载，PullToRefresh依赖配置同场景一，代码示例如下：

  ```ts
  import { PullToRefresh, PullToRefreshConfigurator } from '@ohos/pulltorefresh';

  const tabsList = ['能源', '化工', '塑料', '化纤', '聚氨酯'];

  @Component
  struct Index {
    private refreshScroller: Scroller = new Scroller();
    private refreshConfigurator: PullToRefreshConfigurator = new PullToRefreshConfigurator();
    @State list: Array<string> =
      ['a', 'b', 'c', 'd', 'e', 'f', 'a1', 'b1', 'c1', 'd1', 'e1', 'f1'];

    aboutToAppear(): void {
      this.refreshConfigurator.setHasRefresh(false);
    }

    @Builder
    getListView() {
      List({ space: 10, scroller: this.refreshScroller }) {
        ForEach(this.list,
          (item: string) => {
            ListItem() {
              Text(item)
                .height(100)
                .width('92%')
                .borderRadius(10)
                .textAlign(TextAlign.Center)
                .margin({ right: 16, left: 16, bottom: 16 })
                .backgroundColor('#F1F3F5');
            };
          });
      }
      .height('100%')
      .width('100%')
      .scrollBar(BarState.Off)
      .edgeEffect(EdgeEffect.None)
      .nestedScroll({
        scrollForward: NestedScrollMode.PARENT_FIRST,
        scrollBackward: NestedScrollMode.SELF_FIRST
      });
    }

    build() {
      Column({ space: 10 }) {
        PullToRefresh({
          // 必传项，列表组件所绑定的数据
          data: $list,
          refreshConfigurator: this.refreshConfigurator,
          // 必传项，需绑定传入主体布局内的列表或宫格组件
          scroller: this.refreshScroller,
          // 必传项，自定义主体布局，内部有列表或宫格组件
          customList: () => {
            // 一个用@Builder修饰过的UI方法
            this.getListView();
          },
          // 可选项，上拉加载更多回调
          onLoadMore: () => {
            return new Promise<string>((resolve) => {
              // 模拟网络请求操作，请求网络2秒后得到数据，通知组件，变更列表数据
              setTimeout(() => {
                resolve('加载更多');
                this.list.push('a2');
                this.list.push('b2');
              }, 2000);
            });
          },
          customLoad: null,
          customRefresh: null,
        }).width('100%').height('100%');
      }.width('100%');
    }
  }

  @Entry
  @Component
  struct KeyboadPage {
    private refreshScroller: Scroller = new Scroller();
    @State isRefresh: boolean = false;

    build() {
      Column({ space: 10 }) {
        Refresh({ refreshing: $$this.isRefresh, builder: this.buildRefreshCom() }) {
          this.getListView();
        }.onRefreshing(() => {
          setTimeout(() => {
            this.isRefresh = false;
          }, 1000);
        });
      }
      .width('100%')
      .height('100%');
    }

    @Builder
    buildRefreshCom() {
      Row() {
        LoadingProgress().height(32);
        Text('正在刷新...').fontSize(16).margin({
          left: 20,
        });
      }
      .alignItems(VerticalAlign.Center);
    }

    @Builder
    getListView() {
      List({ scroller: this.refreshScroller }) {
        ListItem() {
          Text('第一条')
            .textAlign(TextAlign.Center)
            .width('92%')
            .margin({ right: 16, left: 16, bottom: 16 })
            .height(100)
            .borderRadius(10)
            .backgroundColor('#F1F3F5');
        };

        ListItem() {
          Text('第二条')
            .textAlign(TextAlign.Center)
            .width('92%')
            .margin({ right: 16, left: 16, bottom: 16 })
            .height(100)
            .borderRadius(10)
            .backgroundColor('#F1F3F5');
        };

        ListItem() {
          Text('第三条')
            .textAlign(TextAlign.Center)
            .width('92%')
            .margin({ right: 16, left: 16, bottom: 16 })
            .height(100)
            .borderRadius(10)
            .backgroundColor('#F1F3F5');
        };

        ListItem() {
          Tabs({
            barPosition: BarPosition.Start,
          }) {
            ForEach(tabsList,
              (item: string, idx: number) => {
                TabContent() {
                  Index();
                }
                .tabBar(this.watchingTabBuilder(idx, item));
              });
          }
          .width('100%')
          .barHeight(50)
          .barMode(BarMode.Scrollable);
        };
      }
      .edgeEffect(EdgeEffect.None)
      .height('100%')
      .width('100%')
      .scrollBar(BarState.Off);
    }

    @Builder
    watchingTabBuilder(index: number, item: string) {
      Text(item)
        .fontSize(16)
        .fontColor('#121212')
        .padding({
          left: 15,
          right: 15,
          top: 12,
          bottom: 12
        })
        .borderRadius(5);
    }
  }
  ```
* 场景四：使用[Refresh](../harmonyos-references/ts-container-refresh.md)组件结合[list](../harmonyos-references/ts-container-list.md)的[onReachEnd](../harmonyos-references/ts-container-list.md#onreachend)事件实现下拉刷新和上拉加载。

  不依赖三方库，使用系统内置Refresh组件处理下拉刷新，List的onReachEnd事件处理上拉加载，通过isLoading和hasMore状态变量控制加载行为，示例代码如下：

  ```ts
  @Entry
  @Component
  struct RefreshLoadPage {
    @State items: number[] = Array.from({ length: 20 }, (_: ESObject, i: number) => i);
    @State isRefreshing: boolean = false;
    @State isLoading: boolean = false;
    @State hasMore: boolean = true;
    private page: number = 1;

    build() {
      Refresh({ refreshing: $$this.isRefreshing }) {
        List() {
          ForEach(this.items, (item: number) => {
            ListItem() {
              Text(`Item ${item}`)
                .height(56)
                .padding({ left: 16 });
            }
          })
          if (this.isLoading) {
            ListItem() {
              Row() {
                LoadingProgress().width(24).height(24);
                Text('加载中...').fontSize(14).margin({ left: 8 });
              }.justifyContent(FlexAlign.Center).width('100%').height(50);
            }
          }
        }
        .onReachEnd(() => {
          if (this.hasMore && !this.isLoading) {
            this.loadMore();
          }
        })
      }
      .onRefreshing(() => {
        this.page = 1;
        this.items = Array.from({ length: 20 }, (_: ESObject, i: number) => i);
        this.hasMore = true;
        this.isRefreshing = false;
      })
    }

    loadMore(): void {
      this.isLoading = true;
      setTimeout(() => {
        let newItems = Array.from({ length: 10 }, (_: ESObject, i: number) => this.items.length + i);
        this.items = this.items.concat(newItems);
        this.page++;
        this.isLoading = false;
        if (this.page >= 5) {
          this.hasMore = false;
        }
      }, 1000);
    }
  }
  ```

## 常见FAQ

Q：页面的数据已经全部加载完成时，如何结束上拉加载的状态？

A：将[PullToRefreshConfigurator类](https://gitee.com/openharmony-sig/ohos_pull_to_refresh#pulltorefreshconfigurator类接口)的setHasLoadMore属性为false，即关闭上拉加载功能。

Q：除了使用PullToRefresh三方组件，是否还有其他方式实现List下拉刷新？

A：容器组件[Refresh](../harmonyos-references/ts-container-refresh.md)组件能够进行页面下拉操作并显示刷新动效。
