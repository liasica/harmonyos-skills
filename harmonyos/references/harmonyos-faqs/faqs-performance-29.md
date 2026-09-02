---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-29
title: 点击返回按钮响应慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 点击返回按钮响应慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:414f80b53f736586c82d1e939ddffa89550e5c34e971bd375503dbe5d6169282
---

## 问题现象

点击页面返回按钮返回到上一状态时响应慢，过了一段时间界面才有变化。

## 背景知识

* 点击应用页面内容到屏幕上有反应过程，设备整体处理流程大致如下：
  + 多模输入服务mmi\_service线程收到用户触摸屏幕的相关事件（比如按下、滑动、离开屏幕），根据窗口的触摸热区判定分发给应用。
  + 应用侧在收到Vsync信号后会响应用户的屏幕点击等输入事件，执行相关的业务流程，如跳转到新页面、显示按钮被按下的效果等，提交绘制指令给render\_service。
  + render\_service会根据绘制指令进行相应的图形计算和渲染操作，将渲染结果写入到帧缓冲区（存储用于显示器输出的图像数据）中，将数据送到屏幕上显示。

* DevEco Profiler：集成在DevEco Studio中的性能调优工具，提供场景化的性能调优功能体验，可以检测应用的性能指标、录制Trace信息，通过分析Trace数据能够发现代码中的性能瓶颈，进而优化性能，更多详细内容可参见[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。

  点击按钮响应慢相关Trace关键字如下：

  | 关键字 | 线程/泳道 | 说明 | 备注 |
  | --- | --- | --- | --- |
  | H:originEventHandle code:501 | mmi\_service | mmi\_service检测到手指离开屏幕。 |  |
  | H:DispatchTouchEvent XXX type=1 | 应用包名 | 应用收到点击离手的事件。 | 应用模块处理起点。 |
  | H:SendCommands | 应用包名 | 应用发送渲染请求，下方H:MarshRSTransactionData表示提交绘制相关数据给render\_service，transactionFlag中包含了应用进程号和序号。 | 应用模块处理终点。 |
  | H:RSMainThread::ProcessCommandUni[应用进程号，序号] | render\_service | render\_service处理渲染请求，在接收Vsync信号时执行，应用进程号、序号与应用发送渲染请求的transactionFlag相同。 | render\_service处理起点。 |
  | H:RSHardwareThread::CommitAndReleaseLayers rate: 帧率，now：时间戳 | RSHardwareThread | 将GPU处理的渲染结果提交到显示硬件，now与H:RSMainThread::ProcessCommandUni上方的H:ReceiveVsync中的now字段一一对应。 | render\_service处理终点。 |
  | H:CustomNode:OnAppear | 应用包名 | 执行自定义组件的aboutToAppear方法。 |  |
  | H:CreateTaskMeasure[组件名][self:组件ID][parent:父组件ID] | 应用包名 | 创建组件并执行测量任务。 |  |

## 问题定位

1. 使用DevEco Studio Frame分析工具抓取点击返回按钮过程的Trace信息，然后在抓取结果上方的输入框分别输入H:originEventHandle code:501、type=1找到mmi\_service检测到手指离开屏幕、应用收到点击离手事件的Trace点。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/q5MliYVGTfiQeNrBwPhDJg/zh-cn_image_0000002628555074.png "点击放大")

   然后以应用收到点击离手事件的Trace点为起点，在上方输入框分别输入H:MarshRSTransactionData、H:RSMainThread::ProcessCommandUni、H:RSHardwareThread::CommitAndReleaseLayers找到应用第一次发送渲染请求、render\_service处理渲染请求、render\_service提交渲染结果的Trace点。计算Trace关键字的时间间隔，得到mmi\_service、应用、render\_service各阶段耗时如下图表所示，耗时主要集中在应用部分。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/nOwJfwBlT9quH6EQdJsl3A/zh-cn_image_0000002628395168.png "点击放大")

   | mmi\_service | 应用 | 应用->render\_service（应用结束点到render\_service起始点） | render\_service | 总和 |
   | --- | --- | --- | --- | --- |
   | 3.3ms | 251.7ms | 13.2ms | 25.0ms | 293.2ms |
2. 分析应用阶段Trace信息，发现耗时主要包含执行自定义组件的aboutToAppear、组件测量部分，可通过ArkTS Callstack泳道查看耗时部分的堆栈信息，确认耗时原因。

   aboutToAppear部分的堆栈信息中可看到执行了XXXPage组件的aboutToAppear函数，该函数中调用了一个load方法较耗时。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/J5bmDgVBQSeI3k_cZE0uJw/zh-cn_image_0000002658914397.png "点击放大")

   组件测量部分的堆栈中可看到有初始化渲染大量组件，组件创建较耗时。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/kPd3J9WzTZa1mcaTYIp3-w/zh-cn_image_0000002658794439.png "点击放大")

   结合前后两者信息可知，在点击返回按钮时，应用创建了XXXPage组件，该组件包含大量子组件，执行aboutToAppear和测量时耗时较多，导致响应慢的问题。

## 分析结论

点击返回按钮时，应用创建组件、执行耗时操作，导致响应慢的问题。

## 修改建议

* 点击返回按钮时，不创建新组件，仅通过设置状态变量来更新页面显示的内容。
* 将耗时操作移到子线程中处理。

```ts
import { taskpool } from '@kit.ArkTS';
import { BusinessError } from '@ohos.base';

// 循环打印模拟耗时任务
@Concurrent
async function timeConsumingTask() : Promise<number> {
  console.info('startTask');
  for (let i = 0; i < 100000; i++) {
    console.info(`number:${i}`);
  }
  return 1;
}

@Entry
@Component
struct TaskPoolDemoPage {
  build() {
    RelativeContainer() {
      Button('执行耗时任务')
        .onClick(() => {
          taskpool.execute(timeConsumingTask).then((result: Object) => {
            console.info(`result:${result as number}`);
          }).catch((error: BusinessError) => {
            console.error(`Failed to execute task: errCode is ${error.code}, errMessage is ${error.message}`);
          });
        })
        .alignRules({
          center: { anchor: '__container__', align: VerticalAlign.Center },
          middle: { anchor: '__container__', align: HorizontalAlign.Center }
        })
    }
    .height('100%')
    .width('100%')
  }
}
```
