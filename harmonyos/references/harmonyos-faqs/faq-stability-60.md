---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faq-stability-60
title: HiAppEvent获取的日志过长无法传输
breadcrumb: FAQ > 应用质量 > 技术质量 > 稳定性 > HiAppEvent获取的日志过长无法传输
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:50+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:8904c83aea9074814a6baef8ba6ebfa7a6b2f7753cc4b76e4e6642e7ce2d3435
---

## 问题现象

使用HiAppEvent监听卡死的异常，获取的故障文件里面会把控制台的所有日志都输出，这样会造成大量冗余日志，经应用测试，整个报文大概在90万字，超出了后台的最大字符限制，如何不使用文件传输的方式，使用普通请求将报错日志传送给后台。

## 背景知识

[HiAppEvent](../harmonyos-guides/hiappevent-intro.md)是在系统层面为应用开发者提供的一种事件打点机制，帮助应用记录在运行过程中发生的故障信息、统计信息、安全信息、用户行为信息，支撑开发者分析应用的运行情况。以便进一步统计分析访问数、日常用户活跃数量、用户操作习惯以及其他影响用户使用产品的关键因素。

## 解决方案

可以设置最大单次传输的数据大小为maxBufferLength，在HiAppEvent回调中获取到故障日志文件路径后，创建一个长度不超过maxBufferLength的ArrayBuffer，使用fs将故障日志文件读取到ArrayBuffer中再发送网络请求。

```ts
import { AbilityConstant, ConfigurationConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';
import { hiAppEvent, hilog } from '@kit.PerformanceAnalysisKit';
import { fileIo as fs } from '@kit.CoreFileKit';
const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      this.context.getApplicationContext().setColorMode(ConfigurationConstant.ColorMode.COLOR_MODE_NOT_SET);
    } catch (err) {
      hilog.error(DOMAIN, 'testTag', 'Failed to set colorMode. Cause: %{public}s', JSON.stringify(err));
    }
    hilog.info(DOMAIN, 'testTag', want.toString());
    hilog.info(DOMAIN, 'testTag', launchParam.toString());
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');

    hiAppEvent.addWatcher({
      name: "watcher",
      appEventFilters: [
        {
          domain: hiAppEvent.domain.OS,
          names: [hiAppEvent.event.APP_FREEZE, hiAppEvent.event.APP_CRASH]
        }
      ],
      onReceive: (domain: string, appEventGroups: Array<hiAppEvent.AppEventGroup>) => {
        hilog.info(0x0000, 'testTag', `HiAppEvent onReceive: domain=${domain}`);
        for (const eventGroup of appEventGroups) {
          hilog.info(0x0000, 'testTag', `HiAppEvent eventName=${eventGroup.name}`);
          for (const eventInfo of eventGroup.appEventInfos) {
            let logPath: string = eventInfo.params['external_log'][0]; // 获取首个日志文件路径
            let accessible = fs.accessSync(logPath);
            if (accessible) {
              let maxBufferLength = 4096;
              let file = fs.openSync(logPath, fs.OpenMode.READ_ONLY);
              try {
                let stat = fs.statSync(logPath); // 获取文件信息
                let bufferLength = Math.min(stat.size, maxBufferLength);// 限制要发送的数据大小
                let buf = new ArrayBuffer(bufferLength); // 创建缓冲区
                fs.readSync(file.fd, buf); // 读取内容到缓冲区
                // sendByHttps() 自行实现将数据异步发送给后台
              } finally {
                fs.closeSync(file); // 关闭文件

              }
            }
          }
        }
      }
    });
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

## 常见FAQ

Q：订阅崩溃事件hiAppEvent.addWatcher中onReceive回调在应用里能正常执行，在元服务里不执行。

A：API18之后可以实现在元服务里执行hiAppEvent.addWatcher中onReceive回调，API18版本之前不支持在元服务实现该事件。

Q：订阅应用终止事件，如果有资源泄漏导致的崩溃，如内存，句柄，线程泄漏导致的崩溃，会被应用终止事件监听到吗？

A：不会，终止事件是指应用程序被系统强制退出的情况，而崩溃主要是应用自身代码异常的情况，两种情况虽然都可以通过HiAppEvent订阅，但却是不同的订阅方式，详细参考：[订阅崩溃事件](../harmonyos-guides/hiappevent-watcher-crash-events-arkts.md)、[订阅终止事件](../harmonyos-guides/hiappevent-watcher-app-killed-events-arkts.md)。

Q：扩展进程的崩溃，能否在APP进程通过注册HiAppEvent的APP\_CRASH事件监听到？

A：关于HiAppEvent对于扩展进程崩溃事件的订阅，只要在同一个应用内，A、B两个进程，进程A已调用addWatcher()接口订阅崩溃事件。如果进程B发生崩溃，进程A也能收到进程B的崩溃回调。只要进程A和B的应用名一致即可。

Q：AGC下的APMS异常管理与HiAppEvent崩溃订阅是否冲突？

A：APMS采集现网应用崩溃信息，与HiAppEvent不冲突。
