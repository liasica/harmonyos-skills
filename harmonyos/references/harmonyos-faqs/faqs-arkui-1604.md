---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-1604
title: Swiper组件实现试卷打分功能
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > Swiper组件实现试卷打分功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:18+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:a20ef767d502cc8ffb906d8e3195b1f84c8c70779d0ccbb0d3285ff99adc120a
---

## 问题现象

如何实现试卷打分功能？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/23wYyAQjTWeGsdZ4jXsqGQ/zh-cn_image_0000002658972557.gif "点击放大")

## 背景知识

* [Swiper](../harmonyos-references/ts-container-swiper.md)是HarmonyOS中的滑块视图容器，提供子组件滑动轮播显示的能力。
* [LazyForEach](../harmonyos-guides/arkts-rendering-control-lazyforeach.md)从数据源中按需迭代数据，并在每次迭代时创建相应组件。当在滚动容器中使用了LazyForEach，框架会根据滚动容器可视区域按需创建组件，当组件滑出可视区域外时，框架会销毁并回收组件以降低内存占用。
* [TextInput](../harmonyos-references/ts-basic-components-textinput.md)是一种单行文本输入框组件，可用于数据的输入，当按下输入法回车键触发该组件的[onSubmit](../harmonyos-references/ts-basic-components-textinput.md#onsubmit)回调函数。

## 解决方案

1. 创建分数数组scores，用于保存每道题的分数。
2. 使用LazyForEach结合Swiper组件循环渲染每个数据源中的元素，前五个页面表示试卷的题目信息，最后一个页面用于计算试卷的总分。
3. 在试卷的题目页面，通过TextInput组件实现分数输入，并在输入完成后使用onSubmit回调函数将输入数据存储到scores数组中。
4. 在试卷的总分页面，自定义calculate函数，用于计算scores数组的数组和。

```screen
// Index.ets
class MyDataSource implements IDataSource {
  private list: number[] = [];

  constructor(list: number[]) {
    this.list = list;
  }

  totalCount(): number {
    return this.list.length;
  }

  getData(index: number): number {
    return this.list[index];
  }

  registerDataChangeListener(): void {
  }

  unregisterDataChangeListener() {
  }
}

@Entry
@Component
struct Page {
  private swiperController: SwiperController = new SwiperController();
  private data: MyDataSource = new MyDataSource([]);
  controller: TextInputController | undefined;
  @State scores: string[] = ['0', '0', '0', '0', '0'];
  @State sum: number = 0;
  @State currentIndex: number = 0;

  calculate(): void {
    let sum = 0;
    for (let i = 0; i < 5; i++) {
      sum += parseInt(this.scores[i].toString());
    }
    this.sum = sum;
  }

  aboutToAppear(): void {
    let list: number[] = [];
    for (let i = 0; i < 6; i++) {
      list.push(i);
    }
    this.data = new MyDataSource(list);
  }

  build() {
    Column({ space: 5 }) {
      Swiper(this.swiperController) {
        LazyForEach(this.data, (index: number) => {
          Column() {
            if (index === 5) {
              Text(`总得分：${this.sum} 分`)
                .textAlign(TextAlign.Center)
                .fontSize(30);
            } else {
              Row() {
                Text(`第${index + 1}题`)
                  .backgroundColor(0xAFEEEE)
                  .textAlign(TextAlign.Center)
                  .fontSize(30);
              };

              Row() {
                Text(`本题得分：${this.scores[index]}分`)
                  .backgroundColor(0xAFEEEE)
                  .textAlign(TextAlign.Center)
                  .fontSize(30);
              };
            }
          }
          .backgroundColor(0xAFEEEE)
          .width('100%')
          .height('100%')
          .justifyContent(FlexAlign.Center);
        }, (item: string) => item);
      }
      .displayCount(1, true)
      .interval(4000)
      .duration(1000)
      .itemSpace(10)
      .indicator(false)
      .width('100%')
      .height('80%')
      .loop(false)
      .onAnimationEnd((index: number) => {
        this.calculate();
        this.currentIndex = index;
      });

      if (this.currentIndex !== 5) {
        Row({ space: 20 }) {
          Button('上一题')
            .onClick(() => {
              this.swiperController.showPrevious();
            });
          Button('下一题')
            .onClick(() => {
              this.swiperController.showNext();
            });
        };

        Row() {
          Text('本题满分20分，请输入得分：');
        };

        Row() {
          TextInput({ text: this.scores[this.currentIndex], placeholder: '请输入0-20之间的数字' })
            .inputFilter('[\-0-9]', (val) => {
              console.error('TextInputExample ： ' + val);
              return 0;
            })
            .onChange((text) => {
              let num: number = Number(text);
              if (num < 0) {
                this.scores[this.currentIndex] = '0';
              } else if (num > 20) {
                this.scores[this.currentIndex] = '20';
              } else {
                this.scores[this.currentIndex] = num.toString();
              }
            })
            .maxLength(2)
            .padding({ left: 16 })
            .placeholderFont({ size: 14 })
            .fontSize(14)
            .onSubmit((EnterKeyType, Event) => {
              this.scores[this.currentIndex] = Event.text;
            })
            .width('80%');
        };
      }
    }.width('100%')
    .margin({ top: 5 });
  }
}
```
