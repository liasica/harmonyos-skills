---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/global-configuration-guide
title: 全局配置项功能场景
breadcrumb: 指南 > 应用框架 > ArkTS（方舟编程语言） > ArkTS并发 > 应用多线程开发实践 > 应用多线程开发实践案例 > 全局配置项功能场景
category: harmonyos-guides
scraped_at: 2026-04-28T07:38:41+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:a4cec6f5343cbaa29e144a016b8c7574c58ba4f21ea48d4652a317b2e10c9a0b
---

对于需要使用进程单例的场景，例如不同并发实例间需要数据保持一致的全局配置项功能，可以采用[共享模块](arkts-sendable-module.md)来实现。

以下示例展示了只有在Wi-Fi打开且用户登录的情况下才能进行下载的功能，具体步骤如下。

1. 编写全局配置文件。

   ```
   1. import { ArkTSUtils } from '@kit.ArkTS';

   3. 'use shared'

   5. @Sendable
   6. class Config {
   7. public lock: ArkTSUtils.locks.AsyncLock = new ArkTSUtils.locks.AsyncLock;
   8. public isLogin: boolean = false;
   9. public loginUser?: string;
   10. public wifiOn: boolean = false;

   12. async login(user: string) {
   13. return this.lock.lockAsync(() => {
   14. this.isLogin = true;
   15. this.loginUser = user;
   16. }, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE)
   17. }

   19. async logout(user?: string) {
   20. return this.lock.lockAsync(() => {
   21. this.isLogin = false;
   22. this.loginUser = '';
   23. }, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE)
   24. }

   26. async getIsLogin(): Promise<boolean> {
   27. return this.lock.lockAsync(() => {
   28. return this.isLogin;
   29. }, ArkTSUtils.locks.AsyncLockMode.SHARED)
   30. }

   32. async getUser(): Promise<string> {
   33. return this.lock.lockAsync(() => {
   34. return this.loginUser!;
   35. }, ArkTSUtils.locks.AsyncLockMode.SHARED)
   36. }

   38. async setWifiState(state: boolean) {
   39. return this.lock.lockAsync(() => {
   40. this.wifiOn = state;
   41. }, ArkTSUtils.locks.AsyncLockMode.EXCLUSIVE)
   42. }

   44. async isWifiOn() {
   45. return this.lock.lockAsync(() => {
   46. return this.wifiOn;
   47. }, ArkTSUtils.locks.AsyncLockMode.SHARED)
   48. }
   49. }

   51. export let config = new Config();
   ```
2. UI主线程及子线程访问全局配置项。

   ```
   1. import { config } from './Config';
   2. import { taskpool } from '@kit.ArkTS';

   4. @Concurrent
   5. async function download() {
   6. if (!await config.isWifiOn()) {
   7. console.info('wifi is off');
   8. return false;
   9. }
   10. if (!await config.getIsLogin()) {
   11. console.info('not login');
   12. return false;
   13. }
   14. console.info(`User[${await config.getUser()}] start download ...`);
   15. return true;
   16. }

   18. @Entry
   19. @Component
   20. struct Index {
   21. @State message: string = 'not login';
   22. @State wifiState: string = 'wifi off';
   23. @State downloadResult: string = '';
   24. input: string = '';

   26. build() {
   27. Row() {
   28. Column() {
   29. Text(this.message)
   30. .fontSize(50)
   31. .fontWeight(FontWeight.Bold)
   32. .alignRules({
   33. center: { anchor: '__container__', align: VerticalAlign.Center },
   34. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   35. })
   36. TextInput({ placeholder: '请输入用户名' })
   37. .id('textInput')
   38. .fontSize(20)
   39. .fontWeight(FontWeight.Bold)
   40. .alignRules({
   41. center: { anchor: '__container__', align: VerticalAlign.Center },
   42. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   43. })
   44. .onChange((value) => {
   45. this.input = value;
   46. })
   47. Text('login')
   48. .fontSize(50)
   49. .fontWeight(FontWeight.Bold)
   50. .alignRules({
   51. center: { anchor: '__container__', align: VerticalAlign.Center },
   52. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   53. })
   54. .onClick(async () => {
   55. if (!await config.getIsLogin() && this.input) {
   56. this.message = 'login: ' + this.input;
   57. try {
   58. config.login(this.input);
   59. } catch (e) {
   60. console.info('login failed');
   61. }
   62. }
   63. })
   64. .backgroundColor(0xcccccc)
   65. Text('logout')
   66. .fontSize(50)
   67. .fontWeight(FontWeight.Bold)
   68. .alignRules({
   69. center: { anchor: '__container__', align: VerticalAlign.Center },
   70. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   71. })
   72. .onClick(async () => {
   73. if (await config.getIsLogin()) {
   74. this.message = 'not login';
   75. try {
   76. config.logout();
   77. } catch (e) {
   78. console.info('logout failed');
   79. }
   80. }
   81. })
   82. .backgroundColor(0xcccccc)
   83. Text(this.wifiState)
   84. .fontSize(50)
   85. .fontWeight(FontWeight.Bold)
   86. .alignRules({
   87. center: { anchor: '__container__', align: VerticalAlign.Center },
   88. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   89. })
   90. Toggle({ type: ToggleType.Switch })
   91. .onChange(async (isOn: boolean) => {
   92. await config.setWifiState(isOn)
   93. this.wifiState = isOn ? 'wifi on' : 'wifi off';
   94. })
   95. Text('download')
   96. .fontSize(50)
   97. .fontWeight(FontWeight.Bold)
   98. .alignRules({
   99. center: { anchor: '__container__', align: VerticalAlign.Center },
   100. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   101. })
   102. .onClick(async () => {
   103. let ret = await taskpool.execute(download);
   104. this.downloadResult = ret ? 'download success' : 'download fail';
   105. })
   106. Text(this.downloadResult)
   107. .fontSize(20)
   108. .fontWeight(FontWeight.Bold)
   109. .alignRules({
   110. center: { anchor: '__container__', align: VerticalAlign.Center },
   111. middle: { anchor: '__container__', align: HorizontalAlign.Center }
   112. })
   113. }
   114. .width('100%')
   115. }
   116. .height('100%')
   117. }
   118. }
   ```
