---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-45
title: 页面向上滑动不流畅，到达底部时频繁等待加载
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 页面向上滑动不流畅，到达底部时频繁等待加载
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:3cefa6bcfe023fba92d01b5756201ba4062bd9d6ab7ed2461315a0b50c6fef7c
---

## 问题现象

浏览应用内页面时，频繁出现滑动到底后需要等待加载的情况，使用体验不流畅。

## 背景知识

* [Smartperf\_Host](https://gitcode.com/openharmony/developtools_smartperf_host/tree/master/smartperf_host)是一款用于深入挖掘和细粒度展示数据的性能功耗调优工具。它可以采集CPU调度、频点、进程线程时间片、堆内存、帧率等数据，并通过泳道图清晰地呈现给开发者。同时，SmartPerf通过GUI以可视化的方式进行分析。目前，该工具为开发者提供了五个分析模板：帧率分析、CPU/线程调度分析、应用启动分析、TaskPool分析和动效分析。
* [WaterFlow](../harmonyos-references/ts-container-waterflow.md)即瀑布流容器，由“行”和“列”分割的单元格所组成，通过容器自身的排列规则，将不同大小的“项目”自上而下，如瀑布般紧密布局。

## 问题定位

1. 使用ArkUI Inspector可以看到相关页面是通过WaterFlow瀑布流实现的。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/JEx_i6tbSC2_AolM5jWVMw/zh-cn_image_0000002628395282.png "点击放大")
2. 使用SmartPerf打开Trace文件，在应用包名主泳道找到H:APP\_LIST\_FLING子泳道，通过泳道中的Trace点可以得知抛滑动作全过程。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/74Txj6UFTxuGYXq97mz6DA/zh-cn_image_0000002658794557.png "点击放大")
3. 在抛滑动作结束后可以在应用包名主线程看到有明显耗时异常的Trace点，根据Duration字段可得知单帧耗时54ms左右。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/RH3W4D44T4Ct5quxahojtg/zh-cn_image_0000002628555194.png "点击放大")
4. 框选异常Trace点，在Slices中可以看到这一帧内创建FlowItemView和LazyItem的数量较多。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/Dg3hnTguQ428O6lOd_30ew/zh-cn_image_0000002658914515.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/MSlZfhvXQ8Kgt2XEAUYcYA/zh-cn_image_0000002628395284.png "点击放大")
5. 在左上角搜索框中分别搜索FlowItemView和LazyItem，可以看到H:CustomNode:BuildItem [FlowItemView]有15次，共耗时18.633ms；H:Builder:BuildLazyItem有23次，共耗时14.311ms。因此是瀑布流无限滚动至末尾时触发的onReachEnd事件回调中对LazyForEach增加新数据耗时导致整体加载耗时。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/Qd9wJPdTRNGXdX_VDDnecQ/zh-cn_image_0000002658794561.png "点击放大")![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/2sZs94VkRvm08cVE1Ih58g/zh-cn_image_0000002628555196.png "点击放大")

   如下示例代码实现瀑布流的无限滚动会出现滑动至底部停顿加载的现象。

   ```screen
    class WaterFlowDataSource implements IDataSource {
      private dataArray: number[] = []
      private listeners: DataChangeListener[] = []

      constructor() {
        for (let i = 0; i < 100; i++) {
          this.dataArray.push(i)
        }
      }

      public getData(index: number): number {
        return this.dataArray[index]
      }

      notifyDataReload(): void {
        this.listeners.forEach(listener => {
          listener.onDataReloaded()
        })
      }

      notifyDataAdd(index: number): void {
        this.listeners.forEach(listener => {
          listener.onDataAdd(index)
        })
      }

      notifyDataChange(index: number): void {
        this.listeners.forEach(listener => {
          listener.onDataChange(index)
        })
      }

      notifyDataDelete(index: number): void {
        this.listeners.forEach(listener => {
          listener.onDataDelete(index)
        })
      }

      notifyDataMove(from: number, to: number): void {
        this.listeners.forEach(listener => {
          listener.onDataMove(from, to)
        })
      }

      public totalCount(): number {
        return this.dataArray.length
      }

      registerDataChangeListener(listener: DataChangeListener): void {
        if (this.listeners.indexOf(listener) < 0) {
          this.listeners.push(listener)
        }
      }

      unregisterDataChangeListener(listener: DataChangeListener): void {
        const pos = this.listeners.indexOf(listener)
        if (pos >= 0) {
          this.listeners.splice(pos, 1)
        }
      }

      public addNewItems(count: number): void {
        let len = this.dataArray.length;
        for (let i = 0; i < count; i++) {
          this.dataArray.push(this.dataArray.length);
        }
        this.listeners.forEach(listener => {
          listener.onDatasetChange([{ type: DataOperationType.ADD, index: len, count: count }]);
        })
      }
    }

    @Reusable
    @Component
    struct ReusableFlowItem {
      @State item: number = 0;

      build() {
        Text(this.item + 1 + '')
          .fontWeight(FontWeight.Regular)
          .fontSize(20)
          .fontColor(Color.Black)
      }
    }

    @Entry
    @Component
    export struct WaterFlowPage {
      private dataSource: WaterFlowDataSource = new WaterFlowDataSource();
      scroller: Scroller = new Scroller();

      @Builder
      itemFoot() {
        Row() {
          LoadingProgress()
            .color(Color.Blue).height(50).aspectRatio(1).width('20%')
          Text(`正在加载`)
            .fontSize(20)
            .width('30%')
            .height(50)
            .align(Alignment.Center)
            .margin({ top: 2 })
        }.width('100%').justifyContent(FlexAlign.Center)
      }

      build() {
        Column({ space: 2 }) {
          WaterFlow({ footer: this.itemFoot(), layoutMode: WaterFlowLayoutMode.SLIDING_WINDOW }) {
            LazyForEach(this.dataSource, (item: number) => {
              FlowItem() {
                ReusableFlowItem({ item: item })
              }
              .width('100%')
              .height(200)
              .border({
                width: 1,
                color: Color.Black
              })
            }, (item: string) => item)
          }
          .columnsTemplate('1fr '.repeat(3))
          .backgroundColor(Color.White)
          .width('100%')
          .height('100%')
          .layoutWeight(1)
          // 触底加载数据
          .onReachEnd(() => {
            setTimeout(() => {
              this.dataSource.addNewItems(100);
            }, 500);
          })
        }
      }
    }
   ```

## 分析结论

瀑布流无限滚动至末尾时新增组件耗时导致整体加载耗时。

## 修改建议

调整增加新数据的时机，在LazyForEach还剩余若干个数据未遍历的情况下[提前新增数据](../harmonyos-guides/arkts-layout-development-create-waterflow.md#提前新增数据)。
