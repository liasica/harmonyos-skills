---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-reuse-date-instances-check
title: "@performance/reuse-date-instances-check"
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/reuse-date-instances-check
category: harmonyos-guides
scraped_at: 2026-09-02T14:50:53+08:00
doc_updated_at: 2026-08-29
content_hash: sha256:9a587462aad1dca07d6829814d0f2187211821b118044971cfd42ff8ba8c0679
---

用于检测在循环或频繁调用的方法中重复创建Date对象，建议开发者重用现有实例或使用时间戳进行计算，降低Date对象的创建成本。

## 规则配置

```screen
// code-linter.json5
{
  "rules": {
    "@performance/reuse-date-instances-check": "warn",
  }
}
```

## 选项

该规则无需配置选项。

## 正例

```screen
aboutToAppear(): void {
    // 记录开始时间戳
    this.startTime = Date.now();
    this.intervalId = setInterval(() => {
      // 只获取时间戳，避免创建Date对象
      const nowTimestamp = Date.now();
      // 重用格式化结果
      const currentTimeFormatted = this.formatElapsedTime(nowTimestamp);
      this.currentTimeDisplay = currentTimeFormatted;
      // 直接使用时间戳计算
      const elapsedMs = nowTimestamp - this.startTime;
      this.elapsedTimeDisplay = this.formatElapsedTime(elapsedMs);
      // 添加到历史记录
      const seconds = Math.floor(nowTimestamp / 1000) % 60;
      if (seconds % 10 === 0) {
        // 每十秒记录一次
        this.elapsedTimes.push(`${this.elapsedTimeDisplay}-${currentTimeFormatted}`);
      }
    }, 1000);
  }
```

## 反例

```screen
aboutToAppear(): void {
  // 记录开始时间
  this.startTime = Date.now();
  // 问题：每秒创建多个Date对象
  this.intervalId = setInterval(() => {
    // 创建新Date对象显示当前时间
    const now = new Date();
    this.currentTimeDisplay = now.toLocaleTimeString();
    // 再次创建Date对象计算持续时间
    const currentDate = new Date();
    const elapsedMs = currentDate.getTime() - this.startTime;
    // 再次创建Date对象格式化持续时间
    const elapsedDate = new Date(elapsedMs);
    const hours = elapsedDate.getUTCHours();
    const minutes = elapsedDate.getUTCMinutes();
    const seconds = elapsedDate.getUTCSeconds();
    const elapsedFormatted = `${hours.toString().padStart(2, '0')}:${
    minutes.toString().padStart(2, '0')}:${
    seconds.toString().padStart(2, '0')}`;
    // 添加到历史记录
    if (seconds % 10 === 0) {
      // 每十秒记录一次
      this.elapsedTimes.push(`${elapsedFormatted}-${new Date().toLocaleString()}`);
    }
  }, 1000);
}
```

## 规则集

```screen
plugin:@performance/recommended
plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
