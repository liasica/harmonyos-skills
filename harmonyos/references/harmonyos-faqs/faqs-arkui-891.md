---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-891
title: 自定义Tabs样式，TabBar底部指示器如何对齐
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 自定义Tabs样式，TabBar底部指示器如何对齐
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:17+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a23acdf725c358b3e0b3f7b02a14e54297c0de96dd696d554aa3631f8d98a2b8
---

## 问题现象

自定义TabBar，如何实现底部指示器（图中文字“页签2”下面的蓝色小横杠）的对齐？问题现象如下图：

## 背景知识

* [选项卡Tabs介绍](../harmonyos-guides/arkts-navigation-tabs.md)：用于了解Tab组件的构成（TabBar、TabContent）。
* [组件区域变化事件](../harmonyos-references/ts-universal-component-area-change-event.md)：可以通过该事件，计算TabBar的相对位置。oldValue返回目标元素变化之前的宽高以及目标元素相对父元素和页面左上角的坐标位置。newValue返回目标元素变化之后的宽高以及目标元素相对父元素和页面左上角的坐标位置。
* 滚动组件通用事件[onDidScroll](../harmonyos-references/ts-container-scrollable-common.md#ondidscroll12)：滚动组件滑动时触发，返回当前帧滑动的偏移量和当前滑动状态。

## 解决方案

| 名称 | 方案一 | 方案二 |
| --- | --- | --- |
| 实现逻辑 | 多个底部指示器，底部指示器与标签捆绑，通过标签切换来控制底部指示器的显示与隐藏。 | 一个底部指示器，根据实际交互跟随标签移动。 |
| 方案优点 | 实现简单。 | 交互体验好。 |
| 原理图示 |  |  |
| 效果图示 |  |  |

* **方案一**：设置Tabs本身的TabBar高度为0，使用List实现自定义页签，在List的每个子项中定义页签名和底部指示器，并实现自定义页签和Tabs切换的联动。

  ```ts
  @Entry
  @Component
  struct TabSolution1 {
    tabArray: Array<number> = [0, 1, 2, 3, 4];
    @State focusIndex: number = 0;
    index: number = 0;
    private controller: TabsController = new TabsController();
    indicatorWidth: number = 50;
    private scrollerForScroll: Scroller = new Scroller();

    // 单独的页签
    @Builder
    myTabBar(tabName: string, tabItem: number, tabIndex: number) {
      Row({ space: 20 }) {
        Column() {
          Text(tabName + tabItem)
            .fontSize(18)
            .fontColor(tabIndex === this.focusIndex ? '#0A59F7' : Color.Black)
            .id(tabIndex.toString());
          // 资源文件需自行替换，可以替换为三角图片
          Column()
            .width(20)
            .height(4)
            .backgroundColor('#0A59F7')
            .visibility(tabIndex === this.focusIndex ? Visibility.Visible : Visibility.Hidden);
        };
      }
      .justifyContent(FlexAlign.Center)
      .constraintSize({ minWidth: 35 })
      .width(100)
      .height(38)
      .onClick(() => {
        this.controller.changeIndex(tabIndex);
        this.focusIndex = tabIndex;
      })
    }

    @Builder
    sideComponent(textName: string) {
      Row({ space: 20 }) {
        // 可以根据需要自行替换
        Text(textName).fontSize(18);
      }
      .justifyContent(FlexAlign.Center)
      .constraintSize({ minWidth: 35 })
      .height(27)
      .backgroundColor('#FFFFFF');
    }

    build() {
      Column() {
        Stack({ alignContent: Alignment.TopStart }) {
          // List自定义页签
          Column() {
            Row({ space: 8 }) {
              List({ space: 20, initialIndex: 0, scroller: this.scrollerForScroll }) {
                ForEach(this.tabArray, (item: number, index: number) => {
                  ListItem() {
                    this.myTabBar('页签 ', item, index);
                  };
                }, (item: string) => item);
              }
              .listDirection(Axis.Horizontal)
              .height(30)
              .width('80%')
              .friction(0.6)
              .alignListItem(ListItemAlign.Start)
              .scrollBar(BarState.Off)
              .width('80%')
              .backgroundColor('#FFFFFF');

              this.sideComponent('更多');
            }
            .alignItems(VerticalAlign.Bottom)
            .width('100%')
            .backgroundColor('#FFFFFF');
          }
          .alignItems(HorizontalAlign.Start)
          .width('100%');
        }
        .height(40)
        .width('100%')
        .backgroundColor('#FFFFFF');

        Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
          ForEach(this.tabArray, (item: number) => {
            TabContent() {
              Text('这是TabContent ' + item + ' 的内容')
                .height(300)
                .width('100%')
                .textAlign(TextAlign.Center)
                .fontSize(30);
            }
            .backgroundColor('#F1F3F5');
          }, (item: string) => item);
        }
        .width('100%')
        .barHeight(0)
        .animationDuration(100)
        .onChange((index: number) => {
          this.focusIndex = index;
          this.scrollerForScroll.scrollToIndex(index - 1, true);
        });
      }
      .height('100%');
    }
  }
  ```
* **方案二**：底部指示器对齐一共有四种情况处理，初始位置、TabBar切换（不涉及页签滑动，即在当前显示区域内切换页签的场景）、TabBar切换（涉及滑动，即切换到在显示区域显示不全的页签）、仅滑动（不涉及页签切换）。
  + **初始位置**：因为保持了初始位置与页签0对齐且底部指示器与页签的宽度相同，只需要通过onAreaChange事件拿到新位置的X坐标，然后让底部指示器左侧外边距的大小等于该值即可。

    | 名称 | 图片说明 |
    | --- | --- |
    | 偏移量计算 |  |
    | 运行效果 |  |

    ```ts
    // 单独的页签
    @Builder
    myTabBar(tabName: string, tabItem: number, tabIndex: number) {
      Row({ space: 20 }) {
        Text(tabName + tabItem)
          .fontSize(18)
          .fontColor(tabIndex === this.focusIndex ? '#0A59F7' : Color.Black)
          .id(tabIndex.toString())
          .onAreaChange((oldValue: Area, newValue: Area) => {
            console.debug(`oldValue:${JSON.stringify(oldValue)}, newValue:${JSON.stringify(newValue)}`);
            // 初始位置：底部指示器
            if (this.focusIndex === tabIndex && (this.indicatorLeftMargin === 0 || this.indicatorWidth === 0)) {
              if (newValue.position.x !== undefined) {
                let positionX = Number.parseFloat(newValue.position.x.toString());
                let preMarginLeft = this.indicatorLeftMargin;
                this.indicatorLeftMargin = Number.isNaN(positionX) ? 0 : positionX;
                console.info(`【页签的onAreaChange】preMarginLeft:${preMarginLeft},nowMarginLeft: ${this.indicatorLeftMargin}`);
              }
              let width = Number.parseFloat(newValue.width.toString());
              this.tabWidth = Number.isNaN(width) ? 0 : width;
              this.indicatorWidth = this.tabWidth;
            }
          });
      }
      .justifyContent(FlexAlign.Center)
      .constraintSize({ minWidth: 35 })
      .width(100)
      .height(30)
      .onClick(() => {
        this.controller.changeIndex(tabIndex);
        this.focusIndex = tabIndex;
      })
      .backgroundColor('#FFFFFF');
    }
    ```
  + **TabBar切换（不涉及滑动）**：在Tabs的onAnimationStart和onAnimationEnd事件，通过getInspectorByKey(id:string)方法获取页签距离左侧的偏移量和页签的宽度，接着进行单位转换（px转vp），最后给到底部指示器。

    | 名称 | 图片说明 |
    | --- | --- |
    | 偏移量计算 |  |
    | 运行效果 |  |

    ```ts
    Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
      ForEach(this.tabArray, (item: number) => {
        TabContent() {
          Text('这是TabContent ' + item + ' 的内容')
            .height(300)
            .width('100%')
            .textAlign(TextAlign.Center)
            .fontSize(30);
        }
        .backgroundColor('#F1F3F5');
      }, (item: string) => item);
    }
    .onAreaChange((oldValue: Area, newValue: Area) => {
      console.debug(`oldValue:${JSON.stringify(oldValue)}, newValue:${JSON.stringify(newValue)}`);
      let width = Number.parseFloat(newValue.width.toString());
      this.tabsWidth = Number.isNaN(width) ? 0 : width;
    })
    .width('100%')
    .barHeight(0)
    .animationDuration(100)
    .onChange((index: number) => {
      this.focusIndex = index;
      this.scrollerForScroll.scrollToIndex(index - 1, true);
    })
    .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
      console.debug(`index:${index}, event:${JSON.stringify(event)}`);
      // 切换动画开始时触发该回调。下划线跟着页面一起滑动
      this.focusIndex = targetIndex;
      let targetIndexInfo = this.getTextInfo(targetIndex);
      this.startAnimateTo(this.animationDuration, targetIndexInfo.left, targetIndexInfo.width);
    })
    .onGestureSwipe((index: number, event: TabsAnimationEvent) => {
      // 在页面跟手滑动过程中，逐帧触发该回调。
      let currentIndicatorInfo = this.getCurrentIndicatorInfo(index, event);
      this.focusIndex = currentIndicatorInfo.index;
      this.indicatorLeftMargin = currentIndicatorInfo.left;
      this.tabWidth = currentIndicatorInfo.width;
      this.indicatorWidth = currentIndicatorInfo.width;
    });
    ```

    ```ts
    // 获取页签信息，返回距左侧偏移量和页签宽度
    private getTextInfo(index: number): Record<string, number> {
      try {
        const rect = this.getUIContext().getComponentUtils().getRectangleById(index.toString());
        return {
          'left': this.getUIContext().px2vp(rect.windowOffset.x),
          'width': this.getUIContext().px2vp(rect.size.width)
        };
      } catch (error) {
        return { 'left': 0, 'width': 0 };
      }
    }

    private getCurrentIndicatorInfo(index: number, event: TabsAnimationEvent): Record<string, number> {
      let nextIndex = index;
      if (index > 0 && event.currentOffset > 0) {
        nextIndex--;
      } else if (index < this.tabArray.length && event.currentOffset < 0) {
        nextIndex++;
      }
      let indexInfo = this.getTextInfo(index);
      let nextIndexInfo = this.getTextInfo(nextIndex);
      let swipeRatio = Math.abs(event.currentOffset / this.tabsWidth);
      let currentIndex = swipeRatio > 0.5 ? nextIndex : index; // 页面滑动超过一半，tabBar切换到下一页。
      let currentLeft = indexInfo.left + (nextIndexInfo.left - indexInfo.left) * swipeRatio;
      let currentWidth = indexInfo.width + (nextIndexInfo.width - indexInfo.width) * swipeRatio;
      return { 'index': currentIndex, 'left': currentLeft, 'width': currentWidth };
    }

    // 动画效果（使底部指示器与页签同步移动）
    private startAnimateTo(duration: number, leftMargin: number, width: number) {
      this.getUIContext().animateTo({
        duration: duration, // 动画时长
        curve: Curve.Linear, // 动画曲线
        iterations: 1, // 播放次数
        playMode: PlayMode.Normal, // 动画模式
        onFinish: () => {
          console.info('play end');
        }
      }, () => {
        this.indicatorLeftMargin = leftMargin;
        this.tabWidth = width;
        this.indicatorWidth = width;
      });
    }
    ```
  + **TabBar切换（涉及滑动）**：底部指示器根据方案二的第二步流程（即TabBar切换且不涉及滑动的场景）设置到对应页签下，然后通过onDidScroll事件跟随页签一起移动。伪代码：第一步是底部指示器左侧偏移量等于目标页签距离左侧的偏移量，第二步即由第一步得到的偏移量减去滑动偏移量。

    | 名称 | 图片说明 |
    | --- | --- |
    | 偏移量计算 |  |
    | 运行效果 |  |

    ```ts
    List({ space: 20, initialIndex: 0, scroller: this.scrollerForScroll }) {
      ForEach(this.tabArray, (item: number, index: number) => {
        ListItem() {
          this.myTabBar('页签 ', item, index);
        };
      }, (item: string) => item);
    }
    .listDirection(Axis.Horizontal)
    .height(30)
    .width('80%')
    .friction(0.6)
    .alignListItem(ListItemAlign.Start)
    .scrollBar(BarState.Off)
    .width('80%')
    .backgroundColor('#FFFFFF')
    .onDidScroll((xOffset: number) => {
      // 场景三，跟随页签一起移动
      this.indicatorLeftMargin -= xOffset;
    });
    ```
  + **仅滑动（不涉及切换）**：通过onDidScroll事件跟随TabBar一起移动。

    | 名称 | 图片说明 |
    | --- | --- |
    | 偏移量计算 |  |
    | 运行效果 |  |

    该情况实现的代码同上述 **TabBar切换（涉及滑动）** 实现代码一致。
  + 方案二完整示例参考如下：

    ```ts
    @Entry
    @Component
    struct TabSolution2 {
      tabArray: Array<number> = [0, 1, 2, 3, 4];
      @State focusIndex: number = 0;
      private controller: TabsController = new TabsController();
      animationDuration: number = 300;
      @State indicatorLeftMargin: number = 0;
      @State indicatorWidth: number = 0;
      private tabsWidth: number = 0;
      private tabWidth: number = 0;
      private scrollerForScroll: Scroller = new Scroller();

      // 单独的页签
      @Builder
      myTabBar(tabName: string, tabItem: number, tabIndex: number) {
        Row({ space: 20 }) {
          Text(tabName + tabItem)
            .fontSize(18)
            .fontColor(tabIndex === this.focusIndex ? '#0A59F7' : Color.Black)
            .id(tabIndex.toString())
            .onAreaChange((oldValue: Area, newValue: Area) => {
              console.debug(`oldValue:${JSON.stringify(oldValue)}, newValue:${JSON.stringify(newValue)}`);
              // 初始位置：底部指示器
              if (this.focusIndex === tabIndex && (this.indicatorLeftMargin === 0 || this.indicatorWidth === 0)) {
                if (newValue.position.x !== undefined) {
                  let positionX = Number.parseFloat(newValue.position.x.toString());
                  let preMarginLeft = this.indicatorLeftMargin;
                  this.indicatorLeftMargin = Number.isNaN(positionX) ? 0 : positionX;
                  console.info(`【页签的onAreaChange】preMarginLeft:${preMarginLeft},nowMarginLeft: ${this.indicatorLeftMargin}`);
                }
                let width = Number.parseFloat(newValue.width.toString());
                this.tabWidth = Number.isNaN(width) ? 0 : width;
                this.indicatorWidth = this.tabWidth;
              }
            });
        }
        .justifyContent(FlexAlign.Center)
        .constraintSize({ minWidth: 35 })
        .width(100)
        .height(30)
        .onClick(() => {
          this.controller.changeIndex(tabIndex);
          this.focusIndex = tabIndex;
        })
        .backgroundColor('#FFFFFF');
      }

      @Builder
      sideComponent(textName: string) {
        Row({ space: 20 }) {
          Text(textName).fontSize(18);
        }
        .justifyContent(FlexAlign.Center)
        .constraintSize({ minWidth: 35 })
        .height(30)
        .backgroundColor('#FFFFFF');
      }

      build() {
        Column() {
          Stack({ alignContent: Alignment.TopStart }) {
            // List自定义页签
            Column() {
              Row({ space: 8 }) {
                List({ space: 20, initialIndex: 0, scroller: this.scrollerForScroll }) {
                  ForEach(this.tabArray, (item: number, index: number) => {
                    ListItem() {
                      this.myTabBar('页签 ', item, index);
                    };
                  }, (item: string) => item);
                }
                .listDirection(Axis.Horizontal)
                .height(30)
                .width('80%')
                .friction(0.6)
                .alignListItem(ListItemAlign.Start)
                .scrollBar(BarState.Off)
                .width('80%')
                .backgroundColor('#FFFFFF')
                .onDidScroll((xOffset: number) => {
                  // 场景三，跟随页签一起移动
                  this.indicatorLeftMargin -= xOffset;
                });

                this.sideComponent('更多');
              }
              .alignItems(VerticalAlign.Bottom)
              .width('100%')
              .backgroundColor('#FFFFFF');
            }
            .alignItems(HorizontalAlign.Start)
            .width('100%');

            // 资源文件需自行替换，可以替换为三角图片
            Column()
              .width(50)
              .height(4)
              .backgroundColor('#0A59F7')
              .margin({ left: this.indicatorLeftMargin, top: 30 });
          }
          .height(40)
          .width('100%')
          .backgroundColor('#FFFFFF');

          Tabs({ barPosition: BarPosition.Start, controller: this.controller }) {
            ForEach(this.tabArray, (item: number) => {
              TabContent() {
                Text('这是TabContent ' + item + ' 的内容')
                  .height(300)
                  .width('100%')
                  .textAlign(TextAlign.Center)
                  .fontSize(30);
              }
              .backgroundColor('#F1F3F5');
            }, (item: string) => item);
          }
          .onAreaChange((oldValue: Area, newValue: Area) => {
            console.debug(`oldValue:${JSON.stringify(oldValue)}, newValue:${JSON.stringify(newValue)}`);
            let width = Number.parseFloat(newValue.width.toString());
            this.tabsWidth = Number.isNaN(width) ? 0 : width;
          })
          .width('100%')
          .barHeight(0)
          .animationDuration(100)
          .onChange((index: number) => {
            this.focusIndex = index;
            this.scrollerForScroll.scrollToIndex(index - 1, true);
          })
          .onAnimationStart((index: number, targetIndex: number, event: TabsAnimationEvent) => {
            console.debug(`index:${index}, event:${JSON.stringify(event)}`);
            // 切换动画开始时触发该回调。下划线跟着页面一起滑动
            this.focusIndex = targetIndex;
            let targetIndexInfo = this.getTextInfo(targetIndex);
            this.startAnimateTo(this.animationDuration, targetIndexInfo.left, targetIndexInfo.width);
          })
          .onGestureSwipe((index: number, event: TabsAnimationEvent) => {
            // 在页面跟手滑动过程中，逐帧触发该回调。
            let currentIndicatorInfo = this.getCurrentIndicatorInfo(index, event);
            this.focusIndex = currentIndicatorInfo.index;
            this.indicatorLeftMargin = currentIndicatorInfo.left;
            this.tabWidth = currentIndicatorInfo.width;
            this.indicatorWidth = currentIndicatorInfo.width;
          });
        }
        .height('100%');
      }

      // 获取页签信息，返回距左侧偏移量和页签宽度
      private getTextInfo(index: number): Record<string, number> {
        try {
          const rect = this.getUIContext().getComponentUtils().getRectangleById(index.toString());
          return {
            'left': this.getUIContext().px2vp(rect.windowOffset.x),
            'width': this.getUIContext().px2vp(rect.size.width)
          };
        } catch (error) {
          return { 'left': 0, 'width': 0 };
        }
      }

      private getCurrentIndicatorInfo(index: number, event: TabsAnimationEvent): Record<string, number> {
        let nextIndex = index;
        if (index > 0 && event.currentOffset > 0) {
          nextIndex--;
        } else if (index < this.tabArray.length && event.currentOffset < 0) {
          nextIndex++;
        }
        let indexInfo = this.getTextInfo(index);
        let nextIndexInfo = this.getTextInfo(nextIndex);
        let swipeRatio = Math.abs(event.currentOffset / this.tabsWidth);
        let currentIndex = swipeRatio > 0.5 ? nextIndex : index; // 页面滑动超过一半，tabBar切换到下一页。
        let currentLeft = indexInfo.left + (nextIndexInfo.left - indexInfo.left) * swipeRatio;
        let currentWidth = indexInfo.width + (nextIndexInfo.width - indexInfo.width) * swipeRatio;
        return { 'index': currentIndex, 'left': currentLeft, 'width': currentWidth };
      }

      // 动画效果（使底部指示器与页签同步移动）
      private startAnimateTo(duration: number, leftMargin: number, width: number) {
        this.getUIContext().animateTo({
          duration: duration, // 动画时长
          curve: Curve.Linear, // 动画曲线
          iterations: 1, // 播放次数
          playMode: PlayMode.Normal, // 动画模式
          onFinish: () => {
            console.info('play end');
          }
        }, () => {
          this.indicatorLeftMargin = leftMargin;
          this.tabWidth = width;
          this.indicatorWidth = width;
        });
      }
    }
    ```
