---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-app-framework-multi-device-1
title: 三折叠设备未适配，页面出现错乱、重叠、拉伸、截断等异常情况
breadcrumb: FAQ > 应用框架开发 > 一次开发多端部署 > 三折叠设备未适配，页面出现错乱、重叠、拉伸、截断等异常情况
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:34+08:00
doc_updated_at: 2026-08-27
content_hash: sha256:44230f6f8ae29aaaffb66bbd949bb5fb139a5cf00f7c28bdce3fb8de48241e6a
---

## 问题现象

应用在三折叠设备的单屏态（F态）、双屏态（M态）和三屏态（G态）上运行时，会出现内容显示异常的现象。在折叠态切换过程中（如从G态切换到F态），还可能出现布局卡顿现象：一次折叠动作会触发多次[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)和windowModeChange回调，系统过渡动画与应用内布局重算争抢主线程，导致动画帧率明显下降，切换完成后可能出现短暂白屏。

## 背景知识

* [三折叠屏幕规格信息](../best-practices/bpta-matext-guide.md#section6795030182116)：三折叠在单屏态、双屏态和三屏态下的硬件参数。
* [一多断点开发](../best-practices/bpta-multi-device-responsive-layout.md#section1532120147301)：响应式布局中最常使用的特征是窗口宽度及窗口高宽比，可以将窗口宽度及窗口高宽比划分为不同的范围，称之为“断点”。当窗口宽度及窗口高宽比从一个断点变化到另一个断点时，改变页面布局（如将页面内容从单列排布调整为双列排布甚至三列排布等）以获得更好的显示效果。

## 问题定位

* 当应用在折叠屏上布局异常时，建议检查代码中是否已通过[getWindowWidthBreakpoint()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getwindowwidthbreakpoint13)与[getWindowHeightBreakpoint()](../harmonyos-references/arkts-apis-uicontext-uicontext.md#getwindowheightbreakpoint13)获取当前窗口横向断点与纵向断点。
* 检查代码中有没有通过[on('windowSizeChange')](../harmonyos-references/arkts-apis-window-window.md#onwindowsizechange7)方法监听窗口尺寸变化。
* 检查应用有没有在接收到on('windowSizeChange')事件后能够及时更新布局的断点，在页面中，获取并及时使用更新后的断点。
* 检查应用是否通过不同的断点调整布局参数以适应新的屏幕尺寸。
* 检查在折叠态切换过程中，是否对on('windowSizeChange')回调进行了节流处理。一次折叠动作可能触发多次回调，若未节流，频繁的布局重算会与系统过渡动画争抢主线程，引起卡顿。

## 分析结论

应用没有通过getWindowWidthBreakpoint()与getWindowHeightBreakpoint()获取当前窗口横向断点与纵向断点。未通过on('windowSizeChange')方法监听窗口尺寸变化，并在监听回调中重新获取断点，及时更新页面布局，导致页面显示异常。即使已监听on('windowSizeChange')事件，若未对回调进行节流处理，折叠态切换过程中频繁触发的回调会导致布局反复重算，与系统过渡动画争抢主线程，引起卡顿和短暂白屏。

## 修改建议

建议参照官方示例实现[断点触发的UI刷新](../best-practices/bpta-multi-device-responsive-layout.md#section175001836203617)，具体步骤如下：

1. 通过窗口属性获取当前窗口宽度，并根据宽度值计算当前所处的断点区间（如sm、md、lg）。
2. 将断点信息及对应的布局模式保存在状态变量中，当断点变化时触发UI布局的同步刷新。
3. 通过on('windowSizeChange')方法监听窗口尺寸变化，并在监听回调中重新获取断点，以达到窗口尺寸变化依旧有良好的体验。
4. 根据AppStorage中存储的窗口信息，对不同断点区间进行针对性布局。
5. 对on('windowSizeChange')回调进行节流处理，避免折叠过程中频繁触发布局重算。使用setTimeout设置150ms节流间隔，仅取最终稳定的窗口宽度值执行断点更新，仅在断点真正变化时才更新状态变量。三折叠的过渡动画约300ms，150ms节流后只触发1-2次布局重算。示例代码如下：

   ```ts
   import { window } from '@kit.ArkUI';
   import { hilog } from '@kit.PerformanceAnalysisKit';

   const BP_SM_MAX = 600;
   const BP_MD_MAX = 840;
   const RESIZE_THROTTLE_MS = 150;

   @Entry
   @ComponentV2
   struct AdaptivePage {
     @Local breakpoint: 'sm' | 'md' | 'lg' = 'sm';
     @Local navMode: NavigationMode = NavigationMode.Stack;
     private resizeTimer: number = -1;
     private pendingWidth: number = 0;
     private navStack: NavPathStack = new NavPathStack();
     private win?: window.Window;

     aboutToAppear(): void {
       window.getLastWindow(this.getUIContext().getHostContext()).then(w => {
         this.win = w;
         try {
           const prop = w.getWindowProperties();
           this.applyBreakpoint(prop.windowRect.width);
           w.on('windowSizeChange', (data: window.Size) => {
             this.pendingWidth = data.width;
             // 节流：150ms内只执行最后一次
             if (this.resizeTimer !== -1) {
               clearTimeout(this.resizeTimer);
             }
             this.resizeTimer = setTimeout(() => {
               this.applyBreakpoint(this.pendingWidth);
               this.resizeTimer = -1;
             }, RESIZE_THROTTLE_MS);
           });
         } catch (err) {
           hilog.error(0x0000, 'AdaptivePage', `getWindowProperties or on failed: ${err}`);
         }
       })
     }

     aboutToDisappear(): void {
       if (this.win) {
         this.win.off('windowSizeChange');
       }
       if (this.resizeTimer !== -1) {
         clearTimeout(this.resizeTimer);
         this.resizeTimer = -1;
       }
     }

     private applyBreakpoint(width: number): void {
       const newBp = width <= BP_SM_MAX ? 'sm' : width <= BP_MD_MAX ? 'md' : 'lg';
       const newMode = width <= BP_SM_MAX ? NavigationMode.Stack : NavigationMode.Split;
       // 仅在断点真正变化时更新，避免重复渲染
       if (newBp !== this.breakpoint) {
         this.breakpoint = newBp;
       }
       if (newMode !== this.navMode) {
         this.navMode = newMode;
       }
     }

     build() {
       Navigation(this.navStack) {
         GridRow({
           breakpoints: {
             value: ['200vp', '300vp', '400vp', '500vp', '600vp'],
             reference: BreakpointsReference.WindowSize
           }
         }) {
           ForEach(['rgb(39,135,217)'], (color: ResourceColor, index?: number | undefined) => {
             GridCol({
               span: {
                 sm: 4, md: 8, lg: 12
               }
             }) {
               Row() {
                 Text(`${"半屏布局"}`)
                   .fontWeight(FontWeight.Bold)
                   .textAlign(TextAlign.Center)
                   .width("100%")
               }
               .width("100%")
               .height('80vp')
               .justifyContent(FlexAlign.Center)
             }.backgroundColor(color)
           })
         }
       }
       .mode(this.navMode)
     }
   }
   ```
