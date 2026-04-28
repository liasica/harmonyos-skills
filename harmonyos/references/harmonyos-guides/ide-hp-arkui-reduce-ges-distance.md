---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hp-arkui-reduce-ges-distance
title: @performance/hp-arkui-reduce-pangesture-distance
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 性能规则@performance > @performance/hp-arkui-reduce-pangesture-distance
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:06+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:fee1472923bcaf1803d8799ac0a90fc6bce83c7a8b203c9f294d566587bb04bf
---

建议设置合理的拖动距离。

应用内点击响应时延场景下，建议优先修改。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@performance/hp-arkui-reduce-pangesture-distance": "suggestion",
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit'

3. @Entry
4. @Component
5. struct PanGestureExample {
6. @State offsetX: number = 0
7. @State offsetY: number = 0
8. @State positionX: number = 0
9. @State positionY: number = 0
10. private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right })

12. build() {
13. Column() {
14. Column() {
15. Text('PanGesture offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
16. }
17. .height(200)
18. .width(300)
19. .padding(20)
20. .border({ width: 3 })
21. .margin(50)
22. .translate({ x: this.offsetX, y: this.offsetY, z: 0 }) // 以组件左上角为坐标原点进行移动
23. // 左右拖动触发该手势事件
24. .gesture(
25. PanGesture(this.panOption)
26. .onActionStart((event: GestureEvent) => {
27. console.info('Pan start')
28. hiTraceMeter.startTrace("PanGesture", 1)
29. })
30. .onActionUpdate((event: GestureEvent) => {
31. if (event) {
32. this.offsetX = this.positionX + event.offsetX
33. this.offsetY = this.positionY + event.offsetY
34. }
35. })
36. .onActionEnd(() => {
37. this.positionX = this.offsetX
38. this.positionY = this.offsetY
39. console.info('Pan end')
40. hiTraceMeter.finishTrace("PanGesture", 1)
41. })
42. )

44. Button('修改PanGesture触发条件')
45. .onClick(() => {
46. // 设定的距离在阈值10以内
47. this.panOption.setDistance(4)
48. })
49. }
50. }
51. }
```

## 反例

```
1. import { hiTraceMeter } from '@kit.PerformanceAnalysisKit'

3. @Entry
4. @Component
5. struct PanGestureExample {
6. @State offsetX: number = 0
7. @State offsetY: number = 0
8. @State positionX: number = 0
9. @State positionY: number = 0
10. private panOption: PanGestureOptions = new PanGestureOptions({ direction: PanDirection.Left | PanDirection.Right })

12. build() {
13. Column() {
14. Column() {
15. Text('PanGesture offset:\nX: ' + this.offsetX + '\n' + 'Y: ' + this.offsetY)
16. }
17. .height(200)
18. .width(300)
19. .padding(20)
20. .border({ width: 3 })
21. .margin(50)
22. .translate({ x: this.offsetX, y: this.offsetY, z: 0 })
23. // 左右拖动触发该手势事件
24. .gesture(
25. PanGesture(this.panOption)
26. .onActionStart((event: GestureEvent) => {
27. console.info('Pan start')
28. hiTraceMeter.startTrace("PanGesture", 1)
29. })
30. .onActionUpdate((event: GestureEvent) => {
31. if (event) {
32. this.offsetX = this.positionX + event.offsetX
33. this.offsetY = this.positionY + event.offsetY
34. }
35. })
36. .onActionEnd(() => {
37. this.positionX = this.offsetX
38. this.positionY = this.offsetY
39. console.info('Pan end')
40. hiTraceMeter.finishTrace("PanGesture", 1)
41. })
42. )

44. Button('修改PanGesture触发条件')
45. .onClick(() => {
46. // 设定的距离超过阈值10
47. this.panOption.setDistance(100)
48. })
49. }
50. }
51. }
```

## 规则集

```
1. plugin:@performance/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
