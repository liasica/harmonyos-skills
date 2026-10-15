---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-reasonable-system-use
title: 后台系统资源合理使用
breadcrumb: 最佳实践 > 功耗 > 应用功耗优化 > 后台任务低功耗 > 后台软件资源合理使用 > 后台系统资源合理使用
category: best-practices
scraped_at: 2026-10-16T07:06:48+08:00
doc_updated_at: 2026-10-15
content_hash: sha256:1c88d6eaa090cff16327e6fc058ba6cc3afcd58e5dc2b7b247b3e9d15d889805
---

无长时任务的应用退至后台后，应释放对应资源，避免阻止系统休眠。

## 约束

接口runningLock.create的type参数BACKGROUND类型已废弃，不建议使用。如果确实需要使用，后台运行时必须主动释放锁。

## 示例

### 应用直接持锁

```screen
import { runningLock } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Return to the background to release the lock
runningLock.create('running_lock_test', runningLock.RunningLockType.BACKGROUND_USER_IDLE)
  .then((lock: runningLock.RunningLock) => {
    try {
      lock.unhold();
    } catch (error) {
      let err = error as BusinessError;
      hilog.warn(0x0000, 'testTag', `setColorMode failed, code=${err.code}, message=${err.message}`);
    }
  })
  .catch((err: Error) => {
    console.error('create running lock failed, err: ' + err);
  });
```

有关RunningLock开发相关接口的使用，详情可以参考[RunningLock锁](../harmonyos-references/js-apis-runninglock.md)。

### 系统帮助应用持锁

使用音频资源时，系统会为应用持锁。如果不释放音频资源，会导致系统持锁不释放。因此，应用在后台应主动释放音频资源。

可参考[合理使用音频资源](bpta-reasonable-audio-use.md)。

```screen
import { UIAbility } from '@kit.AbilityKit';
import { audio } from '@kit.AudioKit';
import { BusinessError } from '@kit.BasicServicesKit';
// ...
let audioRenderer: audio.AudioRenderer;
// ...
export default class EntryAbility extends UIAbility {
  // ...

  onForeground(): void {
    //Apply for the resources required by the system, or reapply for the resources released in onBackground ()
    audio.createAudioRenderer(audioRendererOptions,(err: BusinessError) => {});
  }

  onBackground(): void {
    //Release resources when the UI is invisible
    audioRenderer.stop((err: BusinessError) => {});
  }
}
```
