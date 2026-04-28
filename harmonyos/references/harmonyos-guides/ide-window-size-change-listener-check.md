---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-window-size-change-listener-check
title: @cross-device-app-dev/window-size-change-listener-check
breadcrumb: 指南 > 编写与调试应用 > 代码编辑 > 代码检查 > Code Linter代码检查规则 > 一次开发多端部署规则@cross-device-app-dev > @cross-device-app-dev/window-size-change-listener-check
category: harmonyos-guides
scraped_at: 2026-04-28T07:56:23+08:00
doc_updated_at: 2026-01-15
content_hash: sha256:55c9a5f685bb68d9615becff2ef52e22de05db72008915d4884e87dc4f7a057b
---

应用代码中如果创建了window实例，建议开启窗口尺寸变化（'windowSizeChange'）的监听。

## 规则配置

```
1. // code-linter.json5
2. {
3. "rules": {
4. "@cross-device-app-dev/window-size-change-listener-check": "suggestion"
5. }
6. }
```

## 选项

该规则无需配置额外选项。

## 正例

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. export default class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage): void {
6. let config: window.Configuration = {
7. name: "test",
8. windowType: window.WindowType.TYPE_DIALOG,
9. ctx: this.context
10. };
11. try {
12. window.createWindow(config, (err: BusinessError, data) => {
13. const errCode: number = err.code;
14. if (errCode) {
15. console.error(`Failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
16. return;
17. }
18. data.on('windowSizeChange', () => {
19. console.info('window size changed');
20. });
21. });
22. } catch (exception) {
23. console.error(`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
24. }
25. }
26. }
```

## 反例

```
1. import { UIAbility } from '@kit.AbilityKit';
2. import { window } from '@kit.ArkUI';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. export default class EntryAbility extends UIAbility {
5. onWindowStageCreate(windowStage: window.WindowStage): void {
6. let windowClass: window.Window | undefined = undefined;
7. let config: window.Configuration = {
8. name: "test",
9. windowType: window.WindowType.TYPE_DIALOG,
10. ctx: this.context
11. };
12. try {
13. window.createWindow(config, (err: BusinessError, data) => {
14. const errCode: number = err.code;
15. if (errCode) {
16. console.error(`Failed to create the window. Cause code: ${err.code}, message: ${err.message}`);
17. return;
18. }
19. windowClass = data;
20. console.info('Succeeded in creating the window. Data: ' + JSON.stringify(data));
21. windowClass.resize(500, 1000);
22. });
23. } catch (exception) {
24. console.error(`Failed to create the window. Cause code: ${exception.code}, message: ${exception.message}`);
25. }
26. }
27. }
```

## 规则集

```
1. plugin:@cross-device-app-dev/all
```

Code Linter代码检查规则的配置指导请参考[Code Linter代码检查](ide-code-linter.md)。
