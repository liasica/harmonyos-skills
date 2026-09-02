---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-file-handle-detection
title: 文件句柄泄漏类问题检测方法
breadcrumb: 最佳实践 > 稳定性 > 稳定性检测 > 开发态稳定性检测 > 资源泄漏类问题检测 > 文件句柄泄漏类问题检测方法
category: best-practices
scraped_at: 2026-09-02T15:03:23+08:00
doc_updated_at: 2026-05-18
content_hash: sha256:5648db92245e1d188ddfeeb805ef5a5a1e5ab2bba794f034ae4ac912843e5ae1
---

## 概述

句柄泄漏是指程序在运行过程中获取了系统资源的句柄，但在使用完毕后未能正确释放——这会导致系统资源被长期占用，无法被其他程序或系统本身重新利用。就句柄本身而言，它是进程的私有资源，操作系统会对单个进程的句柄上限做出限制。而句柄指向的实际资源可能是全局性的，整机也会有该资源的使用限制，所以句柄泄漏发生后，可能也会导致整机系统的异常，而不光局限在应用本身。

常见的能生成句柄的系统调用有open、pipe、socket等。

**注意** 

为防止句柄泄漏，请务必记得在使用完fd后，调用close方法进行关闭。

## 实现原理

每个进程打开句柄后，操作系统会在/proc/pid/fd目录下新生成一个链接文件，这个链接文件的名字就是句柄号（进程内唯一的一个数值），通过遍历每个进程下的/proc/pid/fd目录，统计目录下文件个数（进程句柄数），当该进程的句柄数超过系统设置的阈值，则认为是该进程发生了句柄泄漏异常。

## 约束和限制

目前只在开发者选项打开的场景下，检测到句柄泄漏后，才会有泄漏点的栈维测信息，在此前提下，您可以尝试通过HiDebug.setAppResourceLimit来设置更低的fd泄漏阈值，来降低获取维测日志的难度。

在开发者选项关闭的场景下，只有普通维测信息，即包含按照句柄类型聚类后的个数信息，大概能知道是哪种类型的句柄泄漏。

## 检测步骤

如果不知道明确的复现步骤，可以尝试如下方法：

1. 打开“开发者选项”，同时打开它下面的子开关“系统资源泄漏日志”；
2. 在应用中调用HiDebug.setAppResourceLimit设置fd泄漏上限值，默认为5000，如果想快速复现问题，建议设置成2000左右（不建议设置成1000以下，因为系统框架默认会打开很多文件句柄，过小容易导致误报）；
3. 启动[DevEco Testing](https://developer.huawei.com/consumer/cn/deveco-testing/)工具进行稳定性测试，开发者可以选择应用探索测试，如果检测到异常，从工具中能获取到异常日志。

如果知道明确的复现步骤，可以尝试如下方法：

1. 修改应用代码，做一个测试按钮，点击这个按钮枚举下进程的所有句柄。

   ```screen
   import { fileIo, ListFileOptions } from '@kit.CoreFileKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   @Entry
   @Component
   struct Index {
     @State message: string = 'Hello World';

     build() {
       RelativeContainer() {
         Text(this.message)
           .id('HelloWorld')
           .fontSize($r('app.float.page_text_font_size'))
           .fontWeight(FontWeight.Bold)
           .alignRules({
             center: { anchor: '__container__', align: VerticalAlign.Center },
             middle: { anchor: '__container__', align: HorizontalAlign.Center }
           })
           .onClick(() => {
             this.message = 'Welcome';
             let listFileOption:ListFileOptions={};
             listFileOption.recursion = false;
             listFileOption.listNum = 10000;
             fileIo.listFile("/proc/self/fd", listFileOption, (err: BusinessError, fileNames: Array<string>) => {
               if (err) {
                 console.error("list file failed, message:", err.message + ", code:" + err.code);
               } else {
                 console.log("count:", fileNames.length);
                 fileNames.forEach(fileName => {
                   let fd: number = Number(fileName);
                   try {
                     let actName = fileIo.dup(fd);
                     console.info('fd:', fd);
                     console.info('path:', actName.path);
                     fileIo.close(actName);
                   } catch(e) {
                     console.info(e);
                   }
                 });
               }
             });
           })
       }
       .height('100%')
       .width('100%')
     }
   }
   ```
2. 尝试复现问题，然后点击一下上述代码对应的测试按钮，分析日志输出，看多了哪些句柄。如果句柄增加不明显，可以反复重复本步骤。

   **说明** 

   这个演示代码只能打印出应用沙箱目录的文件路径，其他系统路径的文件因为权限问题可能会打印不出来，所以只能定位沙箱目录下文件句柄的泄漏问题。
