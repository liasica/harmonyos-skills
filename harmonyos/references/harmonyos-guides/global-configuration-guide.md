---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/global-configuration-guide
title: 全局配置项功能场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > 全局配置项功能场景
category: harmonyos-guides
scraped_at: 2026-09-02T14:49:46+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:c8284e1135478afbdda3fd751763556e690e7c1b6562b9c6868fa973cb6d0709
---

对于需要使用进程单例的场景，例如不同并发实例间需要数据保持一致的全局配置项功能，可以采用[共享模块](arkts-sendable-module.md)来实现。

以下示例展示了只有在Wi-Fi打开且用户登录的情况下才能进行下载的功能，具体步骤如下。

1. 编写全局配置文件。

   ```typescript
   import { ArkTSUtils } from '@kit.ArkTS';

   'use shared'

   @Sendable
   class Config {
     public lock: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock();
     public isLogin: boolean = false;
     public loginUser?: string;
     public wifiOn: boolean = false;

     async login(user: string) {
       return this.lock.lockAsync(() => {
         this.isLogin = true;
         this.loginUser = user;
       }, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE)
     }

     async logout(user?: string) {
       return this.lock.lockAsync(() => {
         this.isLogin = false;
         this.loginUser = '';
       }, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE)
     }

     async getIsLogin(): Promise<boolean> {
       return this.lock.lockAsync(() => {
         return this.isLogin;
       }, ArkTSUtils.locks.AsyncLockMode.SHARED)
     }

     async getUser(): Promise<string> {
       return this.lock.lockAsync(() => {
         return this.loginUser!;
       }, ArkTSUtils.locks.AsyncLockMode.SHARED)
     }

     async setWifiState(state: boolean) {
       return this.lock.lockAsync(() => {
         this.wifiOn = state;
       }, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE)
     }

     async isWifiOn() {
       return this.lock.lockAsync(() => {
         return this.wifiOn;
       }, ArkTSUtils.locks.AsyncLockMode.SHARED)
     }
   }

   export let config = new Config();
   ```
2. UI主线程及子线程访问全局配置项。

   ```typescript
   import { config } from './Config';
   import { taskpool } from '@kit.ArkTS';

   @Concurrent
   async function download() {
     if (!await config.isWifiOn()) {
       console.info('wifi is off');
       return false;
     }
     if (!await config.getIsLogin()) {
       console.info('not login');
       return false;
     }
     console.info(`User[${await config.getUser()}] start download ...`);
     return true;
   }

   @Entry
   @Component
   struct Index {
     @State message: string = 'not login';
     @State wifiState: string = 'wifi off';
     @State downloadResult: string = '';
     input: string = '';

     build() {
       Row() {
         Column() {
           Text(this.message)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
           TextInput({ placeholder: '请输入用户名' })
             .id('textInput')
             .fontSize(20)
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
             .onChange((value) => {
               this.input = value;
             })
           Text('login')
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
             .onClick(async () => {
               if (!await config.getIsLogin() && this.input) {
                 try {
                   await config.login(this.input);
                   this.message = 'login: ' + this.input;
                 } catch (e) {
                   console.error('login failed');
                 }
               }
             })
             .backgroundColor(0xcccccc)
           Text('logout')
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
             .onClick(async () => {
               if (await config.getIsLogin()) {
                 try {
                   await config.logout();
                   this.message = 'not login';
                 } catch (e) {
                   console.error('logout failed');
                 }
               }
             })
             .backgroundColor(0xcccccc)
           Text(this.wifiState)
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
           Toggle({ type: ToggleType.Switch })
             .onChange(async (isOn: boolean) => {
               await config.setWifiState(isOn)
               this.wifiState = isOn ? 'wifi on' : 'wifi off';
             })
           Text('download')
             .fontSize(50)
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
             .onClick(async () => {
               let ret = await taskpool.execute(download);
               this.downloadResult = ret ? 'download success' : 'download fail';
             })
           Text(this.downloadResult)
             .fontSize(20)
             .fontWeight(FontWeight.Bold)
             .alignRules({
               center: { anchor: '__container__', align: VerticalAlign.Center },
               middle: { anchor: '__container__', align: HorizontalAlign.Center }
             })
         }
         .width('100%')
       }
       .height('100%')
     }
   }
   ```
