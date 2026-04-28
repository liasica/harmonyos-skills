---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-reuse-date-instances-check
title: @performance/reuse-date-instances-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/reuse-date-instances-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:17+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:9c2c33aa206ba8f8b1fe79e7b771e3b82e4e829cbd378c3c6e9cfaebe47622ca
---

用于检测在循环或调用频繁的方法中重复创建Date对象，建议开发者重用现有实例或使用时间戳进行计算，减少创建Date成本。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/reuse-date-instances-check": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. aboutToAppear(): void {
2. // 记录开始时间戳
3. this.startTime = Date.now();
4. this.intervalId = setInterval(() => {
5. // 只获取时间戳，避免创建Date对象
6. const nowTimestamp = Date.now();
7. // 重用格式化结果
8. const currentTimeFormatted = this.formatElapsedTime(nowTimestamp);
9. this.currentTimeDisplay = currentTimeFormatted;
10. // 直接使用时间戳计算
11. const elapsedMs = nowTimestamp - this.startTime;
12. this.elapsedTimeDisplay = this.formatElapsedTime(elapsedMs);
13. // 添加到历史记录
14. const seconds = Math.floor(nowTimestamp / 1000) % 60;
15. if (seconds % 10 === 0) {
16. // 每十秒记录一次
17. this.elapsedTimes.push(`${this.elapsedTimeDisplay}-${currentTimeFormatted}`);
18. }
19. }, 1000);
20. }
```

## 反例

```
1. aboutToAppear(): void {
2. // 记录开始时间
3. this.startTime = Date.now();
4. // 问题：每秒创建多个Date对象
5. this.intervalId = setInterval(() => {
6. // 创建新Date对象显示当前时间
7. const now = new Date();
8. this.currentTimeDisplay = now.toLocaleTimeString();
9. // 再次创建Date对象计算持续时间
10. const currentDate = new Date();
11. const elapsedMs = currentDate.getTime() - this.startTime;
12. // 再次创建Date对象格式化持续时间
13. const elapsedDate = new Date(elapsedMs);
14. const hours = elapsedDate.getUTCHours();
15. const minutes = elapsedDate.getUTCMinutes();
16. const seconds = elapsedDate.getUTCSeconds();
17. const elapsedFormatted = `${hours.toString().padStart(2, '0')}:${
18. minutes.toString().padStart(2, '0')}:${
19. seconds.toString().padStart(2, '0')}`;
20. // 添加到历史记录
21. if (seconds % 10 === 0) {
22. // 每十秒记录一次
23. this.elapsedTimes.push(`${elapsedFormatted}-${new Date().toLocaleString()}`);
24. }
25. }, 1000);
26. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
