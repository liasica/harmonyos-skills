---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-33
title: 应用启动时长时间白屏后启动失败
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 应用启动时长时间白屏后启动失败
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:b5c68598c86d951dba420657376abeb06b647ccff7ab0e5f964ef3bbf3f57a87
---

## 问题现象

应用启动加载首页，首页长时间白屏，启动失败。

## 背景知识

1. 应用中的Web组件运行时，系统会为之分配一个“Render Process”进程，用于渲染。参考文档[进程模型](../harmonyos-guides/process-model-stage.md)。
2. WebView是多渲染进程的，当一个Web应用打开多个页面后，每个页面都有一个渲染进程。
3. 在ArkWeb渲染子进程异常退出导致页面卡死后，应用可通过监听[onRenderExited](../harmonyos-references/arkts-basic-components-web-events.md#onrenderexited9)事件来获取具体的退出原因[RenderExitReason](../harmonyos-references/arkts-basic-components-web-e.md#renderexitreason9)，并在异常回调中根据退出的具体原因，执行相应的异常处理。

## 问题定位

1. 查看faultlogger目录，没有和应用相关的appfreeze日志，应用没有发生卡死。
2. 查看hilog日志，由于卡死的界面采用的是Web组件，搜索关键字*应用包名*:Render，ArkWeb渲染子进程的进程id是35580。

   ```shell
   06-27 14:20:09.482 35580     1 I C04501/应用包名:render/cef: [nodict][frame_impl.cc:964] UpdatePixelRatio in render side SetPixelRatio:3
   06-27 14:20:09.483 35580     1 W C04501/应用包名:render/chromium: [nodict][html_document_parser.cc:196] OptimizeParserBudget set enable: 0
   06-27 14:20:09.493 35580     1 I C04501/应用包名:render/chromium: [nodict][scrollable_area.cc:678] ScrollableArea::SetScrollbarOverlayColorTheme scrollbar color is RGB:0x18, 0x24, 0x31
   06-27 14:20:09.493 35580     1 I C04501/应用包名:render/chromium: [nodict][page_scale_constraints.cc:85] FitToContentsWidth: compare the minimum_scale(0.25) and (1086/2940)
   06-27 14:20:09.529 35580     1 W C04501/应用包名:render/chromium: [nodict][render_frame_impl.cc:4039] event_message: content load finished, routing_id: 1, url: ***
   ```
3. 过滤包含关键字ProcMgr的日志，ArkWeb渲染子进程35580在创建2s后就退出了。

   ```shell
   06-27 14:20:09.239   726 34770 I C01707/concurrent_task_service/CONCUR: [ProcMgr] process 35580 create
   06-27 14:20:09.239   726 34770 I C01707/concurrent_task_service/CONCUR: [ProcMgr] auth status 5 for pid 35580, ret = 0
   06-27 14:20:11.519   726 34770 I C01707/concurrent_task_service/CONCUR: [ProcMgr] process 35580 died
   ```
4. 搜索关键字exitReason，ArkWeb渲染子进程35580进程退出的原因是发生了崩溃。

   ```shell
   06-27 14:20:11.570 35454 35454 I C04500/应用包名/chromium: [nodict][child_process_launcher_helper_linux.cc:277] GetTermination known_dead pid: 35580 exitStatus: 139 exitReason: process crashed
   06-27 14:20:11.572 35454 35454 I C04500/应用包名/cef: [nodict][render_widget_host_view_osr.cc:569] ReleaseCompositor
   06-27 14:20:11.572 35454 35454 I C04500/应用包名/cef: [nodict][render_widget_host_view_osr.cc:575] ReleaseCompositor, widget = 1
   06-27 14:20:11.580 35454 35576 I C04500/应用包名/chromium: [nodict][external_begin_frame_source_ohos.cc:98] ExternalBeginFrameSourceOHOS destructor!!!
   06-27 14:20:11.581 35454 35454 I C04500/应用包名/chromium: [nodict][nweb_handler_delegate.cc:1506] NWebHandlerDelegate::OnLargestContentfulPaint
   06-27 14:20:11.581 35454 35454 I C0391B/应用包名/AceWeb: [(100000:100000:scope)] WebDelegate::OnLargestContentfulPaint, web id = 1
   06-27 14:20:11.581 35454 35454 I C04500/应用包名/chromium: [nodict][nweb_handler_delegate.cc:1901] NWebId: 1 render process exit, reason = 2 reason info = process crashed
   ```

## 分析结论

应用渲染子进程发生崩溃后异常退出，导致启动长时间白屏。

## 修改建议

监听[onRenderExited](../harmonyos-references/arkts-basic-components-web-events.md#onrenderexited9)事件来获取具体的退出原因[RenderExitReason](../harmonyos-references/arkts-basic-components-web-e.md#renderexitreason9)，并在异常回调中根据退出的具体原因，执行相应的异常处理。

使用本例前，请先获取网络权限：[ohos.permission.INTERNET](../harmonyos-guides/permissions-for-all.md#ohospermissioninternet)。

```ts
import { webview } from '@kit.ArkWeb';

@Entry
@Component
struct WebComponentPage {
  needReloadWhenVisible: boolean = false; // Web组件不可见时render退出后阻止重新加载页面，在可见时重新加载页面。
  webIsVisible: boolean = false; // 判断Web组件是否可见。
  // 此处是将子进程异常崩溃和其它异常原因做了区分，应用开发者可根据实际业务特点，细化对应异常的处理策略。
  renderReloadMaxForCrashed: number = 5; // 设置因为异常崩溃后重新加载的最大重试次数，应用可根据业务特点，自行设置试错上限。
  renderReloadCountForCrashed: number = 0; // 异常崩溃后重新加载的次数。
  renderReloadMaxForOthers: number = 10; // 设置因为其它异常原因退出的最大重试次数，应用可根据业务特点，自行设置试错上限。
  renderReloadCountForOthers: number = 0; // 其它异常原因退出后重新加载的次数。
  // 创建Web组件。
  controller: webview.WebviewController = new webview.WebviewController();
  // 指定加载的页面，此处替换成正确的URL地址。
  url: string = 'www.example.com';

  build() {
    Column() {
      Web({ src: this.url, controller: this.controller })
        .onVisibleAreaChange([0, 1.0], (isVisible) => {
          this.webIsVisible = isVisible;
          if (isVisible && this.needReloadWhenVisible) { // Web组件可见时重新加载页面。
            this.needReloadWhenVisible = false;
            this.controller.loadUrl(this.url);
          }
        })
        .fileAccess(false)
        .geolocationAccess(false)
        .backgroundColor(Color.Gray)
        // 应用监听渲染子进程异常退出回调，并进行异常处理。
        .onRenderExited((event) => {
          if (!event) {
            return;
          }
          if (event.renderExitReason === RenderExitReason.ProcessCrashed) {
            if (this.renderReloadCountForCrashed >= this.renderReloadMaxForCrashed) {
              // 设置重试次数上限保护，避免必现问题导致页面被循环加载。
              return;
            }
            console.info(`renderReloadCountForCrashed: ${this.renderReloadCountForCrashed}`);
            this.renderReloadCountForCrashed++;
          } else {
            if (this.renderReloadCountForOthers >= this.renderReloadMaxForOthers) {
              // 设置重试次数上限保护，避免必现问题导致页面被循环加载。
              return;
            }
            console.info(`renderReloadCountForOthers: ${this.renderReloadCountForOthers}`);
            this.renderReloadCountForOthers++;
          }
          if (this.webIsVisible) {
            // Web组件可见则立即重新加载。
            this.controller.loadUrl(this.url);
            return;
          }
          // Web组件不可见时不立即重新加载。
          this.needReloadWhenVisible = true;
        })
    }
  }
}
```
