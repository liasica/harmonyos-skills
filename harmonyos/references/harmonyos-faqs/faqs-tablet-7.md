---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-tablet-7
title: 平板分屏状态下，点击跳转后的页面变为全屏展示
breadcrumb: FAQ > 多设备场景 > 平板 > 常见问题 > 平板分屏状态下，点击跳转后的页面变为全屏展示
category: harmonyos-faqs
scraped_at: 2026-09-02T14:53:48+08:00
doc_updated_at: 2026-06-26
content_hash: sha256:df57998e4f2afcaee0234e56635fa1bd76ba26e449e4ad78284d3adbbe2caf6e
---

## 问题现象

应用在平板上打开，开启分屏模式后，点击页面内容跳转后，页面切换为全屏显示。

## 背景知识

[UIAbility组件启动模式](../harmonyos-guides/uiability-launch-type.md)：UIAbility的启动模式是指UIAbility实例在启动时的不同呈现状态。针对不同的业务场景，系统提供了三种启动模式：singleton（单实例模式）、multiton（多实例模式）、specified（指定实例模式）。

## 问题定位

1. 从设备底部上滑，查看系统后台任务列表，发现跳转页面后，后台存在两个UIAbility实例。
2. 请检查代码中module.json5配置文件的launchType字段配置，当设置为multiton时即为多实例模式，此时每次调用startAbility()方法时，都会在应用进程中创建一个新的该类型UIAbility实例。

   ```json
   {
     "module": {
       "abilities": [
         {
           "launchType": "multiton", // 表示使用的多实例模式，即在最近任务列表中可以看到有多个该类型的UIAbility实例。
         }
       ]
     }
   }
   ```
3. 检查代码中是否使用startAbility()方法唤起新页面，多实例模式下唤起的新页面不会继承已经分屏的实例窗口显示模式。

   ```ts
   import { UIAbility, Want } from '@kit.AbilityKit';
   import { BusinessError } from '@kit.BasicServicesKit';

   export default class EntryAbility extends UIAbility {
     onForeground() {
       let want: Want = {
         bundleName: 'com.example.myapplication',
         abilityName: 'EntryAbility'
       };

       try {
         this.context.startAbility(want, (err: BusinessError) => { // 通过startAbility唤起新的UIAbility实例
           if (err.code) {
             // 处理业务逻辑错误
             console.error(`startAbility failed, code is ${err.code}, message is ${err.message}`);
             return;
           }
           // 执行正常业务
           console.info('startAbility succeed');
         });
       } catch (err) {
         // 处理入参错误异常
         let code = (err as BusinessError).code;
         let message = (err as BusinessError).message;
         console.error(`startAbility failed, code is ${code}, message is ${message}`);
       }
     }
   }
   ```

## 分析结论

应用采用multiton多实例模式，且使用startAbility()方法打开新页面，此时不会保持原始窗口的分屏状态，导致新打开的页面呈现全屏状态。

## 修改建议

修改module.json5配置文件中的launchType字段配置值，设置为singleton单实例模式。
