---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-threading-model-4
title: TaskPool多线程如何共享对象
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > ArkTS线程模型和并发 > TaskPool多线程如何共享对象
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:fff4f7b81200b015a1a7a6d8d124b6001d13a83da82f6c950ea1c396b2982280
---

## 问题现象

根据官方文档的描述，TaskPool内存是完全独立的，例如有一个后台任务需要执行数据库操作和网络请求功能，如果多次调用TaskPool执行后台任务是否意味着每次都需要初始化数据库和网络请求工具类？有什么方法可以在线程间共享工具类初始化的数据？

## 效果预览

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/GDPIeOe0QNeDrr6bax2PBA/zh-cn_image_0000002629058994.png "点击放大")

## 背景知识

* [共享模块](../harmonyos-guides/arkts-sendable-module.md)是进程内只会加载一次的模块，使用“use shared“这一指令来标记一个模块是否为共享模块。
* [Sendable](../harmonyos-guides/arkts-sendable.md)对象为可共享的，其跨线程前后指向同一个JS对象，如果其包含了JS或者Native内容，均可以直接共享，如果底层是Native实现的，则需要考虑线程安全性。

## 解决方案

可以使用共享模块内导出Sendable对象来实现进程单例，从而达到线程间共享对象。

* SharedModule.ets共享对象定义文件。

  ```ts
  // 共享模块sharedModule.ets
  import { ArkTSUtils } from '@kit.ArkTS';

  // 声明当前模块为共享模块，只能导出可Sendable数据
  'use shared';

  // 共享模块，SingletonA全局唯一
  @Sendable
  class SingletonA {
    private count_: number = 0;
    lock_: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock();

    public async getCount(): Promise<number> {
      return this.lock_.lockAsync(() => {
        return this.count_;
      });
    }

    public async increaseCount() {
      // 异步锁中自增count
      await this.lock_.lockAsync(() => {
        this.count_++;
      });
    }
  }

  // 导出单例共享对象
  export const singletonA = new SingletonA();
  ```
* TaskToolSharedPage.ets主线程和线程池访问共享对象页面。

  ```ts
  import { taskpool } from '@kit.ArkTS';
  import { singletonA } from './SharedModule';

  @Concurrent
  async function increaseCount() {
    await singletonA.increaseCount();
    let count:number = await singletonA.getCount();
    console.info(`SharedModule: count is: ${count}`);
  }

  @Concurrent
  async function printCount() {
    let count:number = await singletonA.getCount();
    console.info(`SharedModule: count is: ${count}`);
  }

  @Entry
  @Component
  struct TaskToolSharedPage {

    build() {
      Row() {
        Column() {
          Button('MainThread print count')
            .onClick(async () => {
              try {
                await printCount();
              } catch (err) {
                console.error(`MainThread print count.errCode is ${err.code}, message is ${err.message}`);
              }
            })
            .margin({top:20});
          Button('Taskpool print count')
            .onClick(async () => {
              try {
                await taskpool.execute(printCount);
              } catch (err) {
                console.error(`Taskpool print count.errCode is ${err.code}, message is ${err.message}`);
              }
            })
            .margin({top:20});
          Button('MainThread increase count')
            .onClick(async () => {
              try {
                await increaseCount();
                let count:number = await singletonA.getCount();
                console.info(`MainThread SharedModule: count is: ${count}`);
              } catch (err) {
                console.error(`MainThread increase count.errCode is ${err.code}, message is ${err.message}`);
              }
            })
            .margin({top:20});
          Button('Taskpool increase count')
            .onClick(async () => {
              try {
                await taskpool.execute(increaseCount);
                let count:number = await singletonA.getCount();
                console.info(`Taskpool SharedModule: count is: ${count}`);
              } catch (err) {
                console.error(`Taskpool increase count.errCode is ${err.code}, message is ${err.message}`);
              }
            })
            .margin({top:20});
        }
        .width('100%');
      }
      .height('100%');
    }
  }
  ```

  ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/n9833oiRTD-jfV77EX1gBg/zh-cn_image_0000002628899076.png "点击放大")
