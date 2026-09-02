---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-25
title: 截屏操作耗时较长，多次截屏操作后出现无响应的现象
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 截屏操作耗时较长，多次截屏操作后出现无响应的现象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:49+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:365ee923271e06392a63b397b38a55fd1f91275e6a7e54df8d273211274d33a7
---

## 问题现象

应用具有截屏分享功能，在稳定性测试时，多次执行截屏功能应用发生AppFreeze错误。

## 背景知识

* 用户在使用应用时，如果出现点击无反应或应用无响应等情况，并且持续时间超过一定限制，就会被定义为应用无响应，详情参考[AppFreeze（应用冻屏）检测](../harmonyos-guides/appfreeze-guidelines.md)。
* AppFreeze日志规格说明可以参考[日志规格](../harmonyos-guides/appfreeze-guidelines.md#日志规格)。
* 应用在检测到用户截屏操作，会弹出分享框提示。实现方式可见[截屏事件监听及分享](../architecture-guides/screenshot_listen-0000002261676460.md)。
* [HiSmartPerf](../AppGallery-connect-Guides/smartperf-tool-0000001873208929.md)：无需ROOT设备，即可准确、高效地采集到应用运行时的CPU、GPU等性能数据，了解应用的性能状况。

## 问题定位

1. 查看AppFreeze日志，应用发生了APP\_INPUT\_BLOCK异常，搜索关键字TID:进程ID(PID)，可以获取应用栈信息。

   堆栈中有takeScreenShot字段，说明应用有对截屏事件做特殊处理。

   ```txt
   EVENTNAME = APP_INPUT_BLOCK
   TIMESTAMP = 2025/05/10-13:32:09:970
   PID = 16610
   UID = 20020195
   TID = 16610
   PACKAGE_NAME = com.hx.example
   PROCESS_NAME = com.hx.example
   eventLog_action = ffrt,t:input,t,cmd:c,cmd:dam,tr,k:SysRqFile,cmd:m
   eventLog_interval = 10
   MSG = 
   Fault time:2025/05/10-13:32:05
   User input does not respond!
   Timestamp:2025-05-10 13:32:06:52
   Tid:16610, Name:com.hx.example
   #00 pc 0000000000f348bc /system/lib64/libskia_canvaskit.z.so(neon::matrix_scale_translate(unsigned long, void**, unsigned long, unsigned long, float vector[4], float vector[4], float vector[4], float vector[4], float vector[4], float vector[4], float vector[4], float vector[4])+24)(41c7e50437de39b1aaa05208f048d2dd)
   #01 pc 0000000000f77a64 /system/lib64/libskia_canvaskit.z.so(neon::start_pipeline(unsigned long, unsigned long, unsigned long, unsigned long, void**)+4496)(41c7e50437de39b1aaa05208f048d2dd)
   #02 pc 00000000011281f4 /system/lib64/libskia_canvaskit.z.so(SkRasterPipelineBlitter::blitRect(int, int, int, int)+712)(41c7e50437de39b1aaa05208f048d2dd)
   #03 pc 0000000000f2e33c /system/lib64/libskia_canvaskit.z.so(SkScan::FillRect(SkRect const&, SkRasterClip const&, SkBlitter*)+140)(41c7e50437de39b1aaa05208f048d2dd)
   #04 pc 0000000000f2d998 /system/lib64/libskia_canvaskit.z.so(SkDraw::drawRect(SkRect const&, SkPaint const&, SkMatrix const*, SkRect const*) const+1160)(41c7e50437de39b1aaa05208f048d2dd)
   #05 pc 0000000000f2cec0 /system/lib64/libskia_canvaskit.z.so(SkDraw::drawBitmap(SkBitmap const&, SkMatrix const&, SkRect const*, SkSamplingOptions const&, SkPaint const&) const+964)(41c7e50437de39b1aaa05208f048d2dd)
   // ...
   #21 at takeScreenShot (entry|@lk/lk_oh_fitness_others|1.0.1|src/main/ets/pageshowaspect/help/ScreenShotHelper.ts:19:1)
   ```
2. 由于稳定性测试中会进行频繁的截屏操作，所以需要排查是否截屏事件过多，执行时间过长导致AppFreeze。
3. 搜索关键字"catcher cmd: hilog -z 1000 -P "，可以看到hilog日志中截屏时间频繁。

   ```txt
   05-10 13:31:46.629 16610 16610 I A03D00/com.hx.example/JSAPP: screenshot happenedundefined
   05-10 13:31:46.630 16610 16610 I A03D00/com.hx.example/JSAPP: screenshot happenedundefined
   05-10 13:31:46.631 16610 16610 I A03D00/com.hx.example/JSAPP: screenshot happenedundefined
   05-10 13:31:49.286 16610 16610 I A03D00/com.hx.example/JSAPP: screenshot happenedundefined
   05-10 13:31:49.287 16610 16610 I A03D00/com.hx.example/JSAPP: screenshot happenedundefined
   05-10 13:31:50.011 16610 16610 I A03D00/com.hx.example/JSAPP: screenshot happenedundefined
   05-10 13:31:50.012 16610 16610 I A03D00/com.hx.example/JSAPP: screenshot happenedundefined
   05-10 13:31:54.765 16610 16610 I A03D00/com.hx.example/JSAPP: screenshot happenedundefined
   05-10 13:31:54.767 16610 16610 I A03D00/com.hx.example/JSAPP: screenshot happenedundefined
   05-10 13:31:55.507 16610 16610 I A03D00/com.hx.example/JSAPP: screenshot happenedundefined
   05-10 13:31:55.509 16610 16610 I A03D00/com.hx.example/JSAPP: screenshot happenedundefined
   ```
4. 使用HiSmartPerf工具抓取该过程的Trace信息，在连续截屏的情况下，单个业务执行时间平均0.85s（见顶部时间轴），累计就导致了主线程阻塞。

   ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/l_mDwIRiTV2yno4Pz6Ji3w/zh-cn_image_0000002628394982.png "点击放大")

## 分析结论

应用监听截屏事件，执行相应业务耗时较长，稳定性测试多次截屏时导致主线程卡死。

## 修改建议

优化耗时，当主线程中遇到一些难以避免的耗时操作时，例如同步网络请求、大文件读写、复杂计算、音频处理、数据传输等，可以从以下角度进行性能优化：

* [避免使用耗时接口](../best-practices/bpta-time-optimization-of-the-main-thread.md#section193673511440)，同一接口的不同使用方式存在性能差异，选择耗时更少，性能更优的接口。
* [使用多线程能力](../best-practices/bpta-time-optimization-of-the-main-thread.md#section32971936174416)，可以使用系统自带的Taskpool多线程能力，将耗时任务交由子线程执行，避免主线程的长时间阻塞。

控制执行次数，当遇到用户高频事件输入时，根据业务场景，可以选择节流、防抖或限制次数的方式进行优化：

* 限制执行次数，通过计数变量限制业务执行次数，例如限制弹窗仅弹出一个。
* 节流，固定时间间隔内只允许触发一次操作，忽略中间频繁触发。
* 防抖，事件停止触发后延迟一段时间再执行操作，仅响应最后一次触发。

  ```ts
  import { window } from '@kit.ArkUI';
  import { BusinessError } from '@kit.BasicServicesKit';

  /**
   * 防抖:在一段时间内函数被多次触发，防抖让函数在一段时间后最终只执行一次
   * 返回的函数不需要传参,直接使用this访问外部数据即可
   * @param fn 传入频繁触发的函数
   * @param delay 延迟时间
   * @returns
   */
  export function debounce(fn: Function, delay: number = 1000) {
    let timer: number;
    return () => {
      clearTimeout(timer);
      timer = setTimeout(() => {
        fn();
      }, delay);
    };
  }

  /**
   * 节流:在规定的时间内，只执行一次
   * @param callBack
   * @param delay
   * @param immediately 是否立即执行
   * @returns
   */
  export function throttle(callBack: Function, delay: number = 1000, immediately: boolean = true) {
    let timer = 0;
    if (immediately) {
      return () => {
        if (Date.now() - timer >= delay) {
          callBack();
          timer = Date.now();
        }
      };
    } else {
      return () => {
        if (timer) {
          return;
        }
        timer = setTimeout(() => {
          callBack();
          timer = 0;
        }, delay);
      };
    }
  }

  @Entry
  @Component
  export struct ScreenShotPage {
    @State remind: string = '未截图';
    private uiContext = this.getUIContext();
    private promptAction = this.uiContext.getPromptAction();
    private customDialogComponentId: number = 0;
    private isShowing = false;
    dfn = debounce(() => {
      this.simulateBlockingOperation();
    });
    tfn = throttle(() => {
      this.simulateBlockingOperation();
    });
    @State count: number = 0;
    @State consoleText: string = '';

    @Builder
    screenShotDialog() {
      Column({ space: 15 }) {
        Text('应用内截图事件弹窗')
          .fontSize(20)
        Button('关闭').onClick(() => {
          try {
            this.promptAction.closeCustomDialog(this.customDialogComponentId);
          } catch (error) {
            console.error(`closeCustomDialog error code is ${error.code}, message is ${error.message}`);
          }
        })
      }.padding(15)
    }

    aboutToAppear(): void {
      window.getLastWindow(this.getUIContext().getHostContext(), (err: BusinessError, data: window.Window) => {
        if (err) {
          console.error(`GetLastWindow failed, error code: ${err.code}, error message: ${err.message}`);
        }
        data.on('screenshot', () => {
          if (data.isFocused()) {
            this.remind = '应用内截图';
            this.screenShotEventFunc();
          } else {
            this.remind = '非应用内截图';
          }
        });
      });
    }

    screenShotEventFunc() {
      if (this.isShowing) {
        return;
      }
      this.promptAction.openCustomDialog({
        builder: () => this.screenShotDialog(),
        onDidDisappear: () => {
          this.isShowing = false;
          console.info('onDidDisappear: screenShotDialog');
        }
      }).then((dialogId: number) => {
        this.customDialogComponentId = dialogId;
        this.isShowing = true;
        console.info('openCustomDialog success');
      }).catch((error: BusinessError) => {
        console.error(`openCustomDialog error code is ${error.code}, message is ${error.message}`);
      });
    }

    // 模拟耗时操作的函数
    simulateBlockingOperation(duration: number = 1000) {
      this.count++;
      this.consoleText += `\n${this.count}.开始执行`;
      const startTime = new Date().getTime();
      while (new Date().getTime() - startTime < duration) {
        // 空循环模拟耗时计算
      }
      this.consoleText += '-结束执行';
    }

    build() {
      Column({ space: 15 }) {
        Column() {
          Text('请多次截屏进行测试')
            .fontSize(20)
          Text(this.remind)
        }

        Button('长耗时任务1s').onClick(() => {
          this.simulateBlockingOperation();
        })
        Button('节流方式执行耗时任务').onClick(() => {
          this.tfn();
        })
        Button('防抖方式执行耗时任务').onClick(() => {
          this.dfn();
        })
        Text(`执行次数:${this.count}`)
        Text(this.consoleText)
      }
      .height('100%')
      .width('100%')
      .margin({ top: 30 })
    }
  }
  ```
