---
url: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/changelogs-targeting-api12-b060
title: 针对API 12应用的变更
breadcrumb: 版本说明 > 历史版本 > HarmonyOS 5.0.0(12) > OS平台能力 > 接口行为变更说明 > HarmonyOS NEXT Developer Beta5引入的接口行为变更 > 针对API 12应用的变更
category: harmonyos-releases
scraped_at: 2026-04-28T07:36:12+08:00
doc_updated_at: 2026-01-21
content_hash: sha256:7367fdbbb10a7abf2610bd7cbe309f89ee2cbf7817558feadcc8e024528fd8d1
---

## ArkData

### RelationalStore execute，executeSync接口执行不合法SQL语句错误码变更

**变更原因**

提升该场景接口错误码准确性，提升开发者问题定位效率。

**变更影响**

此变更涉及应用适配。

变更前：执行不合法的SQL语句，报错的error对象code值为14800000。

变更后：执行不合法的SQL语句，报错的error对象code值为14800021。

**起始API Level**

12

**变更的接口/组件**

| 场景 | 变更前 | 变更后 |
| --- | --- | --- |
| execute接口执行不合法SQL语句 | 错误码为14800000 | 错误码为14800021 |
| executeSync接口执行不合法SQL语句 | 错误码为14800000 | 错误码为14800021 |

**适配指导**

在调用execute，executeSync接口执行SQL语句场景，如使用14800000错误码作为判定条件，需要将对应判定条件错误码修改为14800021。

修改前execute接口执行SQL语句报错错误码：

```
1. try {
2. await rdbStore.execute("COMMIT");
3. } catch (err) {
4. if (err.code === 14800000) {
5. console.log(`execute failed, code: ${err.code}`);
6. }
7. }
```

修改后execute接口执行SQL语句报错错误码：

```
1. try {
2. await rdbStore.execute("COMMIT");
3. } catch (err) {
4. if (err.code === 14800021) {
5. console.log(`execute failed, code: ${err.code}`);
6. }
7. }
```

## ArkTS

### xml.XmlPullParser.parse接口解析实体引用事件的行为变更

**变更原因**

parse接口解析xml时，会把实体引用事件识别为文本事件，用户在tokenValueCallbackFunction中指定的回调函数无法得到实体引用事件的解析结果，解析内容会被整合在文本事件中，不符合设计预期，需要修改。

**变更影响**

此变更涉及应用适配。

变更前：实体引用事件的xml信息被解析为文本事件，用户无法在回调函数中针对实体引用事件进行操作，也无法仅通过xml解析结果判断实体引用事件是否存在。

变更后：在API12及更高版本中，实体引用事件的xml信息被解析为实体引用事件，用户可以在回调函数中针对实体引用事件进行操作，也能仅通过xml解析结果判断实体引用事件是否存在。

**起始API Level**

12

**变更的接口/组件**

xml.XmlPullParser.parse

**适配指导**

如果xml原本就不会涉及实体引用事件，则无需适配，没有影响。

如果xml涉及实体引用事件，以下面的例子说明变更前后差异，strXml存放待解析的xml，func为开发者自行准备的tokenValueCallbackFunction型回调函数，parse接口解析后得到的每个事件都会触发一次回调，并传入事件类型和对应的xml解析结果。

```
1. let strXml = '<?xml version="1.0" encoding="utf-8"?>\n' +
2. '<note>&amp;happy&amp;</note>';    // 此处第一个实体引用“&amp;”属于实体引用事件，而第二个实体引用“&amp;”由于紧随文本“happy”，“happy&amp;”作为整体属于文本事件。
3. let textEncoder = new util.TextEncoder();
4. let arrbuffer = textEncoder.encodeInto(strXml);
5. let that = new xml.XmlPullParser(arrbuffer.buffer as object as ArrayBuffer, 'UTF-8');
6. let str = "";
7. function func(key: xml.EventType, value: xml.ParseInfo){
8. str += 'key:' + key +' value:' + value.getText() + '  ';
9. return true;
10. }
11. let options: xml.ParseOptions = {supportDoctype:true, ignoreNameSpace:true, tokenValueCallbackFunction:func}
12. that.parse(options);
13. console.log(str);
```

API 11及之前版本：

```
1. &amp;happy&amp;解析结果为：
2. key为4（文本事件），value为&happy&
```

API 12起：

```
1. &amp;happy&amp;解析结果为2个：
2. key为9（实体引用事件），value为&
3. key为4（文本事件），value为happy&
```

开发者如果需要使用实体引用事件，需要至少使用API12，并在xml中严格遵从实体引用事件的格式，不在实体引用前加普通文本形成文本事件。

开发者如果不需要使用实体引用事件，在xml中实体引用前面加普通文本形成文本事件就行，或者自行适配回调函数。

实体引用事件说明：

目前仅支持在XML中5个预定义的实体引用对应的实体引用事件：

```
1. &lt;    <  less than
2. &gt;    >  greater than
3. &amp;   &  ampersand
4. &apos;  '  apostrophe
5. &quot;  "  quotation mark
```

另外，实体引用前存在文本时会被一起视为文本事件，如：

```
1. <note>happy&lt;&gt;</note> 依次为：启动标签事件；文本事件；结束标签事件。
2. <note>&lt;&gt;happy</note> 依次为：启动标签事件；实体引用事件；实体引用事件；文本事件；结束标签事件。
```

## ArkUI

### FrameNode的isModifiable值为false时，无法通过addComponentContent挂载节点

**变更原因**

addComponentContent接口用于实现ComponentContent对象的挂载，但是只有isModifiable为true的FrameNode对象允许更改其子节点，当前实现与设计不一致。

**变更影响**

此变更涉及应用适配。

变更前：addComponentContent可以向isModifiable为false的FrameNode对象挂载子节点。

变更后：addComponentContent无法向isModifiable为false的FrameNode对象挂载子节点，调用addComponent接口后会抛出异常导致子节点挂载失败，并出现白屏，可以通过try catch捕获异常解决。

| 变更前 | 变更后 |
| --- | --- |
|  |  |

**起始API Level**

12

**变更的接口/组件**

FrameNode的addComponentContent接口。

**适配指导**

开发者在使用addComponentContent前需要判断父节点的isModifiable是否为true，不支持isModifiable为false的FrameNode节点使用addComponentContent新增子节点。需要在声明式组件中动态添加内容时，可以通过占位节点[NodeContainer](../harmonyos-references-V5/ts-basic-components-nodecontainer-V5.md)、[ContentSlot](../harmonyos-guides-V5/arkts-rendering-control-contentslot-V5.md)进行操作。

```
1. import { ComponentContent, NodeContent, typeNode } from "@kit.ArkUI"

3. interface ParamsInterface {
4. text: string;
5. }

7. @Builder
8. function buildText(params: ParamsInterface) {
9. Column() {
10. Text(params.text)
11. .fontSize(20)
12. .fontWeight(FontWeight.Bold)
13. .margin({ bottom: 36 })
14. }
15. }

17. @Entry
18. @Component
19. struct Index {
20. @State message: string = "hello"
21. private content: NodeContent = new NodeContent();

23. build() {
24. Row() {
25. Column() {
26. Button('addComponentContent')
27. .onClick(() => {
28. let column = typeNode.createNode(this.getUIContext(), "Column");
29. column.initialize();
30. if (column.isModifiable()) {
31. column.addComponentContent(new ComponentContent<ParamsInterface>(this.getUIContext(),
32. wrapBuilder<[ParamsInterface]>(buildText), { text: 'Colum Text isModifiable true' }))
33. }
34. this.content.addFrameNode(column)
35. let column1 = this.getUIContext().getFrameNodeById('column1');
36. if (!column1?.isModifiable()) {
37. try {
38. column1?.addComponentContent(new ComponentContent<ParamsInterface>(this.getUIContext(),
39. wrapBuilder<[ParamsInterface]>(buildText), { text: 'Colum1 Text isModifiable false' }))
40. } catch (e) {
41. console.error('addComponentContent fail, err: ' + e);
42. }
43. }
44. })
45. ContentSlot(this.content)
46. }
47. .id('column1')
48. .width('100%')
49. .height('100%')
50. }
51. .height('100%')
52. }
53. }
```

## Device Security Kit

### 可信应用服务接口增加端云认证服务开通检测

**变更原因**

为规范安全摄像头和安全地理位置的使用场景，使用可信应用服务接口前需要通过白名单审核，审核通过后方可开通可信应用服务。

**变更影响**

此变更涉及应用适配。

变更前：开发者不需要开通可信应用服务就可以正常使用接口。

变更后：开发者需要开通可信应用服务才可以正常使用接口，否则调用接口会抛出异常，已上架的应用需要开通服务后重新上架。

接口抛出异常情况如下：

| 接口名 | 异常错误码 |
| --- | --- |
| createAttestKey | 1011500006 |
| destroyAttestKey | 1011500006 |
| initializeAttestContext | 1011500005或1011500006 |
| finalizeAttestContext | 1011500006 |

**起始API Level**

12

**变更的接口/组件**

SystemCapability.Security.TrustedAppService.Core操作证明密钥和证明会话相关接口。

**适配指导**

开发者需要申请加入可信应用服务开通白名单，等待审核通过后，在[AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html)上开通可信应用服务，详细步骤可参考[指导文档](../harmonyos-guides-V5/devicesecurity-deviceverify-activateservice-V5.md)。
