---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkts-184
title: 基于动态时间补偿实现自定义定时器
breadcrumb: FAQ > 应用框架开发 > ArkTS语言 > 方舟编程语言（ArkTS） > 基于动态时间补偿实现自定义定时器
category: harmonyos-faqs
scraped_at: 2026-09-02T15:03:31+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:6027adcf2670b65a034b549b68782255b74f01bdd320278547fd3c133851768a
---

## 问题现象

HarmonyOS中Timer(定时器)，并不是按照设定时间严格执行，每次都会有很小误差，在累计起来可能会有几秒的误差，如何规避。

## 背景知识

[setTimeout](../harmonyos-references/js-apis-timer.md#settimeout)：设置一个定时器，该定时器在定时器到期后执行一个函数。

**说明** 

* 该计时器非精准计时器，实际延迟可能会与预期延迟存在误差。
* 如果值小于1，会被默认取0。
* delay值受系统限制，超出2^32-1时会溢出，delay值为0。

## 解决方案

1. 时间补偿算法：通过start+time\*count-current动态计算下次执行延迟。

   ```ts
   async function myInterval(callback: () => void, time: number) {
     let start: number = Date.now();
     let count: number = 1;
     let current: number = start;
     while (true) {
       await sleep(start + time * count - current);
       current = Date.now();
       count++;
       callback();
     }
   }
   ```
2. 异步控制流：利用sleep()的Promise机制实现非阻塞等待。

   ```ts
   async function sleep(time: number) {
     return await new Promise<void>(resolve => setTimeout(resolve, time));
   }
   ```
3. 误差控制：每次回调后更新当前时间戳，重置计时基准。完整代码如下：

   ```ts
   async function sleep(time: number) {
     return await new Promise<void>(resolve => setTimeout(resolve, time));
   }

   async function myInterval(callback: () => void, time: number) {
     let start: number = Date.now();
     let count: number = 1;
     let current: number = start;
     while (true) {
       await sleep(start + time * count - current);
       current = Date.now();
       count++;
       callback();
     }
   }

   @Entry
   @Component
   struct Page1 {
     @State num: number = 0;

     build() {
       Column({ space: 30 }) {
         Text(`计时 : ${this.num}`)
           .fontSize(30);
         Button('计时开始')
           .onClick(() => {
             let start = Date.now();
             let count: number = 1;
             myInterval(() => {
               console.info('计时', new Date(Date.now() - start).getSeconds(), count++);
               this.num = new Date(Date.now() - start).getSeconds();
             }, 1000);
           });
       }
       .justifyContent(FlexAlign.Center)
       .height('100%')
       .width('100%');
     }
   }
   ```
