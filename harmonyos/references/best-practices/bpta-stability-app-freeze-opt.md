---
url: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-app-freeze-opt
title: 应用冻屏类问题优化建议
breadcrumb: 最佳实践 > 稳定性 > 稳定性优化 > 应用冻屏类问题优化建议
category: best-practices
scraped_at: 2026-09-02T14:53:47+08:00
doc_updated_at: 2026-05-22
content_hash: sha256:6190ab13660e752525866a685852dede0420db4dc4e4bbd3bc2d9880b2c3f72f
---

## 优化建议1：多线程操作锁时，需要合理使用lock\_guard这类自动控制持锁和释放锁的管理方式

以下代码为没有考虑到多线程操作时锁的时序问题，从而导致死锁。

```cpp
int AppFreezeAdviseNegative() {
    // ...
    mtx.lock();
    if (ContainTarget(1)) {
        return -1;
    }
    // ...
     return 0;
}
```

优化建议：多线程操作锁时，需要合理使用lock\_guard这类自动控制持锁和释放锁的管理方式，同时注意锁的控制范围尽量要小，或按照如下修改方式及时释放锁。

```cpp
int AppFreezeAdvisePositive() {
    // ...
    mtx.lock();
    if (ContainTarget(1)) {
        mtx.unlock();
        return -1;
    }
    mtx.unlock();
    // ...
    return 0;
}
```

## 优化建议2：不要在主线程中提交大量重复或耗时操作

应用发生冻屏，但是主线程中却没有识别到耗时函数调用。

```typescript
function getForeachKey(item : ItemType) : string {
    // ...
    return `${item.xxx2}${item.xxx2}...${item.themeStyle}`;
} // 这部分逻辑如果较为耗时，执行次数多，总时长就是发生冻屏的耗时操作
```

```screen
function xxxFunction1(fileUris : string[]): void {
    // ...
    for (const fileuri of fileUris) {
        let file = fileIo.openSync(fileuri, fileIo.OpenMode.READ_ONLY);
        // ...
    }
    // ...
} // 如果使用同步操作，需要考虑到容器弱网或无网等极端情况发生
```

优化建议：

1. 不要在主线程中提交大量重复或耗时操作，需要合理控制页面刷新的范围，考虑大量组件、频繁刷新等场景。
2. 请求云测数据需进行无网/弱网等边界场景测试，避免在生命周期函数中执行耗时操作。

```screen
async function xxxFunction2(fileUris : string[]) : Promise<void> {
    // ...
    AppStorage.setOrCreate<boolean>('isLoadingPic', true); // 用于页面load效果展示
    for (const fileuri of fileUris) {
        let file = await fileIo.open(fileuri, fileIo.OpenMode.READ_ONLY); // 改为异步加载
        // ...
    }
    // ...
}
```
