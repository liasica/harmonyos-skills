---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-172
title: HarmonyOS系统实现异步锁的trylock
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > HarmonyOS系统实现异步锁的trylock
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:54+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:7ec74bfca8ed18b2304f1983584f5b6d7b9a112aa4ff38edf687cab5cee64444
---

## 问题现象

业务的多线程任务希望使用trylock机制，当已经有其他线程持有锁时放弃当前任务，HarmonyOS提供的异步锁如何实现trylock？

## 背景知识

为了解决多并发实例间的数据竞争问题，ArkTS语言基础库引入了[AsyncLock](../harmonyos-references/arkts-apis-arkts-utils-locks.md#asynclock)能力。异步锁通过[lockAsync](../harmonyos-references/arkts-apis-arkts-utils-locks.md#lockasync)进行锁操作。该方法首先获取锁，然后调用回调，最后释放锁。

[Sendable](../harmonyos-guides/arkts-sendable.md#sendable协议)定义了ArkTS的可共享对象体系及其规格约束。符合Sendable协议的数据（以下简称Sendable数据）可以在ArkTS并发实例间传递。

## 解决方案

通过Sendable在不同线程间传递异步锁及锁上下文，获得锁的子锁信息保存到锁上下文，其他锁判定上下文确定自身是否获取到锁，实现trylock机制。

demo实现参考如下：

```screen
import { ArkTSUtils, taskpool, util } from '@kit.ArkTS';
import systemDateTime from '@ohos.systemDateTime';

@Entry
@ComponentV2
struct Index {
  @Local threadCount: number = 3;
  @Local message: string = '';
  build() {
    RelativeContainer() {
      Column() {
        Row() {
          Text(`线程数: `)
          TextInput()
            .type(InputType.Number)
            .onChange((count) => {
              this.threadCount = Number(count);
            })
            .layoutWeight(1)
          Text(this.message)
            .fontColor(Color.Red)
        }
        .width('80%')
        .margin({ top: 50, bottom: 10 })

        Button('开始测试')
          .onClick(() => {
            if (this.threadCount && this.threadCount > 0 && this.threadCount < 100) {
              doTest(this.threadCount);
            } else {
              this.message = '线程数必须大于0小于100';
            }
          })
          .margin({ bottom: 10 })
      }
      .width('100%')
      .alignItems(HorizontalAlign.Center)
      .justifyContent(FlexAlign.Center)
    }
    .height('100%')
    .width('100%')
  }
}

@Concurrent
function lockProcess(name: string, lock: locks.Lock) {
  lock.tryLock().then(result => {
    console.info(`线程${name}获取锁结果：${result}`);
  });
}

function doTest(count: number): void {
  let group = new taskpool.TaskGroup();
  let lock = new locks.ReentrantLock();
  for (let i = 0; i < count; i++) {
    group.addTask(lockProcess, `thread-${i}`, lock.getLock());
  }
  taskpool.execute(group);
}

export namespace locks {
  /**
   * 可重入锁，生成子锁供不同线程使用
   */
  export class ReentrantLock {
    private sysLock: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock();
    private context: LockContext;

    /**
     *
     * @param timeOutMs 锁超时时间，超过时间自动释放 <=0时锁不超时
     */
    constructor(timeOutMs?: number) {
      this.context = new LockContext(timeOutMs);
    }

    // 获取单个线程使用的子锁
    getLock(): Lock {
      return new Lock(this.sysLock, this.context, util.generateRandomUUID());
    }
  }

  /**
   * 公共的锁上下文
   */
  @Sendable
  class LockContext {
    private lockTime: number = systemDateTime.getTime();
    private lockUuid?: string;
    // 默认10s超时
    private timeOutMs: number = 10 * 1000;

    constructor(timeOutMs?: number) {
      if (timeOutMs !== undefined) {
        this.timeOutMs = timeOutMs;
      }
    }

    updateLockUuid(uuid: string) {
      this.lockUuid = uuid;
      this.lockTime = systemDateTime.getTime();
    }

    clearLockUuid() {
      this.lockUuid = undefined;
    }

    isReentrant(uuid: string) {
      return this.lockUuid === uuid;
    }

    isLocked() {
      return this.lockUuid && !this.lockTimeout();
    }

    lockTimeout() {
      if (this.timeOutMs <= 0) {
        return false;
      }
      let now = systemDateTime.getTime();
      return now - this.lockTime > this.timeOutMs;
    }
  }

  @Sendable
  export class Lock {
    private sysLock: ArkTSUtils.locks.AsyncLock;
    private context: LockContext;
    private uuid: string;

    constructor(sysLock: ArkTSUtils.locks.AsyncLock, context: LockContext, uuid: string) {
      this.sysLock = sysLock;
      this.context = context;
      this.uuid = uuid;
    }

    /**
     * 尝试上锁，上锁失败失败返回false
     * @returns
     */
    async tryLock(): Promise<boolean> {
      if (this.context.isReentrant(this.uuid)) {
        return true;
      }
      if (!this.context.isLocked()) {
        await this.sysLock.lockAsync(() => {
          if (!this.context.isLocked()) {
            this.context.updateLockUuid(this.uuid);
          }
        });
      }
      return this.context.isReentrant(this.uuid);
    }

    /**
     * 解锁，未获取到锁时直接返回
     * @returns
     */
    async unlock(): Promise<void> {
      if (!this.context.isLocked()) {
        return;
      }
      if (this.context.isReentrant(this.uuid)) {
        await this.sysLock.lockAsync(() => {
          if (this.context.isReentrant(this.uuid)) {
            this.context.clearLockUuid();
          }
        });
      }
    }
  }
}
```
