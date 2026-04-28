---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-suggest-cache-avplayer
title: @performance/hp-arkui-suggest-cache-avplayer
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-suggest-cache-avplayer
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:07+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:13efefe478a1a25c1e739b987fcc8fee64ffaa8b0dcc91c9b3c7e5dccca7796c
---

建议缓存AVPlayer实例减少起播时延。

音视频起播速度慢的场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-suggest-cache-avplayer": "warn",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import media from '@ohos.multimedia.media';

3. @Entry
4. @Component
5. struct MyComponent{
6. private avPlayer: media.AVPlayer | undefined = undefined;
7. private avPlayerManager: AVPlayerManager = AVPlayerManager.getInstance();

9. aboutToAppear(): void {
10. this.avPlayerManager.switchPlayer();
11. this.avPlayer = this.avPlayerManager.getCurrentPlayer();
12. }

14. aboutToDisappear(): void {
15. this.avPlayerManager.resetCurrentPlayer();
16. this.avPlayer = undefined;
17. }

19. build() {
20. // 组件布局
21. }
22. }

24. class AVPlayerManager {
25. private static instance?: AVPlayerManager;

27. private player1?: media.AVPlayer;
28. private player2?: media.AVPlayer;
29. private currentPlayer?: media.AVPlayer;

31. public static getInstance(): AVPlayerManager {
32. if (!AVPlayerManager.instance) {
33. AVPlayerManager.instance = new AVPlayerManager();
34. }
35. return AVPlayerManager.instance;
36. }

38. async AVPlayerManager() {
39. this.player1 = await media.createAVPlayer();
40. this.player2 = await media.createAVPlayer();
41. }

43. /**
44. * 切换页面时切换AVPlayer实例
45. */
46. switchPlayer(): void {
47. if (this.currentPlayer === this.player1) {
48. this.currentPlayer = this.player2;
49. } else {
50. this.currentPlayer = this.player1;
51. }
52. }

54. getCurrentPlayer(): media.AVPlayer | undefined {
55. return this.currentPlayer;
56. }

58. /**
59. * 使用reset方法重置AVPlayer实例
60. */
61. resetCurrentPlayer(): void {
62. this.currentPlayer?.pause(() => {
63. this.currentPlayer?.reset();
64. });
65. }
66. }
```

## 反例

```
1. import media from '@ohos.multimedia.media';

3. @Entry
4. @Component
5. struct MyComponent{
6. private avPlayer: media.AVPlayer | undefined = undefined;

8. aboutToAppear(): void {
9. // 页面创建时初始化AVPlayer实例
10. media.createAVPlayer().then((ret) => {
11. this.avPlayer = ret;
12. });
13. }

15. aboutToDisappear(): void {
16. // 离开页面时销毁AVPlayer实例
17. if (this.avPlayer) {
18. this.avPlayer.release();
19. }
20. this.avPlayer = undefined;
21. }

23. build() {
24. // 组件布局
25. }
26. }
```

## 规则集

```
1. plugin:@performance/recommended
2. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
