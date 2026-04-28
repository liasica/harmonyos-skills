---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-app-freeze-opt
title: 应用冻屏类问题优化建议
breadcrumb: 最佳实践 > 稳定性 > 稳定性优化 > 应用冻屏类问题优化建议
category: best-practices
scraped_at: 2026-04-28T08:23:02+08:00
doc_updated_at: 2026-03-12
content_hash: sha256:0e741472de9a33358e490a7312165ca231b2f6fa3d91f9317d86cf1e7bad0167
---

## 优化建议1：多线程操作锁时，需要合理使用lock\_guard这类自动控制持锁和释放锁的管理方式

以下代码为没有考虑到多线程操作时锁的时序问题，从而导致死锁。

```
1. int AppFreezeAdviseNegative() {
2. // ...
3. mtx.lock();
4. if (ContainTarget(1)) {
5. return -1;
6. }
7. // ...
8. return 0;
9. }
```

[AppFreezeCase.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppFreeze/entry/src/main/cpp/AppFreezeCase.cpp#L53-L61)

优化建议：多线程操作锁时，需要合理使用lock\_guard这类自动控制持锁和释放锁的管理方式，同时注意锁的控制范围尽量要小，或按照如下修改方式及时释放锁。

```
1. int AppFreezeAdvisePositive() {
2. // ...
3. mtx.lock();
4. if (ContainTarget(1)) {
5. mtx.unlock();
6. return -1;
7. }
8. mtx.unlock();
9. // ...
10. return 0;
11. }
```

[AppFreezeCase.cpp](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppFreeze/entry/src/main/cpp/AppFreezeCase.cpp#L65-L75)

## 优化建议2：不要在主线程中提交大量重复或耗时操作

应用发生冻屏，但是主线程中却没有识别到耗时函数调用。

```
1. function getForeachKey(item : ItemType) : string {
2. // ...
3. return `${item.xxx2}${item.xxx2}...${item.themeStyle}`;
4. } // 这部分逻辑如果较为耗时，执行次数多，总时长就是发生冻屏的耗时操作
```

[appfreezecase.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppFreeze/entry/src/main/ets/pages/appfreezecase.ets#L31-L34)

```
1. function xxxFunction1(fileUris : string[]): void {
2. // ...
3. for (const fileuri of fileUris) {
4. let file = fs.openSync(fileuri, fs.OpenMode.READ_ONLY);
5. // ...
6. }
7. // ...
8. } // 如果使用同步操作，需要考虑到容器弱网或无网等极端情况发生
```

[appfreezecase.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppFreeze/entry/src/main/ets/pages/appfreezecase.ets#L42-L49)

优化建议：

1. 不要在主线程中提交大量重复或耗时操作，需要合理控制页面刷新的范围，考虑大量组件、频繁刷新等场景。
2. 请求云测数据需进行无网/弱网等边界场景测试，避免在生命周期函数中执行耗时操作。

```
1. async function xxxFunction2(fileUris : string[]) : Promise<void> {
2. // ...
3. AppStorage.setOrCreate<boolean>('isLoadingPic', true); // 用于页面load效果展示
4. for (const fileuri of fileUris) {
5. let file = await fs.openSync(fileuri, fs.OpenMode.READ_ONLY); // 改为异步加载
6. // ...
7. }
8. // ...
9. }
```

[appfreezecase.ets](https://gitcode.com/harmonyos_samples/BestPracticeSnippets/blob/master/AppFreeze/entry/src/main/ets/pages/appfreezecase.ets#L53-L61)
