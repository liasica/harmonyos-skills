---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-performance-18
title: 页面文字、按钮等内容加载慢
breadcrumb: FAQ > 应用质量 > 技术质量 > 性能 > 页面文字、按钮等内容加载慢
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:51+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:93d85b740ac2a351efb3efbf651f59c8b74fb395ccec8b6f885bb235e6d8fbc3
---

## 问题现象

页面加载过程时，整体内容加载较快，而单个文字、按钮或某个区域内容必定出现加载慢的现象。

## 背景知识

* [Image](../harmonyos-references/ts-basic-components-image.md)：图片组件，常用于在应用中显示图片。图片组件在加载图片时默认是异步加载方式，可通过[syncLoad](../harmonyos-references/ts-basic-components-image.md#syncload8)设置成同步加载方式。由于同步加载是在主线程上执行，建议在加载尺寸较小的本地图片时使用，如尺寸较大或网络图片则采用异步加载方式。
* ArkUI Inspector：DevEco Studio提供的[布局分析](../harmonyos-guides/ide-arkui-inspector.md)工具，开发者可以借助它预览真机或模拟器中的UI效果，快速定位布局层级问题，也可以观察组件属性、不同组件之间的关系等。
* DevTools：Web前端开发调试工具，支持在电脑上调试移动设备前端页面。开发者通过[setWebDebuggingAccess](../harmonyos-references/arkts-apis-webview-webviewcontroller.md#setwebdebuggingaccess)接口开启Web组件前端页面调试能力，使用DevTools在电脑上调试移动前端网页，更多内容可参考[使用DevTools工具调试前端页面](../harmonyos-guides/web-debugging-with-devtools.md)。
* DevEco Profiler：DevEco Studio提供的场景化调优工具，开发者可以用来完成不同应用模型和场景下的完整性能数据采集，更高效地进行性能问题的分析，更多详细内容可参考[使用Profiler进行性能调优](../harmonyos-guides/ide-profiler-introduction.md)。常见Trace关键字如下：

  | 关键字 | 说明 |
  | --- | --- |
  | H:Create[组件名][self:组件id] | 组件创建 |
  | H:ViewPU.viewPropertyHasChanged 组件名 状态变量名 N | 某个组件状态变量发生更新，N表示该状态变量更新后影响的组件数量。需要在应用启动前运行hdc shell param set persist.ace.debug.enabled 1命令才可以看到该Trace关键字 |
  | H:ABILITY\_OR\_PAGE\_SWITCH | 页面切换过程 |
  | H:MarshRSTransactionData | 应用提交渲染数据给render\_service |

## 问题定位

运行hdc shell param set persist.ace.debug.enabled 1命令、重启应用，使用ArkUI Inspector抓取问题场景下的页面布局，确认当前页面是什么页面，然后进一步分析。

* 应用页面是ArkUI页面：
  1. 使用ArkUI Inspector抓取页面组件树，发现该页面为ArkUI页面，应用采用Text组件来显示页面文字，因此可以分析Trace中Text组件创建时机来确认加载慢的原因。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/3ynQGH9_T1SsdbZLJodj4A/zh-cn_image_0000002628555046.png "点击放大")
  2. 使用DevEco Profiler ArkUI模板工具抓取加载过程的Trace信息，在上方搜索H:ABILITY\_OR\_PAGE\_SWITCH确认页面切换完成的时间、搜索H:Create[Text][self:组件id]确认该文本组件创建的时间，对比两者的时间点进一步分析，可能的情况有：
     + 组件创建在页面切换完成之后，如下图可看到两者时间间隔2.4s。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/picHn8miTsaXhbb_g41R0w/zh-cn_image_0000002628395142.png "点击放大")

       排查文本组件创建前Trace信息，有发现状态变量更新，推测该状态变量包含文本组件构建时传入的文本内容参数。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/Ag71UJTQR5mX4R-FsXkiVg/zh-cn_image_0000002658914367.png "点击放大")

       在代码中检索状态变量ChildItem，确认该变量为Text文本组件的文本内容参数，同时在进入该应用页面时延迟3秒才更新该状态变量（参考以下代码为例），文本内容参数设置较慢，导致文本加载慢的问题。

       ```ts
       aboutToAppear(): void {
         setTimeout(() => {
           let item = undefined;
           // 业务逻辑处理,修改item值
           this.ChildItem = item;
         }, 3000);
       }

       build() {
         Column() {
           List() {
             ForEach(this.ChildItem, (item: string) => {
               Column(){
                 Text(item)
                 // 其他子组件
               }
             })
           }
           .width('100%')
           .height('100%')
         }
         .height('100%')
         .width('100%')
       }
       ```
     + 组件创建在页面开始切换后、页面切换完成之前，如下图所示。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/RGLSVwMPRgGOXC7gszMu5Q/zh-cn_image_0000002658794411.png "点击放大")

       找到组件创建后首次提交渲染数据的Trace点H:MarshRSTransactionData，可看到在页面切换完成之后，组件创建到开始渲染的时间间隔为680ms。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/q9ugpnzaS1Kd6Pfy7bbJoA/zh-cn_image_0000002628555048.png "点击放大")

       分析该过程Trace信息，耗时主要集中在Image组件创建，组件创建时下载网络图片，可知应用设置了同步加载图片（[syncLoad](../harmonyos-references/ts-basic-components-image.md#syncload8)为true）。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/nS6fmYrtQ6q42h-V4-f0pg/zh-cn_image_0000002628395144.png "点击放大")

       网络图片下载耗时，同步加载会等待图片下载完成，导致Image组件创建耗时多，影响到Text组件渲染绘制，引起加载慢问题。

* 应用页面是Web页面：
  1. 使用ArkUI Inspector抓取页面组件树，发现页面内容通过Web组件显示，则可以在右侧输入框中输入content获取网页地址，用电脑端浏览器打开该地址，如果能复现同样现象，则判定为网页问题，可以使用DevTools进一步分析。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/6GE4BdUbQo2hFax4ZWIRCg/zh-cn_image_0000002658914369.png "点击放大")
  2. 使用DevTools性能工具录制页面加载过程，首先排查文字、按钮加载慢是否由网络请求时间较长导致，如下图例中可看到页面中间区域内容加载相较其他内容慢，是在进行网络请求后完成的，而该请求耗时主要集中向服务器发送请求到收到响应阶段，与服务器响应处理效率有关。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/aDhH4x__QcyMzlhGy920dg/zh-cn_image_0000002658794413.png "点击放大")

     如果未看到有明显耗时较多的网络请求，如下图例中页面加载时按钮加载较慢问题，可排查按钮显示之前网页侧代码是否存在计时器触发，即延时任务。如存在计时器触发，则可以通过点击调用树中函数调用右侧链接跳转到网页侧代码，确认是否有延时操作。

     ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/JHx2HBpkSNKoxQf0Oi_HdQ/zh-cn_image_0000002628555050.png)

     如下示例代码可看到网页在加载完成1秒后才显示按钮。

     ```html
     function completeLoading() {
         if (document.readyState == "complete") {
             window.setTimeout(() => {
                 // ...
                 document.getElementById('button_id').style.display = 'block'
             }, 1000)
         }
     }
     ```

## 分析结论

* 使用setTimeout延迟更新状态变量，设置的延迟毫秒数较大，导致内容加载慢。
* 使用Image组件显示网络图片时设置了同步加载，导致内容加载慢。
* 网页网络请求时间较长，应用访问服务器获取资源时，服务器响应处理较慢，导致加载慢。
* 网页加载时对单个文字或按钮设置了延时显示，导致加载慢。

## 修改建议

* 减小调用setTimeout时设置的延迟毫秒数。
* 将Image组件的[syncLoad](../harmonyos-references/ts-basic-components-image.md#syncload8)设置为false或去掉该属性值设置。
* [预解析和预连接优化](../best-practices/bpta-web-develop-optimization.md#section29621418112311)。
* 取消延迟显示或减少延时。
