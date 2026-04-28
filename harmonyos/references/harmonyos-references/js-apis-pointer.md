---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-pointer
title: @ohos.multimodalInput.pointer (鼠标光标)
breadcrumb: API参考 > 系统 > 基础功能 > Input Kit（多模输入服务） > ArkTS API > @ohos.multimodalInput.pointer (鼠标光标)
category: harmonyos-references
scraped_at: 2026-04-28T08:10:15+08:00
doc_updated_at: 2026-04-20
content_hash: sha256:f14d09cc9ea0cc8333eb19b5c041b3f77e9fd5da06add424fbd55b167f3245fd
---

本模块提供鼠标光标管理能力，包括查询、设置鼠标光标属性。

说明

* 本模块首批接口从API version 9开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

## 导入模块

PhonePC/2in1TabletTV

```
1. import { pointer } from '@kit.InputKit';
```

## pointer.setPointerVisible

PhonePC/2in1TabletTV

setPointerVisible(visible: boolean, callback: AsyncCallback<void>): void

设置当前窗口的鼠标光标是否显示，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | 当前窗口鼠标光标是否显示。true表示显示，false表示不显示。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例**：

```
1. import { pointer } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. try {
12. pointer.setPointerVisible(true, (error: BusinessError) => {
13. if (error) {
14. console.error(`Set pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
15. return;
16. }
17. console.info(`Set pointer visible success`);
18. });
19. } catch (error) {
20. console.error(`Set pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
21. }
22. })
23. }
24. }
25. }
```

## pointer.setPointerVisible

PhonePC/2in1TabletTV

setPointerVisible(visible: boolean): Promise<void>

设置当前窗口的鼠标光标是否显示，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | 当前窗口鼠标光标是否显示。true表示显示，false表示不显示。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |

**示例**：

```
1. import { pointer } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. try {
12. pointer.setPointerVisible(false).then(() => {
13. console.info(`Set pointer visible success`);
14. }).catch((error: BusinessError) => {
15. console.error(`Set pointer failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
16. })
17. } catch (error) {
18. console.error(`Set pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
19. }
20. })
21. }
22. }
23. }
```

## pointer.setPointerVisibleSync10+

PhonePC/2in1TabletTV

setPointerVisibleSync(visible: boolean): void

设置当前窗口鼠标光标的显示状态，使用同步方式。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| visible | boolean | 是 | 当前窗口鼠标光标是否显示。true表示显示，false表示不显示。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { pointer } from '@kit.InputKit';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. RelativeContainer() {
8. Text()
9. .onClick(() => {
10. try {
11. pointer.setPointerVisibleSync(false);
12. console.info(`Set pointer visible success`);
13. } catch (error) {
14. console.error(`Set pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
15. }
16. })
17. }
18. }
19. }
```

## pointer.isPointerVisible

PhonePC/2in1TabletTV

isPointerVisible(callback: AsyncCallback<boolean>): void

获取鼠标光标显示状态，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| callback | AsyncCallback<boolean> | 是 | 回调函数，返回鼠标光标状态，true为显示，false为隐藏。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { pointer } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. try {
12. pointer.isPointerVisible((error: BusinessError, visible: boolean) => {
13. if (error) {
14. console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
15. return;
16. }
17. console.info(`Get pointer visible success, visible: ${JSON.stringify(visible)}`);
18. });
19. } catch (error) {
20. console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
21. }
22. })
23. }
24. }
25. }
```

## pointer.isPointerVisible

PhonePC/2in1TabletTV

isPointerVisible(): Promise<boolean>

获取鼠标光标显示状态，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<boolean> | Promise对象，返回鼠标光标状态查询结果。true代表显示状态，false代表隐藏状态。 |

**示例**：

```
1. import { pointer } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';

4. @Entry
5. @Component
6. struct Index {
7. build() {
8. RelativeContainer() {
9. Text()
10. .onClick(() => {
11. try {
12. pointer.isPointerVisible().then((visible: boolean) => {
13. console.info(`Get pointer visible success, visible: ${JSON.stringify(visible)}`);
14. }).catch((error: BusinessError) => {
15. console.error(`Get pointer failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
16. })
17. } catch (error) {
18. console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
19. }
20. })
21. }
22. }
23. }
```

## pointer.isPointerVisibleSync10+

PhonePC/2in1TabletTV

isPointerVisibleSync(): boolean

获取当前窗口鼠标光标的显示状态，使用同步方式。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**返回值**：

| 类型 | 说明 |
| --- | --- |
| boolean | 返回鼠标光标显示或隐藏状态。true代表显示状态，false代表隐藏状态。 |

**示例**：

```
1. import { pointer } from '@kit.InputKit';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. RelativeContainer() {
8. Text()
9. .onClick(() => {
10. try {
11. let visible: boolean = pointer.isPointerVisibleSync();
12. console.info(`Get pointer visible success, visible: ${JSON.stringify(visible)}`);
13. } catch (error) {
14. console.error(`Get pointer visible failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
15. }
16. })
17. }
18. }
19. }
```

## pointer.getPointerStyle

PhonePC/2in1TabletTV

getPointerStyle(windowId: number, callback: AsyncCallback<PointerStyle>): void

获取指定窗口的鼠标样式类型，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | number | 是 | 窗口ID。取值范围为大于等于-1的整数，取值为-1时表示全局窗口。  窗口ID合法并且对应窗口存在时，返回窗口的鼠标光标样式。  窗口ID合法但窗口不存在时，默认返回全局鼠标光标样式。  如果通过[setPointerStyle](js-apis-pointer.md#pointersetpointerstyle)接口为不存在的窗口设置了鼠标光标样式，使用本接口可以正常获取到该光标样式。 |
| callback | AsyncCallback<[PointerStyle](js-apis-pointer.md#pointerstyle)> | 是 | 回调函数，返回鼠标样式类型。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { pointer } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. RelativeContainer() {
10. Text()
11. .onClick(() => {
12. window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
13. if (error.code) {
14. console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
15. return;
16. }
17. let windowId = win.getWindowProperties().id;
18. if (windowId < 0) {
19. console.info(`Invalid windowId`);
20. return;
21. }
22. try {
23. pointer.getPointerStyle(windowId, (error: BusinessError, style: pointer.PointerStyle) => {
24. console.info(`Get pointer style success, style: ${JSON.stringify(style)}`);
25. });
26. } catch (error) {
27. console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
28. }
29. });
30. })
31. }
32. }
33. }
```

## pointer.getPointerStyle

PhonePC/2in1TabletTV

getPointerStyle(windowId: number): Promise<PointerStyle>

获取鼠标样式类型，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | number | 是 | 窗口ID。取值范围为大于等于-1的整数，取值为-1时表示全局窗口。  窗口ID合法并且对应窗口存在时，返回窗口的鼠标光标样式。  窗口ID合法但窗口不存在时，默认返回全局鼠标光标样式。  如果通过[setPointerStyle](js-apis-pointer.md#pointersetpointerstyle-1)接口为不存在的窗口设置了鼠标光标样式，使用本接口可以正常获取到该光标样式。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<[PointerStyle](js-apis-pointer.md#pointerstyle)> | Promise对象，返回鼠标样式类型。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { pointer } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. RelativeContainer() {
10. Text()
11. .onClick(() => {
12. window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
13. if (error.code) {
14. console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
15. return;
16. }
17. let windowId = win.getWindowProperties().id;
18. if (windowId < 0) {
19. console.info(`Invalid windowId`);
20. return;
21. }
22. try {
23. pointer.getPointerStyle(windowId).then((style: pointer.PointerStyle) => {
24. console.info(`Get pointer style success, style: ${JSON.stringify(style)}`);
25. }).catch((error: BusinessError) => {
26. console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
27. });
28. } catch (error) {
29. console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
30. }
31. });
32. })
33. }
34. }
35. }
```

## pointer.getPointerStyleSync10+

PhonePC/2in1TabletTV

getPointerStyleSync(windowId: number): PointerStyle

查询指定窗口的鼠标样式类型，如向东箭头、向西箭头、向南箭头、向北箭头等。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | number | 是 | 窗口ID。取值范围为大于等于-1的整数，取值为-1时表示全局窗口。  窗口ID合法并且对应窗口存在时，返回窗口的鼠标光标样式。  窗口ID合法但窗口不存在时，默认返回全局鼠标光标样式。  如果通过[setPointerStyleSync](js-apis-pointer.md#pointersetpointerstylesync10)接口为不存在的窗口设置了鼠标光标样式，使用本接口可以正常获取到该光标样式。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| [PointerStyle](js-apis-pointer.md#pointerstyle) | 返回鼠标样式类型。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { pointer } from '@kit.InputKit';

3. @Entry
4. @Component
5. struct Index {
6. build() {
7. RelativeContainer() {
8. Text()
9. .onClick(() => {
10. let windowId = -1;
11. try {
12. let style: pointer.PointerStyle = pointer.getPointerStyleSync(windowId);
13. console.info(`Get pointer style success, style: ${JSON.stringify(style)}`);
14. } catch (error) {
15. console.error(`Get pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
16. }
17. })
18. }
19. }
20. }
```

## pointer.setPointerStyle

PhonePC/2in1TabletTV

setPointerStyle(windowId: number, pointerStyle: PointerStyle, callback: AsyncCallback<void>): void

设置指定窗口的鼠标样式类型，使用callback异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | number | 是 | 窗口ID。取值范围为大于等于0的整数。  窗口ID合法并且对应窗口存在时，可以设置窗口的鼠标光标样式。  窗口ID合法但窗口不存在时，也可以设置鼠标光标样式。  设置结果可通过[getPointerStyle](js-apis-pointer.md#pointergetpointerstyle)获取。 |
| pointerStyle | [PointerStyle](js-apis-pointer.md#pointerstyle) | 是 | 鼠标样式。 |
| callback | AsyncCallback<void> | 是 | 回调函数。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { pointer } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. RelativeContainer() {
10. Text()
11. .onClick(() => {
12. window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
13. if (error.code) {
14. console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
15. return;
16. }
17. let windowId = win.getWindowProperties().id;
18. if (windowId < 0) {
19. console.info(`Invalid windowId`);
20. return;
21. }
22. try {
23. pointer.setPointerStyle(windowId, pointer.PointerStyle.CROSS, error => {
24. console.info(`Set pointer style success`);
25. });
26. } catch (error) {
27. console.error(`Set pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
28. }
29. });
30. })
31. }
32. }
33. }
```

## pointer.setPointerStyle

PhonePC/2in1TabletTV

setPointerStyle(windowId: number, pointerStyle: PointerStyle): Promise<void>

设置指定窗口的鼠标样式类型，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | number | 是 | 窗口ID。取值范围为大于等于0的整数。  窗口ID合法并且对应窗口存在时，可以设置窗口的鼠标光标样式。  窗口ID合法但窗口不存在时，也可以设置鼠标光标样式。  设置结果可通过[getPointerStyle](js-apis-pointer.md#pointergetpointerstyle-1)获取。 |
| pointerStyle | [PointerStyle](js-apis-pointer.md#pointerstyle) | 是 | 鼠标样式。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { pointer } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. RelativeContainer() {
10. Text()
11. .onClick(() => {
12. window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
13. if (error.code) {
14. console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
15. return;
16. }
17. let windowId = win.getWindowProperties().id;
18. if (windowId < 0) {
19. console.info(`Invalid windowId`);
20. return;
21. }
22. try {
23. pointer.setPointerStyle(windowId, pointer.PointerStyle.CROSS).then(() => {
24. console.info(`Set pointer style success`);
25. }).catch((error: BusinessError) => {
26. console.error(`Set pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
27. });
28. } catch (error) {
29. console.error(`Set pointer style failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
30. }
31. });
32. })
33. }
34. }
35. }
```

## pointer.setPointerStyleSync10+

PhonePC/2in1TabletTV

setPointerStyleSync(windowId: number, pointerStyle: PointerStyle): void

设置指定窗口的鼠标样式类型，使用同步方式返回结果。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | number | 是 | 窗口ID。取值范围为大于等于0的整数。  窗口ID合法并且对应窗口存在时，可以设置窗口的鼠标光标样式。  窗口ID合法但窗口不存在时，也可以设置鼠标光标样式。  设置结果可通过[getPointerStyleSync](js-apis-pointer.md#pointergetpointerstylesync10)获取。 |
| pointerStyle | [PointerStyle](js-apis-pointer.md#pointerstyle) | 是 | 鼠标样式。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { pointer } from '@kit.InputKit';
2. import { BusinessError } from '@kit.BasicServicesKit';
3. import { window } from '@kit.ArkUI';

5. @Entry
6. @Component
7. struct Index {
8. build() {
9. RelativeContainer() {
10. Text()
11. .onClick(() => {
12. window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
13. if (error.code) {
14. console.error('Failed to obtain the top window. Cause: ' + JSON.stringify(error));
15. return;
16. }
17. let windowId = win.getWindowProperties().id;
18. if (windowId < 0) {
19. console.info(`Invalid windowId`);
20. return;
21. }
22. try {
23. pointer.setPointerStyleSync(windowId, pointer.PointerStyle.CROSS);
24. console.info(`Set pointer style success`);
25. } catch (error) {
26. console.error(`getPointerSize failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
27. }
28. });
29. })
30. }
31. }
32. }
```

## PrimaryButton10+

PhonePC/2in1TabletTV

鼠标主键类型。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| LEFT | 0 | 鼠标左键。 |
| RIGHT | 1 | 鼠标右键。 |

## RightClickType10+

PhonePC/2in1TabletTV

右键菜单的触发方式。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

| 名称 | 值 | 说明 |
| --- | --- | --- |
| TOUCHPAD\_RIGHT\_BUTTON | 1 | 按压触控板右键区域。 |
| TOUCHPAD\_LEFT\_BUTTON | 2 | 按压触控板左键区域。 |
| TOUCHPAD\_TWO\_FINGER\_TAP | 3 | 双指轻击或双指按压触控板。 |
| TOUCHPAD\_TWO\_FINGER\_TAP\_OR\_RIGHT\_BUTTON20+ | 4 | 双指轻击或双指按压触控板、或按压触控板右键区域。 |
| TOUCHPAD\_TWO\_FINGER\_TAP\_OR\_LEFT\_BUTTON20+ | 5 | 双指轻击或双指按压触控板、或按压触控板左键区域。 |

## PointerStyle

PhonePC/2in1TabletTV

鼠标光标样式类型。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

| 名称 | 值 | 说明 | 图示 |
| --- | --- | --- | --- |
| DEFAULT | 0 | 默认 |  |
| EAST | 1 | 向东箭头 |  |
| WEST | 2 | 向西箭头 |  |
| SOUTH | 3 | 向南箭头 |  |
| NORTH | 4 | 向北箭头 |  |
| WEST\_EAST | 5 | 向西东箭头 |  |
| NORTH\_SOUTH | 6 | 向北南箭头 |  |
| NORTH\_EAST | 7 | 向东北箭头 |  |
| NORTH\_WEST | 8 | 向西北箭头 |  |
| SOUTH\_EAST | 9 | 向东南箭头 |  |
| SOUTH\_WEST | 10 | 向西南箭头 |  |
| NORTH\_EAST\_SOUTH\_WEST | 11 | 东北西南调整 |  |
| NORTH\_WEST\_SOUTH\_EAST | 12 | 西北东南调整 |  |
| CROSS | 13 | 准确选择 |  |
| CURSOR\_COPY | 14 | 拷贝 |  |
| CURSOR\_FORBID | 15 | 不可用 |  |
| COLOR\_SUCKER | 16 | 取色器 |  |
| HAND\_GRABBING | 17 | 并拢的手 |  |
| HAND\_OPEN | 18 | 张开的手 |  |
| HAND\_POINTING | 19 | 手形指针 |  |
| HELP | 20 | 帮助选择 |  |
| MOVE | 21 | 移动 |  |
| RESIZE\_LEFT\_RIGHT | 22 | 内部左右调整 |  |
| RESIZE\_UP\_DOWN | 23 | 内部上下调整 |  |
| SCREENSHOT\_CHOOSE | 24 | 截图十字准星 |  |
| SCREENSHOT\_CURSOR | 25 | 截图 |  |
| TEXT\_CURSOR | 26 | 文本选择 |  |
| ZOOM\_IN | 27 | 放大 |  |
| ZOOM\_OUT | 28 | 缩小 |  |
| MIDDLE\_BTN\_EAST | 29 | 向东滚动 |  |
| MIDDLE\_BTN\_WEST | 30 | 向西滚动 |  |
| MIDDLE\_BTN\_SOUTH | 31 | 向南滚动 |  |
| MIDDLE\_BTN\_NORTH | 32 | 向北滚动 |  |
| MIDDLE\_BTN\_NORTH\_SOUTH | 33 | 向南北滚动 |  |
| MIDDLE\_BTN\_NORTH\_EAST | 34 | 向东北滚动 |  |
| MIDDLE\_BTN\_NORTH\_WEST | 35 | 向西北滚动 |  |
| MIDDLE\_BTN\_SOUTH\_EAST | 36 | 向东南滚动 |  |
| MIDDLE\_BTN\_SOUTH\_WEST | 37 | 向西南滚动 |  |
| MIDDLE\_BTN\_NORTH\_SOUTH\_WEST\_EAST | 38 | 四向锥形移动 |  |
| HORIZONTAL\_TEXT\_CURSOR10+ | 39 | 垂直文本选择 |  |
| CURSOR\_CROSS10+ | 40 | 十字光标 |  |
| CURSOR\_CIRCLE10+ | 41 | 圆形光标 |  |
| LOADING10+ | 42 | 正在载入动画光标  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |  |
| RUNNING10+ | 43 | 后台运行中动画光标  **元服务API：** 从API version 12开始，该接口支持在元服务中使用。 |  |
| MIDDLE\_BTN\_EAST\_WEST18+ | 44 | 向东西滚动 |  |
| RUNNING\_LEFT22+ | 45 | 后台运行中动画光标(拓展1) |  |
| RUNNING\_RIGHT22+ | 46 | 后台运行中动画光标(拓展2) |  |
| AECH\_DEVELOPER\_DEFINED\_ICON22+ | 47 | 圆形自定义光标 |  |
| SCREENRECORDER\_CURSOR20+ | 48 | 录屏光标 |  |
| LASER\_CURSOR22+ | 49 | 悬浮光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。  空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。 |  |
| LASER\_CURSOR\_DOT22+ | 50 | 点击光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。  空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。 |  |
| LASER\_CURSOR\_DOT\_RED22+ | 51 | 激光笔光标。手写笔进入空鼠模式时使用该光标，无法直接使用 。  空鼠模式支持通过手写笔在空中转动来控制屏幕上虚拟光标的移动，并借助笔身按键实现上下翻页功能，用于演示PPT、隔空操作等场景。 |  |
| DEVELOPER\_DEFINED\_ICON22+ | -100 | 自定义光标，开发者可使用[setCustomCursor](js-apis-pointer.md#pointersetcustomcursor15)设置自定义光标，不支持使用[setPointerStyle](js-apis-pointer.md#pointersetpointerstyle-1)直接设置。 | 自定义光标样式，通过接口设置。 |

## pointer.setCustomCursor11+

PhonePC/2in1TabletTV

setCustomCursor(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): Promise<void>

设置指定窗口的自定义光标样式，使用Promise异步回调。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | number | 是 | 窗口ID。 |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 自定义光标资源。 |
| focusX | number | 否 | 自定义光标焦点x，取值范围：大于等于0，默认为0。 |
| focusY | number | 否 | 自定义光标焦点y，取值范围：大于等于0，默认为0。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { pointer } from '@kit.InputKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. @Entry
7. @Component
8. struct Index {
9. build() {
10. RelativeContainer() {
11. Text()
12. .onClick(() => {
13. // app_icon为示例资源，请开发者根据实际需求配置资源文件。
14. this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent(
15. $r("app.media.app_icon").id, (error: BusinessError, svgFileData: Uint8Array) => {
16. const svgBuffer: ArrayBuffer = svgFileData.buffer.slice(0);
17. let svgImageSource: image.ImageSource = image.createImageSource(svgBuffer);
18. let svgDecodingOptions: image.DecodingOptions = { desiredSize: { width: 50, height: 50 } };
19. svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
20. window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
21. let windowId = win.getWindowProperties().id;
22. try {
23. pointer.setCustomCursor(windowId, pixelMap).then(() => {
24. console.info(`setCustomCursor success`);
25. });
26. } catch (error) {
27. console.error(`setCustomCursor failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
28. }
29. });
30. }).catch((error: BusinessError) => {
31. console.error(`createPixelMap promise error: ${JSON.stringify(error, [`code`, `message`])}`);
32. });
33. });
34. })
35. }
36. }
37. }
```

## CustomCursor15+

PhonePC/2in1TabletTV

自定义光标资源。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 否 | 否 | 自定义光标。最小限制为资源图本身的最小限制。最大限制为256 x 256px。 |
| focusX | number | 否 | 是 | 自定义光标焦点的水平坐标。该坐标受自定义光标大小的限制。最小值为0，最大值为资源图的宽度最大值，该参数缺省时默认为0。 |
| focusY | number | 否 | 是 | 自定义光标焦点的垂直坐标。该坐标受自定义光标大小的限制。最小值为0，最大值为资源图的高度最大值，该参数缺省时默认为0。 |

## CursorConfig15+

PhonePC/2in1TabletTV

自定义光标配置。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

| 名称 | 类型 | 只读 | 可选 | 说明 |
| --- | --- | --- | --- | --- |
| followSystem | boolean | 否 | 否 | 是否根据系统设置调整光标大小。false表示使用自定义光标样式大小，true表示根据系统设置调整光标大小，可调整范围为：[光标资源图大小，256×256]。 |

## pointer.setCustomCursor15+

PhonePC/2in1TabletTV

setCustomCursor(windowId: number, cursor: CustomCursor, config: CursorConfig): Promise<void>

设置指定窗口的自定义光标样式，使用Promise异步回调。

应用窗口布局改变、热区切换、页面跳转、光标移出再回到窗口、光标在窗口不同区域移动，以上场景可能导致光标切换回系统样式，需要开发者重新设置光标样式。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | number | 是 | 窗口ID。 |
| cursor | [CustomCursor](js-apis-pointer.md#customcursor15) | 是 | 自定义光标资源。 |
| config | [CursorConfig](js-apis-pointer.md#cursorconfig15) | 是 | 自定义光标配置，用于配置是否根据系统设置调整光标大小。如果CursorConfig中followSystem设置为true，则光标大小的可调整范围为：[光标资源图大小，256×256]。 |

**返回值**：

| 类型 | 说明 |
| --- | --- |
| Promise<void> | Promise对象，无返回结果的Promise对象。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)和[鼠标光标错误码](errorcode-pointer.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Abnormal windowId parameter passed in. 2. Abnormal pixelMap parameter passed in; 3. Abnormal focusX parameter passed in.4. Abnormal focusY parameter passed in. |
| 26500001 | Invalid windowId. Possible causes: The window id does not belong to the current process. |

**示例**：

```
1. import { pointer } from '@kit.InputKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. @Entry
7. @Component
8. struct Index {
9. build() {
10. RelativeContainer() {
11. Text()
12. .onClick(() => {
13. // app_icon为示例资源，请开发者根据实际需求配置资源文件。
14. this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent(
15. $r("app.media.app_icon").id, (error: BusinessError, svgFileData: Uint8Array) => {
16. const svgBuffer: ArrayBuffer = svgFileData.buffer.slice(0);
17. let svgImageSource: image.ImageSource = image.createImageSource(svgBuffer);
18. let svgDecodingOptions: image.DecodingOptions = { desiredSize: { width: 50, height: 50 } };
19. svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
20. window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
21. let windowId = win.getWindowProperties().id;
22. try {
23. pointer.setCustomCursor(windowId, { pixelMap: pixelMap, focusX: 25, focusY: 25 },
24. { followSystem: false }).then(() => {
25. console.info(`setCustomCursor success`);
26. });
27. } catch (error) {
28. console.error(`setCustomCursor failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
29. }
30. });
31. }).catch((error: BusinessError) => {
32. console.error(`createPixelMap promise error: ${JSON.stringify(error, [`code`, `message`])}`);
33. });
34. });
35. })
36. }
37. }
38. }
```

## pointer.setCustomCursorSync11+

PhonePC/2in1TabletTV

setCustomCursorSync(windowId: number, pixelMap: image.PixelMap, focusX?: number, focusY?: number): void

设置指定窗口的自定义光标样式，使用同步方式进行设置。

**系统能力**：SystemCapability.MultimodalInput.Input.Pointer

**参数**：

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| windowId | number | 是 | 窗口ID。取值为大于0的整数。 |
| pixelMap | [image.PixelMap](arkts-apis-image-pixelmap.md) | 是 | 自定义光标资源。 |
| focusX | number | 否 | 自定义光标焦点x，取值范围：大于等于0，默认为0。 |
| focusY | number | 否 | 自定义光标焦点y，取值范围：大于等于0，默认为0。 |

**错误码**：

以下错误码的详细介绍请参见[通用错误码](errorcode-universal.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3. Parameter verification failed. |

**示例**：

```
1. import { pointer } from '@kit.InputKit';
2. import { image } from '@kit.ImageKit';
3. import { BusinessError } from '@kit.BasicServicesKit';
4. import { window } from '@kit.ArkUI';

6. @Entry
7. @Component
8. struct Index {
9. build() {
10. RelativeContainer() {
11. Text()
12. .onClick(() => {
13. // app_icon为示例资源，请开发者根据实际需求配置资源文件。
14. this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent(
15. $r("app.media.app_icon").id, (error: BusinessError, svgFileData: Uint8Array) => {
16. const svgBuffer = svgFileData.buffer;
17. let svgImageSource: image.ImageSource = image.createImageSource(svgBuffer);
18. let svgDecodingOptions: image.DecodingOptions = { desiredSize: { width: 50, height: 50 } };
19. svgImageSource.createPixelMap(svgDecodingOptions).then((pixelMap) => {
20. window.getLastWindow(this.getUIContext().getHostContext(), (error: BusinessError, win: window.Window) => {
21. let windowId = win.getWindowProperties().id;
22. try {
23. pointer.setCustomCursorSync(windowId, pixelMap, 25, 25);
24. console.info(`setCustomCursorSync success`);
25. } catch (error) {
26. console.error(`setCustomCursorSync failed, error: ${JSON.stringify(error, [`code`, `message`])}`);
27. }
28. });
29. }).catch((error: BusinessError) => {
30. console.error(`createPixelMap promise error: ${JSON.stringify(error, [`code`, `message`])}`);
31. });
32. });
33. }
34. )
35. }
36. }
37. }
```
