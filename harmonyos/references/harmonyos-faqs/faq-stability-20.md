---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-20
title: 应用在使用过程中持续出现闪退
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用在使用过程中持续出现闪退
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b4c383378b7081ae6e6d178273582c262c3d5f01e1e971667133a2f5b9467a01
---

## 问题现象

应用在使用过程中，频繁上下滑动列表导致闪退。

## 背景知识

* 用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为应用无响应，详情参考[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。
* AppFreeze日志规格说明可以参考[日志规格](../harmonyos-guides/appfreeze-guidelines.md#日志规格)。
* [渲染范围控制](../best-practices/bpta-control-rendering-range.md)：在应用开发中，控制UI渲染范围，防止界面卡顿或掉帧。
* [布局节点减少](../best-practices/bpta-reduce-layout-nodes.md)：在进行页面布局开发时，应该尽量减少布局节点，避免系统绘制更多的布局组件，达到优化渲染性能、减少内存占用的目的。
* [HiSmartPerf](../AppGallery-connect-Guides/smartperf-tool-0000001873208929.md)：无需ROOT设备，即可准确、高效地采集到应用运行时的CPU、GPU等性能数据，了解应用的性能状况。

## 问题定位

1. 查看faultlogger目录下应用的Appfreeze日志，当前执行的任务是vSyncTask绘制任务，开始执行的时间是08:06:44.719，任务执行到08:06:51.671还未结束，执行时间超过7s，任务执行时间过长导致应用卡死。

   ```screen
   Fault time:2025/07/05-08:06:51
   User input does not respond!
   mainHandler dump is:
    EventHandler dump begin curTime: 2025-07-05 08:06:51.671
    Event runner (Thread name = , Thread ID = 29310) is running
    Current Running: start at 2025-07-05 08:06:44.720, Event { send thread = 29310, send time = 2025-07-05 08:06:44.719, handle time = 2025-07-05 08:06:44.719, trigger time = 2025-07-05 08:06:44.719, task name = vSyncTask, caller = [event_queue.cpp(HandleFileDescriptorEvent:280)] }
    History event queue information:
   ```
2. 搜索关键字TID:进程ID(PID)，可以获取应用栈信息。08:06:52:99应用主线程在执行initialRender任务，和页面渲染有关。

   ```screen
   Timestamp:2025-07-05 08:06:52:99
   Tid:29310, Name:com.hx.example
   #00 pc 0000000000447434 /system/lib64/module/arkcompiler/stub.an(RTStub_CallGetter+320)
   #01 at anonymous (entry|common|1.0.0|src/main/ets/components/BillComponent.ts:370:1)
   #02 at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:9157:1)
   #03 at observeComponentCreation2 (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:9177:1)
   #04 at anonymous (entry|common|1.0.0|src/main/ets/components/BillComponent.ts:368:1)
   #05 at ifElseBranchUpdateFunction (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:4300:1)
   #06 at anonymous (entry|common|1.0.0|src/main/ets/components/BillComponent.ts:367:1)
   #07 at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:9157:1)
   #08 at observeComponentCreation2 (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:9177:1)
   #09 at anonymous (entry|common|1.0.0|src/main/ets/components/BillComponent.ts:337:1)
   #10 at ifElseBranchUpdateFunction (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:4300:1)
   #11 at anonymous (entry|common|1.0.0|src/main/ets/components/BillComponent.ts:280:1)
   #12 at updateFunc (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:9157:1)
   #13 at observeComponentCreation2 (/usr1/hmos_for_system/src/increment/sourcecode/foundation/arkui/ace_engine/frameworks/bridge/declarative_frontend/engine/stateMgmt.js:9177:1)
   #14 at initialRender (entry|common|1.0.0|src/main/ets/components/BillComponent.ts:45:1)
   ```
3. 使用HiSmartPerf工具抓取该过程的Trace信息，从Duration可以看出preload任务执行时间达到9s。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/I93eruBySOaSe3eo_BXXoA/zh-cn_image_0000002628316280.png "点击放大")
4. 框选主线程29310中preload任务所在的泳道，其中绝大部分时间都在执行MeasureListItem节点布局任务。过滤MeasureListItem任务，节点布局任务执行总时长达到6.8s，任务数量达到823个。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/YR22m03pRr-CWMvJHfR44w/zh-cn_image_0000002658675509.png "点击放大")
5. 部分节点布局复杂，布局时间达到525ms，且节点数量过多，结合ListItem的使用场景可知应用在加载列表项时没有采用懒加载的方式。

## 分析结论

页面布局复杂并且长列表未采用懒加载导致应用卡死。

## 修改建议

使用懒加载优化长列表加载速度，参考文档[长列表加载](../best-practices/bpta-lazyforeach-optimization.md#section1847219719551)。

```screen
interface DataChangeListener {
  onDataReloaded(): void;

  onDataAdd(index: number): void;

  onDataDelete(index: number): void;

  onDataChange(index: number): void;
}

export class MyDataSource {
  private _data: string[] = [];
  private _listeners: DataChangeListener[] = [];

  pushData(item: string): void {
    this._data.push(item);
    this._listeners.forEach(listener => {
      listener.onDataAdd(this._data.length - 1);
    });
  }

  getAllData(): string[] {
    return this._data;
  }

  totalCount(): number {
    return this._data.length;
  }

  getData(index: number): string {
    return this._data[index];
  }

  registerDataChangeListener(listener: DataChangeListener): void {
    this._listeners.push(listener);
  }

  unregisterDataChangeListener(listener: DataChangeListener): void {
    const index = this._listeners.indexOf(listener);
    if (index !== -1) {
      this._listeners.splice(index, 1);
    }
  }
}

@Entry
@Component
struct MyComponent {
  private data: MyDataSource = new MyDataSource();

  aboutToAppear() {
    for (let i = 0; i <= 100; i++) {
      this.data.pushData(`Hello ${i}`);
    }
  }

  build() {
    List({ space: 3 }) {
      LazyForEach(this.data, (item: string) => {
        ListItem() {
          Row() {
            Text(item).fontSize(50)
              .onAppear(() => {
                console.info(`appear: ${item}`);
              });
          }.margin({ left: 10, right: 10 });
        };
      }, (item: string) => item);
    }.cachedCount(5);
  }
}
```
