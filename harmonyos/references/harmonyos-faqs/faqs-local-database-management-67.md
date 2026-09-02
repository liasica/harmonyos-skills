---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-local-database-management-67
title: 如何实现后台定时器
breadcrumb: FAQ > 应用框架开发 > 本地数据和文件 > 本地数据库管理 > 如何实现后台定时器
category: harmonyos-faqs
scraped_at: 2026-09-02T14:54:29+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:c7fddfa6d18f91f4b8c1180a099b2805234b2facbaafa30160c0fb26662a38d0
---

## 问题现象

在页面设置一个定时器，倒计时结束后页面的元素需要发生变化。当倒计时还在进行中的时候销毁页面，如何在下次创建该页面时正确的获取并展示剩余时间（要计算页面销毁期间的时间），如果还有剩余时间就继续进行倒计时。

## 背景知识

用户首选项为应用提供Key-Value键值型的数据处理能力，支持应用持久化轻量级数据，并对其修改和查询。数据存储形式为键值对，键的类型为字符串型，值的存储数据类型包括数字型、字符型、布尔型以及这3种类型的数组类型。详情请参考用户首选项[使用指南](../harmonyos-guides/data-persistence-by-preferences.md)及相关[API](../harmonyos-references/js-apis-data-preferences.md)。

## 解决方案

主要思路是数据持久化，可以将计时器计时的起始时间保存到用户首选项中，然后根据当前时间和起始时间的差值来进行计时，即使进程被杀掉也不影响。

通过[setInterval](../atomic-ascf/apis-timer.md#setinterval)设定一个定时器，定时器内部控制倒计时逻辑，配合[状态管理](../harmonyos-guides/arkts-state-management-v1.md)，实现倒计时效果。

示例demo如下：

```ts
import { preferences } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Index {
  // 使用@State装饰器管理状态，记录动态更新的数值
  @State message: number = 60;
  private timerId: number = 0;

  getPreferences(): preferences.Preferences | null {
    let dataPreferences: preferences.Preferences | null = null;
    let options: preferences.Options = { name: 'myStore' };
    try {
      dataPreferences =
        preferences.getPreferencesSync(this.getUIContext().getHostContext(), options) as preferences.Preferences;
      return dataPreferences;
    } catch (error) {
      console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
    }

    return dataPreferences;
  }

  aboutToAppear(): void {
    this.count();
  }

  count() {
    this.countdown(this.message);
    if (this.timerId === 0 && this.message > 0) {
      this.timerId = setInterval(() => {
        if (this.message > 0) {
          this.message--;
        } else {
          clearInterval(this.timerId);
          this.timerId = 0;
        }
      }, 1000);
    }
  }

  countdown(message: number) {
    let dataPreferences = this.getPreferences();
    if (dataPreferences !== null) {
      try {
        if (dataPreferences.hasSync('startTime')) {
          console.info(`The key startTime is contained:${dataPreferences.getSync('startTime', 600)}`);
        } else {
          // 此处以此键值对不存在时写入数据为例,涉及开始时间和结束时间
          dataPreferences.putSync('startTime', Date.now());
          let endtime: number = dataPreferences.getSync('startTime', Date.now()) as number + message * 1000;
          dataPreferences.putSync('endTime', endtime);
          dataPreferences.flushSync();
        }
      } catch (error) {
        console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
      }
    }
  }

  onPageShow(): void {
    let dataPreferences = this.getPreferences();
    if (dataPreferences !== null) {
      try {
        if (dataPreferences.hasSync('endTime')) {
          let endtime: number = dataPreferences.getSync('endTime', Date.now()) as number;

          // 根据结束时间和当前时间计算出剩余的倒计时时间
          let remainingTime: number =
            Math.floor((endtime - Date.now()) / 1000) > 0 ? Math.floor((endtime - Date.now()) / 1000) : 0;
          try {
            dataPreferences.putSync('remainingTime', remainingTime);
            dataPreferences.flushSync();
          } catch (error) {
            console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
          }
          this.message = remainingTime;
        }
      } catch (error) {
        console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
      }
    }
  }

  onPageHide(): void {
    let dataPreferences = this.getPreferences();
    if (dataPreferences !== null) {
      try {
        dataPreferences.putSync('remainingTime', this.message);
        dataPreferences.flushSync();
      } catch (error) {
        console.error(`ErrorCode: ${(error as BusinessError).code}, Message: ${(error as BusinessError).message}`);
      }
    }
  }

  build() {
    Column() {
      Text(this.message.toString())
        .fontSize(50)
        .fontWeight(FontWeight.Bold)
        .backgroundColor('#FFF0F0F0')
        .margin({
          bottom: 5,
          top: 5,
          right: 5,
          left: 5
        });
      if (this.message === 0) {
        Text('倒计时结束UI');
      }
      Button('复位').onClick(() => {
        let dataPreferences = this.getPreferences();
        if (dataPreferences !== null) {
          dataPreferences.clearSync();
          if (this.message === 0) {
            this.message = 60;
            this.count();
          } else {
            this.message = 60;
          }
        }
      });
    }.width('100%');
  }
}
```

## 常见FAQ

Q：使用putSync()方法保存数据后，退出app重新进入时为什么无法获取到此前保存的数据？

A：使用putSync()方法只是保存数据到缓存的Preferences实例中，并未将Preferences实例的数据存储到持久化文件，导致无法读取数据。需要执行flushSync()方法。
