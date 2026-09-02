---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkui-795
title: 如何用Progress组件显示任务列表进度
breadcrumb: FAQ > 应用框架开发 > UI框架 > 组件使用 > 如何用Progress组件显示任务列表进度
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:03+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:9cf202d060463fdc88684f357fe07555691b77639ccbe8c0f89f7ad9b8ccb442
---

## 问题现象

使用Progress进度条组件展示任务进度时出现问题：

1. 总任务数5，已完成任务数3，此时删除一条已完成的任务，进度条先增长再减少。这个问题是什么原因导致的，如何解决？

   问题代码如下：

   ```ts
   @Entry
   @Component
   struct TaskListPage1 {
     @State finishedTask: number = 0; // 已完成任务数
     @State totalTask: number = 0; // 总任务数
     @State tasks: TaskInfo[] = []; // 任务列表
     @State deleteButtonBgcolor: string | Color = '#E84026'; // 删除按钮的颜色

     // 删除任务按钮
     @Builder
     DeleteTask(index: number) {
       Stack() {
         Image($r('app.media.ic_public_trash')) // 删除图标，可以更换其他资源
           .draggable(false)
           .width(20);
       }
       .width(40)
       .height(40)
       .borderRadius('50%')
       .margin({ left: 16 })
       .backgroundColor(this.deleteButtonBgcolor)
       .onTouch((event?: TouchEvent) => {
         if (event) {
           if (event.type === TouchType.Down) {
             this.deleteButtonBgcolor = '#AAE84026'; // 按下时图标背景颜色
           } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
             this.deleteButtonBgcolor = '#E84026'; // 取消或抬起恢复图标背景颜色
           }
         }
       })
       .onClick(() => {
         this.tasks.splice(index, 1); // 任务列表删除当前索引的任务
         this.finishedTask = this.tasks.filter((item): boolean => item.isFinished).length; // 重新获取已完成任务数
         this.totalTask = this.tasks.length; // 获取总任务数
       });
     }

     build() {
       Column() {
         // 任务进度以及新增任务按钮
         TaskProgress({ finishedTask: this.finishedTask, totalTask: this.totalTask, tasks: this.tasks }).margin(16);
         // 任务列表
         List({ space: 8 }) {
           ForEach(this.tasks, (item: TaskInfo, index: number) => {
             ListItem() {
               TaskItem({ item: item, finishedTask: this.finishedTask, tasks: this.tasks });
             }.padding({ left: 16, right: 16 })
             .swipeAction({ end: this.DeleteTask(index), edgeEffect: SwipeEdgeEffect.None }); // 左滑出现删除按钮
           });
         }
         .layoutWeight(1)
         .width('100%')
         .scrollBar(BarState.Off);
       }
       .height('100%')
       .width('100%')
       .backgroundColor('#f1f3f5')
       .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
     }
   }

   // 任务进度组件
   @Component
   export struct TaskProgress {
     @Link finishedTask: number;
     @Link totalTask: number;
     @Link tasks: TaskInfo[];
     taskId: number = 0;

     build() {
       Column({ space: 20 }) {
         Row() {
           Text('任务进度：')
             .fontSize(25)
             .fontWeight(FontWeight.Bold);
           // 使用Stack堆叠容器，将进度条和进度展示层叠显示
           Stack() {
             // Start solution1
             Progress({
               value: this.finishedTask, // 进度值，已完成数
               total: this.totalTask, // 进度总长，总任务数
               type: ProgressType.Ring, // 环形
             }).width(90);
             // End solution1
             Text(`${this.finishedTask} / ${this.totalTask}`).fontSize(25);
           };
         }
         .borderRadius(10)
         .height(110)
         .justifyContent(FlexAlign.Center)
         .backgroundColor(Color.White)
         .width('100%');

         Button('新增任务')
           .width('60%')
           .onClick(() => {
             this.tasks.push(new TaskInfo(this.taskId++, false));
             this.totalTask = this.tasks.length;
           });
       }.width('100%');
     }
   }

   // 任务项组件
   @Component
   export struct TaskItem {
     @State item: TaskInfo = new TaskInfo(0, false);
     @Link finishedTask: number;
     @Link tasks: TaskInfo[];

     build() {
       Row() {
         Text(`ID:${this.item.id}`).fontSize(16);
         Checkbox()
           .width(30)
           .shape(CheckBoxShape.CIRCLE)
           .select(this.item.isFinished)
           .onClick(() => {
             if (this.item.isFinished === true) {
               this.finishedTask--;
             } else {
               this.finishedTask++;
             }
             this.item.isFinished = !this.item.isFinished;
           });
       }
       .justifyContent(FlexAlign.SpaceBetween)
       .borderRadius(20)
       .padding({ left: 20, right: 20 })
       .backgroundColor(Color.White)
       .height(56)
       .width('100%');
     }
   }

   // 任务信息，id和完成情况
   export class TaskInfo {
     id: number;
     isFinished: boolean;

     constructor(id: number, isFinished: boolean) {
       this.id = id;
       this.isFinished = isFinished;
     }
   }
   ```

   现象效果图如下：

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/WoHIbE6wREOyLTIVZhp8Eg/zh-cn_image_0000002658916951.png "点击放大")
2. 在问题一的场景中，删除任务后，如何实现进度条从0平滑增长到当前进度的动画效果？

## 背景知识

[Progress](../harmonyos-references/ts-basic-components-progress.md)是进度条显示组件，显示内容为目标操作的当前进度。当进度条组件的样式[style](../harmonyos-references/ts-basic-components-progress.md#style8)中enableSmoothEffect设置为true时（默认为true），表示开启平滑动效，进度值[value](../harmonyos-references/ts-basic-components-progress.md#value)变化时会产生动画效果。

## 解决方案

* **问题一**

  **问题原因**：当删除一个任务项时会修改进度条当前进度值value和进度总长total，当前问题中的情况是3/5改为2/4。默认情况下Progress组件修改total不会产生动画效果，修改value才会展示动画，所以这里的效果是3/5首先因为total变化直接渲染成3/4，再产生3/4到2/4的动画效果。

  **修改方案**：可以将Progress组件的total值设定为一个固定值，只修改value值让任务进度变化。如将进度条total值设置为100，进度值设置为(完成数/任务总数)\*100，任务总数为0时单独设置进度值为0。可以避免Progress组件的total变动导致进度条先增后减。

  核心代码如下：

  ```ts
  Progress({
    value: this.totalTask === 0 ? 0 : (this.finishedTask / this.totalTask) * 100, // 当前进度值占总进度百分比
    total: 100, // 进度总长设置固定值100
    type: ProgressType.Ring, // 环形
  }).width(90);
  ```

  完整代码如下：

  ```ts
  @Entry
  @Component
  struct TaskListPage1 {
    @State finishedTask: number = 0; // 已完成任务数
    @State totalTask: number = 0; // 总任务数
    @State tasks: TaskInfo[] = []; // 任务列表
    @State deleteButtonBgcolor: string | Color = '#E84026'; // 删除按钮的颜色

    // 删除任务按钮
    @Builder
    DeleteTask(index: number) {
      Stack() {
        Image($r('app.media.ic_public_trash')) // 删除图标，可以更换其他资源
          .draggable(false)
          .width(20);
      }
      .width(40)
      .height(40)
      .borderRadius('50%')
      .margin({ left: 16 })
      .backgroundColor(this.deleteButtonBgcolor)
      .onTouch((event?: TouchEvent) => {
        if (event) {
          if (event.type === TouchType.Down) {
            this.deleteButtonBgcolor = '#AAE84026'; // 按下时图标背景颜色
          } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
            this.deleteButtonBgcolor = '#E84026'; // 取消或抬起恢复图标背景颜色
          }
        }
      })
      .onClick(() => {
        this.tasks.splice(index, 1); // 任务列表删除当前索引的任务
        this.finishedTask = this.tasks.filter((item): boolean => item.isFinished).length; // 重新获取已完成任务数
        this.totalTask = this.tasks.length; // 获取总任务数
      });
    }

    build() {
      Column() {
        // 任务进度以及新增任务按钮
        TaskProgress({ finishedTask: this.finishedTask, totalTask: this.totalTask, tasks: this.tasks }).margin(16);
        // 任务列表
        List({ space: 8 }) {
          ForEach(this.tasks, (item: TaskInfo, index: number) => {
            ListItem() {
              TaskItem({ item: item, finishedTask: this.finishedTask, tasks: this.tasks });
            }.padding({ left: 16, right: 16 })
            .swipeAction({ end: this.DeleteTask(index), edgeEffect: SwipeEdgeEffect.None }); // 左滑出现删除按钮
          });
        }
        .layoutWeight(1)
        .width('100%')
        .scrollBar(BarState.Off);
      }
      .height('100%')
      .width('100%')
      .backgroundColor('#f1f3f5')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
  }

  // 任务进度组件
  @Component
  export struct TaskProgress {
    @Link finishedTask: number;
    @Link totalTask: number;
    @Link tasks: TaskInfo[];
    taskId: number = 0;

    build() {
      Column({ space: 20 }) {
        Row() {
          Text('任务进度：')
            .fontSize(25)
            .fontWeight(FontWeight.Bold);
          // 使用Stack堆叠容器，将进度条和进度展示层叠显示
          Stack() {
            Progress({
              value: this.totalTask === 0 ? 0 : (this.finishedTask / this.totalTask) * 100, // 当前进度值占总进度百分比
              total: 100, // 进度总长设置固定值100
              type: ProgressType.Ring, // 环形
            }).width(90);
            Text(`${this.finishedTask} / ${this.totalTask}`).fontSize(25);
          };
        }
        .borderRadius(10)
        .height(110)
        .justifyContent(FlexAlign.Center)
        .backgroundColor(Color.White)
        .width('100%');

        Button('新增任务')
          .width('60%')
          .onClick(() => {
            this.tasks.push(new TaskInfo(this.taskId++, false));
            this.totalTask = this.tasks.length;
          });
      }.width('100%');
    }
  }

  // 任务项组件
  @Component
  export struct TaskItem {
    @State item: TaskInfo = new TaskInfo(0, false);
    @Link finishedTask: number;
    @Link tasks: TaskInfo[];

    build() {
      Row() {
        Text(`ID:${this.item.id}`).fontSize(16);
        Checkbox()
          .width(30)
          .shape(CheckBoxShape.CIRCLE)
          .select(this.item.isFinished)
          .onClick(() => {
            if (this.item.isFinished === true) {
              this.finishedTask--;
            } else {
              this.finishedTask++;
            }
            this.item.isFinished = !this.item.isFinished;
          });
      }
      .justifyContent(FlexAlign.SpaceBetween)
      .borderRadius(20)
      .padding({ left: 20, right: 20 })
      .backgroundColor(Color.White)
      .height(56)
      .width('100%');
    }
  }

  // 任务信息，id和完成情况
  export class TaskInfo {
    id: number;
    isFinished: boolean;

    constructor(id: number, isFinished: boolean) {
      this.id = id;
      this.isFinished = isFinished;
    }
  }
  ```

  运行效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/BzWjGUtaSR60OF6naomdMA/zh-cn_image_0000002628397742.png "点击放大")
* **问题二**

  可以将style中enableSmoothEffect设置为false取消进度条本身的动效，自定义删除任务时的动画效果实现该场景。在删除任务时首先设置进度值为0，再通过[animateTo](../harmonyos-references/arkts-apis-uicontext-uicontext.md#animateto)展示进度从0回到当前进度的动画效果。

  核心代码如下：

  ```ts
  .onClick(() => {
    this.tasks.splice(index, 1); // 任务列表删除当前索引的任务
    this.finishedTask = 0; // 删除后先把进度设为0
    this.totalTask = this.tasks.length; // 获取总任务数
    this.uiContext.animateTo({}, () => { // 展示0到当前进度的动画
      this.finishedTask = this.tasks.filter((item): boolean => item.isFinished).length; // 重新获取已完成任务数
    });
  });
  ```

  完整代码如下：

  ```ts
  @Entry
  @Component
  struct TaskListPage2 {
    @State finishedTask: number = 0; // 已完成任务数
    @State totalTask: number = 0; // 总任务数
    @State tasks: TaskInfo[] = []; // 任务列表
    @State deleteButtonBgcolor: string | Color = '#E84026'; // 删除按钮的颜色
    uiContext: UIContext = this.getUIContext();

    // 删除任务按钮
    @Builder
    DeleteTask(index: number) {
      Stack() {
        Image($r('app.media.ic_public_trash')) // 删除图标，可以更换其他资源
          .draggable(false)
          .width(20);
      }
      .width(40)
      .height(40)
      .borderRadius('50%')
      .margin({ left: 16 })
      .backgroundColor(this.deleteButtonBgcolor)
      .onTouch((event?: TouchEvent) => {
        if (event) {
          if (event.type === TouchType.Down) {
            this.deleteButtonBgcolor = '#AAE84026'; // 按下时图标背景颜色
          } else if (event.type === TouchType.Up || event.type === TouchType.Cancel) {
            this.deleteButtonBgcolor = '#E84026'; // 取消或抬起恢复图标背景颜色
          }
        }
      })
      .onClick(() => {
        this.tasks.splice(index, 1); // 任务列表删除当前索引的任务
        this.finishedTask = 0; // 删除后先把进度设为0
        this.totalTask = this.tasks.length; // 获取总任务数
        this.uiContext.animateTo({}, () => { // 展示0到当前进度的动画
          this.finishedTask = this.tasks.filter((item): boolean => item.isFinished).length; // 重新获取已完成任务数
        });
      });
    }

    build() {
      Column() {
        // 任务进度以及新增任务按钮
        TaskProgress({ finishedTask: this.finishedTask, totalTask: this.totalTask, tasks: this.tasks }).margin(16);
        // 任务列表
        List({ space: 8 }) {
          ForEach(this.tasks, (item: TaskInfo, index: number) => {
            ListItem() {
              TaskItem({ item: item, finishedTask: this.finishedTask, tasks: this.tasks });
            }.padding({ left: 16, right: 16 })
            .swipeAction({ end: this.DeleteTask(index), edgeEffect: SwipeEdgeEffect.None }); // 左滑出现删除按钮
          });
        }
        .layoutWeight(1)
        .width('100%')
        .scrollBar(BarState.Off);
      }
      .height('100%')
      .width('100%')
      .backgroundColor('#f1f3f5')
      .expandSafeArea([SafeAreaType.SYSTEM], [SafeAreaEdge.TOP, SafeAreaEdge.BOTTOM]);
    }
  }

  // 任务进度组件
  @Component
  export struct TaskProgress {
    @Link finishedTask: number;
    @Link totalTask: number;
    @Link tasks: TaskInfo[];
    taskId: number = 0;

    build() {
      Column({ space: 20 }) {
        Row() {
          Text('任务进度：')
            .fontSize(25)
            .fontWeight(FontWeight.Bold);
          // 使用Stack堆叠容器，将进度条和进度展示层叠显示
          Stack() {
            Progress({
              value: this.finishedTask, // 进度值，已完成数
              total: this.totalTask, // 进度总长，总任务数
              type: ProgressType.Ring, // 环形
            }).style({ enableSmoothEffect: false }) // 禁用进度条动画
              .width(90);
            Text(`${this.finishedTask} / ${this.totalTask}`).fontSize(25);
          };
        }
        .borderRadius(10)
        .height(110)
        .justifyContent(FlexAlign.Center)
        .backgroundColor(Color.White)
        .width('100%');

        Button('新增任务')
          .width('60%')
          .onClick(() => {
            this.tasks.push(new TaskInfo(this.taskId++, false));
            this.totalTask = this.tasks.length;
          });
      }.width('100%');
    }
  }

  // 任务项组件
  @Component
  export struct TaskItem {
    @State item: TaskInfo = new TaskInfo(0, false);
    @Link finishedTask: number;
    @Link tasks: TaskInfo[];
    uiContext: UIContext = this.getUIContext();

    build() {
      Row() {
        Text(`ID:${this.item.id}`).fontSize(16);
        Checkbox()
          .width(30)
          .shape(CheckBoxShape.CIRCLE)
          .select(this.item.isFinished)
          .onClick(() => {
            this.uiContext.animateTo({ duration: 200 }, () => {
              if (this.item.isFinished === true) {
                this.finishedTask--;
              } else {
                this.finishedTask++;
              }
              this.item.isFinished = !this.item.isFinished;
            });
          });
      }
      .justifyContent(FlexAlign.SpaceBetween)
      .borderRadius(20)
      .padding({ left: 20, right: 20 })
      .backgroundColor(Color.White)
      .height(56)
      .width('100%');
    }
  }

  // 任务信息，id和完成情况
  export class TaskInfo {
    id: number;
    isFinished: boolean;

    constructor(id: number, isFinished: boolean) {
      this.id = id;
      this.isFinished = isFinished;
    }
  }
  ```

  运行效果图如下：

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/mqnKsYYEQiKoOcvyqbwO1g/zh-cn_image_0000002658797005.png "点击放大")

## 常见FAQ

Q：Progress组件显示完成进度时，如何不展示动画？

A：可以将Progress组件style中enableSmoothEffect设置为false，关闭进度值变化时的动效。

## 总结

默认情况下Progress组件修改进度值value会触发动画效果，修改进度总长total会直接渲染。如果在未关闭进度平滑动效时修改total和value，会出现预期外的视觉表现（如进度先增后减）。建议设置total值为100，通过进度完成情况百分比计算value更新进度值，避免直接修改total。
