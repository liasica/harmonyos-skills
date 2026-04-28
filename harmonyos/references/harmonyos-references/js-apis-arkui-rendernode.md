---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-references/js-apis-arkui-rendernode
title: RenderNode
breadcrumb: API参考 > 应用框架 > ArkUI（方舟UI框架） > ArkTS API > UI界面 > arkui > RenderNode
category: harmonyos-references
scraped_at: 2026-04-28T08:00:40+08:00
doc_updated_at: 2026-03-27
content_hash: sha256:367b5df6a88a36ee3267b3df7f8fffd5de56509b6104a6413b9d1031ce5e302b
---

提供自绘制渲染节点RenderNode，支持开发者通过C API进行开发，完成自定义绘制需求。

说明

* 本模块首批接口从API version 11开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。
* 不建议对[BuilderNode](js-apis-arkui-buildernode.md)中的RenderNode进行修改操作。BuilderNode中持有的[FrameNode](js-apis-arkui-framenode.md)仅用于将该BuilderNode作为子节点挂载到其他FrameNode上，对该FrameNode或对应的RenderNode进行属性设置与子节点操作可能会产生未定义行为，包括但不限于显示异常、事件异常、稳定性问题等。
* RenderNode对象不支持使用JSON序列化。

## 导入模块

PhonePC/2in1TabletTVWearable

```
1. import { RenderNode } from '@kit.ArkUI';
```

## RenderNode

PhonePC/2in1TabletTVWearable

### constructor

PhonePC/2in1TabletTVWearable

constructor()

RenderNode的构造函数。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = {
5. x: 0,
6. y: 0,
7. width: 100,
8. height: 100
9. };
10. renderNode.backgroundColor = 0xffff0000;

12. // 继承NodeController实现自定义UI控制器
13. class MyNodeController extends NodeController {
14. private rootNode: FrameNode | null = null;

16. makeNode(uiContext: UIContext): FrameNode | null {
17. this.rootNode = new FrameNode(uiContext);

19. const rootRenderNode = this.rootNode.getRenderNode();
20. if (rootRenderNode !== null) {
21. rootRenderNode.appendChild(renderNode);
22. }

24. return this.rootNode;
25. }
26. }

28. @Entry
29. @Component
30. struct Index {
31. private myNodeController: MyNodeController = new MyNodeController();

33. build() {
34. Row() {
35. NodeContainer(this.myNodeController)
36. }
37. }
38. }
```

### appendChild

PhonePC/2in1TabletTVWearable

appendChild(node: RenderNode): void

在RenderNode最后一个子节点后添加新的子节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [RenderNode](js-apis-arkui-rendernode.md#rendernode-1) | 是 | 需要添加的RenderNode。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100025 | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'node' is invalid: its corresponding FrameNode cannot be adopted." |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = {
5. x: 0,
6. y: 0,
7. width: 100,
8. height: 100
9. };
10. renderNode.backgroundColor = 0xffff0000;
11. const child = new RenderNode();
12. child.frame = {
13. x: 10,
14. y: 10,
15. width: 50,
16. height: 50
17. };
18. child.backgroundColor = 0xff00ff00;
19. renderNode.appendChild(child);

21. // 继承NodeController实现自定义UI控制器
22. class MyNodeController extends NodeController {
23. private rootNode: FrameNode | null = null;

25. makeNode(uiContext: UIContext): FrameNode | null {
26. this.rootNode = new FrameNode(uiContext);

28. const rootRenderNode = this.rootNode.getRenderNode();
29. if (rootRenderNode !== null) {
30. // 在RenderNode最后一个子节点后添加新的子节点
31. rootRenderNode.appendChild(renderNode);
32. }

34. return this.rootNode;
35. }
36. }

38. @Entry
39. @Component
40. struct Index {
41. private myNodeController: MyNodeController = new MyNodeController();

43. build() {
44. Row() {
45. NodeContainer(this.myNodeController)
46. }
47. }
48. }
```

### insertChildAfter

PhonePC/2in1TabletTVWearable

insertChildAfter(child: RenderNode, sibling: RenderNode | null): void

在RenderNode指定子节点之后添加新的子节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| child | [RenderNode](js-apis-arkui-rendernode.md#rendernode-1) | 是 | 需要添加的子节点。 |
| sibling | [RenderNode](js-apis-arkui-rendernode.md#rendernode-1) | null | 是 | 新节点将插入到该节点之后。若该参数设置为空，则新节点将插入到首个子节点之前。 |

**错误码：**

以下错误码的详细介绍请参见[自定义节点错误码](errorcode-node.md)。

| 错误码ID | 错误信息 |
| --- | --- |
| 100025 | The parameter is invalid. Details about the invalid parameter and the reason are included in the error message. For example: "The parameter 'child' is invalid: its corresponding FrameNode cannot be adopted." |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = {
5. x: 0,
6. y: 0,
7. width: 200,
8. height: 350
9. };
10. renderNode.backgroundColor = 0xffff0000;
11. for (let i = 0; i < 5; i++) {
12. const node = new RenderNode();
13. node.frame = {
14. x: 10,
15. y: 10 + 60 * i,
16. width: 50,
17. height: 50
18. };
19. node.backgroundColor = 0xff00ff00;
20. renderNode.appendChild(node);
21. }

23. const child = new RenderNode();
24. child.frame = {
25. x: 70,
26. y: 70,
27. width: 50,
28. height: 50
29. };
30. child.backgroundColor = 0xffffff00;
31. const sibling = renderNode.getChild(1);
32. // 将child节点插入至sibling节点之后
33. renderNode.insertChildAfter(child, sibling);

35. // 继承NodeController实现自定义UI控制器
36. class MyNodeController extends NodeController {
37. private rootNode: FrameNode | null = null;

39. makeNode(uiContext: UIContext): FrameNode | null {
40. this.rootNode = new FrameNode(uiContext);

42. const rootRenderNode = this.rootNode.getRenderNode();
43. if (rootRenderNode !== null) {
44. rootRenderNode.appendChild(renderNode);
45. }

47. return this.rootNode;
48. }
49. }

51. @Entry
52. @Component
53. struct Index {
54. private myNodeController: MyNodeController = new MyNodeController();

56. build() {
57. Row() {
58. NodeContainer(this.myNodeController)
59. }
60. }
61. }
```

### removeChild

PhonePC/2in1TabletTVWearable

removeChild(node: RenderNode): void

从RenderNode中删除指定的子节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| node | [RenderNode](js-apis-arkui-rendernode.md#rendernode-1) | 是 | 需要删除的子节点。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = {
5. x: 0,
6. y: 0,
7. width: 200,
8. height: 350
9. };
10. renderNode.backgroundColor = 0xffff0000;
11. for (let i = 0; i < 5; i++) {
12. const node = new RenderNode();
13. node.frame = {
14. x: 10,
15. y: 10 + 60 * i,
16. width: 50,
17. height: 50
18. };
19. node.backgroundColor = 0xff00ff00;
20. renderNode.appendChild(node);
21. }

23. // 删除renderNode下序列号为1的子节点
24. const node = renderNode.getChild(1);
25. renderNode.removeChild(node);

27. // 继承NodeController实现自定义UI控制器
28. class MyNodeController extends NodeController {
29. private rootNode: FrameNode | null = null;

31. makeNode(uiContext: UIContext): FrameNode | null {
32. this.rootNode = new FrameNode(uiContext);

34. const rootRenderNode = this.rootNode.getRenderNode();
35. if (rootRenderNode !== null) {
36. rootRenderNode.appendChild(renderNode);
37. }

39. return this.rootNode;
40. }
41. }

43. @Entry
44. @Component
45. struct Index {
46. private myNodeController: MyNodeController = new MyNodeController();

48. build() {
49. Row() {
50. NodeContainer(this.myNodeController)
51. }
52. }
53. }
```

### clearChildren

PhonePC/2in1TabletTVWearable

clearChildren(): void

清除当前RenderNode的所有子节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.size = { width: 200, height: 300 };
5. for (let i = 0; i < 10; i++) {
6. let childNode = new RenderNode();
7. childNode.size = { width: i * 10, height: i * 10 };
8. childNode.position = { x: i * 10, y: i * 10 };
9. childNode.backgroundColor = 0xFF0000FF - 0X11 * i;
10. renderNode.appendChild(childNode);
11. }

13. // 继承NodeController实现自定义UI控制器
14. class MyNodeController extends NodeController {
15. private rootNode: FrameNode | null = null;

17. makeNode(uiContext: UIContext): FrameNode | null {
18. this.rootNode = new FrameNode(uiContext);

20. const rootRenderNode = this.rootNode.getRenderNode();
21. if (rootRenderNode !== null) {
22. rootRenderNode.appendChild(renderNode);
23. }

25. return this.rootNode;
26. }
27. }

29. @Entry
30. @Component
31. struct Index {
32. private myNodeController: MyNodeController = new MyNodeController();

34. build() {
35. Column() {
36. NodeContainer(this.myNodeController)
37. .borderWidth(1)
38. .width(200)
39. .height(300)
40. Button("clearChildren")
41. .onClick(() => {
42. renderNode.clearChildren(); // 清除renderNode的所有子节点
43. })
44. }.width("100%")
45. }
46. }
```

### getChild

PhonePC/2in1TabletTVWearable

getChild(index: number): RenderNode | null

获取当前RenderNode指定位置的子节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| index | number | 是 | 需要查询的子节点的序列号。 |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RenderNode](js-apis-arkui-rendernode.md#rendernode-1) | null | 子节点。若该RenderNode不包含所查询的子节点，则返回空对象null。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.size = { width: 200, height: 300 };
5. for (let i = 0; i < 10; i++) {
6. let childNode = new RenderNode();
7. childNode.size = { width: i * 10, height: i * 10 };
8. childNode.position = { x: i * 10, y: i * 10 };
9. childNode.backgroundColor = 0xFF0000FF - 0X11 * i;
10. renderNode.appendChild(childNode);
11. }

13. // 继承NodeController实现自定义UI控制器
14. class MyNodeController extends NodeController {
15. private rootNode: FrameNode | null = null;

17. makeNode(uiContext: UIContext): FrameNode | null {
18. this.rootNode = new FrameNode(uiContext);

20. const rootRenderNode = this.rootNode.getRenderNode();
21. if (rootRenderNode !== null) {
22. rootRenderNode.appendChild(renderNode);
23. }

25. return this.rootNode;
26. }
27. }

29. @Entry
30. @Component
31. struct Index {
32. private myNodeController: MyNodeController = new MyNodeController();

34. build() {
35. Column() {
36. NodeContainer(this.myNodeController)
37. .borderWidth(1)
38. .width(200)
39. .height(300)
40. Button("getChild")
41. .onClick(() => {
42. for (let i = 0; i < 11; i++) {
43. let childNode: RenderNode | null = renderNode.getChild(i);
44. if (childNode == null) {
45. // renderNode不存在序列号为10的子节点，此时返回null
46. console.error(`the ${i} of renderNode's childNode is null`);
47. } else {
48. // 正常获取子节点并打印节点属性
49. console.info(`the ${i} of renderNode's childNode has a size of {${childNode.size.width},${childNode.size.height}}`);
50. }
51. }

53. })
54. }.width("100%")
55. }
56. }
```

### getFirstChild

PhonePC/2in1TabletTVWearable

getFirstChild(): RenderNode | null

获取当前RenderNode的第一个子节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RenderNode](js-apis-arkui-rendernode.md#rendernode-1) | null | 首个子节点。若该RenderNode不包含子节点，则返回空对象null。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = {
5. x: 0,
6. y: 0,
7. width: 200,
8. height: 350
9. };
10. renderNode.backgroundColor = 0xffff0000;
11. for (let i = 0; i < 5; i++) {
12. const node = new RenderNode();
13. node.frame = {
14. x: 10,
15. y: 10 + 60 * i,
16. width: 50,
17. height: 50
18. };
19. node.backgroundColor = 0xff00ff00;
20. renderNode.appendChild(node);
21. }

23. // 继承NodeController实现自定义UI控制器
24. class MyNodeController extends NodeController {
25. private rootNode: FrameNode | null = null;

27. makeNode(uiContext: UIContext): FrameNode | null {
28. this.rootNode = new FrameNode(uiContext);

30. const rootRenderNode = this.rootNode.getRenderNode();
31. if (rootRenderNode !== null) {
32. rootRenderNode.appendChild(renderNode);
33. }

35. return this.rootNode;
36. }
37. }

39. @Entry
40. @Component
41. struct Index {
42. private myNodeController: MyNodeController = new MyNodeController();

44. build() {
45. Row() {
46. NodeContainer(this.myNodeController)
47. .width(200)
48. .height(350)
49. Button('getFirstChild')
50. .onClick(() => {
51. // 获取renderNode的首个子节点
52. const firstChild = renderNode.getFirstChild();
53. if (firstChild === null) {
54. console.error('the fist child is null');
55. } else {
56. console.info(`the position of fist child is x: ${firstChild.position.x}, y: ${firstChild.position.y}`);
57. }
58. })
59. }
60. }
61. }
```

### getNextSibling

PhonePC/2in1TabletTVWearable

getNextSibling(): RenderNode | null

获取当前RenderNode的下一个同级节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RenderNode](js-apis-arkui-rendernode.md#rendernode-1) | null | 当前RenderNode的下一个同级节点。若该RenderNode不包含下一个同级节点，则返回空对象null。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = {
5. x: 0,
6. y: 0,
7. width: 200,
8. height: 350
9. };
10. renderNode.backgroundColor = 0xffff0000;
11. for (let i = 0; i < 5; i++) {
12. const node = new RenderNode();
13. node.frame = {
14. x: 10,
15. y: 10 + 60 * i,
16. width: 50,
17. height: 50
18. };
19. node.backgroundColor = 0xff00ff00;
20. renderNode.appendChild(node);
21. }

23. // 继承NodeController实现自定义UI控制器
24. class MyNodeController extends NodeController {
25. private rootNode: FrameNode | null = null;

27. makeNode(uiContext: UIContext): FrameNode | null {
28. this.rootNode = new FrameNode(uiContext);

30. const rootRenderNode = this.rootNode.getRenderNode();
31. if (rootRenderNode !== null) {
32. rootRenderNode.appendChild(renderNode);
33. }

35. return this.rootNode;
36. }
37. }

39. @Entry
40. @Component
41. struct Index {
42. private myNodeController: MyNodeController = new MyNodeController();

44. build() {
45. Row() {
46. NodeContainer(this.myNodeController)
47. .width(200)
48. .height(350)
49. Button('getNextSibling')
50. .onClick(() => {
51. const child = renderNode.getChild(1);
52. // 获取renderNode序列号为1的子节点后，再获取它的下一个同级节点
53. const nextSibling = child!.getNextSibling()
54. if (nextSibling === null || child === null) {
55. console.error('the child or nextChild is null');
56. } else {
57. console.info(`the position of child is x: ${child.position.x}, y: ${child.position.y}, the position of nextSibling is x: ${nextSibling.position.x}, y: ${nextSibling.position.y}`);
58. }
59. })
60. }
61. }
62. }
```

### getPreviousSibling

PhonePC/2in1TabletTVWearable

getPreviousSibling(): RenderNode | null

获取当前RenderNode的上一个同级节点。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [RenderNode](js-apis-arkui-rendernode.md#rendernode-1) | null | 当前RenderNode的上一个同级节点。若该RenderNode不包含上一个同级节点，则返回空对象null。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = {
5. x: 0,
6. y: 0,
7. width: 200,
8. height: 350
9. };
10. renderNode.backgroundColor = 0xffff0000;
11. for (let i = 0; i < 5; i++) {
12. const node = new RenderNode();
13. node.frame = {
14. x: 10,
15. y: 10 + 60 * i,
16. width: 50,
17. height: 50
18. };
19. node.backgroundColor = 0xff00ff00;
20. renderNode.appendChild(node);
21. }

23. // 继承NodeController实现自定义UI控制器
24. class MyNodeController extends NodeController {
25. private rootNode: FrameNode | null = null;

27. makeNode(uiContext: UIContext): FrameNode | null {
28. this.rootNode = new FrameNode(uiContext);

30. const rootRenderNode = this.rootNode.getRenderNode();
31. if (rootRenderNode !== null) {
32. rootRenderNode.appendChild(renderNode);
33. }

35. return this.rootNode;
36. }
37. }

39. @Entry
40. @Component
41. struct Index {
42. private myNodeController: MyNodeController = new MyNodeController();

44. build() {
45. Row() {
46. NodeContainer(this.myNodeController)
47. .width(200)
48. .height(350)
49. Button('getPreviousSibling')
50. .onClick(() => {
51. const child = renderNode.getChild(1);
52. // 获取renderNode序列号为1的子节点后，再获取它的上一个同级节点
53. const previousSibling = child!.getPreviousSibling()
54. if (child === null || previousSibling === null) {
55. console.error('the child or previousChild is null');
56. } else {
57. console.info(`the position of child is x: ${child.position.x}, y: ${child.position.y}, the position of previousSibling is x: ${previousSibling.position.x}, y: ${previousSibling.position.y}`);
58. }
59. })
60. }
61. }
62. }
```

### backgroundColor

PhonePC/2in1TabletTVWearable

set backgroundColor(color: number)

设置当前RenderNode的背景颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | number | 是 | 背景颜色值，ARGB格式，示例：0xE5E5E5。 |

get backgroundColor(): number

获取当前RenderNode的背景颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前RenderNode的背景颜色，默认值为0X00000000。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = { x: 0, y: 0, width: 100, height: 100 };
5. // 设置renderNode的背景颜色
6. renderNode.backgroundColor = 0XFF00FF00;
7. // 获取renderNode的背景颜色
8. const backgroundColor = renderNode.backgroundColor;

10. // 继承NodeController实现自定义UI控制器
11. class MyNodeController extends NodeController {
12. private rootNode: FrameNode | null = null;

14. makeNode(uiContext: UIContext): FrameNode | null {
15. this.rootNode = new FrameNode(uiContext);

17. const rootRenderNode = this.rootNode.getRenderNode();
18. if (rootRenderNode !== null) {
19. rootRenderNode.appendChild(renderNode);
20. }

22. return this.rootNode;
23. }
24. }

26. @Entry
27. @Component
28. struct Index {
29. private myNodeController: MyNodeController = new MyNodeController();
30. build() {
31. Row() {
32. NodeContainer(this.myNodeController)
33. }
34. }
35. }
```

### clipToFrame

PhonePC/2in1TabletTVWearable

set clipToFrame(useClip: boolean)

设置是否对当前RenderNode剪裁。若设置为true，则超出该RenderNode大小的部分将会被截断。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| useClip | boolean | 是 | 设置是否进行剪裁。  true表示对当前RenderNode剪裁，false表示不对当前RenderNode剪裁。 |

get clipToFrame(): boolean

获取当前RenderNode是否需要进行剪裁。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 获取当前RenderNode是否需要进行剪裁，默认值为true。  true表示对当前RenderNode剪裁，false表示不对当前RenderNode剪裁。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = { x: 0, y: 0, width: 100, height: 100 };
5. renderNode.backgroundColor = 0xffff0000;
6. // 设置renderNode是否需要剪裁
7. renderNode.clipToFrame = true;
8. // 获取renderNode是否需要剪裁
9. const clipToFrame = renderNode.clipToFrame;

11. const childNode = new RenderNode();
12. childNode.frame = { x: 10, y: 10, width: 150, height: 50 };
13. childNode.backgroundColor = 0xffffff00;
14. renderNode.appendChild(childNode);

16. // 继承NodeController实现自定义UI控制器
17. class MyNodeController extends NodeController {
18. private rootNode: FrameNode | null = null;

20. makeNode(uiContext: UIContext): FrameNode | null {
21. this.rootNode = new FrameNode(uiContext);

23. const rootRenderNode = this.rootNode.getRenderNode();
24. if (rootRenderNode !== null) {
25. rootRenderNode.appendChild(renderNode);
26. }

28. return this.rootNode;
29. }
30. }

32. @Entry
33. @Component
34. struct Index {
35. private myNodeController: MyNodeController = new MyNodeController();

37. build() {
38. Row() {
39. NodeContainer(this.myNodeController)
40. }
41. }
42. }
```

### opacity

PhonePC/2in1TabletTVWearable

set opacity(value: number)

设置当前RenderNode的不透明度。若输入的数值小于0，会被视为0。若输入的数值大于1，会被视为1。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| value | number | 是 | 将要设置的不透明度，数据范围为[0, 1]，值越大透明度越低。 |

get opacity(): number

获取当前RenderNode的不透明度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 获取当前RenderNode的不透明度，默认值为1，不透明。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = { x: 0, y: 0, width: 100, height: 100 };
5. renderNode.backgroundColor = 0xffff0000;
6. // 设置renderNode的不透明度
7. renderNode.opacity = 0.5;
8. // 获取renderNode的不透明度
9. const opacity = renderNode.opacity;

11. // 继承NodeController实现自定义UI控制器
12. class MyNodeController extends NodeController {
13. private rootNode: FrameNode | null = null;

15. makeNode(uiContext: UIContext): FrameNode | null {
16. this.rootNode = new FrameNode(uiContext);

18. const rootRenderNode = this.rootNode.getRenderNode();
19. if (rootRenderNode !== null) {
20. rootRenderNode.appendChild(renderNode);
21. }

23. return this.rootNode;
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. private myNodeController: MyNodeController = new MyNodeController();

32. build() {
33. Row() {
34. NodeContainer(this.myNodeController)
35. }
36. }
37. }
```

### size

PhonePC/2in1TabletTVWearable

set size(size: Size)

设置当前RenderNode的大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| size | [Size](js-apis-arkui-graphics.md#size) | 是 | 将要设置的RenderNode的大小。 |

get size(): Size

获取当前RenderNode的大小。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Size](js-apis-arkui-graphics.md#size) | 获取当前RenderNode的大小，默认值宽度和高度为0。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.backgroundColor = 0xffff0000;
5. // 设置renderNode的大小
6. renderNode.size = { width: 100, height: 100 };
7. // 获取renderNode的大小
8. const size = renderNode.size;

10. // 继承NodeController实现自定义UI控制器
11. class MyNodeController extends NodeController {
12. private rootNode: FrameNode | null = null;

14. makeNode(uiContext: UIContext): FrameNode | null {
15. this.rootNode = new FrameNode(uiContext);

17. const rootRenderNode = this.rootNode.getRenderNode();
18. if (rootRenderNode !== null) {
19. rootRenderNode.appendChild(renderNode);
20. }

22. return this.rootNode;
23. }
24. }

26. @Entry
27. @Component
28. struct Index {
29. private myNodeController: MyNodeController = new MyNodeController();

31. build() {
32. Row() {
33. NodeContainer(this.myNodeController)
34. }
35. }
36. }
```

### position

PhonePC/2in1TabletTVWearable

set position(position: Position)

设置当前RenderNode的位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| position | [Position](js-apis-arkui-graphics.md#position) | 是 | 将要设置的RenderNode的位置。 |

get position(): Position

获取当前RenderNode的位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Position](js-apis-arkui-graphics.md#position) | 获取当前RenderNode的位置，默认位置为{ x: 0, y: 0 }。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.backgroundColor = 0xffff0000;
5. renderNode.size = { width: 100, height: 100 };
6. // 设置renderNode的位置
7. renderNode.position = { x: 10, y: 10 };
8. // 获取renderNode的位置
9. const position = renderNode.position;

11. // 继承NodeController实现自定义UI控制器
12. class MyNodeController extends NodeController {
13. private rootNode: FrameNode | null = null;

15. makeNode(uiContext: UIContext): FrameNode | null {
16. this.rootNode = new FrameNode(uiContext);

18. const rootRenderNode = this.rootNode.getRenderNode();
19. if (rootRenderNode !== null) {
20. rootRenderNode.appendChild(renderNode);
21. }

23. return this.rootNode;
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. private myNodeController: MyNodeController = new MyNodeController();

32. build() {
33. Row() {
34. NodeContainer(this.myNodeController)
35. }
36. }
37. }
```

### frame

PhonePC/2in1TabletTVWearable

set frame(frame: Frame)

设置当前RenderNode的大小和位置。当和[position](js-apis-arkui-rendernode.md#position)、[size](js-apis-arkui-rendernode.md#size)同时使用时，以后设置的为准。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| frame | [Frame](js-apis-arkui-graphics.md#frame) | 是 | 将要设置的RenderNode的大小和位置。 |

get frame(): Frame

获取当前RenderNode的大小和位置。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Frame](js-apis-arkui-rendernode.md#frame) | 获取当前RenderNode的大小和位置，默认值为{ x: 0, y: 0, width: 0, height: 0 }。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.backgroundColor = 0xffff0000;
5. // 设置renderNode的大小和位置
6. renderNode.frame = { x: 10, y: 10, width: 100, height: 100 };
7. // 获取renderNode的大小和位置
8. const frame = renderNode.frame;

10. // 继承NodeController实现自定义UI控制器
11. class MyNodeController extends NodeController {
12. private rootNode: FrameNode | null = null;

14. makeNode(uiContext: UIContext): FrameNode | null {
15. this.rootNode = new FrameNode(uiContext);

17. const rootRenderNode = this.rootNode.getRenderNode();
18. if (rootRenderNode !== null) {
19. rootRenderNode.appendChild(renderNode);
20. }

22. return this.rootNode;
23. }
24. }

26. @Entry
27. @Component
28. struct Index {
29. private myNodeController: MyNodeController = new MyNodeController();

31. build() {
32. Row() {
33. NodeContainer(this.myNodeController)
34. }
35. }
36. }
```

### pivot

PhonePC/2in1TabletTVWearable

set pivot(pivot: Pivot)

设置当前RenderNode的轴心，影响RenderNode的缩放和旋转效果。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| pivot | [Pivot](js-apis-arkui-graphics.md#pivot) | 是 | 将要设置的RenderNode的轴心。 |

get pivot(): Pivot

获取当前RenderNode的轴心。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Pivot](js-apis-arkui-graphics.md#pivot) | 获取当前RenderNode的轴心，默认值为{ x: 0.5, y: 0.5}。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.backgroundColor = 0xffff0000;
5. renderNode.frame = { x: 10, y: 10, width: 100, height: 100 };
6. // 设置renderNode的轴心
7. renderNode.pivot = { x: 0.5, y: 0.6 };
8. // 获取renderNode的轴心
9. const pivot = renderNode.pivot;

11. renderNode.rotation = { x: 15, y: 0, z: 0 };

13. // 继承NodeController实现自定义UI控制器
14. class MyNodeController extends NodeController {
15. private rootNode: FrameNode | null = null;

17. makeNode(uiContext: UIContext): FrameNode | null {
18. this.rootNode = new FrameNode(uiContext);

20. const rootRenderNode = this.rootNode.getRenderNode();
21. if (rootRenderNode !== null) {
22. rootRenderNode.appendChild(renderNode);
23. }

25. return this.rootNode;
26. }
27. }

29. @Entry
30. @Component
31. struct Index {
32. private myNodeController: MyNodeController = new MyNodeController();

34. build() {
35. Row() {
36. NodeContainer(this.myNodeController)
37. }
38. }
39. }
```

### scale

PhonePC/2in1TabletTVWearable

set scale(scale: Scale)

设置当前RenderNode的比例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| scale | [Scale](js-apis-arkui-graphics.md#scale) | 是 | 将要设置的RenderNode的缩放比例。 |

get scale(): Scale

获取当前RenderNode的比例。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Scale](js-apis-arkui-graphics.md#scale) | 获取当前RenderNode的比例，默认值为{ x: 1, y: 1 }。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.backgroundColor = 0xffff0000;
5. renderNode.frame = { x: 10, y: 10, width: 100, height: 100 };
6. // 设置renderNode的比例
7. renderNode.scale = { x: 0.5, y: 1 };
8. // 获取renderNode的比例
9. const scale = renderNode.scale;

11. // 继承NodeController实现自定义UI控制器
12. class MyNodeController extends NodeController {
13. private rootNode: FrameNode | null = null;

15. makeNode(uiContext: UIContext): FrameNode | null {
16. this.rootNode = new FrameNode(uiContext);

18. const rootRenderNode = this.rootNode.getRenderNode();
19. if (rootRenderNode !== null) {
20. rootRenderNode.appendChild(renderNode);
21. }

23. return this.rootNode;
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. private myNodeController: MyNodeController = new MyNodeController();

32. build() {
33. Row() {
34. NodeContainer(this.myNodeController)
35. }
36. }
37. }
```

### translation

PhonePC/2in1TabletTVWearable

set translation(translation: Translation)

设置当前RenderNode的平移量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| translation | [Translation](js-apis-arkui-graphics.md#translation) | 是 | 将要设置的RenderNode的平移量。 |

get translation(): Translation

获取当前RenderNode的平移量。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Translation](js-apis-arkui-graphics.md#translation) | 获取当前RenderNode的平移量，默认值为{ x: 0, y: 0 }。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.backgroundColor = 0xffff0000;
5. renderNode.frame = { x: 10, y: 10, width: 100, height: 100 };
6. // 设置renderNode的平移量
7. renderNode.translation = { x: 100, y: 0 };
8. // 获取renderNode的平移量
9. const translation = renderNode.translation;

11. // 继承NodeController实现自定义UI控制器
12. class MyNodeController extends NodeController {
13. private rootNode: FrameNode | null = null;

15. makeNode(uiContext: UIContext): FrameNode | null {
16. this.rootNode = new FrameNode(uiContext);

18. const rootRenderNode = this.rootNode.getRenderNode();
19. if (rootRenderNode !== null) {
20. rootRenderNode.appendChild(renderNode);
21. }

23. return this.rootNode;
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. private myNodeController: MyNodeController = new MyNodeController();

32. build() {
33. Row() {
34. NodeContainer(this.myNodeController)
35. }
36. }
37. }
```

### rotation

PhonePC/2in1TabletTVWearable

set rotation(rotation: Rotation)

设置当前RenderNode的旋转角度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| rotation | [Rotation](js-apis-arkui-graphics.md#rotation) | 是 | 将要设置的RenderNode的旋转角度。 |

get rotation(): Rotation

获取当前RenderNode的旋转角度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Rotation](js-apis-arkui-graphics.md#rotation) | 当前RenderNode的旋转角度。默认值为{ x: 0, y: 0, z: 0}。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.backgroundColor = 0xffff0000;
5. renderNode.frame = { x: 10, y: 10, width: 100, height: 100 };
6. // 设置renderNode的旋转角度
7. renderNode.rotation = { x: 45, y: 0, z: 0 };
8. // 获取renderNode的旋转角度
9. const rotation = renderNode.rotation;

11. // 继承NodeController实现自定义UI控制器
12. class MyNodeController extends NodeController {
13. private rootNode: FrameNode | null = null;

15. makeNode(uiContext: UIContext): FrameNode | null {
16. this.rootNode = new FrameNode(uiContext);

18. const rootRenderNode = this.rootNode.getRenderNode();
19. if (rootRenderNode !== null) {
20. rootRenderNode.appendChild(renderNode);
21. }

23. return this.rootNode;
24. }
25. }

27. @Entry
28. @Component
29. struct Index {
30. private myNodeController: MyNodeController = new MyNodeController();

32. build() {
33. Row() {
34. NodeContainer(this.myNodeController)
35. }
36. }
37. }
```

### transform

PhonePC/2in1TabletTVWearable

set transform(transform: Matrix4)

设置当前RenderNode的变换矩阵。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| transform | [Matrix4](js-apis-arkui-graphics.md#matrix4) | 是 | 将要设置的RenderNode的变换矩阵。 |

get transform(): Matrix4

获取当前RenderNode的变换矩阵。默认值为：

```
1. [
2. 1, 0, 0, 0,
3. 0, 1, 0, 0,
4. 0, 0, 1, 0,
5. 0, 0, 0, 1
6. ]
```

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Matrix4](js-apis-arkui-graphics.md#matrix4) | 当前RenderNode的变换矩阵。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.backgroundColor = 0xffff0000;
5. renderNode.frame = { x: 10, y: 10, width: 100, height: 100 };
6. // 设置renderNode的变换矩阵
7. renderNode.transform = [
8. 1, 0, 0, 0,
9. 0, 2, 0, 0,
10. 0, 0, 1, 0,
11. 0, 0, 0, 1
12. ];
13. // 获取renderNode的变换矩阵
14. const transform = renderNode.transform;

16. // 继承NodeController实现自定义UI控制器
17. class MyNodeController extends NodeController {
18. private rootNode: FrameNode | null = null;

20. makeNode(uiContext: UIContext): FrameNode | null {
21. this.rootNode = new FrameNode(uiContext);

23. const rootRenderNode = this.rootNode.getRenderNode();
24. if (rootRenderNode !== null) {
25. rootRenderNode.appendChild(renderNode);
26. }

28. return this.rootNode;
29. }
30. }

32. @Entry
33. @Component
34. struct Index {
35. private myNodeController: MyNodeController = new MyNodeController();

37. build() {
38. Row() {
39. NodeContainer(this.myNodeController)
40. }
41. }
42. }
```

### shadowColor

PhonePC/2in1TabletTVWearable

set shadowColor(color: number)

设置当前RenderNode的阴影颜色，ARGB格式。若设置了[shadowAlpha](js-apis-arkui-rendernode.md#shadowalpha)，则不透明度以shadowAlpha为准。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | number | 是 | 将要设置的RenderNode的阴影颜色，ARGB格式。  取值范围是符合ARGB格式的颜色。 |

get shadowColor(): number

获取当前RenderNode的阴影颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前RenderNode的阴影颜色，ARGB格式，默认值为0X00000000。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.backgroundColor = 0xffff0000;
5. renderNode.frame = { x: 10, y: 10, width: 100, height: 100 };
6. renderNode.shadowElevation = 10;
7. // 设置renderNode的阴影颜色
8. renderNode.shadowColor = 0XFF00FF00;
9. // 获取renderNode的阴影颜色
10. const shadowColor = renderNode.shadowColor;

12. // 继承NodeController实现自定义UI控制器
13. class MyNodeController extends NodeController {
14. private rootNode: FrameNode | null = null;

16. makeNode(uiContext: UIContext): FrameNode | null {
17. this.rootNode = new FrameNode(uiContext);

19. const rootRenderNode = this.rootNode.getRenderNode();
20. if (rootRenderNode !== null) {
21. rootRenderNode.appendChild(renderNode);
22. }

24. return this.rootNode;
25. }
26. }

28. @Entry
29. @Component
30. struct Index {
31. private myNodeController: MyNodeController = new MyNodeController();

33. build() {
34. Row() {
35. NodeContainer(this.myNodeController)
36. }
37. }
38. }
```

### shadowOffset

PhonePC/2in1TabletTVWearable

set shadowOffset(offset: Offset)

设置当前RenderNode的阴影偏移。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| offset | [Offset](js-apis-arkui-graphics.md#offset) | 是 | 将要设置的RenderNode的阴影偏移。 |

get shadowOffset(): Offset

获取当前RenderNode的阴影偏移。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Offset](js-apis-arkui-graphics.md#offset) | 当前RenderNode的阴影偏移，默认值为{ x: 0, y: 0 }。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.backgroundColor = 0xffff0000;
5. renderNode.frame = { x: 10, y: 10, width: 100, height: 100 };
6. renderNode.shadowElevation = 10;
7. renderNode.shadowColor = 0XFF00FF00;
8. // 设置renderNode的阴影偏移
9. renderNode.shadowOffset = { x: 10, y: 10 };
10. // 获取renderNode的阴影偏移
11. const shadowOffset = renderNode.shadowOffset;

13. // 继承NodeController实现自定义UI控制器
14. class MyNodeController extends NodeController {
15. private rootNode: FrameNode | null = null;

17. makeNode(uiContext: UIContext): FrameNode | null {
18. this.rootNode = new FrameNode(uiContext);

20. const rootRenderNode = this.rootNode.getRenderNode();
21. if (rootRenderNode !== null) {
22. rootRenderNode.appendChild(renderNode);
23. }

25. return this.rootNode;
26. }
27. }

29. @Entry
30. @Component
31. struct Index {
32. private myNodeController: MyNodeController = new MyNodeController();

34. build() {
35. Row() {
36. NodeContainer(this.myNodeController)
37. }
38. }
39. }
```

### label12+

PhonePC/2in1TabletTVWearable

set label(label: string)

设置当前RenderNode的标签。若当前节点是通过new创建的RenderNode，则设置的标签信息会在节点Inspector信息的属性中。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| label | string | 是 | 将要设置的RenderNode的标签。 |

get label(): string

获取当前RenderNode的标签。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| string | 当前RenderNode的标签，默认值为""。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController, UIContext } from '@kit.ArkUI';

3. // 继承NodeController实现自定义UI控制器
4. class MyNodeController extends NodeController {
5. private rootNode: FrameNode | null = null;

7. makeNode(uiContext: UIContext): FrameNode | null {
8. this.rootNode = new FrameNode(uiContext);
9. const renderNode: RenderNode | null = this.rootNode.getRenderNode();
10. if (renderNode !== null) {
11. const renderChildNode: RenderNode = new RenderNode();
12. renderChildNode.frame = { x: 0, y: 0, width: 100, height: 100 };
13. renderChildNode.backgroundColor = 0xffff0000;
14. // 设置renderNode的标签
15. renderChildNode.label = 'customRenderChildNode';
16. // 获取renderNode的标签并打印日志
17. console.info('label:', renderChildNode.label);
18. renderNode.appendChild(renderChildNode);
19. }

21. return this.rootNode;
22. }
23. }

25. @Entry
26. @Component
27. struct Index {
28. private myNodeController: MyNodeController = new MyNodeController();

30. build() {
31. Column() {
32. NodeContainer(this.myNodeController)
33. .width(300)
34. .height(700)
35. .backgroundColor(Color.Gray)
36. }
37. }
38. }
```

### shadowAlpha

PhonePC/2in1TabletTVWearable

set shadowAlpha(alpha: number)

设置当前RenderNode的阴影颜色的Alpha值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| alpha | number | 是 | 将要设置的RenderNode的阴影颜色的Alpha值。  取值范围是alpha值。 |

get shadowAlpha(): number

获取当前RenderNode的阴影颜色的Alpha值。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前RenderNode的阴影颜色的Alpha值，默认值为0。 |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.backgroundColor = 0xffff0000;
5. renderNode.frame = { x: 10, y: 10, width: 100, height: 100 };
6. renderNode.shadowElevation = 10;
7. renderNode.shadowColor = 0XFF00FF00;
8. renderNode.shadowOffset = { x: 10, y: 10 };
9. // 设置renderNode的阴影颜色Alpha值
10. renderNode.shadowAlpha = 0.1;
11. // 获取renderNode的阴影颜色Alpha值
12. const shadowAlpha = renderNode.shadowAlpha;

14. // 继承NodeController实现自定义UI控制器
15. class MyNodeController extends NodeController {
16. private rootNode: FrameNode | null = null;

18. makeNode(uiContext: UIContext): FrameNode | null {
19. this.rootNode = new FrameNode(uiContext);

21. const rootRenderNode = this.rootNode.getRenderNode();
22. if (rootRenderNode !== null) {
23. rootRenderNode.appendChild(renderNode);
24. }

26. return this.rootNode;
27. }
28. }

30. @Entry
31. @Component
32. struct Index {
33. private myNodeController: MyNodeController = new MyNodeController();

35. build() {
36. Row() {
37. NodeContainer(this.myNodeController)
38. }
39. }
40. }
```

### shadowElevation

PhonePC/2in1TabletTVWearable

set shadowElevation(elevation: number)

设置当前RenderNode的阴影的光照高度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| elevation | number | 是 | 将要设置的RenderNode的光照高度。  取值范围：[0, +∞) |

get shadowElevation(): number

获取当前RenderNode的阴影的光照高度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前RenderNode的阴影高度，默认值为0。  取值范围：[0, +∞) |

**示例：**

```
1. import {  RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.backgroundColor = 0xffff0000;
5. renderNode.frame = { x: 0, y: 0, width: 100, height: 100 };
6. renderNode.shadowOffset = { x: 10, y: 10 };
7. renderNode.shadowAlpha = 0.7;
8. // 设置renderNode的阴影光照高度
9. renderNode.shadowElevation = 30;
10. // 获取renderNode的阴影光照高度
11. const shadowElevation = renderNode.shadowElevation;

13. // 继承NodeController实现自定义UI控制器
14. class MyNodeController extends NodeController {
15. private rootNode: FrameNode | null = null;

17. makeNode(uiContext: UIContext): FrameNode | null {
18. this.rootNode = new FrameNode(uiContext);

20. const rootRenderNode = this.rootNode.getRenderNode();
21. if (rootRenderNode !== null) {
22. rootRenderNode.appendChild(renderNode);
23. }

25. return this.rootNode;
26. }
27. }

29. @Entry
30. @Component
31. struct Index {
32. private myNodeController: MyNodeController = new MyNodeController();

34. build() {
35. Row() {
36. NodeContainer(this.myNodeController)
37. }
38. }
39. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/28/v3/sr-JhwXDTc-3mmqaDZJ3TA/zh-cn_image_0000002552959456.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000035Z&HW-CC-Expire=86400&HW-CC-Sign=CA4DBEAF6B2C413CB52C8B451DE8EDE8E886E97D3FC394745DCE432E6509F7FF)

### shadowRadius

PhonePC/2in1TabletTVWearable

set shadowRadius(radius: number)

设置当前RenderNode的阴影模糊半径。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | number | 是 | 将要设置的RenderNode的阴影模糊半径。  取值范围：[0, +∞) |

get shadowRadius(): number

获取当前RenderNode的阴影模糊半径。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| number | 当前RenderNode的阴影模糊半径，默认值为0。  取值范围：[0, +∞) |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.backgroundColor = 0xff0000ff;
5. renderNode.frame = {
6. x: 100,
7. y: 100,
8. width: 100,
9. height: 100
10. };
11. renderNode.shadowOffset = { x: 10, y: 10 };
12. renderNode.shadowAlpha = 0.7;
13. // 设置renderNode的阴影模糊半径
14. renderNode.shadowRadius = 30;
15. // 获取renderNode的阴影模糊半径
16. const shadowRadius = renderNode.shadowRadius;
17. console.info(`FrameNode ${shadowRadius}`);

19. // 继承NodeController实现自定义UI控制器
20. class MyNodeController extends NodeController {
21. private rootNode: FrameNode | null = null;

23. makeNode(uiContext: UIContext): FrameNode | null {
24. this.rootNode = new FrameNode(uiContext);

26. const rootRenderNode = this.rootNode.getRenderNode();
27. if (rootRenderNode !== null) {
28. rootRenderNode.appendChild(renderNode);
29. }

31. return this.rootNode;
32. }
33. }

35. @Entry
36. @Component
37. struct Index {
38. private myNodeController: MyNodeController = new MyNodeController();

40. build() {
41. Row() {
42. NodeContainer(this.myNodeController)
43. }
44. }
45. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/fADzuLoGTY-uDnR8eUFuBg/zh-cn_image_0000002583479457.jpg?HW-CC-KV=V1&HW-CC-Date=20260428T000035Z&HW-CC-Expire=86400&HW-CC-Sign=E0B8ACE383657A57FC0F906D7875CABE339A962E2AA257479CC7081A34671CAA)

### draw

PhonePC/2in1TabletTVWearable

draw(context: DrawContext): void

绘制方法，需要开发者进行实现。该方法会在RenderNode进行绘制时被调用。

该接口的[DrawContext](js-apis-arkui-graphics.md#drawcontext)中的Canvas是用于记录指令的临时Canvas，并非节点的真实Canvas。使用请参见[调整自定义绘制Canvas的变换矩阵](../harmonyos-guides/arkts-user-defined-arktsnode-rendernode.md#调整自定义绘制canvas的变换矩阵)。

说明

RenderNode初始化时，会调用两次draw方法。第一次调用是在首次创建FrameNode时触发Render流程，第二次调用是在首次设置modifier时触发绘制。后续绘制流程皆由modifier触发。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| context | [DrawContext](js-apis-arkui-graphics.md#drawcontext) | 是 | 图形绘制上下文。 |

**示例：**

ArkTS侧代码：

```
1. // Index.ets
2. import bridge from "libentry.so"; // 该 so 由开发者通过 NAPI 编写并生成
3. import { RenderNode, FrameNode, NodeController, DrawContext } from '@kit.ArkUI';

5. // 继承RenderNode，实现自定义绘制方法
6. class MyRenderNode extends RenderNode {
7. uiContext: UIContext;

9. constructor(uiContext: UIContext) {
10. super();
11. this.uiContext = uiContext;
12. }

14. // 绘制RenderNode时调用此函数
15. draw(context: DrawContext) {
16. // 需要将 context 中的宽度和高度从vp转换为px
17. bridge.nativeOnDraw(0, context, this.uiContext.vp2px(context.size.height), this.uiContext.vp2px(context.size.width));
18. }
19. }

21. // 继承NodeController实现自定义UI控制器
22. class MyNodeController extends NodeController {
23. private rootNode: FrameNode | null = null;

25. makeNode(uiContext: UIContext): FrameNode | null {
26. this.rootNode = new FrameNode(uiContext);

28. const rootRenderNode = this.rootNode.getRenderNode();
29. if (rootRenderNode !== null) {
30. const renderNode = new MyRenderNode(uiContext);
31. renderNode.size = { width: 100, height: 100 }
32. rootRenderNode.appendChild(renderNode);
33. }

35. return this.rootNode;
36. }
37. }

39. @Entry
40. @Component
41. struct Index {
42. private myNodeController: MyNodeController = new MyNodeController();
43. build() {
44. Row() {
45. NodeContainer(this.myNodeController)
46. }
47. }
48. }
```

C++侧可通过NAPI来获取Canvas，并进行后续的自定义绘制操作。

```
1. // native_bridge.cpp
2. #include "napi/native_api.h"
3. #include <native_drawing/drawing_canvas.h>
4. #include <native_drawing/drawing_color.h>
5. #include <native_drawing/drawing_path.h>
6. #include <native_drawing/drawing_pen.h>

8. static napi_value OnDraw(napi_env env, napi_callback_info info)
9. {
10. size_t argc = 4;
11. napi_value args[4] = { nullptr };
12. napi_get_cb_info(env, info, &argc, args, nullptr, nullptr);

14. int32_t id;
15. napi_get_value_int32(env, args[0], &id);

17. // 获取 Canvas 指针
18. void* temp = nullptr;
19. napi_unwrap(env, args[1], &temp);
20. OH_Drawing_Canvas *canvas = reinterpret_cast<OH_Drawing_Canvas*>(temp);

22. // 获取 Canvas 宽度
23. int32_t width;
24. napi_get_value_int32(env, args[2], &width);

26. // 获取 Canvas 高度
27. int32_t height;
28. napi_get_value_int32(env, args[3], &height);

30. // 传入canvas、height、width等信息至绘制函数中进行自定义绘制
31. auto path = OH_Drawing_PathCreate();
32. OH_Drawing_PathMoveTo(path, width / 4, height / 4);
33. OH_Drawing_PathLineTo(path, width * 3 / 4, height / 4);
34. OH_Drawing_PathLineTo(path, width * 3 / 4, height * 3 / 4);
35. OH_Drawing_PathLineTo(path, width / 4, height * 3 / 4);
36. OH_Drawing_PathLineTo(path, width / 4, height / 4);
37. OH_Drawing_PathClose(path);

39. auto pen = OH_Drawing_PenCreate();
40. OH_Drawing_PenSetWidth(pen, 10);
41. OH_Drawing_PenSetColor(pen, OH_Drawing_ColorSetArgb(0xFF, 0xFF, 0x00, 0x00));
42. OH_Drawing_CanvasAttachPen(canvas, pen);

44. OH_Drawing_CanvasDrawPath(canvas, path);

46. return nullptr;
47. }

49. EXTERN_C_START
50. static napi_value Init(napi_env env, napi_value exports)
51. {
52. napi_property_descriptor desc[] = {
53. { "nativeOnDraw", nullptr, OnDraw, nullptr, nullptr, nullptr, napi_default, nullptr }
54. };
55. napi_define_properties(env, exports, sizeof(desc) / sizeof(desc[0]), desc);
56. return exports;
57. }
58. EXTERN_C_END

60. static napi_module demoModule = {
61. .nm_version =1,
62. .nm_flags = 0,
63. .nm_filename = nullptr,
64. .nm_register_func = Init,
65. .nm_modname = "entry",
66. .nm_priv = ((void*)0),
67. .reserved = { 0 },
68. };

70. extern "C" __attribute__((constructor)) void RegisterEntryModule(void)
71. {
72. napi_module_register(&demoModule);
73. }
```

修改工程中的src/main/cpp/CMakeLists.txt文件，添加如下内容：

```
1. # the minimum version of CMake.
2. cmake_minimum_required(VERSION 3.4.1)
3. project(NapiTest)

5. set(NATIVERENDER_ROOT_PATH ${CMAKE_CURRENT_SOURCE_DIR})

7. include_directories(${NATIVERENDER_ROOT_PATH}
8. ${NATIVERENDER_ROOT_PATH}/include)

10. add_library(entry SHARED native_bridge.cpp)
11. target_link_libraries(entry PUBLIC libace_napi.z.so)
12. target_link_libraries(entry PUBLIC libace_ndk.z.so)
13. target_link_libraries(entry PUBLIC libnative_drawing.so)
```

同时在工程中的src/main/cpp/types/libentry/index.d.ts文件中，添加自定义绘制函数在ArkTs侧的定义，如：

```
1. import { DrawContext } from '@kit.ArkUI';

3. export const nativeOnDraw: (id: number, context: DrawContext, width: number, height: number) => number;
```

### invalidate

PhonePC/2in1TabletTVWearable

invalidate(): void

该方法会触发RenderNode的重新渲染。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. import bridge from "libentry.so"; // 该 so 由开发者通过 NAPI 编写并生成
2. import { RenderNode, FrameNode, NodeController, DrawContext } from '@kit.ArkUI';

4. // 继承RenderNode，实现自定义绘制方法
5. class MyRenderNode extends RenderNode {
6. uiContext: UIContext;

8. constructor(uiContext: UIContext) {
9. super();
10. this.uiContext = uiContext;
11. }

13. draw(context: DrawContext) {
14. // 需要将 context 中的宽度和高度从vp转换为px
15. bridge.nativeOnDraw(0, context, this.uiContext.vp2px(context.size.height), this.uiContext.vp2px(context.size.width));
16. }
17. }

19. // 继承NodeController实现自定义UI控制器
20. class MyNodeController extends NodeController {
21. private rootNode: FrameNode | null = null;
22. newNode: MyRenderNode | null = null;

24. makeNode(uiContext: UIContext): FrameNode | null {
25. this.rootNode = new FrameNode(uiContext);
26. const renderNode = this.rootNode.getRenderNode();
27. if (renderNode === null) {
28. return this.rootNode;
29. }
30. this.newNode = new MyRenderNode(uiContext);
31. this.newNode.size = { width: 100, height: 100 };
32. renderNode.appendChild(this.newNode);
33. return this.rootNode;
34. }
35. }

37. @Entry
38. @Component
39. struct Index {
40. private myNodeController: MyNodeController = new MyNodeController();

42. build() {
43. Column() {
44. Column() {
45. NodeContainer(this.myNodeController)
46. .width('100%')
47. Button('Invalidate')
48. .onClick(() => {
49. // 触发RenderNode的重新渲染
50. this.myNodeController.newNode?.invalidate()
51. })
52. }
53. .width('100%')
54. .height('100%')
55. }
56. .height('100%')
57. }
58. }
```

libentry.so的构建方式见draw方法的示例。

### borderStyle12+

PhonePC/2in1TabletTVWearable

set borderStyle(style: Edges<BorderStyle>)

设置当前RenderNode的边框样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| style | [Edges](js-apis-arkui-graphics.md#edgest12)<[BorderStyle](ts-appendix-enums.md#borderstyle)> | 是 | RenderNode的边框样式。 |

get borderStyle(): Edges<BorderStyle>

获取当前RenderNode的边框样式。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Edges](js-apis-arkui-graphics.md#edgest12)<[BorderStyle](ts-appendix-enums.md#borderstyle)> | RenderNode的边框样式。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = { x: 0, y: 0, width: 150, height: 150 };
5. renderNode.backgroundColor = 0XFF00FF00;
6. renderNode.borderWidth = { left: 8, top: 8, right: 8, bottom: 8 };
7. // 设置renderNode的边框样式
8. renderNode.borderStyle = {
9. left: BorderStyle.Solid,
10. top: BorderStyle.Dotted,
11. right: BorderStyle.Dashed,
12. bottom: BorderStyle.Solid
13. }
14. // 获取renderNode的边框样式
15. const borderStyle = renderNode.borderStyle;

18. // 继承NodeController实现自定义UI控制器
19. class MyNodeController extends NodeController {
20. private rootNode: FrameNode | null = null;

22. makeNode(uiContext: UIContext): FrameNode | null {
23. this.rootNode = new FrameNode(uiContext);

25. const rootRenderNode = this.rootNode.getRenderNode();
26. if (rootRenderNode !== null) {
27. rootRenderNode.appendChild(renderNode);
28. }

30. return this.rootNode;
31. }
32. }

34. @Entry
35. @Component
36. struct Index {
37. private myNodeController: MyNodeController = new MyNodeController();

39. build() {
40. Row() {
41. NodeContainer(this.myNodeController)
42. }
43. }
44. }
```

### borderWidth12+

PhonePC/2in1TabletTVWearable

set borderWidth(width: Edges<number>)

设置当前RenderNode的边框宽度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| width | [Edges](js-apis-arkui-graphics.md#edgest12)<number> | 是 | RenderNode的边框宽度，单位为vp。 |

get borderWidth(): Edges<number>

获取当前RenderNode的边框宽度。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Edges](js-apis-arkui-graphics.md#edgest12)<number> | RenderNode的边框宽度，默认所有边框宽度为0vp。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = { x: 0, y: 0, width: 150, height: 150 };
5. renderNode.backgroundColor = 0XFF00FF00;
6. // 设置renderNode的边框宽度
7. renderNode.borderWidth = { left: 8, top: 8, right: 8, bottom: 8 };
8. // 获取renderNode的边框宽度
9. const borderWidth = renderNode.borderWidth;

12. // 继承NodeController实现自定义UI控制器
13. class MyNodeController extends NodeController {
14. private rootNode: FrameNode | null = null;

16. makeNode(uiContext: UIContext): FrameNode | null {
17. this.rootNode = new FrameNode(uiContext);

19. const rootRenderNode = this.rootNode.getRenderNode();
20. if (rootRenderNode !== null) {
21. rootRenderNode.appendChild(renderNode);
22. }

24. return this.rootNode;
25. }
26. }

28. @Entry
29. @Component
30. struct Index {
31. private myNodeController: MyNodeController = new MyNodeController();

33. build() {
34. Row() {
35. NodeContainer(this.myNodeController)
36. }
37. }
38. }
```

### borderColor12+

PhonePC/2in1TabletTVWearable

set borderColor(color: Edges<number>)

设置当前RenderNode的边框颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| color | [Edges](js-apis-arkui-graphics.md#edgest12)<number> | 是 | RenderNode的边框颜色。 |

get borderColor(): Edges<number>

获取当前RenderNode的边框颜色。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [Edges](js-apis-arkui-graphics.md#edgest12)<number> | RenderNode的边框颜色，默认所有边框颜色为0XFF000000。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = { x: 0, y: 0, width: 150, height: 150 };
5. renderNode.backgroundColor = 0XFF00FF00;
6. renderNode.borderWidth = { left: 8, top: 8, right: 8, bottom: 8 };
7. // 设置renderNode的边框颜色
8. renderNode.borderColor = { left: 0xFF0000FF, top: 0xFF0000FF, right: 0xFF0000FF, bottom: 0xFF0000FF };
9. // 获取renderNode的边框颜色
10. const borderColor = renderNode.borderColor;

13. // 继承NodeController实现自定义UI控制器
14. class MyNodeController extends NodeController {
15. private rootNode: FrameNode | null = null;

17. makeNode(uiContext: UIContext): FrameNode | null {
18. this.rootNode = new FrameNode(uiContext);

20. const rootRenderNode = this.rootNode.getRenderNode();
21. if (rootRenderNode !== null) {
22. rootRenderNode.appendChild(renderNode);
23. }

25. return this.rootNode;
26. }
27. }

29. @Entry
30. @Component
31. struct Index {
32. private myNodeController: MyNodeController = new MyNodeController();

34. build() {
35. Row() {
36. NodeContainer(this.myNodeController)
37. }
38. }
39. }
```

### borderRadius12+

PhonePC/2in1TabletTVWearable

set borderRadius(radius: BorderRadiuses)

设置当前RenderNode的边框圆角。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| radius | [BorderRadiuses](js-apis-arkui-graphics.md#borderradiuses12) | 是 | RenderNode的边框圆角，单位为vp。 |

get borderRadius(): BorderRadiuses

获取当前RenderNode的边框圆角。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [BorderRadiuses](js-apis-arkui-graphics.md#borderradiuses12) | RenderNode的边框圆角，默认所有边框圆角为0vp。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = { x: 0, y: 0, width: 150, height: 150 };
5. renderNode.backgroundColor = 0XFF00FF00;
6. // 设置renderNode的边框圆角
7. renderNode.borderRadius = { topLeft: 32, topRight: 32, bottomLeft: 32, bottomRight: 32 };
8. // 获取renderNode的边框圆角
9. const borderRadius = renderNode.borderRadius;

12. // 继承NodeController实现自定义UI控制器
13. class MyNodeController extends NodeController {
14. private rootNode: FrameNode | null = null;

16. makeNode(uiContext: UIContext): FrameNode | null {
17. this.rootNode = new FrameNode(uiContext);

19. const rootRenderNode = this.rootNode.getRenderNode();
20. if (rootRenderNode !== null) {
21. rootRenderNode.appendChild(renderNode);
22. }

24. return this.rootNode;
25. }
26. }

28. @Entry
29. @Component
30. struct Index {
31. private myNodeController: MyNodeController = new MyNodeController();

33. build() {
34. Row() {
35. NodeContainer(this.myNodeController)
36. }
37. }
38. }
```

### shapeMask12+

PhonePC/2in1TabletTVWearable

set shapeMask(shapeMask: ShapeMask)

设置当前RenderNode的遮罩。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shapeMask | [ShapeMask](js-apis-arkui-graphics.md#shapemask12) | 是 | RenderNode的遮罩。 |

get shapeMask(): ShapeMask

获取当前RenderNode的遮罩。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ShapeMask](js-apis-arkui-graphics.md#shapemask12) | RenderNode的边框遮罩。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, ShapeMask } from '@kit.ArkUI';

3. // 创建遮罩并设置填充颜色、边框颜色、边框宽度
4. const mask = new ShapeMask();
5. mask.setRectShape({ left: 0, right: 150, top: 0, bottom: 150 });
6. mask.fillColor = 0X55FF0000;
7. mask.strokeColor = 0XFFFF0000;
8. mask.strokeWidth = 24;

10. const renderNode = new RenderNode();
11. renderNode.frame = { x: 0, y: 0, width: 150, height: 150 };
12. renderNode.backgroundColor = 0XFF00FF00;
13. // 设置renderNode的遮罩
14. renderNode.shapeMask = mask;
15. // 获取renderNode的遮罩
16. const shapeMask = renderNode.shapeMask;

19. // 继承NodeController实现自定义UI控制器
20. class MyNodeController extends NodeController {
21. private rootNode: FrameNode | null = null;

23. makeNode(uiContext: UIContext): FrameNode | null {
24. this.rootNode = new FrameNode(uiContext);

26. const rootRenderNode = this.rootNode.getRenderNode();
27. if (rootRenderNode !== null) {
28. rootRenderNode.appendChild(renderNode);
29. }

31. return this.rootNode;
32. }
33. }

35. @Entry
36. @Component
37. struct Index {
38. private myNodeController: MyNodeController = new MyNodeController();

40. build() {
41. Row() {
42. NodeContainer(this.myNodeController)
43. }
44. }
45. }
```

### shapeClip12+

PhonePC/2in1TabletTVWearable

set shapeClip(shapeClip: ShapeClip)

设置当前RenderNode的裁剪形状。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| shapeClip | [ShapeClip](js-apis-arkui-graphics.md#shapeclip12) | 是 | RenderNode的裁剪形状。 |

get shapeClip(): ShapeClip

获取当前RenderNode的裁剪形状。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [ShapeClip](js-apis-arkui-graphics.md#shapeclip12) | RenderNode的裁剪形状。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, ShapeClip } from '@kit.ArkUI';

3. // 创建图形裁剪形状并设置路径绘制指令
4. const clip = new ShapeClip();
5. clip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });

7. const renderNode = new RenderNode();
8. renderNode.frame = {
9. x: 0,
10. y: 0,
11. width: 150,
12. height: 150
13. };
14. renderNode.backgroundColor = 0XFF00FF00;
15. // 设置renderNode的裁剪形状
16. renderNode.shapeClip = clip;
17. // 获取renderNode的裁剪形状
18. const shapeClip = renderNode.shapeClip;

20. // 继承NodeController实现自定义UI控制器
21. class MyNodeController extends NodeController {
22. private rootNode: FrameNode | null = null;

24. makeNode(uiContext: UIContext): FrameNode | null {
25. this.rootNode = new FrameNode(uiContext);

27. const rootRenderNode = this.rootNode.getRenderNode();
28. if (rootRenderNode !== null) {
29. rootRenderNode.appendChild(renderNode);
30. }

32. return this.rootNode;
33. }
34. }

36. @Entry
37. @Component
38. struct Index {
39. private myNodeController: MyNodeController = new MyNodeController();

41. build() {
42. Column() {
43. NodeContainer(this.myNodeController)
44. .borderWidth(1)
45. Button("setRectShape")
46. .onClick(() => {
47. shapeClip.setRectShape({
48. left: 0,
49. right: 150,
50. top: 0,
51. bottom: 150
52. });
53. renderNode.shapeClip = shapeClip;
54. })
55. Button("setRoundRectShape")
56. .onClick(() => {
57. shapeClip.setRoundRectShape({
58. rect: {
59. left: 0,
60. top: 0,
61. right: this.getUIContext().vp2px(150),
62. bottom: this.getUIContext().vp2px(150)
63. },
64. corners: {
65. topLeft: { x: 32, y: 32 },
66. topRight: { x: 32, y: 32 },
67. bottomLeft: { x: 32, y: 32 },
68. bottomRight: { x: 32, y: 32 }
69. }
70. });
71. renderNode.shapeClip = shapeClip;
72. })
73. Button("setCircleShape")
74. .onClick(() => {
75. shapeClip.setCircleShape({ centerY: 75, centerX: 75, radius: 75 });
76. renderNode.shapeClip = shapeClip;
77. })
78. Button("setOvalShape")
79. .onClick(() => {
80. shapeClip.setOvalShape({
81. left: 0,
82. right: this.getUIContext().vp2px(150),
83. top: 0,
84. bottom: this.getUIContext().vp2px(100)
85. });
86. renderNode.shapeClip = shapeClip;
87. })
88. Button("setCommandPath")
89. .onClick(() => {
90. shapeClip.setCommandPath({ commands: "M100 0 L0 100 L50 200 L150 200 L200 100 Z" });
91. renderNode.shapeClip = shapeClip;
92. })
93. }
94. }
95. }
```

### dispose12+

PhonePC/2in1TabletTVWearable

dispose(): void

立即释放当前RenderNode。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = { x: 0, y: 100, width: 100, height: 100 };
5. renderNode.backgroundColor = 0xffff0000;

7. // 继承NodeController实现自定义UI控制器
8. class MyNodeController extends NodeController {
9. private rootNode: FrameNode | null = null;

11. makeNode(uiContext: UIContext): FrameNode | null {
12. this.rootNode = new FrameNode(uiContext);

14. const rootRenderNode = this.rootNode!.getRenderNode();
15. if (rootRenderNode !== null) {
16. rootRenderNode.size = { width: 200, height: 200 };
17. rootRenderNode.backgroundColor = 0xff00ff00;
18. rootRenderNode.appendChild(renderNode);
19. }

21. return this.rootNode;
22. }

24. disposeRenderNode() {
25. const rootRenderNode = this.rootNode!.getRenderNode();
26. // 释放当前renderNode前，移除该renderNode的所有子节点
27. if (rootRenderNode !== null) {
28. rootRenderNode.removeChild(renderNode);
29. }
30. renderNode.dispose();
31. }
32. }

34. @Entry
35. @Component
36. struct Index {
37. private myNodeController: MyNodeController = new MyNodeController();

39. build() {
40. Column({ space: 4 }) {
41. NodeContainer(this.myNodeController)
42. Button('RenderNode dispose')
43. .onClick(() => {
44. this.myNodeController.disposeRenderNode();
45. })
46. .width('100%')
47. }
48. }
49. }
```

### markNodeGroup12+

PhonePC/2in1TabletTVWearable

set markNodeGroup(isNodeGroup: boolean)

标记是否优先绘制节点及其子节点。若设置为true，则透明度等属性将在节点绘制完毕后再进行合成。设置效果如下：

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/XgZ2Zt9kTTe2jBqR5WcuFQ/zh-cn_image_0000002552799808.png?HW-CC-KV=V1&HW-CC-Date=20260428T000035Z&HW-CC-Expire=86400&HW-CC-Sign=7D078706B9FF30952909BDC5748C5A5C86C803F55F4E466F901A49E898ACB056)

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| isNodeGroup | boolean | 是 | 设置是否优先绘制节点及其子节点。  true表示优先绘制节点及其子节点，false表示不是优先绘制节点及其子节点。 |

get markNodeGroup(): boolean

获取当前节点是否标记了优先绘制。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 当前节点是否标记了优先绘制。  true表示当前节点标记了优先绘制，false表示当前节点没有标记优先绘制。  默认值：false |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, DrawContext } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';

4. // 继承RenderNode，实现自定义绘制方法
5. class MyRenderNode extends RenderNode {
6. draw(context: DrawContext) {
7. const canvas = context.canvas;
8. const brush = new drawing.Brush();
9. brush.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
10. canvas.attachBrush(brush);
11. canvas.drawRect({ left: 0, right: 200, top: 0, bottom: 200 });
12. canvas.detachBrush();

14. brush.setColor({ alpha: 255, red: 0, green: 255, blue: 0 });
15. canvas.attachBrush(brush);
16. canvas.drawRect({ left: 100, right: 300, top: 100, bottom: 300 });
17. canvas.detachBrush();
18. }
19. }

21. const renderNode = new MyRenderNode();
22. renderNode.frame = { x: 100, y: 100, width: 200, height: 200 };
23. renderNode.backgroundColor = 0xff0000ff;
24. // 标记当前renderNode为优先绘制
25. renderNode.markNodeGroup = true;
26. renderNode.opacity = 0.5;

28. const isNodeGroup = renderNode.markNodeGroup;

30. // 继承NodeController实现自定义UI控制器
31. class MyNodeController extends NodeController {
32. private rootNode: FrameNode | null = null;

34. makeNode(uiContext: UIContext): FrameNode | null {
35. this.rootNode = new FrameNode(uiContext);

37. const rootRenderNode = this.rootNode.getRenderNode();
38. if (rootRenderNode !== null) {
39. rootRenderNode.appendChild(renderNode);
40. }

42. return this.rootNode;
43. }
44. }

46. @Entry
47. @Component
48. struct Index {
49. private myNodeController: MyNodeController = new MyNodeController();

51. build() {
52. Row() {
53. NodeContainer(this.myNodeController)
54. }
55. }
56. }
```

### lengthMetricsUnit12+

PhonePC/2in1TabletTVWearable

set lengthMetricsUnit(unit: LengthMetricsUnit)

设置RenderNode各个属性使用的单位。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| unit | [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 是 | 设置RenderNode各个属性使用的单位。 |

get lengthMetricsUnit(): LengthMetricsUnit

获取RenderNode各个属性使用的单位。

**元服务API：** 从API version 12开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| [LengthMetricsUnit](js-apis-arkui-graphics.md#lengthmetricsunit12) | 获取RenderNode各个属性使用的单位，默认值为LengthMetricsUnit.DEFAULT。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController, DrawContext } from '@kit.ArkUI';
2. import { drawing } from '@kit.ArkGraphics2D';
3. import { LengthMetricsUnit } from '@kit.ArkUI';

5. // 继承RenderNode，设置RenderNode各个属性使用的单位
6. class BaseRenderNode extends RenderNode {
7. constructor() {
8. super();
9. this.lengthMetricsUnit = LengthMetricsUnit.PX;
10. }
11. }

13. // 继承BaseRenderNode，实现自定义绘制方法
14. class MyRenderNode extends BaseRenderNode {
15. draw(context: DrawContext) {
16. const canvas = context.canvas;
17. const brush = new drawing.Brush();
18. brush.setColor({ alpha: 255, red: 255, green: 0, blue: 0 });
19. canvas.attachBrush(brush);
20. canvas.drawRect({ left: 0, right: 200, top: 0, bottom: 200 });
21. canvas.detachBrush();
22. }
23. }

25. const renderNode = new MyRenderNode();
26. renderNode.frame = { x: 100, y: 100, width: 200, height: 200 };
27. renderNode.backgroundColor = 0xff0000ff;
28. renderNode.rotation = { x: 0, y: 0, z: 45 };

30. // 继承NodeController实现自定义UI控制器
31. class MyNodeController extends NodeController {
32. private rootNode: FrameNode | null = null;

34. makeNode(uiContext: UIContext): FrameNode | null {
35. this.rootNode = new FrameNode(uiContext);
36. const rootRenderNode = this.rootNode.getRenderNode();
37. if (rootRenderNode !== null) {
38. rootRenderNode.appendChild(renderNode);
39. }
40. return this.rootNode;
41. }
42. }

44. @Entry
45. @Component
46. struct Index {
47. private myNodeController: MyNodeController = new MyNodeController();

49. build() {
50. Row() {
51. NodeContainer(this.myNodeController)
52. }
53. }
54. }
```

### isDisposed20+

PhonePC/2in1TabletTVWearable

isDisposed(): boolean

查询当前RenderNode对象是否已解除与后端实体节点的引用关系。前端节点均绑定有相应的后端实体节点，当节点调用dispose接口解除绑定后，再次调用接口可能会出现crash、返回默认值的情况。由于业务需求，可能存在节点在dispose后仍被调用接口的情况。为此，提供此接口以供开发者在操作节点前检查其有效性，避免潜在风险。

**元服务API：** 从API version 20开始，该接口支持在元服务中使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**返回值：**

| 类型 | 说明 |
| --- | --- |
| boolean | 后端实体节点是否解除引用。true为节点已与后端实体节点解除引用，false为节点未与后端实体节点解除引用。 |

**示例：**

```
1. import { RenderNode, FrameNode, NodeController } from '@kit.ArkUI';

3. const renderNode = new RenderNode();
4. renderNode.frame = { x: 100, y: 100, width: 100, height: 100 };
5. renderNode.backgroundColor = 0xff2787d9;

7. // 继承NodeController实现自定义UI控制器
8. class MyNodeController extends NodeController {
9. private rootNode: FrameNode | null = null;

11. makeNode(uiContext: UIContext): FrameNode | null {
12. this.rootNode = new FrameNode(uiContext);

14. const rootRenderNode = this.rootNode!.getRenderNode();
15. if (rootRenderNode !== null) {
16. rootRenderNode.size = { width: 300, height: 300 };
17. rootRenderNode.backgroundColor = 0xffd5d5d5;
18. rootRenderNode.appendChild(renderNode);
19. }

21. return this.rootNode;
22. }

24. disposeRenderNode() {
25. const rootRenderNode = this.rootNode!.getRenderNode();
26. if (rootRenderNode !== null) {
27. rootRenderNode.removeChild(renderNode);
28. }
29. renderNode.dispose();
30. }

32. isDisposed() : string {
33. if (renderNode !== null) {
34. // 检查当前renderNode是否已经与后端节点解除引用
35. if (renderNode.isDisposed()) {
36. return 'renderNode isDisposed is true';
37. }
38. else {
39. return 'renderNode isDisposed is false';
40. }
41. }
42. return 'renderNode is null';
43. }
44. }

46. @Entry
47. @Component
48. struct Index {
49. @State text: string = ''
50. private myNodeController: MyNodeController = new MyNodeController();

52. build() {
53. Column({ space: 4 }) {
54. NodeContainer(this.myNodeController)
55. Button('RenderNode dispose')
56. .onClick(() => {
57. this.myNodeController.disposeRenderNode();
58. this.text = '';
59. })
60. .width(200)
61. .height(50)
62. Button('RenderNode isDisposed')
63. .onClick(() => {
64. this.text = this.myNodeController.isDisposed();
65. })
66. .width(200)
67. .height(50)
68. Text(this.text)
69. .fontSize(25)
70. }
71. .width('100%')
72. .height('100%')
73. }
74. }
```

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/k_TucOFGReOTfjCwB8wn6g/zh-cn_image_0000002583439503.gif?HW-CC-KV=V1&HW-CC-Date=20260428T000035Z&HW-CC-Expire=86400&HW-CC-Sign=87E2975C357F75603FD04226551CC9750D5A74BBF6EDA10B97D0DEEA4A68B3CE)
