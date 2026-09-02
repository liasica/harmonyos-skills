---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-sensor-service-7
title: 如何实现接近身体自动灭屏的功能
breadcrumb: FAQ > 系统开发 > 硬件 > 传感器（Sensor Service） > 如何实现接近身体自动灭屏的功能
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:40+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:241582f79a2fcfa74613b288a9cc333d4c004544efef772b1f0f56060d74f23b
---

## 问题现象

在接听电话的时候，手机靠近身体，为了避免误触，需要将手机灭屏，怎么实现？

## 背景知识

* [RunningLock锁](../harmonyos-references/js-apis-runninglock.md)：运行锁，能够阻止CPU进入低功耗状态，保证业务能够在系统待机状态下继续活动的一种锁机制。
* [RunningLockType.PROXIMITY\_SCREEN\_CONTROL](../harmonyos-references/js-apis-runninglock.md#runninglocktype)：接近光锁，使能接近光传感器，并根据传感器与障碍物的距离远近发起亮灭屏流程。
* [RunningLock.create](../harmonyos-references/js-apis-runninglock.md#runninglockcreate9)：创建RunningLock锁。

## 解决方案

利用光传感器去判断手机与障碍物的距离，并依据与障碍物的距离发起亮灭屏的流程。

* 实现过程：
  1. src/main/module.json5文件配置RunningLock权限。

     ```screen
     {
       "name": "ohos.permission.RUNNING_LOCK"
     }
     ```
  2. 创建一个接近光锁。

     ```screen
     runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL)
       .then((lock: runningLock.RunningLock) => {
         this.runLock = lock;
         this.runLock.hold(-1);
       })
       .catch((err: Error) => {
         console.error(`create running lock failed, err: ${err}`);
       });
     ```

* 完整示例参考如下：

  ```screen
  import { runningLock } from '@kit.BasicServicesKit';

  @Entry
  @Component
  struct RunningLockDemo {
    message: string = '接近光锁';
    private runLock: runningLock.RunningLock | null = null;

    build() {
      Column() {
        Text(this.message)
          .maxLines(10)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .alignRules({
            center: { anchor: '__container__', align: VerticalAlign.Center },
            middle: { anchor: '__container__', align: HorizontalAlign.Center }
          });
        Button('启用RunningLock').onClick(() => {
          this.runningLock();
        });
      }
      .height('100%')
      .width('100%');
    }

    runningLock() {
      runningLock.create('running_lock_test', runningLock.RunningLockType.PROXIMITY_SCREEN_CONTROL)
        .then((lock: runningLock.RunningLock) => {
          this.runLock = lock;
          this.runLock.hold(-1);
        })
        .catch((err: Error) => {
          console.error(`create running lock failed, err: ${err}`);
        });
    }
  }
  ```
