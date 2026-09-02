---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-86
title: 如何检测资源泄漏问题
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > 如何检测资源泄漏问题
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-07-07
content_hash: sha256:8ebb9aa486e626babf68311a028865c8cf289320331c0c9932a863eb07efa063
---

## 问题现象

如何检测应用资源泄漏问题？

## 背景知识

* 资源泄漏主要分为内存泄漏、句柄泄漏、线程泄漏，指句柄、线程或内存等资源在应用运行过程中未被正确释放，导致资源长期占用且无法被其他应用使用。对于每种泄漏，系统会通过周期采样的方式对进程的资源使用情况进行检测，如果资源使用超过阈值，会抓取对应维测并上报泄漏事件。资源泄漏的相关内容可查看[Resource Leak（资源泄漏）检测](../harmonyos-guides/resource-leak-guidelines.md)。
* HiAppEvent是系统为应用开发者提供的事件打点机制，支持记录应用运行过程中的故障、统计、安全和行为事件，帮助开发者定位问题、分析应用运行情况，统计访问量、用户活跃度、操作习惯以及其他影响用户使用产品的关键因素，更多内容可查看[HiAppEvent介绍](../harmonyos-guides/hiappevent-intro.md)。
* [DevEco Profiler](../harmonyos-guides/ide-profiler.md)提供实时监控（Realtime Monitor）能力，提供全方位的设备资源监测，覆盖系统事件、异常报告、CPU占用、内存占用、实时帧率、GPU使用率、能耗以及网络流量消耗等多个维度的数据，能够结合代码进行白盒分析，明确不合理的负载出现位置，帮助识别性能瓶颈，定界问题所在，提高解决问题的效率。

## 解决方案

检测资源泄漏问题的方法如下表所示：

| 阶段 | 内存泄漏 | 句柄泄漏 | 线程泄漏 |
| --- | --- | --- | --- |
| 开发态 | HiDumper、DevEco Profiler、DevEco Testing | DevEco Testing | hdc shell ps命令、DevEco Testing |
| 运行态 | HiAppEvent | HiAppEvent | HiAppEvent |

* 开发态检测：
  1. 有明确的测试场景：执行测试场景相应的测试步骤，通过工具或命令确认应用是否有资源泄漏问题。
     + 内存泄漏：

       方式一：通过hidumper命令查询是否存在内存泄漏。

       1. 打开应用，通过hdc shell "hidumper -s WindowManagerService -a '-a'"获取当前应用的pid，如下图中可以看到pid为7066。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/rWAFjaefT66tTijQeRka4w/zh-cn_image_0000002628395024.png "点击放大")
       2. 输入hdc shell "hidumper --mem [pid]"查看应用的内存信息，在测试过程观察Pss（实际使用物理内存）Total一列的数据，是否存在持续增长未回落的情况。如下图中可以看到应用占用3494411KB的内存，主要为Native堆内存（3439852KB），存在Native堆内存泄漏问题。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/VKrzKRWmScu4wQSbnppQtA/zh-cn_image_0000002658914243.png "点击放大")

       方式二：使用DevEco Profiler检测是否存在内存泄漏问题。

       启动应用，打开DevEco Profiler工具，选取应用后启动[实时监控](../harmonyos-guides/realtime-monitor.md)功能，执行测试步骤，查看Memory泳道应用内存变化情况，当一段时间内存不断上涨无回落或者内存占用增长多（比如达到3GB及以上），则可初步判断应用存在内存泄漏问题。

       ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/PzuZdfcxRJKZsoug_7Hqag/zh-cn_image_0000002658794291.png "点击放大")
     + 线程泄漏：
       1. 打开应用，通过hdc shell "hidumper -s WindowManagerService -a '-a'"获取当前应用的pid，如下图中可以看到pid为7066。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/glVmnTcrSNiUwVXezsIhLA/zh-cn_image_0000002628554930.png "点击放大")
       2. 通过hdc shell ps -T [pid]命令可以查看应用进程的线程信息，通过hdc shell "ps -T [pid] | wc -l"命令可以查看应用进程的线程总数，如下图中可以看到应用进程的线程总数为1619，超出了线程泄漏检测的阈值（700个）。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/IyuOBC2qTOK9i9rutbx4mQ/zh-cn_image_0000002628395030.png "点击放大")
     + 句柄泄漏：

       如检测应用是否存在文件句柄泄漏类问题，可参考文件句柄泄漏类问题检测方法中的[检测步骤](../best-practices/bpta-stability-file-handle-detection.md#section10763954174218)。
  2. 无明确的测试场景：使用DevEco Testing进行[探索测试](../harmonyos-guides/other-test.md#section3638191433115)或[稳定性基础质量测试](../harmonyos-guides/stability-testing.md#section1661194962815)，检测是否存在资源泄漏问题。
* 运行态检测：可以使用HiAppEvent订阅资源泄漏事件，检测资源泄漏问题，相关开发步骤如下。
  1. 新建一个Native C++应用工程，编辑工程中的"entry > src > main > ets > entryability > EntryAbility.ets"文件，在OnCreate函数中订阅资源泄漏事件，示例代码如下：

     ```ts
     addEventWatch() {
       let watcher: hiAppEvent.Watcher = {
         // 自定义观察者名称
         name: 'watcher',
         // 订阅了资源泄漏事件
         appEventFilters: [
           {
             domain: hiAppEvent.domain.OS,
             names: [hiAppEvent.event.RESOURCE_OVERLIMIT]
           }
         ],
         // 实现订阅实时回调函数
         onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
           hilog.info(0x0000, 'testTag', `HiAppEvent onReceive: domain=${domain}`);
           for (const eventGroup of appEventGroups) {
             hilog.info(0x0000, 'testTag', `HiAppEvent eventName=${eventGroup.name}`);
             for (const eventInfo of eventGroup.appEventInfos) {
               // 打印资源泄漏事件的信息
               hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo=${JSON.stringify(eventInfo)}`);
             }
           }
         }
       };
       let configParams: Record<string, hiAppEvent.ParamType> = {
         'js_heap_logtype': 'event', // 仅获取事件
       };
       // 设置资源泄漏事件的自定义配置
       hiAppEvent.setEventConfig(hiAppEvent.event.RESOURCE_OVERLIMIT, configParams);
       hiAppEvent.addWatcher(watcher);
     }
     ```
  2. 构造资源泄漏场景，触发资源泄漏。
     + JS泄漏：
       1. 编辑工程中的"entry > src > main > ets > pages > Index.ets"文件，新增triggerJsLeak函数，在函数中多次创建大数组，添加按钮并在onClick函数中调用triggerJsLeak函数。

          ```ts
          // JS泄漏
          triggerJsLeak() {
            for (let i = 0; i < 100; i++) {
              this.leakedArray.push(new Array(100000).fill(1));
            }
          }
          ```
       2. 启动应用后连续点击按钮多次，应用会闪退，重新打开应用后可以看到如下日志打印，resource\_type字段为js\_heap。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/WaPLO6yST9yDrNSt-pTyiQ/zh-cn_image_0000002658914247.png "点击放大")
     + Pss内存泄漏：
       1. 编辑工程中"entry > src > main > cpp > napi\_init.cpp"文件，新增TriggerPssLeak函数，在函数中启动一个线程去申请内存构造Pss内存泄漏。

          ```cpp
          static void AllocateSize() 
          {
              for (int i = 0; i < 3; i++) {
                  int size = 1181116006; // 大约1.1G字节
                  char *p = (char *) malloc(size);
                  std::fill_n(p, size, 'a');
              }
              OH_LOG_INFO(LOG_APP, "AllocateSize");
          }

          static napi_value TriggerPssLeak(napi_env env, napi_callback_info info)
          {
              size_t argc = 2;
              napi_value args[2] = {nullptr};

              napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);

              std::thread t1(AllocateSize);
              t1.detach();
              return 0;
          }
          ```

          在初始化函数init中增加TriggerPssLeak接口映射。

          ```cpp
          static napi_value Init(napi_env env, napi_value exports)
          {
              napi_property_descriptor desc[] = {
                  { "triggerPssLeak", nullptr, TriggerPssLeak, nullptr, nullptr, nullptr, napi_default, nullptr },
                  { "triggerThreadLeak", nullptr, TriggerThreadLeak, nullptr, nullptr, nullptr, napi_default, nullptr },
              };
              napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
              return exports;
          }
          ```
       2. 在接口声明文件（entry > src > main > cpp > types > libentry > index.d.ts）中添加triggerPssLeak函数导出声明。

          ```ts
          export const triggerThreadLeak:() => void;
          ```
       3. 编辑工程中的"entry > src > main > ets > pages > Index.ets"文件，添加按钮并在onClick函数中调用triggerPssLeak。

          ```ts
          // Pss泄漏
          triggerPssLeak() {
            testNapi.triggerPssLeak();
          }
          ```
       4. 启动应用后点击按钮，使用Profiler的[实时监控](../harmonyos-guides/realtime-monitor.md)功能，通过Memory泳道确认应用当前占用内存3.3GB。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/1XsMpU_OSti8y4jhvDyUzg/zh-cn_image_0000002658794295.png "点击放大")

          等待15到30分钟左右，可以看到有如下日志打印，resource\_type字段为pss\_memory。同一个应用，24小时内至多上报一次资源泄漏事件，测试时可以通过重启设备来实现短时间内二次上报。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/NNjgqZUDS1afBlBa1ttTqg/zh-cn_image_0000002628554932.png "点击放大")
     + Ion泄漏：
       1. 编辑工程中的"entry > src > main > ets > pages > Index.ets"文件，新增triggerIonLeak函数，创建多个像素图来构造Ion泄漏，添加按钮并在onClick函数中调用triggerIonLeak函数。

          ```ts
          // Ion泄漏
          triggerIonLeak() {
            for (let i = 0; i < 4800; i++) {
              let imageSource = image.createImageSource(this.buffer);
              imageSource.createPixelMap().then((pixel: image.PixelMap) => {
                pixel.setMemoryNameSync(`leak_image_${i}`);
                this.leakedPixelMap.push(pixel);
              }).catch((error: BusinessError) => {
                hilog.error(DOMAIN, 'testTag', `create pixel map ${i} failed. code is ${error.code} message is ${error.message}`);
              });
            }
          }
          ```
       2. 启动应用后点击按钮，等待几分钟后可以看到如下日志打印，resource\_type字段为ion\_memory。如果长时间未看到相关日志打印，可以重启手机后重新执行该步骤。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/XP8w20CrRBOhmVu-S6uFng/zh-cn_image_0000002628395032.png "点击放大")
     + 句柄泄漏：
       1. 编辑工程中的"entry > src > main > ets > pages > Index.ets"文件，新增triggerFdLeak函数，打开多个文件来构造句柄泄漏，添加按钮并在onClick函数中调用triggerFdLeak函数。

          ```ts
          // Fd泄漏
          triggerFdLeak() {
            let filesDir = this.getUIContext().getHostContext()?.filesDir ?? '';
            for (let i = 0; i < 32768; i++) {
              let path = filesDir + '/leakFile.txt';
              fileIo.open(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE)
                .then((file: fileIo.File)=> {
                  this.leakedFds.push(file.fd);
                })
                .catch((error: BusinessError) => {
                  hilog.error(DOMAIN, 'testTag', `open ${path} failed. code is ${error.code} message is ${error.message}`);
                });
            }
          }
          ```
       2. 启动应用后点击按钮，等待几分钟后运行hdc shell ls -l /data/log/reliability/resource\_leak/fd\_leak命令查看是否有应用进程的句柄泄漏日志生成（文件名为进程pid\_fd\_leak.txt）。如果有日志生成，将应用退出后重启，可以看到有如下日志打印，resource\_type字段为fd；如果长时间未看到句柄泄漏日志生成，可以重启手机后重新执行该步骤。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/Ucg4n5_URQyQyQubOpXViQ/zh-cn_image_0000002658914249.png "点击放大")
     + 线程泄漏：
       1. 编辑工程中"entry > src > main > cpp > napi\_init.cpp"文件，新增TriggerThreadLeak函数，启动多个线程构造线程泄漏。

          ```cpp
          void* ThreadLeakFun(void*)
          {
              while(1) {
                  std::this_thread::sleep_for(std::chrono::milliseconds(500));
              }
          }

          static napi_value TriggerThreadLeak(napi_env env, napi_callback_info info)
          {
              size_t argc = 2;
              napi_value args[2] = {nullptr};

              napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);

              for(int i = 0; i < 1600; i++) {
                  pthread_t thread;
                  pthread_create(&thread, NULL, ThreadLeakFun, NULL);
              }
              OH_LOG_INFO(LOG_APP, "TriggerThreadLeak");
              return 0;
          }
          ```

          在初始化函数init中增加TriggerThreadLeak接口映射。

          ```cpp
          static napi_value Init(napi_env env, napi_value exports)
          {
              napi_property_descriptor desc[] = {
                  { "triggerPssLeak", nullptr, TriggerPssLeak, nullptr, nullptr, nullptr, napi_default, nullptr },
                  { "triggerThreadLeak", nullptr, TriggerThreadLeak, nullptr, nullptr, nullptr, napi_default, nullptr },
              };
              napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
              return exports;
          }
          ```
       2. 在接口声明文件（entry > src > main > cpp > types > libentry > index.d.ts）中添加triggerThreadLeak函数导出声明。

          ```ts
          export const triggerThreadLeak:() => void;
          ```
       3. 编辑工程中的"entry > src > main > ets > pages > Index.ets"文件，添加按钮并在onClick函数中调用triggerThreadLeak。

          ```ts
          // 线程泄漏
          triggerThreadLeak() {
            testNapi.triggerThreadLeak();
          }
          ```
       4. 启动应用后点击按钮，等待几分钟后可以看到有如下日志打印，resource\_type字段为thread。如果长时间未看到相关日志打印，可以重启手机后重新执行该步骤。

          ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/f84_doRrSwOYOMGstSKqyw/zh-cn_image_0000002658794297.png "点击放大")

完整代码如下：

* EntryAbility.ets文件：

  ```ts
  import { ConfigurationConstant, UIAbility } from '@kit.AbilityKit';
  import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
  import { window } from '@kit.ArkUI';

  const DOMAIN = 0x0000;

  export default class EntryAbility extends UIAbility {
    onCreate(): void {
      try {
        this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
      } catch (err) {
        hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
      }
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
      this.addEventWatch();
    }

    addEventWatch() {
      let watcher: hiAppEvent.Watcher = {
        // 自定义观察者名称
        name: 'watcher',
        // 订阅了资源泄漏事件
        appEventFilters: [
          {
            domain: hiAppEvent.domain.OS,
            names: [hiAppEvent.event.RESOURCE_OVERLIMIT]
          }
        ],
        // 实现订阅实时回调函数
        onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
          hilog.info(0x0000, 'testTag', `HiAppEvent onReceive: domain=${domain}`);
          for (const eventGroup of appEventGroups) {
            hilog.info(0x0000, 'testTag', `HiAppEvent eventName=${eventGroup.name}`);
            for (const eventInfo of eventGroup.appEventInfos) {
              // 打印资源泄漏事件的信息
              hilog.info(0x0000, 'testTag', `HiAppEvent eventInfo=${JSON.stringify(eventInfo)}`);
            }
          }
        }
      };
      let configParams: Record<string, hiAppEvent.ParamType> = {
        'js_heap_logtype': 'event', // 仅获取事件
      };
      // 设置资源泄漏事件的自定义配置
      hiAppEvent.setEventConfig(hiAppEvent.event.RESOURCE_OVERLIMIT, configParams);
      hiAppEvent.addWatcher(watcher);
    }

    onDestroy(): void {
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
    }

    onWindowStageCreate(windowStage: window.WindowStage): void {
      // Main window is created, set main page for this ability
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

      windowStage.loadContent('pages/Index', (err) => {
        if (err.code) {
          hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
          return;
        }
        hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
        windowStage.getMainWindow().then((win: window.Window) => {
          win.setWindowKeepScreenOn(true);
        });
      });
    }

    onWindowStageDestroy(): void {
      // Main window is destroyed, release UI related resources
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
    }

    onForeground(): void {
      // Ability has brought to foreground
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
    }

    onBackground(): void {
      // Ability has back to background
      hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
    }
  }
  ```
* Index.ets文件：

  ```ts
  import testNapi from 'libentry.so';
  import { image } from '@kit.ImageKit';
  import { BusinessError } from '@kit.BasicServicesKit';
  import { fileIo } from '@kit.CoreFileKit';
  import { hilog } from '@kit.PerformanceAnalysisKit';

  const DOMAIN = 0x0000;

  @Entry
  @Component
  struct Index {
    private buffer?: ArrayBuffer;

    private leakedArray: Array<number[]> = [];

    private leakedPixelMap: Array<image.PixelMap> = [];

    private leakedFds: number[] = [];

    aboutToAppear(): void {
      let resourceManager = this.getUIContext().getHostContext()?.resourceManager;
      if (resourceManager) {
        resourceManager.getMediaByName('background').then((value: Uint8Array) => {
          this.buffer = value.buffer.slice(0);
        });
      }
    }

    // JS泄漏
    triggerJsLeak() {
      for (let i = 0; i < 100; i++) {
        this.leakedArray.push(new Array(100000).fill(1));
      }
    }

    // Pss泄漏
    triggerPssLeak() {
      testNapi.triggerPssLeak();
    }

    // Ion泄漏
    triggerIonLeak() {
      for (let i = 0; i < 4800; i++) {
        let imageSource = image.createImageSource(this.buffer);
        imageSource.createPixelMap().then((pixel: image.PixelMap) => {
          pixel.setMemoryNameSync(`leak_image_${i}`);
          this.leakedPixelMap.push(pixel);
        }).catch((error: BusinessError) => {
          hilog.error(DOMAIN, 'testTag', `create pixel map ${i} failed. code is ${error.code} message is ${error.message}`);
        });
      }
    }

    // Fd泄漏
    triggerFdLeak() {
      let filesDir = this.getUIContext().getHostContext()?.filesDir ?? '';
      for (let i = 0; i < 32768; i++) {
        let path = filesDir + '/leakFile.txt';
        fileIo.open(path, fileIo.OpenMode.CREATE | fileIo.OpenMode.READ_WRITE)
          .then((file: fileIo.File)=> {
            this.leakedFds.push(file.fd);
          })
          .catch((error: BusinessError) => {
            hilog.error(DOMAIN, 'testTag', `open ${path} failed. code is ${error.code} message is ${error.message}`);
          });
      }
    }

    // 线程泄漏
    triggerThreadLeak() {
      testNapi.triggerThreadLeak();
    }

    build() {
      Column() {
        Button('Js Leak')
          .margin({
            top: 20
          })
          .onClick(() => {
            // 点击几下即可触发应用崩溃，然后重启
            this.triggerJsLeak();
          })

        Button('Pss Leak')
          .margin({
            top: 20
          })
          .onClick(() => {
            this.triggerPssLeak();
          })

        Button('Ion Leak')
          .margin({
            top: 20
          })
          .onClick(() => {
            this.triggerIonLeak();
          })

        Button('Fd Leak')
          .margin({
            top: 20
          })
          .onClick(() => {
            // 重启后点击该按钮, 如出现fd_leak泄漏日志后重启应用, 等待一段时间后可触发
            this.triggerFdLeak();
          })

        Button('Thread Leak')
          .margin({
            top: 20
          })
          .onClick(() => {
            // 点击该按钮, 等待一段时间后可触发
            this.triggerThreadLeak();
          })
      }
      .height('100%')
      .width('100%')
    }
  }
  ```
* napi\_init.cpp文件：

  ```cpp
  /*
   * Copyright (c) Huawei Technologies Co., Ltd. 2026-2026. All rights reserved.
   */

  #include "napi/native_api.h"
  #include <cstdlib>
  #include <hilog/log.h>
  #include <thread>

  static void AllocateSize() 
  {
      for (int i = 0; i < 3; i++) {
          int size = 1181116006; // 大约1.1G字节
          char *p = (char *) malloc(size);
          std::fill_n(p, size, 'a');
      }
      OH_LOG_INFO(LOG_APP, "AllocateSize");
  }

  static napi_value TriggerPssLeak(napi_env env, napi_callback_info info)
  {
      size_t argc = 2;
      napi_value args[2] = {nullptr};

      napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);

      std::thread t1(AllocateSize);
      t1.detach();
      return 0;
  }

  void* ThreadLeakFun(void*)
  {
      while(1) {
          std::this_thread::sleep_for(std::chrono::milliseconds(500));
      }
  }

  static napi_value TriggerThreadLeak(napi_env env, napi_callback_info info)
  {
      size_t argc = 2;
      napi_value args[2] = {nullptr};

      napi_get_cb_info(env, info, &argc, args , nullptr, nullptr);

      for(int i = 0; i < 1600; i++) {
          pthread_t thread;
          pthread_create(&thread, NULL, ThreadLeakFun, NULL);
      }
      OH_LOG_INFO(LOG_APP, "TriggerThreadLeak");
      return 0;
  }

  EXTERN_C_START
  static napi_value Init(napi_env env, napi_value exports)
  {
      napi_property_descriptor desc[] = {
          { "triggerPssLeak", nullptr, TriggerPssLeak, nullptr, nullptr, nullptr, napi_default, nullptr },
          { "triggerThreadLeak", nullptr, TriggerThreadLeak, nullptr, nullptr, nullptr, napi_default, nullptr },
      };
      napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
      return exports;
  }
  EXTERN_C_END

  static napi_module demoModule = {
      .nm_version = 1,
      .nm_flags = 0,
      .nm_filename = nullptr,
      .nm_register_func = Init,
      .nm_modname = "entry",
      .nm_priv = ((void*)0),
      .reserved = { 0 },
  };

  extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
  {
      napi_module_register(&demoModule);
  }
  ```
* Index.d.ts文件：

  ```ts
  export const triggerPssLeak: () => void;
  export const triggerThreadLeak:() => void;
  ```
