---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-639
title: 如何实现九宫格抽奖
breadcrumb: FAQ > 应用框架开发 > UI框架 > UI界面 > 如何实现九宫格抽奖
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:21+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:796a5bc3ab026b52a98504f80088d5a789c21de2342f38fa11bc892d815786fa
---

## 问题现象

在一些活动中会需要提供一个抽奖功能，如何实现九宫格滚动抽奖的功能？

## 背景知识

* [Flex](../harmonyos-references/ts-container-flex.md)：Flex是以弹性方式布局子组件的容器组件，能够高效地排列、对齐子元素并分配剩余空间。其wrap属性的参数设置为[FlexWrap.Wrap](../harmonyos-references/ts-appendix-enums.md#flexwrap)时，可以实现子组件单行显示不下时自动换行的功能。
* [@ObservedV2装饰器和@Trace装饰器](../harmonyos-guides/arkts-new-observedv2-and-trace.md)：用于装饰类以及类中的属性，使得被装饰的类和属性具有深度观测的能力。

## 解决方案

1. 定义一个单元格奖品类，可采用@ObservedV2装饰器和@Trace装饰器装饰为状态变量，并将九个单元格奖品实例存入对象数组备用。

   ```ts
   // 定义一个可观察的Prize类，用于表示奖品信息。
   @ObservedV2
   class Prize {
     @Trace title: string;
     @Trace color: string;
     @Trace description: string;

     constructor(title: string, color: string, description: string = '') {
       this.title = title;
       this.color = color;
       this.description = description;
     }
   }
   ```
2. 使用Flex弹性布局，设置Flex组件宽度为三倍单元格宽度及单元格间距宽度之和，ForEach依次渲染步骤一中的单元格奖品实例的对象数组，同时设置Flex组件属性为FlexWrap.Wrap。当子组件横向排列超出Flex组件的单元格会自动排布到下一行，从而实现九宫格排列。

   ```ts
     // 遍历奖品数组，创建每个奖品的UI
     ForEach(this.prizeArray, (item: Prize, index: number) => {
       Column() {
         Text(`${item.title}`)
           .fontColor(index === 4 ? Color.White : item.color)
           .fontSize(16);
         Text(`${item.description}`)
           .fontColor(index === 4 ? Color.White : item.color)
           .fontSize(20);
       }
       .clickEffect({ level: ClickEffectLevel.LIGHT, scale: 0.8 })
       .onClick(() => {
         // 如果正在动画中，忽略点击
         if (this.isAnimating) {
           return;
         }
         // 如果点击的是抽奖按钮，开始抽奖
         if (index === 4) {
           this.isAnimating = true;
           this.startLottery();
         } else {
           for (let i = 0; i < this.selectionOrder.length; i++) {
             if (this.selectionOrder[i] === index) {
               this.selectedIndex = i; // 更新选中索引到对应位置
             }
           }
         }
       })
       .alignItems(HorizontalAlign.Center)
       .justifyContent(FlexAlign.Center)
       .width(`${this.cellWidth}lpx`)
       .height(`${this.cellWidth}lpx`)
       .margin(`${this.baseMargin}lpx`)
       .backgroundColor(index === 4 ? '#ff5444' :
         (this.selectionOrder[this.selectedIndex % this.selectionOrder.length] === index ? Color.Gray : Color.White))
       .borderRadius(10) // 设置圆角
       .shadow({
         // 设置阴影效果
         radius: 10,
         color: '#f98732',
         offsetX: 0,
         offsetY: 20
       });
     });
   }.width(`${this.cellWidth * 3 + this.baseMargin * 6}lpx`)
   .margin({ top: 30 });
   ```
3. 通过随机数得到最终奖品，设置抽奖的加减速逻辑，并在停止时设置提醒弹窗。

   ```ts
   // 开始抽奖逻辑
   startLottery(speed: number = 500) {
     setTimeout(() => {
       // 如果速度大于50，则递归调用startLottery以逐渐加速
       if (speed > 50) {
         speed -= 50;
         this.startLottery(speed);
       } else {
         this.runAtConstantSpeed(); // 达到最高速度后进入匀速阶段
         return;
       }
       this.selectedIndex++; // 每次调用时更新选中索引
     }, speed);
   }

   // 以恒定速度运行抽奖
   runAtConstantSpeed() {
     let randData = this.random.generateRandomSync(3);
     let speed = Math.floor(randData.data[0] / 255 * this.selectionOrder.length);
     clearInterval(this.intervalID); // 清除之前的定时器
     // 设置新的定时器来更新选中索引
     this.intervalID = setInterval(() => {
       // 如果选中索引达到速度值，停止并进入减速阶段
       if (this.selectedIndex >= speed) {
         clearInterval(this.intervalID);
         this.slowDown();
         return;
       }
       this.selectedIndex++;
     }, 50);
   }

   // 减速逻辑
   slowDown(speed = 50) {
     // 设置延时执行
     setTimeout(() => {
       // 如果速度小于500，则递归调用slowDown以逐渐减速
       if (speed < 500) {
         speed += 50;
         this.slowDown(speed);
       } else {
         this.selectedIndex %= this.selectionOrder.length; // 确保索引在有效范围内
         let index = this.selectionOrder[this.selectedIndex]; // 获取最终选中的奖品索引
         this.isAnimating = false; // 动画结束
         this.getUIContext().showAlertDialog({
           title: '结果',
           message: `${this.prizeArray[index].title}${this.prizeArray[index].description}`, // 显示奖品信息
           confirm: {
             defaultFocus: true,
             value: '我知道了',
             action: () => {
             }
           },
           alignment: DialogAlignment.Center,
         });
         return;
       }
       this.selectedIndex++;
     }, speed);
   }
   ```
4. 同时可以通过[@Provide/@Consume](../harmonyos-guides/arkts-provide-and-consume.md)设置子组件实时显示和编辑奖品的信息。

   ```ts
   // 定义MyPrizeUpdate结构组件，用于显示和编辑选中的奖品信息
   @Component
   struct MyPrizeUpdate {
     @Consume selectedIndex: number; // 当前选中的奖品索引
     @Consume private selectionOrder: number[]; // 保存抽奖顺序的数组
     @Consume private prizeArray: Prize[]; // 保存所有奖品的数组

     build() {
       Column({ space: 20 }) {
         Row() {
           Text('标题：');
           TextInput({ text: this.prizeArray[this.selectionOrder[this.selectedIndex % this.selectionOrder.length]].title })
             .width('300lpx')
             .onChange((value) => {
               this.prizeArray[this.selectionOrder[this.selectedIndex % this.selectionOrder.length]].title = value; // 更新奖品标题
             });
         };

         Row() {
           Text('描述：');
           TextInput({
             text: `${this.prizeArray[this.selectionOrder[this.selectedIndex % this.selectionOrder.length]].description}`
           }).width('300lpx').onChange((value) => {
             this.prizeArray[this.selectionOrder[this.selectedIndex % this.selectionOrder.length]].description = value;
           });
         };

         Row() {
           Text('颜色：');
           TextInput({
             text: `${this.prizeArray[this.selectionOrder[this.selectedIndex % this.selectionOrder.length]].color}`
           }).width('300lpx').onChange((value) => {
             this.prizeArray[this.selectionOrder[this.selectedIndex % this.selectionOrder.length]].color = value;
           });
         };
       }
       .justifyContent(FlexAlign.Start)
       .padding(40)
       .width('100%')
       .backgroundColor(Color.White);
     }
   }
   ```

完整示例参考如下：

```screen
import cryptoFramework from '@ohos.security.cryptoFramework';

// 定义一个可观察的Prize类，用于表示奖品信息。
@ObservedV2
class Prize {
  @Trace title: string;
  @Trace color: string;
  @Trace description: string;

  constructor(title: string, color: string, description: string = '') {
    this.title = title;
    this.color = color;
    this.description = description;
  }
}

// 定义MyPrizeUpdate结构组件，用于显示和编辑选中的奖品信息
@Component
struct MyPrizeUpdate {
  @Consume selectedIndex: number; // 当前选中的奖品索引
  @Consume private selectionOrder: number[]; // 保存抽奖顺序的数组
  @Consume private prizeArray: Prize[]; // 保存所有奖品的数组

  build() {
    Column({ space: 20 }) {
      Row() {
        Text('标题：');
        TextInput({ text: this.prizeArray[this.selectionOrder[this.selectedIndex % this.selectionOrder.length]].title })
          .width('300lpx')
          .onChange((value) => {
            this.prizeArray[this.selectionOrder[this.selectedIndex % this.selectionOrder.length]].title = value; // 更新奖品标题
          });
      };

      Row() {
        Text('描述：');
        TextInput({
          text: `${this.prizeArray[this.selectionOrder[this.selectedIndex % this.selectionOrder.length]].description}`
        }).width('300lpx').onChange((value) => {
          this.prizeArray[this.selectionOrder[this.selectedIndex % this.selectionOrder.length]].description = value;
        });
      };

      Row() {
        Text('颜色：');
        TextInput({
          text: `${this.prizeArray[this.selectionOrder[this.selectedIndex % this.selectionOrder.length]].color}`
        }).width('300lpx').onChange((value) => {
          this.prizeArray[this.selectionOrder[this.selectedIndex % this.selectionOrder.length]].color = value;
        });
      };
    }
    .justifyContent(FlexAlign.Start)
    .padding(40)
    .width('100%')
    .backgroundColor(Color.White);
  }
}

// 定义抽奖页面入口组件
@Entry
@Component
struct LotteryPage {
  @Provide private selectedIndex: number = 0; // 提供当前选中的索引，初始值为0
  private random: cryptoFramework.Random = cryptoFramework.createRandom();
  private isAnimating: boolean = false; // 标记是否正在进行动画，初始值为false
  @Provide private selectionOrder: number[] = [0, 1, 2, 5, 8, 7, 6, 3]; // 定义抽奖顺序
  private cellWidth: number = 200;
  private baseMargin: number = 10;
  @Provide private prizeArray: Prize[] = [
    new Prize('红包', '#ff9675', '10元'),
    new Prize('话费', '#ff9f2e', '5元'),
    new Prize('红包', '#8e7fff', '50元'),
    new Prize('红包', '#48d1ea', '30元'),
    new Prize('开始抽奖', '#fffdfd'),
    new Prize('谢谢参与', '#5f5f5f'),
    new Prize('谢谢参与', '#5f5f5f'),
    new Prize('超市红包', '#5f5f5f', '100元'),
    new Prize('鲜花', '#75b0fe'),
  ];
  private intervalID: number = 0; // 定时器ID，用于控制抽奖速度

  // 开始抽奖逻辑
  startLottery(speed: number = 500) {
    setTimeout(() => {
      // 如果速度大于50，则递归调用startLottery以逐渐加速
      if (speed > 50) {
        speed -= 50;
        this.startLottery(speed);
      } else {
        this.runAtConstantSpeed(); // 达到最高速度后进入匀速阶段
        return;
      }
      this.selectedIndex++; // 每次调用时更新选中索引
    }, speed);
  }

  // 以恒定速度运行抽奖
  runAtConstantSpeed() {
    let randData = this.random.generateRandomSync(3);
    let speed = Math.floor(randData.data[0] / 255 * this.selectionOrder.length);
    clearInterval(this.intervalID); // 清除之前的定时器
    // 设置新的定时器来更新选中索引
    this.intervalID = setInterval(() => {
      // 如果选中索引达到速度值，停止并进入减速阶段
      if (this.selectedIndex >= speed) {
        clearInterval(this.intervalID);
        this.slowDown();
        return;
      }
      this.selectedIndex++;
    }, 50);
  }

  // 减速逻辑
  slowDown(speed = 50) {
    // 设置延时执行
    setTimeout(() => {
      // 如果速度小于500，则递归调用slowDown以逐渐减速
      if (speed < 500) {
        speed += 50;
        this.slowDown(speed);
      } else {
        this.selectedIndex %= this.selectionOrder.length; // 确保索引在有效范围内
        let index = this.selectionOrder[this.selectedIndex]; // 获取最终选中的奖品索引
        this.isAnimating = false; // 动画结束
        this.getUIContext().showAlertDialog({
          title: '结果',
          message: `${this.prizeArray[index].title}${this.prizeArray[index].description}`, // 显示奖品信息
          confirm: {
            defaultFocus: true,
            value: '我知道了',
            action: () => {
            }
          },
          alignment: DialogAlignment.Center,
        });
        return;
      }
      this.selectedIndex++;
    }, speed);
  }

  // 构建UI方法
  build() {
    Column() {
      Flex({ wrap: FlexWrap.Wrap }) {
        // 遍历奖品数组，创建每个奖品的UI
        ForEach(this.prizeArray, (item: Prize, index: number) => {
          Column() {
            Text(`${item.title}`)
              .fontColor(index === 4 ? Color.White : item.color)
              .fontSize(16);
            Text(`${item.description}`)
              .fontColor(index === 4 ? Color.White : item.color)
              .fontSize(20);
          }
          .clickEffect({ level: ClickEffectLevel.LIGHT, scale: 0.8 })
          .onClick(() => {
            // 如果正在动画中，忽略点击
            if (this.isAnimating) {
              return;
            }
            // 如果点击的是抽奖按钮，开始抽奖
            if (index === 4) {
              this.isAnimating = true;
              this.startLottery();
            } else {
              for (let i = 0; i < this.selectionOrder.length; i++) {
                if (this.selectionOrder[i] === index) {
                  this.selectedIndex = i; // 更新选中索引到对应位置
                }
              }
            }
          })
          .alignItems(HorizontalAlign.Center)
          .justifyContent(FlexAlign.Center)
          .width(`${this.cellWidth}lpx`)
          .height(`${this.cellWidth}lpx`)
          .margin(`${this.baseMargin}lpx`)
          .backgroundColor(index === 4 ? '#ff5444' :
            (this.selectionOrder[this.selectedIndex % this.selectionOrder.length] === index ? Color.Gray : Color.White))
          .borderRadius(10) // 设置圆角
          .shadow({
            // 设置阴影效果
            radius: 10,
            color: '#f98732',
            offsetX: 0,
            offsetY: 20
          });
        });
      }.width(`${this.cellWidth * 3 + this.baseMargin * 6}lpx`)
      .margin({ top: 30 });
      MyPrizeUpdate().margin({ top: 20 });
    }
    .height('100%')
    .width('100%')
    .backgroundColor('#ffb350');
  }
}
```

## 总结

本方案主要是实现九宫格的布局以及随机抽奖的逻辑及动画，其中随机抽奖的逻辑及动画不同的活动有不同的需求，需要自己实现特定逻辑。而九宫格布局除了以Flex组件自动换行实现之外，还可以采用[Grid组件](../harmonyos-references/ts-container-grid.md)实现九宫格布局。
