---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-23
title: 应用导入大量图片后卡死
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用导入大量图片后卡死
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:2d8092277e285b773e3c510d2afbab60863acf0c81d6dc9f5187fb5928f61f4f
---

## 问题现象

应用在导入大量图片后，页面卡死无响应。

## 背景知识

* 应用中的Web组件运行时，系统会为之分配一个Render进程，用于渲染。如图中的“Render Process”。参考文档[进程模型](../harmonyos-guides/process-model-stage.md)。![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/h9_AlIZHR6aXomgwEFgvPg/zh-cn_image_0000002658794245.png "点击放大")
* WebView是多渲染进程的，当一个Web应用打开多个页面后，每个页面都有一个渲染进程。

## 问题定位

1. 查看faultlogger目录，没有appfreeze日志，说明应用没有发生卡死。
2. 查看hilog日志，观察到chromium字段，说明界面采用的是Web组件，搜索关键字com.hx.example:render，可以看到应用渲染进程id是15400。

   ```txt
   06-23 15:01:15.076 15400 15400 W C04501/com.hx.example:render/chromium: [nodict][render_frame_impl.cc:4038] event_message: content load finished, routing_id: 1, url: ***
   06-23 15:01:15.086 15400 15400 W C04501/com.hx.example:render/chromium: [nodict][render_frame_impl.cc:4081] event_message: page load finished, routing_id: 1, url: ***
   06-23 15:01:15.404 15400 15400 I C04501/com.hx.example:render/chromium: [nodict][paint_timing.cc:134] event_message: MarkFirstContentfulPaint
   06-23 15:01:15.527 15400 15400 I C04501/com.hx.example:render/chromium: [nodict][frame_selection.cc:949] Focused Or Active State Changed, focused=0, active_and_focused=0
   ```
3. 搜索关键字ProcMgr，可以看到应用渲染进程15400在15:06:13已经终止，和页面发生卡死的时间一致。

   ```txt
   06-23 15:06:13.095   850 26512 I C02699/memmgrservice/MemMgr: PrioManager::UpdatePriorityLocked pid=15400, bundleUid=20020161, bundleName=com.hx.example, procName=com.hx.example, time=1750662373087500000, reason=PROCESS_TERMINATED
   06-23 15:06:13.095  1375  1447 I C05A02/privacy_service/PermissionRecordManager: [RemoveRecordFromStartListByPid:913]TokenId 0, pid 15400
   06-23 15:06:13.095  1375  6430 I C05A02/privacy_service/PrivacySecCompEnhanceAgent: [OnProcessDied:37]OnProcessDied pid 15400
   06-23 15:06:13.095  1375  6430 E C05A02/privacy_service/PrivacySecCompEnhanceAgent: [RemoveSecCompEnhance:112]Not found pid 15400 data.
   06-23 15:06:13.096   850 26512 E C02699/memmgrservice/MemMgr: PrioManager::UpdatePriorityLocked reason=PROCESS_TERMINATED, res: proc[pid=15400] is not exist
   06-23 15:06:13.096   789   789 I C01707/concurrent_task_service/CONCUR: [ProcMgr] process 15400 died
   ```
4. 搜索关键字EXIT\_REASON\_TAG，查看进程退出的原因，可以看到渲染进程退出的原因是应用内存超限（App Memory Deterioration）。

   ```txt
   06-23 15:06:13.113   652 26493 I C02DA0/hiview/FaultLeakDetectorManager: NotifyProcessDied: NotifyProcessDied process:com.hx.example:15400
   06-23 15:06:13.113  2412 25117 I C01560/wifi_manager_service/OHWIFI_HANDLER: StaStateMachine ExecuteMessage msg:2
   06-23 15:06:13.115   652  2724 I C01336/hiview/AMS: [ability_manager_client.cpp:1607][EXIT_REASON_TAG] pid:1, reason:7, exitMsg: App Memory Deterioration
   06-23 15:06:13.119  1510  2540 I C01336/foundation/AMS: [ability_manager_service.cpp:2406][EXIT_REASON_TAG] pid:1, reason:7, exitMsg:App Memory Deterioration
   ```

## 分析结论

应用内存超限导致渲染进程异常终止，从而使页面发生了卡死。

## 修改建议

监听[onRenderExited](../harmonyos-references/arkts-basic-components-web-events.md#onrenderexited9)事件来获取具体的退出原因[RenderExitReason](../harmonyos-references/arkts-basic-components-web-e.md#renderexitreason9)，并在异常回调中根据退出的具体原因，执行相应的异常处理。

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponent {
  needReloadWhenVisible: boolean = false; // Web组件不可见时render退出后阻止重新加载页面，在可见时重新加载页面。
  webIsVisible: boolean = false; // 判断Web组件是否可见。
  // 此处是将子进程异常崩溃和其它异常原因做了区分，应用开发者可根据实际业务特点，细化对应异常的处理策略。
  renderReloadMaxForCrashed: number = 5; // 设置因为异常崩溃后重新加载的最大重试次数，应用可根据业务特点，自行设置试错上限。
  renderReloadCountForCrashed: number = 0; // 异常崩溃后重新加载的次数。
  renderReloadMaxForOthers: number = 10; // 设置因为其它异常原因退出的最大重试次数，应用可根据业务特点，自行设置试错上限。
  renderReloadCountForOthers: number = 0; // 其它异常原因退出后重新加载的次数。
  // 创建Web组件。
  controller: webview.WebviewController = new webview.WebviewController();
  // 指定加载的页面。
  url: string = 'xx.xx.xx';

  build() {
    Column() {
      Web({ src: this.url, controller: this.controller })
        .fileAccess(false)
        .geolocationAccess(false)
        .onVisibleAreaChange([0, 1.0], (isVisible) => {
          this.webIsVisible = isVisible;
          if (isVisible && this.needReloadWhenVisible) { // Web组件可见时重新加载页面。
            this.needReloadWhenVisible = false;
            this.controller.loadUrl(this.url);
          }
        })
        // 应用监听渲染子进程异常退出回调，并进行异常处理。
        .onRenderExited((event) => {
          if (!event) {
            return;
          }
          if (event.renderExitReason == RenderExitReason.ProcessCrashed) {
            if (this.renderReloadCountForCrashed >= this.renderReloadMaxForCrashed) {
              // 设置重试次数上限保护，避免必现问题导致页面被循环加载。
              return;
            }
            console.log('renderReloadCountForCrashed: ' + this.renderReloadCountForCrashed);
            this.renderReloadCountForCrashed++;
          } else {
            if (this.renderReloadCountForOthers >= this.renderReloadMaxForOthers) {
              // 设置重试次数上限保护，避免必现问题导致页面被循环加载。
              return;
            }
            console.log('renderReloadCountForOthers: ' + this.renderReloadCountForOthers);
            this.renderReloadCountForOthers++;
          }
          if (this.webIsVisible) {
            // Web组件可见则立即重新加载。
            this.controller.loadUrl(this.url);
            return;
          }
          // Web组件不可见时不立即重新加载。
          this.needReloadWhenVisible = true;
        });
    };
  }
}
```
