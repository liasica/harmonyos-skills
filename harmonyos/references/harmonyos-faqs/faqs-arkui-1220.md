---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1220
title: 如何实现Tabs组件隐藏部分Tab页面
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现Tabs组件隐藏部分Tab页面
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:20+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fdf81d13d9552f72336965cbb2087b8c8c5cca25e901da9247ed680867658fc6
---

## 问题现象

Tabs组件怎样实现隐藏部分Tab页面的效果。

## 背景知识

* [Tabs组件](../harmonyos-references/ts-container-tabs.md)是通过TabContent页签进行内容视图切换的容器组件，每个页签对应一个内容视图。
* Tabs组件不支持自定义组件作为子组件，仅可包含子组件[TabContent](../harmonyos-references/ts-container-tabcontent.md)以及渲染控制类型if/else和ForEach。

## 解决方案

* **方案一**：通过if/else控制Tabs页面渲染。

  实现重点如下：
  1. 在渲染过程中需注意渲染的页面位置判定参数的连续性，即下文中tabBuilder(index: number, name: string)组件的index参数需是本页面的位置参数。
  2. 跳转到本位置时，采用this.currentIndex===index语句控制当前页面tabBar页高亮显示。
  3. 由于页面隐藏后，this.currentIndex的获取方式会保证其总是连续的，所以index参数也必须重设为连续的，否则tabBar会显示异常。

  完整示例代码如下：

  ```ts
  @Entry
  @Component
  struct Index {
    @State
    private currentIndex: number = 0;
    private controller: TabsController = new TabsController();
    @State change: boolean = true;

    // tabBar组件
    @Builder
    tabBuilder(index: number, name: string) {
      RelativeContainer() {
        Text(name)
          .fontColor(this.currentIndex === index ? '#0a59f7' : '#182431')
          .fontSize(16)
          .fontWeight(this.currentIndex === index ? 500 : 400)
          .height('auto')
          .padding({
            left: 8,
            right: 8,
            top: 6,
            bottom: 6
          })
          .id('textTitle')
          .alignRules({
            middle: { anchor: '__container__', align: HorizontalAlign.Center },
            center: { anchor: '__container__', align: VerticalAlign.Center }
          });
        Divider()
          .strokeWidth(2)
          .color('#0a59f7')
          .opacity(this.currentIndex === index ? 1 : 0)
          .width(100)
          .alignRules({ bottom: { anchor: '__container__', align: VerticalAlign.Bottom } });
      }
      .width(100);
    }

    build() {
      RelativeContainer() {
        Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
          TabContent() {
            Text('页面一');
          }.tabBar(this.tabBuilder(0, '页面一'));

          TabContent() {
            Text('页面二，点击显隐页面三')
              .onClick(() => {
                this.change = !this.change;
              });
          }
          .tabBar(this.tabBuilder(1, '页面二'));

          if (this.change) {
            TabContent() {
              Text('页面三');
            }
            .tabBar(this.tabBuilder(2, '页面三'));

            TabContent() {
              Text('页面四');
            }
            .tabBar(this.tabBuilder(3, '页面四'));

            TabContent() {
              Text('页面五');
            }
            .tabBar(this.tabBuilder(4, '页面五'));
          } else {
            // 当隐藏页面后需要保证TabContent页面的第一个参数Index连续
            TabContent() {
              Text('页面四');
            }
            .tabBar(this.tabBuilder(2, '页面四'));

            TabContent() {
              Text('页面五');
            }
            .tabBar(this.tabBuilder(3, '页面五'));
          }
        }
        .barMode(BarMode.Scrollable)
        .onChange((index) => {
          this.currentIndex = index;
        })
        .animationDuration(400)
        .scrollable(true)
        .vertical(false)
        .width('100%')
        .fadingEdge(false);
      };
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/B0H9tl4hQTuOwVqEQXZeMg/zh-cn_image_0000002628594022.gif "点击放大")
* **方案二**：使用ForEach操作数组进行页面部分隐藏。

  实现重点如下：
  1. 将Tabs栏的数据封装在数组中，使用ForEach遍历展示；
  2. 操作数组来对Tab页面进行部分隐藏。

  完整示例代码如下：

  ```ts
  interface Info {
    id: number;
    name: string;
  }

  @Entry
  @Component
  struct PageTwo {
    private controller: TabsController = new TabsController();
    @State currentIndex: number = 0;
    @State colorArray: Info[] = [
      { id: 0, name: '首页' },
      { id: 1, name: '新品' },
      { id: 2, name: '社区' },
      { id: 3, name: '购物车' },
      { id: 4, name: '我的' },
    ];

    @Builder
    tabBuilder(index: number, name: string) {
      RelativeContainer() {
        Text(name)
          .fontColor(this.currentIndex === index ? '#0a59f7' : '#182431')
          .fontSize(16)
          .fontWeight(this.currentIndex === index ? 500 : 400)
          .height('auto')
          .padding({
            left: 8,
            right: 8,
            top: 6,
            bottom: 6
          })
          .id('textTitle')
          .alignRules({
            middle: { anchor: '__container__', align: HorizontalAlign.Center },
            center: { anchor: '__container__', align: VerticalAlign.Center }
          });
        Divider()
          .strokeWidth(2)
          .color('#0a59f7')
          .opacity(this.currentIndex === index ? 1 : 0)
          .width(100)
          .alignRules({ bottom: { anchor: '__container__', align: VerticalAlign.Bottom } });
      }
      .width(100);
    }

    build() {
      Tabs({ barPosition: BarPosition.Start, index: this.currentIndex, controller: this.controller }) {
        ForEach(this.colorArray, (item: Info, index: number) => {
          TabContent() {
            if (index === 2) {
              Text('点击显隐最后一个页面')
                .onClick(() => {
                  if (this.colorArray.length === 5) {
                    this.colorArray.splice(this.colorArray.length - 1, 1);
                  } else {
                    this.colorArray.push({ id: 4, name: '我的' });
                  }
                });
            } else {
              Text(`页面${index}`);
            }
          }.tabBar(this.tabBuilder(index, item.name));
        });
      }
      .onChange((index) => {
        this.currentIndex = index;
      });
    }
  }
  ```

  实现效果如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/BjEo23dsRXmdbpINL8gpXQ/zh-cn_image_0000002628753918.png "点击放大")

## 常见FAQ

Q：利用visibility属性设置页面隐藏时手势滑动会出现空白页面？

A：因为visibility属性只是将页面隐藏，实际仍会创建该页面，该页面会占据一个索引位置，手势左右滑动是按照索引顺序展示，滑动到对应的索引位置时，由于该页面是隐藏状态，所以依旧会出现空白页面。

Q：为什么有时利用if/else隐藏页面后tabBar显示异常？

A：一般判断tabBar高亮显示的原理是不同页面传入不同的连续数字信息对应其在页面栈内的位置，但是判断隐藏后，导致数字不连续了，以上述方案为例，如果仅仅隐藏页面三，不修改页面四、页面五的位置参数，则会导致页面异常。
